# Sisters of St. Casimir — Integration Case Record

## Integration Overview

**Congregation:** Sisters of St. Casimir  
**Case slug:** `st-casimir`  
**Status:** Active / living documentation  
**Framework:** Linear Reciprocity Model (LRM)  
**Discovery environment:** HARC / NAPWR

The Sisters of St. Casimir collection arrived with a strong existing finding aid and a relatively standardized intellectual structure that corresponded closely with the HARC descriptive schema. Unlike collections requiring extensive reconstruction or reconciliation, the primary work involved **controlled integration, container renumbering, limited physical reconciliation, and preservation of highly sensitive evidentiary order within the congregation's Cause materials**.

Most series relationships and descriptive structures could be retained with minimal intervention.

A smaller number of packed boxes contained materials that clearly belonged with records in other boxes or series. These discrepancies were generally straightforward to resolve through comparison with the finding aid, record content, and existing arrangement.

A second major consideration involved the congregation's foundress and the ongoing beatification and sainthood process. The collection contains extensive **Cause files, documentation, inventories, notes, and relics assembled as evidence for submission to or review by the Vatican**. These materials were treated as a distinct evidentiary environment and preserved exactly in the order and container relationships in which they were received.

---

## Source-System Inventory

| Source | Format / System | Scope | Authority Level | Location / Path |
|---|---|---|---|---|
| Physical archival collection | Boxes / folders / objects / relics | Entire transferred collection | Primary contextual evidence | HARC Archives: HARC_007 |
| Existing finding aid | Finding aid / EAD / archival description | Entire collection | Authoritative descriptive derivative | Internal server - HARC-1` |
| Legacy box numbering | Physical container system | Entire collection | Primary legacy control | Physical collection / finding aid |
| Cause inventories | Inventories / evidentiary lists | Cause files and relics | Primary evidentiary control | Internal server - HARC-1 |
| Current processing master | XLSX / CSV | Reconciled collection description | Secondary working description | Internal server - HARC-1 |
| Current ArchivesSpace record | ArchivesSpace | Resource + archival objects | Current system of record | [ArchivesSpace record](https://harc.libraryhost.com/repositories/2/resources/6) |
| Digital files | AWS / preservation storage | Digitized subset | Digital-control evidence | s3://harc-collections/HARC-007 - Sisters of Saint Casimir Collection/ |
| NAPWR ingest dataset | CSV / DCTERMS | Public discovery subset | Normalized derivative | s3://harc-collections/HARC-007 - Sisters of Saint Casimir Collection |

---

# Primary Challenges

The St. Casimir collection was comparatively well controlled, but several integration issues required documentation:

- the inherited finding aid was strong and required little structural reconstruction;
- existing series generally corresponded well with the HARC schema;
- legacy box numbering did not correspond with HARC's container-control system;
- some packed materials had been placed in boxes or series other than where the finding aid and content indicated they belonged;
- newly discovered or associated materials needed to be incorporated without disrupting existing HARC numbering;
- the Cause files and relic inventories required preservation of exact evidentiary order;
- no rearrangement of Cause materials could be undertaken merely for descriptive convenience;
- notes, supporting documentation, relics, labels, and inventory relationships required preservation as an integrated evidentiary system.

The principal archival task was therefore **controlled normalization without unnecessary intervention**.

---

# Arrangement and Description

## Principles Applied

- Retain the existing intellectual arrangement wherever it remained accurate and compatible with HARC standards.
- Preserve existing series relationships rather than reconstructing a structure that already functioned effectively.
- Assign HARC container numbers independently from inherited box numbers.
- Maintain traceability between legacy container information and new HARC numbers.
- Add decimal container extensions when later materials belonged intellectually with an existing box sequence.
- Correct obvious packing or placement discrepancies when supported by the finding aid and record content.
- Preserve Cause files, relics, inventories, notes, and associated documentation exactly in their received order.
- Do not physically reorganize evidentiary Cause materials solely to create a cleaner archival arrangement.
- Treat Vatican-oriented inventories and evidentiary relationships as part of the archival context of the materials.

---

## Arrangement Decisions

| Area | Legacy / Existing Structure | Action | Result / Rationale |
|---|---|---|---|
| Series structure | Existing series were already well developed and closely aligned with HARC schema | **Preserve / Map** | Existing intellectual organization retained with only minor normalization |
| Finding aid | Strong and internally coherent | **Preserve** | Used as the principal descriptive baseline for integration |
| Box numbering | Collection arrived with its own box-number sequence | **Renumber for HARC control** | HARC box numbers assigned while legacy numbering was retained for traceability |
| Additional related material | Newly identified material belonged with an already numbered HARC box | **Extend numbering** | Decimal numbering used, e.g. `90` followed by `90.1`, to preserve intellectual and physical continuity without renumbering the entire sequence |
| Mispacked records | Some materials were physically packed with records from another box or series | **Reassign** | Material returned intellectually and, where appropriate, physically to the series or grouping supported by the finding aid and content |
| Cause files | Extensive files maintained as evidence in the foundress's beatification/sainthood process | **Preserve exactly** | Original sequence, notes, folders, and evidentiary relationships retained |
| Relics | Relics corresponded with inventories created for evidentiary purposes | **Preserve exactly** | Relics remained in their received containers and sequence to maintain correspondence with inventories and evidentiary documentation |
| Cause notes and supporting documentation | Notes and associated records accompanied formal Cause materials | **Preserve exactly** | Treated as part of the evidentiary context rather than as miscellaneous processing material |
| Ambiguous Cause relationships | Any uncertainty involving an evidentiary item or inventory relationship | **Deferred** | No rearrangement or reinterpretation without sufficient evidence |

---

# HARC Box Numbering

A significant integration step involved replacing the inherited container numbering with the HARC container-control system while preserving the intellectual arrangement.

The process followed:

```text
Existing Intellectual Arrangement
        ↓
