# Standard — BACKLOG.md

| Field | Value |
|---|---|
| ID | KNOW-09 |
| Document | templates/BACKLOG.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `BACKLOG.md` — future work, prioritized, uncommitted. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the backlog: the single holding place for work the project intends but has not committed, so ideas neither vanish nor leak into TASKS uncommitted.
**Scope.** Structure and rules of `BACKLOG.md`; not committed work (TASKS), not direction (ROADMAP).
**Responsibilities.** Specification, structure, priority model, promotion rule, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; templates/PROJECT.md (goals traceability).
**Consumers.** Product Analyst (owner), Orchestrator (planning), Human Owner (priorities).
**Related documents.** templates/TASKS.md (promotion target); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E03/E10/E22.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/BACKLOG.md` |
| Class | I — Snapshot |
| Knowledge domain | Business |
| Owner (role) | Product Analyst |
| Default read tier | T1 (WF_FEATURE: the item being built), T2 otherwise |
| Profile | Standard+ (Minimal: folds into PROJECT §Scope per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E22 (Owner input), E10 (scope change), E03 (promotion — mark promoted), E32 (work returned) |
| Required inputs | Owner wishes (MEETING_NOTES), discovered needs, deferred work |
| Expected outputs | An ordered answer to "what next?" whenever capacity frees |
| Archive policy | Promoted and rejected items rotate to `archive/BACKLOG_<YYYY>.md` (K7.3) with disposition noted |

## Priority Model

Three bands, deliberately coarse: **P1** — next up: promote when capacity frees; **P2** — intended: revisit each planning pass; **P3** — someday: parked, kept honest. Ordering within a band is positional (top = first). Finer-grained scoring is noise at AMF's scale (P7).

## Structure

1. **Header** — per standard.
2. **Items by band** — per item: title · serves (G-ref) · one-line description · acceptance sketch · refs (D-NNN, Q-NNN if any).
3. **Recently promoted / rejected** — dispositions since last rotation.

Rules: every item traces to a goal ("serves G2") or is explicitly marked `Owner wish` — items serving nothing are scope creep in waiting (Article XIII duty: challenge them); **promotion is the only path to TASKS** (E03 marks the item promoted with its T-NNN); backlog items carry no IDs — identity begins at promotion (the T-NNN); acceptance sketch = one line of "done looks like", matured into full acceptance criteria at promotion (gate G0, [QUALITY_GATES.md](../../quality/QUALITY_GATES.md)).

## Skeleton

```markdown
# Backlog — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-09 |
| Document | BACKLOG.md |
| Class | I — Snapshot |
| Profile-tier | Standard+ |
| Owner | Product Analyst |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## P1 — next up
- **<title>** — serves G<N>. <one line>. Done looks like: <sketch>. Refs: —

## P2 — intended
- ...

## P3 — someday
- ...

## Recently promoted / rejected
- <title> → T-NNN (S-ID) | rejected: <why> (S-ID)
```

## Maintenance Notes

Groom on Owner contact (E22) and at planning: bands drift stale fast. A P1 item untouched for many sessions is a question — either promote it or demote it, and say why.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: three-band model, promotion rule |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 5 forward reference (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

B-NNN item IDs are the noted candidate if cross-references to unpromoted items become common (R4 addition, D2); withheld pending evidence (P9).
