# Standard — RISK_REGISTER.md

| Field | Value |
|---|---|
| ID | KNOW-15 |
| Document | templates/RISK_REGISTER.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `RISK_REGISTER.md` — uncertain events with project impact, tracked with mitigation. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the risk register: what could hurt the project, how likely, how bad, and what we're doing about it — surfaced before it happens, not after.
**Scope.** Structure and rules of `RISK_REGISTER.md`; not occurred defects (KNOWN_ISSUES), not deliberate compromises (TECHNICAL_DEBT).
**Responsibilities.** Specification, scoring model, entry format, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4/§5, [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (R-NNN).
**Consumers.** Orchestrator (owner), all roles (E15 duty), WF_ARCHITECTURE_REVIEW, Human Owner (exposure awareness).
**Related documents.** templates/KNOWN_ISSUES.md, templates/LESSONS_LEARNED.md (occurred risks feed lessons); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E15/E16.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/RISK_REGISTER.md` |
| Class | I — Snapshot |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | T1 (WF_ARCHITECTURE_REVIEW), T2 otherwise |
| Profile | Full (Minimal/Standard: folds into CURRENT_STATUS §Blocked/waiting notes per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E15 (identified), E16 (changed/closed/occurred) |
| Required inputs | The uncertain event, its trigger, its impact channel |
| Expected outputs | An exposure view the Owner can act on; mitigations owned and dated |
| Archive policy | CLOSED/OCCURRED items rotate to `archive/RISK_REGISTER_<YYYY>.md` (K7.3) |

## Scoring Model

Likelihood × impact, each **L / M / H** — judged, not computed; three levels resist false precision (P7). Exposure = the pair ("H/M"). Anything H/H is announced in CURRENT_STATUS and flagged to the Owner at next contact (E22 opportunity).

**Status:** `OPEN → MITIGATING → CLOSED` plus `OCCURRED` (it happened: spawn the I-NNN/T-NNN it implies, write the L-NNN lesson — E16's conditional).

## Entry Format

Table row: `R-NNN · risk (event, not fear — "Firestore free tier exceeded", not "database problems") · likelihood · impact · mitigation (action, not intention) · owner role · status · refs`.

Rules: mitigation names an *action with an owner* ("cache reads client-side — Engineer, T-023"), else it is `accepted` explicitly — silent unmitigated risks are the register lying (Article IV); risks that stopped being uncertain move out: OCCURRED → issue/task, impossible → CLOSED with note.

## Structure

1. **Header** — per standard.
2. **Next ID** — counter (K5.1).
3. **Open** — table, exposure-sorted (H/H first).
4. **Closed / occurred (recent)** — since last rotation.

## Skeleton

```markdown
# Risk Register — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-15 |
| Document | RISK_REGISTER.md |
| Class | I — Snapshot |
| Profile-tier | Full |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

Next ID: R-001

## Open
| ID | Risk | L | I | Mitigation | Owner | Status | Refs |
|---|---|---|---|---|---|---|---|

## Closed / occurred (recent)
| ID | Risk | Outcome | Refs |
|---|---|---|---|
```

## Maintenance Notes

Reviewed at planning when the session's work touches a risk's area, and in full at WF_ARCHITECTURE_REVIEW. The register's failure mode is theater: ten stale L/L entries and the real H/H unlisted. Fewer, truer rows (K8.1).

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: L/M/H model, entry format |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Numeric scoring only if a project's Owner requires reporting in that form — a presentation concern, not a model change.
