# AMF Quick Start

| Field | Value |
|---|---|
| ID | ROOT-05 |
| Document | QUICK_START.md |
| Module | root |
| Class | S — Stable spec (operator reference) |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Orchestrator |
| Maintainer | Orchestrator |
| Authority | Operator cheat sheet. Non-normative: every rule shown here is owned and stated in full elsewhere, linked inline. When this page and a linked document disagree, the linked document wins. |

---

## Document Contract

**Purpose.** Fit the whole operating loop on one screen: what an agent actually *does* each session, the four decisions it makes constantly, and where to look when unsure — so daily use needs no re-reading of the full framework.
**Scope.** A condensed pointer map for operators (human or AI). Owns no rules; contradicts none.
**Responsibilities.** The session loop at a glance; the constant decisions; the "where do I look" table; the daily-maintenance note.
**Dependencies.** Everything it links; authoritative sources always win over this summary (Article II).
**Consumers.** Any agent mid-work; a human learning AMF fast.
**Related documents.** [AMF_MANIFEST.md](AMF_MANIFEST.md) (full registry), [core/SESSION_MANAGEMENT.md](core/SESSION_MANAGEMENT.md), [operations/PLAYBOOK_INDEX.md](operations/PLAYBOOK_INDEX.md).
**Update policy.** D1 (Maintainer) for pointer upkeep; it tracks the framework, never leads it.

---

## 1. The Session Loop (memorize this)

Seven stages, every session, in order — full contract: [core/SESSION_MANAGEMENT.md §2](core/SESSION_MANAGEMENT.md).

```text
1 INITIALIZE  session ID · read CLAUDE.md → .amf/INSTANCE.md ·
              CHECK: last session log entry closed? if not → WF_RECOVERY first ·
              pick the workflow (§3)
2 RECONSTRUCT read T0 (INSTANCE → CURRENT_STATUS → latest handover),
              then the workflow's reading list · log deviations
3 PLAN        tasks · roles · gates · expected doc updates ·
              FLAG every D3 to the Owner NOW, before work
4 EXECUTE     work under role contracts · decisions logged by class (§2) ·
              record ledger events as they happen
5 REVIEW      pass the gates · reviewer ≠ author, always (§4)
6 DOCUMENT    apply UPDATE_MATRIX for every event · refresh CURRENT_STATUS
7 HANDOVER    close the log entry · write the handover ·
              stranger test: could a cold session resume from it alone?
```

No handover = the session was **interrupted**; the next one starts with recovery. The three outputs every session produces no matter what: session-log entry, handover, refreshed CURRENT_STATUS.

## 2. The Four Decisions You Make Constantly

- **What class is this decision?** — D1 reversible & yours → decide + log · D2 architecture/interfaces/deps/cross-boundary → Architect + Decision Record · D3 irreversible/costly/external/scope → **Human Owner**. Unclear → higher class. ([AI_CONSTITUTION.md Art. VI](core/AI_CONSTITUTION.md), classifier: [AGENT_SYSTEM.md §3.1](agents/AGENT_SYSTEM.md))
- **Does this fact have a home?** — one owning document, reference everywhere else, never copy. ([Art. III](core/AI_CONSTITUTION.md))
- **Did I record it?** — every change traces to the session; ledger events written when they happen (Decisions, Issues, Risks…). ([Art. V](core/AI_CONSTITUTION.md) · [UPDATE_MATRIX.md](knowledge/UPDATE_MATRIX.md))
- **Is this gate really passed?** — binary, evidenced, and checked by someone who didn't author it. "Mostly" doesn't exist. ([Art. IX/X](core/AI_CONSTITUTION.md) · [QUALITY_GATES.md](quality/QUALITY_GATES.md))

## 3. Which Workflow? (first match wins)

Unclosed predecessor → **RECOVERY** · no `.amf/` → **NEW_PROJECT** · shipping → **RELEASE** · something broke → **BUGFIX** · new capability → **FEATURE** · structure w/o behavior change → **REFACTORING** · deps/upkeep/upgrade → **MAINTENANCE** · a question → **RESEARCH** · audit the design → **ARCHITECTURE_REVIEW** · review as the goal → **CODE_REVIEW** · fix the docs → **DOCUMENTATION**. Full rules + any operational situation: [workflows/WORKFLOW_INDEX.md §3](workflows/WORKFLOW_INDEX.md) · [operations/PLAYBOOK_INDEX.md](operations/PLAYBOOK_INDEX.md).

## 4. The Seven Roles (who owns what)

| Role | Owns | Gate |
|---|---|---|
| Orchestrator | sessions, tasks, status, risks, questions, handovers | (routes) |
| Product Analyst | project, backlog, roadmap, assumptions, Owner input | G0 |
| Architect | architecture, decisions, debt, research · **all D2** | G1 (authors) |
| Engineer | the code, dependencies | G2 (self+evidence) |
| Reviewer | review verdicts (no domain — independence) | G1/G3 (checks) |
| QA Engineer | known issues, verification | G4 |
| Release Manager | changelog, release history | G5 · G6 (Owner approves) |

Assume a role explicitly and log it (`as <Role>: <what for>`). Titles beyond these seven map here — [agents/AGENT_LIBRARY.md](agents/AGENT_LIBRARY.md).

## 5. Where Do I Look?

| Question | Go to |
|---|---|
| What's the rule? | [core/AI_CONSTITUTION.md](core/AI_CONSTITUTION.md) (must/never) · [core/FRAMEWORK_RULES.md](core/FRAMEWORK_RULES.md) (conventions) |
| What does this term mean? | [core/FRAMEWORK_GLOSSARY.md](core/FRAMEWORK_GLOSSARY.md) |
| Which documents do I read now? | [knowledge/CONTEXT_RECONSTRUCTION.md](knowledge/CONTEXT_RECONSTRUCTION.md) |
| When do I update what? | [knowledge/UPDATE_MATRIX.md](knowledge/UPDATE_MATRIX.md) |
| What must be true to pass gate N? | [quality/QUALITY_GATES.md](quality/QUALITY_GATES.md) |
| What's "done"? | [quality/DEFINITION_OF_DONE.md](quality/DEFINITION_OF_DONE.md) |
| How do I run situation X? | [operations/PLAYBOOK_INDEX.md](operations/PLAYBOOK_INDEX.md) |
| How do I adopt AMF into a project? | [operations/ADOPTION_GUIDE.md](operations/ADOPTION_GUIDE.md) |
| Is the framework still consistent? | `python3 tools/amf-lint.py` |

## 6. Daily Maintenance Note

Framework upkeep runs like any project: a [WF_MAINTENANCE](workflows/WF_MAINTENANCE.md) / [WF_DOCUMENTATION](workflows/WF_DOCUMENTATION.md) session. Start it by running the linter (`python3 tools/amf-lint.py`) — it executes the V1–V11 checks ([FRAMEWORK_AUDIT.md §2](operations/FRAMEWORK_AUDIT.md)) and tells you exactly what drifted. Fix, bump versions + revision rows, log the release in [CHANGELOG.md](CHANGELOG.md). No framework release ships red.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-16 | Orchestrator (AI), v1.1.0 | Initial operator cheat sheet |
| 1.0.1 | 2026-07-16 | Orchestrator (AI), v1.1.0 self-review | Linter check count V1–V10 -> V1–V11 |

## Future Extension Notes

Stays one screen forever. If it grows, the surplus belongs in the document it summarizes, not here.
