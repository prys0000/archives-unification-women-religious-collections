# Archives Unification — Women Religious Collections

**Standardized process to assess, normalize, and merge collections from multiple women religious repositories into a single, sustainable archival repository.**  
Focus areas: arrangement & description, metadata crosswalks, ingest workflows, quality assurance, rights & restrictions, and long-term stewardship.

> Standards: **DACS**, **EAD**, **Dublin Core**, **PREMIS**, **AAT/FAST/LCNAF**, **IIIF (optional)**  
> Target systems (example): **ArchivesSpace** for description; **Omeka S** (or similar) for public delivery.

---

## Table of Contents
- [Purpose](#purpose)
- [Scope & Assumptions](#scope--assumptions)
- [Governance & Roles](#governance--roles)
- [Process Overview](#process-overview)
- [Information Model](#information-model)
  - [Controlled Series (S1–S10)](#controlled-series-s1s10)
  - [Identifiers & Filenaming](#identifiers--filenaming)
  - [Containers & Locations](#containers--locations)
- [Metadata & Crosswalks](#metadata--crosswalks)
- [Workstreams](#workstreams)
- [Quality Assurance](#quality-assurance)
- [Policies & Ethics](#policies--ethics)
- [Repository Structure](#repository-structure)
- [How to Use This Playbook](#how-to-use-this-playbook)
- [Contributing](#contributing)
- [License](#license)

---

## Purpose
Document a **repeatable, evidence-based** approach to standardize, combine, and migrate collections from ~10 legacy repositories (with uneven prior processing) into one central repository, while preserving provenance, honoring community context, and enabling discovery.

## Scope & Assumptions
- **Collections:** Mixed levels of description; some fully processed, many minimally inventoried.
- **Content types:** Administrative records, formation/membership, ministries (education/health/social/pastoral), visual materials, AV/oral histories, legal/financial, digital assets.
- **Outcomes:** Unified series model, clean crosswalks, validated ingest packages, and public-facing description with appropriate restrictions.

---

## Governance & Roles
| Role | Responsibilities |
|---|---|
| Project Lead | Scope, timeline, decision log, risk mgmt. |
| Arrangement Lead | Series mapping, folder structure, finding aid synthesis. |
| Metadata Lead | Crosswalks (EAD/DC), controlled vocabularies, data validation. |
| Systems Lead | ArchivesSpace/OAI/exports, Omeka S mappings, integrations. |
| Preservation Lead | PREMIS events, storage tiers, checksums, fixity. |
| QA Coordinator | Sampling plans, acceptance criteria, remediation cycles. |

*RACI is defined per workstream in `/docs/governance/`.*

---

## Process Overview
1. **Discovery & Assessment** — inventory sources; capture processing status, risk, and priority.
2. **Normalization** — map legacy description to a **controlled series model** and shared vocabularies.
3. **Arrangement & Description** — synthesize series/subseries; write scope/arrangement notes; preserve original order where meaningful.
4. **Metadata Crosswalks** — align EAD ↔ DC/Omeka S; authorities (AAT/FAST/LCNAF); dates/extent normalization.
5. **Digitization & Digital Assets** — establish master/access policy, file naming, and PREMIS event capture.
6. **Packaging for Ingest** — create ArchivesSpace import CSV/EAD; attach digital objects; assign rights.
7. **QA/QC** — run validators, sampling checks, and remediation; record outcomes.
8. **Publication & Access** — push to public system; verify links/derivatives; implement restrictions.
9. **Sustainability** — change mgmt, documentation, training, and periodic audits.

---

## Information Model

### Controlled Series (S1–S10)
| Code | Series | Scope (abbrev.) | Example Subseries |
|---|---|---|---|
| **S1** | Governance & Administration | Constitutions/rules; Chapter; Council; policies; committees. | S1.1 Constitutions & Rules · S1.2 General Chapter · S1.3 Council Minutes · S1.4 Policies · S1.5 Committees & Reports |
| **S2** | Membership & Community Life | Vocation through perpetual profession; directories; necrologies; jubilees. | S2.1 Inquiry/Vocation · S2.2 Candidacy · S2.3 Postulancy · S2.4 Novitiate · S2.5 Temp. Profession · S2.6 Perpetual · S2.7 Ongoing Formation · S2.8 Directories · S2.9 Necrologies · S2.10 Jubilees |
| **S3** | Ministries & Apostolates | Education, health care, social services, overseas missions, parish/pastoral. | S3.1 Education · S3.2 Health Care · S3.3 Social Services · S3.4 Missions · S3.5 Parish/Pastoral |
| **S4** | Financial & Development | Accounting, audits, grants, fundraising, donor relations. | S4.1 Accounting/Budgets · S4.2 Audits · S4.3 Grants · S4.4 Development · S4.5 Donors |
| **S5** | Property & Facilities | Real estate, construction, architectural drawings, maintenance, cemeteries. | S5.1 Real Estate · S5.2 Construction/Renovation · S5.3 Plans/Maps · S5.4 Facilities Ops · S5.5 Cemeteries |
| **S6** | Communications & Publications | Newsletters/serials, press/clippings, brochures, web/social. | S6.1 Newsletters · S6.2 Press/Clippings · S6.3 Brochures/Ephemera · S6.4 Web/Social · S6.5 Media Relations |
| **S7** | Visual Materials & Artwork | Photos, albums/scrapbooks; works on paper; paintings/framed; sculpture; exhibits. | S7.1 Photographs · S7.2 Works on Paper · S7.3 Paintings & Framed · S7.4 Sculpture & Objects · S7.5 Exhibitions · S7.6 Reproductions |
| **S8** | Audio-Visual & Oral History | Audio, video/film, oral histories (recordings & transcripts), event recordings. | S8.1 Audio · S8.2 Video/Film · S8.3 Oral Histories · S8.4 Event Recordings |
| **S9** | Legal & Corporate Records | Incorporation/bylaws, trademarks/IP, insurance/risk, contracts, counsel. | S9.1 Incorporation/Bylaws · S9.2 Trademarks/IP · S9.3 Insurance/Risk · S9.4 Contracts · S9.5 Counsel |
| **S10** | Digital Assets & Info Systems | Born-digital, digitized masters, access copies, metadata/exports, backups. | S10.1 Born-Digital · S10.2 Digitized Masters · S10.3 Access Copies · S10.4 Metadata/Exports · S10.5 Backups |

**Arrangement principles**
- Function/provenance first (e.g., Governance vs. Formation vs. Ministries); format second where appropriate (e.g., S7).
- Keep documentation with the record it documents (e.g., commission files with commissioned artworks).
- Respect original order for minutes, registers, and bound items; document deviations.

### Identifiers & Filenaming
- Pattern: `COLLID-SERIES-SUBSERIES-BOX-FOLDER-ITEM` (zero-padded).  
  Example: `WR004-S2-4-0002-0001-0003` → collection WR004, Series S2 (Membership), Subseries 4 (Novitiate).
- Digital masters: `{identifier}__pm.tif` (preservation master); access: `{identifier}__ac.jpg` / `{identifier}__ac.mp4`.

### Containers & Locations
- Map oversize/3D to dedicated locations (flat files, map cases, object racks).  
- Track location in finding aid + container list; mirror in systems fields (extent/types).

---

## Metadata & Crosswalks
- **`/mappings/aspace_crosswalk.xlsx`** — EAD ↔ controlled series/subseries ↔ ArchivesSpace import CSV.
- **`/mappings/omeka_dc_crosswalk.xlsx`** — EAD/DC field alignment for public site (Omeka S).
- **Authorities:** AAT (formats/materials), FAST/LC (subjects), LCNAF/ULAN (names), TGN (places).
- **Date policy:** normalize to ISO-8601; retain original display strings.

---

## Workstreams
- **Intake & Appraisal (`/templates/intake/`)** — accession, transfer logs, donor communications.
- **Arrangement & Description (`/models/`, `/docs/arrangement/`)** — series mapping, scope notes, arrangement statements.
- **Metadata (`/mappings/`)** — crosswalks, controlled lists, validation rules.
- **Digitization (`/policies/digitization.md`)** — master/access specs; device profiles; PREMIS events.
- **Systems (`/scripts/`)** — ASpace import/export; OAI harvest; Omeka S sync.
- **Access & Outreach (`/docs/access/`)** — restrictions, rights, takedown, IIIF (optional).

---

## Quality Assurance
**Acceptance criteria (per batch)**
- ✅ All described units mapped to S1–S10 with subseries where applicable.  
- ✅ Required metadata present (title, date, extent, scope/abstract, creator, identifiers).  
- ✅ Authorities validated against AAT/FAST/LC where used.  
- ✅ Digital objects linked; derivatives present for public access.  
- ✅ Restrictions and rights statements applied consistently.

**Sampling plan**
- **Descriptive accuracy:** 5–10% stratified across series; verify titles/dates/identifiers.  
- **Metadata validation:** 100% machine checks; 10% human spot-check.  
- **Digital integrity:** 100% checksums; 2% bit-level re-verify.  
- **Link integrity:** 100% public links tested post-publication.

**Tools**
- `/scripts/validation/` — CSV/EAD validators, authority checks, link checker, checksum verify.

---

## Policies & Ethics
- **Restrictions:** personal/formation files; personnel evaluations; health & spiritual direction notes.  
- **Rights:** identify copyright holder; state permitted uses; provide request workflow.  
- **Cultural & community sensitivity:** consult congregational leadership; document ethical considerations in `/policies/`.

---

## Repository Structure
