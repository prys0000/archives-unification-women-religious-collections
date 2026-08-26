# Sisters of Charity of the Blessed Virgin Mary (BVM), Dubuque

## Integration Overview

**Congregation:** Sisters of Charity of the Blessed Virgin Mary (BVM), Dubuque  
**Case slug:** `bvm-dubuque`  
**Status:** Active / living documentation  
**Framework:** Linear Reciprocity Model (LRM)  
**Discovery environment:** HARC / NAPWR

This case record documents the source systems, reconciliation decisions, transformations, exceptions, and reusable lessons identified during integration of the BVM collection.

---

## Source-System Inventory

| Source | Format / System | Scope | Authority Level | Location / Path |
|---|---|---|---|---|
| Physical archival collection | Boxes / folders | Entire transferred collection | Primary contextual evidence | `HARC Archives: HARC_001` |
| Legacy collection inventory | XLSX | Collection and file-level description | Primary legacy description | Internal server - HARC-1 |
| Existing finding aid | EAD XML | Collection hierarchy | Authoritative descriptive derivative | `[path]` | Internal server - HARC-1 |
| Current ArchivesSpace record | ArchivesSpace | Resource + archival objects | Current system of record | [ArchivesSpace record](https://harc.libraryhost.com/repositories/2/resources/3) |
| Digital files | AWS S3 | Digitized subset | Digital-control evidence | `[s3://harc-collections/HARC-001 - Sisters of Charity of the Blessed Virgin Mary Collection/]` |
| NAPWR ingest dataset | CSV / DCTERMS | Public discovery subset | Normalized derivative | `[s3://harc-collections/HARC-001 - Sisters of Charity of the Blessed Virgin Mary Collection/]` |

---

## Primary Challenges

Record only those present in this collection:

- inconsistent or legacy spreadsheet structures
- mixed or flattened hierarchy
- descriptive and vocabulary drift
- physical/intellectual arrangement mismatch
- legacy identifiers
- incomplete or inconsistent dates
- agent or creator inconsistencies
- EAD / ArchivesSpace transformation issues
- digital-object or media mismatches
- encoding or technical errors
- provenance gaps

---

## Arrangement and Description

### Principles

- Preserve existing box and folder numbering whenever viable.
- Do not rearrange physical materials solely to match a normalized hierarchy.
- Preserve meaningful local ministry, administrative, and institutional terminology.
- Base hierarchy changes on physical, documentary, or provenance evidence.
- Document ambiguity rather than forcing unsupported decisions.
- Standardize for interoperability without erasing congregation-specific context.

### Decisions

| Area | Legacy / Existing Structure | Action | Result / Rationale |
|---|---|---|---|
| Series / subseries | Records grouped under broad local administrative headings that overlapped in function | Preserve / Map | Retained the original heading as contextual metadata while mapping records into the standardized HARC series/subseries structure for consistency and discovery |
| Physical order | Box order preserved | Preserve No Change | Physical arrangement was retained because box and folder numbering remained stable; intellectual relationships were corrected in ArchivesSpace without unnecessary physical rearrangement |
| Container numbering | Existing box and folder numbers were already in active use and referenced in legacy documentation | Preserve | Numbers were preserved to maintain continuity with the physical collection and previous inventories |
| Broad subject columns | Spreadsheet columns represented topics such as education, missions, administration, or healthcare rather than true metadata fields | Restructure | Topic columns were converted into subject/function values so the spreadsheet represented one archival record per row |
| Local terminology | Congregation-specific administrative or ministry terms differed from standardized archival terminology | Preserve + Normalize | Local terminology was retained as a variant or contextual value while a normalized form was used for shared searching |

---

## Metadata, Authorities, and Digital Objects

| Area | Issues / Decisions |
|---|---|
| **Dates** | Missing dates, dates recovered from titles/descriptions, ambiguous expressions, normalization rules |
| **Agents / Authorities** | Existing agents, duplicate candidates, variant names, congregation-specific naming practices |
| **Identifiers** | Legacy identifiers, normalized IDs |
| **Digital Objects** | Primary files, thumbnails, access restrictions |
| **Vocabulary** | Local terminology, authorized forms, preserved variants |
| **Provenance** | Source tracking, prior processing evidence |

---

## Transformation Tools

The following tools and scripted workflows were used during collection reconciliation, normalization, ingest, and publication.

| Tool / Workflow | Purpose | Input | Output / Result | Version / Notes |
|---|---|---|---|---|
| **Spreadsheet normalization** | Consolidated legacy spreadsheets, corrected field structures, removed invalid formatting, and prepared one-record-per-row working data | XLSX / CSV legacy inventories | Normalized master spreadsheet / CSV | Project workflow; version as used |
| **Encoding repair** | Corrected corrupted characters and legacy encoding problems such as `Ã¢â‚¬â€œ` | CSV / XLSX text fields | UTF-8 normalized data | Applied during preprocessing |
| **Date extraction and normalization** | Identified missing date expressions and extracted defensible dates from titles or descriptions | Titles, descriptions, legacy date fields | Standardized date expressions for ArchivesSpace and NAPWR | Automated where unambiguous; ambiguous dates reviewed manually |
| **Hierarchy validation** | Checked series, subseries, file, box, and folder relationships and identified missing or incorrect parent-child relationships | Normalized spreadsheet / ArchivesSpace import data | Corrected hierarchical ingest structure | Box and folder numbers preserved where valid |
| **ArchivesSpace import preparation** | Converted reconciled collection data into the required ArchivesSpace bulk-import structure and validated required fields | Normalized XLSX / CSV | ArchivesSpace-ready import workbook | ArchivesSpace **4.1.1** environment |
| **Authority reconciliation** | Compared creators and agents against existing ArchivesSpace authority records to prevent duplicate person or organization records | Creator / agent values + existing authority list | Reconciled agent assignments and variant-name review | Human review used for ambiguous matches |
| **Media validation** | Checked digital-object URLs, primary files, thumbnails, duplicates, and relationships between media and archival records | Digital-object inventory / AWS links / archival identifiers | Validated media mappings and corrected links | AWS-hosted files where applicable |
| **EAD-to-Omeka / NAPWR transformation** | Parsed ArchivesSpace EAD and transformed selected archival components into the standardized NAPWR DCTERMS schema | EAD XML | Omeka-ready CSV + audit / warning output | `RUN_EAD_TO_OMEKA.bat` + `ead_to_omeka.py` |
| **NAPWR ingest validation** | Verified field order, repository/congregation values, source URLs, digital media, and shared discovery metadata prior to publication | NAPWR DCTERMS CSV | Validated Omeka S import dataset | Shared 15-field NAPWR schema |

### Automation and Review

Automation was used for repeatable transformations such as field normalization, encoding repair, date detection, hierarchy checking, media validation, and schema conversion. Decisions involving ambiguous identity, arrangement, provenance, or uncertain dates remained subject to archivist review.

**System version:** ArchivesSpace 4.1.1  
**Script versions:** Record GitHub release, commit, or local version when available.

---

## Adaptive Model Lessons

| Issue Observed | Archivist Decision | Reusable Rule / System Change | Applies Elsewhere? |
|---|---|---|---|
| Dates were frequently present in titles but missing from the formal date field | Extract dates only when the title contains a clear, defensible date expression | Added date-detection logic that flags unambiguous title dates for normalization and sends ambiguous cases to review | Yes |
| Legacy spreadsheets contained subjects or ministries as separate columns rather than metadata values | Treat these columns as topical/function values rather than true fields | Added spreadsheet-normalization rules to unpivot false metadata columns into standardized subject/function values | Yes |
| Existing creator names did not always match ArchivesSpace agent records exactly | Reconcile against existing agents before creating new authorities | Added authority-matching step using normalized names and selected biographical fields; ambiguous matches require human review | Yes |
| Physical box order did not always match the intellectual hierarchy | Preserve stable box/folder numbering while correcting intellectual relationships separately | Added hierarchy-validation procedure that distinguishes physical control from intellectual arrangement | Yes |
| Multiple legacy terms represented the same ministry or administrative function | Preserve the original term while mapping it to a standardized discovery value | Added legacy-to-normalized vocabulary mapping with retained variants | Yes |
| EAD exported technically valid hierarchy but omitted some useful local context | Preserve selected legacy terms and relationships during transformation to later systems | Updated EAD-to-NAPWR mapping to retain contextual values rather than relying only on formal hierarchy | Yes |
| Digital records contained both primary files and thumbnail derivatives | Prefer the documented thumbnail for portal display while preserving the primary-file relationship | Added media-selection and validation logic to distinguish derivatives from source files | Yes |
| Duplicate media relationships appeared during Omeka ingest | Verify record/media pairs before publication | Added duplicate-media validation by archival identifier and media URL | Yes |
| Character corruption appeared in legacy CSV/XLSX data | Repair known encoding patterns before ingest | Added UTF-8 normalization and known-character repair to preprocessing | Yes |
| A local term could not be mapped confidently to a shared vocabulary | Preserve the local value and defer normalization | Added an exception class for unresolved semantic mappings rather than forcing a standardized term | Yes |
| Parent-child relationships were implicit rather than encoded | Reconstruct hierarchy only when supported by titles, sequence, container data, or finding-aid evidence | Added hierarchy-reconstruction rules plus a manual-review flag for uncertain relationships | Yes |
| Public portal search exposed duplicate or inconsistent values that were not obvious during backend processing | Treat discovery behavior as QA evidence | Added portal spot-checking to the validation workflow so later discovery can trigger previous metadata correction | Yes |

---

## Research Significance

The BVM collection reinforces the broader finding that archival environments frequently contain multiple overlapping descriptive systems rather than a single authoritative structure. Physical arrangement, legacy spreadsheets, finding aids, ArchivesSpace records, and digital-object systems may each preserve different aspects of the collection's informational history.

The processing actions demonstrates that successful ingest requires more than technical conversion. It requires comparison among source systems, preservation of provenance, reconstruction of hierarchy, semantic normalization, and explicit documentation of archival decisions.

The collection also contributes evidence for the Linear Reciprocity Model by showing that workflow control systems can identify and prevent potential issues or barriers. Issues identified during ArchivesSpace ingest, digital-object validation, or NAPWR discovery can reveal earlier inconsistencies in hierarchy, terminology, authority control, dates, or source description.

### Contribution to the General Framework

| Finding | Research Significance |
|---|---|
| Multiple descriptive environments existed for the same collection | Supports the LRM argument that archival information systems must be reconciled rather than treated as a simple source-to-destination migration |
| Legacy terminology remained meaningful after normalization | Supports semantic alignment without descriptive flattening |
| Physical and intellectual arrangements did not always correspond exactly | Demonstrates the need for reciprocal comparison between physical evidence and archival description |
| Repeated metadata problems could be converted into reusable rules | Supports the adaptive learning model and institutional computational memory |
| Public discovery exposed issues not obvious during backend processing | Supports the idea that access systems can function as quality-assurance feedback |
| The same problem classes appeared in other congregational collections | Provides evidence that the framework may be generalizable beyond a single collection |

### Broader Significance

The value of the case lies not only in the successful integration of one congregational archive, but in its contribution to a comparative body of evidence across women religious collections.

As additional congregation case records are completed, recurring patterns can be evaluated systematically. This allows the project to distinguish between:

- problems unique to one collection;
- problems common to several repositories;
- and structural barriers characteristic of distributed archival information systems.

That distinction strengthens the research basis of the Linear Reciprocity Model and the HARC/NAPWR interoperability framework.
