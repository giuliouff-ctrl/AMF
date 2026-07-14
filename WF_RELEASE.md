# Workflow — Release

| Field | Value |
|---|---|
| ID | WFLW-08 |
| Document | WF_RELEASE.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for shipping: gates G4–G6, the cut, the deploy, the record. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Ship releases the Owner can trust and undo: verified scope, honest known-issues accounting, recorded approval, concrete rollback.
**Scope.** One release. Building its content was prior sessions' work; this workflow ships it.
**Responsibilities.** Steps, roles, gates, aborts for shipping.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_RELEASE row), [QUALITY_GATES.md](../quality/QUALITY_GATES.md) (G5/G6), templates/RELEASE_HISTORY.md, templates/CHANGELOG.md, [AI_CONSTITUTION.md Article I](../core/AI_CONSTITUTION.md).
**Consumers.** Release Manager (lead), QA Engineer, Orchestrator, Human Owner (G6).
**Related documents.** [roles/RELEASE_MANAGER.md](../agents/roles/RELEASE_MANAGER.md).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 3: ship/deploy/publish (milestone reached, Owner request) |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_RELEASE |
| Roles | Release Manager (lead), QA Engineer, Orchestrator, **Human Owner** (G6 — D3, every profile, always) |
| Gates | G5 → G6 (G4 state *checked*, not re-run, unless stale) |
| Key E-codes | E23 (the cut + entry + propagations), E09 (the approval), E29 |
| Output | Shipped, recorded, revertible release |

## Steps

| # | Gate | Role | Action |
|---|---|---|---|
| 1 | — | Release Manager | Freeze scope: what ships = CHANGELOG §Unreleased as it stands; late additions need their own full gate chains — no drive-by scope |
| 2 | — | QA Engineer | Readiness check: G4 records exist and are current for the scope; open-issues accounting compiled — every OPEN with severity, CRITICALs flagged (an open CRITICAL makes ship/hold an Owner question, packaged now) |
| 3 | G5 | Release Manager | Knowledge check per [checklist](../quality/QUALITY_GATES.md): matrix walked, CURRENT_STATUS true, DECISIONS complete, TASKS honest — an inconsistent instance ships nothing |
| 4 | — | Release Manager | Assemble the package: scope headline · CHANGELOG section · verification evidence · full known-issues list · **concrete rollback path** ("revert deployment <id>", not "roll back") |
| 5 | G6 | Orchestrator → Human Owner | Package presented plainly (P4.4); the Owner decides — ship, hold, or ship-with-known as an informed choice. **No deploy before this yes** (Article I; the RM's defining prohibition) |
| 6 | — | Release Manager | Approval recorded: D-NNN (E09) + Approval message; **the cut** (Unreleased → version block); deploy per the project's ship path (ARCHITECTURE §Environments) |
| 7 | — | QA Engineer | Post-deploy smoke pass on the primary flows at the target — shipped means *verified running*, not *uploaded* |
| 8 | — | Release Manager | E23 propagations: RELEASE_HISTORY entry (audit-sufficient, rollback included), ROADMAP milestone (E29), CURRENT_STATUS deploy state; session closes normally |

## Failure and Abort Paths

- **G6 denied / hold** → recorded (the denial is Owner direction: MEETING_NOTES/E22 + decisions as applicable); scope stays cut-ready; nothing deploys.
- **Deploy fails** → execute the package's rollback path *now*; incident recorded (E13/E15 as applicable, E26 if systemic); Owner informed immediately; the release entry records the failed attempt honestly (Article IV — RELEASE_HISTORY is the audit trail either way).
- **Smoke fails post-deploy** → rollback per path unless the Owner, informed, accepts ship-with-known on the spot (D3 either way); never "fix forward silently".
- **G5 fails** → documentation pass first (its failure routing); the release waits for a consistent instance.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

Multi-environment chains (staging→prod) extend steps 6–7 per target with per-target G6 sub-approvals — flagged in the RM contract and RELEASE_HISTORY standard; additive.
