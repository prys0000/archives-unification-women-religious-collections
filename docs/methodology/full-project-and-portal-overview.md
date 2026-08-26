# Archives Unification — Women Religious Collections

**A federated archival interoperability framework for assessing, reconciling, normalizing, integrating, and discovering collections of women religious across heterogeneous repositories.**

This project develops a repeatable technical and methodological infrastructure for bringing independently created archival systems into a shared discovery environment without erasing provenance, local descriptive practice, institutional context, or the intellectual structures embedded in legacy records.

The work now operates at two interconnected levels:

1. **Collection unification and archival systems engineering** — arrangement, metadata reconciliation, EAD/ArchivesSpace transformation, authority control, digital-object linking, validation, and preservation-aware ingest.
2. **NAPWR — Portal for the Archives of Women Religious** — a federated Omeka S discovery platform that provides cross-hub searching, congregation-level browsing, a large Sisters Name Index, standardized digital-object publication, and an AI-assisted conversational discovery layer.

**Core Standards:** DACS · EAD 2002 · Dublin Core / DCTERMS · PREMIS  
**Primary Systems:** ArchivesSpace · Omeka S · Amazon Web Services · Preservation Repositories  
**Supporting Technologies:** Python · Windows BAT automation · XML/EAD parsing · CSV normalization · API-mediated discovery · JavaScript search interfaces · AI-assisted retrieval

---

# Major Project Development — From Collection Reconciliation to Federated Archival Infrastructure

The project began as an effort to reconcile heterogeneous women religious collections for ingest into common archival systems. That work has expanded into a broader model for **federated archival interoperability**.

The central problem is no longer simply how to convert one spreadsheet, one EAD file, or one finding aid into another system. The larger methodological problem is how to preserve the evidential and contextual value of independently maintained archival environments while making those environments computationally interoperable across institutions.

Recent work has therefore connected three layers that are often treated separately:

- **archival processing and descriptive reconciliation**
- **machine-actionable transformation and validation**
- **public cross-repository discovery**

The result is a developing infrastructure in which local archival systems remain authoritative while shared schemas, automated transformations, authority structures, and discovery interfaces allow researchers to move across repositories as though they were interacting with a coherent research environment.

This work operationalizes the **Linear Reciprocity Model (LRM)** by treating every transformation as a reciprocal relationship between the source system and the destination system rather than as a one-directional migration.

---

# Current Congregational Integration Corpus

Recent processing, reconciliation, ingest, and portal-development work now includes major collection environments associated with:

- **Sisters of the Most Precious Blood**, O'Fallon, Missouri
- **Sisters of St. Francis of the Holy Cross**, Green Bay, Wisconsin
- **Sisters of St. Casimir**, Chicago, Illinois
- **Sisters of Charity of the Blessed Virgin Mary (BVM)**, Dubuque, Iowa
- **Our Lady of Victory Missionary Sisters (Victory Noll Sisters)**, Huntington, Indiana

These collections differ substantially in arrangement history, metadata maturity, descriptive vocabulary, digitization practice, identifier construction, and source-system architecture. Their differences have made them especially useful as a comparative test environment for the project's reconciliation methods.

The work is not premised on forcing every congregation into an identical descriptive history. Instead, the project separates **interoperability requirements** from **local archival meaning**. Common structures are established where needed for exchange, search, and computational processing, while congregation-specific terminology, legacy identifiers, arrangement evidence, and descriptive distinctions are retained as contextual data.

---

# NAPWR — Portal for the Archives of Women Religious

**Live platform:**  
https://sistersarchives.libraryhost.com/s/portal-for-the-archives-of-women-religious/page/welcome

The **NAPWR Portal for the Archives of Women Religious** represents the public-facing implementation of the project's interoperability model.

Rather than functioning as a conventional digital repository in which all contributing institutions surrender their records to a single centralized system, the portal is designed as a **federated discovery layer**. Participating repositories retain their own finding aids, digital collections, systems, and institutional identities while a shared data layer makes selected descriptive information discoverable through one interface.

The portal currently brings together four contributing archival hubs:

- Heritage and Research Center at Saint Mary's
- Boston College Catholic Religious Archives
- Santa Clara University Archives and Special Collections
- Women Religious Archives Collaborative

