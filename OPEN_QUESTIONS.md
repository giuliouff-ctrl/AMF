# Standard — OPEN_QUESTIONS.md

| Field | Value |
|---|---|
| ID | KNOW-18 |
| Document | templates/OPEN_QUESTIONS.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `OPEN_QUESTIONS.md` — unresolved questions that block or shape work. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the questions register: what the project doesn't know and needs to — routed to whoever can answer, tracked until answered.
**Scope.** Structure and rules of `OPEN_QUESTIONS.md`; not provisional answers (ASSUMPTIONS), not investigation itself (RESEARCH/WF_RESEARCH).
**Responsibilities.** Specification, entry format, routing model, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4/§5, [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (Q-NNN); [SESSION_MANAGEMENT.md](../../core/SESSION_MANAGEMENT.md) §10.5-adjacent rule (unresolved escalations land here pre-handover).
**Consumers.** Orchestrator (owner), all roles (E19 duty), Human Owner (questions routed to them), WF_RESEARCH (T1 primary).
**Related documents.** templates/ASSUMPTIONS.md, templates/RESEARCH.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E19/E20.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/OPEN_QUESTIONS.md` |
| Class | I — Snapshot |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | T1 (WF_RESEARCH: the question), T2 otherwise; Owner-routed items surface via CURRENT_STATUS §Blocked |
| Profile | Full (Minimal/Standard: folds into CURRENT_STATUS §Blocked/waiting per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E19 (raised — incl. unresolved escalations before handover), E20 (answered) |
| Required inputs | The question, precisely; what it blocks; who can answer |
| Expected outputs | Nothing blocked silently; every Owner contact primed with the questions waiting for them |
| Archive policy | ANSWERED items rotate to `archive/OPEN_QUESTIONS_<YYYY>.md` (K7.3) |

## Entry Format

Table row: `Q-NNN · question (answerable as phrased — "which payment provider does the client's bank support?", not "payments?") · raised (S-ID) · blocks (T-NNN/decision/nothing-but-shapes-X) · routed to (Owner / Architect / research / external) · status (OPEN / ANSWERED) · answer ref`.

Rules: **routing is mandatory** — a question routed to no one is a worry, not a register entry; answers land where they belong (a D-record, an assumption validated, a PROJECT edit) and the row points there (E20's conditionals) — the register holds the *pointer*, never the answer body (Article III); questions blocking work also appear as the blocker on their task (E06) and in CURRENT_STATUS §Blocked.

## Structure

1. **Header** — per standard.
2. **Next ID** — counter (K5.1).
3. **Open** — table, blocking-first; Owner-routed grouped for easy reading at Owner contact.
4. **Answered (recent)** — since last rotation.

## Skeleton

```markdown
# Open Questions — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-18 |
| Document | OPEN_QUESTIONS.md |
| Class | I — Snapshot |
| Profile-tier | Full |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

Next ID: Q-001

## Open
| ID | Question | Raised | Blocks | Routed to | Status |
|---|---|---|---|---|---|

## Answered (recent)
| ID | Question | Answer ref | Closed |
|---|---|---|---|
```

## Maintenance Notes

The Owner-routed group is this register's highest-value view: at every E22 contact, the Product Analyst walks it. A question aging OPEN across many sessions with `routed to: Owner` and no ask is an Article XIII failure — escalation means *asking*, not filing.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: routing model, answer-pointer rule |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

None anticipated; this register is deliberately minimal — its pressure valve is answering questions, not restructuring the file.
