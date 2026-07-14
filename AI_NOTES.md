# Standard — AI_NOTES.md

| Field | Value |
|---|---|
| ID | KNOW-23 |
| Document | templates/AI_NOTES.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `AI_NOTES.md` — the lowest-authority holding pen for observations with no home yet. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the notes ledger: the safety valve that keeps K8.5 honest — observations, hunches and oddities that fit no owned document get written here instead of being lost or misfiled.
**Scope.** Structure and rules of `AI_NOTES.md`; explicitly *not* a shadow home for anything the registry already owns.
**Responsibilities.** Specification, entry format, triage rule, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4, K8.5; [AI_CONSTITUTION.md](../../core/AI_CONSTITUTION.md) Article II (session artifacts vs. standing knowledge).
**Consumers.** Any role (writes); WF_DOCUMENTATION (triage pass); deep onboarding (T3, optional).
**Related documents.** every owned document (triage destinations); [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E30.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/AI_NOTES.md` |
| Class | **A — Ledger** |
| Knowledge domain | Unhomed observations (lowest authority in the instance) |
| Owner (role) | any role writes; Orchestrator triages |
| Default read tier | **T3** — never by default |
| Profile | Full (Minimal/Standard: fold per the [folding map](../../operations/PROFILES.md) — a short Notes section wherever it lands) |
| Update triggers | E30 (observation with no home) |
| Required inputs | The observation + a suggested home |
| Expected outputs | Nothing lost; nothing squatting — entries either graduate to owned documents or expire |
| Archive policy | Triaged entries rotate to `archive/AI_NOTES_<YYYY>.md` (K7.3) with disposition |

## Entry Format

One line per note: `<YYYY-MM-DD> · <S-ID> · <observation> · suggested home: <doc / "none, hunch">`. Multi-line only when the observation genuinely needs it.

**Triage rule (the standard's core):** at every WF_DOCUMENTATION session — and opportunistically at any session's Stage 6 — open notes are dispositioned: **graduate** (an E-code applies after all → move to the owned document, mark the note), **expire** (no longer relevant → mark), or **hold** (still unclear → keep, max ~2 triage cycles before it must graduate or expire). AI_NOTES is a buffer, not a residence (K8.5: never a shadow knowledge base).

**Authority rule:** nothing here binds anything. A note is a hunch until it graduates; citing AI_NOTES as authority for a decision is an Article II violation.

## Structure

1. **Header** — per standard.
2. **Open notes** — untriaged lines.
3. **Triaged (recent)** — dispositioned since last rotation.

## Skeleton

```markdown
# AI Notes — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-23 |
| Document | AI_NOTES.md |
| Class | A — Ledger |
| Profile-tier | Full |
| Owner | any role (writes) / Orchestrator (triage) |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Open notes
- <YYYY-MM-DD> · <S-ID> · <observation> · suggested home: <doc>

## Triaged (recent)
- <note> → graduated to <doc> | expired (<S-ID>)
```

## Maintenance Notes

Existence test for a healthy instance: this file is *short*. Long AI_NOTES means either triage isn't happening (process defect) or the registry is missing a document type (raise the Proposal — that's exactly the signal K8.5 wants).

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: entry format, triage rule, authority rule |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

None — this document's design goal is to stay the smallest, least important file in the instance.