This architecture is significant because it separates **custodial control** from **discovery interoperability**. A researcher does not need to understand the technical architecture, metadata conventions, or search behavior of every participating repository before beginning research. The portal mediates those differences through common search, browsing, identity, and metadata structures while preserving links back to the authoritative source environment.

---

# Portal Methodology

The portal is being developed through a methodology of **provenance-aware schema mediation**.

In this model, source repositories are not treated as deficient versions of a future centralized database. They are treated as historically situated information systems with their own descriptive decisions, inherited vocabularies, record structures, and technical constraints.

The workflow therefore proceeds through five methodological operations:

## 1. Source-System Characterization

Each incoming repository or collection is evaluated as an information environment rather than only as a set of records.

Assessment includes:

- source platform
- hierarchy and component levels
- identifier patterns
- descriptive conventions
- authority practices
- date structures
- digital-object relationships
- local terminology
- physical arrangement evidence
- repository-specific access links
- known data loss or transformation history

This establishes the informational context required before normalization begins.

## 2. Canonical Exchange Modeling

A limited set of shared fields is defined for cross-repository exchange and discovery.

The canonical model is deliberately narrower than the total descriptive richness of any one repository. It functions as an **interoperability contract**, not a replacement finding aid.

Shared elements include:

- title
- collection / parent relationship
- repository or contributing hub
- creator
- date
- place
- subject
- type
- description
- source record
- identifier
- rights
- digital media
- congregation

## 3. Reciprocal Transformation

Source values are mapped into the shared model while retaining links to the original context.

Normalization is therefore bidirectional in principle:

**source context → normalized representation → source authority**

The normalized portal record remains traceable to the authoritative archival record rather than becoming an isolated derivative.

## 4. Validation and Exception Capture

Transformations are checked for:

- missing required fields
- invalid hierarchy
- broken digital links
- malformed XML
- encoding corruption
- inconsistent identifiers
- unrecognized controlled values
- mismatched creator or agent forms
- missing or ambiguous dates
- duplicated media relationships
- unexpected source-system structures

Exceptions are documented rather than silently discarded.

## 5. Iterative Rule Formalization

Recurring exceptions are converted into reusable processing rules.

This is one of the most important aspects of the project. The system becomes more effective not because archival judgment is delegated to an opaque model, but because repeated professional decisions are progressively formalized into:

- transformation rules
- validation tests
- crosswalk logic
- exception handlers
- authority mappings
- date-repair patterns
- vocabulary mappings
- ingest safeguards

This produces a form of **institutional computational memory** that improves later processing while remaining reviewable by archivists.

---

# Portal Architecture

The developing architecture can be represented as:

```text
LOCAL / HUB SYSTEMS
ArchivesSpace · EAD · CSV · legacy databases · local digital collections
        │
        ▼
SOURCE ASSESSMENT
Hierarchy · provenance · identifiers · vocabulary · digital-object relationships
        │
        ▼
TRANSFORMATION AND RECONCILIATION LAYER
Python scripts · BAT launchers · crosswalks · authority reconciliation · validation
        │
        ▼
CANONICAL NAPWR EXCHANGE MODEL
Shared DCTERMS fields · repository identity · source links · standardized media fields
        │
        ▼
OMEKA S FEDERATED DISCOVERY LAYER
Collections Search · Browse · Sisters Name Index · digital objects
        │
        ▼
AI-ASSISTED DISCOVERY
Conversational research interface · query interpretation · guided archival navigation
        │
        ▼
AUTHORITATIVE SOURCE SYSTEMS
Finding aids · repository records · digital files · archivist-mediated research
```

The arrows should be understood as reciprocal rather than purely linear. Corrections discovered at the portal, validation, or access stage can expose problems in earlier metadata, mappings, source descriptions, or automation rules. Those findings then inform subsequent processing.

---

# Standardized Hub Ingest and Automation Toolkits

A major recent development is the creation of reusable Windows-based automation toolkits that allow partner repositories to transform source archival data into a shared portal structure without requiring each institution to independently design a complex migration workflow.

The most developed workflow converts **ArchivesSpace EAD directly to an Omeka-ready Dublin Core CSV**.

## EAD-to-Omeka Workflow

