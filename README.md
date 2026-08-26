# Archives Unification — Women Religious Collections

## Federated archival interoperability for HARC and NAPWR

This repository documents the methods, crosswalks, validation procedures, transformation tools, collection-level case records, and public-discovery architecture developed through the unification of women religious archival collections and the **NAPWR — Portal for the Archives of Women Religious**.

The project addresses a recurring archival systems problem: collections created and maintained by different congregations and repositories frequently contain significant historical and descriptive knowledge, but that knowledge is distributed across incompatible spreadsheets, finding aids, EAD exports, ArchivesSpace records, digital-object systems, local vocabularies, physical arrangements, and institutional practices.

The project does **not** treat those differences as defects to be erased.

Instead, it develops a framework for **semantic alignment without descriptive flattening**: enough standardization to support interoperability, cross-repository search, validation, migration, and long-term stewardship while preserving provenance, local terminology, legacy arrangement, and community-specific context.

## Core Research and Operational Model

The work is organized around the **Linear Reciprocity Model (LRM)**:

```text
SOURCE ⇄ RECONCILIATION ⇄ DESCRIPTION ⇄ SYSTEM ⇄ DISCOVERY ⇄ USER
```

The model assumes that archival information is transformed repeatedly across its lifecycle and that later stages can reveal defects or losses introduced earlier. Discovery, therefore, is not merely the endpoint of processing; it can also function as quality-assurance feedback.

The operational environment connects:

- physical collections
- legacy spreadsheets and databases
- EAD
- ArchivesSpace
- DACS-based archival description
- Dublin Core / DCTERMS
- Omeka S
- AWS-hosted digital objects and derivatives
- authority and identity reconciliation
- the Sisters Name Index
- faceted cross-repository discovery
- AI-assisted conversational access

## Current Congregational Integration Corpus

Current documentation includes collection environments associated with:

- Sisters of the Most Precious Blood
- Sisters of St. Francis of the Holy Cross
- Sisters of St. Casimir
- Sisters of Charity of the Blessed Virgin Mary (BVM), Dubuque
- Our Lady of Victory Missionary Sisters / Victory Noll Sisters

These collections are maintained as separate integration case records because the purpose is comparative: recurring problems across distinct collections provide evidence for which methods are collection-specific and which are generalizable.

## Repository Map

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

## Documentation Logic

The repository separates four kinds of knowledge:

### 1. Methodology

Why the system is designed this way.

These documents define the theoretical framework, adaptive learning model, portal methodology, and quality-assurance philosophy.

### 2. Crosswalks

How information moves between systems.

Crosswalk documentation records explicit field mappings, inheritance rules, provenance controls, transformation assumptions, and exception handling.

### 3. Congregation Case Records

What happened in a specific collection.

Each case record documents source conditions, transformations, exceptions, local terms, authority issues, QA findings, and lessons that may improve future ingest.

### 4. Portal and Tool Documentation

How the infrastructure works.

Portal documentation describes discovery architecture and AI-assisted access. Tool directories document reproducible transformation, normalization, validation, and authority-reconciliation procedures.

## Guiding Principles

1. **Preserve before transforming.**
2. **Document provenance at every stage.**
3. **Do not mistake technical validity for contextual completeness.**
4. **Standardize shared discovery requirements without erasing local meaning.**
5. **Automate repeatable consequences of archival judgment, not archival judgment itself.**
6. **Capture exceptions instead of silently discarding them.**
7. **Treat public discovery as part of the archival information system.**
8. **Keep AI subordinate to archival evidence and source authority.**
9. **Make every transformation reviewable.**
10. **Allow each completed ingest to improve the next one.**

## Standards and Systems

**Standards:** DACS · EAD 2002 · Dublin Core / DCTERMS · PREMIS-oriented preservation practice  
**Systems:** ArchivesSpace · Omeka S · AWS · preservation repositories  
**Automation:** Python · Windows BAT launchers · CSV/XLSX normalization · XML/EAD parsing · validation scripts

## Status

This repository is living documentation. It should evolve as additional congregations, hubs, source systems, authority structures, and discovery requirements are incorporated into NAPWR.

# Licensing & Reuse

To maximize the openness, searchability, and longevity of historical research, the assets in this repository are split under separate open licensing terms:

* **Code & Page Architecture:** The underlying software scripts, functional layouts, and site templates are licensed under the [MIT License](LICENSE).
* **Content & Narrative Templates:** General text, written frameworks, and documentation styles are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org).
* **Data, Schemas & Metadata:** All data models, front-matter YAML templates, mapping schemas, and archival metadata collections are dedicated to the public domain under [Creative Commons CC0 1.0 Universal](https://creativecommons.org).

## Attribution Requirement
If you fork this repository, adapt the schemas, or reuse these templates for other digital humanities or archival unification efforts, you must provide attribution back to the source:
`Adapted from the [Archives Unification for Women Religious Collections](https://github.com/prys0000/archives-unification-women-religious-collections) project by @prys0000.`

