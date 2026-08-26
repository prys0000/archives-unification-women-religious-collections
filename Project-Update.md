# Operationalizing the Linear Reciprocity Model Through Multi-Collection Archival Ingest and Reconciliation at HARC/NAPWR

## Introduction

The ingest and reconciliation work undertaken across multiple women religious collections at HARC and within the broader NAPWR environment demonstrates a practical implementation of the **Linear Reciprocity Model (LRM)** within a live, distributed archival setting.

Across congregational collections, the same categories of archival friction have appeared repeatedly:

- inconsistent spreadsheet environments
- flattened or structurally invalid metadata
- conflicting descriptive systems
- mismatches between physical and intellectual arrangement
- legacy identifiers with inconsistent application
- variable authority practices
- descriptive drift across custodians and systems
- incomplete or partially transformed EAD and ArchivesSpace structures
- digital-object relationships that do not consistently align with archival hierarchy
- software-dependent structures that obscure the original logic of the records

These recurring conditions indicate that the problems are not unique to a single collection. They are characteristic of distributed archival environments in which records have accumulated across decades, custodians, repositories, software systems, and descriptive practices.

The framework therefore formalizes an operational model HARC and NAPWR can use when ingesting collections from external repositories, congregations, ministries, and partner institutions.

Rather than treating archival ingest as a simple metadata transfer process, the model understands ingest as a reciprocal restructuring event among:

1. the originating archival culture and intellectual system
2. the receiving archival information system
3. the physical collection
4. the descriptive technologies used to mediate access
5. the archivists responsible for interpretation and stewardship
6. the users whose search behavior reveals the strengths and weaknesses of the resulting system

The central methodological finding is that preservation of original order, reconciliation of legacy descriptive systems, and normalization into modern archival standards can occur simultaneously without requiring the destruction of local informational context.

---

# Recurring Core Problems Across Congregational Collections

## Initial Condition

The collections processed through this environment have arrived with multiple overlapping descriptive systems.

Although the terminology, arrangement, and technical history differ from congregation to congregation, the underlying structural challenges are strikingly similar.

## 1. Physical Original Order

Many collections retain physical arrangements based on the operational, ministerial, geographic, or administrative structures used by the originating congregation.

These may include arrangements by:

- apostolate
- ministry
- mission
- geographic location
- house or institution
- administrative office
- program
- activity
- function
- chronological filing
- mixed local filing systems

The physical arrangement often reflects the lived organizational structure of the congregation more directly than later archival systems do.

A generalized relationship may appear as:

```text
Operational Function → Local File Unit → Mixed Documentary Contents
```

These labels and sequences are therefore treated as evidence of a historical informational system rather than as incidental filing behavior.

---

# 2. Legacy Spreadsheet Structures

A recurring challenge across collections has been the presence of spreadsheets created over many years by different individuals, repositories, vendors, or processing projects.

Common problems include:

- mixed hierarchical levels in single rows
- subjects incorrectly transformed into columns
- functions represented as both fields and values
- multiple spreadsheets describing overlapping portions of the same collection
- inconsistent controlled vocabularies
- flattened contextual relationships
- descriptive drift over time
- duplicate semantic columns
- inconsistent or missing identifiers
- dates placed in titles rather than date fields
- creator and agent values entered in non-authorized forms
- container values disconnected from intellectual hierarchy
- inconsistent digital-object or thumbnail links
- character-encoding corruption
- hidden spreadsheet structures that interfere with downstream ingest

These spreadsheets frequently contain significant archival knowledge, but they do not always represent archival records in a structurally valid relational or hierarchical form.

The goal of reconciliation is therefore not to discard them, but to identify the archival intelligence embedded within them and convert that intelligence into a stable, machine-actionable structure.

---

# 3. Existing EAD and ArchivesSpace Structures

Another recurring condition involves collections for which EAD or ArchivesSpace description already exists, but where those descriptions represent only one stage in a longer processing history.

A common pattern is:

```text
Legacy Arrangement → Intermediate Spreadsheet → EAD / ArchivesSpace → Revised Ingest Environment
```

