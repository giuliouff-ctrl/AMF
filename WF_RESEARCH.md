# Workflow — Research

| Field | Value |
|---|---|
| ID | WFLW-10 |
| Document | WF_RESEARCH.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for investigation: answer a question once, keep the answer forever. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Investigate with method and preserve findings as evidence — so no question is researched twice and no decision rests on vibes.
**Scope.** Investigation and findings. The decisions findings enable run through the normal D2/D3 chain.
**Responsibilities.** Steps, roles, aborts.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_RESEARCH row), templates/RESEARCH.md, templates/OPEN_QUESTIONS.md.
**Consumers.** Architect (lead), Product Analyst (business questions), Orchestrator.
**Related documents.** [MESSAGE_TYPES.md §2.9](../communication/MESSAGE_TYPES.md) (Proposal — a frequent output).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 8: a Q-NNN needs investigation; a pending decision needs evidence |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_RESEARCH |
| Roles | Architect (technical lead) or Product Analyst (business questions); Orchestrator |
| Gates | G5 only — research has no build chain; its rigor lives in the method |
| Key E-codes | E21 (conclusion), E20 (question answered), E17/E18 (assumptions touched), E19 (follow-ups) |
| Output | A RESEARCH entry (or folded equivalent) with method, evidence, conclusion; the question answered or honestly narrowed |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | lead | **Read before investigating**: related RESEARCH entries (the ledger's whole point), the Q-NNN's context, standing assumptions in the area |
| 2 | lead | Fix the question precisely (answerable as phrased — templates/OPEN_QUESTIONS.md rule) and the **method**: what will be read/tested/measured, and what evidence would decide it either way |
| 3 | lead | Investigate per method; evidence collected as it appears (links, numbers, test outputs) — not reconstructed after |
| 4 | lead | Conclude with confidence stated: the answer, its strength, what would overturn it. Dead ends are findings too (knowing X doesn't work is worth keeping) |
| 5 | lead | E21: entry written (method/evidence/conclusion split honest — future sessions re-judge old evidence under new constraints); E20 if it answers the Q-NNN; Proposal/Decision Request if it enables a decision; new Q-NNNs for what it opened |
| 6 | Orchestrator | G5; anything the findings invalidate propagates (E18 cascade if an assumption fell) |

## Failure and Abort Paths

- **Question turns out to be a decision in disguise** ("which X should we…" with adequate evidence already): stop researching, route the Decision Request — research is for missing evidence, not decision avoidance (Article XIII).
- **Method can't reach the evidence** (needs Owner data, paid access, real-world trial): the *narrowed* question with what's blocking becomes the finding; blocked part routes (E19 Owner-bound, or a D3 request if it needs spending).
- **Investigation sprawls**: the method from step 2 is the budget — sprawl means re-planning with a sharper question, logged.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

None anticipated; the method-first discipline is stable.
