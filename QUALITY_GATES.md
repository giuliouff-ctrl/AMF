# Quality Gates

| Field | Value |
|---|---|
| ID | QUAL-02 |
| Document | QUALITY_GATES.md |
| Module | quality |
| Class | S — Stable spec |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | QA Engineer (content) / Architect (model) |
| Maintainer | Architect |
| Authority | Normative per-gate checklists G0–G6. Every criterion is binary and evidence-checkable. Subordinate to [QUALITY_SYSTEM.md](QUALITY_SYSTEM.md). |

---

## Document Contract

**Purpose.** Give every gate its objective checklist: the exact criteria that must all hold for the gate to pass.
**Scope.** Criteria only. Mechanics (evidence, failure, merging) are [QUALITY_SYSTEM.md](QUALITY_SYSTEM.md)'s; authority is [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md)'s; when gates run is each workflow's.
**Responsibilities.** Seven checklists; per-gate evidence form and failure routing.
**Dependencies.** [QUALITY_SYSTEM.md](QUALITY_SYSTEM.md), [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) (G2/G3 cite it), [REVIEW_STANDARDS.md](REVIEW_STANDARDS.md) (G1/G3 verdict source), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) (G5 walks it).
**Consumers.** Gate checkers per the authority map; all roles preparing work for gates.
**Related documents.** templates/* (documents the criteria inspect).
**Update policy.** D2 (Architect); checklist items are the expected MINOR evolution — through governance, never mid-review (Article XI).

---

## How to Read

All criteria of a gate must hold — one miss is FAIL (binary, Q1). *Checked by* per [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md), restated one-line here for usability only. Evidence per Q3 rules.

## G0 — Requirements Ready

*Declared by Product Analyst; buildability confirmed by Architect.*

| # | Criterion |
|---|---|
| 0.1 | The work item traces to a goal (G-ref) or an explicit Owner wish (MEETING_NOTES ref) |
| 0.2 | Acceptance criteria exist and are checkable — each one answerable yes/no by G4 |
| 0.3 | Constraints named (from PROJECT §Constraints and ARCHITECTURE, as applicable) |
| 0.4 | Out-of-scope stated where ambiguity is plausible |
| 0.5 | Architect confirms buildability within current architecture, or names the D2 the work will require |

Evidence: the task's criteria block (TASKS/BACKLOG promotion record). Failure: back to the Product Analyst; if the gap is Owner-side, a routed question (E19).

## G1 — Design Approved

*Authored by Architect; checked by Reviewer per [REVIEW_STANDARDS.md §3](REVIEW_STANDARDS.md).*

| # | Criterion |
|---|---|
| 1.1 | The design serves every G0 acceptance criterion (traceable, criterion by criterion) |
| 1.2 | ARCHITECTURE §Invariants respected — none broken, none silently redefined |
| 1.3 | Every D2 the design embodies has its Decision Record (D-NNN refs present) |
| 1.4 | ARCHITECTURE.md updated (E11) or its same-session update is in the plan |
| 1.5 | No undeclared debt: shortcuts are E24-registered with triggers, or absent |
| 1.6 | Proportionality: the design is as simple as the criteria allow (P7/P9 — Reviewer judgment against the written principles) |
| 1.7 | Review Report verdict: PASS |

Evidence: the Review Report. Failure: findings to the Architect; second same-cause FAIL escalates (Q4.2).

## G2 — Implementation Complete

*Self-declared by Engineer, evidence mandatory (Q3.3).*

| # | Criterion |
|---|---|
| 2.1 | Every acceptance criterion addressed (claimed with pointers, not "all done") |
| 2.2 | [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) self-check walked for the work type, results listed |
| 2.3 | Project conventions followed (ARCHITECTURE §Conventions) |
| 2.4 | Dependency changes recorded (E12) with their D-NNNs |
| 2.5 | Known gaps and un-checked areas declared explicitly (Article IV — the honest-gaps list is part of the declaration) |
| 2.6 | No secrets in code; configuration externalized |

Evidence: the G2 declaration block in the session log — built/checked/not-checked. Failure: n/a (an incomplete G2 is simply not declared); a *false* G2 discovered later voids downstream gates (Q4.3).

## G3 — Review Passed

*Checked by Reviewer per [REVIEW_STANDARDS.md §2](REVIEW_STANDARDS.md).*

| # | Criterion |
|---|---|
| 3.1 | Implementation matches the approved design (G1's) — deviations have their D-NNNs |
| 3.2 | Code review standard passed (correctness, conventions, error handling, security basics, maintainability — §2 of the standards) |
| 3.3 | No undeclared debt or silent D2 (the two canonical smells checked explicitly) |
| 3.4 | ARCHITECTURE.md still true of the tree after this change |
| 3.5 | DoD conformance plausible on inspection (full conformance is G4's to verify behaviorally) |
| 3.6 | Review Report verdict: PASS; BLOCKING findings: none open |

Evidence: the Review Report. Failure: findings to the Engineer; Q4.2 applies.

## G4 — Verification Passed

*Checked by QA Engineer.*

| # | Criterion |
|---|---|
| 4.1 | Every G0 acceptance criterion exercised, result recorded per criterion |
| 4.2 | Regression pass on the change's blast radius (adjacent features, shared components, written data) — scope named, results recorded |
| 4.3 | No new CRITICAL issues; new non-critical issues registered (E13) with severities |
| 4.4 | DoD verification items for the work type confirmed behaviorally |
| 4.5 | Evidence inspectable: what was run/clicked/compared, and what it showed |

Evidence: the verification record (criterion-by-criterion). Failure: to the Engineer with the failing criteria; Q4.2 applies.

## G5 — Knowledge Updated

*Checked by Release Manager.*

| # | Criterion |
|---|---|
| 5.1 | [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) walked for every event in scope — each event's mandatory targets updated (M3.3) |
| 5.2 | CURRENT_STATUS.md refreshed and true |
| 5.3 | CHANGELOG §Unreleased current for the scope's user-visible work |
| 5.4 | DECISIONS.md complete: no known decision without its record |
| 5.5 | TASKS.md true: states match reality, done work marked with evidence refs |
| 5.6 | Touched documents stamped (R10.2) and internally consistent |

Evidence: the walked-matrix note (events × targets). Failure: a documentation pass before anything proceeds — an inconsistent instance ships nothing.

## G6 — Release Approved

*Decided by the Human Owner (D3); requested by Release Manager.*

| # | Criterion |
|---|---|
| 6.1 | Package complete: scope headline; CHANGELOG section; verification evidence (G4 refs); full open-issues accounting with severities; concrete rollback path |
| 6.2 | G0–G5 records exist for the release scope (or their profile-merged equivalents, Q5.3) |
| 6.3 | Owner approval given on the *true* package (Article IV — approving a softened picture voids the gate) |
| 6.4 | Approval recorded: D-NNN (E09) + Approval message + RELEASE_HISTORY entry reference |

Evidence: the release package + the recorded approval. Failure: hold — the ship/hold call with known issues is the Owner's, fully informed, never engineered around.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 5 | Initial seven checklists |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Per-technology annexes attach as `G4-annex-<tech>` extensions of 4.2/4.4 (e.g. web: responsive matrix, console cleanliness, Lighthouse targets *as recorded project targets*, not universal numbers) — additive, evidence rules unchanged.
