# Standard — MEETING_NOTES.md

| Field | Value |
|---|---|
| ID | KNOW-20 |
| Document | templates/MEETING_NOTES.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `MEETING_NOTES.md` — the append-only ledger of Owner and stakeholder inputs. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the stakeholder-input ledger: everything the Human Owner (or a client stakeholder) tells the project, captured at the source — the raw material scope, priorities and D3 decisions trace back to.
**Scope.** Structure and rules of `MEETING_NOTES.md`; not the decisions themselves (DECISIONS), not the scope updates (PROJECT/BACKLOG — E22's conditionals put them there).
**Responsibilities.** Specification, entry format, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Articles I, VII.
**Consumers.** Product Analyst (owner), Orchestrator (D3 packaging), any session tracing "where did this requirement come from?".
**Related documents.** templates/PROJECT.md, templates/BACKLOG.md, templates/DECISIONS.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E22.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/MEETING_NOTES.md` |
| Class | **A — Ledger** |
| Knowledge domain | Business |
| Owner (role) | Product Analyst |
| Default read tier | T2 (traceback reads) |
| Profile | Full (Minimal/Standard: Owner inputs recorded directly as their E22 conditionals — PROJECT/BACKLOG edits with session refs — per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E22 (Owner/stakeholder input received) — same session as the contact |
| Required inputs | What was said, by whom, as directly as possible |
| Expected outputs | Traceable provenance for every requirement and every D3 |
| Archive policy | K7.2 by age |

## Entry Format

```markdown
## <YYYY-MM-DD> — <who> (<channel>)
- **Session:** <S-ID>
- **Inputs:** <what was said — direction, wishes, complaints, answers; near-verbatim for anything decision-bearing>
- **D3 given:** <verbatim, → D-NNN | none>
- **Propagated:** <PROJECT §X / BACKLOG items / Q-NNN answered / — >
- **Open from this contact:** <new Q-NNNs, promised follow-ups>
```

Rules: decision-bearing statements are captured **near-verbatim** (Article I: the Owner's words, not their paraphrase); the entry records *inputs*, the conditionals record *effects* — an entry whose Propagated line is empty while its Inputs mention scope is an unapplied E22 (E31); casual channels count (a WhatsApp "can it also do X?" is an input like any meeting).

## Structure

1. **Header** — per standard.
2. **Entries** — newest last.

## Skeleton

```markdown
# Meeting Notes — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-20 |
| Document | MEETING_NOTES.md |
| Class | A — Ledger |
| Profile-tier | Full |
| Owner | Product Analyst |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Entries
```

## Maintenance Notes

The provenance ledger: when a future session wonders whether a constraint is real or folklore, the answer is a date and a name here. For freelance client work this ledger doubles as the polite record of "you asked for this on the 12th" — write it knowing the client may one day read it.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: near-verbatim rule, propagation tracking |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Multi-stakeholder projects may group entries by stakeholder; additive restructure, same entry format.
