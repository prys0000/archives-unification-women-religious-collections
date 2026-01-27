# Archives Unification — Women Religious Collections

**Standardized process to assess, normalize, and merge collections from multiple women religious repositories into a single, sustainable archival repository.**  
Focus areas: arrangement & description, metadata crosswalks, ingest workflows, quality assurance, rights & restrictions, and long-term stewardship.

> Standards: **DACS**, **EAD**, **Dublin Core**, **PREMIS**  
> Target systems: **ArchivesSpace** (description + management); **Omeka S** (or similar) for public delivery.

---

## Table of Contents
- [Purpose](#purpose)
- [Scope & Assumptions](#scope--assumptions)
- [Process Overview](#process-overview)
- [Adaptive Learning Model & Automation Layer](#adaptive-learning-model--automation-layer)
- [Information Model](#information-model)
  - [Controlled Series (S1–S10)](#controlled-series-s1s10)
  - [Subseries](#subseries)
  - [Agent Naming Standard](#agent-naming-standard-women-religious)
  - [Arrangement Principles](#arrangement-principles)
  - [Identifiers & Filenaming](#identifiers--filenaming)
  - [Containers & Locations](#containers--locations)
- [Metadata & Crosswalks](#metadata--crosswalks-to-date)
- [Workstreams](#workstreams)
- [Quality Assurance](#quality-assurance)
- [Policies & Ethics](#policies--ethics)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Purpose
Document a **repeatable, evidence-based** approach to standardize, combine, and migrate collections from ~10 legacy repositories (with uneven prior processing) into one central repository, while preserving provenance, honoring community context, and enabling discovery.

## Scope & Assumptions
- **Collections:** mixed levels of description; some fully processed, many minimally inventoried.
- **Content types:** administrative records, formation/membership, ministries (education/health/social/pastoral), visual materials, AV/oral histories, legal/financial, born-digital assets.
- **Outcomes:** unified series model, clean crosswalks, validated ingest packages, and public-facing description with appropriate restrictions.

---

## Process Overview
1. **Discovery & Assessment** — inventory sources; capture processing status, risk, and priority.
2. **Normalization** — map legacy description to a **controlled series model** and shared vocabularies.
3. **Arrangement & Description** — synthesize series/subseries; write scope/arrangement notes; preserve original order where meaningful.
4. **Metadata Crosswalks** — align EAD ↔ DC/Omeka; normalize authorities and dates/extent.
5. **Digitization & Digital Assets** — establish master/access policy, file naming, and PREMIS event capture.
6. **Packaging for Ingest** — create ArchivesSpace import CSV/EAD; attach digital objects; assign rights.
7. **QA/QC** — run validators, sampling checks, and remediation; record outcomes.
8. **Publication & Access** — push to public system; verify links/derivatives; implement restrictions.
9. **Sustainability** — change management, documentation, training, and periodic audits.

---

## Adaptive Learning Model & Automation Layer

This project is supported by an **adaptive learning model** that standardizes processing decisions across partner collections in the unification project. The model captures and applies repeatable rules for:

- **Arrangement & description** (series/subseries placement, scope/arrangement patterns)
- **Vocabulary normalization** (legacy/local terms → authorized standardized terms)
- **Metadata transformation** (worksheets/EAD exports → ArchivesSpace + Omeka-ready structures)
- **Quality control** (repeatable validation checks and remediation workflows)

A supporting set of scripts operationalizes these rules by:
- transforming legacy spreadsheets and EAD exports into **ArchivesSpace- and Omeka-ready** outputs
- enforcing QC checks (required fields, controlled terms, identifiers/URIs)
- preserving legacy context by retaining **local labels/identifiers/notes** as **variants and/or term notes**, while promoting the standardized authorized form

---

## Information Model

### Controlled Series (S1–S10)

| Series # | Title | Description | Date range | Extent | Arrangement | Access | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Governance and Administration | Records documenting the organizational structure, decision-making processes, and administrative functions of the congregation. Includes constitutional documents, general chapter proceedings, leadership correspondence, and policy development. | example (1850-present) | Variable | Chronological by administrative term, then alphabetical by record type | Some materials restricted per canonical requirements | Core administrative records essential for institutional continuity |
| 2 | Congregation History and Identity | Materials documenting the foundation, development, and historical narrative of the congregation. Includes founder materials, historical research, anniversaries, jubilees, and publications about congregation history. | example (1790-present) | Variable | Chronological and by record type | Generally open | Includes materials predating formal establishment |
| 3 | Membership and Sisters' Records | Individual files and collective records documenting members of the congregation throughout its history. Includes biographical information, formation records, ministry assignments, and necrology materials. | example (1850-present) | Extensive | Alphabetical by sister's name or chronological by entrance date | Restricted - Privacy considerations | Includes both professed members and candidates |
| 4 | Ministry and Apostolic Works | Records documenting the various ministries, missions, and apostolic activities of the congregation. Includes educational institutions, healthcare facilities, social service programs, and missionary work. | example (1850-present) | Extensive | By ministry type, then chronological or geographical | Variable by institution | Represents primary apostolic mission of congregation |
| 5 | Properties and Facilities | Records documenting the acquisition, development, maintenance, and disposition of congregation properties. Includes motherhouses, convents, institutions, and other real estate holdings. | example (1850-present) | Moderate to Extensive | By property name or location, then chronological | Some legal documents restricted | Includes architectural drawings and construction records |
| 6 | Financial and Legal Records | Financial records, legal documents, and business records documenting the fiscal operations and legal affairs of the congregation. Includes budgets, audits, investments, contracts, and legal proceedings. | example (1850-present) | Extensive | Chronological by fiscal year and by record type | Restricted - Confidential | Retention schedules apply to many financial records |
| 7 | Communications and Publications | Published and unpublished communications produced by or about the congregation. Includes newsletters, magazines, bulletins, promotional materials, and correspondence with external constituencies. | example (1850-present) | Moderate to Extensive | By publication title or communication type, then chronological | Generally open | Includes both internal and public communications |
| 8 | External Relations and Affiliations | Records documenting relationships with external organizations, affiliations, partnerships, and membership in larger ecclesiastical or professional bodies. Includes Vatican relations, diocesan connections, and ecumenical activities. | example (1850-present) | Moderate | Alphabetical by organization or chronological | Some materials restricted | Documents congregation's place in broader church and society |
| 9 | Visual and Audio Materials | Non-textual materials including photographs, audiovisual recordings, artwork, and digital media documenting the congregation's history, activities, and members. Organized by format and subject. | example (1880-present) | Extensive | By format, then chronological or by subject | Privacy restrictions on some photographs | Requires special storage and handling |
| 10 | Reference and Research Files | Materials collected for reference purposes, research projects, and administrative use. Includes subject files, clippings, external publications, and materials about related topics not directly created by the congregation. | example (1850-present) | Moderate | Alphabetical by subject or topic | Generally open | Supplementary materials for research and context |

### Subseries

| Series # | Subseries # | Title | Description | Dates | Access | Notes |
|---|---|---|---|---|---|---|
| 1 | 1.1 | Constitutions and By-Laws | Original and revised constitutions, rules, by-laws, and canonical documents defining the congregation | example (1850-present) |  |  |
| 1 | 1.2 | General Chapter Records | Proceedings, reports, proposals, voting records, and related materials from general chapters | example (1850-present) |  |  |
| 1 | 1.3 | Leadership Council Records | Minutes, correspondence, reports, and working files of the Superior General/President and Council | example (1850-present) |  |  |
| 1 | 1.4 | Provincial Administration | Administrative records from provincial or regional leadership | example (1900-present) |  |  |
| 1 | 1.5 | Policies and Procedures | Congregation-wide policies, procedures manuals, and operational guidelines | example (1900-present) |  |  |
| 2 | 2.1 | Founders and Early History | Records, correspondence, and biographical materials of founders and early leaders | example (1790-1900) |  |  |
| 2 | 2.2 | Historical Research and Studies | Research files, historical compilations, timelines, and analytical studies | example (1850-present) |  |  |
| 2 | 2.3 | Anniversaries and Jubilees | Materials from centennials, sesquicentennials, and other major commemorations | example (1900-present) |  |  |
| 2 | 2.4 | Annals and Chronicles | Annual reports, chronicles, and narrative histories of congregation activities | example (1850-present) |  |  |
| 2 | 2.5 | Heritage and Charism Materials | Documents related to congregation mission, charism, spirituality, and traditions | example (1850-present) |  |  |
| 3 | 3.1 | Individual Sisters' Files | Personal files containing biographical data, correspondence, ministry records, and documentation | example (1850-present) | Restricted |  |
| 3 | 3.2 | Initial Formation Records | Records of candidates, postulants, and novices including entrance applications and formation materials | example (1850-present) | Restricted |  |
| 3 | 3.3 | Necrology Files | Death records, obituaries, memorial materials, and funeral records | example (1850-present) | Restricted |  |
| 3 | 3.4 | Community Directories and Registers | Membership lists, biographical directories, and statistical registers | example (1850-present) | Restricted |  |
| 3 | 3.5 | Group Photographs and Jubilee Materials | Class photos, group portraits, and jubilee celebration records | example (1890-present) | Restricted |  |
| 4 | 4.1 | Educational Institutions | Records of schools, colleges, and universities operated or staffed by the congregation | example (1850-present) |  |  |
| 4 | 4.2 | Healthcare Facilities | Records of hospitals, clinics, and healthcare ministries | example (1860-present) |  |  |
| 4 | 4.3 | Social Services and Outreach | Documentation of social service programs, community outreach, and charitable works | example (1900-present) |  |  |
| 4 | 4.4 | Parish and Pastoral Ministry | Records related to parish assignments, religious education, and pastoral care | example (1850-present) |  |  |
| 4 | 4.5 | Mission Territories | Records from domestic and international mission assignments and establishments | example (1890-present) |  |  |
| 4 | 4.6 | Ministry Closure and Transition Records | Documentation of discontinued or transferred ministries | example (1950-present) |  |  |
| 5 | 5.1 | Motherhouse and Generalate | Records related to the congregation's central administration building and grounds | example (1850-present) |  |  |
| 5 | 5.2 | Formation and Retreat Centers | Records of novitiate facilities, formation houses, and retreat centers | example (1850-present) |  |  |
| 5 | 5.3 | Convents and Local Communities | Records of individual convent properties and local community houses | example (1850-present) |  |  |
| 5 | 5.4 | Property Acquisitions and Sales | Deeds, titles, purchase agreements, and property transaction records | example (1850-present) |  |  |
| 5 | 5.5 | Architectural Plans and Specifications | Building plans, architectural drawings, and construction specifications | example (1900-present) |  |  |
| 6 | 6.1 | Annual Budgets and Financial Reports | Operating budgets, financial statements, and annual fiscal reports | example (1850-present) | Restricted |  |
| 6 | 6.2 | Audits and Tax Records | Independent audits, IRS filings, and tax documentation | example (1920-present) | Restricted |  |
| 6 | 6.3 | Investment and Endowment Records | Investment portfolios, endowment management, and related correspondence | example (1900-present) | Restricted |  |
| 6 | 6.4 | Legal Documents and Contracts | Incorporation papers, contracts, agreements, and legal opinions | example (1850-present) | Restricted |  |
| 6 | 6.5 | Insurance Records | Insurance policies, claims, and risk management documentation | example (1900-present) | Restricted |  |
| 6 | 6.6 | Development and Fundraising | Records of capital campaigns, planned giving, and donor relations | example (1950-present) | Restricted |  |
| 7 | 7.1 | Congregation Newsletters and Bulletins | Internal newsletters, bulletins, and periodic communications to members | example (1880-present) |  |  |
| 7 | 7.2 | Official Publications and Periodicals | Magazines, journals, and other serial publications produced by the congregation | example (1890-present) |  |  |
| 7 | 7.3 | Promotional and Recruitment Materials | Vocation literature, brochures, and promotional publications | example (1900-present) |  |  |
| 7 | 7.4 | Press Releases and Media Relations | Press releases, media kits, and external communications materials | example (1950-present) |  |  |
| 7 | 7.5 | Annual Reports to Members | Annual reports, state of the congregation addresses, and summary reports | example (1950-present) |  |  |
| 8 | 8.1 | Vatican and Canonical Relations | Correspondence with Vatican offices, canonical permissions, and official church communications | example (1850-present) |  |  |
| 8 | 8.2 | Diocesan Relations | Correspondence and agreements with diocesan authorities and bishops | example (1850-present) |  |  |
| 8 | 8.3 | Conference and Association Memberships | Records related to LCWR, CMSWR, and other professional religious organizations | example (1950-present) |  |  |
| 8 | 8.4 | Ecumenical and Interfaith Relations | Records of participation in ecumenical activities and interfaith dialogue | example (1960-present) |  |  |
| 8 | 8.5 | Associate and Affiliate Programs | Records of lay associate programs and affiliate relationships | example (1980-present) |  |  |
| 9 | 9.1 | Photographic Materials | Individual and group photographs, slides, negatives, and digital images | example (1880-present) |  |  |
| 9 | 9.2 | Audio Recordings | Oral histories, speeches, recordings of events, and musical recordings | example (1950-present) |  |  |
| 9 | 9.3 | Video and Film Materials | Motion pictures, video recordings, and documentary films | example (1960-present) |  |  |
| 9 | 9.4 | Artwork and Visual Displays | Paintings, drawings, posters, banners, and exhibition materials | example (1850-present) |  |  |
| 9 | 9.5 | Digital Media and Born-Digital Records | Digital photographs, electronic files, websites, and social media archives | example (1990-present) |  |  |
| 10 | 10.1 | Subject Files | Topical files on various subjects relevant to congregation history and mission | example (1850-present) |  |  |
| 10 | 10.2 | Newspaper Clippings and Press Materials | Collected clippings, press coverage, and media materials about the congregation | example (1880-present) |  |  |
| 10 | 10.3 | External Publications and Reports | Publications from other religious congregations, church documents, and related materials | example (1900-present) |  |  |
| 10 | 10.4 | Research Project Files | Working files from historical research, dissertations, and scholarly projects | example (1950-present) |  |  |

---

### Agent Naming Standard (Women Religious)

To support cross-congregation discovery, de-duplication, and stable ArchivesSpace agent creation, the portal uses one consistent display label format for women religious. Use the [Agent Naming Standard/Agent_Use_Guide.md](Agent Naming Standard/Agent_Use_Guide.md).

#### Portal display label (canonical)
**Title Religious Name, Congregation (Birth Name), DOB–DOD**

**Example:**  
**Sister Ellen, Sisters of Charity of the Blessed Virgin Mary (Agatha Hurley), 1826-1902**

**Why this works:**
- improves search and filtering across congregations
- reduces duplicate-name collisions (e.g., “Sister Mary Joseph”)
- preserves identity context (congregation + birth name + life dates)
- remains stable even when source spellings vary

> **Note:** The ArchivesSpace **Agent** record stores additional identifying details and variant name forms.

#### Rules for building the label
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

#### Partner workflow (required for consistency)
1) Maintain a congregation authority worksheet (preferred name + variants; variants separated by semicolons).  
2) Run extraction to collect candidate names/roles/places from narrative fields.  
3) Standardize names using the authority worksheet (preferred → canonical).  
4) Populate the staging sheet (one person per row) for ArchivesSpace agent bulk upload.

> Reminder: For ArchivesSpace agent bulk upload, **one row = one person**. If a biography mentions multiple sisters, split them into separate rows.

---

### Arrangement Principles
- Function/provenance first (e.g., Governance vs. Formation vs. Ministries); format second where appropriate (e.g., S9).
- Keep documentation with the record it documents (e.g., commission files with commissioned artworks).
- Respect original order for minutes, registers, and bound items; document deviations.

### Identifiers & Filenaming
- Pattern: `HARC_COLLID_SERIES_SUBSERIES_(FILE)_BOX_FOLDER_ITEM` (zero-padded 0000).  
  **Example:** `HARC-004-(S)2-(SS)4-(BOX)0002-(FOLDER)0001-(ITEM)0003` → collection HARC-004, Series S2, Subseries 4.
- Digital masters: `{identifier}__pm.tif` (preservation master); access: `{identifier}__ac.jpg` / `{identifier}__ac.mp4`.

### Containers & Locations
- Map oversize/3D to dedicated locations (flat files, map cases, object racks).
- Track location in finding aid + container list; mirror in system fields where applicable.

---

## Metadata & Crosswalks (to date)
- **`/mappings/aspace_crosswalk.xlsx`** — EAD ↔ series/subseries model ↔ ArchivesSpace import templates (CSV-ready).
- **`/mappings/omeka_dc_crosswalk.xlsx`** — EAD/DC alignment for public discovery in Omeka S (field + label behavior).
- **`/mappings/bvm_crosswalk.xlsx`** — BVM worksheet crosswalk: legacy/local fields ↔ standardized NAPWR/HARC terms ↔ ArchivesSpace/Omeka-ready outputs.
- **`/mappings/csc_crosswalk.xlsx`** — CSC worksheet crosswalk: legacy/local fields ↔ standardized NAPWR/HARC terms ↔ ArchivesSpace/Omeka-ready outputs.
- **`/mappings/oms_crosswalk.xlsx`** — OMS worksheet crosswalk: legacy/local fields ↔ standardized NAPWR/HARC terms ↔ ArchivesSpace/Omeka-ready outputs.

### Controlled vocabularies & authority alignment
- **Standardize without erasing context:** authorized standardized term is canonical; legacy/local terms remain traceable via **variants, scope notes, term notes, and retained identifiers**.
- **Authority sources (matching + normalization):**
  - **LCSH / LCCN** — topical subjects and authorized headings
  - **LCNAF** — persons, corporate bodies, and religious institutes where applicable
  - **Getty** — **AAT** (materials/genres/object types), **TGN** (places), **ULAN** (creators when relevant)
  - **Catholic-specific controlled lists** — crosswalked into standardized headings; mapped to LoC/Getty where possible
- **Congregational controlled lists (unification project):**
  - Crosswalks created for **original + legacy congregational vocabularies** → **standardized project vocabularies**
  - Legacy labels retained as **variants/alternate labels** with partner attribution and notes

### ArchivesSpace implementation support
- **ArchivesSpace controlled values:** mappings and guidance for built-in controlled lists (subjects, agents, places, etc.) while preserving external URIs/IDs.
- **Bulk uploads & data operations:** repeatable workflows (agents/subjects/places/digital objects) supported by:
  - de-duplication rules (authorized as canonical; legacy as variant)
  - consistent source attribution (local vs LoC vs Getty)
  - capture of identifiers/URIs and explanatory notes for auditability

### Date policy
- **Normalization:** ISO-8601 for machine use (sorting, exports, faceting)
- **Display preservation:** retain original/human-readable strings alongside normalized dates

---

## Workstreams
- **Adaptive Standardization & Learning (`/models/`, `/docs/model/`, `/scripts/`)** — the decision layer for unification:
  - standardizes arrangement + description patterns across partners (series/subseries, titles, scope notes)
  - normalizes controlled terms to authorized forms while retaining legacy variants/notes
  - drives repeatable transforms into ArchivesSpace + Omeka import structures
- **Intake & Appraisal (`/templates/intake/`)** — accession documentation, transfer logs, donor communications.
- **Arrangement & Description (`/models/`, `/docs/arrangement/`)** — series mapping (S1–S10), arrangement statements, scope notes.
- **Metadata & Crosswalks (`/mappings/`)** — crosswalks (EAD ↔ worksheets ↔ ASpace/Omeka), controlled lists, field rules, validation rules.
- **Digitization (`/policies/digitization.md`)** — preservation/access specifications; device profiles; PREMIS event capture.
- **Systems & Pipelines (`/scripts/`)** — ASpace import/export and bulk uploads; identifier/URI enrichment; validation utilities; exports; Omeka sync.
- **Access & Outreach (`/docs/access/`)** — restrictions, rights, takedown, discovery guidance; IIIF (optional).

---

## Quality Assurance

### Acceptance criteria (per batch)
- ✅ **Arrangement integrity:** all described units mapped to **S1–S10**, with subseries assigned where applicable.
- ✅ **Required metadata present:** title, date(s), extent, scope/abstract, creator, identifiers.
- ✅ **Authority + controlled-term compliance (when used):**
  - **LCSH / LCCN** — authorized topical subjects (canonical form)
  - **LCNAF** — authorized names (people/corporate bodies/religious institutes where applicable)
  - **Getty** — AAT (materials/genres/object types), TGN (places), ULAN (creators when relevant)
  - **Catholic-specific controlled lists** — crosswalked into standardized headings and mapped to LoC/Getty where possible
- ✅ **Legacy preservation rule:** standardized authorized term is canonical; legacy/local terms remain traceable as **variants and/or term notes** with identifiers and partner attribution.
- ✅ **Bulk upload readiness:** ArchivesSpace imports conform to required fields and controlled value expectations (agents/subjects/places/digital objects as applicable).
- ✅ **Digital objects:** linked correctly; access derivatives present when required.
- ✅ **Restrictions + rights:** applied consistently across records and exports.

### Sampling plan
- **Descriptive accuracy:** 5–10% stratified sample across series (verify titles, dates, identifiers, series/subseries placement).
- **Metadata validation:** 100% automated checks; 10% human spot-check for edge cases (ambiguous terms, dates, legacy variants).
- **Digital integrity:** 100% checksums; 2% bit-level re-verification.
- **Link integrity:** 100% public links tested post-publication (ArchivesSpace public UI and Omeka where applicable).

### Tools
- **`/scripts/validation/`** — CSV/EAD validators, authority matching checks, identifier/URI checks, link checker, checksum verification.

---

## Policies & Ethics
- **Restrictions:** personal/formation files; personnel evaluations; health & spiritual direction notes.
- **Rights:** identify copyright holder; state permitted uses; provide request workflow.
- **Cultural & community sensitivity:** consult congregational leadership; document ethical considerations in `/policies/`.

---

## Repository Structure
_TODO: Add directory map and brief descriptions of key folders._

## Contributing
_TODO: Add contribution guidelines and coding/data standards._

## License
_TODO: Add license statement._