During these transformations, the originating organizational logic may be partially dissolved, reinterpreted, flattened, or redistributed into standardized series structures.

The resulting EAD may be technically valid while still obscuring:

- original functional relationships
- legacy numbering systems
- physical evidence
- congregation-specific terminology
- relationships among ministries or administrative units
- prior arrangement decisions

The project therefore distinguishes **technical validity** from **contextual completeness**.

A technically valid archival structure is not automatically the most contextually faithful representation of the collection.

---

# The Linear Reciprocity Model in Practice

## Foundational Principle

The Linear Reciprocity Model proposes that archival information systems should not impose unilateral descriptive control over collections.

Instead, archival systems should reciprocally adapt to the informational logic present in the collection while simultaneously normalizing metadata for:

- long-term stewardship
- interoperability
- preservation
- system migration
- public discovery
- computational processing
- cross-repository research

The multi-collection work at HARC/NAPWR demonstrates that archival ingest is better understood as:

> A reciprocal negotiation among legacy organizational structures, archival standards, technical systems, physical evidence, and contemporary access requirements.

Rather than replacing legacy systems outright, the ingest process:

- captures them
- preserves them
- interprets them
- maps them
- normalizes them
- validates them
- and connects them to contemporary archival infrastructure

---

# The HARC/NAPWR Ingest and Reconciliation Framework

# Stage 1 — Preservation of Original Informational Context

## Goal

Preserve original informational structures before normalization begins.

## Operational Actions

- preserve original spreadsheets intact
- preserve source files prior to transformation
- preserve physical box and folder labels through photography or transcription when necessary
- preserve original descriptive terminology
- preserve legacy identifiers
- preserve original intellectual arrangement patterns
- document source-system architecture
- retain evidence of prior processing decisions

## LRM Principle

The originating informational environment contains embedded contextual meaning and organizational logic that may be impossible to reconstruct after normalization.

The source environment is therefore treated as archival evidence in its own right.

---

# Stage 2 — Unified Data Consolidation

## Goal

Create a coherent working environment while preserving provenance.

## Operational Actions

- merge related datasets into unified working structures
- preserve source file information
- preserve source worksheet information
- preserve source row information where useful
- retain raw original text
- retain original identifiers
- preserve positional and container data
- distinguish original values from normalized values
- document transformations

## LRM Principle

Reciprocal systems require provenance to remain visible at every transformation stage.

The normalized record must remain traceable to the environment from which it originated.

---

# Stage 3 — Structural Normalization

## Goal

Convert invalid, inconsistent, or flattened data structures into archival record-level structures.

## Operational Actions

- identify false or semantically overloaded columns
- unpivot subject or function columns into proper values
- convert one-dimensional spreadsheets into hierarchical structures
- normalize record granularity
- standardize field relationships
- identify duplicate semantic fields
- separate descriptive values from structural metadata
- repair malformed date structures
- stabilize creator and agent fields
- normalize identifier placement

## LRM Principle

Systems must adapt structurally to the informational logic embedded in the collection rather than simply forcing incompatible structures into a predetermined template.

A normalized environment should be structurally valid without becoming contextually reductive.

A common target structure is:

```text
One Row = One Archival Record
```

rather than:

```text
One Column = One Program, Subject, Function, or Local Category
```

---

# Stage 4 — Legacy Intellectual Structure Preservation

## Goal

Preserve original arrangement systems alongside normalized archival hierarchy.

## Operational Actions

Create or retain parallel descriptive fields where appropriate, such as:

- legacy series or function
- legacy apostolate or ministry
- legacy file unit number
- legacy box number
- original label transcription
- program or activity
- original department
- originating office
- local subject term
- prior arrangement note

## LRM Principle

Normalization should not erase originating informational relationships.

The project therefore supports a dual-context model in which legacy structure and normalized archival hierarchy can coexist.

For example:

```text
Legacy Functional Structure
        ⇅
Normalized Archival Hierarchy
```

This allows the collection to remain computationally interoperable while preserving evidence of how the originating community understood its own records.