The standardized workflow uses:

- `RUN_EAD_TO_OMEKA.bat`
- `ead_to_omeka.py`
- the shared NAPWR Dublin Core import template
- automated audit output
- parse-warning output when source XML requires recovery

The BAT launcher provides a low-barrier Windows interface while the Python layer performs structured EAD parsing and field transformation.

Users can export an EAD file from ArchivesSpace, drag one or more files onto the BAT launcher, review the resulting audit file, and import the normalized CSV into Omeka S.

This replaces a longer chain of manual operations that previously could require:

- XML transformation
- intermediate spreadsheet conversion
- manual field cleanup
- row merging
- media-link identification
- thumbnail selection
- date normalization
- repeated copy-and-paste work

The objective is not merely speed. The larger methodological benefit is **repeatability**. A shared transformation pipeline reduces the probability that each hub will interpret portal requirements differently.

---

# Shared EAD-to-Omeka Mapping

The current workflow maps archival description into a common 15-column DCTERMS-oriented import environment.

| Omeka Field | Source / Rule |
|---|---|
| `dcterms:title` | EAD component title |
| `dcterms:alternative` | Reserved / blank where not supplied |
| `dcterms:isPartOf` | Collection relationship |
| `dcterms:publisher` | Repository / contributing institution |
| `dcterms:creator` | Nearest valid origination or controlled fallback |
| `dcterms:contributor` | Reserved / blank where not supplied |
| `dcterms:date` | Display or normalized EAD date |
| `dcterms:spatial` | Geographic terms |
| `dcterms:subject` | Subject, occupation, function, and title terms |
| `dcterms:type` | Genre/form or conservative media inference |
| `dcterms:description` | Scope and contents, abstract, or descriptive fallback |
| `dcterms:source` | Authoritative ArchivesSpace public record |
| `dcterms:identifier` | Component unit identifier |
| `dcterms:rights` | Use restriction or shared rights statement |
| `Media URL` | AWS thumbnail or primary digital file |

The transform can inherit appropriate subject and geographic context from parent components while preserving the source ArchivesSpace record as the authoritative reference.

---

# Digital-Object Selection and Media Normalization

The portal workflow includes explicit logic for distinguishing archival description from publishable digital objects.

By default, the conversion toolkit identifies item- or file-level components containing direct AWS-hosted digital media. It can:

- detect direct `amazonaws.com` links
- prefer thumbnail derivatives for Omeka media ingest
- fall back to the primary file when no thumbnail exists
- exclude representative series-level imagery unless intentionally enabled
- preserve the source ArchivesSpace URL
- create an audit record of all discovered media relationships

This distinction is essential in large archival hierarchies because a finding aid may contain thousands of components but only a subset has corresponding digital content suitable for public portal ingest.

The audit environment makes those automated selections reviewable before publication.

---

# Data Repair and Normalization Utilities

The automation environment has expanded beyond basic crosswalking.

Recent workflows include procedures for:

- repairing malformed XML or embedded HTML
- detecting character-encoding corruption
- normalizing spreadsheet structures
- converting legacy spreadsheet formats
- preserving hierarchy during CSV/XLSX transformation
- identifying missing date expressions
- deriving dates conservatively from titles when source evidence supports the inference
- checking container hierarchy
- validating digital-object URLs
- distinguishing primary files from thumbnails
- reconciling duplicate media
- standardizing contributor and repository values
- preparing ArchivesSpace bulk-import structures
- generating Omeka-ready import files
- creating review and exception outputs

These utilities form an **archival middleware layer** between heterogeneous source systems and the shared discovery platform.

---

# Sisters Name Index — Cross-Congregational Identity and Biographical Discovery

The **Sisters Name Index** is a second major discovery component of the portal.

It extends beyond ordinary collection-level search by treating names, biographical attributes, vocation, geography, and congregational membership as structured discovery points.

The interface supports filtering across fields such as:

- congregation
- record status
- birth decade
- birth country
- birth state or region
- work / vocation
- mission country
- mission state or region
- entrance decade
- first profession decade
- final profession decade
- death decade
- departure from congregation
- language

Records can be expanded in place, allowing researchers to move rapidly through biographical information without navigating hundreds or thousands of separate item pages.

