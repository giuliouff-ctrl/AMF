# Workflow — Code Review

| Field | Value |
|---|---|
| ID | WFLW-07 |
| Document | WF_CODE_REVIEW.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for a standalone review session. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Review work as a session's whole purpose: accumulated changes, pre-adoption codebases, or an explicit "review this" request — with the same rigor as inline G3s.
**Scope.** Review and findings routing. Fixing anything found is *other* sessions' work (the Reviewer never patches).
**Responsibilities.** Steps, roles, aborts.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_CODE_REVIEW row), [REVIEW_STANDARDS.md](../quality/REVIEW_STANDARDS.md) (the entire method), [MESSAGE_TYPES.md §2.3](../communication/MESSAGE_TYPES.md).
**Consumers.** Reviewer (lead), Orchestrator, QA Engineer (findings intake).
**Related documents.** [WF_ARCHITECTURE_REVIEW.md](WF_ARCHITECTURE_REVIEW.md) (design-level counterpart).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 10: review as the session's purpose |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_CODE_REVIEW |
| Roles | Reviewer (lead); Orchestrator (scope + routing); QA Engineer (defect intake) |
| Gates | G3 for each item in scope; G5 |
| Key E-codes | E13 (defects found), E24 flags (undeclared debt), E31 (knowledge drift), E32 |
| Output | Review Report(s); findings routed into the instance as durable entities |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | Orchestrator | Fix the review scope explicitly: which changes/files/areas, against which criteria (the tasks' G0 criteria, or "conventions + standards" for scopeless audits) |
| 2 | Reviewer | The ritual, in full ([REVIEW_STANDARDS.md §5](../quality/REVIEW_STANDARDS.md)): assumption, standards re-read, non-authorship check per item |
| 3 | Reviewer | Review per [§2](../quality/REVIEW_STANDARDS.md) in blast-radius order; one Review Report per coherent scope unit — findings with references, locations, severities |
| 4 | QA / Architect / Orchestrator | Findings routed at report time: defects → E13; undeclared debt → E24 flags to Architect; knowledge drift → E31 fixes or entries; improvement NOTEs → BACKLOG/TECHNICAL_DEBT candidates |
| 5 | Orchestrator | Verdict consequences: FAILed items become rework tasks (E03) — this session routes, the fixing sessions fix; G5 close |

## Failure and Abort Paths

- **Non-authorship fails for the whole scope** (this session-thread wrote it all): the review waits for a genuinely cold session (A2.4). At Minimal, the C8.3 cross-check assignment stands in — but a scope authored *this same session* is never reviewable this session.
- **Scope too large for the session**: reviewed portion reported honestly; remainder becomes a follow-up review task with the exact boundary in the handover (never a skimmed "rest looks fine").
- **Standards gap found** (case the standards don't cover): stricter reading applies now; Proposal after (Article XI).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

Pre-adoption codebase audits (step-1 scope = "everything") pair naturally with WF_NEW_PROJECT's existing-codebase path — cross-referenced there.
