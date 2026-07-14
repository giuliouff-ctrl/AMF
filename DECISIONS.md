# Standard — DECISIONS.md

| Field | Value |
|---|---|
| ID | KNOW-10 |
| Document | templates/DECISIONS.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `DECISIONS.md` — the append-only ledger of D2/D3 Decision Records. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the decisions ledger: the structural fix for re-litigated decisions — every D2/D3 choice, its alternatives and its rationale, permanently.
**Scope.** Structure and rules of `DECISIONS.md`; not decision *authority* ([AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Article VI), not the message flow ([COMMUNICATION_PROTOCOL.md](../../communication/COMMUNICATION_PROTOCOL.md)).
**Responsibilities.** Specification, entry format, index rules, skeleton, example.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4/§5, [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Articles VI/VII, [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (D-NNN).
**Consumers.** All roles (reading before proposing anything already decided); Architect (owner).
**Related documents.** templates/ARCHITECTURE.md (points here for rationale); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E08/E09.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/DECISIONS.md` |
| Class | **A — Ledger** (append-only, Article VII) |
| Knowledge domain | Technical design |
| Owner (role) | Architect (D3 entries recorded by Orchestrator, Owner's words verbatim) |
| Default read tier | T1 (index + relevant entries, most workflows) |
| Profile | Minimal+ |
| Update triggers | E08 (D2), E09 (D3) — at the moment of decision (M3.1) |
| Required inputs | Context, options actually considered, the choice, rationale, consequences, dissent if any |
| Expected outputs | A record sufficient to *not reopen* the decision without new facts |
| Archive policy | K7.2 rotation by entry age; index stub always remains in place |

## Entry Format

```markdown
## D-NNN — <decision title>
- **Date/Session:** <YYYY-MM-DD> · <S-ID> · **Class:** D2|D3 · **Decider:** <Architect|Human Owner>
- **Context:** <the situation forcing a choice>
- **Options:** <A — one line> / <B — one line> / <C — one line>
- **Decision:** <the choice>
- **Rationale:** <why this one — the load-bearing paragraph>
- **Consequences:** <what this commits us to; what it forecloses>
- **Dissent:** <recorded disagreement, or omit line>
- **Refs:** <G-goals, T-tasks, I-issues, supersedes D-MMM if any>
```

Rules: **append-only** — corrections and reversals are *new* entries with `supersedes D-MMM` in Refs; the superseded entry is never edited (Article VII). Options must be the ones actually considered — a record with one option is a announcement, not a decision (Article XIII). D3 entries record the Owner's decision verbatim (Article I).

## Structure

1. **Header** — per standard.
2. **Next ID** — counter (K5.1).
3. **Index** — table: ID · title · class · date · status (ACTIVE / SUPERSEDED-by-D-MMM). *The index is navigation metadata: it is regenerated as entries append — the append-only rule binds entries, not the index.*
4. **Records** — entries, newest last.

## Skeleton

```markdown
# Decisions — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-10 |
| Document | DECISIONS.md |
| Class | A — Ledger |
| Profile-tier | Minimal+ |
| Owner | Architect |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

Next ID: D-001

## Index
| ID | Title | Class | Date | Status |
|---|---|---|---|---|

## Records
```

## Example Entry

```markdown
## D-003 — Firestore for persistence
- **Date/Session:** 2026-07-15 · S-20260715-01 · **Class:** D2 · **Decider:** Architect
- **Context:** WMS needs multi-user persistence; client budget requires free tier (PROJECT §Constraints).
- **Options:** A — Firestore (free tier, realtime) / B — Supabase (SQL, free tier tighter) / C — local-only JSON (no multi-user)
- **Decision:** Firestore.
- **Rationale:** Free tier covers projected volume ×10; realtime sync needed for G2 (multi-station scanning); team stack familiarity.
- **Consequences:** NoSQL modeling for inventory (see ARCHITECTURE §Data model); vendor lock-in accepted; offline mode deferred (BACKLOG).
- **Refs:** G2, T-007
```

## Maintenance Notes

The reading rule that makes this ledger pay: before proposing anything structural, check the index (C3.1 lists include it). "New facts" is the only key that reopens a decision — and reopening means a *new* superseding entry.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: entry format, index rules, example |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 4 references; field mapping confirmed (R8.3) |

## Future Extension Notes

Message-form Decision Record maps field-for-field onto this entry format — confirmed by [MESSAGE_TYPES.md §2.5](../../communication/MESSAGE_TYPES.md).