---

# Stage 5 — Reconciliation Between Physical and Intellectual Systems

## Goal

Create reciprocal links between physical materials and descriptive systems.

## Operational Actions

- assign standardized box identifiers where needed
- build box and folder reconciliation indexes
- compare physical labels to finding-aid structures
- link EAD or ArchivesSpace components to physical materials
- preserve legacy numbering
- identify mismatches
- document redistributed or reinterpreted records
- maintain container continuity when intellectually appropriate
- verify hierarchy without unnecessarily disturbing stable physical control

## LRM Principle

Physical arrangement and intellectual arrangement should reciprocally reinforce one another.

Neither should be treated as automatically superior.

Physical evidence can reveal descriptive drift, while intellectual description can reveal relationships no longer visible from box order alone.

---

# Stage 6 — Controlled Vocabulary and Semantic Stabilization

## Goal

Create stable descriptive systems while preserving historical terminology.

## Operational Actions

- standardize congregation names
- standardize ministry and apostolate terms
- normalize document and resource types
- normalize geographic values
- reconcile synonymous terms
- reconcile creator and agent forms
- standardize repository and hub values
- preserve original terminology as variants
- distinguish authorized forms from local historical usage
- maintain crosswalks among legacy and standardized terms

## LRM Principle

Descriptive control should stabilize access without erasing historical semantics.

Standardization functions as a mediation layer rather than as a replacement for source language.

---

# Stage 7 — EAD and ArchivesSpace Reconstruction

## Goal

Generate stable archival descriptive systems from reconciled source environments.

## Operational Actions

- rebuild hierarchical EAD structures
- prepare ArchivesSpace ingest spreadsheets
- establish parent-child relationships
- restore missing contextual hierarchy
- reconcile existing agents against authorized agent lists
- populate missing date expressions when source evidence supports the inference
- validate container relationships
- normalize identifiers
- connect digital and physical control systems
- correct malformed spreadsheet structures that prevent successful ingest

## LRM Principle

Archival systems should emerge from reconciled informational environments rather than from premature forcing of collections into rigid pre-existing structures.

The resulting record structure should be both technically valid and contextually defensible.

---

# Stage 8 — Digital Object and Access Reconciliation

## Goal

Maintain reliable relationships among archival description, digital objects, derivatives, thumbnails, and public access systems.

## Operational Actions

- validate digital-object URLs
- distinguish primary files from access derivatives
- verify thumbnail relationships
- detect duplicate media
- preserve authoritative source links
- identify missing or mismatched digital objects
- prepare Omeka-ready media mappings
- validate externally hosted media
- maintain correspondence among ArchivesSpace, AWS, Omeka S, and portal records

## LRM Principle

Digital access objects are not separate from archival description.

They form another reciprocal layer whose integrity depends on stable relationships among file, description, identifier, repository, and public interface.

---

# Stage 9 — Portal and Discovery Normalization

## Goal

Transform locally described collections into a shared discovery environment without erasing repository identity.

## Operational Actions

- map local description to shared NAPWR fields
- standardize hub and congregation values
- transform EAD into Omeka-ready DCTERMS structures
- preserve authoritative source URLs
- create consistent collection and item relationships
- support faceted search
- expose person-level discovery through the Sisters Name Index
- support cross-repository browsing
- provide structured data for AI-assisted retrieval

## LRM Principle

Interoperability does not require centralization.

NAPWR functions as a discovery layer over distributed repositories rather than as a replacement for them.

The shared portal schema therefore acts as an interoperability contract while source systems retain archival authority.

---

# Stage 10 — Iterative Validation and Adaptive Learning

## Goal

Transform recurring ingest problems into reusable institutional knowledge.

## Operational Actions

- document processing exceptions
- identify recurring error patterns
- update scripts and crosswalks
- formalize successful remediation rules
- maintain validation routines
- expand authority mappings
- record ambiguous cases for human review
- reuse established decisions in later collections
- monitor public discovery behavior for upstream metadata problems

## LRM Principle

