# Standard — PROJECT.md

| Field | Value |
|---|---|
| ID | KNOW-05 |
| Document | templates/PROJECT.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `PROJECT.md` — the business truth of a project. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the project identity document: vision, goals, scope and constraints — the "why" every technical decision ultimately answers to.
**Scope.** Structure and rules of `PROJECT.md`; not roadmap (ROADMAP), not requirements-in-progress (BACKLOG).
**Responsibilities.** Specification, structure, skeleton, maintenance rules for PROJECT.md.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4.
**Consumers.** All roles; heaviest readers: Product Analyst (owner), Architect (constraints), Orchestrator (planning).
**Related documents.** templates/BACKLOG.md, templates/ROADMAP.md, templates/ASSUMPTIONS.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E09/E10/E22.
**Update policy.** D2 (Architect) for this standard. Content changes in instances follow E10 (scope is D3-backed).

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/PROJECT.md` |
| Class | I — Snapshot |
| Knowledge domain | Business |
| Owner (role) | Product Analyst |
| Default read tier | T1 (§Goals+§Scope in WF_FEATURE; full in deep onboarding) |
| Profile | Minimal+ |
| Update triggers | E10 (scope change — D3-backed), E09, E22 (Owner input affecting vision/goals) |
| Required inputs | Owner's intent, captured at adoption and via MEETING_NOTES thereafter |
| Expected outputs | Stable business context: what success means, what is out of bounds |
| Archive policy | Never rotates; superseded scope visible via D-NNN records (E10 always carries one) |

## Structure

1. **Header** — per standard.
2. **Vision** — one paragraph: what this project is and for whom.
3. **Goals** — numbered, testable business goals ("G1: ..."), each with its success criterion.
4. **Non-goals** — explicit exclusions; the cheapest scope defense that exists.
5. **Users & stakeholders** — who uses it, who pays for it, who approves it.
6. **Scope** — what is in, at headline level (detail lives in BACKLOG/TASKS).
7. **Constraints** — business constraints: budget posture (e.g. free-tier-only), deadlines, legal/brand requirements, client's technical limits. Technical constraints derived from these live in ARCHITECTURE.
8. **Success criteria** — how the Owner will judge the project done/healthy.

Rules: goals are referenced by ID from BACKLOG items and D-records ("serves G2"). Changes to §2–§4 and §6 are scope changes: E10, D3-backed, never silent. This document answers *why*; anything answering *how* belongs in ARCHITECTURE.

## Skeleton

```markdown
# Project — <NAME>

| Field | Value |
|---|---|
| ID | KNOW-05 |
| Document | PROJECT.md |
| Class | I — Snapshot |
| Profile-tier | Minimal+ |
| Owner | Product Analyst |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Vision
<one paragraph>

## Goals
- **G1:** <goal> — success: <criterion>
- **G2:** ...

## Non-goals
- <explicit exclusion>

## Users & stakeholders
| Who | Role in project |
|---|---|
| <user type> | <uses it for ...> |
| <Owner/client> | <approves, pays, directs> |

## Scope
<headline in-scope items>

## Constraints
- <business constraint>

## Success criteria
- <how the Owner judges done/healthy>
```

## Maintenance Notes

The most stable instance document by design: if PROJECT.md churns, either scope discipline has failed or the project's identity was never captured (both E31 findings). Goals get IDs so downstream documents can trace to them; renumbering is forbidden (treat like entity IDs).

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard |

## Future Extension Notes

Client-site projects may warrant a Brand/Content constraints subsection under §7; add on evidence (P9), not by default.