HARC Container Number Assigned
        ↓
Legacy Box Number Preserved as Reference
```

Where additional materials were later identified as belonging with an existing HARC box sequence, the existing numbering was not disturbed.

For example:

```text
HARC Box 90
HARC Box 90.1
HARC Box 90.2
```

This approach allowed new materials to remain associated with the correct intellectual grouping without forcing wholesale renumbering of subsequent containers.

The numbering convention therefore served as a **stabilization mechanism** rather than as a new intellectual arrangement.

---

# Legacy-to-Normalized Mapping

| Legacy / Local Value | Type | Normalized Value | Preserve Variant? | Rationale |
|---|---|---|---:|---|
| Legacy box number | Container control | HARC box number | Yes | Original numbering retained for provenance and cross-reference |
| Existing series title | Series | HARC-aligned series title where needed | Yes | Existing arrangement was already substantially compatible with HARC |
| Cause terminology | Evidentiary / local terminology | Preserve local Cause terminology | Yes | Terminology reflects the formal process and evidentiary context |
| Relic inventory number | Evidentiary identifier | Preserve exactly | Yes | Required to maintain correspondence among relic, inventory, and evidence |
| Local institutional term | Subject / Function / Organization | Normalized value | Yes | Standardization improves interoperability while retaining congregation usage |

---

# Cause Files and Relics

The Cause materials represent a special archival environment within the St. Casimir collection.

These records were assembled in connection with the foundress's beatification and sainthood process and include extensive documentary evidence, inventories, notes, files, and relics.

Their arrangement reflects more than ordinary administrative filing.

The relationship among:

```text
Cause File
   ⇅
Inventory
   ⇅
Supporting Notes
   ⇅
Relic / Evidentiary Object
   ⇅
