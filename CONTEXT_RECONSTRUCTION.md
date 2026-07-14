# Context Reconstruction

| Field | Value |
|---|---|
| ID | KNOW-02 |
| Document | CONTEXT_RECONSTRUCTION.md |
| Module | knowledge |
| Class | S — Stable spec |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Single source of truth for reading tiers and per-workflow reading lists. Workflows embed these lists by reference, never by copy. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Make context reconstruction a bounded, specified operation: define what every session reads always (T0), what each workflow reads (T1), and what is read only on demand or never by default — so a cold session recovers full working context within a finite budget.

**Scope.** Reading order and reading discipline for project sessions. Not what documents contain ([KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md), templates/) and not when they update ([UPDATE_MATRIX.md](UPDATE_MATRIX.md)).

**Responsibilities.** Tier definitions; the T0 sequence; per-workflow T1 reading lists; deep-onboarding order; reading discipline rules.

**Dependencies.** [KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md) (registry, tiers column), [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) (Stage 2 contract), [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) (AD-3).

**Consumers.** Every session at Stage 2; workflow authors (each workflow references its row here).

**Related documents.** [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md), templates/HANDOVER.md, templates/CURRENT_STATUS.md.

**Update policy.** D2 (Architect). Tuning a T1 list is the expected, cheap change (MINOR); changing tier definitions touches the compatibility discussion in [VERSIONING.md](../core/VERSIONING.md) and is D3.

---

## 1. Reading Tiers

| Tier | Definition | When read |
|---|---|---|
| **T0** | The invariant minimum: bootstrap, configuration, present state, latest handover | Always, every session, in the fixed order of §2 |
| **T1** | The active workflow's declared list (§3) | After workflow selection, before planning |
| **T2** | Anything referenced by T0/T1 content or needed by the work in hand | On demand, when the reference is followed |
| **T3** | `archive/`, rotated ledger years, ARCHIVED documents, AI_NOTES, LESSONS_LEARNED | Never by default; reading requires a logged reason |

Tier membership defaults per document are in the [KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md) §2 registry; this document's lists bind per workflow.

## 2. T0 — The Invariant Sequence

Four reads, fixed order, no exceptions:

1. **`CLAUDE.md`** (project root) — the bootstrap pointer: which framework version, where the instance is.
2. **`.amf/INSTANCE.md`** — profile, pinned version, active documents, deviations in force.
3. **`.amf/knowledge/CURRENT_STATUS.md`** — the project as the last session left it.
4. **Latest handover** (`.amf/sessions/handovers/`, newest) — exact resumption point, warnings, next actions.

If any T0 document is missing or stale-stamped, that is itself the first finding of the session: an interruption or knowledge defect to resolve before work ([SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) §5, Article IV).

## 3. T1 — Per-Workflow Reading Lists

Section addressing (`DOC §Section`) means read that section, not the whole file (§4, D1 discipline). "DECISIONS (index + relevant)" means the index table plus entries the work touches.

