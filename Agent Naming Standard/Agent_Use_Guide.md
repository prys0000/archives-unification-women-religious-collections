# Agent/Sister Naming Worksheets: What We Collect vs What We Upload

This project distinguishes between (1) **preservation-grade backend data** collected for archival longevity and identity management, and (2) a **curated subset** used for **public discovery** and **bulk uploads**. The bulk upload sheet is treated as a reproducible export derived from the master worksheet—not the authoritative record.

---

## What the two attached worksheets represent

### `names_metadata_template.xlsx` (metadata collection worksheet example)
This is the **rich capture layer** (what we *collect*). It currently includes fields such as:

- `dcterms:identifier`
- `dcterms:contributor` (congregation / partner)
- `dcterms:title` (name label used for discovery)
- `harc:titleBirthName`
- `harc:titleFamilyName`
- `harc:dateBirth`
- `harc:dateDied`
- `harc:entranceDate`
- `harc:firstVowsDate`
- `harc:finalVowsDate`
- `harc:reenterDate`
- `harc:spatialMission`
- `harc:vocation`
- `dcterms:description`
- `dcterms:spatial`

> Note: This file includes an empty/unnamed column header (a blank column). Remove it to avoid transform issues.

### `names_csv_chunk_transform.csv` (ArchivesSpace upload staging)
This is the **upload-facing layer** (what we *push*). It contains core name/date fields plus operational columns such as:

- `NOTES` (critical for preserving legacy IDs, variant forms, provenance, and normalization decisions)
- `ENTRANCE_SORT_DATE` (machine-sort helper)
- additional “Unnamed:” columns (e.g., `Unnamed: 16–20`) that should be removed before treating this as a clean staging template

---

## Principle: preservation-grade backend vs curated public display

### Backend (archival longevity / stewardship)
Backend collection preserves the full identity and provenance context needed for long-term management and future migrations:

- stable identifiers (local + project)
- variant names, abbreviations, misspellings, and legacy forms
- congregation attribution + source notes (“where did this name/date come from?”)
- authority alignments (LCNAF/LCSH/LCCN, Getty where relevant)
- lifecycle events (entrance / vows / death) and uncertainty notes
- privacy/restriction logic (formation/personnel/health/spiritual direction)
- internal notes and crosswalk decisions that support de-duplication

### Public-facing portal (curated, safe, useful)
Public-facing display is intentionally smaller and standardized to support discovery without exposing sensitive information:

Typically safe/useful:
- canonical portal label (NAPWR standard)
- congregation
- life dates (or partial dates)
- vocation / ministry summary (high level)
- short public bio/description (if reviewed)
- place info at an appropriate level (e.g., mission region/city when permitted)

Typically not public by default:
- entrance / vows / re-entry dates (policy-dependent; often sensitive)
- internal notes, personnel/formation evaluations
- medical/health and spiritual direction content
- highly granular location histories that create privacy risk

---

## Transformation pipeline: worksheet → staging → ArchivesSpace

### Step A — Collect (metadata worksheet)
Use the metadata worksheet as the **capture layer** and source of truth.

**Minimum fields to collect per person (recommended):**
- `dcterms:identifier` (stable person ID — do not change once assigned)
- `dcterms:contributor` (standard congregation string)
- `dcterms:title` (preferred religious name form or canonical label strategy)
- `harc:titleBirthName` and/or `harc:titleFamilyName` (if known)
- `harc:dateBirth`, `harc:dateDied` (ISO when possible; otherwise year; otherwise blank)
- `dcterms:description` (public summary or internal bio—label clearly via notes/policy)

Optional (project-dependent):
- `harc:vocation`, `harc:spatialMission`, `dcterms:spatial`

### Step B — Standardize + enrich (model rules)
Apply naming and controlled rules consistently:

- normalize dates (ISO-8601 where possible)
- build a canonical **portal label** using the naming standard
- generate machine helpers (e.g., `ENTRANCE_SORT_DATE`)
- compile legacy terms/IDs and variant forms into `NOTES`

### Step C — Produce upload sheet (ArchivesSpace staging)
Generate `names-csv-chuck-text.xlsx` as the **upload-ready view**:

- includes only what the bulk pipeline needs
- is safe to regenerate at any time from the master worksheet
- retains `NOTES` as the bridge for provenance, exceptions, and auditability

---

## Recommended mapping contract between the two sheets

### 1) Pass-through fields (same in both)
- `dcterms:identifier`
- `dcterms:contributor`
- `dcterms:title`
- `harc:titleBirthName`
- `harc:titleFamilyName`
- `harc:dateBirth`
- `harc:dateDied`
- `harc:entranceDate`
- `harc:firstVowsDate`
- `harc:finalVowsDate`
- `harc:reenterDate`
- `harc:spatialMission`
- `harc:vocation`
- `dcterms:description`
- `dcterms:spatial`

### 2) Upload-only helper fields (computed)
- `ENTRANCE_SORT_DATE` (computed from entrance date; blank if unknown)
- `NOTES` (compiled from: legacy IDs + name variants + normalization notes + source citations)

### 3) Backend-only fields (recommended, even if not uploaded every run)
Add these to the master worksheet (or to a linked authority worksheet) to support scaling across partners:

- `portal_label` (canonical display label)
- `name_variants` (semicolon-separated)
- `local_partner_person_id` (if different from `dcterms:identifier`)
- `authority_lcnaf_uri` (if matched)
- `authority_lc_subject_uri` / `lc_lccn` (when relevant)
- `tgn_uri` (when place normalization is done)
- `privacy_flag` / `public_ok` (Y/N)
- `source_note` (where the data came from)

---

## Summary
We collect **preservation-grade person metadata** in the master worksheet (including variants, identifiers, sources, and normalization notes) and then generate:

1) a **curated, upload-ready view** for ArchivesSpace bulk operations, and  
2) a **curated public subset** for portal display.

The upload sheet is a reproducible export derived from the master worksheet—not the authoritative record.
