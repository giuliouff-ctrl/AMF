# Workflow — Feature

| Field | Value |
|---|---|
| ID | WFLW-03 |
| Document | WF_FEATURE.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for building a new capability, G0 through G5 (+G6 when it ships). The framework's most-used workflow. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Sequence the full engineering chain for new capability: defined → designed → built → reviewed → verified → recorded.
**Scope.** One committed feature (a promoted backlog item / T-NNN). Shipping is WF_RELEASE's unless the session ships immediately (then G6 appends here by reference).
**Responsibilities.** Steps, roles, gates, aborts for feature work.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_FEATURE row), [QUALITY_GATES.md](../quality/QUALITY_GATES.md), [DEFINITION_OF_DONE.md §3](../quality/DEFINITION_OF_DONE.md), [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md).
**Consumers.** All roles.
**Related documents.** [WF_RELEASE.md](WF_RELEASE.md), templates/TASKS.md, templates/BACKLOG.md.
**Update policy.** D2 (Architect). Its T1 row is the framework's first flagged tuning candidate.

## Specification

| | |
|---|---|
| Trigger | Selection rule 5: new capability / user-visible behavior change |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_FEATURE |
| Roles | Product Analyst, Architect, Engineer, Reviewer, QA Engineer, Release Manager (G5); Orchestrator throughout |
| Gates | G0 → G1 → G2 → G3 → G4 → G5; G6 only if shipping this session (per [WF_RELEASE.md](WF_RELEASE.md) steps 4–7) |
| Key E-codes | E03–E05, E08, E11, E12, E13 (if found), E05→CHANGELOG |
| Output | Feature DONE per [DoD §3](../quality/DEFINITION_OF_DONE.md); knowledge current |

## Steps

| # | Gate | Role | Action |
|---|---|---|---|
| 1 | G0 | Product Analyst | Mature the item's acceptance criteria (promotion per templates/BACKLOG.md); constraints and out-of-scope named; Architect confirms buildability (0.5) |
| 2 | — | Orchestrator | Task created/claimed (E03/E04); D3 scan at PLAN (Article I — anything Owner-reserved in this feature is flagged *now*) |
| 3 | G1 | Architect → Reviewer | Design pass proportional to structure (never zero for structural work); D2s recorded at decision time (E08); ARCHITECTURE updated (E11); Reviewer checks per [REVIEW_STANDARDS.md §3](../quality/REVIEW_STANDARDS.md) |
| 4 | G2 | Engineer | Implement per design and conventions; dependencies via Decision Request + E12; mid-task D2 discoveries pause-and-request (never silent); G2 declared with evidence — built / checked / not-checked |
| 5 | G3 | Reviewer | Ritual ([REVIEW_STANDARDS.md §5](../quality/REVIEW_STANDARDS.md)) → review per §2 → Review Report; findings routed (E13 defects, E24 flags) |
| 6 | G4 | QA Engineer | Every acceptance criterion exercised with evidence; regression pass on blast radius; new issues registered honestly |
| 7 | G5 | Release Manager | Matrix walked (M3.3 scope); CHANGELOG §Unreleased line (E05, user language); CURRENT_STATUS refreshed |
| 8 | (G6) | per [WF_RELEASE.md](WF_RELEASE.md) | Only if shipping now — package, Owner approval, deploy, E23 |

## Failure and Abort Paths

- **Gate FAIL** → findings back to the authoring step; second same-cause FAIL escalates (Q4.2) — typical resolutions: criteria were wrong (back to G0), design was wrong (back to G1), scope was wrong (D3 to Owner).
- **Feature bigger than discovered** → stop at the moment of discovery; re-scope through PA (+D3 if scope changes); remainder to BACKLOG (E32) — never quietly absorbed.
- **Blocked on external/Owner input** → E06 + E19 (routed question), work parks, session proceeds elsewhere or closes honestly.
- **Bug discovered en route** → I-NNN (E13); absorbed only per the Index composition rule, else parked.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

Multi-session features are the norm at scale: each session runs steps up to a clean boundary, hands over per [SESSION_MANAGEMENT.md §6](../core/SESSION_MANAGEMENT.md); the gate chain resumes where the handover says.
