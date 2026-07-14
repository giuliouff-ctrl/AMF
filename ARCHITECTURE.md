# Standard — ARCHITECTURE.md

| Field | Value |
|---|---|
| ID | KNOW-06 |
| Document | templates/ARCHITECTURE.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `ARCHITECTURE.md` — the current technical truth of a project. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the system-design snapshot: how the project is built *now*, so any session can modify it without reverse-engineering it.
**Scope.** Structure and rules of `ARCHITECTURE.md`; not decision rationale (DECISIONS owns the *why*), not dependency inventory (DEPENDENCIES).
**Responsibilities.** Specification, structure, skeleton, maintenance rules for ARCHITECTURE.md.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; templates/DECISIONS.md (rationale split).
**Consumers.** All roles; heaviest: Engineer (implementation), Architect (owner), Reviewer (G1/G3 checks).
**Related documents.** templates/DECISIONS.md, templates/DEPENDENCIES.md, templates/TECHNICAL_DEBT.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E08/E11.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/ARCHITECTURE.md` |
| Class | I — Snapshot |
| Knowledge domain | Technical design |
| Owner (role) | Architect |
| Default read tier | T1 (most workflows; affected-area sections suffice — C4.2) |
| Profile | Minimal+ |
| Update triggers | E11 (architecture change, always D-NNN-backed via E08), E08 conditional |
| Required inputs | D2 Decision Records; the actual state of the source tree |
| Expected outputs | A description of the system accurate enough to code against |
| Archive policy | Never rotates; superseded designs live in DECISIONS entries and CHANGELOG |

## Structure

1. **Header** — per standard.
2. **System overview** — one diagram-or-paragraph: parts and how they talk. Front-load this (K8.1).
3. **Stack** — languages, frameworks, platforms, hosting; each entry cites the D-NNN that chose it.
4. **Components** — per component: responsibility, location in the tree, interfaces, invariants.
5. **Data model** — entities, storage, ownership of truth; migrations posture.
6. **Integrations** — external services and how they're bound (auth mode, limits, failure behavior).
7. **Conventions** — project code standards: structure, naming, patterns in force (the project-level analogue of FRAMEWORK_RULES; per R1.1 scope note, code conventions live here, not in the framework).
8. **Environments & deployment** — how it runs locally, how it ships.
9. **Invariants** — the "must never break" list; Reviewer checks G1/G3 against these.

Rules: **describes, never justifies** — every "why" is a D-NNN link (Article III; the rationale's home is DECISIONS). Must match the source tree: divergence is E31, and the *document* is presumed wrong until the tree is checked (the tree is the implementation fact; the ledger–snapshot rule M4.1 applies between documents, not between documents and reality). Sections may be omitted only if genuinely inapplicable (a static site has no data model) — omission is stated in §2, not silent.

## Skeleton

```markdown
# Architecture — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-06 |
| Document | ARCHITECTURE.md |
| Class | I — Snapshot |
| Profile-tier | Minimal+ |
| Owner | Architect |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## System overview
<parts + how they talk; note here any inapplicable sections below>

## Stack
| Layer | Choice | Decided |
|---|---|---|
| <language/framework> | <choice> | D-NNN |

## Components
### <Component>
- **Responsibility:** ...
- **Location:** <path>
- **Interfaces:** ...
- **Invariants:** ...

## Data model
<entities, storage, source of truth>

## Integrations
| Service | Purpose | Binding | Failure behavior |
|---|---|---|---|

## Conventions
<project code standards in force>

## Environments & deployment
<local run; ship path>

## Invariants
- <must never break>
```

## Maintenance Notes

Updated in the same session as any structural change (E11) — an ARCHITECTURE.md that lags the tree is the single most expensive knowledge defect for future sessions. The Reviewer's G1 pass includes "does this change keep ARCHITECTURE.md true?".

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard |

## Future Extension Notes

Projects with heavy API surface may split §4 interfaces into a generated annex when tooling exists; until then, one document (P9).
