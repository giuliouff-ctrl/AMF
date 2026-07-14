# Workflow — New Project

| Field | Value |
|---|---|
| ID | WFLW-02 |
| Document | WF_NEW_PROJECT.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for bringing a project under AMF: instantiation, discovery, initial knowledge. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Turn "let's build X" into a working instance with real knowledge: profile chosen, documents instantiated, scope discovered, architecture decided, first plan standing.
**Scope.** From no-instance to ready-for-WF_FEATURE. Instantiation mechanics live in [ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md); this workflow sequences them with discovery.
**Responsibilities.** Steps, roles, gates, aborts for project bootstrap.
**Dependencies.** [ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md), [PROFILES.md](../operations/PROFILES.md), [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_NEW_PROJECT row), [QUALITY_GATES.md](../quality/QUALITY_GATES.md) (G0, G1).
**Consumers.** Orchestrator (lead), Product Analyst (discovery lead), Architect.
**Related documents.** templates/* (what gets instantiated).
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 2: no `.amf/` exists (also: existing codebase adopting AMF) |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_NEW_PROJECT |
| Roles | Orchestrator (lead), Product Analyst, Architect; Human Owner (inputs, profile D3) |
| Gates | G0 (initial scope), G1 (initial architecture) |
| Key E-codes | E27 (configuration), E22 (discovery inputs), E08 (stack D2s), E01/E02 |
| Output | A complete, consistent instance: ready for the first WF_FEATURE session |

## Steps

| # | Role | Action | Emits / records |
|---|---|---|---|
| 1 | Orchestrator | Instantiate per [ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md): profile choice with the Owner (configuration is D3-backed), `.amf/` skeletons per profile, CLAUDE.md bootstrap, INSTANCE.md pinned | E27 + D-NNN |
| 2 | Product Analyst | **Discovery** with the Owner: identity, goals, users, scope, constraints, references — per the adoption guide's discovery method (MADRE binding, §4 there). Batched questions, defaults proposed, near-verbatim capture | E22 (MEETING_NOTES at Full; direct propagation at folds); PROJECT.md content |
| 3 | Product Analyst | Write PROJECT.md: vision, testable goals (G-IDs), non-goals, scope, constraints, success criteria; seed BACKLOG (and ROADMAP at Standard+) | G0 declared on initial scope |
| 4 | Architect | Confirm buildability (G0 item 0.5); make the founding D2s — stack, structure, data approach — honoring the Owner's standing constraints (e.g. free-tier posture from PROJECT §Constraints) | Decision Requests → E08 records |
| 5 | Architect | Write ARCHITECTURE.md: overview, stack (D-refs), components, conventions, invariants; DEPENDENCIES at Standard+ | E11-equivalent initial write |
| 6 | Reviewer (per profile: Orchestrator cross-check at Minimal, C8.3) | G1 on the initial architecture — fit to goals, simplicity (P9: no speculative structure in a day-one design) | Review Report |
| 7 | Orchestrator + PA | First plan: promote the first backlog items (E03, acceptance criteria per G0), CURRENT_STATUS first honest write, ROADMAP §Now | TASKS, CURRENT_STATUS |
| 8 | Orchestrator | Adoption verification checklist ([ADOPTION_GUIDE.md §6](../operations/ADOPTION_GUIDE.md)); DOCUMENT + HANDOVER as usual | E02 |

## Failure and Abort Paths

- **Owner unavailable mid-discovery**: record what stands (E22 partial), park precise gaps as Owner-routed questions (E19), close the session honestly — a half-discovered project is stated as such in CURRENT_STATUS, never padded with assumptions (Article IV; anything assumed goes through E17 explicitly).
- **Existing codebase**: step 5 becomes *reverse-engineering* — ARCHITECTURE.md describes what exists (verified against the tree), unknowns marked unknown; a follow-up WF_ARCHITECTURE_REVIEW is seeded in BACKLOG.
- **Profile doubt**: start one lighter (P8) — upgrading is cheap ([PROFILES.md §5](../operations/PROFILES.md)), shrinking mid-project is a D3.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

If discovery templates evolve (MADRE revisions), only the adoption guide's binding section changes — this sequence is method-agnostic.