Later stages of the archival information system should be allowed to provide feedback to earlier stages.

The workflow is therefore not simply:

```text
Source → Ingest → Access
```

It is:

```text
Source ⇄ Reconciliation ⇄ Description ⇄ System ⇄ Discovery ⇄ Review
```

The system becomes progressively more effective because each completed ingest contributes reviewable knowledge to subsequent processing.

---

# Archival Drift and Informational Degradation

The multi-collection environment has exposed several recurring forms of archival drift.

## Structural Drift

Original functional or local organizational systems are redistributed into later archival hierarchies.

## Semantic Drift

Terms change meaning or are applied inconsistently across custodians, spreadsheets, and systems.

## Relational Drift

Physical, intellectual, digital, and authority relationships become disconnected.

## Technological Drift

Data structures evolve around the capabilities or limitations of software rather than archival logic.

## Provenance Drift

The origin of a descriptive decision becomes unclear after repeated migration or reprocessing.

## Authority Drift

Names, creators, congregations, and institutions acquire inconsistent forms across repositories or systems.

## Access Drift

Public interfaces expose only a portion of the relationships present in the underlying archival data.

These forms of drift are cumulative.

A collection may remain technically accessible while gradually losing the relationships necessary for accurate interpretation.

---

# Why Traditional Archival Ingest Often Fails

Traditional ingest workflows often assume that:

- incoming data is structurally valid
- spreadsheets are relationally coherent
- EAD accurately reflects original order
- existing hierarchy is internally consistent
- creators are already normalized
- dates occupy expected fields
- container structures correspond cleanly to description
- digital objects are correctly linked
- normalization should replace legacy systems

The multi-collection work demonstrates that these assumptions are frequently incorrect.

Collections developed outside a single centralized archival environment often contain:

- embedded local organizational logic
- functional rather than hierarchical arrangement
- mixed descriptive paradigms
- iterative community-created metadata
- evolving vocabularies
- inconsistent authority control
- multiple technical migrations
- duplicated or overlapping descriptive environments

Ignoring these realities can produce:

- contextual loss
- inaccurate hierarchy
- broken provenance
- poor discovery
- ingest failure
- unnecessary reprocessing
- archival paralysis

---

# HARC/NAPWR Reciprocal Ingest Philosophy

The framework therefore proposes:

## The archival system should adapt to the collection before the collection adapts to the archival system.

This principle does not reject archival standards.

It changes the order in which standards are applied.

The reciprocal model:

- delays premature flattening
- preserves contextual evidence
- identifies the source system before altering it
- builds reciprocal mappings
- stabilizes semantics
- documents exceptions
- normalizes only after relationships are understood
- allows automation without surrendering archival judgment

The objective is **semantic alignment without descriptive flattening**.

---

# Standardization Across Multiple Congregational Collections

The recurring challenges observed across collections from women religious demonstrate that the framework is not collection-specific.

Recent and ongoing work has included collection environments associated with:

- Sisters of the Most Precious Blood
- Sisters of St. Francis of the Holy Cross
- Sisters of St. Casimir
- Sisters of Charity of the Blessed Virgin Mary
- Our Lady of Victory Missionary Sisters / Victory Noll Sisters

Each congregation possesses a distinct history, vocabulary, arrangement tradition, institutional structure, and processing history.

Yet the same broader system problems recur:

- heterogeneous source description
- local naming practices
- variable metadata quality
- fragmented hierarchy
- different levels of processing
- multiple custodial histories
- physical/intellectual mismatches
- inconsistent date and identifier structures
- non-uniform digital-object practices
- different technical platforms

This repetition is important.

It demonstrates that the methods developed through the project are not a one-off remediation response. They constitute a **generalizable archival interoperability framework** for distributed women religious collections.

---

# Practical Outcomes for HARC and NAPWR

Using this framework allows HARC and NAPWR to:

## 1. Preserve Original Community Knowledge

The informational systems created by women religious remain visible even after normalization.

## 2. Scale Ingest Across Distributed Repositories

Collections from multiple congregations and hubs can be processed through a common methodology without requiring identical source systems.