Vatican-Oriented Documentation
```

constitutes part of the evidentiary meaning of the records.

For that reason, the Cause materials were preserved **exactly as received**.

No attempt was made to:

- simplify their internal arrangement;
- redistribute relics into object-based categories;
- separate notes from associated files;
- consolidate duplicate-looking folders;
- reorganize materials according to the broader HARC series model;
- renumber evidentiary items independently of their inventories.

Where HARC required higher-level container control, that control was added around the inherited evidentiary structure rather than substituted for it.

---

# Evidentiary Order

The St. Casimir Cause materials illustrate an important distinction between ordinary archival arrangement and **evidentiary order**.

In many archival collections, minor physical rearrangement may improve access without significantly affecting meaning.

That assumption cannot automatically be applied to materials assembled as documentary evidence for an external formal process.

Here, sequence and association may themselves carry evidentiary significance.

The processing rule therefore became:

> **Where an inherited order represents an evidentiary relationship, preservation of that relationship takes precedence over descriptive convenience.**

This principle applied to:

- Cause files;
- inventories;
- relics;
- labels;
- notes;
- supporting documentation;
- item numbering;
- container relationships.

---

# Metadata, Authorities, and Digital Objects

| Area | Issues / Decisions |
|---|---|
| **Dates** | Existing descriptive control was generally strong; normalization was applied only where required for system consistency |
| **Agents / Authorities** | Names were reconciled against existing ArchivesSpace authorities while preserving congregation-specific forms where meaningful |
| **Identifiers** | Legacy identifiers and Cause/relic inventory numbers were retained; HARC container numbers were added as a separate control system |
| **Hierarchy** | Existing hierarchy was largely preserved because it already aligned well with the HARC schema |
| **Containers** | HARC numbering was applied without treating numbering changes as intellectual rearrangement |
| **Cause Records** | Existing sequence and evidentiary relationships preserved without normalization that would disrupt context |
| **Relics** | Inventory-to-object relationships preserved exactly |
| **Digital Objects** | Digital materials mapped to the established hierarchy where applicable |
| **Provenance** | Strong inherited description allowed provenance relationships to be preserved with comparatively little reconstruction |

---

# Transformation Tools

| Tool / Workflow | Purpose | Input | Output / Result | Version / Notes |
|---|---|---|---|---|
| **Spreadsheet normalization** | Standardized working data for ingest without materially altering established arrangement | Existing descriptive data | Normalized processing master | Limited intervention required |
| **Hierarchy validation** | Confirmed inherited hierarchy against HARC structure | Finding aid / processing data | Validated series and parent-child relationships | Existing structure largely retained |
| **Container renumbering** | Assigned HARC control numbers and recorded legacy container references | Legacy box sequence | HARC container sequence | Decimal extensions used for later additions |
| **ArchivesSpace import preparation** | Prepared standardized records for HARC ArchivesSpace | Normalized collection data | ArchivesSpace-ready import | ArchivesSpace 4.1.1 |
| **Authority reconciliation** | Matched existing creators and agents to controlled records | Finding aid / agent data | Reconciled authorities | Human review where needed |
| **Media validation** | Verified digital-object relationships | Digital files / archival identifiers | Validated media mappings | Applied where digitized |
| **EAD-to-Omeka / NAPWR transformation** | Converted established archival description into NAPWR discovery structure | EAD XML | Omeka-ready DCTERMS CSV | `RUN_EAD_TO_OMEKA.bat` + `ead_to_omeka.py` |
| **NAPWR ingest validation** | Verified portal values and source relationships | NAPWR CSV | Validated portal ingest | Shared NAPWR schema |

---

# Adaptive Model Lessons

| Issue Observed | Archivist Decision | Reusable Rule / System Change | Applies Elsewhere? |
|---|---|---|---|
| Existing arrangement was already strong and closely aligned with HARC | Avoid unnecessary restructuring | Added principle: **normalization does not require intervention when inherited structure is already valid** | Yes |
| Legacy box numbering differed from HARC control requirements | Assign HARC numbers while preserving legacy numbers separately | Added dual-container-control method | Yes |
| Additional material belonged with an already established HARC box | Extend existing number using decimal notation | Added container-extension convention such as `90.1` rather than renumbering subsequent boxes | Yes |
| Some packed materials belonged to other series or boxes | Use finding aid and content evidence to correct obvious placement errors | Added limited physical-reconciliation step during container validation | Yes |
| Cause files possessed evidentiary order beyond ordinary archival arrangement | Preserve exact inherited sequence | Added **evidentiary-order preservation** as a distinct arrangement rule | Yes |
| Relics corresponded directly with formal inventories | Treat object/inventory relationship as evidentiary metadata | Added validation requirement for relic-to-inventory associations | Yes |
| Notes and seemingly informal material accompanied Cause evidence | Preserve them within the evidentiary context | Added rule against removing or reorganizing contextual notes from formal evidence files | Yes |
| HARC schema could accommodate inherited structure with minimal change | Map rather than reconstruct | Reinforced minimum-necessary-intervention principle | Yes |

---

# Research Significance

The Sisters of St. Casimir collection provides an important contrast to collections requiring extensive reconstruction or relational repair.

The inherited finding aid and arrangement were already comparatively strong and substantially compatible with the HARC schema.

This case therefore demonstrates that the Linear Reciprocity Model does not prescribe intervention for its own sake.

Reciprocity also means recognizing when the source system is already functioning well.

## Contribution to the General Framework

| Finding | Research Significance |
|---|---|
| Existing finding aid was strong and largely compatible with HARC | Demonstrates that reciprocal ingest can result in preservation rather than reconstruction |
| Only limited materials required physical reassignment | Supports proportional intervention based on actual evidence rather than standardized reprocessing |
| HARC container numbering differed from inherited numbering | Demonstrates separation of physical control requirements from intellectual arrangement |
| Decimal box extensions allowed later additions without destabilizing existing numbers | Provides a scalable method for preserving container continuity |
| Cause files were already organized as evidentiary units | Demonstrates that certain inherited structures carry evidentiary significance beyond ordinary filing order |
| Relics corresponded with formal inventories | Expands archival relationship management beyond document-to-document relationships |
| Cause notes, files, inventories, and relics were preserved together | Demonstrates the importance of maintaining multi-format evidentiary context |
| Minimal normalization was sufficient | Supports the LRM principle that systems should adapt to valid source structures rather than unnecessarily remake them |

---

# Broader Significance

The St. Casimir case adds a third distinct condition to the comparative HARC/NAPWR framework.

```text
MOST PRECIOUS BLOOD
Insufficient inherited descriptive control
        ↓
