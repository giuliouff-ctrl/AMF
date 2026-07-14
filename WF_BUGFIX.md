# Workflow — Bug Fix

| Field | Value |
|---|---|
| ID | WFLW-04 |
| Document | WF_BUGFIX.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for defect resolution: reproduce, find the cause, fix, verify, close. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Fix defects at the cause, with evidence, without regressions — and leave the record that prevents rediscovery.
**Scope.** One I-NNN (or a freshly reported defect that becomes one at step 1). Systemic patterns exit to WF_ARCHITECTURE_REVIEW.
**Responsibilities.** Steps, roles, gates, aborts for defect work.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_BUGFIX row), [DEFINITION_OF_DONE.md §4](../quality/DEFINITION_OF_DONE.md), [QUALITY_GATES.md](../quality/QUALITY_GATES.md), templates/KNOWN_ISSUES.md.
**Consumers.** QA Engineer, Engineer, Architect (structural causes), Reviewer.
**Related documents.** [WF_REFACTORING.md](WF_REFACTORING.md) (architectural-cause exit).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 4: something broken / an I-NNN addressed |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_BUGFIX |
| Roles | QA Engineer (repro + verification), Engineer (cause + fix), Architect (if structural), Reviewer |
| Gates | G2 → G3 → G4 → G5 (G0/G1 satisfied by the issue record + cause analysis) |
| Key E-codes | E13 (if new), E14, E08 (structural cause), conditional E12/E24 |
| Output | Issue RESOLVED per [DoD §4](../quality/DEFINITION_OF_DONE.md), with root cause named |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | QA Engineer | Confirm/complete the I-NNN: reproduction, observed vs expected, severity honest. New defect without a record → E13 first (found means recorded) |
| 2 | Engineer | **Cause analysis** before any fix: trace to the root; name it. Symptom-patch only as an explicitly accepted scope (D-ref per DoD B.1) |
| 3 | Engineer / Architect | If the cause is structural → Decision Request (D2, Architect); if the cause *is the design* → abort path below |
| 4 | Engineer | Fix at the cause; guard added where the project's approach supports it (B.5); G2 declared with evidence |
| 5 | Reviewer | G3 per standards — fidelity, no smuggled scope, conventions |
| 6 | QA Engineer | G4: original repro no longer reproduces (demonstrated); regression check on everything sharing the mechanism (B.3); close E14 with evidence |
| 7 | Release Manager | G5; CHANGELOG line if user-visible (E14 conditional) |

## Failure and Abort Paths

- **Cannot reproduce** → issue updated with attempts + evidence, status stays OPEN/INVESTIGATING, routed back to its reporter with precise questions (E19 if Owner-side); no "works for me" closures (Article IV).
- **Cause is architectural** → stop; the fix becomes a WF_REFACTORING or WF_FEATURE via re-plan (D2/D3 as applicable); an interim mitigation may ship as its own honest symptom-patch with D-ref + debt entry (E24).
- **Fix breaks something else** (G4 catches it) → new I-NNN, back to step 2 — regressions are new defects, not iterations to hide.
- **Defect pattern detected** (same area/cause repeatedly) → QA connects the dots: Risk Report or Architecture Review proposal — this workflow stops absorbing what is structurally broken.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

A production-incident variant (time pressure, comms duties) is the anticipated WF_INCIDENT (Index future note); until it exists, incidents run here with the Owner informed early per §5.1 triggers.