## 3. Reduce Archival Paralysis

Collections can be ingested iteratively rather than waiting for an unattainable state of perfect normalization.

## 4. Improve ArchivesSpace Integration

Reconciled structures support:

- valid hierarchical ingest
- agent matching
- container control
- digital-object linkage
- date normalization
- identifier consistency
- repeatable EAD generation

## 5. Improve Omeka and NAPWR Integration

Standardized transformation supports:

- DCTERMS mapping
- cross-hub collection search
- faceted browsing
- source-record linking
- digital media publication
- Sisters Name Index integration
- AI-assisted discovery

## 6. Support Long-Term Interoperability

Parallel preservation of original and normalized structures enables future migration, reinterpretation, remapping, and system evolution.

## 7. Build Institutional Computational Memory

Repeated decisions are captured as scripts, mappings, validation checks, authority controls, and documented rules.

The system therefore becomes more stable as additional collections are processed.

---

# Automation as an Operational Layer

The framework has increasingly been implemented through repeatable BAT and Python workflows.

These tools operationalize archival decisions for tasks including:

- spreadsheet normalization
- EAD parsing
- EAD-to-Omeka conversion
- ArchivesSpace ingest preparation
- hierarchy checking
- date normalization
- character-encoding repair
- authority reconciliation
- digital-object validation
- thumbnail selection
- media-link verification
- audit generation
- exception reporting

The purpose of automation is not to replace archival interpretation.

Its purpose is to ensure that once an interpretation has been carefully made, the same mechanical logic does not need to be recreated manually for every subsequent collection.

This is a key distinction between **automating judgment** and **automating the repeatable consequences of judgment**.

The project focuses on the latter.

---

# Adaptive Learning and Internal Learning Systems

The accumulating scripts, crosswalks, exception handlers, authority tables, and validation procedures form an internal learning system.

A new collection may introduce a previously unseen structure or anomaly.

The sequence is:

```text
New Collection
     ↓
Exception Identified
     ↓
Archivist Analysis
     ↓
Resolution
     ↓
Rule Formalization
     ↓
Validation
     ↓
Reusable Processing Knowledge
```

This approach creates a form of **human-supervised adaptive standardization**.

The learning system is not dependent on autonomous machine inference.

Instead, professional archival decisions are progressively formalized into transparent computational rules that can be reused, revised, challenged, and documented.

---

# Public Discovery as a Quality-Control Mechanism

The implementation of the NAPWR portal extends the LRM beyond backend ingest.

Public discovery systems can reveal problems that may remain invisible within source data.

For example:

- a missing search facet may expose inconsistent field mapping
- duplicate sisters may expose unresolved identity records
- unexpected clustering may expose uncontrolled vocabulary
- broken media may expose invalid URLs
- failed retrieval may expose incomplete metadata
- misleading search results may expose overly broad normalization
- missing cross-repository relationships may reveal insufficient authority reconciliation

The public interface is therefore not simply an endpoint.

It becomes another diagnostic layer within the archival information system.

This creates a reciprocal loop in which access can influence description and future ingest design.

---

# AI-Assisted Discovery Within the Reciprocal Model

The developing AI-assisted archival chatbot introduces another discovery layer into this reciprocal system.

Its purpose is to help researchers translate natural-language questions into archival search pathways.

The chatbot can assist users in navigating among:

- collections
- congregations
- sisters
- ministries
- locations
- dates
- finding aids
- digital objects
- name records

Its role is interpretive and navigational rather than authoritative.

Within the LRM, the chatbot represents another mediation layer:

```text
Research Question
      ⇅
Natural-Language Interpretation
      ⇅
Structured Archival Retrieval
      ⇅
Authoritative Source Record
```

Problems identified through conversational discovery can also reveal weaknesses in controlled vocabulary, metadata normalization, authority structures, or portal design.

AI-assisted discovery therefore participates in the reciprocal feedback model without replacing archival evidence or human judgment.

---

# Generalized Project Update — Multi-Collection Ingest, Reconciliation, and the Linear Reciprocity Model

