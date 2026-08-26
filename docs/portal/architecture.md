# NAPWR Portal Architecture

## Purpose

NAPWR is a federated discovery architecture connecting independently authoritative archival repositories through a shared metadata and access layer.

## Conceptual Architecture

```text
LOCAL / HUB SYSTEMS
ArchivesSpace · EAD · CSV · databases · digital collections
        ⇅
SOURCE CHARACTERIZATION
Hierarchy · provenance · identifiers · vocabulary · media relationships
        ⇅
TRANSFORMATION / RECONCILIATION
Python · BAT · crosswalks · authorities · validation
        ⇅
NAPWR CANONICAL EXCHANGE MODEL
Shared DCTERMS · congregation · hub · source links · media
        ⇅
OMEKA S DISCOVERY LAYER
Browse · Search · Facets · Collection Records · Digital Objects
        ⇅
IDENTITY / BIOGRAPHICAL LAYER
Sisters Name Index
        ⇅
CONVERSATIONAL DISCOVERY
AI-assisted natural-language retrieval
        ⇅
AUTHORITATIVE SOURCE SYSTEMS
Finding aids · repository records · archivist-mediated research
```

The arrows are reciprocal because downstream discovery can identify upstream metadata or mapping problems.

## Architectural Principles

### Federated, Not Custodially Centralized

Participating repositories retain archival authority.

### Canonical Discovery Model

Only the fields needed for shared discovery are standardized centrally.

### Source Traceability

Portal records should preserve pathways back to authoritative records.

### Layered Discovery

Different research tasks require different interfaces:

- collection search
- name discovery
- digital browsing
- conversational query assistance

### Explainable Transformation

Mappings should be documented in crosswalks rather than hidden in scripts.

## Primary Components

### Source Layer

May include:

- ArchivesSpace
- EAD
- CSV/XLSX
- local databases
- digital collections
- physical inventories

### Transformation Layer

Responsible for:

- parsing
- normalization
- reconciliation
- mapping
- validation
- audit output

### Canonical Metadata Layer

Provides consistent:

- titles
- collection relationships
- repository/hub values
- congregation values
- creators
- dates
- spatial terms
- subjects
- descriptions
- source links
- identifiers
- rights
- media

### Discovery Layer

Omeka S presents shared records and facets.

### Identity Layer

The Sisters Name Index supports person-centered research across congregations.

### Conversational Layer

The chatbot assists natural-language navigation while remaining subordinate to source evidence.

## Failure Boundaries

The architecture should make it possible to distinguish:

- source-data failure
- transformation failure
- mapping failure
- portal-indexing failure
- media failure
- authority failure
- conversational-retrieval failure

That separation is essential for maintainability.
