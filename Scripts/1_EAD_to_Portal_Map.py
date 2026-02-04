import argparse
from pathlib import Path
from typing import Dict, List, Any

import pandas as pd
from lxml import etree


SS_NS = "urn:schemas-microsoft-com:office:spreadsheet"
NS = {"ss": SS_NS}


def read_spreadsheetml_worksheet(xml_path: Path, worksheet_name: str) -> pd.DataFrame:
    """
    Reads an Excel 2003 XML Spreadsheet (SpreadsheetML) worksheet into a DataFrame.
    Handles ss:Index gaps in cells.
    """
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
    df = pd.DataFrame(data, columns=header).fillna("")
    return df


def load_portal_schema(portal_xlsx: Path, sheet: str) -> pd.DataFrame:
    """
    portal.xlsx must have:
      - 'Portal Label' (output column name)
    and ideally:
      - 'ArchivesSpace_field' (maps from EAD/ContainerList column)
    """
    schema = pd.read_excel(portal_xlsx, sheet_name=sheet, dtype=str).fillna("")
    if "Portal Label" not in schema.columns:
        raise ValueError("portal.xlsx must contain a column named 'Portal Label'.")
    if "ArchivesSpace_field" not in schema.columns:
        # still works: will output columns with blanks
        schema["ArchivesSpace_field"] = ""
    return schema


def normalize_colname(x: Any) -> str:
    return str(x).strip()


def map_container_to_portal(
    container_df: pd.DataFrame,
    portal_schema: pd.DataFrame,
    *,
    keep_all_levels: bool = True
) -> pd.DataFrame:
    """
    For each row in portal_schema:
      - output column name = Portal Label
      - source column name = ArchivesSpace_field
      - if source exists in container_df -> copy values
      - else -> blank

    keep_all_levels=True keeps series/subseries/file/item rows.
    """
    container_cols = {normalize_colname(c): c for c in container_df.columns}
    portal_labels = [normalize_colname(x) for x in portal_schema["Portal Label"].tolist() if normalize_colname(x)]

    # Create output with all portal columns, initialized blank
    out = pd.DataFrame({label: [""] * len(container_df) for label in portal_labels})

    # Fill portal columns where a mapping exists and the source column exists
    for _, row in portal_schema.iterrows():
        portal_label = normalize_colname(row.get("Portal Label", ""))
        if not portal_label:
            continue

        src = normalize_colname(row.get("ArchivesSpace_field", ""))
        if not src:
            # no mapping provided -> leave blank
            continue

        # If the EAD sheet has that column, copy it; otherwise leave blank
        if src in container_cols:
            out[portal_label] = container_df[container_cols[src]].astype(str).fillna("")

    # OPTIONAL: add EAD columns that are NOT represented in portal.xlsx
    # User asked: "If columns dont exist in either then just create a column with blank."
    # The strict interpretation for portal upload is: output portal columns only (extras excluded).
    # If you want a UNION output (portal + all EAD columns), enable this behavior here.
    # For now: portal-only output.

    return out.fillna("")


def main():
    ap = argparse.ArgumentParser(
        description="Map hierarchical EAD→Excel SpreadsheetML (ContainerList) to Portal upload sheet. Missing fields become blanks."
    )
    ap.add_argument("--ead_xml", required=True, help="Path to EAD-to-Excel SpreadsheetML XML (ead-excel.xml).")
    ap.add_argument("--portal_xlsx", required=True, help="Path to portal.xlsx.")
    ap.add_argument("--out_xlsx", required=True, help="Output .xlsx path.")
    ap.add_argument("--container_sheet", default="ContainerList", help="Worksheet in ead-excel.xml (default: ContainerList).")
    ap.add_argument("--portal_sheet", default="Sheet1", help="Sheet in portal.xlsx (default: Sheet1).")
    ap.add_argument("--add_ead_extras", action="store_true",
                    help="If set, append any EAD columns not mapped in portal.xlsx as extra columns (rarely needed for portal import).")
    args = ap.parse_args()

    ead_xml = Path(args.ead_xml)
    portal_xlsx = Path(args.portal_xlsx)
    out_xlsx = Path(args.out_xlsx)

    container_df = read_spreadsheetml_worksheet(ead_xml, args.container_sheet)
    portal_schema = load_portal_schema(portal_xlsx, args.portal_sheet)

    out_df = map_container_to_portal(container_df, portal_schema, keep_all_levels=True)

    # Optional: append unmapped EAD columns (only if you truly want them in the output)
    if args.add_ead_extras:
        portal_mapped = set(normalize_colname(x) for x in portal_schema["ArchivesSpace_field"].tolist() if normalize_colname(x))
        extras = [c for c in container_df.columns if normalize_colname(c) not in portal_mapped]
        for c in extras:
            # add as-is, but only if not already present as a portal label
            if c not in out_df.columns:
                out_df[c] = container_df[c].astype(str).fillna("")

    with pd.ExcelWriter(out_xlsx, engine="openpyxl") as xw:
        out_df.to_excel(xw, index=False, sheet_name="portal_upload")

    print(f"Wrote: {out_xlsx}  (rows: {len(out_df)}, cols: {len(out_df.columns)})")


if __name__ == "__main__":
    main()
