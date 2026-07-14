# Session Management

| Field | Value |
|---|---|
| ID | CORE-07 |
| Document | SESSION_MANAGEMENT.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.0.4 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Normative for the session lifecycle: how every AI working session begins, proceeds, ends, and hands over. Operationalizes [AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article VIII. |

---

## Document Contract

**Purpose.** Define the session — AMF's atomic unit of work — as a contract: its lifecycle stages, their entry and exit criteria, required outputs, and the rules for interruption and recovery. This is what makes finite, stateless AI sessions compose into continuous projects.

**Scope.** Every AI working session, in framework work and project work, in any topology. Workflow-specific step detail is out of scope ([workflows module](../workflows/WORKFLOW_INDEX.md)); which documents to read per workflow is out of scope ([CONTEXT_RECONSTRUCTION.md](../knowledge/CONTEXT_RECONSTRUCTION.md)). This document owns the stage contract both plug into.

**Responsibilities.** Session definition and identity; the seven-stage lifecycle; the session checklist; required outputs and updates; interruption semantics; the recovery contract; multi-session work.

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md) (Articles I, IV, V, VI, VIII, IX); [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) (session ID grammar R4.1, update procedure §10).

**Consumers.** Every role in every session — this document is itself Tier-0 adjacent: its rules must be internalized before any work.

**Related documents.** [CONTEXT_RECONSTRUCTION.md](../knowledge/CONTEXT_RECONSTRUCTION.md) (reading tiers and lists), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) (what DOCUMENT updates), [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md), [WF_RECOVERY.md](../workflows/WF_RECOVERY.md).

**Update policy.** Amendment process per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5 (class C). Stage identities (the seven names and their order) fall under the compatibility discussion of [VERSIONING.md](VERSIONING.md) — treat as stable for 1.x.

---

## 1. The Session

**Definition.** A session is one continuous engagement of an AI agent with a project (or with the framework), from initialization to handover. It is AMF's atomic unit of accountability: context enters at its start, knowledge leaves at its end.

**Rules of session identity:**

- **S1.1** Every session has an ID per [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) R4.1 (`S-YYYYMMDD-NN`), assigned at INITIALIZE, stamped on everything the session produces.
- **S1.2** One session executes one workflow. Executing a second workflow in the same session requires explicit justification in the session log (typical legitimate case: a bug discovered mid-feature, small enough that splitting sessions costs more than it protects).
- **S1.3** All work happens inside sessions (Article VIII). There is no "quick change outside process"; the Minimal profile makes small sessions cheap instead.
- **S1.4** A session that produced no handover is **interrupted**, whatever the reason (§5).

## 2. Lifecycle — Seven Stages

Stages run in order. A stage may be *trivially satisfied* (e.g. PLAN for a one-line fix is one sentence) but never silently skipped: skipping requires a logged justification. HANDOVER is never skippable, and never trivial.

### Stage 1 — INITIALIZE

| | |
|---|---|
| Inputs | The incoming request (from the Owner or a scheduled trigger); the project's bootstrap pointer (CLAUDE.md → INSTANCE.md) |
| Activities | Assign session ID. Read the bootstrap. **Check for interruption:** if the latest session-log entry has no matching handover, this session must enter recovery (§5) before anything else. Identify the request; select the workflow via [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md). Confirm profile and pinned framework version from INSTANCE.md. |
| Outputs | Session ID; selected workflow; opened session-log entry (ID, date, workflow, request summary) |
| Exit criteria | Workflow selected; no unresolved interruption; log entry open |

Bootstrap exception: when no instance exists yet, INITIALIZE routes to the new-project workflow, which begins by instantiating one ([ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md)).

### Stage 2 — RECONSTRUCT

| | |
|---|---|
| Inputs | Reading tiers and the workflow's T1 list from [CONTEXT_RECONSTRUCTION.md](../knowledge/CONTEXT_RECONSTRUCTION.md) |
| Activities | Read T0 (always: INSTANCE.md → CURRENT_STATUS.md → latest handover), then the workflow's T1 list. Pull T2 documents only as the work references them. Reading beyond the budget is permitted with a logged reason. |
| Outputs | Log note: what was read, plus any deviation and its reason |
| Exit criteria | The agent can state, from documents alone: project state, the work at hand, its constraints, and relevant prior decisions. If it cannot, the knowledge system has failed — record the gap (Article IV) before proceeding on assumptions. |

### Stage 3 — PLAN

| | |
|---|---|
| Inputs | Reconstructed context; the request |
| Activities | State intended tasks (IDs per R4.1), roles to be assumed, gates in scope, documents expected to change. **Classify upcoming decisions**; anything D3 is flagged to the Owner now, before work (Article I) — never discovered at the end. |
| Outputs | Session plan in the session log (bulleted; proportional to the work) |
| Exit criteria | Plan recorded; D3 items either approved, rescoped out, or the session re-planned around them |

### Stage 4 — EXECUTE

| | |
|---|---|
| Inputs | The plan |
| Activities | Perform the work under role contracts ([AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md) and `agents/roles/`) and the communication protocol ([COMMUNICATION_PROTOCOL.md](../communication/COMMUNICATION_PROTOCOL.md)). Role assumptions logged. Decisions handled per class as they arise (Article VI). Deviations from plan are re-planned in the log, not improvised silently. |
| Outputs | The work itself; inline D1 log entries; Decision Records for D2/D3; messages per protocol |
| Exit criteria | Planned work done, or the remainder explicitly deferred with reasons |

