# Message Types

| Field | Value |
|---|---|
| ID | COMM-02 |
| Document | MESSAGE_TYPES.md |
| Module | communication |
| Class | S — Stable spec |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Normative specification of the ten message types: fields, routes, lifecycles, persistence. Subordinate to [COMMUNICATION_PROTOCOL.md](COMMUNICATION_PROTOCOL.md). |

---

## Document Contract

**Purpose.** Specify each message type completely: what it is for, who sends it to whom, what its body must contain, how it resolves, and where it persists.

**Scope.** The ten v1.0 types. Envelope and system rules are [COMMUNICATION_PROTOCOL.md](COMMUNICATION_PROTOCOL.md)'s; routing authority is [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md)'s.

**Responsibilities.** Type specifications; the ledger-feeding map; conversion rules (P3.3) per type.

**Dependencies.** [COMMUNICATION_PROTOCOL.md](COMMUNICATION_PROTOCOL.md), [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md) (§3.3 routing, §4 gates, §5 escalation), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) (E-codes each type triggers), templates/* (persistence formats).

**Consumers.** Every role; the workflows (steps name emitted types).

**Related documents.** templates/DECISIONS.md (Decision Record format identity), templates/KNOWN_ISSUES.md, templates/RISK_REGISTER.md, templates/SESSION_LOG.md.

**Update policy.** D2 (Architect); new types are the expected additive change (MINOR).

---

## 1. Specification Format

Each type defines: **From → To** (route), **Purpose**, **Body** (required fields beyond the envelope), **Lifecycle** (born status → terminal), **Persists to** (the full form's home, P5.1), **Response** (required response + responder, P4.2), **Conversion** (what a PENDING becomes at session end, P3.3).

## 2. The Ten Types

### 2.1 Task Request

| | |
|---|---|
| From → To | Orchestrator → any role |
| Purpose | Assign committed work |
| Body | Task title; origin ref (B-item/G-goal/I-NNN/D-NNN); acceptance criteria ref (G0 output); constraints; expected gates |
| Lifecycle | PENDING → RESOLVED on acceptance or bounce |
| Persists to | TASKS.md (E03 — the task row is the record) |
| Response | Acceptance (Status Report `accepted`) or bounce with reason (wrong role, malformed, blocked) |
| Conversion | The task row itself is durable; unaccepted requests revert to backlog with the bounce reason logged |

### 2.2 Status Report

| | |
|---|---|
| From → To | any role → Orchestrator |
| Purpose | Report work state at stage boundaries, blockers, completion (P7.3 volume rule) |
| Body | Re (T-NNN); state (per TASKS model); evidence refs for claims; blockers with refs (E06) |
| Lifecycle | Born RESOLVED (notification) |
| Persists to | SESSION_LOG.md Events line; TASKS.md state (E04/E05/E06) |
| Response | None required; Orchestrator acts on content (routing, E-codes) |
| Conversion | n/a (never PENDING) |

### 2.3 Review Report

| | |
|---|---|
| From → To | Reviewer → Orchestrator + authoring role |
| Purpose | Deliver a gate verdict (G1/G3) against written standards |
| Body | Gate; work item ref; verdict `PASS` \| `PASS_WITH_NOTES` \| `FAIL`; findings[] — each: standard/DoD/design ref violated, severity (`BLOCKING`/`NOTE`), location (file:line where applicable) |
| Lifecycle | Born RESOLVED (the verdict is the resolution); FAIL obligates rework routing by the Orchestrator |
| Persists to | Full form in SESSION_LOG.md (gate record); defect findings → KNOWN_ISSUES.md via Bug Report/E13; undeclared-debt findings → flagged for E24 |
| Response | On FAIL: rework plan (Orchestrator routes); second FAIL same cause escalates ([AGENT_SYSTEM.md §5.1](../agents/AGENT_SYSTEM.md)) |
| Conversion | Unresolved BLOCKING findings at session end → I-NNN entries or task rows, never loose notes |

### 2.4 Decision Request

| | |
|---|---|
| From → To | any role → Architect (D2) · any role → Orchestrator → Human Owner (D3) |
| Purpose | Put a classified decision in front of its authority |
| Body | Class (with §3.1 checklist reasoning if non-obvious); context; options actually considered (≥2 or the honest "only one found, here's why"); recommendation; what is blocked meanwhile |
| Lifecycle | PENDING → RESOLVED by Decision Record; or ESCALATED (class was higher than requested) |
| Persists to | DECISIONS.md as a pending entry when it outlives its session |
| Response | Decision Record from the class authority — same session or explicit conversion |
| Conversion | Pending entry in DECISIONS.md + Q-NNN if it blocks (E19); blocked work marked BLOCKED (E06) |

### 2.5 Decision Record

| | |
|---|---|
| From → To | Architect (D2) / Human Owner via Orchestrator's pen (D3) → all roles |
| Purpose | Commit and preserve a decision |
| Body | **Identical, field-for-field, to the templates/DECISIONS.md entry format**: context, options, decision, rationale, consequences, dissent (if any), refs. The message *is* the ledger entry — no separate form exists |
| Lifecycle | Born RESOLVED |
| Persists to | DECISIONS.md (E08/E09); conditional propagations per the matrix |
| Response | None; execution is faithful (Article XIII), relitigation requires new facts |
| Conversion | n/a |

### 2.6 Escalation

| | |
|---|---|
| From → To | any role → Orchestrator → (if beyond it) Human Owner |
| Purpose | Move a §5.1-triggered situation to its authority |
| Body | Situation; trigger (which [§5.1](../agents/AGENT_SYSTEM.md) row); options considered; recommendation; what is blocked (P4.4 packaging for Owner-bound) |
| Lifecycle | PENDING → RESOLVED by decision/route; or remains open |
| Persists to | Full form in SESSION_LOG.md; unresolved → OPEN_QUESTIONS.md (E19) |
| Response | Resolution or routing by the Orchestrator; Owner decision where terminal |
| Conversion | Q-NNN (mandatory — §5.3 hygiene: never carried silently) |

### 2.7 Bug Report

| | |
|---|---|
| From → To | any role → QA Engineer |
| Purpose | Register a discovered defect or limitation |
| Body | Observed vs expected; reproduction (or best known); area; severity *suggestion* (QA assigns final); evidence ref |
| Lifecycle | PENDING → RESOLVED when registered (I-NNN assigned) |
| Persists to | KNOWN_ISSUES.md (E13 — the issue row is the record) |
| Response | I-NNN assignment + severity by QA, same session (E13 is a discovery-time duty) |
| Conversion | The I-NNN row is durable by definition |

### 2.8 Risk Report

| | |
|---|---|
| From → To | any role → Orchestrator |
| Purpose | Surface an uncertain event with project impact |
| Body | The event (not the fear — templates/RISK_REGISTER.md rule); suggested likelihood/impact; mitigation idea if any; refs |
| Lifecycle | PENDING → RESOLVED when registered (R-NNN) |
| Persists to | RISK_REGISTER.md (E15) |
| Response | R-NNN registration + scoring by the Orchestrator |
| Conversion | The R-NNN row is durable |

### 2.9 Proposal

| | |
|---|---|
| From → To | any role → Architect |
| Purpose | Propose a change: project-structural (feeds a D2), or framework-level (extension per [GOVERNANCE §7](../core/FRAMEWORK_GOVERNANCE.md), or amendment per §5 — where this type is the §5.1 written proposal) |
| Body | The change; problem it solves; for framework proposals: why no extension point suffices; expected impact |
| Lifecycle | PENDING → RESOLVED: accepted (→ Decision Request/Record chain, or governance process) or declined with reason |
| Persists to | RESEARCH.md when investigated (E21); DECISIONS.md when it becomes one; governance records for amendments |
| Response | Architect's disposition, same session or converted |
| Conversion | Q-NNN or backlog item, per content |

### 2.10 Approval

| | |
|---|---|
| From → To | gate authority ([AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md)) / Human Owner → requesting role |
| Purpose | Record a formal yes: gate passages and the Owner's G6/D3 grants |
| Body | What is approved (exact scope); conditions attached (if any); evidence refs the approval rests on |
| Lifecycle | Born RESOLVED |
| Persists to | SESSION_LOG.md gate record; G6 additionally as its D-NNN (E09) and in the RELEASE_HISTORY entry |
| Response | None; conditions attached become tasks or criteria (converted immediately) |
| Conversion | n/a |

## 3. Ledger-Feeding Map

Exit-criterion view: every instance ledger's feed, by message type or event (no orphan ledgers).

| Ledger | Fed by |
|---|---|
| DECISIONS.md | Decision Request (pending) · Decision Record |
| SESSION_LOG.md | Status Report · Review Report · Escalation · Approval · every E01/E02/E07 event |
| KNOWN_ISSUES.md* | Bug Report |
| RISK_REGISTER.md* | Risk Report |
| RESEARCH.md | Proposal (investigated) · E21 |
| CHANGELOG.md | Event-fed: E05/E12/E14/E25 conditionals (Release Manager's pen) |
| RELEASE_HISTORY.md | Approval (G6) + E23 |
| MEETING_NOTES.md | Owner input per P6.1/E22 (inbound authority, not a typed message) |
| LESSONS_LEARNED.md | Event-fed: E26 (often downstream of Escalation/Review findings) |
| AI_NOTES.md | Event-fed: E30 |
| Handovers | Event-fed: E02 |

*Snapshot registers with ledger-grade ID discipline; listed for feeding completeness.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 4 | Initial ten types + ledger-feeding map |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- Candidate types await evidence (P9): Handoff Note (multi-agent parallel work), Incident Report (production events — today: Bug Report + Risk Report + lesson).
- Each new type must fill every row of the §1 format — a type without a persistence target or conversion rule is malformed by definition.
