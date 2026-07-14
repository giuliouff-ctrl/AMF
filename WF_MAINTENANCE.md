# Workflow — Maintenance

| Field | Value |
|---|---|
| ID | WFLW-09 |
| Document | WF_MAINTENANCE.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for upkeep: dependency updates, housekeeping batches, framework upgrades. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Keep projects healthy between feature pushes: dependencies current-enough, small items cleared in batches, the instance's framework pin current — all with the same gate discipline, proportionally applied.
**Scope.** Upkeep batches and framework upgrades (E28). Individual defects exit to WF_BUGFIX; structural work to WF_REFACTORING.
**Responsibilities.** Steps, roles, aborts; the framework-upgrade path.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_MAINTENANCE row), templates/DEPENDENCIES.md, [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md) (E28 path).
**Consumers.** Engineer (lead), QA Engineer, Orchestrator.
**Related documents.** [VERSIONING.md §4](../core/VERSIONING.md) (pinning).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 7: dependency updates, housekeeping batch, framework upgrade |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_MAINTENANCE |
| Roles | Engineer (lead), QA Engineer (regression), Orchestrator; Architect on D2s (majors) |
| Gates | G2 → G3-light/G4 (regression-focused; profile merging per Q5 applies naturally here) → G5 |
| Key E-codes | E12 (each dependency change), E28 (framework upgrade), E14 (batch fixes), E25 |
| Output | Updated, verified, recorded upkeep; or an upgraded instance pin |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | Engineer | Read the constraint column first (templates/DEPENDENCIES.md — it exists for this step); plan the batch: what updates, what stays pinned and why, what the project's update policy says |
| 2 | Engineer / Architect | Patch/minor updates within policy = D1 batch; **majors and anything on the constraint list = D2 each** (Decision Request — a major is an interface change by definition) |
| 3 | Engineer | Apply; E12 per change (purpose/constraint columns updated — the *why* travels with the what); G2 with evidence |
| 4 | QA Engineer | Regression pass proportional to the batch's blast radius (a lockfile refresh ≠ a framework major); results recorded |
| 5 | Release Manager | G5; CHANGELOG lines only for user-visible effects (E12 conditional) |

**Framework upgrade path (E28)**: steps 1–5 with the "dependency" being AMF itself — executed per [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md): read release notes → apply migrations in order → bump `amf_version` in INSTANCE.md → verify per the guide's checklist → record (E28: INSTANCE, CHANGELOG, SESSION_LOG). One version state at a time — never partially migrated ([VERSIONING.md §8](../core/VERSIONING.md)).

## Failure and Abort Paths

- **Update breaks something** → the constraint column earns its keep: revert, record the constraint ("pinned: vN breaks X"), I-NNN if the breakage matters upstream, move on — a maintenance session never grinds on one dependency.
- **Update requires code changes beyond trivial** → that's feature/refactor work: task created, update deferred with the reason on the row.
- **Framework migration fails** → rollback to the pinned version (never between versions); failure recorded, Proposal to the framework if the migration notes were wrong (that's a framework defect).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure incl. framework-upgrade path |

## Future Extension Notes

Scheduled-maintenance cadence defaults per profile may land in PROFILES on evidence; the procedure is cadence-agnostic.
