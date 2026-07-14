# Standard — KNOWN_ISSUES.md

| Field | Value |
|---|---|
| ID | KNOW-13 |
| Document | templates/KNOWN_ISSUES.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `KNOWN_ISSUES.md` — defects and limitations, tracked honestly. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the issues register: every known defect and limitation, so nothing broken is ever a surprise to a future session or the Owner.
**Scope.** Structure and rules of `KNOWN_ISSUES.md`; not fixing procedure ([WF_BUGFIX.md](../../workflows/WF_BUGFIX.md)), not systemic risk (RISK_REGISTER).
**Responsibilities.** Specification, severity/status models, entry format, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4/§5, [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (I-NNN).
**Consumers.** QA Engineer (owner), all roles (E13 duty), WF_BUGFIX (T1), WF_RELEASE (ship decision).
**Related documents.** templates/RISK_REGISTER.md (systemic escalation), templates/CHANGELOG.md (fixes surface there); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E13/E14.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/KNOWN_ISSUES.md` |
| Class | I — Snapshot |
| Knowledge domain | Verification & defects |
| Owner (role) | QA Engineer |
| Default read tier | T1 (WF_BUGFIX: the issue; WF_FEATURE: affected area; WF_RELEASE: all open) |
| Profile | Standard+ (Minimal: folds into CURRENT_STATUS §Doesn't work per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E13 (found — by anyone, recorded via QA), E14 (resolved) |
| Required inputs | Reproduction, observed vs expected, severity judgment |
| Expected outputs | A ship-decision-ready view of what is broken |
| Archive policy | RESOLVED/WONTFIX items rotate to `archive/KNOWN_ISSUES_<YYYY>.md` (K7.3); open items never |

## Severity and Status Models

**Severity** — three levels, judged by user impact: **CRITICAL** (blocks core use or corrupts data — blocks release, gate G4/G6), **MAJOR** (significant function degraded, workaround exists), **MINOR** (cosmetic, edge-case, papercut).

**Status** — `OPEN → INVESTIGATING → RESOLVED`, plus `WONTFIX` (deliberate, always with a D-NNN — accepting a defect is a decision, not a shrug).

## Entry Format

Table row per issue: `I-NNN · severity · status · area · summary · repro/evidence ref · refs (T-NNN fixing it, D-NNN if WONTFIX)`. Complex issues may add a subsection below the table (`### I-NNN`) with full reproduction and analysis — the row remains the index.

Rules: found ≠ fixed-later — E13 records at discovery, in the same session, however inconvenient (Article IV); a CRITICAL open issue is announced in CURRENT_STATUS §Doesn't work by reference; "limitations" (never-built, known-absent) are issues too, marked `limitation` in area — users don't distinguish.

## Structure

1. **Header** — per standard.
2. **Next ID** — counter (K5.1).
3. **Open** — table, CRITICAL first.
4. **Resolved / wontfix (recent)** — since last rotation.
5. **Details** — optional `### I-NNN` subsections.

## Skeleton

```markdown
# Known Issues — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-13 |
| Document | KNOWN_ISSUES.md |
| Class | I — Snapshot |
| Profile-tier | Standard+ |
| Owner | QA Engineer |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

Next ID: I-001

## Open
| ID | Sev | Status | Area | Summary | Evidence | Refs |
|---|---|---|---|---|---|---|

## Resolved / wontfix (recent)
| ID | Sev | Resolution | Summary | Refs |
|---|---|---|---|---|

## Details
```

## Maintenance Notes

The honesty organ of the instance (Article IV): its completeness is exactly as valuable as its worst omission. WF_RELEASE reads Open in full — an issue found post-release that was known pre-release and unrecorded is the framework's definition of failure.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: severity/status models, entry format |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

If issue volume warrants, per-area sub-tables (D2, additive). Severity model is deliberately three-level — resist inflation (P7).
