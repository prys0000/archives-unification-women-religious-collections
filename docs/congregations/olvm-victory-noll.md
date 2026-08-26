# Our Lady of Victory Missionary Sisters / Victory Noll — Integration Case Record

## Integration Overview

**Congregation:** Our Lady of Victory Missionary Sisters / Victory Noll Sisters  
**Case slug:** `olvm-victory-noll`  
**Status:** Active / living documentation  
**Framework:** Linear Reciprocity Model (LRM)  
**Discovery environment:** HARC / NAPWR

The Victory Noll collection arrived in generally usable descriptive and physical condition. Existing arrangement, inventories, and archival description provided a meaningful basis for processing.

The principal problem was not absence of control, but **earlier archival intervention that had altered the provenance and intellectual relationships of records**.

At some point in the collection's processing history, records were removed from their functional or administrative series and redistributed into individual Sisters' files when those Sisters were associated with the activity represented by the documents.

For example:

- General Chapter minutes associated with a Sister were removed from the General Chapter records and placed in that Sister's file.
- Financial or administrative documents were removed from their originating series when a particular Sister had created, signed, or participated in them.
- Records relating to building committees, institutional development, or other organizational activities were redistributed into the files of Sisters who served on those committees.
- Documents authored or represented by an individual Sister were sometimes treated as biographical records even when their provenance was institutional or functional.

This practice occurred repeatedly across the collection.

The result was a substantial separation between **records about a person** and **records created through an institutional function in which that person participated**.

---

## Source-System Inventory

