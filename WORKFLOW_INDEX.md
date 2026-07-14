# Workflow Index

| Field | Value |
|---|---|
| ID | WFLW-01 |
| Document | WORKFLOW_INDEX.md |
| Module | workflows |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Orchestrator (content) / Architect (structure) |
| Maintainer | Orchestrator |
| Authority | Normative catalog and selection rules: every session request maps here to exactly one workflow. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Make workflow selection deterministic: the Orchestrator classifies every request through the ordered rules below at INITIALIZE ([SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) Stage 1).
**Scope.** Catalog and selection. Each workflow's procedure is its own file; the common lifecycle is [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md)'s.
**Responsibilities.** The catalog; the selection rules; the composition rule for mixed requests.
**Dependencies.** [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md), [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) (every workflow has its reading row — C3.3).
**Consumers.** Orchestrator, every session, Stage 1.
**Related documents.** The eleven WF_* files; operations/EXTENDING_AMF.md (adding workflows).
**Update policy.** D2 (Architect for structure, new workflows via extension procedure); selection rule changes are D2.

---

## 1. How Workflows Work

A workflow details the PLAN→DOCUMENT specifics of one session type; Stages 1–2 and 7 are common to all ([SESSION_MANAGEMENT.md §2](../core/SESSION_MANAGEMENT.md)). Every workflow declares: trigger, T1 reading (by reference to its [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) row — never copied, C3.1), roles per step, messages emitted, E-codes applied, gates in scope (authority per [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md), criteria per [QUALITY_GATES.md](../quality/QUALITY_GATES.md)), and failure/abort paths.

## 2. Catalog

| Workflow | One line | File |
|---|---|---|
| WF_NEW_PROJECT | Instantiate AMF, run discovery, bootstrap the instance | [WF_NEW_PROJECT.md](WF_NEW_PROJECT.md) |
| WF_FEATURE | New capability, G0→G5 (+G6 when shipping) | [WF_FEATURE.md](WF_FEATURE.md) |
| WF_BUGFIX | Defect: reproduce → cause → fix → verify → close | [WF_BUGFIX.md](WF_BUGFIX.md) |
| WF_REFACTORING | Behavior-preserving change; debt retirement | [WF_REFACTORING.md](WF_REFACTORING.md) |
| WF_ARCHITECTURE_REVIEW | Periodic/triggered design audit | [WF_ARCHITECTURE_REVIEW.md](WF_ARCHITECTURE_REVIEW.md) |
| WF_CODE_REVIEW | Standalone review session | [WF_CODE_REVIEW.md](WF_CODE_REVIEW.md) |
| WF_RELEASE | Ship: G4–G6, cut, deploy, record | [WF_RELEASE.md](WF_RELEASE.md) |
| WF_MAINTENANCE | Dependency updates, housekeeping, framework upgrades | [WF_MAINTENANCE.md](WF_MAINTENANCE.md) |
| WF_RESEARCH | Investigation answering a Q-NNN or feeding a decision | [WF_RESEARCH.md](WF_RESEARCH.md) |
| WF_DOCUMENTATION | Knowledge audit and repair | [WF_DOCUMENTATION.md](WF_DOCUMENTATION.md) |
| WF_RECOVERY | Reconcile an interrupted/corrupted predecessor session | [WF_RECOVERY.md](WF_RECOVERY.md) |

## 3. Selection Rules

Ordered; **first match wins** — this is what makes every plausible request map to exactly one workflow:

1. The previous session is unclosed (log entry without handover — S1.4)? → **WF_RECOVERY**, before anything else. The original request waits.
2. No `.amf/` instance exists? → **WF_NEW_PROJECT**.
3. Request is to ship/deploy/publish? → **WF_RELEASE**.
4. Something that worked is broken, or an I-NNN is being addressed? → **WF_BUGFIX**.
5. New capability or change in behavior users can see? → **WF_FEATURE**.
6. Improve structure without changing behavior (debt, cleanup, restructure)? → **WF_REFACTORING**.
7. Update dependencies / housekeeping batch / framework upgrade (E28)? → **WF_MAINTENANCE**.
8. Answer a question / investigate before deciding? → **WF_RESEARCH**.
9. Audit or repair the design as a whole? → **WF_ARCHITECTURE_REVIEW**.
10. Review existing work as the session's purpose? → **WF_CODE_REVIEW**.
11. Fix/improve the knowledge itself (E31 backlog, audit, rotations)? → **WF_DOCUMENTATION**.
12. **None of the above**: Orchestrator selects the nearest workflow, logs the classification reasoning, and — if the case recurs — raises a Proposal to extend this index (M5.1 pattern).

**Composition rule.** A mixed request ("fix X and add Y") is split at PLAN: the primary intent selects the workflow (rules order = priority order); the remainder becomes tasks or backlog items for their own sessions (S1.2). A small discovery mid-workflow (a bug found while building a feature) may be absorbed with logged justification — S1.2's legitimate case — or spun off as an I-NNN.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 | Initial catalog + ordered selection rules |

## Future Extension Notes

New workflows enter per operations/EXTENDING_AMF.md: reading row first (C3.3), then the WF_ file, then a catalog row and a selection rule positioned deliberately in the order. Anticipated candidates: WF_MIGRATION (data/platform moves), WF_INCIDENT (production events) — awaiting evidence (P9).