## Authority and Identity Reconciliation

The underlying name work also addresses a recurring archival problem: one person may appear under multiple forms across time and systems.

Women religious may be represented through combinations of:

- civil name
- baptismal name
- religious name
- surname variants
- initials
- titles
- birth and death dates
- entrance and profession dates
- congregation-specific naming conventions

The project therefore treats the name index as more than a directory. It is developing into a **cross-repository identity reconciliation layer**.

Structured fields support distinctions among:

- family name
- religious name
- baptismal name
- life dates
- place of birth
- entrance date
- first profession
- final profession
- career or vocation
- mission locations
- biographical description
- archivist notes
- language
- congregation

This creates the basis for more reliable person-level discovery across collections that were originally described independently.

---

# Faceted Cross-Repository Collection Search

The portal's collection browser provides a shared discovery interface over heterogeneous collections.

Current facets include:

- congregation
- contributing hub
- date
- spatial location
- creator
- subject

This is a significant architectural choice. Rather than requiring users to begin by knowing which institution holds a relevant collection, the portal allows them to begin with a **research concept** such as a sister's name, a congregation, a place, a ministry, a date, or a subject.

The system then returns records from the appropriate contributing repositories while retaining source attribution.

This shifts the discovery model from:

> **Which repository should I search?**

to:

> **What evidence exists across the participating archival network?**

That change is central to the research value of NAPWR.

---

# AI-Assisted Archival Chatbot

The project now also includes an **AI-assisted conversational discovery interface** developed to sit alongside conventional search, browse, and name-index access.

The chatbot is not intended to replace the finding aid, the archivist, or the source record. Its purpose is to provide a **natural-language mediation layer** between researchers and a complex multi-repository archival environment.

A researcher may know a concept but not the descriptive vocabulary needed to search an archival system. The conversational interface can help interpret that intent and guide the user toward relevant:

- congregations
- sisters
- ministries
- places
- dates
- collections
- finding aids
- name-index records
- digitized materials

## Retrieval-Oriented Design

The chatbot is designed around a retrieval-first principle.

The system should distinguish between:

1. **evidence available in the archival data**, and
2. **generated explanatory language used to help the researcher navigate that evidence**.

The archival record remains authoritative.

This is particularly important for women religious archives because names, dates, ministry assignments, institutional affiliations, and congregation histories may be highly specific and are not appropriate domains for unsupported model inference.

## AI as Interface, Not Archival Authority

The role of AI in this environment is therefore constrained and purposeful.

AI is used to assist with:

- interpreting natural-language questions
- reformulating queries
- identifying likely archival entities
- connecting user terminology with archival terminology
- navigating the name index and collection search
- summarizing retrieved descriptive context
- guiding researchers toward authoritative records

It is not treated as an autonomous descriptive authority.

Ambiguous biographical identity, provenance, restrictions, arrangement decisions, and archival interpretation remain subject to human review and source evidence.

---

# Adaptive Learning Model and Internal Learning System

The project incorporates a **human-supervised adaptive learning model** for processing and interoperability.

The term *learning* is used here in an archival-systems sense: the infrastructure accumulates reusable knowledge from prior processing decisions and applies that knowledge to later collections.

Each ingest can reveal new patterns such as:

- previously unseen date constructions
- alternate creator forms
- congregation-specific terminology
- new hierarchy conventions
- malformed EAD patterns
- new identifier structures
- different media-link practices
- duplicate patterns
- local subject terms
- new digital-object relationships

When those patterns are resolved, the solution can be formalized into the next version of the system.

The accumulated knowledge is expressed through:

- updated crosswalks
- authority tables
- parsing rules
- controlled mappings
- validation scripts
- exception libraries
- normalization functions
- review procedures
- documented decision rules

This creates an iterative feedback structure:

```text
INGEST
  ↓
EXCEPTION
  ↓
ARCHIVIST REVIEW
  ↓
DECISION
  ↓
RULE FORMALIZATION
  ↓
VALIDATION
  ↓
REUSE IN FUTURE INGEST
```

The adaptive model therefore reduces repeated manual problem solving while preserving professional accountability.

It is intentionally **human-in-the-loop**. Automation handles scale and repeatability; archivists retain interpretive control.

