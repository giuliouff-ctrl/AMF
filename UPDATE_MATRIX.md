# Update Matrix

| Field | Value |
|---|---|
| ID | KNOW-03 |
| Document | UPDATE_MATRIX.md |
| Module | knowledge |
| Class | S — Stable spec |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Normative lookup: which events oblige which document updates, recorded by whom. Operationalizes [AI_CONSTITUTION.md](../core/AI_CONSTITUTION.md) Article V for instances. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Eliminate "should I update something?" as a judgment call: every event that can occur in a session maps to its mandatory and conditional document updates and a recording owner.

**Scope.** Instance document updates triggered by project events. Not framework-document updates ([FRAMEWORK_RULES.md](../core/FRAMEWORK_RULES.md) §10) and not document content rules (templates/).

**Responsibilities.** The event catalog with codes; the matrix; timing, conflict and completeness rules.

**Dependencies.** [KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md) (registry, ownership), [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) (Stage 6 applies this matrix), [AI_CONSTITUTION.md](../core/AI_CONSTITUTION.md) (Articles IV, V, VII).

**Consumers.** Every session at Stage 6 (DOCUMENT); every role when an event occurs mid-EXECUTE.

**Related documents.** templates/* (entry formats for each target), [CONTEXT_RECONSTRUCTION.md](CONTEXT_RECONSTRUCTION.md).

**Update policy.** D2 (Architect); new event rows are the expected additive change (MINOR).

---

## 1. How to Use the Matrix

At Stage 6 (and continuously during EXECUTE for ledger-bound events), walk the session's events against the matrix. **Mandatory** targets always update; **Conditional** targets update when their condition holds. The **Recorded by** role owns the entry (domain owners per [KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md) §3; in collapsed profiles, the inheriting role).

Event codes (`E-NN`) are stable and citable in session logs ("applied E08, E13").

## 2. The Matrix

| Code | Event | Mandatory updates | Conditional updates | Recorded by |
|---|---|---|---|---|
| E01 | Session started | SESSION_LOG (open entry) | — | Orchestrator |
| E02 | Session ended | SESSION_LOG (close), HANDOVER (write), CURRENT_STATUS (refresh) | — | Orchestrator |
| E03 | Task created | TASKS | BACKLOG (if promoted from it: mark promoted) | Orchestrator |
| E04 | Task started / status changed | TASKS | — | Orchestrator |
| E05 | Task completed | TASKS | CHANGELOG §Unreleased (if user-visible) | Orchestrator (+ Release Manager for CHANGELOG) |
| E06 | Task blocked | TASKS (status + reason) | OPEN_QUESTIONS (if blocked on a question), RISK_REGISTER (if blocked by a risk) | Orchestrator |
| E07 | D1 decision made | SESSION_LOG (inline note) | — | acting role |
| E08 | D2 decision made | DECISIONS (record) | ARCHITECTURE (if structural), TECHNICAL_DEBT (if debt taken/retired), DEPENDENCIES (if dependency choice) | Architect |
| E09 | D3 decision made | DECISIONS (record, Owner verbatim) | PROJECT (if scope/goals), ROADMAP (if milestones), INSTANCE (if configuration) | Orchestrator |
| E10 | Scope changed (approved D3) | PROJECT | BACKLOG, ROADMAP, TASKS (re-scoped items) | Product Analyst |
| E11 | Architecture changed | ARCHITECTURE (+ D-NNN ref, per E08) | KNOWN_ISSUES (if it resolves/creates issues) | Architect |
| E12 | Dependency added / updated / removed | DEPENDENCIES | RISK_REGISTER (if risk-bearing), CHANGELOG (if user-visible) | Engineer |
| E13 | Defect found | KNOWN_ISSUES (I-NNN) | RISK_REGISTER (if systemic) | QA Engineer |
| E14 | Defect resolved | KNOWN_ISSUES (status) | CHANGELOG §Unreleased | QA Engineer (+ Release Manager) |
| E15 | Risk identified | RISK_REGISTER (R-NNN) | — | Orchestrator |
| E16 | Risk changed / closed / occurred | RISK_REGISTER | LESSONS_LEARNED (if occurred: L-NNN) | Orchestrator |
| E17 | Assumption made | ASSUMPTIONS | — | Product Analyst |
| E18 | Assumption validated / invalidated | ASSUMPTIONS | If invalidated: every document that leaned on it (trace refs) + LESSONS_LEARNED | Product Analyst |
| E19 | Question raised | OPEN_QUESTIONS (Q-NNN) | — | Orchestrator |
| E20 | Question answered | OPEN_QUESTIONS (status + answer ref) | DECISIONS (if the answer decides), ASSUMPTIONS (if it validates) | Orchestrator |
| E21 | Research concluded | RESEARCH (entry) | OPEN_QUESTIONS (if it answers), DECISIONS (if it triggers a Proposal → record) | Architect |
| E22 | Owner input received | MEETING_NOTES (entry) | PROJECT / BACKLOG / ROADMAP (per content), DECISIONS (if D3 given) | Product Analyst |
| E23 | Release shipped | RELEASE_HISTORY (entry), CHANGELOG (cut Unreleased → version), CURRENT_STATUS | ROADMAP (milestone reached), KNOWN_ISSUES (shipped-with-known list) | Release Manager |
| E24 | Debt taken | TECHNICAL_DEBT (+ D-NNN ref) | — | Architect |
| E25 | Debt retired | TECHNICAL_DEBT (status) | CHANGELOG (if user-visible) | Architect |
| E26 | Lesson learned | LESSONS_LEARNED (L-NNN) | — | Orchestrator |
| E27 | Instance configuration changed (profile, opt-ins) | INSTANCE (+ D-NNN ref — D3) | active documents created/folded per profile | Orchestrator |
| E28 | Framework upgraded | INSTANCE (pin), SESSION_LOG | any document migrated per [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md) | Orchestrator |
| E29 | Milestone reached / moved | ROADMAP | CURRENT_STATUS | Product Analyst |
| E30 | Observation with no home | AI_NOTES (entry + suggested home) | — | any role |
| E31 | Knowledge defect found (stale, contradictory, missing) | The defective document (fix) or KNOWN_ISSUES (if deferred) | LESSONS_LEARNED (if systemic) | finder (Article IV duty) |
| E32 | Work deferred / dropped from plan | SESSION_LOG (with reason) | TASKS (status), BACKLOG (if returned to backlog) | Orchestrator |

## 3. Timing Rules

- **M3.1** Ledger-bound events (E07–E09, E13, E15, E19, E21, E22, E26, E30) record **when they occur**, during EXECUTE — a decision or defect is written down at the moment it exists, not reconstructed at Stage 6.
- **M3.2** Snapshot-bound updates may batch to Stage 6, except TASKS status changes, which track in near-real-time (they are the session's working state).
- **M3.3** Stage 6 is the completeness check: every event of the session either has its updates applied or its deferral logged. Same session, always (Article V).

## 4. Conflict and Consistency Rules

- **M4.1** **Ledger wins.** When a snapshot contradicts a ledger, the ledger is presumed true; the snapshot is corrected (E31). Rationale: ledgers are append-only records of what happened; snapshots are derived views.
- **M4.2** **Cross-session inconsistency** (two sessions left contradictory statements): the finding session determines truth from ledgers and artifacts, fixes the wrong document, and logs the reconciliation. If truth cannot be determined, the contradiction is recorded openly in the affected documents (Article IV) and a Q-NNN raised.
- **M4.3** **Single-writer discipline.** Within a session, updates to one document happen under its owning role's assumption. Parallel topologies (future) must serialize writes per document.

## 5. Completeness Rule

- **M5.1** An event with no matrix row: record it in the nearest owning document by domain (§3 of [KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md)), then raise a Proposal to add the row (D2). The matrix must converge to total coverage — gaps are framework defects, not session judgment calls.
- **M5.2** In Minimal profile, targets resolve to folded sections (folding map: [PROFILES.md §2](../operations/PROFILES.md)); the obligation is identical.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial catalog: 32 events, timing, conflict and completeness rules |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- New event rows are the expected evolution (M5.1 feeds them); candidates already visible: "external service outage observed", "performance regression detected" — awaiting real-project evidence (P9).
- If tooling lands, Stage 6 completeness (M3.3) becomes checkable: session-log events × matrix rows × document stamps.