| Source | Format / System | Scope | Authority Level | Location / Path |
|---|---|---|---|---|
| Physical archival collection | Boxes / folders | Entire transferred collection | Primary contextual evidence | HARC Archives: HARC_010 |
| Legacy inventories / spreadsheets | XLSX / CSV | Collection and file-level description | Primary legacy description | Internal server - HARC-1 |
| Existing finding aid | EAD / finding aid | Collection hierarchy | Authoritative descriptive derivative | Internal server - HARC-1 |
| Existing personal / Sisters files | Boxes / folders | Biographical and redistributed material | Primary contextual evidence requiring reconciliation | Internal server - HARC-1 |
| Current ArchivesSpace record | ArchivesSpace | Resource + archival objects | Current system of record | [ArchivesSpace record](https://harc.libraryhost.com/repositories/2/resources/12) |
| Digital files | AWS / preservation storage | Digitized subset | Digital-control evidence | s3://harc-collections/HARC-010 - Our Lady of Victory Missionary Sisters Collection/ |
| NAPWR ingest dataset | CSV / DCTERMS | Public discovery subset | Normalized derivative | s3://harc-collections/HARC-010 - Our Lady of Victory Missionary Sisters Collection/ |

---

# Primary Challenges

The major challenges in the Victory Noll collection were:

- prior removal of records from their originating functional series;
- redistribution of institutional records into individual Sisters' files;
- loss or weakening of provenance relationships;
- conflation of authorship, participation, subject, and archival provenance;
- fragmentation of General Chapter, financial, committee, administrative, and institutional records;
- duplication or partial duplication of intellectual relationships;
- uncertainty about whether some records should remain in Sisters' files or be intellectually restored to their originating series;
- physical order reflecting prior archival intervention rather than necessarily original organizational practice;
- descriptive systems perpetuating earlier redistribution decisions;
- need to preserve evidence of the intervention while reconstructing more accurate archival relationships.

The central archival problem was therefore **contextual fragmentation caused by person-centered redistribution of functionally created records**.

---

# Core Informational Problem

The inherited arrangement frequently operated according to a logic resembling:

```text
Institutional Record
      ↓
Person Associated with Record
      ↓
Moved into Sister's File
```

For example:

```text
General Chapter Minutes
      ↓
Sister Mary Elizabeth participated
      ↓
Minutes removed from General Chapter series
      ↓
Placed in Sister Mary Elizabeth's box
```

or:

```text
Building Committee Records
      ↓
Sister served on committee
      ↓
Documents authored or signed by Sister
      ↓
Removed from committee / institutional records
      ↓
Placed in Sister's personal file
```

This transformed a **provenance-based archival relationship** into a **person-association relationship**.

The distinction is critical.

A record may be:

- created by a Sister;
- signed by a Sister;
- authored by a Sister;
- received by a Sister;
- about a Sister;
- associated with a Sister;

without being a record whose primary archival provenance is that Sister's personal file.

---

# Arrangement and Description

## Principles Applied

- Preserve evidence of prior archival intervention.
- Do not assume inherited physical placement reflects original provenance.
- Distinguish **creator**, **participant**, **subject**, and **record provenance**.
- Restore institutional records intellectually to the function or office that created them when evidence supports doing so.
- Preserve relationships to individual Sisters through agents, subjects, notes, or related-record references rather than by physically or intellectually redefining provenance.
- Retain stable box and folder numbering where practical.
- Avoid unnecessary physical rearrangement when intellectual reconstruction can restore context.
- Document ambiguous cases rather than forcing reassignment.
- Preserve useful legacy references so earlier citations and inventories remain traceable.

---

## Arrangement Decisions

| Area | Legacy / Existing Structure | Action | Result / Rationale |
|---|---|---|---|
| General Chapter records | Minutes or related documents removed from Chapter records and filed with individual Sisters who participated | **Reassign intellectually** | Records restored to the General Chapter context because provenance derives from the governing body, while Sisters remain linked as participants, creators, or subjects where appropriate |
| Financial records | Financial documents placed in Sisters' files because they signed, prepared, or administered them | **Reassign intellectually** | Records mapped back to financial or administrative series when their function was institutional rather than biographical |
| Committee records | Committee documents distributed among files of Sisters who served on the committee | **Reconstruct** | Committee provenance restored; individual Sisters represented through agent relationships or notes |
| Building / property projects | Documents relating to construction or institutional projects placed in personal files of participating Sisters | **Reassign / Map** | Records placed intellectually with property, facilities, administration, or project records depending on function |
| Sisters' files | Personal files contained both genuinely biographical records and records removed from institutional series | **Separate intellectually** | Biographical records retained in Sisters' records; institutional records mapped back to originating function |
| Physical container order | Existing boxes reflected years of prior processing intervention | **Preserve physically where practical** | Intellectual hierarchy corrected without requiring wholesale reboxing or renumbering |
| Legacy references | Earlier inventories may point to redistributed material in Sisters' boxes | **Preserve** | Legacy location/reference retained to support traceability and explain prior arrangement |
| Ambiguous records | Some records could plausibly belong to both personal and institutional contexts | **Deferred / Cross-reference** | No unsupported reassignment; related-record notes or dual access points used where appropriate |

---

# Provenance Versus Personal Association

A central processing distinction for the Victory Noll collection became:

```text
WHO IS ASSOCIATED WITH THE RECORD?
              ≠
WHOSE RECORD IS IT?
```

For example:

A Sister serving on the General Chapter may be an important:

- creator;
- participant;
- correspondent;
- signatory;
- subject;

but the minutes remain records of the **General Chapter**.

Likewise, a Sister who served on a building committee may have written many of the documents, but the records may belong intellectually to:

- the committee;
- central administration;
- property and facilities;
- financial administration;
- institutional planning;

rather than to her biographical file.

This distinction became one of the most important reconciliation rules developed from the collection.

---

# Legacy-to-Normalized Mapping

| Legacy / Local Placement | Type | Normalized Placement / Value | Preserve Variant? | Rationale |
|---|---|---|---:|---|
| General Chapter documents in Sister's file | Governance / Person association | Governance → General Chapter | Yes | Preserve legacy location while restoring functional provenance |
| Financial document in Sister's box | Financial / Administrative | Financial and Legal Records | Yes | Sister may be creator or signatory without being the provenance unit |
| Building committee material in personal file | Committee / Property | Properties and Facilities or Governance, depending on function | Yes | Institutional function takes precedence over personal association |
| Ministry committee documents in Sister's file | Ministry / Committee | Ministry or committee series | Yes | Participation retained through agent/subject access |
| Legacy person-centered placement | Person / Function | Normalized functional placement | Yes | Restore originating context while retaining legacy relationship |

---

# Metadata, Authorities, and Relationships

| Area | Issues / Decisions |
|---|---|
| **Dates** | Existing dates were generally usable, but redistributed records sometimes required contextual comparison with the originating institutional series |
| **Agents / Authorities** | Sisters were linked as creators, participants, correspondents, or subjects rather than used as the sole basis for provenance |
| **Identifiers** | Legacy box/folder references were preserved where needed to maintain traceability to prior inventories |
| **Hierarchy** | Institutional provenance was reconstructed where records had been redistributed according to personal association |
| **Related Records** | Cross-references were used where a Sister's participation remained important to discovery |
| **Digital Objects** | Digital relationships were checked against reconstructed intellectual placement rather than inherited personal-file location alone |
| **Vocabulary** | Governance, committee, administrative, financial, ministry, and property functions were stabilized for consistent mapping |
| **Provenance** | Processing explicitly documented prior intervention and distinguished inherited placement from reconstructed archival context |

---

# Transformation Tools

| Tool / Workflow | Purpose | Input | Output / Result | Version / Notes |
|---|---|---|---|---|
| **Spreadsheet normalization** | Consolidated legacy descriptive data and identified person-centered redistribution patterns | Legacy spreadsheets / inventories | Reconciled working dataset | Project workflow |
| **Hierarchy validation** | Compared existing hierarchy against functional provenance | Spreadsheet / EAD / physical evidence | Corrected parent-child relationships | Essential for identifying redistributed records |
| **ArchivesSpace import preparation** | Prepared reconciled hierarchy for bulk ingest | Normalized dataset | ArchivesSpace-ready import | ArchivesSpace 4.1.1 |
| **Authority reconciliation** | Connected Sisters to records without treating every association as provenance | Agent lists / descriptive data | Reconciled creator, subject, and participant relationships | Human review for ambiguous roles |
| **Date normalization** | Standardized dates where needed | Titles / date fields / record context | Normalized date expressions | Review used when context unclear |
| **Media validation** | Confirmed digital media followed corrected intellectual relationships | Digital-object links / identifiers | Validated media relationships | Applied where digitized |
| **EAD-to-Omeka / NAPWR transformation** | Converted reconciled ArchivesSpace EAD into shared portal schema | EAD XML | Omeka-ready DCTERMS CSV | `RUN_EAD_TO_OMEKA.bat` + `ead_to_omeka.py` |
| **NAPWR ingest validation** | Confirmed corrected relationships were reflected in public discovery | NAPWR CSV | Validated portal records | Shared NAPWR schema |

---

# Adaptive Model Lessons

| Issue Observed | Archivist Decision | Reusable Rule / System Change | Applies Elsewhere? |
|---|---|---|---|
| Institutional records were moved into personal files because a Sister participated in their creation | Separate personal association from archival provenance | Added rule: **person association alone does not determine intellectual placement** | Yes |
| General Chapter records were fragmented among Sisters' files | Restore governance records to their institutional context | Added provenance check for governing-body records appearing within personal files | Yes |
| Committee records followed committee members rather than the committee function | Reconstruct committee provenance | Added committee/function validation during hierarchy review | Yes |
| Financial records followed individual administrators | Map to institutional financial function while retaining agent relationships | Added function-over-person review for administrative and financial records | Yes |
| Physical placement reflected prior processing intervention rather than original order | Preserve physical control while correcting intellectual hierarchy | Reinforced distinction between inherited physical order and evidential original order | Yes |
| Legacy finding aids perpetuated earlier redistribution | Do not treat inherited description as automatically authoritative | Added source-to-source reconciliation before accepting existing hierarchy | Yes |
| Sisters remained important access points after records were restored to institutional series | Retain person relationships through agents, subjects, and cross-references | Added dual-access strategy separating provenance from discoverability | Yes |
| Prior archival processing itself created contextual loss | Document intervention as part of collection history | Added **processing-induced archival drift** as a distinct analytical category | Yes |

---

# New Archival Drift Identified

## Processing-Induced Relational Drift

The Victory Noll case demonstrates a particularly important form of archival drift:

**processing-induced relational drift**.

This occurs when a prior archival intervention changes the relationships among records by reorganizing them according to a logic that differs from the context of their creation.

In this case:

```text
Functional Provenance
      ↓
Prior Archival Intervention
      ↓
Person-Centered Redistribution
      ↓
Fragmented Institutional Context
```

The records remained physically preserved.

Their informational relationships did not.

This distinction is significant because archival loss can occur without a single document being destroyed.

The loss occurred in the **relationships among records**.

---

# Research Significance

The Victory Noll collection provides especially strong evidence for the Linear Reciprocity Model because it demonstrates that archival information loss can be introduced **during archival processing itself**.

The collection was not fundamentally uncontrolled.

Rather, prior processing decisions altered the relationships among otherwise well-preserved records.

## Contribution to the General Framework

| Finding | Research Significance |
|---|---|
| Records were removed from institutional series and redistributed into personal files | Demonstrates that archival intervention can produce relational and provenance drift |
| Personal association was used as a basis for physical and intellectual placement | Shows the importance of distinguishing access relationships from provenance |
| General Chapter records became fragmented | Demonstrates how person-centered arrangement can weaken governance context |
| Committee records followed committee members rather than functions | Shows how functional relationships can disappear even when individual documents survive |
| Existing physical order reflected prior archival intervention | Demonstrates that inherited order is not necessarily original order |
| Existing description could perpetuate earlier processing decisions | Shows that technical or descriptive authority must be evaluated against provenance evidence |
| Corrected intellectual arrangement can coexist with stable physical control | Supports reciprocal management of physical and intellectual systems |
| Person relationships can remain discoverable without controlling provenance | Supports layered access through agents, subjects, related records, and portal search |

---

# Broader Significance

The Victory Noll case adds an important dimension to the project's understanding of archival drift.

In the Most Precious Blood collection, significant context had to be reconstructed because formal descriptive control was largely absent.

In Victory Noll, substantial control existed, but previous processing had **reconfigured the relationships among records**.

These cases therefore represent two different information failures:

```text
MOST PRECIOUS BLOOD
Insufficient inherited descriptive control
        ↓
Contextual reconstruction

VICTORY NOLL
Inherited descriptive control altered provenance
        ↓
Relational reconciliation
```

The Victory Noll case demonstrates that archival preservation cannot be evaluated solely by the survival of documents.

A collection may retain every page and still experience significant informational degradation if records are separated from the functions, offices, committees, or governing bodies that created them.

This supports a central LRM proposition:

> **Archival authenticity depends not only on preserving records, but also on preserving or reconstructing the relationships that give those records meaning.**

The case further demonstrates why downstream access mechanisms should not depend exclusively on physical placement.

A Sister can remain highly discoverable through:

- authority relationships;
- creator fields;
- subject access;
- committee relationships;
- related-record links;
- the Sisters Name Index;
- NAPWR faceted search;
- AI-assisted retrieval;

without removing an institutional record from its proper archival context.

The Victory Noll collection therefore provides a strong example of how **provenance and discoverability can be separated operationally without sacrificing either one**.