### Stage 5 — REVIEW

| | |
|---|---|
| Inputs | Completed work; the workflow's gates; quality standards ([QUALITY_GATES.md](../quality/QUALITY_GATES.md), [REVIEW_STANDARDS.md](../quality/REVIEW_STANDARDS.md)) |
| Activities | Pass each in-scope gate. Separation of duties applies (Article IX): reviewer role explicitly assumed, standard re-read, Review Report produced. Gate results are binary (Article X). A second failure for the same cause escalates. |
| Outputs | Gate records with evidence; Review Report(s); findings routed (issues ledger, back-to-author) |
| Exit criteria | Every in-scope gate passed, or the session outcome downgraded and the failure recorded honestly (Article IV) |

### Stage 6 — DOCUMENT

| | |
|---|---|
| Inputs | Everything that happened; [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) |
| Activities | Apply the update matrix for every event of the session: status, tasks, decisions, issues, risks, changelog, and the rest. CURRENT_STATUS.md is always refreshed — it must describe the project as the session leaves it. Update procedure per [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §10 on every touched document. |
| Outputs | Updated instance knowledge |
| Exit criteria | No event of the session lacks its documentation (Article V); no touched document lacks its stamp |

### Stage 7 — HANDOVER

| | |
|---|---|
| Inputs | The session's full record |
| Activities | Close the session-log entry: outcomes, decisions made, gates passed/failed, open items. Write the handover file (`sessions/handovers/S-….md`, standard: [HANDOVER](../knowledge/templates/HANDOVER.md)): state of work, exact next recommended actions, warnings and open risks for the successor. Verify the instance is internally consistent (no half-applied updates). |
| Outputs | Closed log entry; handover file |
| Exit criteria | **A stranger test, honestly applied:** could a cold session with no access to this one resume the work from the handover plus the instance alone? If no, the handover is not done. |

## 3. Session Checklist

The compact form of §2 — every session, in order:

```text
[ ] 1. Session ID assigned; bootstrap read; interruption check clean
[ ] 2. Workflow selected; log entry opened
[ ] 3. T0 + workflow T1 read; deviations logged
[ ] 4. Plan recorded; D3 items flagged/approved BEFORE work
[ ] 5. Work executed under role contracts; decisions logged per class
[ ] 6. Gates passed with separation of duties; failures recorded honestly
[ ] 7. Update matrix applied; CURRENT_STATUS refreshed
[ ] 8. Session log closed; handover written; stranger test passed
```

## 4. Required Outputs and Updates

Every session, regardless of workflow or profile, produces at minimum: the **session-log entry** (opened at INITIALIZE, closed at HANDOVER), the **handover file**, and a **refreshed CURRENT_STATUS.md**. Everything else follows the update matrix. A session that produces "no changes" still produces these three — recording that nothing changed, and why.

## 5. Interruption and Recovery

**Interruption semantics.** A session is interrupted when it ends without a handover — context-window exhaustion, crash, abandonment, or the Owner stopping it. Interruption is detected, not declared: the next session finds a log entry without a handover (S1.4, INITIALIZE check).

**The recovery contract.** The successor session must, before any other work:

1. **Quarantine.** Treat all state the interrupted session may have touched as untrusted (Article VIII consequences).
2. **Assess.** Reconstruct what the interrupted session did from its partial log, the instance's stamps (R10.2), and the work artifacts themselves.
3. **Reconcile.** For each touched artifact: complete the update, roll it back, or record it as intentionally kept-partial with reasons. No artifact stays unexplained (Article V).
4. **Close.** Write the missing handover *on behalf of* the interrupted session, marked as reconstructed, then proceed with a normal session.

The full procedure, including corrupted-state handling, is [WF_RECOVERY.md](../workflows/WF_RECOVERY.md); this contract is what that workflow must implement.

**Mid-session failure discipline.** An agent that recognizes it is approaching a hard stop (context limits, unrecoverable confusion) stops executing and jumps to an abbreviated DOCUMENT + HANDOVER with whatever is true — a short honest handover beats a long interrupted mess.

## 6. Multi-Session Work

Work larger than one session is carried by the handover chain, not by memory:

- The task (T-NNN) persists in TASKS.md with its current state; each session's handover names the exact resumption point.
- Intermediate artifacts that must survive live in the instance (or the project tree), never in conversation.
- Long-running efforts re-derive their plan each session from the documents (Stage 3) — plans are session-scoped (Article II: session artifacts carry no standing authority).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial session contract: seven stages, checklist, interruption and recovery semantics |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 2 | Swept Phase 2 forward references to live links (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 3 | Swept Phase 3 forward reference (R8.3) |
| 1.0.3 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 4-5 forward references (R8.3) |
| 1.0.4 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- Phases 2 and 6 delivered the reading lists, update matrix, workflow selection and recovery procedure; all references swept (R8.3).
- Candidate v1.1 addition, on evidence: a session *budget* declaration at PLAN (expected scope ceiling) to make mid-session failure discipline (§5) proactive rather than reactive.
- Parallel multi-agent sessions (true concurrent topology) will need a session-coordination section: ID sub-spaces and log merge rules. Additive; the seven stages are designed to hold per agent.
