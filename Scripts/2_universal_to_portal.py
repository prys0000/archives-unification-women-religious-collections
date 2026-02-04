#!/usr/bin/env python3
"""
universal_to_portal.py

Universal mapper:
- Input: .xlsx / .csv / SpreadsheetML .xml (EAD->Excel export)
- Output: portal_upload.xlsx with columns defined by portal.xlsx ("Portal Label")
- Mapping: map_json file controlling which source columns feed which portal columns
- Enrichment: dates (including dates embedded in title), name extraction, controlled vocab matching

Key upgrades in this rewrite:
✅ Fixes missing variables (TITLE_DATE1/2/YEAR were referenced but not defined)
✅ Fixes function order (parse_monthname_date used before defined)
✅ Adds robust date parsing: ISO, year, year ranges, month-name dates, title-embedded dates, date ranges
✅ Adds "source_any_of" fallback (Description vs Scope and Contents vs Summary, etc.)
✅ Removes stray / duplicated code that was outside functions (the raw_date block at bottom)
✅ Fixes indentation issues inside enrich_output
✅ Keeps behavior: if a mapped column doesn’t exist -> blanks
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
from lxml import etree


# =========================
# SpreadsheetML XML support
# =========================
SS_NS = "urn:schemas-microsoft-com:office:spreadsheet"
NS = {"ss": SS_NS}


def read_spreadsheetml_worksheet(xml_path: Path, worksheet_name: str) -> pd.DataFrame:
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    ws = None
    for w in root.findall(".//ss:Worksheet", namespaces=NS):
        name = w.get(f"{{{SS_NS}}}Name")
        if name == worksheet_name:
            ws = w
            break

    if ws is None:
        available = [w.get(f"{{{SS_NS}}}Name") for w in root.findall(".//ss:Worksheet", namespaces=NS)]
        raise ValueError(f"Worksheet '{worksheet_name}' not found. Available: {available}")

    table = ws.find(".//ss:Table", namespaces=NS)
    if table is None:
        raise ValueError(f"No ss:Table found in worksheet '{worksheet_name}'")

    rows: List[List[str]] = []
    for row in table.findall("ss:Row", namespaces=NS):
        out: List[str] = []
        col_idx = 1
        for cell in row.findall("ss:Cell", namespaces=NS):
            idx = cell.get(f"{{{SS_NS}}}Index")
            if idx is not None:
                idx_i = int(idx)
                while col_idx < idx_i:
                    out.append("")
                    col_idx += 1

            data = cell.find("ss:Data", namespaces=NS)
            val = ""
            if data is not None and data.text is not None:
                val = str(data.text)
            out.append(val)
            col_idx += 1

        rows.append(out)

    if not rows:
        return pd.DataFrame()

    maxlen = max(len(r) for r in rows)
    rows = [r + [""] * (maxlen - len(r)) for r in rows]

    header = rows[0]
    data = rows[1:]
    return pd.DataFrame(data, columns=header).fillna("")


# =========================
# Load source input (xlsx/csv/xml)
# =========================
def load_input_table(input_path: Path, sheet: Optional[str], xml_sheet: str) -> pd.DataFrame:
    ext = input_path.suffix.lower()

    if ext == ".xml":
        return read_spreadsheetml_worksheet(input_path, xml_sheet)

    if ext in [".xlsx", ".xlsm", ".xls"]:
        return pd.read_excel(input_path, sheet_name=sheet or 0, dtype=str).fillna("")

    if ext == ".csv":
        return pd.read_csv(input_path, dtype=str).fillna("")

    raise ValueError(f"Unsupported input type: {ext}. Use .xlsx, .csv, or SpreadsheetML .xml")


# =========================
# Portal schema (Portal Label list)
# =========================
def load_portal_labels(portal_xlsx: Path, portal_sheet: str) -> List[str]:
    df = pd.read_excel(portal_xlsx, sheet_name=portal_sheet, dtype=str).fillna("")
    if "Portal Label" not in df.columns:
        raise ValueError("portal.xlsx must contain a column named 'Portal Label'.")
    return [str(x).strip() for x in df["Portal Label"].tolist() if str(x).strip()]


# =========================
# Normalization / transforms
# =========================
def t_strip(v: Any) -> str:
    return ("" if v is None else str(v)).strip()


def t_collapse_ws(v: Any) -> str:
    s = "" if v is None else str(v)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\s*\n\s*", "\n", s)
    return s.strip()


def t_norm_semicolons(v: Any) -> str:
    s = t_strip(v)
    if not s:
        return ""
    s = re.sub(r"\s*;\s*", "; ", s)
    s = re.sub(r"(; )+", "; ", s)
    s = re.sub(r";\s*$", "", s)
    return s


def t_dedupe_semicolon_list(v: Any) -> str:
    s = t_norm_semicolons(v)
    if not s:
        return ""
    parts = [p.strip() for p in s.split(";") if p.strip()]
    seen = set()
    out = []
    for p in parts:
        k = p.lower()
        if k not in seen:
            out.append(p)
            seen.add(k)
    return "; ".join(out)


TRANSFORMS = {
    "strip": t_strip,
    "collapse_ws": t_collapse_ws,
    "norm_semicolons": t_norm_semicolons,
    "dedupe_semicolon_list": t_dedupe_semicolon_list,
}


# =========================
# Date parsing (ISO + month-name + ranges + title embedded)
# =========================
MONTH_MAP = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}
MONTHS = r"(January|February|March|April|May|June|July|August|September|October|November|December)"

# Basic formats
DATE_YYYY = re.compile(r"^\s*(\d{4})\s*$")
DATE_RANGE_YYYY = re.compile(r"^\s*(\d{4})\s*[-–]\s*(\d{4})\s*$")
DATE_ISO = re.compile(r"^\s*(\d{4})-(\d{2})-(\d{2})\s*$")
DATE_ISO_DT = re.compile(r"^\s*(\d{4})-(\d{2})-(\d{2})\s+\d{2}:\d{2}:\d{2}\s*$")

# Month name formats
DATE_MON_D_Y = re.compile(rf"\b{MONTHS}\s+(\d{{1,2}}),\s*(\d{{4}})\b", re.IGNORECASE)  # May 3, 1964
DATE_D_MON_Y = re.compile(rf"\b(\d{{1,2}})\s+{MONTHS}\s+(\d{{4}})\b", re.IGNORECASE)  # 3 May 1964
DATE_MON_Y = re.compile(rf"\b{MONTHS}\s+(\d{{4}})\b", re.IGNORECASE)                  # May 1964

# For extracting date-like strings from title/notes
TITLE_DATE1 = re.compile(rf"\b{MONTHS}\s+\d{{1,2}},\s+\d{{4}}\b", re.IGNORECASE)      # May 3, 1964
TITLE_DATE2 = re.compile(rf"\b\d{{1,2}}\s+{MONTHS}\s+\d{{4}}\b", re.IGNORECASE)      # 3 May 1964
TITLE_YEAR = re.compile(r"\b(18\d{2}|19\d{2}|20\d{2})\b")


def to_iso_date(y: int, m: int, d: int) -> str:
    return datetime(y, m, d).strftime("%Y-%m-%d")


def parse_monthname_date(s: str) -> str:
    """
    Returns ISO date (YYYY-MM-DD) if it finds:
      - May 3, 1964
      - 3 May 1964
    Else "".
    """
    s = t_strip(s)
    if not s:
        return ""

    m = DATE_MON_D_Y.search(s)
    if m:
        mon = MONTH_MAP[m.group(1).lower()]
        day = int(m.group(2))
        year = int(m.group(3))
        return to_iso_date(year, mon, day)

    m = DATE_D_MON_Y.search(s)
    if m:
        day = int(m.group(1))
        mon = MONTH_MAP[m.group(2).lower()]
        year = int(m.group(3))
        return to_iso_date(year, mon, day)

    return ""


def parse_month_year_span(s: str) -> Tuple[str, str]:
    """
    If matches 'May 1964', returns (begin_iso, end_iso) for that month.
    """
    m = DATE_MON_Y.search(s)
    if not m:
        return "", ""

    mon = MONTH_MAP[m.group(1).lower()]
    year = int(m.group(2))
    begin = to_iso_date(year, mon, 1)

    if mon == 12:
        end = to_iso_date(year, 12, 31)
    else:
        next_month = datetime(year, mon + 1, 1)
        end = (next_month - pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    return begin, end


def extract_date_from_text(text: str) -> str:
    """
    Returns a date-like display string from text if found:
    - 'May 3, 1964'
    - '3 May 1964'
    - else the first 4-digit year
    """
    s = t_strip(text)
    if not s:
        return ""

    m = TITLE_DATE1.search(s)
    if m:
        return m.group(0)

    m = TITLE_DATE2.search(s)
    if m:
        return m.group(0)

    m = TITLE_YEAR.search(s)
    if m:
        return m.group(1)

    return ""


def parse_dates_cell(raw: str) -> Tuple[str, str, str]:
    """
    Returns: (date_begin, date_end, date_display)
    Supports:
      - YYYY
      - YYYY-YYYY
      - YYYY-MM-DD
      - YYYY-MM-DD 00:00:00
      - Month-name dates (May 3, 1964 / 3 May 1964)
      - Month year (May 1964) -> month span
      - Simple ranges: 'A - B' or 'A–B' or 'A—B' (best effort)
    """
    s = t_strip(raw)
    if not s:
        return "", "", ""

    # Range split (best effort)
    # We split on the first dash-like separator between two date-ish chunks.
    m_range = re.split(r"\s*[-–—]\s*", s, maxsplit=1)
    if len(m_range) == 2 and m_range[0] and m_range[1]:
        b1, e1, d1 = parse_dates_cell(m_range[0])
        b2, e2, d2 = parse_dates_cell(m_range[1])
        begin = b1 or b2
        end = e2 or e1
        display = f"{d1 or m_range[0]}-{d2 or m_range[1]}"
        # Only accept as a "range parse" if we got at least one side with something
        if begin or end:
            return begin, end, display

    # Excel-ish datetime
    m = DATE_ISO_DT.match(s)
    if m:
        iso = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        return iso, iso, iso

    # ISO date
    m = DATE_ISO.match(s)
    if m:
        iso = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        return iso, iso, iso

    # Year range
    m = DATE_RANGE_YYYY.match(s)
    if m:
        y1, y2 = m.group(1), m.group(2)
        return f"{y1}-01-01", f"{y2}-12-31", f"{y1}-{y2}"

    # Single year
    m = DATE_YYYY.match(s)
    if m:
        y = m.group(1)
        return f"{y}-01-01", f"{y}-12-31", y

    # Month-name full date -> ISO
    iso = parse_monthname_date(s)
    if iso:
        return iso, iso, s

    # Month YYYY -> month span
    b, e = parse_month_year_span(s)
    if b and e:
        return b, e, s

    # Fallback: keep display only
    return "", "", s


# =========================
# Controlled vocab loading + matching
# =========================
def build_vocab_index(
    rows: pd.DataFrame,
    term_col: str,
    variants_col: Optional[str],
    uri_col: Optional[str]
) -> Dict[str, Dict[str, str]]:
    """
    Creates a phrase index:
      key: normalized phrase (lower, single spaces)
      value: { "term": authorized_term, "uri": uri_or_blank }
    Includes authorized term itself + variants (split on ; or ,)
    """
    idx: Dict[str, Dict[str, str]] = {}

    def norm_phrase(p: str) -> str:
        p = (p or "").strip().lower()
        p = re.sub(r"\s+", " ", p)
        return p

    for _, r in rows.iterrows():
        term = t_strip(r.get(term_col, ""))
        if not term:
            continue
        uri = t_strip(r.get(uri_col, "")) if uri_col else ""

        phrases = [term]
        if variants_col:
            v = t_strip(r.get(variants_col, ""))
            if v:
                parts = re.split(r"\s*;\s*", v) if ";" in v else re.split(r"\s*,\s*", v)
                phrases.extend([p for p in parts if p.strip()])

        for p in phrases:
            k = norm_phrase(p)
            if not k:
                continue
            if k not in idx:
                idx[k] = {"term": term, "uri": uri}

    return idx


def match_vocab(text: str, vocab_index: Dict[str, Dict[str, str]]) -> Tuple[str, str]:
    """
    Returns (matched_terms, matched_uris) as semicolon lists.
    Simple phrase matching: phrase occurs in lowercase text.
    """
    s = (text or "").lower()
    if not s:
        return "", ""

    hits_terms: List[str] = []
    hits_uris: List[str] = []
    seen = set()

    phrases = sorted(vocab_index.keys(), key=len, reverse=True)
    for ph in phrases:
        if ph in s:
            term = vocab_index[ph]["term"]
            uri = vocab_index[ph].get("uri", "")
            key = term.lower()
            if key not in seen:
                hits_terms.append(term)
                if uri:
                    hits_uris.append(uri)
                seen.add(key)

    return "; ".join(hits_terms), "; ".join(hits_uris)


# =========================
# Name extraction (heuristic, no installs)
# =========================
SISTER_PAT = re.compile(r"\b(?:Sister|Sr\.?|Mother)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\b")
PROPER_NAME_PAT = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b")

STOP_PROPER = {
    "Sisters Of", "Sisters Of St", "Sisters Of Saint", "Sisters Of The",
    "Holy Father", "Roman Catholic", "United States", "St Casimir", "St. Casimir"
}


def extract_names(text: str) -> str:
    s = t_collapse_ws(text)
    if not s:
        return ""

    hits: List[str] = []
    seen = set()

    for m in SISTER_PAT.finditer(s):
        nm = m.group(1).strip()
        key = nm.lower()
        if key not in seen:
            hits.append(nm)
            seen.add(key)

    for m in PROPER_NAME_PAT.finditer(s):
        nm = m.group(1).strip()
        if nm in STOP_PROPER:
            continue
        if nm.lower().startswith("series ") or nm.lower().startswith("box "):
            continue
        if len(nm.split()) < 2:
            continue
        key = nm.lower()
        if key not in seen:
            hits.append(nm)
            seen.add(key)

    return "; ".join(hits)


# =========================
# Draft mapping creation (optional)
# =========================
def norm_key(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[\s\-_]+", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def best_match(target: str, candidates: List[str]) -> Tuple[str, float]:
    t = norm_key(target)
    t_tokens = set(t.split())
    if not t_tokens:
        return ("", 0.0)

    best = ""
    best_score = 0.0
    for c in candidates:
        c_norm = norm_key(c)
        c_tokens = set(c_norm.split())
        if not c_tokens:
            continue
        inter = len(t_tokens & c_tokens)
        union = len(t_tokens | c_tokens)
        score = inter / union if union else 0.0
        if score > best_score:
            best_score = score
            best = c
    return best, best_score


def make_mapping_file(portal_labels: List[str], source_cols: List[str], out_map: Path):
    """
    Creates a draft mapping with best-guess column matches.
    You should manually edit for multi-source fallbacks, especially for Description fields.
    """
    mapping = {
        "input_sheet": None,
        "xml_sheet": "ContainerList",
        "constants": {},
        "portal_rules": {},
        "enrich": {
            "date_source_any_of": ["Dates", "Date", "date", "dates"],
            "title_source_any_of": ["title", "Title", "Item Title"],
            "text_cols_for_enrichment": [
                "title", "Title",
                "Description", "Scope and Contents", "Scope & Contents", "Summary", "Abstract", "Notes",
                "Key words/Subjects", "Subjects"
            ],
            "append_enrichment_cols": True
        }
    }

    for label in portal_labels:
        guess, score = best_match(label, source_cols)

        rule: Dict[str, Any] = {"source": "", "transforms": []}
        if score >= 0.35:
            rule["source"] = guess

        if re.search(r"(title|abstract|description|scope|note|summary)", norm_key(label)):
            rule["transforms"] = ["strip", "collapse_ws"]
        elif re.search(r"(subject|keyword)", norm_key(label)):
            rule["transforms"] = ["strip", "dedupe_semicolon_list"]
        else:
            rule["transforms"] = ["strip"]

        mapping["portal_rules"][label] = rule

    out_map.write_text(json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")


# =========================
# Apply rules + enrichment
# =========================
def first_existing_col(source_df: pd.DataFrame, candidates: List[str]) -> str:
    for c in candidates:
        c = t_strip(c)
        if c and c in source_df.columns:
            return c
    return ""


def apply_rules(source_df: pd.DataFrame, portal_labels: List[str], rules: Dict, constants: Dict) -> pd.DataFrame:
    out = pd.DataFrame({lab: [""] * len(source_df) for lab in portal_labels})

    for lab in portal_labels:
        rule = rules.get(lab, {}) or {}

        src = t_strip(rule.get("source", ""))
        src_any = rule.get("source_any_of", []) or []
        if (not src) and src_any:
            src = first_existing_col(source_df, src_any)

        if src == "__CONST__":
            out[lab] = [str(constants.get(lab, ""))] * len(source_df)
        else:
            if src and src in source_df.columns:
                out[lab] = source_df[src].astype(str).fillna("")
            else:
                out[lab] = [""] * len(source_df)

        tfms = rule.get("transforms", []) or []
        for tname in tfms:
            tname = t_strip(tname)
            if not tname:
                continue
            if tname not in TRANSFORMS:
                raise ValueError(f"Unknown transform '{tname}' in mapping for '{lab}'")
            out[lab] = out[lab].map(TRANSFORMS[tname])

    return out.fillna("")


def load_controlled_vocabs(vocab_dir: Path) -> Dict[str, Dict[str, Dict[str, str]]]:
    """
    Loads known controlled vocab workbooks if present in vocab_dir.
    Looks for:
      - catholicsubjects.xlsx
      - vocations.xlsx
    """
    vocabs: Dict[str, Dict[str, Dict[str, str]]] = {}

    cs_path = vocab_dir / "catholicsubjects.xlsx"
    if cs_path.exists():
        cs = pd.read_excel(cs_path, sheet_name=0, dtype=str).fillna("")
        if "Validation_Status" in cs.columns:
            cs = cs[cs["Validation_Status"].astype(str).str.upper().str.strip() == "YES"].copy()

        term_col = "Term" if "Term" in cs.columns else ("LCSH_Heading" if "LCSH_Heading" in cs.columns else cs.columns[0])
        variants_col = "Variants" if "Variants" in cs.columns else None
        uri_col = "LCSH_URI" if "LCSH_URI" in cs.columns else None

        vocabs["catholic_subjects"] = build_vocab_index(cs, term_col, variants_col, uri_col)

    v_path = vocab_dir / "vocations.xlsx"
    if v_path.exists():
        v = pd.read_excel(v_path, sheet_name=0, dtype=str).fillna("")
        term_col = "LCSH_heading" if "LCSH_heading" in v.columns else v.columns[0]
        variants_col = "Variants" if "Variants" in v.columns else None
        uri_col = "lcsh_uri" if "lcsh_uri" in v.columns else None
        vocabs["vocations"] = build_vocab_index(v, term_col, variants_col, uri_col)

    return vocabs


def enrich_output(source_df: pd.DataFrame, out_df: pd.DataFrame, vocab_dir: Path, enrich_cfg: Dict) -> pd.DataFrame:
    """
    Adds enrichment columns (appended by default):
      - date_begin, date_end, date_display
      - persons_extracted
      - subjects_catholic_matched, subjects_catholic_uris
      - vocations_matched, vocations_uris

    Date behavior:
      - Uses first existing date column from enrich_cfg['date_source_any_of']
      - If date cell blank, tries to extract from title column(s)
      - Month-name dates become ISO begin/end
    """
    df = out_df.copy()
    vocabs = load_controlled_vocabs(vocab_dir)

    append_cols = bool(enrich_cfg.get("append_enrichment_cols", True))
    if not append_cols:
        return df

    date_any = enrich_cfg.get("date_source_any_of", []) or ["Dates"]
    title_any = enrich_cfg.get("title_source_any_of", []) or ["title", "Title"]

    date_col = first_existing_col(source_df, date_any)
    title_col = first_existing_col(source_df, title_any)

    text_cols = enrich_cfg.get("text_cols_for_enrichment", []) or []
    existing_text_cols = [c for c in text_cols if c in source_df.columns]

    combined_text: List[str] = []
    for _, r in source_df.iterrows():
        parts = []
        for c in existing_text_cols:
            val = t_strip(r.get(c, ""))
            if val:
                parts.append(val)
        combined_text.append(" ".join(parts))
    combined_text_series = pd.Series(combined_text)

    # Dates split (column if exists; else title extraction if possible)
    begins, ends, displays = [], [], []
    for _, r in source_df.iterrows():
        raw_date = ""
        if date_col:
            raw_date = t_strip(r.get(date_col, ""))

        if not raw_date and title_col:
            title_val = t_strip(r.get(title_col, ""))
            extracted = extract_date_from_text(title_val)
            raw_date = extracted or ""

        b, e, d = parse_dates_cell(raw_date)
        begins.append(b)
        ends.append(e)
        displays.append(d)

    df["date_begin"] = begins
    df["date_end"] = ends
    df["date_display"] = displays

    # Names extracted
    df["persons_extracted"] = combined_text_series.map(extract_names)

    # Catholic subjects
    if "catholic_subjects" in vocabs:
        terms, uris = [], []
        for t in combined_text_series.tolist():
            mt, mu = match_vocab(t, vocabs["catholic_subjects"])
            terms.append(mt)
            uris.append(mu)
        df["subjects_catholic_matched"] = pd.Series(terms).map(t_dedupe_semicolon_list)
        df["subjects_catholic_uris"] = pd.Series(uris).map(t_dedupe_semicolon_list)

    # Vocations
    if "vocations" in vocabs:
        terms, uris = [], []
        for t in combined_text_series.tolist():
            mt, mu = match_vocab(t, vocabs["vocations"])
            terms.append(mt)
            uris.append(mu)
        df["vocations_matched"] = pd.Series(terms).map(t_dedupe_semicolon_list)
        df["vocations_uris"] = pd.Series(uris).map(t_dedupe_semicolon_list)

    # Normalize semicolon lists lightly
    for col in ["persons_extracted"]:
        if col in df.columns:
            df[col] = df[col].map(t_dedupe_semicolon_list)

    return df


# =========================
# Main CLI
# =========================
def main():
    ap = argparse.ArgumentParser(
        description="Universal mapper: any spreadsheet/XML -> portal upload sheet using mapping JSON + enrichment (vocabs, dates, names)."
    )
    ap.add_argument("--input", required=True, help="Input file (.xlsx, .csv, or SpreadsheetML .xml).")
    ap.add_argument("--portal_xlsx", required=True, help="Portal schema workbook containing 'Portal Label'.")
    ap.add_argument("--portal_sheet", default="Sheet1", help="Sheet name in portal.xlsx (default: Sheet1).")

    ap.add_argument("--input_sheet", default=None, help="Sheet name/index for input XLSX (default: first sheet).")
    ap.add_argument("--xml_sheet", default="ContainerList", help="Worksheet name for SpreadsheetML XML input (default: ContainerList).")

    ap.add_argument("--make_map", action="store_true", help="Generate a draft mapping JSON and exit.")
    ap.add_argument("--out_map", default="source_to_portal_map.json", help="Path to write draft mapping JSON.")
    ap.add_argument("--map_json", default="", help="Mapping JSON path to use for conversion.")
    ap.add_argument("--out_xlsx", default="portal_upload.xlsx", help="Output Excel file path.")
    ap.add_argument("--vocab_dir", default=".", help="Folder containing controlled vocab XLSX files (default: current folder).")

    args = ap.parse_args()

    input_path = Path(args.input)
    portal_xlsx = Path(args.portal_xlsx)
    portal_labels = load_portal_labels(portal_xlsx, args.portal_sheet)

    source_df = load_input_table(input_path, args.input_sheet, xml_sheet=args.xml_sheet)

    if args.make_map:
        make_mapping_file(portal_labels, list(source_df.columns), Path(args.out_map))
        print(f"Wrote draft mapping: {args.out_map}")
        return

    if not args.map_json:
        raise SystemExit("ERROR: You must provide --map_json to convert (or use --make_map first).")

    map_path = Path(args.map_json)
    try:
        mapping = json.loads(map_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"ERROR: mapping JSON invalid: {e}")

    rules = mapping.get("portal_rules", {}) or {}
    constants = mapping.get("constants", {}) or {}
    enrich_cfg = mapping.get("enrich", {}) or {}

    out_df = apply_rules(source_df, portal_labels, rules, constants)

    out_df = enrich_output(source_df, out_df, Path(args.vocab_dir), enrich_cfg)
    
        # --- Copy enrichment dates into required portal columns (if empty) ---
    if "date_begin" in out_df.columns and "Date span (indexed)" in out_df.columns:
        out_df["Date span (indexed)"] = out_df["Date span (indexed)"].where(
            out_df["Date span (indexed)"].astype(str).str.strip() != "",
            out_df["date_begin"]
        )

    if "date_display" in out_df.columns and "Date (display)" in out_df.columns:
        out_df["Date (display)"] = out_df["Date (display)"].where(
            out_df["Date (display)"].astype(str).str.strip() != "",
            out_df["date_display"]
        )


    with pd.ExcelWriter(Path(args.out_xlsx), engine="openpyxl") as xw:
        out_df.to_excel(xw, index=False, sheet_name="portal_upload")

    print(f"Wrote: {args.out_xlsx}  (rows: {len(out_df)}, cols: {len(out_df.columns)})")


if __name__ == "__main__":
    main()
