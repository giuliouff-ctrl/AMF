# Framework Glossary

| Field | Value |
|---|---|
| ID | CORE-06 |
| Document | FRAMEWORK_GLOSSARY.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.6.0 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Canonical vocabulary of AMF. Every definition here is the official one; other documents may elaborate within their scope but never contradict. Subordinate to [AI_CONSTITUTION.md](AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Give every important AMF concept exactly one official definition, eliminating ambiguous terminology across the framework and all instances.

**Scope.** Framework terminology. Project-domain terms (a project's own business vocabulary) belong in that project's instance, not here.

**Responsibilities.** The term registry; the terminology rules.

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md) (concepts it defines are summarized, not redefined, here).

**Consumers.** Every role; every phase; any human reader. First stop for any terminology doubt.

**Related documents.** Each entry points to the document that owns the concept's full semantics.

**Update policy.** New entries are D2 (Architect) per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §6; changing an existing definition's meaning is D3 (amendment). Per [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) R1.4, a new term may not be used anywhere before its entry exists here.

---

## 1. Terminology Rules

- **One term per concept, one concept per term.** Synonyms are forbidden in normative text: it is always *task* (never ticket, todo), *issue* (never bug report as a noun for the record; "Bug Report" names the message type), *handover* (never handoff), *ledger* / *snapshot* per their definitions below.
- **Definitions here are one to three sentences.** Full semantics live in the owning document, linked from the entry.
- **Capitalization.** Role names, message types, gate IDs, decision classes and lifecycle stages are capitalized as defined (Architect, Decision Record, G3, D2, HANDOVER). Ordinary uses of the same English words are not.

## 2. Terms

**Agent** — An AI actor operating under AMF, always through a Role. In single-instance topology, one agent assumes roles sequentially; in multi-instance topology, agents run in parallel. Owner of full semantics: [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md).

**Amendment** — The governed procedure for changing constitutional-class content. See [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5.

**Architecture** — (of a project) The system design of that project, owned by its instance's ARCHITECTURE.md; (of AMF) the design of the framework itself, fixed in [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md).

**Archive** — Tier-3 storage for historical material (`archive/` in an instance; ARCHIVED status for documents). Archived content is preserved and excluded from default reading. See [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §7, [KNOWLEDGE_SYSTEM.md §7](../knowledge/KNOWLEDGE_SYSTEM.md).

**Authority** — The right to decide or to bind behavior, always held by a level of the hierarchy in [AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article II. Every document's header states its authority in one sentence.

**Backlog** — The instance's prioritized record of future work not yet active. Owned by the Product Analyst role via BACKLOG.md (standard: [templates/BACKLOG.md](../knowledge/templates/BACKLOG.md)).

**Class** — See *Lifecycle Class* and *Decision Class*. Unqualified "class" is avoided in normative text.

**Certification Level** — The honest field-validation status of a framework version (C0 Audited → C3 Hardened), never claimed above its evidence. Owner: [CERTIFICATION.md](../operations/CERTIFICATION.md).

**Consumer** — A role or document that reads and depends on a document, as declared in its Document Contract.

**Context Budget** — The bounded amount of reading a session performs to reconstruct context: T0 plus the active workflow's T1 list. See *Reading Tier*; owner: [CONTEXT_RECONSTRUCTION.md](../knowledge/CONTEXT_RECONSTRUCTION.md).

**Context Reconstruction** — Stage 2 of the session lifecycle: rebuilding working knowledge of a project from its instance documents alone. See [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md) §2.

**Decision** — A committed choice among alternatives. Every decision has exactly one owner and one Decision Class ([AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article VI).

**Decision Class** — The blast-radius classification of a decision: **D1** (local, reversible — acting role decides), **D2** (structural — Architect decides, record mandatory), **D3** (strategic/irreversible — Human Owner decides). Defined in [AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article VI.

**Decision Record** — The persistent record of a D2/D3 decision: context, options, choice, rationale, consequences. Lives in the instance's DECISIONS.md ledger; message form identical to the ledger entry per [MESSAGE_TYPES.md §2.5](../communication/MESSAGE_TYPES.md).

**Definition of Done** — The per-work-type floor under every completion claim (feature, fix, refactor, documentation), owned by [DEFINITION_OF_DONE.md](../quality/DEFINITION_OF_DONE.md). Acceptance criteria say what *this* work must do; the DoD says what *all* work of its kind must be.

**Dependency** — (between documents) A normative reliance, always pointing same-level-or-downward in the layer graph ([../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §8); (of a project) an external component the project relies on, recorded in DEPENDENCIES.md (standard: [templates/DEPENDENCIES.md](../knowledge/templates/DEPENDENCIES.md)).

**Document Contract** — The mandatory section stating a framework document's purpose, scope, responsibilities, dependencies, consumers, related documents and update policy. See [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §6.

**Envelope** — The fixed field set every message carries (type, id, session, from, to, subject, refs, status, body), frozen for 1.x. Owner: [COMMUNICATION_PROTOCOL.md §2](../communication/COMMUNICATION_PROTOCOL.md).

**Escalation** — Routing a matter to a higher authority (role → Orchestrator → Human Owner) because it exceeds the current holder's authority or resolution failed. Mandatory triggers in [AGENT_SYSTEM.md §5](../agents/AGENT_SYSTEM.md); message type per [MESSAGE_TYPES.md §2.6](../communication/MESSAGE_TYPES.md).

**Extension Point** — A designed place where AMF grows additively without amendment: new roles, workflows, knowledge domains, message types, profiles. See [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §7.

**Folding Map** — The per-profile table stating where every folded document's content lives, so no knowledge category is ever unsupported. Owner: [PROFILES.md §2](../operations/PROFILES.md).

**Framework** — AMF itself: the versioned, read-only-during-project-work body of rules, roles, workflows and standards. Contrast *Instance*.

**Gate** (Quality Gate) — A binary, objective checkpoint (G0–G6) that work must pass to proceed. Identities fixed in [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §12; checklists owned by [QUALITY_GATES.md](../quality/QUALITY_GATES.md).

**Handover** — The mandatory closing artifact of every session: state of work, next actions, warnings — sufficient for a cold successor session to resume (the "stranger test"). See [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md) §2 Stage 7.

**Human Owner** — The human holding absolute authority over the framework and every project ([AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article I). Decides D3, approves releases and amendments.

**Instance** — A project's `.amf/` directory: its configuration (INSTANCE.md), living knowledge, and session records — instantiated from framework templates at adoption. Contrast *Framework*.

**Issue** — A recorded defect or limitation (I-NNN) in the instance's KNOWN_ISSUES.md (standard: [templates/KNOWN_ISSUES.md](../knowledge/templates/KNOWN_ISSUES.md)).

**Knowledge Domain** — A category of project knowledge (business, architecture, planning, risk…) with exactly one owning role. Map owned by [KNOWLEDGE_SYSTEM.md §3](../knowledge/KNOWLEDGE_SYSTEM.md).

**Knowledge System** — The complete per-project memory: the instance documents, their ownership, update rules and reading structure. The framework's answer to session-boundary context loss. Owner: [KNOWLEDGE_SYSTEM.md](../knowledge/KNOWLEDGE_SYSTEM.md).

**Ledger** — An append-only instance document (class A): history is only ever added, never rewritten ([AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article VII). Examples: DECISIONS.md, SESSION_LOG.md, CHANGELOG.md. Contrast *Snapshot*.

**Lesson** — A recorded retrospective insight (L-NNN) in the instance's LESSONS_LEARNED.md ledger (standard: [templates/LESSONS_LEARNED.md](../knowledge/templates/LESSONS_LEARNED.md)), captured so failures and successes inform future sessions and framework versions.

**Lifecycle Class** — One of five change-policy classes a document belongs to: **C** (constitutional), **S** (stable spec), **T** (template/canonical standard), **I** (instance snapshot), **A** (instance ledger). Defined in [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §7.1.

**Maintainer** — The role that executes edits on a document and keeps its metadata, history and links correct. Contrast *Owner (of a document)*. See [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §3.

**Manifest** — [AMF_MANIFEST.md](../AMF_MANIFEST.md): the single entry point and document registry of the framework.

**Message** — A structured exchange between roles (or with the Owner) following the communication envelope; ten types (Task Request, Status Report, Review Report, Decision Request, Decision Record, Escalation, Bug Report, Risk Report, Proposal, Approval). Owner: [COMMUNICATION_PROTOCOL.md](../communication/COMMUNICATION_PROTOCOL.md) and [MESSAGE_TYPES.md](../communication/MESSAGE_TYPES.md).

**Milestone** — A named, dated target on a project's roadmap, owned by ROADMAP.md (standard: [templates/ROADMAP.md](../knowledge/templates/ROADMAP.md)).

**Module** — One of the seven top-level units of the framework (core, knowledge, agents, communication, quality, workflows, operations), each with a single responsibility and explicit dependencies.

**Open Question** — A recorded unresolved question (Q-NNN) that blocks or shapes work, tracked in OPEN_QUESTIONS.md (standard: [templates/OPEN_QUESTIONS.md](../knowledge/templates/OPEN_QUESTIONS.md)) until answered; unresolved escalations land here before handover.

**Owner (of a document/domain)** — The role accountable for content being true, complete and purpose-consistent; approves substantive changes at its delegation level. See [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §3. Not to be confused with the *Human Owner*.

**Playbook** — The executing procedure for an operational situation; in AMF, workflows/guides *are* the playbooks, mapped one lookup away in [PLAYBOOK_INDEX.md](../operations/PLAYBOOK_INDEX.md).

**Profile** — An adoption size (Minimal, Standard, Full) that subsets active instance documents, collapsed roles and gate merging — without ever dropping a knowledge category. Owner: [PROFILES.md](../operations/PROFILES.md).

**Project** — A software effort managed under AMF: source tree plus instance.

**Reading List** — The T1 document list a workflow declares for context reconstruction; defined per workflow, and only there, in [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md).

**Reading Tier** — The priority level of a document for session reading: **T0** (always), **T1** (per active workflow), **T2** (on demand), **T3** (archive, never by default). Owner: [CONTEXT_RECONSTRUCTION.md §1](../knowledge/CONTEXT_RECONSTRUCTION.md).

**Recovery** — The mandatory reconciliation a session performs when its predecessor was interrupted. Contract in [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md) §5; procedure in [WF_RECOVERY.md](../workflows/WF_RECOVERY.md).

**Review** — Gate-checking work against a written standard by a role that did not produce it ([AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article IX).

**Review Report** — The Reviewer's binary-verdict artifact (PASS / PASS_WITH_NOTES / FAIL with findings). Message type per [MESSAGE_TYPES.md §2.3](../communication/MESSAGE_TYPES.md); standards in [REVIEW_STANDARDS.md](../quality/REVIEW_STANDARDS.md).

**Risk** — A recorded uncertain event with project impact (R-NNN), tracked with likelihood and mitigation in RISK_REGISTER.md (standard: [templates/RISK_REGISTER.md](../knowledge/templates/RISK_REGISTER.md)).

**Role** — A contract an agent assumes: identity, ownership, authority, prohibitions, escalation duties. The seven v1.0 roles: Orchestrator, Product Analyst, Architect, Engineer, Reviewer, QA Engineer, Release Manager. Owner: [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md) and the contracts in `agents/roles/`.

**Role Assumption** — The explicit, logged act of taking on a role's authority in single-instance topology (`as <Role>: <what for>`); protocol in [AGENT_SYSTEM.md §2.2](../agents/AGENT_SYSTEM.md).

**Runtime** — The execution environment hosting AMF agents (Claude Code in v1.0). The binding between AMF and a runtime is a *runtime adapter*, described in [ADOPTION_GUIDE.md §3](../operations/ADOPTION_GUIDE.md).

**Session** — One continuous engagement from INITIALIZE to HANDOVER; AMF's atomic unit of work and accountability. Owner: [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md).

**Session Log** — The instance's append-only ledger of sessions (SESSION_LOG.md): one entry per session, opened at INITIALIZE, closed at HANDOVER.

**Single Source of Truth** — The constitutional rule that every fact has exactly one owning document, referenced everywhere else ([AI_CONSTITUTION.md](AI_CONSTITUTION.md) Article III).

**Snapshot** — An instance document (class I) that always describes the present and is freely rewritten, because ledgers preserve what it supersedes. Examples: CURRENT_STATUS.md, TASKS.md. Contrast *Ledger*.

**Specialization** — An expertise lens on a role (`Engineer[frontend]`, `Architect[security]`): changes posture, never authority or ownership. Mechanism: [AGENT_LIBRARY.md §3](../agents/AGENT_LIBRARY.md).

**Status** — A document's lifecycle state: DRAFT, ACTIVE, DEPRECATED, ARCHIVED. Vocabulary and transitions in [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §7.

**Task** — A unit of tracked work (T-NNN) in the instance's TASKS.md snapshot.

**Technical Debt** — A deliberate, recorded compromise to be repaid, tracked in TECHNICAL_DEBT.md (standard: [templates/TECHNICAL_DEBT.md](../knowledge/templates/TECHNICAL_DEBT.md)) with the intent behind it.

**Topology** — How roles are executed by the runtime: single-instance (one agent, sequential role assumption — default) or multi-instance (parallel subagents). Framework semantics are identical in both ([../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) AD-4).

**Update Trigger** — The catalogued event (E-code) that obliges specific document updates by a specific role, per [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md).

**Workflow** — An executable end-to-end procedure for one session type, composing roles, messages, knowledge updates and gates. Owner: [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md) and the WF_* procedures.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial registry: 53 terms + terminology rules |
| 1.1.0 | 2026-07-12 | Architect (AI), Phase 2 | Added Reading List, Update Trigger (55 terms); swept Phase 2 forward references to live links (R8.3) |
| 1.2.0 | 2026-07-12 | Architect (AI), Phase 3 | Added Role Assumption (56 terms); swept Phase 3 forward references (R8.3) |
| 1.3.0 | 2026-07-12 | Architect (AI), Phase 4-5 | Added Definition of Done, Envelope (58 terms); swept Phase 4-5 references (R8.3) |
| 1.4.0 | 2026-07-12 | Architect (AI), Phase 8 | Added Folding Map (59 terms); swept Phase 6-8 references (R8.3) |
| 1.5.0 | 2026-07-12 | Architect (AI), Phase 7 (Agent Library) | Added Specialization (60 terms) |
| 1.6.0 | 2026-07-13 | Architect (AI), Phases 8-10 | Added Playbook, Certification Level (62 terms) |

## Future Extension Notes

- All planned v1.0 terms are registered; future additions follow the D2 path per Update policy.
- If the registry exceeds comfortable single-file navigation (~120 terms), split alphabetically — a structure change requiring only Manifest registry updates (MINOR).
