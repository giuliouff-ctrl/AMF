# Communication Protocol

| Field | Value |
|---|---|
| ID | COMM-01 |
| Document | COMMUNICATION_PROTOCOL.md |
| Module | communication |
| Class | S — Stable spec |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Normative for every structured exchange between roles and with the Human Owner: the envelope, routing, response obligations, and how messages are recorded per topology. The envelope field set is part of the v1.x compatibility promise ([VERSIONING.md §6](../core/VERSIONING.md)). Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Make intent, status and decisions travel as structured messages instead of ambient prose — so that obligations are explicit, routable and auditable in any topology.

**Scope.** The message system: envelope, lifecycle, routing, recording, obligations. Not the ten type definitions ([MESSAGE_TYPES.md](MESSAGE_TYPES.md)) and not who holds which authority ([AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md)).

**Responsibilities.** Envelope; message identity; status lifecycle; routing and response obligations; single-instance recording; cross-session conversion; Owner communications.

**Dependencies.** [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md) (roles as endpoints, §5 escalation, §7 Owner interface), [FRAMEWORK_RULES.md](../core/FRAMEWORK_RULES.md) §4 (M-NN grammar), [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) (messages live inside sessions), [AI_CONSTITUTION.md](../core/AI_CONSTITUTION.md) (Articles II, IV, V).

**Consumers.** Every role, every exchange; the workflows (each step names the messages it emits).

**Related documents.** [MESSAGE_TYPES.md](MESSAGE_TYPES.md), templates/SESSION_LOG.md (the recording surface), templates/DECISIONS.md (Decision Record persistence).

**Update policy.** D2 (Architect); envelope changes are D3 (compatibility promise).

---

## 1. Why Messages

Unstructured prose loses three things AMF cannot afford to lose: **who owes whom what** (obligations), **what happened to a request** (lifecycle), and **where the outcome lives** (persistence). The protocol's core rule follows:

- **P1.1** **Obligations exist only in messages or documents.** A request made in passing prose creates no duty; if it matters, it is a message (or it is written into an owned document). Conversely, every message of a requesting type creates an explicit obligation (§4).

## 2. The Envelope

Every message carries exactly these fields — the type's body extends, never replaces, them:

| Field | Content |
|---|---|
| `type` | One of the ten types in [MESSAGE_TYPES.md](MESSAGE_TYPES.md) |
| `id` | `M-NN`, sequential within the session ([FRAMEWORK_RULES.md §4](../core/FRAMEWORK_RULES.md)); cited as `<S-ID>/M-NN` across sessions |
| `session` | The S-ID it was emitted in |
| `from` / `to` | Role names, or `Human Owner` |
| `subject` | One line |
| `refs` | Entity IDs and documents concerned (R4.4 discipline) |
| `status` | `PENDING` → `RESOLVED` \| `ESCALATED` (§3) |
| `body` | The type's required fields |

## 3. Status Lifecycle

- **P3.1** A message is born `PENDING` if its type requires a response (§4), else born `RESOLVED` (pure notifications: Status Report, Decision Record, Approval).
- **P3.2** `PENDING` resolves when the required response exists (the resolution is noted on the message record), or becomes `ESCALATED` when routed up per the [escalation matrix](../agents/AGENT_SYSTEM.md).
- **P3.3** **No message crosses a session boundary PENDING.** Before HANDOVER, every PENDING message converts to a durable entity: a task (E03), an open question (E19), a pending Decision Record, or an escalation package — per its type's conversion rule ([MESSAGE_TYPES.md](MESSAGE_TYPES.md)). Messages are session artifacts (Article II); obligations that outlive the session must live in documents.

## 4. Routing and Response Obligations

- **P4.1** Routing follows authority, fixed per type ([MESSAGE_TYPES.md](MESSAGE_TYPES.md) binds each type to its route from [AGENT_SYSTEM.md §3.3/§5.2](../agents/AGENT_SYSTEM.md)). A message to the wrong endpoint is re-routed by the receiver, not answered out of lane.
- **P4.2** Each requesting type names its required response and responder. The response deadline is uniform: **same session** — or explicit conversion per P3.3 with the reason logged.
- **P4.3** Ignoring a message is not a state. A receiver that cannot respond substantively responds with what blocks it (honesty per Article IV beats silence).
- **P4.4** Messages *to* the Human Owner go through the interface rules ([AGENT_SYSTEM.md §7](../agents/AGENT_SYSTEM.md)): Orchestrator packaging for D3/escalations, batched questions, recommendation-first.

## 5. Recording (single-instance topology)

In the default topology, messages are not literal exchanges — they are **structured entries in the session log's Events line** (templates/SESSION_LOG.md), in the compact form:

```text
M-NN TYPE from→to "subject" [refs] :: resolution-or-PENDING-conversion
```

- **P5.1** The compact form is the message of record for types whose persistence target is the session log. Types with a document persistence target (Decision Record → DECISIONS.md, Bug Report → KNOWN_ISSUES.md, …) write their **full form into the target** — the log line then carries just the pointer. One home per fact (Article III): full body in exactly one place.
- **P5.2** The full form is the envelope plus required body fields, as a block — used whenever the compact line cannot carry the required fields (Decision Requests, Escalations, Review Reports always use full form in their target).
- **P5.3** In multi-instance topology, literal exchanges still persist identically: the target document is the record, the exchange is transport. Recording rules are topology-invariant by design (AD-4).

## 6. Owner Communications

- **P6.1** Inbound Owner input is not a typed message — it is *the* authority speaking (Article I). It is captured per E22 (MEETING_NOTES, near-verbatim for decision-bearing content) and then *generates* typed messages internally (a D3 instruction generates its Decision Record; a wish generates backlog work via the Product Analyst).
- **P6.2** Outbound communications to the Owner use the typed system (Decision Request for D3, Escalation, Approval requests) — packaged per P4.4, in plain language (P6: the Owner reads everything).

## 7. Protocol Hygiene

- **P7.1** Refs discipline: every message about an entity carries its ID; every message that triggered a document write carries the pointer both ways (log line ↔ document entry, per R8 cross-reference rules).
- **P7.2** Messages are never edited after resolution — corrections are new messages (the log is a ledger, Article VII).
- **P7.3** Volume discipline: messages are for obligations and outcomes, not narration. Routine progress inside one role's task needs no Status Report until a stage boundary, a blocker, or completion (K8.1 density applies to logs too).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 4 | Initial protocol: envelope, lifecycle, routing obligations, topology-invariant recording |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- New message types extend via [MESSAGE_TYPES.md](MESSAGE_TYPES.md) (envelope reuse, D2); the envelope itself is frozen for 1.x.
- Multi-instance transport specifics (queues, concurrent sub-sessions) attach here as an additive section when a parallel runtime is real (P10 — not before).
