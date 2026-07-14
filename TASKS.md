# Standard — TASKS.md

| Field | Value |
|---|---|
| ID | KNOW-08 |
| Document | templates/TASKS.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `TASKS.md` — active work, tracked. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the active-work snapshot: every unit of tracked work, its state, and nothing stale.
**Scope.** Structure and rules of `TASKS.md`; not future work (BACKLOG), not work history (SESSION_LOG).
**Responsibilities.** Specification, structure, skeleton, task-state model, maintenance rules.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4/§5 (ID counter), [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (T-NNN).
**Consumers.** Orchestrator (owner), all working roles; every planning stage.
**Related documents.** templates/BACKLOG.md (promotion), templates/SESSION_LOG.md (history); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E03–E06, E32.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/TASKS.md` |
| Class | I — Snapshot |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | T1 (WF_FEATURE, WF_BUGFIX, WF_RELEASE) |
| Profile | Minimal+ |
| Update triggers | E03 (created), E04 (state change — near-real-time per M3.2), E05 (completed), E06 (blocked), E32 (deferred) |
| Required inputs | Session plans; BACKLOG promotions; blocking refs (Q-NNN, R-NNN) |
| Expected outputs | Truthful working state, at any moment of any session |
| Archive policy | DONE tasks older than the latest handover rotate to `archive/TASKS_<YYYY>.md` (K7.3); open tasks never rotate |

## Task-State Model

`TODO → IN_PROGRESS → DONE`, with `BLOCKED` reachable from either active state and returning to it. Exactly these four states.

| State | Meaning | Required fields |
|---|---|---|
| TODO | Committed work, not started (uncommitted work stays in BACKLOG) | title, origin (B-item/G-goal/I-NNN/D-NNN ref) |
| IN_PROGRESS | Being worked, this session or resumable | + owner role, session started |
| BLOCKED | Cannot proceed | + blocking ref (Q-NNN, R-NNN, Owner, external) |
| DONE | Completed against the [Definition of Done](../../quality/DEFINITION_OF_DONE.md) | + session completed, evidence ref |

## Structure

1. **Header** — per standard.
2. **Next ID** — counter line (K5.1): `Next ID: T-NNN`.
3. **Active** — table: ID · title · state · owner role · refs (origin, blockers) · one-line note.
4. **Recently done** — DONE tasks since the last rotation, same columns.

Rules: one task = one outcome — a task needing sub-lists is several tasks; every task's origin is traceable (Article V): a backlog item, goal, issue, decision, or Owner request; DONE requires the [DoD](../../quality/DEFINITION_OF_DONE.md) plus evidence refs; TASKS holds *what and state*, the session log holds *how it went*.

## Skeleton

```markdown
# Tasks — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-08 |
| Document | TASKS.md |
| Class | I — Snapshot |
| Profile-tier | Minimal+ |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

Next ID: T-001

## Active
| ID | Title | State | Role | Refs | Note |
|---|---|---|---|---|---|

## Recently done
| ID | Title | Done in | Evidence |
|---|---|---|---|
```

## Maintenance Notes

The tell of a healthy instance: TASKS matches what is actually happening, minute by minute (M3.2 — status changes are not batched to Stage 6). A BLOCKED task without a blocking ref is malformed (E31).

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: four-state model, structure, rotation |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 5 forward references (R8.3) |

## Future Extension Notes

If real projects need estimates or priorities on tasks, add columns by evidence (P9) — the state model itself is stable.
