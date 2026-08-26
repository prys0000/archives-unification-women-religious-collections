# AI-Assisted Archival Chatbot

## Purpose

The NAPWR chatbot provides a natural-language mediation layer between researchers and structured archival discovery systems.

It is intended to help users who know their historical question but do not know:

- archival terminology
- congregation naming conventions
- repository location
- controlled subjects
- name variants
- finding-aid structure

## Role

The chatbot may assist with:

- interpreting a research question
- reformulating search terms
- identifying likely archival entities
- connecting natural language to structured fields
- directing users to relevant collections
- directing users to Sisters Name Index records
- explaining retrieved archival context
- surfacing authoritative source links

## Epistemic Model

```text
USER QUESTION
      ↓
QUERY INTERPRETATION
      ↓
STRUCTURED RETRIEVAL
      ↓
ARCHIVAL EVIDENCE
      ↓
EXPLANATORY RESPONSE
```

The system should distinguish retrieval from generation.

## What the Chatbot Is Not

It is not:

- the archival record
- an autonomous authority file
- a replacement for the finding aid
- a replacement for the archivist
- a source of unsupported biographical facts

## Retrieval-First Principle

Where possible, responses should be grounded in:

- portal records
- name-index records
- finding aids
- repository sources
- controlled project data

When evidence is absent, the system should communicate uncertainty rather than fabricate specificity.

## Entity Types

Useful entity classes include:

- sister/person
- congregation
- ministry/apostolate
- institution
- geographic location
- collection
- date/period
- subject
- repository/hub

## Feedback to the LRM

Chatbot failures are system evidence.

Examples:

- user terminology cannot be mapped → vocabulary gap
- person not found → authority/index gap
- irrelevant collection retrieved → mapping/search issue
- source not linked → provenance/access issue

Conversational access is therefore both a service layer and a diagnostic layer.

## Human Oversight

Human review remains required for:

- ambiguous identity
- provenance
- restrictions
- sensitive description
- arrangement interpretation
- contested historical claims
