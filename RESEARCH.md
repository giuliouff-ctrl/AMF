# Standard — RESEARCH.md

| Field | Value |
|---|---|
| ID | KNOW-19 |
| Document | templates/RESEARCH.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `RESEARCH.md` — the append-only ledger of investigations and findings. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the research ledger: investigations run once, findings kept forever — so no question is researched twice.
**Scope.** Structure and rules of `RESEARCH.md`; not the questions themselves (OPEN_QUESTIONS), not decisions taken on findings (DECISIONS).
**Responsibilities.** Specification, entry format, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Article VII.
**Consumers.** Architect (owner), WF_RESEARCH (T1: related entries — read before investigating), any role checking "did we already look at this?".
**Related documents.** templates/OPEN_QUESTIONS.md, templates/DECISIONS.md, templates/ASSUMPTIONS.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E21.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/RESEARCH.md` |
| Class | **A — Ledger** |
| Knowledge domain | Technical design |
| Owner (role) | Architect |
| Default read tier | T2 (T1 related-entries in WF_RESEARCH) |
| Profile | Full (Minimal/Standard: findings land directly in the D-record or document they serve, per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E21 (research concluded) — one entry per concluded investigation |
| Required inputs | The question investigated, method, findings with evidence, conclusion |
| Expected outputs | Reusable findings; ammunition for D-records |
| Archive policy | K7.2 by age; entries referenced by ACTIVE decisions noted in the stub index |

## Entry Format

```markdown
## <YYYY-MM-DD> — <topic>
- **Session:** <S-ID> · **For:** <Q-NNN / D-NNN candidate / T-NNN>
- **Question:** <what exactly was investigated>
- **Method:** <docs read, options tested, benchmarks run — enough to judge the finding's weight>
- **Findings:** <what was learned, with evidence refs/links>
- **Conclusion:** <the answer, and its confidence>
- **Follow-ups:** <new Q-NNNs raised, or none>
```

Rules: findings are *evidence*, conclusions are *judgment* — keep the fields honest so a future session can re-judge old evidence under new constraints; an investigation that dead-ends is still an entry (knowing X doesn't work is a finding — Article IV); the decision taken on a finding lives in DECISIONS with a ref back — never duplicated here (Article III).

## Structure

1. **Header** — per standard.
2. **Entries** — newest last. (No counter — entries are date+topic keyed.)

## Skeleton

```markdown
# Research — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-19 |
| Document | RESEARCH.md |
| Class | A — Ledger |
| Profile-tier | Full |
| Owner | Architect |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Entries
```

## Maintenance Notes

The read-before rule earns the ledger: WF_RESEARCH's T1 includes "related entries" precisely so the second session on a topic starts from the first one's findings. Method quality determines reuse value — "read the docs" is not a method; "tested X and Y against the free-tier quota with N records" is.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: entry format, evidence/judgment split |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Topic tagging if volume warrants search structure; withheld pending evidence (P9).