---

# Linear Reciprocity Model and Reciprocal Ingest

The **Linear Reciprocity Model (LRM)** provides the theoretical and operational framework for the project.

Traditional migration models often represent archival processing as a linear movement:

```text
SOURCE → TRANSFORM → DESTINATION
```

The LRM instead treats archival information systems as reciprocally dependent stages.

```text
SOURCE ⇄ TRANSFORMATION ⇄ DESCRIPTION ⇄ SYSTEM ⇄ DISCOVERY ⇄ USER
```

A decision made at one stage affects the informational possibilities of later stages, while problems discovered later can reveal deficiencies in earlier stages.

Within the NAPWR environment, reciprocity operates among:

- originating informational cultures
- legacy organizational systems
- physical arrangement environments
- archival standards
- archival information systems
- digital-object repositories
- portal schemas
- search interfaces
- AI-assisted discovery
- archivists
- researchers

The framework recognizes that:

- normalization should not erase originating informational structures
- legacy systems contain contextual and evidential meaning
- local vocabularies may need preservation even when authorized forms are introduced
- discovery failures can reveal upstream metadata problems
- access systems can become quality-assurance environments
- repeated ingest problems should modify future workflow design
- archival systems should adapt to collections as collections are adapted for systems

The OLVM ingest initially demonstrated these principles operationally. Subsequent work across multiple congregations and the NAPWR portal extends the model from a collection-level workflow into a cross-repository infrastructure.

---

# Information Model

## Controlled Series Structure (S1–S10)

| Series | Title |
|---|---|
| S1 | Governance and Administration |
| S2 | Congregation History and Identity |
| S3 | Membership and Sisters' Records |
| S4 | Ministry and Apostolic Works |
| S5 | Properties and Facilities |
| S6 | Financial and Legal Records |
| S7 | Communications and Publications |
| S8 | External Relations and Affiliations |
| S9 | Visual and Audio Materials |
| S10 | Reference and Research Files |

The controlled series model functions as a stabilization layer for collection integration.

It is not intended to retroactively erase meaningful original arrangement. Instead, it provides a shared analytic and processing structure that can coexist with local arrangement through reciprocal mappings and contextual notes.

This distinction is essential in collections that have experienced:

- multiple custodians
- partial reprocessing
- box-number continuity without intellectual continuity
- local series titles
- mission-based arrangements
- administrative reorganizations
- later accretions
- hybrid physical and digital filing systems

---

# Metadata and Crosswalks

The project maintains multiple crosswalk environments supporting:

- EAD ↔ ArchivesSpace
- EAD ↔ NAPWR portal schema
- Dublin Core / DCTERMS ↔ Omeka S
- legacy spreadsheets ↔ normalized tabular structures
- local descriptive fields ↔ shared discovery fields
- congregation-specific names ↔ reconciled authority forms
- physical arrangement ↔ intellectual arrangement
- source digital objects ↔ portal media records

## Controlled Vocabulary Strategy

Authorized forms are standardized where needed for interoperability while preserving:

- local terminology
- congregation-specific labels
- historical usage
- legacy identifiers
- variant spellings
- culturally meaningful naming practices
- source-system values

Authority reconciliation may draw from:

- LCNAF
- LCSH
- Getty vocabularies
- local authority files
- congregation-specific authority systems
- internally maintained cross-repository identity tables

The goal is **semantic alignment without descriptive flattening**.

---

# Process Overview

## 1. Discovery and Assessment

- inventory incoming systems and materials
- characterize source schemas
- assess descriptive quality and risk
- identify processing history
- identify structural inconsistencies
- inspect physical and intellectual arrangement
- preserve original information environments before transformation

## 2. Consolidation and Preservation

- merge working datasets where appropriate
- preserve source provenance
- retain original labels and identifiers
- capture physical arrangement evidence
- document source-system relationships
- retain unmodified reference copies of source data

## 3. Structural Normalization

- identify invalid spreadsheet structures
- normalize record-level relationships
- repair encoding corruption
- convert flattened data into hierarchical structures
- reconcile duplicated or conflicting fields
- validate container and parent-child relationships

## 4. Arrangement and Description

