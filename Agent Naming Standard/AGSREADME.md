# Agent Naming Standard (Women Religious)

To support cross-congregation discovery, de-duplication, and stable ArchivesSpace agent creation, the portal uses one consistent display label format for women religious.

## Portal display label (canonical)
#### Title Religious Name, Congregation (Birth Name), DOB–DOD

**Example:**  
***Sister Ellen, Sisters of Charity of the Blessed Virgin Mary (Agatha Hurley), 1826-1902***

**Why this works:**
- improves search and filtering across congregations
- reduces duplicate-name collisions (e.g., “Sister Mary Joseph”)
- preserves identity context (congregation + birth name + life dates)
- remains stable even when source spellings vary

> *Note: The ArchivesSpace **Agent** record stores additional identifying details and variant name forms.*

## Rules for building the label
Use these rules consistently:
- **Title:** use `Sister` unless a more specific title is known (e.g., `Mother`).
- **Religious name:** use the preferred form from the partner authority worksheet.
- **Congregation:** use the standardized congregation string (consistent spelling).
- **Birth name:** include in parentheses **only if known**.
- **Dates:** use `YYYY-YYYY` when possible (or `YYYY-` / `-YYYY` if partial dates are allowed).

Omit safely when unknown:
- if birth name unknown → omit parentheses entirely
- if dates unknown → omit the date portion entirely

**Examples:**
- **Full:** Sister Ellen, Sisters of Charity of the Blessed Virgin Mary (Agatha Hurley), 1826-1902
- **No birth name:** Sister Ellen, Sisters of Charity of the Blessed Virgin Mary, 1826-1902
- **No dates:** Sister Ellen, Sisters of Charity of the Blessed Virgin Mary (Agatha Hurley)

## ArchivesSpace agent record guidance
- **Authorized name (primary):** use the canonical portal label elements to ensure uniqueness:
  - prefix/title: `Sister` / `Mother`
  - primary name: religious name
  - qualifier: standardized congregation string (when needed for disambiguation)
  - dates: DOB–DOD (or partial)
- **Variants (alternate names):** store common abbreviations and legacy forms:
  - `Sr. …`, `S. …`, spelling variants, nickname forms
  - birth-name forms (where known)
- **Notes:** preserve legacy identifiers, provenance, and crosswalk notes used for unification and de-duplication decisions.
- > Reminder: For ArchivesSpace agent bulk upload, **one row = one person**. If a biography mentions multiple sisters, split them into separate rows.


## Partner workflow (required for consistency)
1) Maintain a congregation authority worksheet (preferred name + variants; variants separated by semicolons).  
2) Run extraction to collect candidate names/roles/places from narrative fields.  
3) Standardize names using the authority worksheet (preferred → canonical).  
4) Populate the staging sheet (one person per row) for ArchivesSpace agent bulk upload.


