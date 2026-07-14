# Workflow — Refactoring

| Field | Value |
|---|---|
| ID | WFLW-05 |
| Document | WF_REFACTORING.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for behavior-preserving structural change and debt retirement. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Change structure without changing behavior — provably — and retire the debt that motivated it.
**Scope.** One refactoring effort (typically a TECHNICAL_DEBT item). Behavior changes exit to WF_FEATURE/WF_BUGFIX.
**Responsibilities.** Steps, roles, gates, aborts.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_REFACTORING row), [DEFINITION_OF_DONE.md §5](../quality/DEFINITION_OF_DONE.md), templates/TECHNICAL_DEBT.md.
**Consumers.** Architect (lead), Engineer, Reviewer, QA Engineer.
**Related documents.** [WF_BUGFIX.md](WF_BUGFIX.md), [WF_ARCHITECTURE_REVIEW.md](WF_ARCHITECTURE_REVIEW.md).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 6: structural improvement, no behavior change; typically a debt item's repayment trigger firing |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_REFACTORING |
| Roles | Architect (lead: scope + design), Engineer, Reviewer, QA Engineer |
| Gates | G1 (refactor design) → G2 → G3 → G4 (behavior preservation) → G5 |
| Key E-codes | E25 (debt retired), E11 (structure moved), conditional E12 |
| Output | Same behavior, better structure, debt row RETIRED per [DoD §5](../quality/DEFINITION_OF_DONE.md) |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | Architect | Scope from the debt item (its D-ref carries the original intent); define the target structure and — critically — the **behavior baseline**: which flows must demonstrably not change |
| 2 | QA Engineer | Capture the baseline evidence *before* any change: the flows exercised, results recorded (this is R.1's "before") |
| 3 | Reviewer | G1 on the refactor design: pays for itself (P7), no scope smuggling planned, invariants intact |
| 4 | Engineer | Refactor; anything functional discovered en route becomes its own task (R.2 — logged, parked); G2 with evidence |
| 5 | Reviewer | G3: fidelity to the refactor design; conventions; the diff contains structure only |
| 6 | QA Engineer | G4 = **before/after comparison** on the baseline flows (R.1's "after"); regression on the blast radius |
| 7 | Architect | E25: debt row retired (or remaining scope re-recorded honestly); E11: ARCHITECTURE true again |
| 8 | Release Manager | G5; CHANGELOG only if externally visible (usually silent — internal work) |

## Failure and Abort Paths

- **Behavior change turns out necessary** → stop: that is a design finding, not a refactor step. Decision Request (D2); the effort re-plans as feature/fix + refactor, separately gated.
- **Baseline can't be captured** (untestable area) → that *is* the first debt to retire: make it observable first, or record the accepted risk (E15) with the Owner informed if user-facing.
- **Refactor grows** ("while we're here") → P9 discipline: the planned scope completes; discoveries go to TECHNICAL_DEBT/BACKLOG. A refactor that never converges is scope creep in structural clothing.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

None anticipated; the baseline-first discipline is the load-bearing idea and is stable.
