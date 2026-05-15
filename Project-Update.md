# Operationalizing the Linear Reciprocity Model Through Archival Ingest and Reconciliation at HARC

## Introduction

The ingest and reconciliation process undertaken for the Our Lady of Victory Missionary Sisters (OLVM) collections demonstrates a practical implementation of the Linear Reciprocity Model (LRM) within a live archival environment. The issues encountered throughout this process—including inconsistent spreadsheets, flattened metadata structures, conflicting descriptive systems, and mismatches between physical and intellectual arrangement—represent the exact forms of archival friction and information barriers the LRM was designed to identify and resolve.

This framework formalizes the operational process HARC can use when ingesting collections from external repositories, congregations, ministries, and partner institutions. Rather than treating archival ingest as a simple metadata transfer process, the framework recognizes ingest as a reciprocal restructuring event between:

1. The originating archival culture and intellectual system
2. The receiving archival information system
3. The physical collection itself
4. The descriptive technologies used to mediate access
5. The archivists and users interacting with the system

The OLVM project illustrates how the preservation of original order, reconciliation of legacy descriptive systems, and normalization into modern archival standards can occur simultaneously without destroying contextual meaning.

---

# Core Problem Identified During OLVM Ingest

## Initial Condition

The OLVM materials arrived with multiple overlapping descriptive environments:

### 1. Physical Original Order

The physical boxes were arranged primarily by apostolate and functional ministry:

```text
Apostolate → File Unit → Mixed Contents
```

Examples included:

- Catechetics
- Community Outreach (COR)
- Cherish the Earth
- Foreign Missions
- Education

The labels reflected lived organizational structures and operational ministry functions developed internally by the congregation.

---

### 2. Legacy Spreadsheet Structures

The spreadsheets received from external custodians reflected multiple generations of descriptive practice.

Problems identified included:

- Mixed hierarchical levels in single rows
- Subjects incorrectly transformed into columns
- Apostolates represented as both fields and values
- Multiple spreadsheets created by different individuals
- Inconsistent controlled vocabularies
- Flattened contextual relationships
- Descriptive drift over time
- Duplicate semantic columns (e.g., Bolivia, Corporal)
- Lack of normalized identifiers

The spreadsheets did not represent archival records in a structurally valid relational format.

---

### 3. Existing EAD/ArchivesSpace Structures

The EAD represented a later-stage processing environment in which the original apostolate-centered order had been partially dissolved and redistributed into formal archival series:

```text
Series → Subseries → File → Box
```

While technically compliant with archival standards, the EAD obscured portions of the congregation’s original operational logic and functional relationships.

---

# The Linear Reciprocity Model in Practice

## Foundational Principle

The Linear Reciprocity Model proposes that archival information systems should not impose unilateral descriptive control over collections. Instead, systems must reciprocally adapt to the originating informational logic of collections while simultaneously normalizing metadata for long-term management, interoperability, and access.

The OLVM ingest demonstrates that archival processing should be understood as:

> A reciprocal negotiation between legacy organizational structures and modern archival systems.

Rather than replacing legacy systems outright, the ingest process captures, preserves, maps, and reconciles them.

---

# The HARC Ingest and Reconciliation Framework

## Stage 1 — Preservation of Original Informational Context

### Goal

Preserve all original informational structures before normalization begins.

### Operational Actions

- Preserve original spreadsheets intact
- Preserve physical box labels through photography and transcription
- Preserve original folder structures
- Preserve original descriptive terminology
- Preserve legacy identifiers
- Preserve original intellectual arrangement patterns

### LRM Principle

The originating informational environment contains embedded contextual meaning and organizational logic that cannot be reconstructed after normalization.

### OLVM Example

The apostolate labels:

```text
CATECHETICS 3
CHERISH THE EARTH 3
COR – North Miami
```

were treated as evidence of a legacy intellectual arrangement system rather than informal notes.

---

# Stage 2 — Unified Data Consolidation

## Goal

Create a single source of truth while preserving provenance.

### Operational Actions

- Merge all spreadsheets into a unified dataset
- Preserve source tracking:
  - Source file
  - Source worksheet
  - Source row
- Preserve raw row text
- Preserve positional data

### LRM Principle

Reciprocal systems require preservation of provenance at every transformation stage.

### OLVM Example

A unified master workbook was created containing:

- Raw original rows
- Source metadata
- Original text combinations
- Normalized archival fields

No original information was deleted during reconciliation.

---

# Stage 3 — Structural Normalization

## Goal

Convert invalid or flattened data structures into archival record-level structures.

### Operational Actions

- Identify false columns
- Unpivot subject columns into rows
- Convert one-dimensional spreadsheets into hierarchical structures
- Normalize record granularity
- Standardize field relationships