- apply consistent series/subseries logic where appropriate
- preserve original order where contextually meaningful
- create reciprocal relationships between legacy and normalized systems
- document intellectual decisions separately from mechanical transformation

## 5. Metadata Crosswalk and Reconciliation

- normalize authorities
- harmonize controlled vocabularies
- align EAD, ArchivesSpace, DCTERMS, and Omeka fields
- preserve local terminology as variants or contextual notes
- reconcile creators and agents against existing authority records

## 6. Packaging and Ingest

- generate ArchivesSpace-ready structures
- create EAD-ready hierarchical environments
- generate NAPWR / Omeka import files
- attach digital objects and thumbnail derivatives
- preserve authoritative source links
- assign restrictions and rights

## 7. Quality Assurance and Validation

- validate required fields
- test structural integrity
- verify identifiers and URIs
- review digital-object relationships
- inspect audit outputs
- conduct box-level reconciliation
- document remediation decisions

## 8. Publication and Access

- publish selected digital records
- index records for faceted portal search
- synchronize congregation and hub values
- expose name-index data
- validate derivatives and links
- connect records back to authoritative finding aids

## 9. Conversational and Assisted Discovery

- expose natural-language research pathways
- translate user questions into archival search concepts
- connect names, places, dates, congregations, and ministries
- direct users toward authoritative records
- maintain distinctions between generated guidance and archival evidence

## 10. Sustainability and Iterative Processing

- maintain versioned scripts
- update mappings and authority structures
- preserve documentation
- support partner training
- capture recurring exceptions
- formalize improved rules
- maintain reciprocal links between systems

---

# Workstreams

## Federated Portal Development

Design and development of the NAPWR discovery environment, including hub representation, shared schemas, site architecture, browse interfaces, and public access.

## Adaptive Standardization and Learning

Development of reusable ingest, normalization, reconciliation, exception-handling, and validation logic.

## Intake and Appraisal

Accessioning, transfer documentation, source-system capture, preservation assessment, and risk characterization.

## Arrangement and Description

Series/subseries mapping, scope notes, hierarchy reconstruction, container verification, and contextual preservation.

## Metadata and Crosswalks

Crosswalk development, authority reconciliation, vocabulary harmonization, identity normalization, and canonical exchange modeling.

## Digital Objects and Preservation

Digital-object linking, derivative generation, AWS-hosted access files, thumbnail workflows, PREMIS-oriented preservation thinking, and storage management.

## Systems and Pipelines

ArchivesSpace imports, EAD generation, EAD-to-Omeka transformation, BAT/Python utilities, data repair, validation, audit generation, and public discovery synchronization.

## Sisters Name Authority and Indexing

Cross-congregational identity reconciliation, biographical normalization, name variant management, and multidimensional name discovery.

## AI-Assisted Research Access

Conversational search, natural-language mediation, query reformulation, archival navigation, and evidence-linked discovery.

## Access and Outreach

Rights management, restrictions, research guidance, public access systems, interpretive discovery, and researcher support.

---

# Quality Assurance

## Validation Goals

- arrangement integrity
- hierarchy integrity
- required metadata completeness
- authority compliance
- identifier consistency
- digital-object validation
- thumbnail / primary-file relationship accuracy
- source-link preservation
- rights consistency
- provenance preservation
- cross-hub field consistency
- reciprocal relationship integrity

## Validation Methods

The framework incorporates:

- automated validation
- audit CSV generation
- warning files
- deterministic field checks
- stratified sampling
- human review
- box-level reconciliation
- EAD comparison
- link validation
- authority comparison
- portal spot-checking
- iterative correction

Public discovery itself becomes part of the QA environment. Search failures, missing facets, incorrect names, and unexpected result clustering can expose upstream problems in ingest or normalization.

---

# Policies, Ethics, and Epistemic Control

The project emphasizes:

- ethical stewardship
- preservation of community context
- privacy and restriction management
- culturally sensitive description
- transparent normalization practices
- provenance preservation
- source-system traceability
- explainable automation
- human review of ambiguous transformations
- clear distinction between archival evidence and AI-generated guidance

The project rejects the assumption that computational uniformity is inherently equivalent to archival quality.

A successful shared system must be able to standardize enough information to support discovery while retaining enough difference to preserve meaning.

---

# Research Contribution

