# Sisters of St. Francis of the Holy Cross — Integration Case Record

## Integration Overview

**Congregation:** Sisters of St. Francis of the Holy Cross  
**Case slug:** `st-francis-holy-cross`  
**Status:** Active / living documentation  
**Framework:** Linear Reciprocity Model (LRM)  
**Discovery environment:** HARC / NAPWR

The Sisters of St. Francis of the Holy Cross collection arrived in very strong condition.

The collection is comparatively small, and the accompanying inventory was thorough, coherent, and already suitable for integration with HARC systems. Physical boxes were well organized, descriptive control was strong, and minimal intellectual or structural remediation was required.

The collection also includes a substantial group of maps and architectural blueprints. These materials were well organized descriptively but require improved physical housing and preservation support because of their size and format.

The principal archival task was therefore **controlled integration with minimal intervention**, combined with targeted preservation work for oversize materials.

---

## Source-System Inventory

| Source | Format / System | Scope | Authority Level | Location / Path |
|---|---|---|---|---|
| Physical archival collection | Boxes / folders | Entire transferred collection | Primary contextual evidence | HARC Archives: HARC_005 |
| Existing inventory | XLSX / CSV / finding aid | Entire collection | Primary legacy description | Internal server - HARC-1 |
| Map and blueprint inventory | Inventory / descriptive list | Oversize maps and architectural records | Primary legacy description | Internal server - HARC-1 |
| Physical map / blueprint collection | Oversize paper records | Architectural and geographic materials | Primary contextual evidence | HARC-Stacks |
| Current processing master | XLSX / CSV | Integrated collection description | Secondary working description | s3://harc-collections/HARC-005 - Sisters of Saint Francis of the Holy Cross Collection/ |
| Current ArchivesSpace record | ArchivesSpace | Resource + archival objects | Current system of record | [ArchivesSpace record](https://harc.libraryhost.com/repositories/2/resources/7) |
| Digital files | AWS / preservation storage | Digitized subset, where applicable | Digital-control evidence | s3://harc-collections/HARC-005 - Sisters of Saint Francis of the Holy Cross Collection/ |
| NAPWR ingest dataset | CSV / DCTERMS | Public discovery subset | Normalized derivative | s3://harc-collections/HARC-005 - Sisters of Saint Francis of the Holy Cross Collection/ |

---

# Primary Challenges

The St. Francis collection presented few major descriptive or structural problems.

Primary considerations were:

- the collection was small and already well organized;
- the existing inventory was thorough and dependable;
- box-level control was already stable;
- hierarchy and descriptive structure required little correction;
- existing arrangement could be retained with minimal intervention;
- maps and blueprints were well organized intellectually but required improved physical housing;
- oversize materials required preservation attention without disrupting established descriptive relationships;
- any normalization was primarily technical or system-oriented rather than corrective.

The principal archival task was therefore **integration rather than reconstruction**.

---

# Arrangement and Description

## Principles Applied

- Preserve the existing intellectual arrangement wherever it remained accurate.
- Avoid unnecessary restructuring of a collection that already possessed strong descriptive control.
- Retain stable box numbering and folder relationships.
- Map existing description into HARC and NAPWR structures with minimal semantic intervention.
- Treat oversize maps and blueprints as a preservation and housing issue rather than as an arrangement problem.
- Maintain links between oversize materials and their intellectual context even if physical storage changes.
- Document any rehousing or relocation so researchers can continue to identify related records reliably.

---

## Arrangement Decisions

| Area | Legacy / Existing Structure | Action | Result / Rationale |
|---|---|---|---|
| Overall hierarchy | Strong, coherent, and already well organized | **Preserve** | No significant restructuring required |
| Series / subseries | Existing structure fit HARC descriptive needs with little modification | **Preserve / Map** | Existing intellectual arrangement retained |
| Box numbering | Boxes arrived with usable and stable control | **No Change / Map** | Existing physical control preserved where compatible with HARC |
| Folder relationships | Existing folders corresponded well with inventory | **Preserve** | No need for reconstruction |
| Descriptive inventory | Thorough and internally consistent | **Preserve / Normalize minimally** | Used as principal basis for ArchivesSpace integration |
| Maps | Intellectually organized but physically oversize | **Preserve intellectually / Rehouse physically** | Descriptive relationships retained while physical housing is improved |
| Blueprints | Well organized but require preservation-quality oversize storage | **Preserve intellectually / Rehouse physically** | Physical preservation improved without changing archival context |
| Oversize relocation | Some materials may require movement to map cases or flat storage | **Cross-reference** | Intellectual placement remains unchanged; physical location updated through container/location notes |
| Metadata normalization | Minor differences required for HARC/NAPWR interoperability | **Normalize minimally** | Technical standardization without unnecessary alteration of source description |

---

# Maps and Blueprints

The map and blueprint component is the principal area requiring additional physical intervention.

These materials were already well organized and did not require intellectual reconstruction.

The primary need is **preservation-oriented rehousing**.

The guiding relationship is:

```text
Existing Intellectual Arrangement
        ↓
Preserve Description and Identifiers
        ↓
Rehouse Oversize Material
        ↓
Update Physical Location Control
```

Physical relocation should not be interpreted as intellectual rearrangement.

Where maps or blueprints are moved from standard boxes into:

- flat files;
- map cases;
- oversize folders;
- protective enclosures;
- rolled-storage systems where appropriate;

their relationship to the original series, folder, project, building, or institutional context should remain explicit in ArchivesSpace and related inventories.

---

# Legacy-to-Normalized Mapping

Because the inherited description was already strong, only limited normalization should be necessary.

| Legacy / Local Value | Type | Normalized Value | Preserve Variant? | Rationale |
|---|---|---|---:|---|
| Existing series title | Series | HARC-equivalent series title if needed | Yes | Existing terminology already meaningful and structurally sound |
| Existing box number | Container | HARC container value where required | Yes | Preserve legacy traceability |
| Building / property name | Place / Institution | Authorized or normalized form | Yes | Standardized discovery while preserving historical usage |
| Map title | Title | Standardized descriptive title only if necessary | Yes | Original title remains evidentiary and useful |
| Blueprint designation | Resource type | Blueprint / Architectural Drawing | Yes | Supports consistent discovery without altering source description |

---

# Metadata, Authorities, and Digital Objects

| Area | Issues / Decisions |
|---|---|
| **Dates** | Existing date information was generally reliable; only minor normalization required |
| **Agents / Authorities** | Existing creator and organizational names reconciled against HARC authority structures where needed |
| **Identifiers** | Existing identifiers retained wherever stable |
| **Hierarchy** | Strong inherited hierarchy largely preserved |
| **Containers** | Existing box control retained; oversize location notes added where rehousing occurs |
| **Maps / Blueprints** | Intellectual relationships preserved while physical housing is improved |
| **Digital Objects** | Digital files, if present, linked to established descriptions rather than requiring major reconstruction |
| **Vocabulary** | Minimal normalization for HARC/NAPWR interoperability |
| **Provenance** | Strong descriptive and physical control reduced the need for significant provenance reconstruction |

---

# Transformation Tools

| Tool / Workflow | Purpose | Input | Output / Result | Version / Notes |
|---|---|---|---|---|
| **Spreadsheet normalization** | Standardized minor formatting and field differences | Existing inventory | HARC-ready working dataset | Minimal intervention |
| **Hierarchy validation** | Confirmed existing series, file, and container relationships | Inventory / processing data | Validated hierarchy | Few corrections expected |
| **ArchivesSpace import preparation** | Prepared well-structured descriptive data for ingest | Existing inventory / normalized dataset | ArchivesSpace-ready import | ArchivesSpace 4.1.1 |
| **Authority reconciliation** | Matched existing names and organizations to HARC authority records | Inventory / agent data | Reconciled authority values | Limited remediation |
| **Date normalization** | Standardized date formatting where required | Existing date fields | Normalized date expressions | Minor use |
| **Media validation** | Verified digital-object links where present | Digital files / identifiers | Validated media relationships | Applied as needed |
| **EAD-to-Omeka / NAPWR transformation** | Converted validated ArchivesSpace description into shared portal metadata | EAD XML | Omeka-ready DCTERMS CSV | `RUN_EAD_TO_OMEKA.bat` + `ead_to_omeka.py` |
| **NAPWR ingest validation** | Confirmed shared portal values and source relationships | NAPWR CSV | Validated portal ingest | Shared NAPWR schema |

---

# Adaptive Model Lessons

| Issue Observed | Archivist Decision | Reusable Rule / System Change | Applies Elsewhere? |
|---|---|---|---|
| Collection arrived with strong descriptive and physical control | Avoid unnecessary restructuring | Reinforced minimum-intervention principle for well-organized incoming collections | Yes |
| Existing inventory was already thorough and reliable | Use inherited description as primary baseline | Added decision rule allowing direct mapping when source description passes structural validation | Yes |
| Box control was stable | Preserve existing numbering where compatible | Reinforced rule that HARC normalization does not require renumbering when control is already effective | Yes |
| Maps and blueprints were intellectually sound but physically vulnerable | Separate preservation intervention from intellectual rearrangement | Added oversize-rehousing workflow that retains existing descriptive relationships | Yes |
| Physical relocation may occur during rehousing | Update location control without changing hierarchy | Added cross-reference requirement for relocated oversize material | Yes |
| Minimal metadata normalization was needed | Do not over-process well-structured collections | Reinforced proportional-intervention principle | Yes |

---

# Research Significance

The Sisters of St. Francis of the Holy Cross collection provides another important comparative case because it demonstrates a collection requiring **very little intellectual remediation**.

The collection arrived with:

- strong descriptive control;
- a thorough inventory;
- stable box organization;
- reliable hierarchy;
- well-organized oversize materials.

The principal need was preservation-oriented rehousing of maps and blueprints rather than reconstruction of archival relationships.

## Contribution to the General Framework

| Finding | Research Significance |
|---|---|
| Existing description was already strong | Demonstrates that reciprocal ingest can function primarily as validation and integration |
| Physical boxes were ready for use | Shows that source systems should be preserved when they already provide effective control |
| Minimal hierarchy correction was required | Supports proportional intervention rather than uniform reprocessing |
| Maps and blueprints were intellectually organized but physically vulnerable | Demonstrates separation between intellectual arrangement and physical preservation needs |
| Oversize rehousing can occur without changing archival hierarchy | Supports reciprocal management of physical and intellectual control |
| Only limited normalization was necessary | Demonstrates that interoperability does not require extensive transformation when source data is already compatible |

---

# Broader Significance

The St. Francis collection strengthens the comparative HARC/NAPWR framework because it represents a low-friction integration case.

The developing comparison now includes several distinct archival conditions:

```text
MOST PRECIOUS BLOOD
Insufficient inherited descriptive control
        ↓
Contextual reconstruction

VICTORY NOLL
Prior processing disrupted provenance
        ↓
Relational reconciliation

ST. CASIMIR
Strong inherited arrangement + specialized evidentiary records
        ↓
Controlled integration and evidentiary preservation

ST. FRANCIS OF THE HOLY CROSS
Strong inventory + stable physical control
        ↓
Minimal intervention and preservation-focused integration
```

The St. Francis case is significant precisely because comparatively little corrective work was required.

It demonstrates that the Linear Reciprocity Model should not be measured by the amount of transformation it produces.

A successful reciprocal ingest may involve substantial reconstruction.

It may involve relational repair.

Or it may involve recognizing that the inherited archival system is already functioning effectively and should be changed as little as possible.

The collection therefore supports a principle of **proportional intervention**:

> **The degree of archival intervention should correspond to the degree of demonstrated informational need.**

The maps and blueprints further demonstrate that **preservation need and descriptive need are not the same thing**.

A collection can be intellectually sound while still requiring significant physical preservation work.

For HARC/NAPWR, this case confirms that standardization should be selective, evidence-based, and respectful of well-functioning source systems.
