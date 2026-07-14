# Standard — RELEASE_HISTORY.md

| Field | Value |
|---|---|
| ID | KNOW-22 |
| Document | templates/RELEASE_HISTORY.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `RELEASE_HISTORY.md` — the append-only ledger of what actually shipped. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the release ledger: every release, its evidence and its approval — the shipping counterpart of DECISIONS.
**Scope.** Structure and rules of `RELEASE_HISTORY.md`; not the user-facing notes (CHANGELOG), not release procedure ([WF_RELEASE.md](../../workflows/WF_RELEASE.md)).
**Responsibilities.** Specification, entry format, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Articles I, VII (G6 is D3).
**Consumers.** Release Manager (owner), WF_RELEASE (T1: last entry), Human Owner (audit), WF_RECOVERY (deploy-state evidence).
**Related documents.** templates/CHANGELOG.md, templates/ROADMAP.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E23.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/RELEASE_HISTORY.md` |
| Class | **A — Ledger** |
| Knowledge domain | Shipping |
| Owner (role) | Release Manager |
| Default read tier | T1 last entry (WF_RELEASE), T2 otherwise |
| Profile | Standard+ (Minimal: folds into CURRENT_STATUS §Health deploy line + CHANGELOG fold, per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E23 (release shipped) — the entry is written as the release happens, not after |
| Required inputs | Version, scope, verification evidence, G6 approval (D-NNN), deploy target |
| Expected outputs | An audit trail: what ran where, when, approved by whom, revertible how |
| Archive policy | K7.2 by age; the latest entries never rotate |

## Entry Format

```markdown
## <version> — <YYYY-MM-DD>
- **Session:** <S-ID> · **Approved:** D-NNN (G6, Human Owner)
- **Scope:** <one line — headline of what this release is>
- **Changelog:** CHANGELOG.md §<version>
- **Verification:** <gates G4/G5 evidence refs — what was checked, result>
- **Deployed to:** <target/URL> · **Method:** <how>
- **Shipped with known issues:** <I-NNN list, or "none open at CRITICAL/MAJOR">
- **Rollback:** <how to revert this specific release>
```

Rules: no entry without its G6 D-NNN (releasing is D3 — Article I; the entry *is* the audit trail); "shipped with known issues" is mandatory and honest (Article IV) — the Owner approved a release, which means approving its known state; rollback is per-release and concrete ("revert Vercel deployment <id>", not "roll back").

## Structure

1. **Header** — per standard.
2. **Entries** — newest first (unlike other ledgers: the last release is the operative one).

## Skeleton

```markdown
# Release History — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-22 |
| Document | RELEASE_HISTORY.md |
| Class | A — Ledger |
| Profile-tier | Standard+ |
| Owner | Release Manager |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Entries
```

## Maintenance Notes

The difference from CHANGELOG, kept sharp: CHANGELOG tells *users* what changed; this ledger tells *engineers and the Owner* what ran where with what evidence. If production misbehaves, the first read is the last entry here — write each entry for that moment.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: entry format with evidence and rollback |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Multi-environment projects (staging/prod) would add a per-target sub-line — additive to the entry format.