Contextual reconstruction

VICTORY NOLL
Existing arrangement altered by prior processing
        ↓
Relational reconciliation

ST. CASIMIR
Strong inherited arrangement
        ↓
Controlled integration and preservation
```

This comparison is important because it demonstrates that the Linear Reciprocity Model does not assume every collection requires the same treatment.

The appropriate response depends upon the informational condition of the collection.

For St. Casimir, the most responsible intervention was often **not to change the arrangement**.

The major systems work involved:

- adopting HARC container control;
- correcting limited packing discrepancies;
- maintaining legacy references;
- validating hierarchy;
- and protecting the exact evidentiary order of Cause materials.

The Cause files also extend the LRM by demonstrating that archival relationships may possess different levels of evidentiary sensitivity.

Ordinary descriptive normalization can be relatively flexible.

Evidence assembled for a formal ecclesiastical process requires a different threshold.

The case therefore contributes the principle of **evidentiary order preservation**:

> When arrangement, numbering, documentation, and physical association form part of an evidentiary process, those relationships should be treated as archival evidence rather than as incidental container organization.

Within the broader project, St. Casimir demonstrates that reciprocal archival processing includes knowing when to reconstruct, when to reconcile, when to normalize, and when the most responsible action is simply to **preserve an inherited system that is already doing its job well**.