### LRM Principle

Systems must adapt structurally to the informational logic embedded in the collection rather than forcing incompatible structures onto the data.

### OLVM Example

Columns such as:

- Bolivia
- Corporal
- Healthcare
- Education

were determined not to be true metadata fields, but rather topical or functional descriptors incorrectly converted into spreadsheet columns.

The normalized structure became:

```text
One Row = One Archival Record
```

instead of:

```text
One Column = One Program or Subject
```

---

# Stage 4 — Legacy Intellectual Structure Preservation

## Goal

Preserve original arrangement systems alongside normalized archival hierarchy.

### Operational Actions

Create parallel fields such as:

- Legacy Apostolate
- Legacy File Unit Number
- Legacy Box Number
- Original Label Transcription
- Program or Activity

### LRM Principle

Normalization should not erase originating informational relationships.

### OLVM Example

The original apostolate structure was preserved as a parallel descriptive layer:

```text
Apostolate → File Unit → Contents
```

while simultaneously mapping materials into:

```text
Series → Subseries → File
```

This created a dual-context archival model.

---

# Stage 5 — Reconciliation Between Physical and Intellectual Systems

## Goal

Create reciprocal links between physical materials and descriptive systems.

### Operational Actions

- Assign standardized Box_IDs
- Build box reconciliation indexes
- Link EAD components to physical materials
- Preserve legacy numbering systems
- Create verification workflows

### LRM Principle

Physical arrangement and intellectual arrangement must reciprocally reinforce one another.

### OLVM Example

A reconciliation dashboard was developed to allow archivists to:

- Open physical boxes
- Compare labels to EAD descriptions
- Identify legacy apostolate relationships
- Verify mismatched or redistributed records
- Document archival drift

This process exposed the degree to which the existing EAD had separated materials from their original contextual relationships.

---

# Stage 6 — Controlled Vocabulary and Semantic Stabilization

## Goal

Create stable descriptive systems while preserving historical terminology.

### Operational Actions

- Build controlled apostolate vocabularies
- Standardize document types
- Normalize locations
- Reconcile synonymous terms
- Preserve original terms in parallel fields

### LRM Principle

Descriptive control should stabilize access without erasing historical semantics.

### OLVM Example

Terms such as:

- COR
- Community Outreach
- Community Outreach (COR)

were normalized into controlled values while retaining original terminology for contextual interpretation.

---

# Stage 7 — EAD and ArchivesSpace Reconstruction

## Goal

Generate new archival descriptive systems from normalized reciprocal structures.

### Operational Actions

- Rebuild hierarchical EAD structures
- Generate ArchivesSpace ingest spreadsheets
- Create parent-child relationships
- Restore missing contextual hierarchy
- Link digital and physical control systems

### LRM Principle

Archival systems should emerge from reconciled informational environments rather than forcing collections into rigid pre-existing structures.

### OLVM Example

The rebuilt EAD structure incorporated:

- Series
- Subseries
- File-level records
- Legacy apostolate relationships
- Box reconciliation data
- Source provenance tracking

This produced a significantly more contextually accurate archival description than the original flattened EAD.

---

# Archival Drift and Informational Degradation

## Observed During OLVM Processing

The project exposed multiple forms of archival drift:

### Structural Drift

Original apostolate systems were flattened into administrative hierarchies.

### Semantic Drift

Terms evolved inconsistently across spreadsheets and descriptive environments.

### Relational Drift

Physical and intellectual relationships became disconnected.

### Technological Drift

Spreadsheet structures were created around software convenience rather than archival logic.

### Provenance Drift

Original descriptive decisions became obscured over time.

---

# Why Traditional Archival Ingest Often Fails

Traditional ingest workflows often assume:

- incoming data is structurally valid
- spreadsheets are relationally coherent
- EAD accurately reflects original order
- normalization should replace legacy systems

The OLVM process demonstrates these assumptions are frequently incorrect.

Collections created outside centralized archival systems often contain:

- embedded local organizational logic
- functional rather than hierarchical arrangement
- mixed descriptive paradigms
- iterative community-created metadata
- evolving vocabularies

Ignoring these realities creates archival paralysis, contextual loss, and discoverability failures.

---

# HARC’s Reciprocal Ingest Philosophy

The HARC framework therefore proposes:

## The archival system should adapt to the collection before the collection adapts to the archival system.

This does not reject standards.

Instead, it:

- delays premature flattening
- preserves contextual evidence
- builds reciprocal mappings
- allows normalization to occur without informational destruction

---

# Practical Outcomes for HARC

Using this framework allows HARC to:

## 1. Preserve Original Community Knowledge

