# Sisters of the Most Precious Blood

## Integration Overview

**Congregation:** Sisters of the Most Precious Blood, O'Fallon, Missouri  
**Case slug:** `most-precious-blood`  
**Status:** Active / living documentation  
**Framework:** Linear Reciprocity Model (LRM)  
**Discovery environment:** HARC / NAPWR

This case record documents the integration of the Sisters of the Most Precious Blood collection into the HARC/NAPWR archival environment.

The collection presented a significant departure from cases in which a legacy finding aid, box inventory, or established intellectual hierarchy could be reconciled against the transferred materials. No original finding aid, box-level inventory, or comparable descriptive control documentation accompanied the collection.

A hard drive containing digital files was transferred with the collection, but the files were not organized according to an identifiable archival series structure and did not consistently indicate their relationship to specific physical records or descriptive units.

As a result, processing required substantial reconstruction of archival context from the surviving materials themselves, supplemented where possible by institutional knowledge provided by members of the congregation.

---

## Source-System Inventory

| Source | Format / System | Scope | Authority Level | Location / Path |
|---|---|---|---|---|
| Physical archival collection | Boxes / folders / objects | Transferred physical collection | Primary contextual evidence | HARC Archives: HARC_003 |
| Original finding aid | Not provided | None available | Not available | None |
| Box / folder inventory | Not provided | None available | Not available | None |
| Legacy descriptive spreadsheet | Not provided / not identified | None available | Not available | None |
| Transferred digital files | Hard drive / mixed digital files | Digital subset of collection | Digital-control evidence / contextual evidence | Internal server - HARC-1 |
| Congregational knowledge | Oral / direct identification by Sisters of the Most Precious Blood | Selected materials, particularly artwork | Primary contextual evidence | Document in processing notes / identification records |
| Current processing master | XLSX / CSV | Reconstructed collection description | Secondary working description | s3://harc-collections/HARC-003 - Sisters of the Most Precious Blood Collection/ |
| Current ArchivesSpace record | ArchivesSpace | Resource + archival objects | Current system of record | [ArchivesSpace record](https://harc.libraryhost.com/repositories/2/resources/9) |
| Digital preservation / access files | AWS S3 / preservation storage | Digitized or transferred digital subset | Digital-control evidence | s3://harc-collections/HARC-003 - Sisters of the Most Precious Blood Collection/ |
| NAPWR ingest dataset | CSV / DCTERMS | Public discovery subset | Normalized derivative | s3://harc-collections/HARC-003 - Sisters of the Most Precious Blood Collection/` |

---

## Primary Challenges

The Most Precious Blood collection presented several significant processing and information-system challenges:

- no original finding aid accompanied the transfer;
- no box-level or folder-level inventory was available;
- no inherited intellectual hierarchy could be reliably treated as original arrangement;
- provenance relationships had to be reconstructed from surviving evidence;
- digital files existed without a clear relationship to series, subseries, folders, or physical containers;
- digital filenames and folder structures did not consistently provide archival context;
- some objects, particularly artwork, required identification through congregational knowledge;
- descriptive decisions therefore required a higher level of evidentiary reconstruction than collections with established legacy control;
- normalization could not begin from the assumption that an inherited descriptive system represented the collection accurately.

The primary archival problem was consequently not reconciliation between several competing descriptive structures, but **reconstruction in the absence of sufficient inherited descriptive control**.

---

# Source Condition and Informational Logic

Unlike collections containing established finding aids or inventories, the Most Precious Blood materials did not provide a single inherited intellectual structure that could serve as the baseline for normalization.

The surviving informational environment consisted primarily of:

```text
Physical Materials
        +
Unstructured / Loosely Structured Digital Files
        +
Internal Evidence Within the Records
        +
Congregational Knowledge
        ↓
Reconstructed Archival Context
```

This required the collection to be approached evidentially.

Arrangement and description were derived from the relationships that could be demonstrated through:

- physical grouping;
- folder and object labels;
- record contents;
- names and institutional references;
- dates;
- ministries and activities represented in the materials;
- recurring functions;
- digital filenames and directories where informative;
- relationships among records;
- knowledge supplied by members of the congregation.

Where evidence was insufficient, relationships were documented as uncertain rather than reconstructed speculatively.

---

# Arrangement and Description

## Principles Applied

- No original finding aid was assumed to exist where none was provided.
- An artificial "original order" was not invented to compensate for missing documentation.
- Physical relationships were preserved when they appeared meaningful and stable.
- Existing labels, filenames, inscriptions, and other source evidence were documented before normalization.
- Digital folder structures were treated as evidence only when their organizational meaning could be established.
- Congregational knowledge was incorporated as contextual evidence and documented as such.
- Intellectual hierarchy was reconstructed only when supported by multiple forms of evidence.
- Ambiguous records were described conservatively rather than assigned to unsupported series.
- Standardized HARC structures were used as a stabilization framework, not as evidence of the collection's historical original arrangement.

---

## Arrangement Decisions

| Area | Legacy / Existing Structure | Action | Result / Rationale |
|---|---|---|---|
| Overall collection hierarchy | No original finding aid or documented hierarchy was provided | **Reconstruct** | Intellectual structure was developed from record content, physical evidence, institutional functions, dates, and identifiable relationships rather than from an inherited finding aid |
| Original order | Insufficient documentation existed to establish a complete original order | **Deferred / Reconstruct selectively** | Original order was not claimed where it could not be demonstrated; meaningful surviving relationships were preserved |
| Physical containers | Physical materials retained observable groupings but lacked complete box-level descriptive control | **Preserve + Document** | Existing physical relationships were retained where useful while intellectual control was created separately |
| Series assignment | Records were not consistently identified by series or function | **Map / Reassign** | Materials were assigned to appropriate standardized series only when content and provenance supported the relationship |
| Digital files | Files on transferred hard drive were not consistently arranged by archival series | **Reconcile** | Files were reviewed by content, filename, date, subject, and institutional context before being associated with archival descriptions |
| Digital folder structure | Existing directories did not consistently represent intellectual arrangement | **Do Not Assume** | Directory structure was documented but not automatically converted into archival hierarchy |
| Artwork | Some works lacked sufficient identification in transferred descriptive documentation | **Identify through community knowledge** | Sisters of the Most Precious Blood assisted with identification; those identifications were documented as congregational contextual evidence |
| Ambiguous records | Some materials lacked sufficient evidence for confident placement | **Deferred** | Records were described conservatively and not forced into unsupported intellectual relationships |
| Local terminology | Congregational names, ministries, institutions, and internal terminology appeared within records | **Preserve + Normalize** | Original terminology was retained while standardized values were added where needed for ArchivesSpace and NAPWR interoperability |

---

# Metadata, Authorities, and Digital Objects

| Area | Issues / Decisions |
|---|---|
| **Dates** | Dates were derived from records, filenames, inscriptions, internal evidence, or contextual documentation when clearly supported. Ambiguous dates were not converted into false precision. |
| **Agents / Authorities** | Personal and organizational names were reconciled against existing authority records where possible. Names supplied through congregational identification were documented and reviewed before authority assignment. |
| **Identifiers** | New archival identifiers were required because a comprehensive inherited control system was not available. Any surviving legacy numbers or labels were preserved where found. |
| **Digital Objects** | Hard-drive files required substantial review because they were not consistently tied to archival hierarchy or physical records. Relationships were established only where content, filenames, metadata, or other evidence supported the association. |
| **Artwork** | Identification of artwork relied in part on Sisters of the Most Precious Blood who possessed direct institutional knowledge. These identifications were treated as valuable community-based contextual evidence and documented accordingly. |
| **Vocabulary** | Congregation-specific terminology was retained where historically meaningful and mapped to standardized HARC/NAPWR values where appropriate. |
| **Provenance** | The absence of a finding aid and box inventory made provenance reconstruction especially important. Decisions were based on surviving physical, documentary, digital, and community evidence. |

---

# Digital File Reconstruction

The transferred hard drive represented an important but structurally limited source.

The existence of a digital file did not establish its archival placement.

Files therefore required evaluation using combinations of:

- filename;
- directory;
- embedded metadata when available;
- file creation/modification information where evidentially useful;
- names;
- dates;
- subjects;
- institutions;
- ministries;
- visual content;
- relationship to physical material;
- relationship to other digital files.

A digital directory was not automatically treated as an archival series.

The processing model distinguished:

```text
Storage Organization
        ≠
Archival Intellectual Arrangement
```

Only demonstrated relationships were carried forward into ArchivesSpace or NAPWR.

---

# Community Knowledge and Participatory Identification

One of the most significant contextual resources available during processing was the knowledge of Sisters of the Most Precious Blood themselves.

Members of the congregation assisted with identification of artwork and provided information that was not recoverable from the transferred descriptive documentation alone.

This information was treated as **community-generated contextual evidence**.

The use of congregational knowledge is consistent with the reciprocal approach of the project because the originating community is recognized as possessing informational knowledge that may not exist within formal archival systems.

Where such identifications were used, processing documentation should record:

- material identified;
- name or role of the person providing the identification, when appropriate under institutional documentation practices;
- date of identification;
- nature of the information supplied;
- level of certainty;
- any corroborating evidence.

This prevents valuable community knowledge from becoming another undocumented layer of archival description.

---

# Transformation Tools

| Tool / Workflow | Purpose | Input | Output / Result | Version / Notes |
|---|---|---|---|---|
| **Spreadsheet normalization** | Created structured processing data where inherited tabular control was absent or incomplete | Newly created working inventories / extracted descriptive data | Normalized master dataset | Project workflow |
| **Date extraction and normalization** | Identified defensible dates from record titles, filenames, descriptions, or internal evidence | Titles, filenames, descriptions, records | Standardized date values / review flags | Human review for ambiguous cases |
| **Hierarchy validation** | Checked reconstructed series, subseries, file, and item relationships | Processing master / ArchivesSpace import data | Validated hierarchy and review exceptions | Especially important because no inherited hierarchy was available |
| **ArchivesSpace import preparation** | Converted reconstructed description into ArchivesSpace bulk-ingest structure | Normalized processing dataset | ArchivesSpace-ready import workbook | ArchivesSpace 4.1.1 environment |
| **Authority reconciliation** | Compared identified persons and organizations against existing authorities | Names from records, artwork identification, working data | Reconciled agents and variant names | Ambiguous identities require human review |
| **Media validation** | Reviewed hard-drive files and later digital-object relationships | Hard-drive files / digital inventory / AWS links | Validated media mappings | Digital placement not inferred solely from folder structure |
| **EAD-to-Omeka / NAPWR transformation** | Converted validated archival description into the shared NAPWR discovery schema | ArchivesSpace EAD | Omeka-ready DCTERMS CSV + audit output | `RUN_EAD_TO_OMEKA.bat` + `ead_to_omeka.py` |
| **NAPWR ingest validation** | Verified source links, congregation values, dates, media, and shared fields | NAPWR CSV | Validated portal ingest | Shared NAPWR schema |

### Automation and Review

Automation was applied only after sufficient descriptive structure had been established.

Because this collection lacked a reliable inherited finding aid or inventory, early-stage processing depended heavily on human archival analysis. Automation became more useful after hierarchy, authority relationships, dates, identifiers, and digital associations had been reconstructed sufficiently to support repeatable rules.

---

# Adaptive Model Lessons

| Issue Observed | Archivist Decision | Reusable Rule / System Change | Applies Elsewhere? |
|---|---|---|---|
| No original finding aid or inventory accompanied the collection | Do not fabricate an inherited hierarchy; reconstruct only from available evidence | Added a source-control assessment step that distinguishes **reconciliation** from **archival reconstruction** | Yes |
| Physical materials lacked comprehensive box-level descriptive control | Preserve surviving relationships while creating new intellectual control separately | Added a workflow for collections with insufficient inherited descriptive infrastructure | Yes |
| Digital files existed without reliable series or collection relationships | Do not treat directory structure as archival hierarchy automatically | Added digital-context validation requiring evidence beyond storage location before assigning archival relationships | Yes |
| Digital filenames sometimes supplied useful context but were inconsistent | Use filenames as evidentiary clues, not authoritative description | Added conditional filename-derived metadata rules with human review | Yes |
| Some artwork could not be identified from transferred documentation | Seek and document knowledge from members of the originating community | Added community-knowledge identification as a documented contextual evidence source | Yes |
| Community identifications existed outside formal metadata systems | Record source and certainty of externally supplied identification | Added provenance requirements for participatory/community-generated description | Yes |
| No single source could serve as descriptive authority | Evaluate authority according to the question being answered | Reinforced contextual authority model within Source-System Inventory | Yes |
| Missing documentation increased temptation to impose standardized structure too early | Delay normalization until evidentiary relationships are established | Added an explicit reconstruction-before-normalization rule for low-control collections | Yes |
| Ambiguous records could not always be assigned confidently | Leave unresolved rather than force placement | Added **Deferred** as a formal arrangement decision and validation status | Yes |

---

# Research Significance

The Sisters of the Most Precious Blood collection provides an important test of the Linear Reciprocity Model because it represents a substantially different information condition from collections possessing established finding aids, inventories, or mature archival control systems.

The central problem was not primarily conflict among several inherited descriptive systems.

It was the **absence of sufficient inherited descriptive infrastructure**.

This distinction is significant.

The collection demonstrates that reciprocal archival processing must account not only for competing representations of a collection, but also for situations in which significant portions of the descriptive chain are missing.

## Contribution to the General Framework

| Finding | Research Significance |
|---|---|
| No original finding aid or box inventory was provided | Demonstrates that the framework must support archival reconstruction as well as metadata reconciliation |
| No inherited hierarchy could be treated confidently as original order | Shows the importance of distinguishing preserved original order from retrospectively reconstructed intellectual arrangement |
| Digital files lacked reliable archival placement | Demonstrates that digital storage organization cannot automatically be equated with archival hierarchy |
| Multiple evidence types were necessary to reconstruct context | Supports the LRM principle that archival meaning emerges through reciprocal comparison among physical, digital, descriptive, and human information systems |
| Sisters from the congregation assisted with artwork identification | Demonstrates the continuing informational authority of the originating community and the value of participatory contextual description |
| Community knowledge supplied information absent from formal archival systems | Expands the project's conception of the archival information environment beyond formal metadata and repository systems |
| Ambiguity could not always be resolved | Supports explicit documentation of uncertainty rather than forced normalization |
| Reconstructed control could subsequently support ArchivesSpace and NAPWR | Demonstrates that standardization can follow evidentiary reconstruction without pretending the standardized structure is inherited original order |

## Broader Significance

The Most Precious Blood case broadens the research basis of the HARC/NAPWR project.

Other collections demonstrate how multiple, conflicting, or drifting descriptive environments can be reconciled.

This collection demonstrates what occurs when the archival information chain itself is incomplete.

The processing model therefore must support at least two related but distinct conditions:

```text
MULTIPLE LEGACY SYSTEMS
        ↓
Reconciliation

and

INSUFFICIENT LEGACY CONTROL
        ↓
Contextual Reconstruction
```

Both ultimately require normalization and interoperability, but they begin from fundamentally different evidentiary conditions.

The case also highlights an important extension of the Linear Reciprocity Model: **the originating community itself can function as an active information source within the archival system**.

The Sisters who assisted with identifying artwork were not simply supplementing deficient metadata. They contributed contextual knowledge that had not been successfully transmitted through the formal archival transfer.

That makes the case especially significant for understanding how archival information can persist outside formal descriptive technologies and be reintroduced into the archival system through documented human knowledge.

The collection therefore supports a broader interpretation of reciprocal archival systems in which:

```text
Records
   ⇅
Physical Arrangement
   ⇅
Digital Files
   ⇅
Community Knowledge
   ⇅
Archivist Interpretation
   ⇅
ArchivesSpace / NAPWR
   ⇅
Researcher Discovery
```

The case demonstrates that interoperability depends not simply on transforming metadata, but on first determining what evidence survives, where knowledge resides, and how confidently archival relationships can be reconstructed.
