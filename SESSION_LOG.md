# Standard — SESSION_LOG.md

| Field | Value |
|---|---|
| ID | KNOW-24 |
| Document | templates/SESSION_LOG.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `sessions/SESSION_LOG.md` — the append-only ledger of everything every session did. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the session ledger: the accountability spine of an instance — one entry per session, opened at INITIALIZE, closed at HANDOVER.
**Scope.** Structure and rules of `SESSION_LOG.md`; not the successor-facing handover (templates/HANDOVER.md) and not the lifecycle itself ([SESSION_MANAGEMENT.md](../../core/SESSION_MANAGEMENT.md)).
**Responsibilities.** Specification, entry format, skeleton, interruption signature.
**Dependencies.** [SESSION_MANAGEMENT.md](../../core/SESSION_MANAGEMENT.md) (Stages 1, 7; §5), [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (S-ID).
**Consumers.** Orchestrator (owner); WF_RECOVERY (primary evidence); audits.
**Related documents.** templates/HANDOVER.md, templates/CURRENT_STATUS.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E01/E02/E07/E32.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/sessions/SESSION_LOG.md` |
| Class | **A — Ledger** (append-only) |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | T1 recent entries (WF_RECOVERY: primary) |
| Profile | Minimal+ |
| Update triggers | E01 (open), E02 (close), E07 (D1 inline), E32 (deferrals) — continuously during the session |
| Required inputs | Everything the session does, as it does it |
| Expected outputs | A per-session account audit-sufficient without the conversation that produced it |
| Archive policy | K7.2 rotation by year/volume; the open entry and last ~10 closed entries never rotate |

## Entry Format

```markdown
## S-YYYYMMDD-NN
- **Opened:** <date> · **Workflow:** <WF_*> · **Request:** <one line>
- **Read:** T0 + <T1 row applied>; deviations: <none | what + why>
- **Plan:** <bulleted, proportional; D3 flags noted>
- **Events:** <running log: role assumptions, D1 notes (E07), E-codes applied, deviations from plan>
- **Decisions:** <D-NNN list, or "D1-only">
- **Gates:** <G-N: PASS/FAIL + evidence ref, per gate in scope>
- **Outcome:** <done / partial / aborted — honest, Article IV>
- **Open items:** <deferred work (E32), unresolved Q-NNN>
- **Closed:** <date> · **Handover:** handovers/S-YYYYMMDD-NN.md
```

Rules: the entry is opened with its first three fields at INITIALIZE and grows during the session — **an entry with no `Closed:` line is the interruption signature** ([SESSION_MANAGEMENT.md](../../core/SESSION_MANAGEMENT.md) §5, detected at the next INITIALIZE). Recovery closes such entries *marked as reconstructed*. Entries are never edited after close; corrections are E31 notes in the current session's entry.

## Structure

1. **Header** — per standard. (No ID counter — session IDs are date-derived, R4.1.)
2. **Entries** — newest last.

## Skeleton

```markdown
# Session Log — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-24 |
| Document | SESSION_LOG.md |
| Class | A — Ledger |
| Profile-tier | Minimal+ |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Entries
```

## Maintenance Notes

Write as you go (M3.1): a log reconstructed at session end is a memoir, not a record. Granularity guide: every role assumption, every E-code applied, every plan deviation — one line each; reasoning stays in the artifacts it produced.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: entry format, interruption signature |

## Future Extension Notes

Parallel topology will need per-agent sub-entries under one session heading (SESSION_MANAGEMENT future note) — additive to this format.
