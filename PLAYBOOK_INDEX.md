# Playbook Index

| Field | Value |
|---|---|
| ID | OPRN-06 |
| Document | PLAYBOOK_INDEX.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Release Manager (content) / Orchestrator (situations) |
| Maintainer | Release Manager |
| Authority | The situation-to-procedure map of AMF: every recurring operational scenario resolved to its executing procedure. Owns only the thin scenarios no other document executes (§3). Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Translate theory into execution by *navigation*: an agent facing any operational situation finds here, in one lookup, exactly which procedure runs it — because in AMF the workflows, guides and registers *are* the playbooks, and duplicating them would rot (Article III; the brief's own rule: no duplicated procedures).
**Scope.** The scenario map plus compact cycles for the four scenarios that lacked a single home (§3). Procedure bodies live where they live.
**Responsibilities.** The map; the four thin-scenario cycles; the missing-scenario rule.
**Dependencies.** [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md) (selection rules — this map extends them from *requests* to *situations*), [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md).
**Consumers.** Every session at PLAN; adopters learning the framework by scenario.
**Related documents.** All workflows; [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md), [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md), [ARCHIVING.md](ARCHIVING.md), [FRAMEWORK_AUDIT.md](FRAMEWORK_AUDIT.md).
**Update policy.** D2 (Architect); new scenario rows are the expected cheap change.

---

## 1. How to Use

Find the situation, run the procedure. Every referenced procedure already defines the full playbook surface — trigger, preconditions, required context (T1), participating roles, steps, decision points, gates, failure paths, escalation, knowledge updates — in the uniform workflow shape ([WORKFLOW_INDEX.md §1](../workflows/WORKFLOW_INDEX.md)). Checklists: session-level in [SESSION_MANAGEMENT.md §3](../core/SESSION_MANAGEMENT.md), gate-level in [QUALITY_GATES.md](../quality/QUALITY_GATES.md), adoption in [ADOPTION_GUIDE.md §6](ADOPTION_GUIDE.md).

## 2. The Map

| Situation | Procedure |
|---|---|
| Project initialization / discovery / planning | [WF_NEW_PROJECT.md](../workflows/WF_NEW_PROJECT.md) + [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) (MADRE discovery: §4 there) |
| Architecture design | [WF_FEATURE.md](../workflows/WF_FEATURE.md) step 3 (per-feature) / [WF_NEW_PROJECT.md](../workflows/WF_NEW_PROJECT.md) steps 4–6 (founding) |
| Feature development | [WF_FEATURE.md](../workflows/WF_FEATURE.md) |
| Bug investigation / resolution | [WF_BUGFIX.md](../workflows/WF_BUGFIX.md) |
| Hotfix / emergency / incident | §3.1 below (until WF_INCIDENT exists) |
| Risk management | §3.2 below |
| Technical debt management | §3.3 below |
| Documentation updates / knowledge synchronization | [WF_DOCUMENTATION.md](../workflows/WF_DOCUMENTATION.md); per-session sync is Stage 6 + [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) |
| Research | [WF_RESEARCH.md](../workflows/WF_RESEARCH.md) |
| Code review | [WF_CODE_REVIEW.md](../workflows/WF_CODE_REVIEW.md) |
| Architecture review | [WF_ARCHITECTURE_REVIEW.md](../workflows/WF_ARCHITECTURE_REVIEW.md) |
| Security / performance review | [WF_CODE_REVIEW.md](../workflows/WF_CODE_REVIEW.md) or [WF_ARCHITECTURE_REVIEW.md](../workflows/WF_ARCHITECTURE_REVIEW.md) run under `Reviewer/QA[security \| performance]` specialization ([AGENT_LIBRARY.md §3](../agents/AGENT_LIBRARY.md)); security basics are already in every G3 ([REVIEW_STANDARDS.md §2](../quality/REVIEW_STANDARDS.md)) |
| Testing / QA validation | G4 execution per [QUALITY_GATES.md](../quality/QUALITY_GATES.md) inside the active workflow |
| Release preparation / deployment / rollback | [WF_RELEASE.md](../workflows/WF_RELEASE.md) (rollback: its abort paths + the package's per-release path) |
| Maintenance | [WF_MAINTENANCE.md](../workflows/WF_MAINTENANCE.md) |
| Framework upgrade / migration | [WF_MAINTENANCE.md](../workflows/WF_MAINTENANCE.md) E28 path + [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md) |
| Interrupted / corrupted state | [WF_RECOVERY.md](../workflows/WF_RECOVERY.md) |
| Project closure / archiving / reactivation | [ARCHIVING.md](ARCHIVING.md) |
| Retrospective / continuous improvement | §3.4 below |
| Framework self-audit | [FRAMEWORK_AUDIT.md](FRAMEWORK_AUDIT.md) |

## 3. Thin-Scenario Cycles

The four scenarios without a single executing home elsewhere. Each is a compact cycle over existing machinery — deliberately not a new workflow until evidence demands one (P9).

### 3.1 Incident / hotfix response

Trigger: production is broken or degrading *now*. Until the flagged WF_INCIDENT exists, run [WF_BUGFIX.md](../workflows/WF_BUGFIX.md) with three overrides:
1. **Owner informed immediately** (§5.1 trigger 7 territory — production impact is Owner-visible impact), before analysis completes.
2. **Mitigate before you cure**: rollback per the last RELEASE_HISTORY entry's path or disable the broken surface — a D3-speed decision the Owner makes on the spot; root-cause work follows as normal WF_BUGFIX.
3. **Record as you go, reconcile after**: the abbreviated-handover discipline ([SESSION_MANAGEMENT.md §5](../core/SESSION_MANAGEMENT.md)) applies from the start; E13 + E15 + E26 are mandatory closes (an incident always yields a lesson).

### 3.2 Risk management cycle

Continuous, not sessional: **identify** at any moment (E15, anyone — Risk Report); **score honestly** (L/M/H, [templates/RISK_REGISTER.md](../knowledge/templates/RISK_REGISTER.md)); **mitigate with an owner and a ref** or accept explicitly; **review** when work touches the risk's area (PLAN stage) and in full at [WF_ARCHITECTURE_REVIEW.md](../workflows/WF_ARCHITECTURE_REVIEW.md) step 5; **close or convert** (E16 — OCCURRED spawns the issue/task and the lesson). H/H exposure always reaches the Owner at next contact.

### 3.3 Technical debt cycle

**Take deliberately** (E24: D-ref + carrying cost + repayment trigger — never retroactively, [templates/TECHNICAL_DEBT.md](../knowledge/templates/TECHNICAL_DEBT.md)); **carry visibly** (debt pressure in CURRENT_STATUS §Health); **watch triggers** at PLAN; **repay** via [WF_REFACTORING.md](../workflows/WF_REFACTORING.md) when a trigger fires (E25); **audit** the register at [WF_ARCHITECTURE_REVIEW.md](../workflows/WF_ARCHITECTURE_REVIEW.md) step 5.

### 3.4 Retrospective / continuous improvement

Per project: at every milestone reached (E29) or release shipped (E23), the Orchestrator runs a short retrospective pass inside the closing session — what cost more than planned, what the ledgers show (gate failures, recovery events, E31 density), lessons written (E26, advice-titled per [templates/LESSONS_LEARNED.md](../knowledge/templates/LESSONS_LEARNED.md)). Per framework: lessons harvest → Proposals → MINOR releases, the loop owned by [VERSIONING.md §9](../core/VERSIONING.md) and executed at release planning per [FRAMEWORK_AUDIT.md §5](FRAMEWORK_AUDIT.md).

## 4. Missing-Scenario Rule

A situation with no row: the Orchestrator maps it to the nearest procedure, logs the mapping reasoning, and — if it recurs — raises a Proposal for a row here or a new workflow ([EXTENDING_AMF.md](EXTENDING_AMF.md)); mirrors [WORKFLOW_INDEX.md §3](../workflows/WORKFLOW_INDEX.md) rule 12 at the situation level.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-13 | Architect (AI), Phase 8 (Operational Playbooks) | Initial map + four thin-scenario cycles |

## Future Extension Notes

Rows graduate to workflows on evidence: incident response (3.1) is first in line — its overrides are a WF_INCIDENT specification in waiting.
