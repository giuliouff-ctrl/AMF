# Definition of Done

| Field | Value |
|---|---|
| ID | QUAL-03 |
| Document | DEFINITION_OF_DONE.md |
| Module | quality |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | QA Engineer (content) / Architect (model) |
| Maintainer | Architect |
| Authority | Normative definition of "done" per work type. Completion claims are made against this document, nowhere else. Subordinate to [QUALITY_SYSTEM.md](QUALITY_SYSTEM.md). |

---

## Document Contract

**Purpose.** Fix what "done" means, per work type, so completion is a checkable state instead of a feeling — the substance behind G2's self-check and G4's confirmation.
**Scope.** The four work types' DoD. Gate criteria ([QUALITY_GATES.md](QUALITY_GATES.md)) reference this; acceptance criteria (per task, from G0) complement it — DoD is the floor, criteria are the spec.
**Responsibilities.** The common core; four type-specific definitions; proportionality rules.
**Dependencies.** [QUALITY_SYSTEM.md](QUALITY_SYSTEM.md), [AI_CONSTITUTION.md](../core/AI_CONSTITUTION.md) (Articles IV, V, VI), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md).
**Consumers.** Engineer (G2 self-check), Reviewer (G3 plausibility), QA Engineer (G4 confirmation, conformance judgment).
**Related documents.** templates/TASKS.md (DONE state requires this), templates/KNOWN_ISSUES.md, templates/TECHNICAL_DEBT.md.
**Update policy.** D2 (Architect); items evolve MINOR through governance.

---

## 1. How DoD Works

- **D1.1** DoD is the **floor under every completion claim**: a task enters DONE only when its type's definition holds *and* its acceptance criteria pass. Criteria say what this work must do; DoD says what all work of this kind must be.
- **D1.2** DoD items are binary and never waived (Article X; the QA Engineer's first prohibition). An item genuinely inapplicable to a task is *declared* inapplicable in the G2 evidence with one line of why — silence is a violation, declaration is honesty (Article IV).
- **D1.3** **Proportionality lives in the criteria, not the DoD.** A landing page and a WMS differ in their acceptance criteria and project targets (recorded in PROJECT/ARCHITECTURE); the DoD below applies identically to both. This is how the bar stays fixed while effort scales (Q1 economy).

## 2. Common Core (every work type)

| # | Done means |
|---|---|
| C.1 | Acceptance criteria pass (or the goal it serves is met, for untasked work — which should not exist per Article V) |
| C.2 | Project conventions followed (ARCHITECTURE §Conventions) — the work is indistinguishable in style from the codebase's best |
| C.3 | Knowledge updated: every event the work caused has its matrix updates (E-codes applied, same session) |
| C.4 | No silent D2s, no undeclared debt (Articles VI; E24 for the declared kind) |
| C.5 | Honest state: whatever is not done, not checked, or fragile is written down (TASKS note, G2 gaps list, or I-NNN) |

## 3. Feature

Everything in §2, plus:

| # | Done means |
|---|---|
| F.1 | The feature works end-to-end through its primary flow — exercised, not assumed |
| F.2 | Project targets met where the project declares them (responsiveness, accessibility, performance — per PROJECT §Constraints / ARCHITECTURE §Conventions; absent declarations, the professional defaults the Architect has recorded) |
| F.3 | Error paths behave: invalid input, missing data, failed external calls — handled or explicitly declared out of scope in the criteria |
| F.4 | No new console errors / build warnings introduced (or equivalent cleanliness for the stack) |
| F.5 | CHANGELOG §Unreleased line written, user language (E05) |
| F.6 | In-code documentation updated where the project keeps it (per its conventions) |

## 4. Bug Fix

Everything in §2, plus:

| # | Done means |
|---|---|
| B.1 | Root cause identified and named in the fix's record — symptom-patching is declared as such if that is the accepted scope (D-ref) |
| B.2 | The reproduction from I-NNN no longer reproduces — demonstrated |
| B.3 | Regression check on the cause's area: what shares the mechanism, checked |
| B.4 | The issue closed properly (E14): resolution + evidence ref on the I-NNN row |
| B.5 | A guard proportionate to the defect added where the project's testing approach supports it (test, check, assertion) — or its absence declared with reason |
| B.6 | CHANGELOG line if user-visible (E14 conditional) |

## 5. Refactor

Everything in §2, plus:

| # | Done means |
|---|---|
| R.1 | Behavior preserved — demonstrated by before/after evidence on the affected flows (the refactor's own G4 substance) |
| R.2 | No functional change smuggled in (a fix or feature found mid-refactor becomes its own task — Article V) |
| R.3 | The motivating debt item retired (E25) or the remaining scope re-recorded honestly |
| R.4 | ARCHITECTURE.md true after the change (E11 where structure moved) |
| R.5 | The tree is simpler or better-factored *by the project's recorded conventions* — the Reviewer confirms the refactor paid for itself (P7) |

## 6. Documentation

Everything in §2, plus:

| # | Done means |
|---|---|
| K.1 | Content true against reality it describes — verified, not transcribed from memory (Article IV) |
| K.2 | Placed in the owning document (Article III) — no duplicated facts, references elsewhere |
| K.3 | Conventions per [FRAMEWORK_RULES.md](../core/FRAMEWORK_RULES.md) (headers, IDs, statuses, markdown) or the project's own documentation conventions, as applicable |
| K.4 | Cross-references resolve (R8.4) |
| K.5 | Update procedure applied (R10: version/stamp, revision row) |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 5 | Initial DoD: common core + four work types |

## Future Extension Notes

- A fifth work type (e.g. Migration/Upgrade, for E28 sessions) is the first expected addition — awaiting real-use evidence (P9).
- Per-stack cleanliness expansions of F.4 belong in G4 annexes ([QUALITY_GATES.md](QUALITY_GATES.md) future note), not here.
