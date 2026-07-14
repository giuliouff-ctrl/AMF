# Standard — ASSUMPTIONS.md

| Field | Value |
|---|---|
| ID | KNOW-17 |
| Document | templates/ASSUMPTIONS.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `ASSUMPTIONS.md` — working assumptions, declared and tracked to validation. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the assumptions register: everything the project treats as true without having verified it — declared, so its invalidation is an event instead of a surprise.
**Scope.** Structure and rules of `ASSUMPTIONS.md`; not open uncertainty (OPEN_QUESTIONS — a question awaits an answer; an assumption *is* the answer, provisionally), not risk (RISK_REGISTER).
**Responsibilities.** Specification, entry format, validation discipline, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Article IV (honest gaps).
**Consumers.** Product Analyst (owner), Architect (design-bearing assumptions), WF_RESEARCH (validation work).
**Related documents.** templates/OPEN_QUESTIONS.md (boundary above), templates/RESEARCH.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E17/E18.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/ASSUMPTIONS.md` |
| Class | I — Snapshot |
| Knowledge domain | Business |
| Owner (role) | Product Analyst |
| Default read tier | T1 (WF_RESEARCH, WF_ARCHITECTURE_REVIEW), T2 otherwise |
| Profile | Full (Minimal/Standard: load-bearing assumptions noted inline where they bear, marked "assumed", per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E17 (made), E18 (validated/invalidated — invalidation propagates, see below) |
| Required inputs | The assumption, its basis, what leans on it |
| Expected outputs | A validation queue; blast-radius map for each invalidation |
| Archive policy | VALIDATED/INVALIDATED items rotate to `archive/ASSUMPTIONS_<YYYY>.md` (K7.3) |

## Entry Format

Per item: **assumption** (a falsifiable statement — "client's staff will use Android scanners", not "users are fine") · made (date, S-ID) · basis (why we believe it) · **leaned on by** (refs: D-NNN, ARCHITECTURE sections, G-goals) · validation plan (how/when we'll know) · status (WORKING / VALIDATED / INVALIDATED).

Rules: **the "leaned on by" column is the point** — E18 invalidation walks it: every listed ref gets revisited, the conditional cascade in the matrix (E18) is executed, and an L-NNN records what assuming cost; an assumption nothing leans on is trivia — don't register it (K8.1); design-bearing assumptions (leaned on by ARCHITECTURE or a D-record) get a validation plan with a *date or trigger*, not "eventually".

## Structure

1. **Header** — per standard.
2. **Working** — entries, most-leaned-on first.
3. **Settled (recent)** — validated/invalidated since last rotation.

## Skeleton

```markdown
# Assumptions — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-17 |
| Document | ASSUMPTIONS.md |
| Class | I — Snapshot |
| Profile-tier | Full |
| Owner | Product Analyst |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Working
- **<falsifiable statement>** — made <date> · <S-ID>
  - Basis: <why believed>
  - Leaned on by: <D-NNN, ARCHITECTURE §X, G-N>
  - Validate: <how/when>
  - Status: WORKING

## Settled (recent)
- **<statement>** — VALIDATED/INVALIDATED <S-ID> · <consequence refs>
```

## Maintenance Notes

The cheapest insurance in the instance: writing "assumed, unverified" next to a load-bearing belief costs one line; discovering it false unrecorded costs the redesign *plus* the archaeology. When a session catches itself saying "presumably" — that's an E17.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: falsifiability rule, lean-on tracing |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

A-NNN IDs if cross-referencing demand appears (R4 addition); withheld pending evidence (P9).
