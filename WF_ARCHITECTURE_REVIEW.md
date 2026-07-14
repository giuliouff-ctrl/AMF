# Workflow — Architecture Review

| Field | Value |
|---|---|
| ID | WFLW-06 |
| Document | WF_ARCHITECTURE_REVIEW.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for auditing a project's design as a whole. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Periodically (or on signal) ask the questions daily work never asks: is the design still right, are the decisions still valid, is the debt still chosen, are the risks still the ones we wrote down?
**Scope.** Audit and findings. Executing structural changes is WF_REFACTORING's; deciding them is the normal D2/D3 chain.
**Responsibilities.** Steps, roles, aborts.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_ARCHITECTURE_REVIEW row — the widest T1 in the framework, deliberately), [REVIEW_STANDARDS.md §3](../quality/REVIEW_STANDARDS.md).
**Consumers.** Architect (lead), Reviewer, Orchestrator, QA Engineer.
**Related documents.** [WF_REFACTORING.md](WF_REFACTORING.md), templates/RISK_REGISTER.md, templates/TECHNICAL_DEBT.md.
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 9: pre-milestone, defect-pattern signal (from WF_BUGFIX exits), invalidated load-bearing assumption (E18), or scheduled |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_ARCHITECTURE_REVIEW |
| Roles | Architect (lead), Reviewer (independent check on the Architect's findings — Article IX applies to audits too), QA (defect-pattern input), Orchestrator |
| Gates | G5 (the audit's own record); any resulting work carries its own gates later |
| Key E-codes | E08 (decisions from findings), E15/E16 (risk changes), E24 (newly recognized *deliberate* debt only — see abort notes), E31, E21 |
| Output | An audit record with findings and dispositions; refreshed risk/debt registers; action items as tasks/backlog |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | Architect | Tree-vs-document audit: ARCHITECTURE.md against reality (the tree is the fact — templates/ARCHITECTURE.md rule); every divergence is E31, fixed or logged now |
| 2 | Architect | Invariants audit: each §Invariants item — still true? still *right*? (an invariant nobody needs is structure debt) |
| 3 | Architect | Decision validity pass over the DECISIONS index: which records' premises have changed (new facts = the only key that reopens — superseding entries, not edits) |
| 4 | QA Engineer | Defect-pattern input: issue clusters by area/cause — what is the code saying the design got wrong? |
| 5 | Architect | Debt & risk sweep: TECHNICAL_DEBT triggers fired? RISK_REGISTER still the true top risks (theater check)? ASSUMPTIONS still standing? |
| 6 | Reviewer | Independent check of the findings set per [REVIEW_STANDARDS.md §3](../quality/REVIEW_STANDARDS.md) — the Architect's audit of its own design is exactly the case Article IX exists for |
| 7 | Orchestrator | Dispositions: findings → decisions (E08), risks (E15/E16), refactor items (TECHNICAL_DEBT/BACKLOG), Owner items (D3 packaging where scope/cost surfaced); audit record written (RESEARCH entry at Full, session log otherwise); G5 |

## Failure and Abort Paths

- **Audit finds accidental mess** (not chosen): that's issues/refactor items, never retroactive "debt" (the register doesn't launder — templates/TECHNICAL_DEBT.md rule).
- **Findings exceed the session**: prioritized honestly, top items dispositioned, rest recorded with the boundary named — an unfinished audit that says so beats a finished-looking one (Article IV).
- **Design fundamentally wrong for current goals**: that's a D3 conversation (cost/scope) — packaged for the Owner with options, not heroically re-architected in place.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

A lightweight cadence suggestion (e.g. every N sessions / pre-milestone) may become a PROFILES-level default once real-project evidence exists (P9).
