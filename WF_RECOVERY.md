# Workflow — Recovery

| Field | Value |
|---|---|
| ID | WFLW-12 |
| Document | WF_RECOVERY.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Procedure implementing the recovery contract of [SESSION_MANAGEMENT.md §5](../core/SESSION_MANAGEMENT.md): reconcile an interrupted or corrupted predecessor before any other work. Subordinate to [WORKFLOW_INDEX.md](WORKFLOW_INDEX.md). |

---

## Document Contract

**Purpose.** Make interruption survivable: detect what the interrupted session did, reconcile every touched artifact, close its record honestly, and only then let normal work proceed.
**Scope.** Interrupted sessions (no handover) and corrupted instance state. This workflow *is* the SESSION_MANAGEMENT §5 contract, operationalized — the contract governs; this file sequences.
**Responsibilities.** Steps, roles, aborts; the corruption variant.
**Dependencies.** [SESSION_MANAGEMENT.md §5](../core/SESSION_MANAGEMENT.md) (the contract), [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (WF_RECOVERY row), templates/SESSION_LOG.md (interruption signature), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) M4.2.
**Consumers.** Orchestrator (lead); domain owners for per-document reconciliation.
**Related documents.** templates/HANDOVER.md (reconstructed handovers).
**Update policy.** D2 (Architect); the underlying contract is class C (amendment only).

## Specification

| | |
|---|---|
| Trigger | Selection rule 1 — **pre-empts everything**: INITIALIZE finds a log entry without `Closed:` (S1.4), or unexplained state (stamps from unknown sessions, E31-grade corruption) |
| T1 reading | [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md), row WF_RECOVERY |
| Roles | Orchestrator (lead); domain owners per touched document; Human Owner if irreconcilable (§5.2 — possible data loss is D3 territory) |
| Gates | G5 for the reconciliation itself |
| Key E-codes | E31 (each reconciliation), E26 (lesson if the interruption had a preventable cause), E01/E02 |
| Output | A closed (reconstructed) predecessor record; a trustworthy instance; the original request free to proceed |

## Steps

The four contract steps ([SESSION_MANAGEMENT.md §5](../core/SESSION_MANAGEMENT.md)), sequenced:

| # | Contract step | Action |
|---|---|---|
| 1 | **Quarantine** | Everything the interrupted session may have touched is untrusted: enumerate from its partial log entry, document stamps (R10.2) carrying its S-ID, and artifact timestamps. Build the touched-list explicitly — reconciliation is per item, no item unexamined |
| 2 | **Assess** | Reconstruct what it was doing: partial log (workflow, plan, events up to the cut), the artifacts themselves, TASKS states. Determine the interruption point as precisely as the evidence allows — and no more precisely (Article IV: "unknown" is a valid finding) |
| 3 | **Reconcile** | Per touched artifact, exactly one disposition, by its domain owner: **complete** (the update was mid-flight and its intent is evident) · **roll back** (half-applied, intent unclear) · **keep-partial documented** (valid as far as it went; the edge marked). Snapshots re-derived from ledgers where they conflict (M4.1). Every disposition is an E31 entry |
| 4 | **Close** | Write the missing handover *on behalf of* the predecessor, header-marked `Reconstructed by: <this S-ID>` (templates/HANDOVER.md); close its log entry marked reconstructed; refresh CURRENT_STATUS to the reconciled truth; G5 on the reconciliation |

Then: the session's *original* request proceeds — as its own properly selected workflow (rule 1 satisfied, re-run the selection). If recovery consumed the session, the handover says exactly that.

**Corruption variant** (no interrupted session, but state contradicts itself): steps 1–3 with the touched-list built from the contradiction outward (M4.2: ledgers presumed true, finding session determines truth, undeterminable → open contradiction recorded + Q-NNN).

## Failure and Abort Paths

- **Irreconcilable state** (artifacts destroyed, history gaps, conflicting ledgers): stop at the boundary of what is knowable; package for the **Human Owner** ([AGENT_SYSTEM.md §5.2](../agents/AGENT_SYSTEM.md) — data loss decisions are D3): what is known, what is lost, options. Permanent loss, once decided, is recorded in LESSONS_LEARNED (Article VII consequences).
- **Recovery interrupted** (the irony case): the contract is re-entrant by design — the next session finds *two* unclosed entries and reconciles oldest-first; dispositions already E31-logged are not redone.
- **Preventable cause identified** (e.g. sessions routinely hitting context limits mid-EXECUTE): E26 lesson + the mid-session failure discipline of [SESSION_MANAGEMENT.md §5](../core/SESSION_MANAGEMENT.md) re-read — recovery that recurs is a process defect, not weather.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial procedure: four contract steps + corruption variant |

## Future Extension Notes

Parallel topology adds concurrent-session reconciliation (merge rules) — the per-artifact disposition model is designed to extend to it.
