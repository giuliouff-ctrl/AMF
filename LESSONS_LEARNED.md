# Standard — LESSONS_LEARNED.md

| Field | Value |
|---|---|
| ID | KNOW-21 |
| Document | templates/LESSONS_LEARNED.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `LESSONS_LEARNED.md` — the append-only ledger of retrospective insight. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the lessons ledger: what this project taught — feeding both this project's future sessions and the framework's own evolution ([VERSIONING.md](../../core/VERSIONING.md) §9 builds releases from these).
**Scope.** Structure and rules of `LESSONS_LEARNED.md`; not incident records (KNOWN_ISSUES, RISK_REGISTER §occurred), not framework change proposals ([Proposal message](../../communication/MESSAGE_TYPES.md) — a lesson may *trigger* one).
**Responsibilities.** Specification, entry format, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4/§5, [FRAMEWORK_RULES.md](../../core/FRAMEWORK_RULES.md) R4.1 (L-NNN); [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) §2.4 (systemic violations must land here).
**Consumers.** Orchestrator (owner), Architect (framework evolution harvest), retrospective passes.
**Related documents.** templates/RISK_REGISTER.md (E16), templates/ASSUMPTIONS.md (E18); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E26.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/LESSONS_LEARNED.md` |
| Class | **A — Ledger** |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | **T3** — read at retrospectives, framework harvest, and deep onboarding only |
| Profile | Full (Minimal/Standard: lessons worth keeping go to AI_NOTES fold or directly into the framework Proposal they justify, per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E26; mandatory after E16 OCCURRED, E18 invalidation, constitutional violations (§2.4) |
| Required inputs | What happened, what it cost, what changes |
| Expected outputs | Fewer repeated mistakes; evidence for framework MINORs |
| Archive policy | K7.2 by age |

## Entry Format

```markdown
## L-NNN — <lesson, stated as advice>
- **Date/Session:** <YYYY-MM-DD> · <S-ID> · **Trigger:** <what happened — R-NNN occurred, A invalidated, violation, plain hindsight>
- **What happened:** <the concrete story, short>
- **Cost:** <time lost, rework, trust — honest>
- **Lesson:** <the transferable insight>
- **Change:** <what now differs: a convention adopted (ARCHITECTURE §Conventions), a check added, a framework Proposal raised — with ref | "awareness only">
```

Rules: the title is the *advice*, not the anecdote ("Verify free-tier quotas before designing around a service", not "Firestore problem") — the ledger is skimmed by future sessions reading titles; successes qualify (a thing that worked surprisingly well is a lesson too); a lesson with `Change: awareness only` three times over is a lesson being ignored — that itself is an E26.

## Structure

1. **Header** — per standard.
2. **Next ID** — counter (K5.1).
3. **Entries** — newest last.

## Skeleton

```markdown
# Lessons Learned — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-21 |
| Document | LESSONS_LEARNED.md |
| Class | A — Ledger |
| Profile-tier | Full |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

Next ID: L-001

## Entries
```

## Maintenance Notes

The framework's own feedstock: at release planning, the Architect harvests instance lessons for the next AMF version (VERSIONING §9 — evidence-driven roadmap). Write entries knowing they have two readers: this project's next session, and the framework's next version.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: advice-titled entries, change tracking |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 4 forward reference (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Cross-project lessons library is a named v2 direction (architecture §14.2); this format is designed to aggregate as-is.