The lived informational systems created by women religious remain visible and searchable.

---

## 2. Scale Ingest Across Distributed Repositories

Collections arriving from multiple congregations can be normalized into shared systems while preserving local context.

---

## 3. Reduce Archival Paralysis

Instead of attempting perfect structure immediately, HARC can ingest collections iteratively while maintaining reciprocal links between systems.

---

## 4. Improve ArchivesSpace and Omeka Integration

Normalized structures support:

- EAD generation
- ArchivesSpace ingest
- Omeka indexing
- public portal access
- faceted searching
- future AI-assisted discovery

---

## 5. Support Long-Term Interoperability

Parallel preservation of original and normalized structures enables future reinterpretation, migration, and system evolution.

---

# Project Update — OLVM Collection Ingest, Reconciliation, and the Linear Reciprocity Model

The arrival of the **Our Lady of Victory Missionary Sisters (OLVM)** collection significantly expanded and operationalized the unification framework described throughout this project. During ingest and assessment, the OLVM materials exposed multiple overlapping descriptive systems that had evolved over decades across physical storage environments, spreadsheets, legacy inventories, and existing EAD/ArchivesSpace implementations.

Rather than treating these inconsistencies as isolated metadata problems, the OLVM ingest process demonstrated the need for a reciprocal archival processing model capable of preserving original contextual systems while simultaneously normalizing collections into interoperable archival standards.

The OLVM collection arrived with:

- physical box-level organizational systems primarily arranged by apostolate, ministry, or operational activity
- multiple generations of spreadsheets created by different individuals and repositories
- inconsistent metadata structures and vocabularies
- flattened or invalid relational spreadsheet models
- partially transformed EAD and ArchivesSpace descriptions
- legacy numbering systems and descriptive drift between physical and intellectual arrangement

This ingest process became a practical implementation of the **Linear Reciprocity Model (LRM)** developed through this project.

## Reciprocal Ingest and Reconciliation

The OLVM workflows demonstrated that archival ingest should not be understood as a one-directional migration into a centralized system. Instead, ingest operates as a reciprocal negotiation between:

- the originating informational culture of the congregation
- legacy organizational structures
- physical arrangement systems
- modern archival standards
- archival information systems such as ArchivesSpace and Omeka S
- archivists and users interacting with the collection

As part of this process, workflows were developed to:

- preserve original informational structures prior to normalization
- consolidate multiple spreadsheet environments into unified datasets while retaining provenance
- identify and correct invalid or flattened metadata structures
- preserve original apostolate-centered arrangement systems as contextual metadata
- reconcile physical box labels with EAD and ArchivesSpace hierarchies
- normalize records into scalable archival structures suitable for long-term stewardship and public access
- generate controlled vocabularies while retaining legacy terminology as variant forms
- rebuild hierarchical EAD and ArchivesSpace ingest structures from reconciled datasets

This work also exposed multiple forms of archival drift including structural drift, semantic drift, provenance drift, and technological drift caused by years of decentralized descriptive practices and software-dependent workflows.

## Operational Outcome

The OLVM ingest process resulted in the development of:

- normalized reconciliation datasets
- box-level reconciliation dashboards
- reciprocal metadata preservation workflows
- EAD reconstruction pipelines
- ArchivesSpace-ready ingest structures
- controlled vocabulary harmonization procedures
- provenance-preserving normalization methods

These workflows now serve as an operational framework for ingesting and reconciling collections from multiple women religious repositories participating in the HARC/NAPWR unification initiative.

Importantly, this process demonstrated that standardization does not require the destruction of originating descriptive systems. Instead, the project emphasizes preserving and mapping legacy informational environments alongside normalized archival structures in order to maintain contextual integrity while enabling interoperability, scalability, and long-term access.

## Related Framework Documentation

Additional documentation formalizing this ingest and reconciliation framework, including the operational implementation of the Linear Reciprocity Model within the OLVM collection, is available here:

**[LINK TO FULL LRM / OLVM INGEST FRAMEWORK DOCUMENT]**

---

# Conclusion

The OLVM ingest process demonstrates that archival processing is not merely metadata creation.

It is:

- informational reconciliation
- structural normalization
- contextual preservation
- reciprocal systems design

The Linear Reciprocity Model provides a framework for understanding and operationalizing these relationships within modern archival information systems.

Rather than replacing legacy systems, the HARC ingest model:

- preserves them
- maps them
- stabilizes them
- and integrates them into scalable archival infrastructures.

The result is an archival environment that maintains original context while supporting contemporary standards, discoverability, interoperability, and long-term stewardship.

This framework represents not simply a processing workflow, but a new model for reciprocal archival ingest within distributed cultural heritage environments.

