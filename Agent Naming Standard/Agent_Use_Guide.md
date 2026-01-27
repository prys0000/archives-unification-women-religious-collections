# Agent/Sister Naming Worksheets: What We Collect vs What We Upload

This project distinguishes between (1) **preservation-grade backend data** collected for archival longevity and identity management, and (2) a **curated subset** used for **public discovery** and **bulk uploads**. The bulk upload sheet is treated as a reproducible export derived from the master worksheet—not the authoritative record.

---

## What the two worksheets represent

### `names_metadata_template.xlsx` (metadata capture: backend/source-of-truth)
This is the **rich capture layer** (what we *collect*). It includes identity, lifecycle events, narrative context, and normalization fields, such as:

- **Identity**
  - `ID`
  - `congregation`
  - `Family_Name`
  - `Baptismal_Name`
  - `Religious_Name`
  - `current_name` (preferred/current label used for standardization)
- **Dates/places**
  - `date_of_birth`, `place_of_birth`
  - `entrance_date`, `re_entrance_date`
  - `first_profession` ... `final_profession`
  - `date_of_death`
  - `left_congregation`
- **Narrative + context**
  - `Vocation(s):work_experience_career`
  - `location_mission`
  - `biography`
  - `notes`, `additional_notes`
  - `SUMRY-2`
- **Normalization outputs (unification support)**
  - `napwr:roles_lcsh(1)` (role normalization/authority alignment)
  - `napwr:places_canonical`
  - `napwr:place_variants_found`
  - `registry_book___registry_book_`, `page___page` (source citation pointers)

> Note: If you see duplicated columns (e.g., multiple `additional_notes`) or headers with trailing line breaks, normalize the column names before running transforms.

### `names_csv_chuck_transform.csv` (ArchivesSpace upload staging/export)
This is the **upload-facing layer** (what we *push*). It is a curated, stable, reproducible export used to generate ArchivesSpace Agent records consistently.

Common characteristics:
- includes the standardized name fields needed for agents
- includes computed helpers (e.g., sort dates)
- includes `NOTES` to preserve legacy IDs, provenance, variants, and normalization decisions
- should not contain stray `Unnamed:` columns (remove them if present)

---

## Principle: preservation-grade backend vs curated public display

### Backend (archival longevity / stewardship)
Backend collection preserves identity + provenance context needed for long-term stewardship and future migrations:
- stable identifiers (project + partner)
- variant name forms (abbreviations, spellings, legacy labels)
- congregation attribution + sources (e.g., registry book/page)
- authority alignments (LCNAF/LCSH/LCCN; Getty where relevant)
- lifecycle events (entrance/profession/death) and uncertainty notes
- privacy/restriction flags and internal processing notes

### Public-facing portal (curated subset)
Public display is intentionally smaller and standardized for safe discovery:
- canonical portal label (NAPWR standard)
- congregation
- life dates (or partial)
- high-level vocation/role summary (when permitted)
- curated biography/summary (reviewed)
- places at an appropriate level (policy-dependent)

---

## Transformation pipeline: worksheet → staging → ArchivesSpace

### Step A — Collect (`names_test.xlsx`)
Use `names_test.xlsx` as the **capture layer** and source of truth.

### Step B — Standardize + enrich (model rules)
Apply consistent rules to generate:
- the canonical portal label (from naming standard)
- controlled roles/places fields (NAPWR normalized)
- authority/variant handling
- provenance notes (registry book/page, partner IDs)

### Step C — Export for bulk upload (`names-csv-chuck-text.xlsx`)
Generate an upload-ready view for ArchivesSpace:
- minimal, stable fields required for agent creation
- `NOTES` carries: legacy IDs + variants + mapping decisions + sources
- output is reproducible (can be regenerated from `names_test.xlsx`)
