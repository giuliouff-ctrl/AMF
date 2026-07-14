# Standard — CHANGELOG.md

| Field | Value |
|---|---|
| ID | KNOW-12 |
| Document | templates/CHANGELOG.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `CHANGELOG.md` — the append-only ledger of user-visible change. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the changelog: what changed for users, when, accumulating under Unreleased and cut into versions at release.
**Scope.** Structure and rules of `CHANGELOG.md`; not release execution (RELEASE_HISTORY owns shipping evidence), not internal change (SESSION_LOG).
**Responsibilities.** Specification, entry format, cut rule, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Article VII.
**Consumers.** Release Manager (owner), Human Owner and end clients (readable release notes), WF_RELEASE.
**Related documents.** templates/RELEASE_HISTORY.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E05/E12/E14/E23/E25.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/CHANGELOG.md` |
| Class | **A — Ledger** |
| Knowledge domain | Shipping |
| Owner (role) | Release Manager |
| Default read tier | T1 §Unreleased (WF_RELEASE, WF_MAINTENANCE), T2 otherwise |
| Profile | Standard+ (Minimal: folds into CURRENT_STATUS §Recent per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E05 (user-visible completion), E12/E14/E25 conditional, E23 (release: cut Unreleased → version) |
| Required inputs | User-visible outcomes, in user language |
| Expected outputs | Release notes a non-technical client can read |
| Archive policy | K7.2 — released sections older than ~a year rotate; Unreleased and recent versions stay |

## Entry Format

Under `## Unreleased`, categorized lines: `### Added / Changed / Fixed / Removed` — each line: what, in user terms, + refs `(T-NNN, I-NNN)`. At release (E23), the Unreleased block becomes `## <version> — <YYYY-MM-DD>` verbatim, and a fresh empty Unreleased opens. That cut is the only restructuring ever allowed (Article VII: entries themselves never edited after cut).

Rules: user language, not implementation language ("Order search now matches partial codes", not "refactored query builder"); internal-only work does not appear here at all — it lives in SESSION_LOG (this ledger's silence *is* the signal that a session was internal-only); every line traces (refs) but reads standalone.

## Structure

1. **Header** — per standard.
2. **Unreleased** — accumulating categorized lines.
3. **Versions** — newest first, cut blocks.

## Skeleton

```markdown
# Changelog — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-12 |
| Document | CHANGELOG.md |
| Class | A — Ledger |
| Profile-tier | Standard+ |
| Owner | Release Manager |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Unreleased
### Added
### Changed
### Fixed
### Removed

## Versions
```

## Example

```markdown
## 1.2.0 — 2026-08-03
### Added
- Barcode scanning from the picking screen (T-031)
### Fixed
- Stock counts no longer drift after concurrent edits (I-014)
```

## Maintenance Notes

Written at E05 time, not reconstructed at release — the Release Manager's cut should be an edit of nothing and a promotion of everything. Empty category headings are removed at cut (no empty sections, P9); the skeleton shows all four only as the accumulation surface.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: categories, cut rule, user-language rule |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Versioning scheme of the *project* (semver or date-based) is the project's D2, recorded in DECISIONS and noted in ARCHITECTURE §Conventions — this standard is scheme-agnostic by design.
