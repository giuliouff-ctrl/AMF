# Workflow — Documentation

| Field | Value |
|---|---|
| ID | WFLW-11 |
| Document | WF_DOCUMENTATION.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure for knowledge audit and repair — the session type that keeps the memory system trustworthy. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Audit and repair the instance's knowledge: fix drift, close E31 backlog, triage notes, rotate archives — so every other workflow can keep trusting what it reads.
**Scope.** The instance's knowledge health. Framework documentation work follows the same shape with framework documents as the subject.
**Responsibilities.** Steps, roles, aborts.
**Dependencies.** [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_DOCUMENTATION row), [KNOWLEDGE_SYSTEM.md §8](../knowledge/KNOWLEDGE_SYSTEM.md) (the quality rules audited against), [DEFINITION_OF_DONE.md §6](../quality/DEFINITION_OF_DONE.md).
**Consumers.** Orchestrator (lead), every domain owner for its documents.
**Related documents.** templates/AI_NOTES.md (triage rule executes here), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) E31.
**Update policy.** D2 (Architect).

## Specification

| | |
|---|---|
| Trigger | Selection rule 11: E31 accumulation, audit due, rotations pending, or reconstruction friction reported (C4.5 findings) |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_DOCUMENTATION (headers + structure — an audit pass, not a full read) |
| Roles | Orchestrator (lead); each domain owner repairs its own documents (M4.3 single-writer) |
| Gates | G5 — this workflow *is* an extended G5; docs work meets [DoD §6](../quality/DEFINITION_OF_DONE.md) |
| Key E-codes | E31 (each fix), E30 triage, E26 (systemic findings) |
| Output | A consistent instance; triaged notes; rotated archives; an honest health line in CURRENT_STATUS |

## Steps

| # | Role | Action |
|---|---|---|
| 1 | Orchestrator | Audit pass per [K8 rules](../knowledge/KNOWLEDGE_SYSTEM.md): every active document — header current? stamps recent? structure per template? no empty sections? density honest? |
| 2 | Orchestrator | Consistency pass: snapshots vs ledgers (M4.1 — ledger wins), CURRENT_STATUS vs TASKS vs KNOWN_ISSUES cross-check, entity refs resolve (R4.4), links resolve (R8.4) |
| 3 | domain owners | Repairs, each by its owner (E31 per fix, stamped): truth fixes first (Article IV), then structure, then style |
| 4 | Orchestrator | AI_NOTES triage (the template's rule): graduate / expire / hold — max two holds, then it moves or dies |
| 5 | Orchestrator | Rotations per [K7](../knowledge/KNOWLEDGE_SYSTEM.md): oversized ledgers, closed snapshot items, old handovers — stubs left in place |
| 6 | Orchestrator | Systemic read: recurring drift in one document = a standard problem (Proposal to the framework), recurring drift by one workflow = its G5 discipline failing (lesson, E26); G5 close |

## Failure and Abort Paths

- **Contradiction with undeterminable truth** (M4.2's hard case): recorded openly in both documents + Q-NNN — a documented contradiction is honest; a guessed resolution is corruption.
- **Audit finds interrupted-session residue** (unexplained stamps): stop — that's WF_RECOVERY territory; this workflow resumes after reconciliation.
- **Scope exceeds session**: worst-first (truth defects before style), boundary in the handover.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure |

## Future Extension Notes

If `amf lint` lands (tooling direction), steps 1–2 become tool-assisted; steps 3–6 remain judgment.
