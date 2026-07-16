# Framework Governance

| Field | Value |
|---|---|
| ID | CORE-03 |
| Document | FRAMEWORK_GOVERNANCE.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.0.6 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Governs how AMF itself changes: who owns what, who approves what, and how documents live and die. Subordinate to [AI_CONSTITUTION.md](AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Define how AMF governs and evolves itself: the governance model, decision hierarchy for framework matters, ownership model, document lifecycle authority, the amendment process, and the change approval matrix.

**Scope.** The framework as a product. Does not govern project-level decisions (that is the agent system's application of decision classes — [AGENT_SYSTEM.md §3](../agents/AGENT_SYSTEM.md)) and does not define version *semantics* ([VERSIONING.md](VERSIONING.md)) or status *vocabulary* ([FRAMEWORK_RULES.md](FRAMEWORK_RULES.md)).

**Responsibilities.** Governance model; framework change classification; ownership model and ownership registry; lifecycle transition authority; amendment process; approval matrix; extension-vs-amendment boundary.

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md) (Articles I, II, VI).

**Consumers.** Architect and Orchestrator routinely; every role when a change to the framework is contemplated; the Human Owner for approvals.

**Related documents.** [VERSIONING.md](VERSIONING.md), [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md), [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md), [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md).

**Update policy.** Amendment process (§5 of this document). Class C: Human Owner approval required for all substantive change.

---

## 1. Governance Model

AMF is governed by three forces in fixed relation:

1. **The Human Owner — sovereign.** Ultimate authority over the framework and every project under it. Approves amendments, releases, and all D3 matters. Not bound by the framework (Constitution, Article I).
2. **The Constitution — law.** Binds all AI behavior. Changes only through amendment (§5).
3. **Stewardship roles — administration.** The **Architect** role stewards the framework's technical content: drafts changes, guards consistency, approves what the matrix (§6) delegates to it. The **Orchestrator** role administers process: registries, session discipline, routing to the Owner. Stewards execute governance; they do not own it.

Design authority for v1.0 structure rests with the approved [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md); this document governs everything after that approval.

## 2. Framework Change Classification

Framework changes map onto the constitutional decision classes (Constitution, Article VI) as follows:

| Class | Framework meaning | Examples | Decides |
|---|---|---|---|
| D1 | Non-substantive: wording, typos, formatting, link repairs. No behavioral or structural meaning changes. | Fixing a broken cross-reference; clarifying a sentence without changing its norm | Maintainer of the document |
| D2 | Substantive but additive or contained: new optional documents, new checklist items, new workflows, template field additions with defaults, spec clarifications that change behavior | Adding WF_RESEARCH detail; new message type | Architect |
| D3 | Structural or constitutional: anything touching the Constitution, authority hierarchy, decision classes, gate identities, lifecycle classes, instance directory contract, the seven roles' identities, or any MAJOR version change | Amending an article; renaming a role; changing `.amf/` layout | Human Owner |

Ambiguity resolves upward (Constitution §3). A D1 that turns out to change meaning is a violation of Article V and is remediated as a D2.

## 3. Ownership Model

**Owner** — accountable for a document's content being true, complete and consistent with its purpose. Content authority: approves substantive changes at its delegation level.
**Maintainer** — executes edits, keeps metadata, revision history and cross-references correct. May apply D1 changes without the Owner.

Rules:

- Every document has exactly one Owner and exactly one Maintainer (they may coincide). Orphan documents are forbidden; discovering one is a defect routed to the Architect.
- Ownership follows the module ownership defined in the architecture (§5): content ownership of module documents belongs to the module's owning role; all class C documents are owned by the Human Owner with the Architect as Maintainer.
- Ownership transfer is a D2 recorded in the receiving document's revision history.

**Ownership registry (by module):**

| Documents | Owner | Maintainer |
|---|---|---|
| AMF_ARCHITECTURE.md, core/* (8) | Human Owner | Architect |
| knowledge/* (25 documents) | Architect | Architect |
| agents/* (9 documents) | Architect | Architect |
| communication/* (2 documents) | Architect | Architect |
| quality/* (4 documents) | QA Engineer (content), Architect (model) | Architect |
| workflows/* (12 documents) | Orchestrator (content), Architect (structure) | Orchestrator |
| operations/* (8 documents) | Release Manager (content), Architect (profiles/audit) | Release Manager |
| AMF_MANIFEST.md, README.md, QUICK_START.md, CHANGELOG.md | Orchestrator / Human Owner | Orchestrator |
| SCHEMA_REGISTRY.md | Architect | Architect |

The authoritative document registry lives in [AMF_MANIFEST.md](../AMF_MANIFEST.md); this table is its ownership view.

## 4. Document Lifecycle Authority

Status vocabulary and transition mechanics are defined in [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §7. Governance assigns *who authorizes* each transition:

| Transition | Authorized by |
|---|---|
| (new) → DRAFT | Document Owner (creation per phase plan or extension procedure) |
| DRAFT → ACTIVE | Class C: Human Owner. Class S/T: Architect, against the owning phase's exit criteria or EXTENDING_AMF.md |
| ACTIVE → DEPRECATED | Same authority as activation; replacement must be named at deprecation time ([VERSIONING.md](VERSIONING.md) §5) |
| DEPRECATED → ARCHIVED | Architect, after the grace period in [VERSIONING.md](VERSIONING.md) §5 |
| DRAFT → ARCHIVED (abandoned) | Document Owner |

No other transitions exist. In particular, ARCHIVED is terminal and DEPRECATED never returns to ACTIVE (a revived need produces a new document).

## 5. Amendment Process

Required for every D3 framework change (§2). Six steps, none skippable:

1. **Proposal.** A Proposal message ([MESSAGE_TYPES.md §2.9](../communication/MESSAGE_TYPES.md)) stating: the change, the problem it solves, and why no extension point suffices.
2. **Impact analysis.** The Architect analyzes effects across all modules and instances: which documents change, which instance migrations are required, what breaks. Recorded with the proposal.
3. **Owner decision.** The Human Owner approves, rejects, or returns for revision. Recorded as a Decision Record.
4. **Execution.** The Architect applies the change; every touched document gets a version bump and revision-history entry per [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §10.
5. **Versioning.** Framework version bumped per [VERSIONING.md](VERSIONING.md); migration notes written ([UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md)).
6. **Registry.** Manifest registry updated ([AMF_MANIFEST.md](../AMF_MANIFEST.md)), plus this document's §3 ownership table.

Repealed constitutional articles are marked repealed in place — numbering is stable (see AI_CONSTITUTION.md, Future Extension Notes).

## 6. Change Approval Matrix

| Change | Class | Approver | Version effect ([VERSIONING.md](VERSIONING.md)) |
|---|---|---|---|
| Typo/wording/link fix | D1 | Maintainer | PATCH (doc) |
| Clarification changing behavior | D2 | Architect | MINOR (doc) |
| New optional document / workflow / message type / checklist item / profile | D2 | Architect | MINOR (framework) |
| New role or knowledge domain | D2 | Architect, Owner informed | MINOR (framework) |
| Template structure change (breaking instances) | D3 | Human Owner | MAJOR (framework) |
| Constitution, authority hierarchy, decision classes, gate identities, lifecycle classes, instance layout, role identities | D3 | Human Owner | MAJOR (framework), or MINOR if strictly additive |
| Framework release (any) | D3 | Human Owner (gate G6) | Tag per release |

## 7. Extension vs Amendment Boundary

Growth uses **extension points** and needs no amendment: new roles, workflows, knowledge domains, message types, quality checklist annexes, profiles (procedure: [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md)). Everything on the D3 row set of §6 is **amendment territory**. The test: *does the change alter anything existing, or only add alongside it?* Additions extend; alterations amend.

## 8. Compatibility Policy

Governance guarantees the process side of compatibility: no D3 change ships without impact analysis (§5.2) and a migration path; deprecations always name replacements and honor the grace period. The substance of the compatibility promise (what stays stable across v1.x) is owned by [VERSIONING.md](VERSIONING.md) §6.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial governance model, ownership registry, amendment process, approval matrix |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 2 | Ownership registry: knowledge module delivered (D1 registry edit) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 3 | Registry: agents module delivered; swept Phase 3 reference (R8.3) |
| 1.0.3 | 2026-07-12 | Architect (AI), Phase 4-5 | Registry: communication and quality delivered; swept references (R8.3) |
| 1.0.4 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |
| 1.0.5 | 2026-07-13 | Architect (AI), Phases 8-10 | Registry: operations grew to 8 documents (playbooks, audit, certification) |
| 1.0.6 | 2026-07-16 | Architect (AI), v1.1.0 | Registry: root docs grew (QUICK_START, CHANGELOG, SCHEMA_REGISTRY) |

## Future Extension Notes

- The registry's authoritative copy lives in AMF_MANIFEST.md (Phase 8, done).
- If AMF gains multiple human stakeholders, §1 needs a delegation model (Owner delegating approval scopes); designed as an additive section, not a rewrite.
- Tooling (v2 direction, architecture §14.2) may automate §5.4/§5.6 execution steps; the approval steps remain human/role decisions.