The ingest and reconciliation work conducted across multiple women religious collections has significantly expanded and operationalized the unification framework described throughout this project.

Across collections, materials have repeatedly presented overlapping descriptive systems that evolved across physical storage, spreadsheets, legacy inventories, finding aids, EAD, ArchivesSpace, digital repositories, and public discovery systems.

Although each congregation has its own administrative history and descriptive culture, the same categories of system friction have consistently appeared:

- physical organization based on local ministry, function, mission, or administration
- multiple generations of spreadsheets
- inconsistent metadata structures
- flattened or invalid relational models
- descriptive drift
- legacy numbering systems
- mismatches between physical and intellectual arrangement
- partially transformed EAD or ArchivesSpace structures
- authority inconsistencies
- date normalization problems
- digital-object inconsistencies
- variable technical practices among custodians

These recurring conditions demonstrate that archival ingest should not be conceptualized as a one-directional migration into a centralized system.

Instead, ingest operates as a reciprocal negotiation among:

- originating informational cultures
- legacy organizational structures
- physical arrangement systems
- contemporary archival standards
- ArchivesSpace
- Omeka S
- NAPWR
- digital-object repositories
- archivists
- researchers
- AI-assisted discovery environments

As part of this process, workflows have been developed to:

- preserve original informational structures before normalization
- consolidate multiple spreadsheet environments while retaining provenance
- identify and correct flattened metadata structures
- preserve legacy arrangement systems as contextual metadata
- reconcile physical containers with EAD and ArchivesSpace hierarchy
- normalize records for long-term management
- reconcile controlled vocabularies
- preserve original terminology as variant forms
- rebuild EAD and ArchivesSpace structures
- standardize NAPWR exchange fields
- transform EAD into Omeka-ready records
- validate media relationships
- support cross-repository discovery
- capture processing exceptions as reusable system knowledge

The recurring nature of these challenges across collections transforms the framework from a collection-specific workflow into a broader methodology for distributed archival systems.

---

# Operational Outcome

The multi-collection processing environment has resulted in the development of:

- normalized reconciliation datasets
- box- and folder-level verification workflows
- reciprocal metadata preservation practices
- EAD reconstruction pipelines
- ArchivesSpace-ready ingest structures
- authority reconciliation procedures
- controlled vocabulary harmonization
- standardized NAPWR import schemas
- BAT and Python transformation utilities
- EAD-to-Omeka pipelines
- digital-object validation methods
- source-link preservation practices
- audit and exception reporting
- Sisters Name Index structures
- cross-hub discovery mechanisms
- AI-assisted research access
- provenance-preserving normalization methods

These workflows now function collectively as an operational framework for ingesting, reconciling, standardizing, and exposing collections from multiple women religious repositories.

The repeated experience across collections confirms that standardization does not require destruction of originating descriptive systems.

Instead, legacy informational environments can be preserved and mapped alongside normalized archival structures to maintain contextual integrity while enabling:

- interoperability
- scalability
- discoverability
- preservation
- future migration
- cross-repository research

---

# Conclusion

The multi-collection ingest environment demonstrates that archival processing is not merely metadata creation.

It is:

- informational reconciliation
- structural normalization
- semantic stabilization
- authority reconciliation
- contextual preservation
- technical transformation
- reciprocal systems design

The Linear Reciprocity Model provides a framework for understanding and operationalizing those relationships across modern archival information systems.

Rather than replacing legacy systems, the HARC/NAPWR ingest model:

- preserves them
- interprets them
- maps them
- stabilizes them
- validates them
- and integrates them into scalable archival infrastructures

The result is an environment capable of maintaining originating context while supporting contemporary archival standards, public discovery, interoperability, automation, and long-term stewardship.

The significance of the project is therefore larger than any one congregation or collection.

The repeated appearance of the same structural problems across distinct women religious archives demonstrates that the framework addresses a broader class of archival information-system challenges.

It represents not simply a processing workflow, but a model for **reciprocal archival ingest and federated interoperability within distributed cultural heritage environments**.
