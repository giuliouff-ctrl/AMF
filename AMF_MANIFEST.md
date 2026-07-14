# AMF Manifest

| Field | Value |
|---|---|
| ID | ROOT-01 |
| Document | AMF_MANIFEST.md |
| Module | root |
| Class | S — Stable spec |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Orchestrator |
| Maintainer | Orchestrator (registry) / Architect (structure) |
| Authority | Single entry point and authoritative document registry of AMF (AD-9). Navigation only — it indexes everything and governs nothing. Subordinate to [core](core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Be the one place any reader — human or AI — starts: what AMF is, what to read first for your situation, and the complete registry of what exists.
**Scope.** Navigation and registry. No content authority: every fact this file points at lives in its owning document.
**Responsibilities.** Start-here paths; module map; the document registry; registry maintenance rules.
**Dependencies.** None normatively (AD-9 — a pure index cannot create cycles); it lists all modules.
**Consumers.** Everyone, first.
**Related documents.** All of them — that is the point.
**Update policy.** Registry rows update on every document addition/removal/status/version change (R10.6, D1 by the Maintainer); structural changes are D2.

---

## 1. What This Is

**AMF (AI Multi-Agent Framework) v1.0.0** — an engineering operating system that turns an AI coding agent into a structured engineering organization: seven roles with explicit authority, a per-project memory that survives sessions, ten message types, seven quality gates, eleven workflows, three adoption profiles. Certification status: **C0 — Audited** ([CERTIFICATION.md §4](operations/CERTIFICATION.md)). Identity and mission: [core/AMF_OVERVIEW.md](core/AMF_OVERVIEW.md). Design rationale: [AMF_ARCHITECTURE.md](AMF_ARCHITECTURE.md) (frozen).

## 2. Start Here

| You are | Read, in order |
|---|---|
| **A human, new to AMF** | [core/AMF_OVERVIEW.md](core/AMF_OVERVIEW.md) → [core/AI_CONSTITUTION.md](core/AI_CONSTITUTION.md) → [operations/ADOPTION_GUIDE.md](operations/ADOPTION_GUIDE.md) (incl. its dry-run §7) → skim [core/FRAMEWORK_GLOSSARY.md](core/FRAMEWORK_GLOSSARY.md) |
| **An AI session working on a project** | Never here first — the project's `CLAUDE.md` → `.amf/INSTANCE.md`, then [core/SESSION_MANAGEMENT.md](core/SESSION_MANAGEMENT.md) (seven stages) with reading budget per [knowledge/CONTEXT_RECONSTRUCTION.md](knowledge/CONTEXT_RECONSTRUCTION.md) |
| **An AI session working on AMF itself** | [AMF_ARCHITECTURE.md](AMF_ARCHITECTURE.md) (the frozen design contract) → [core/FRAMEWORK_GOVERNANCE.md](core/FRAMEWORK_GOVERNANCE.md) (what may change and how) → the documents your change touches |
| **Adopting AMF into a project** | [operations/ADOPTION_GUIDE.md](operations/ADOPTION_GUIDE.md) → [operations/PROFILES.md](operations/PROFILES.md) → [workflows/WF_NEW_PROJECT.md](workflows/WF_NEW_PROJECT.md) |
| **Any operational situation** ("which procedure runs X?") | [operations/PLAYBOOK_INDEX.md](operations/PLAYBOOK_INDEX.md) |
| **Any terminology doubt** | [core/FRAMEWORK_GLOSSARY.md](core/FRAMEWORK_GLOSSARY.md), always |

Reading tiers (T0–T3) and per-workflow reading lists: [knowledge/CONTEXT_RECONSTRUCTION.md](knowledge/CONTEXT_RECONSTRUCTION.md) — the single source of truth for reading order; this manifest never duplicates it. Every official artifact structure: [SCHEMA_REGISTRY.md](SCHEMA_REGISTRY.md).

## 3. Module Map

Dependencies run strictly downward ([AMF_ARCHITECTURE.md §8](AMF_ARCHITECTURE.md)):

| Module | Owns | Spec entry |
|---|---|---|
| `core/` | Constitution, governance, principles, rules, glossary, sessions, versioning | [AMF_OVERVIEW.md](core/AMF_OVERVIEW.md) |
| `knowledge/` | Instance memory: 22 document standards, reading tiers, update matrix | [KNOWLEDGE_SYSTEM.md](knowledge/KNOWLEDGE_SYSTEM.md) |
| `agents/` | Seven role contracts, decision classes in operation, escalation; title mapping in [AGENT_LIBRARY.md](agents/AGENT_LIBRARY.md) | [AGENT_SYSTEM.md](agents/AGENT_SYSTEM.md) |
| `communication/` | Envelope + ten message types | [COMMUNICATION_PROTOCOL.md](communication/COMMUNICATION_PROTOCOL.md) |
| `quality/` | Gates G0–G6, DoD, review standards | [QUALITY_SYSTEM.md](quality/QUALITY_SYSTEM.md) |
| `workflows/` | Eleven session procedures + selection rules | [WORKFLOW_INDEX.md](workflows/WORKFLOW_INDEX.md) |
| `operations/` | Adoption, profiles, upgrade, extension, archiving, playbook map, framework audit, certification | [ADOPTION_GUIDE.md](operations/ADOPTION_GUIDE.md) |

## 4. Document Registry

Authoritative (R10.6; ownership view: [core/FRAMEWORK_GOVERNANCE.md §3](core/FRAMEWORK_GOVERNANCE.md)). Generated from document headers; a row disagreeing with its file's header is a defect in whichever was updated last.

| ID | Document | Class | Version | Status |
|---|---|---|---|---|
| ROOT-01 | [AMF_MANIFEST.md](AMF_MANIFEST.md) | S | 1.0.2 | ACTIVE |
| ROOT-02 | [README.md](README.md) | S | 1.0.0 | ACTIVE |
| ROOT-03 | [AMF_ARCHITECTURE.md](AMF_ARCHITECTURE.md) | C | 1.0.0 | ACTIVE (frozen) |
| ROOT-04 | [SCHEMA_REGISTRY.md](SCHEMA_REGISTRY.md) | S | 1.0.0 | ACTIVE |
| CORE-01 | [core/AMF_OVERVIEW.md](core/AMF_OVERVIEW.md) | C | 1.0.5 | ACTIVE |
| CORE-02 | [core/AI_CONSTITUTION.md](core/AI_CONSTITUTION.md) | C | 1.0.0 | ACTIVE |
| CORE-03 | [core/FRAMEWORK_GOVERNANCE.md](core/FRAMEWORK_GOVERNANCE.md) | C | 1.0.5 | ACTIVE |
| CORE-04 | [core/FRAMEWORK_PRINCIPLES.md](core/FRAMEWORK_PRINCIPLES.md) | C | 1.0.0 | ACTIVE |
| CORE-05 | [core/FRAMEWORK_RULES.md](core/FRAMEWORK_RULES.md) | C | 1.1.1 | ACTIVE |
| CORE-06 | [core/FRAMEWORK_GLOSSARY.md](core/FRAMEWORK_GLOSSARY.md) | C | 1.6.0 | ACTIVE |
| CORE-07 | [core/SESSION_MANAGEMENT.md](core/SESSION_MANAGEMENT.md) | C | 1.0.4 | ACTIVE |
| CORE-08 | [core/VERSIONING.md](core/VERSIONING.md) | C | 1.0.2 | ACTIVE |
| KNOW-01 | [knowledge/KNOWLEDGE_SYSTEM.md](knowledge/KNOWLEDGE_SYSTEM.md) | S | 1.0.2 | ACTIVE |
| KNOW-02 | [knowledge/CONTEXT_RECONSTRUCTION.md](knowledge/CONTEXT_RECONSTRUCTION.md) | S | 1.0.2 | ACTIVE |
| KNOW-03 | [knowledge/UPDATE_MATRIX.md](knowledge/UPDATE_MATRIX.md) | S | 1.0.1 | ACTIVE |
| KNOW-04 | [knowledge/templates/INSTANCE.md](knowledge/templates/INSTANCE.md) | T | 1.0.1 | ACTIVE |
| KNOW-05 | [knowledge/templates/PROJECT.md](knowledge/templates/PROJECT.md) | T | 1.0.0 | ACTIVE |
| KNOW-06 | [knowledge/templates/ARCHITECTURE.md](knowledge/templates/ARCHITECTURE.md) | T | 1.0.0 | ACTIVE |
| KNOW-07 | [knowledge/templates/ROADMAP.md](knowledge/templates/ROADMAP.md) | T | 1.0.1 | ACTIVE |
| KNOW-08 | [knowledge/templates/TASKS.md](knowledge/templates/TASKS.md) | T | 1.0.1 | ACTIVE |
| KNOW-09 | [knowledge/templates/BACKLOG.md](knowledge/templates/BACKLOG.md) | T | 1.0.2 | ACTIVE |
| KNOW-10 | [knowledge/templates/DECISIONS.md](knowledge/templates/DECISIONS.md) | T | 1.0.1 | ACTIVE |
| KNOW-11 | [knowledge/templates/CURRENT_STATUS.md](knowledge/templates/CURRENT_STATUS.md) | T | 1.0.1 | ACTIVE |
| KNOW-12 | [knowledge/templates/CHANGELOG.md](knowledge/templates/CHANGELOG.md) | T | 1.0.1 | ACTIVE |
| KNOW-13 | [knowledge/templates/KNOWN_ISSUES.md](knowledge/templates/KNOWN_ISSUES.md) | T | 1.0.1 | ACTIVE |
| KNOW-14 | [knowledge/templates/TECHNICAL_DEBT.md](knowledge/templates/TECHNICAL_DEBT.md) | T | 1.0.2 | ACTIVE |
| KNOW-15 | [knowledge/templates/RISK_REGISTER.md](knowledge/templates/RISK_REGISTER.md) | T | 1.0.1 | ACTIVE |
| KNOW-16 | [knowledge/templates/DEPENDENCIES.md](knowledge/templates/DEPENDENCIES.md) | T | 1.0.1 | ACTIVE |
| KNOW-17 | [knowledge/templates/ASSUMPTIONS.md](knowledge/templates/ASSUMPTIONS.md) | T | 1.0.1 | ACTIVE |
| KNOW-18 | [knowledge/templates/OPEN_QUESTIONS.md](knowledge/templates/OPEN_QUESTIONS.md) | T | 1.0.1 | ACTIVE |
| KNOW-19 | [knowledge/templates/RESEARCH.md](knowledge/templates/RESEARCH.md) | T | 1.0.1 | ACTIVE |
| KNOW-20 | [knowledge/templates/MEETING_NOTES.md](knowledge/templates/MEETING_NOTES.md) | T | 1.0.1 | ACTIVE |
| KNOW-21 | [knowledge/templates/LESSONS_LEARNED.md](knowledge/templates/LESSONS_LEARNED.md) | T | 1.0.2 | ACTIVE |
| KNOW-22 | [knowledge/templates/RELEASE_HISTORY.md](knowledge/templates/RELEASE_HISTORY.md) | T | 1.0.1 | ACTIVE |
| KNOW-23 | [knowledge/templates/AI_NOTES.md](knowledge/templates/AI_NOTES.md) | T | 1.0.1 | ACTIVE |
| KNOW-24 | [knowledge/templates/SESSION_LOG.md](knowledge/templates/SESSION_LOG.md) | T | 1.0.0 | ACTIVE |
| KNOW-25 | [knowledge/templates/HANDOVER.md](knowledge/templates/HANDOVER.md) | T | 1.0.0 | ACTIVE |
| AGNT-01 | [agents/AGENT_SYSTEM.md](agents/AGENT_SYSTEM.md) | S | 1.0.3 | ACTIVE |
| AGNT-02 | [agents/ROLE_TEMPLATE.md](agents/ROLE_TEMPLATE.md) | S | 1.1.0 | ACTIVE |
| AGNT-03 | [agents/roles/ORCHESTRATOR.md](agents/roles/ORCHESTRATOR.md) | S | 1.0.0 | ACTIVE |
| AGNT-04 | [agents/roles/PRODUCT_ANALYST.md](agents/roles/PRODUCT_ANALYST.md) | S | 1.0.1 | ACTIVE |
| AGNT-05 | [agents/roles/ARCHITECT.md](agents/roles/ARCHITECT.md) | S | 1.0.0 | ACTIVE |
| AGNT-06 | [agents/roles/ENGINEER.md](agents/roles/ENGINEER.md) | S | 1.0.1 | ACTIVE |
| AGNT-07 | [agents/roles/REVIEWER.md](agents/roles/REVIEWER.md) | S | 1.0.1 | ACTIVE |
| AGNT-08 | [agents/roles/QA_ENGINEER.md](agents/roles/QA_ENGINEER.md) | S | 1.0.1 | ACTIVE |
| AGNT-09 | [agents/roles/RELEASE_MANAGER.md](agents/roles/RELEASE_MANAGER.md) | S | 1.0.2 | ACTIVE |
| AGNT-10 | [agents/AGENT_LIBRARY.md](agents/AGENT_LIBRARY.md) | S | 1.0.0 | ACTIVE |
| COMM-01 | [communication/COMMUNICATION_PROTOCOL.md](communication/COMMUNICATION_PROTOCOL.md) | S | 1.0.1 | ACTIVE |
| COMM-02 | [communication/MESSAGE_TYPES.md](communication/MESSAGE_TYPES.md) | S | 1.0.1 | ACTIVE |
| QUAL-01 | [quality/QUALITY_SYSTEM.md](quality/QUALITY_SYSTEM.md) | S | 1.0.1 | ACTIVE |
| QUAL-02 | [quality/QUALITY_GATES.md](quality/QUALITY_GATES.md) | S | 1.0.1 | ACTIVE |
| QUAL-03 | [quality/DEFINITION_OF_DONE.md](quality/DEFINITION_OF_DONE.md) | S | 1.0.0 | ACTIVE |
| QUAL-04 | [quality/REVIEW_STANDARDS.md](quality/REVIEW_STANDARDS.md) | S | 1.0.0 | ACTIVE |
| WFLW-01 | [workflows/WORKFLOW_INDEX.md](workflows/WORKFLOW_INDEX.md) | S | 1.0.0 | ACTIVE |
| WFLW-02 | [workflows/WF_NEW_PROJECT.md](workflows/WF_NEW_PROJECT.md) | S | 1.0.0 | ACTIVE |
| WFLW-03 | [workflows/WF_FEATURE.md](workflows/WF_FEATURE.md) | S | 1.0.0 | ACTIVE |
| WFLW-04 | [workflows/WF_BUGFIX.md](workflows/WF_BUGFIX.md) | S | 1.0.0 | ACTIVE |
| WFLW-05 | [workflows/WF_REFACTORING.md](workflows/WF_REFACTORING.md) | S | 1.0.0 | ACTIVE |
| WFLW-06 | [workflows/WF_ARCHITECTURE_REVIEW.md](workflows/WF_ARCHITECTURE_REVIEW.md) | S | 1.0.0 | ACTIVE |
| WFLW-07 | [workflows/WF_CODE_REVIEW.md](workflows/WF_CODE_REVIEW.md) | S | 1.0.0 | ACTIVE |
| WFLW-08 | [workflows/WF_RELEASE.md](workflows/WF_RELEASE.md) | S | 1.0.0 | ACTIVE |
| WFLW-09 | [workflows/WF_MAINTENANCE.md](workflows/WF_MAINTENANCE.md) | S | 1.0.0 | ACTIVE |
| WFLW-10 | [workflows/WF_RESEARCH.md](workflows/WF_RESEARCH.md) | S | 1.0.0 | ACTIVE |
| WFLW-11 | [workflows/WF_DOCUMENTATION.md](workflows/WF_DOCUMENTATION.md) | S | 1.0.0 | ACTIVE |
| WFLW-12 | [workflows/WF_RECOVERY.md](workflows/WF_RECOVERY.md) | S | 1.0.0 | ACTIVE |
| OPRN-01 | [operations/ADOPTION_GUIDE.md](operations/ADOPTION_GUIDE.md) | S | 1.0.0 | ACTIVE |
| OPRN-02 | [operations/PROFILES.md](operations/PROFILES.md) | S | 1.0.0 | ACTIVE |
| OPRN-03 | [operations/UPGRADE_GUIDE.md](operations/UPGRADE_GUIDE.md) | S | 1.0.0 | ACTIVE |
| OPRN-04 | [operations/EXTENDING_AMF.md](operations/EXTENDING_AMF.md) | S | 1.0.0 | ACTIVE |
| OPRN-05 | [operations/ARCHIVING.md](operations/ARCHIVING.md) | S | 1.0.0 | ACTIVE |
| OPRN-06 | [operations/PLAYBOOK_INDEX.md](operations/PLAYBOOK_INDEX.md) | S | 1.0.0 | ACTIVE |
| OPRN-07 | [operations/FRAMEWORK_AUDIT.md](operations/FRAMEWORK_AUDIT.md) | S | 1.0.0 | ACTIVE |
| OPRN-08 | [operations/CERTIFICATION.md](operations/CERTIFICATION.md) | S | 1.0.0 | ACTIVE |

## 5. Registry Maintenance

- **New document** → row added by its creating change (extension procedure or amendment), same session.
- **Version/status change** → row updated per R10.6, same session.
- **Never** does this registry lead: headers are the truth, the registry mirrors (Article III — the fact's home is the header; this is the index of homes).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 8 | Initial manifest: start-here paths, module map, full registry at release v1.0.0 |
| 1.0.1 | 2026-07-12 | Architect (AI), Phases 6-7 (user briefs) | Registered SCHEMA_REGISTRY (ROOT-04) and AGENT_LIBRARY (AGNT-10); schema pointer added |
| 1.0.2 | 2026-07-13 | Architect (AI), Phases 8-10 | Registered PLAYBOOK_INDEX, FRAMEWORK_AUDIT, CERTIFICATION (OPRN-06..08); C0 status; situation path |

## Future Extension Notes

If the registry outgrows comfortable diffing (~150 rows), split per-module registry files with this section as their index — structure-only change (D2).
