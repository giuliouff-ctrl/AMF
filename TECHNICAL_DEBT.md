# Standard — TECHNICAL_DEBT.md

| Field | Value |
|---|---|
| ID | KNOW-14 |
| Document | templates/TECHNICAL_DEBT.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `TECHNICAL_DEBT.md` — deliberate compromises, registered with intent. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the debt register: every deliberate shortcut, its cost, and the condition under which it gets repaid — so debt is a managed instrument, not an accumulating secret.
**Scope.** Structure and rules of `TECHNICAL_DEBT.md`; not defects (KNOWN_ISSUES — broken is not debt), not the decision to take debt (DECISIONS, always linked).
**Responsibilities.** Specification, entry format, debt discipline, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4; templates/DECISIONS.md (E24 requires a D-ref).
**Consumers.** Architect (owner), WF_REFACTORING (T1: the item), WF_MAINTENANCE, Reviewer (G3: new undeclared debt is a finding).
**Related documents.** templates/KNOWN_ISSUES.md (boundary above); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E24/E25.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/TECHNICAL_DEBT.md` |
| Class | I — Snapshot |
| Knowledge domain | Technical design |
| Owner (role) | Architect |
| Default read tier | T1 (WF_REFACTORING, WF_ARCHITECTURE_REVIEW), T2 otherwise |
| Profile | Full (Minimal/Standard: folds into ARCHITECTURE §Invariants-adjacent note per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E24 (taken — with D-NNN), E25 (retired) |
| Required inputs | The compromise, its reason, its carrying cost, its repayment trigger |
| Expected outputs | A prioritizable repayment queue; honest debt pressure for CURRENT_STATUS §Health |
| Archive policy | Retired items rotate to `archive/TECHNICAL_DEBT_<YYYY>.md` (K7.3) |

## Entry Format

Per item: **title** · taken (date, S-ID, D-NNN) · **what was compromised** · **why** (one line — full rationale in the D-record) · **carrying cost** (what it makes slower/riskier while it exists) · **repayment trigger** ("repay when/if X") · status (CARRIED / REPAYING-T-NNN / RETIRED).

Rules: debt is *deliberate* — an accidental mess found later is an issue (I-NNN) or an immediate fix, not retroactive "debt" (Article IV: the register never launders negligence into strategy); every entry has its D-NNN (E24 — taking debt is a D2, someone chose it); a repayment trigger is mandatory: debt with no trigger is a euphemism for "never".

## Structure

1. **Header** — per standard.
2. **Carried** — items, heaviest carrying cost first.
3. **Recently retired** — since last rotation.

## Skeleton

```markdown
# Technical Debt — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-14 |
| Document | TECHNICAL_DEBT.md |
| Class | I — Snapshot |
| Profile-tier | Full |
| Owner | Architect |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Carried
- **<title>** — taken <date> · <S-ID> · D-NNN
  - Compromised: <what>
  - Why: <one line>
  - Carrying cost: <what it makes slower/riskier>
  - Repay when: <trigger>
  - Status: CARRIED

## Recently retired
- **<title>** — retired <S-ID>, by T-NNN
```

## Maintenance Notes

The Reviewer's G3 checklist ([QUALITY_GATES.md](../../quality/QUALITY_GATES.md) item 3.3) includes "does this change take undeclared debt?" — this register is where a PASS_WITH_NOTES lands. Debt pressure (count × carrying cost, judged) feeds CURRENT_STATUS §Health in one word.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: entry format, debt discipline |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 5 forward reference (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

DT-NNN IDs if cross-referencing demand appears (R4 addition, D2); withheld pending evidence (P9).