| Workflow | T1 list, in order |
|---|---|
| WF_NEW_PROJECT | No instance yet: [ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md) + [PROFILES.md](../operations/PROFILES.md). After instantiation, the session's own outputs are its context. |
| WF_FEATURE | PROJECT §Goals+§Scope · ARCHITECTURE · TASKS · BACKLOG (the item) · DECISIONS (index + relevant) · KNOWN_ISSUES (affected area) |
| WF_BUGFIX | KNOWN_ISSUES (the issue) · ARCHITECTURE (affected area) · TASKS · DEPENDENCIES (if dependency-related) · DECISIONS (index) |
| WF_REFACTORING | ARCHITECTURE · TECHNICAL_DEBT (the item) · DECISIONS (index + relevant) · KNOWN_ISSUES (affected area) |
| WF_ARCHITECTURE_REVIEW | ARCHITECTURE (full) · DECISIONS (full index, entries as needed) · TECHNICAL_DEBT · RISK_REGISTER · KNOWN_ISSUES · ASSUMPTIONS |
| WF_CODE_REVIEW | [REVIEW_STANDARDS.md](../quality/REVIEW_STANDARDS.md) + [DEFINITION_OF_DONE.md](../quality/DEFINITION_OF_DONE.md) (framework) · ARCHITECTURE (affected area) · the task's context (T-NNN + its refs) |
| WF_RELEASE | CHANGELOG §Unreleased · KNOWN_ISSUES (open) · TASKS (open) · RELEASE_HISTORY (last entry) · ROADMAP (the milestone) |
| WF_MAINTENANCE | DEPENDENCIES · KNOWN_ISSUES · TECHNICAL_DEBT · CHANGELOG §Unreleased |
| WF_RESEARCH | OPEN_QUESTIONS (the question) · RESEARCH (related entries) · ASSUMPTIONS (related) · ARCHITECTURE (if technical) |
| WF_DOCUMENTATION | [KNOWLEDGE_SYSTEM.md](KNOWLEDGE_SYSTEM.md) §8 (quality rules) · every active instance document's header + structure (audit pass, not full read) |
| WF_RECOVERY | SESSION_LOG (last entries) · the interrupted session's partial record · every document stamped with the interrupted session's ID · latest complete handover |

Rules:

- **C3.1** These lists are the single source of truth. Workflows cite their row; copying a list into a workflow is an Article III violation.
- **C3.2** Lists assume Standard/Full profiles; in Minimal, folded documents resolve to their folded sections (folding map: [PROFILES.md §2](../operations/PROFILES.md)).
- **C3.3** A workflow added later must add its row here first (extension procedure).

## 4. Reading Discipline

- **C4.1** **Budget.** T0 + the T1 row is the budget. Reading beyond it is permitted with a logged reason ([SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) Stage 2); reading *less* requires the same justification as skipping a stage.
- **C4.2** **Sections over files.** Where the list addresses a section, read the section. Whole-file reads of large snapshots to "get oriented" are what T0 exists to prevent.
- **C4.3** **Follow, don't hoard.** T2 is pulled when a reference is actually followed — not preloaded speculatively.
- **C4.4** **T3 is deliberate.** Archive and low-authority documents (AI_NOTES) are read only with a logged reason: investigating history, an audit, or recovery.
- **C4.5** **Failure to reconstruct is a finding.** If, after the budget, the agent cannot state project state, constraints and relevant prior decisions, the knowledge system has a defect: record it (Article IV, issue or lesson), *then* widen reading — never silently compensate.

## 5. Deep Onboarding Order

For the rare full-context need (new long-term engagement, architecture review of an unfamiliar project, audits), the canonical complete order — after T0:

1. PROJECT (full) — why the project exists
2. ARCHITECTURE (full) — how it is built
3. DECISIONS (index, then entries newest-first) — why it is built that way
4. ROADMAP → TASKS → BACKLOG — where it is going
5. KNOWN_ISSUES → RISK_REGISTER → TECHNICAL_DEBT → DEPENDENCIES — what constrains it
6. ASSUMPTIONS → OPEN_QUESTIONS → RESEARCH — what is uncertain
7. CHANGELOG / RELEASE_HISTORY / SESSION_LOG — how it got here (skim, newest-first)
8. LESSONS_LEARNED, AI_NOTES — T3, only if the engagement warrants it

This order is informative, not a session requirement; invoking it is a logged deviation under C4.1.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial tiers, T0 sequence, eleven T1 lists, reading discipline, deep-onboarding order |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 5 forward reference (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- T1 lists are the framework's most tunable surface: expect MINOR revisions from real-project evidence (VERSIONING §9); WF_FEATURE's list is the first candidate flagged for tuning.
- Phase 6 swept its references; every workflow has a row (C3.3, verified).
- If context-size telemetry becomes available (tooling direction), each row can gain a measured typical-cost column — informative only.
