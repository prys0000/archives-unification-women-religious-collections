# Linear Reciprocity Model

## Purpose

The **Linear Reciprocity Model (LRM)** provides the conceptual and operational framework for ingest, reconciliation, transformation, description, and discovery within the HARC/NAPWR environment.

Conventional migration models often imply a one-directional sequence:

```text
SOURCE → TRANSFORM → DESTINATION
```

That representation is inadequate for archival systems because each transformation can modify, obscure, expose, or restore relationships created at earlier stages.

The LRM therefore models the archival information environment as:

```text
SOURCE ⇄ RECONCILIATION ⇄ DESCRIPTION ⇄ SYSTEM ⇄ DISCOVERY ⇄ USER
```

The term **linear** identifies the existence of identifiable stages.  
The term **reciprocity** rejects the assumption that influence moves in only one direction.

## Foundational Claim

Archival information systems should adapt to the informational logic present in a collection before requiring the collection to adapt to the technical constraints of the archival system.

This does not reject standards. It changes the order and evidential basis through which standards are applied.

## Information Barriers Addressed by the Model

Recurring collection work has identified:

- structural drift
- semantic drift
- relational drift
- technological drift
- provenance drift
- authority drift
- access drift

These forms of drift may develop when a collection passes through multiple custodians, spreadsheets, databases, finding aids, migrations, and public interfaces.

## Reciprocal Relationships

### Physical ⇄ Intellectual

Physical order can reveal relationships missing from a finding aid.  
A finding aid can reveal intellectual relationships no longer obvious from physical order.

Neither should be assumed authoritative without reconciliation.

### Legacy Description ⇄ Standardized Description

Legacy terms may be inconsistent for cross-repository search but historically meaningful.

Authorized terminology can stabilize access while local terms remain available as variants or contextual evidence.

### Source System ⇄ Destination System

A transformation should not be evaluated only by whether the destination accepts it.

The source should remain traceable, reviewable, and recoverable.

### Ingest ⇄ Discovery

Discovery failures can reveal ingest failures:

- missing facets
- duplicate identities
- unexpected search clusters
- broken links
- absent dates
- incorrect creator mappings

Public access therefore produces quality-assurance evidence.

### Automation ⇄ Archivist

Automation provides repeatability and scale.  
The archivist evaluates ambiguity, contextual meaning, and defensibility.

The project automates **rules derived from archival judgment**, not the judgment itself.

## Ten Operational Stages

1. Preserve original informational context.
2. Consolidate data while retaining provenance.
3. Normalize unstable structures.
4. Preserve legacy intellectual structures.
5. Reconcile physical and intellectual systems.
6. Stabilize semantics and authorities.
7. Reconstruct EAD and ArchivesSpace structures.
8. Reconcile digital objects and access derivatives.
9. Normalize for NAPWR discovery.
10. Capture exceptions and update reusable rules.

## Dual-Context Description

A key LRM strategy is maintaining both:

```text
Legacy / Local Context
        ⇅
Normalized / Shared Context
```

Examples include:

- original ministry term + normalized ministry term
- legacy identifier + current identifier
- physical box label + intellectual series
- local person-name form + authorized/reconciled identity
- source record URL + portal derivative record

This allows standardization without pretending that only one descriptive representation has informational value.

## Research Significance

The repeated appearance of the same classes of archival friction across multiple women religious collections suggests that the LRM is not merely a repair method for one collection. It is being evaluated as a general framework for distributed archival information systems in which provenance, interoperability, system design, and public discovery must coexist.

## Documentation Requirement

Every major transformation governed by the LRM should be capable of answering:

- What was the source structure?
- What was changed?
- Why was it changed?
- What information was preserved?
- What could not be normalized safely?
- Which rule was applied?
- Which exceptions were created?
- How can the result be traced back to the source?
- What did downstream validation or discovery reveal?