The project functions simultaneously as an operational archival program and as a research environment for studying archival information systems.

Its broader contribution is the proposition that interoperability can be built through **reciprocal standardization** rather than destructive homogenization.

The NAPWR implementation demonstrates how:

- distributed repositories can remain independently authoritative
- shared exchange schemas can mediate heterogeneous description
- lightweight automation can operationalize archival standards at scale
- exception capture can become an adaptive institutional learning mechanism
- identity reconciliation can support cross-congregational research
- portal interfaces can expose relationships not visible within a single finding aid
- AI can assist discovery without being granted archival authority
- downstream access behavior can inform upstream metadata improvement

In this sense, the portal is not simply the final access stage of the project. It is part of the archival information system itself.

The search interface, name index, ingest pipeline, validation environment, archival descriptions, digital objects, and conversational interface form a connected information ecology in which each component both depends on and provides feedback to the others.

---

# Current Research and Development Questions

The project continues to test several questions:

1. How much normalization is necessary for reliable cross-repository discovery?
2. Which local descriptive differences must remain visible to preserve provenance and community context?
3. How can repeated archivist decisions be formalized into reusable computational rules without obscuring professional judgment?
4. How can cross-congregational authority data improve discovery without collapsing historically distinct naming systems?
5. How should AI-mediated archival interfaces expose uncertainty, evidence, and source authority?
6. Can public discovery behavior function as a meaningful feedback mechanism for upstream archival quality control?
7. How can a shared portal scale to additional repositories without imposing technically burdensome participation requirements?

---

# Repository and Documentation Structure

Recommended project documentation structure:

```text
/
├── README.md
├── docs/
│   ├── methodology/
│   │   ├── linear-reciprocity-model.md
│   │   ├── adaptive-learning-model.md
│   │   ├── portal-methodology.md
│   │   └── quality-assurance.md
│   ├── crosswalks/
│   │   ├── ead-to-omeka.md
│   │   ├── archivesspace-to-napwr.md
│   │   └── name-authority-fields.md
│   ├── congregations/
│   │   ├── most-precious-blood.md
│   │   ├── st-francis-holy-cross.md
│   │   ├── st-casimir.md
│   │   ├── bvm-dubuque.md
│   │   └── olvm-victory-noll.md
│   └── portal/
│       ├── architecture.md
│       ├── collection-search.md
│       ├── sisters-name-index.md
│       └── chatbot.md
├── tools/
│   ├── ead-to-omeka/
│   ├── archivesspace-import/
│   ├── spreadsheet-normalization/
│   ├── media-validation/
│   └── authority-reconciliation/
├── templates/
│   ├── NAPWR-import-template-dcterms.csv
│   └── validation-templates/
└── examples/
    ├── audit-output/
    └── normalized-ingest/
```

---

# Contributing

Future partner documentation should identify:

- supported source systems
- minimum exchange fields
- accepted identifier practices
- required repository attribution
- rights and access requirements
- digital-object requirements
- authority reconciliation procedures
- review responsibilities
- versioning expectations
- escalation procedures for ambiguous mappings

Participation should be designed around a low technical barrier: repositories should not need to rebuild their archival systems in order to participate in the shared discovery network.

---

# License

_TODO: Add licensing and reuse statement for documentation, code, templates, and partner-supplied metadata._

---

# Project Direction

The project has moved beyond a single collection migration workflow.

It is now developing as a **federated archival information infrastructure for women religious collections**: one that combines archival theory, metadata engineering, automation, authority control, public discovery, and AI-assisted research access while keeping provenance and human archival judgment at the center of the system.

The NAPWR portal is the practical expression of that model.

The collection-processing pipelines make heterogeneous records interoperable.  
The Sisters Name Index creates a cross-congregational identity layer.  
The faceted search environment creates shared discovery across repositories.  
The automation toolkits make participation repeatable and scalable.  
The adaptive model turns prior processing decisions into reusable institutional knowledge.  
The chatbot adds a natural-language pathway into the archival network.  
The Linear Reciprocity Model connects all of these components into a single archival information system.

Together, these elements establish a framework in which women religious archives can remain distinct in custody and context while becoming meaningfully connected for research, discovery, preservation, and long-term stewardship.
