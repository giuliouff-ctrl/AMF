# Standard — CURRENT_STATUS.md

| Field | Value |
|---|---|
| ID | KNOW-11 |
| Document | templates/CURRENT_STATUS.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `CURRENT_STATUS.md` — the project as the last session left it. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the freshest document in the instance: the T0 snapshot that tells a cold session where the project stands, in one read.
**Scope.** Structure and rules of `CURRENT_STATUS.md`; not the resumption point (latest HANDOVER owns "what next, exactly"), not history (SESSION_LOG).
**Responsibilities.** Specification, structure, skeleton, maintenance rules for CURRENT_STATUS.md.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; [SESSION_MANAGEMENT.md](../../core/SESSION_MANAGEMENT.md) §4 (mandatory refresh).
**Consumers.** Every session (T0 read #3); the Human Owner checking project health.
**Related documents.** templates/HANDOVER.md (division of labor below), templates/TASKS.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E02/E23.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/CURRENT_STATUS.md` |
| Class | I — Snapshot |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | **T0** (read #3, every session) |
| Profile | Minimal+ |
| Update triggers | E02 (every session end — mandatory, no exception), E23, E29 conditional mid-session |
| Required inputs | The session's outcomes; open items across TASKS/KNOWN_ISSUES |
| Expected outputs | An honest one-page state: works / doesn't / in flight / blocked |
| Archive policy | Never rotates — fully rewritten each session; history lives in SESSION_LOG |

## Structure

1. **Header** — per standard.
2. **State summary** — one paragraph, present tense: what the project is right now. **As-of** date + session ID in the first line.
3. **Works / Doesn't work** — two honest lists (Article IV). "Doesn't work" includes known-broken and never-built-yet in scope.
4. **In flight** — active focus; open tasks by ID with one-line state.
5. **Blocked / waiting** — what cannot proceed and on what (Q-NNN, R-NNN, Owner input).
6. **Recent** — last ~3 sessions' outcomes, one line each (older: SESSION_LOG).
7. **Health** — quick indicators: knowledge current? verification green? deploy state? debt pressure?

**Division of labor with HANDOVER:** CURRENT_STATUS describes *state* for anyone; HANDOVER prescribes *next actions* for the successor session. Status never contains instructions; handovers never substitute for state.

Rules: full rewrite each session (E02) — never diff-patched into staleness; one page is the budget (K8.1): detail belongs in the documents this one points to; the Minimal-profile folding target for issues/risks/questions summaries ([folding map](../../operations/PROFILES.md)).

## Skeleton

```markdown
# Current Status — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-11 |
| Document | CURRENT_STATUS.md |
| Class | I — Snapshot |
| Profile-tier | Minimal+ |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## State summary
**As of <YYYY-MM-DD> · <S-ID>.** <one paragraph, present tense>

## Works
- <verified working>

## Doesn't work
- <broken or not yet built, in scope>

## In flight
- T-NNN <title> — <one-line state>

## Blocked / waiting
- <item> — on <Q-NNN / R-NNN / Owner>

## Recent
- <S-ID>: <one-line outcome>

## Health
- Knowledge: <current / gaps noted> · Verification: <state> · Deploy: <state> · Debt: <pressure>
```

## Maintenance Notes

The stranger test's first half lives here: status plus latest handover must orient a cold session completely. If a session ends and this file still describes the *previous* session's world, E02 was violated — that is an interrupted session's signature (SESSION_MANAGEMENT §5).

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Health indicators (§7) may formalize into measured values if tooling lands; keep them one line each regardless — this document's value is its brevity.
