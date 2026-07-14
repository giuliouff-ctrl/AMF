# Standard — ROADMAP.md

| Field | Value |
|---|---|
| ID | KNOW-07 |
| Document | templates/ROADMAP.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `ROADMAP.md` — milestones and direction. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the roadmap: the time-shaped view of the project — milestones, their meaning, and current direction.
**Scope.** Structure and rules of `ROADMAP.md`; not the work items themselves (BACKLOG/TASKS), not business goals (PROJECT).
**Responsibilities.** Specification, structure, milestone rules, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; templates/PROJECT.md (goals it sequences).
**Consumers.** Product Analyst (owner), Human Owner (expectations), Release Manager (release targets), Orchestrator (planning).
**Related documents.** templates/RELEASE_HISTORY.md (milestones shipped); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E09/E23/E29.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/ROADMAP.md` |
| Class | I — Snapshot |
| Knowledge domain | Business |
| Owner (role) | Product Analyst |
| Default read tier | T1 (WF_RELEASE: the milestone), T2 otherwise |
| Profile | Standard+ (Minimal: folds into PROJECT per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E29 (milestone reached/moved), E23 (release), E09 (D3 affecting milestones) |
| Required inputs | Owner's priorities and dates; delivery reality from sessions |
| Expected outputs | Honest answer to "what lands when, and what's after that?" |
| Archive policy | Completed milestones rotate to `archive/ROADMAP_<YYYY>.md` after their release ships (K7.3) |

## Structure

1. **Header** — per standard.
2. **Now / Next / Later** — three horizons: *Now* (the active milestone), *Next* (the following one, shaped), *Later* (direction, unshaped). Deliberately only the first has dates you can hold.
3. **Milestones** — table per milestone: name · target date (or "unscheduled") · definition of reached · goals served (G-refs) · status (PLANNED / ACTIVE / REACHED / MOVED-with-D-ref).
4. **Direction notes** — the PA's reading of where this is going; explicitly non-binding.

Rules: milestone dates move only with a recorded reason (E29 entry cites what moved it — a D-NNN for scope-driven moves, otherwise the session); "reached" is defined *when the milestone is created*, not when it is claimed (Article X spirit); milestones are named plainly ("Public launch", "Client handoff") — no versions here, versions belong to releases.

## Skeleton

```markdown
# Roadmap — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-07 |
| Document | ROADMAP.md |
| Class | I — Snapshot |
| Profile-tier | Standard+ |
| Owner | Product Analyst |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Now
**<milestone>** — target <date>. <one line>

## Next
**<milestone>** — <shape>

## Later
- <direction>

## Milestones
| Milestone | Target | Reached means | Serves | Status |
|---|---|---|---|---|

## Direction notes
<non-binding read of the trajectory>
```

## Maintenance Notes

Small client projects often have exactly two milestones ("launch", "handoff") — that is a complete roadmap; do not pad it (P9). The document earns its place when the Owner asks "when?": the answer should already be here.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: three-horizon model, milestone rules |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

If milestone cross-referencing becomes common, M-NN IDs are the candidate (R4 addition); withheld pending evidence.
