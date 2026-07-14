# AMF Overview

| Field | Value |
|---|---|
| ID | CORE-01 |
| Document | AMF_OVERVIEW.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.0.5 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Canonical statement of AMF's identity, mission and scope. Subordinate to [AI_CONSTITUTION.md](AI_CONSTITUTION.md); design rationale authority remains with [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md). |

---

## Document Contract

**Purpose.** State what AMF is, why it exists, the philosophy behind it, and how its parts fit — the orientation document for any newcomer, human or AI.

**Scope.** Identity, mission, model, module map, non-goals, navigation. Not rules ([AI_CONSTITUTION.md](AI_CONSTITUTION.md), [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md)), not judgment ([FRAMEWORK_PRINCIPLES.md](FRAMEWORK_PRINCIPLES.md)), not design rationale ([../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md)).

**Responsibilities.** The identity narrative; the layered model as orientation; the module map; the non-goals; framework navigation (now delegated to the Manifest — §7 points there).

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md), [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md).

**Consumers.** First document any human reads; early orientation for AI sessions working on the framework itself. (Project sessions orient through their instance, not through this document.)

**Related documents.** All core documents; [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md).

**Update policy.** Amendment process per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5 (class C). The module map updates as phases deliver (D1 registry-style edits).

---

## 1. What AMF Is

The **AI Multi-Agent Framework (AMF)** is an engineering operating system for AI-driven software development. It converts a general-purpose AI coding agent into a structured engineering organization: specialized roles with explicit authority, a persistent per-project memory that survives session boundaries, standardized communication, objective quality gates, and versioned governance.

AMF is two artifacts in fixed relation:

- **The Framework** — this repository. Versioned, technology-agnostic, read-only during project work. It defines how AI agents think, decide, communicate, document, review and evolve software.
- **The Instance** — a `.amf/` directory inside each project. That project's living memory: configuration, knowledge documents, session records. Created from framework templates at adoption; owned by the project.

One framework, many instances. Upgrading the framework never means editing projects by hand beyond the published migration path.

## 2. Why AMF Exists

Unstructured AI assistance fails long-running projects in seven predictable ways (catalogued as F1–F7 in [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §2.1): decisions get re-litigated, context evaporates between sessions, architecture drifts, roles blur, documentation diverges from reality, quality varies with phrasing, and process crushes small projects.

AMF's mission is to make AI-driven software projects **predictable, maintainable, scalable and repeatable** by closing those failure modes structurally — with documents, ownership and procedure, not with hope. The test of every AMF component is that a completely cold AI session can pick up any AMF project and continue it competently by reading a bounded set of files.

## 3. The Model

Three layers, strict authority order ([AI_CONSTITUTION.md](AI_CONSTITUTION.md) Articles I–II):

```text
HUMAN OWNER      absolute authority; decides D3; approves releases and amendments
      ↓ directs / approves / overrides
FRAMEWORK        seven modules of rules, roles, standards and procedures (this repo)
      ↓ instantiates / governs
INSTANCE         one per project: config, living knowledge, session records
```

Work happens in **sessions** — atomic units that begin by reconstructing context from the instance and end by handing over to an unknown successor ([SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md)). Agents act through **roles** with contracts. Decisions carry **classes** (D1/D2/D3) proportional to blast radius. Work passes **gates** (G0–G6) that are binary and objective. Projects adopt at a **profile** (Minimal/Standard/Full) so process weight matches project weight.

## 4. Philosophy in Brief

Three documents carry the full philosophy; this is the shape of it:

- The **Constitution** constrains: thirteen non-negotiable articles, from Human Primacy to Professional Engineering Mindset.
- The **Principles** guide judgment where rules end: single responsibility, low coupling, documentation-driven, AI-first yet human-readable, scaling down as deliberately as up, no speculation.
- The **Rules** fix conventions: names, IDs, metadata, statuses, references — exceptionless, and by design machine-checkable.

The recurring theme: **explicit beats implicit, structure beats memory, evidence beats speculation.**

## 5. The Seven Modules

| Module | Responsibility | Status |
|---|---|---|
| `core/` | Identity, constitution, governance, principles, rules, glossary, sessions, versioning | ACTIVE (Phase 1) |
| `knowledge/` | Per-project memory: instance document standards, reading tiers, update matrix | ACTIVE (Phase 2) |
| `agents/` | The organization: seven role contracts, hierarchy, escalation, decision classes in operation | ACTIVE (Phase 3) |
| `communication/` | Message envelope and the ten message types | ACTIVE (Phase 4) |
| `quality/` | Gates G0–G6, Definition of Done, review standards | ACTIVE (Phase 5) |
| `workflows/` | Eleven executable session procedures + selection rules | ACTIVE (Phase 6) |
| `operations/` | Adoption, profiles, upgrades, extension, archiving, playbooks, audit, certification | ACTIVE (Phases 7–10) |

Plus the root **[Manifest](../AMF_MANIFEST.md)**: single entry point and document registry. Dependencies run strictly downward through this list ([../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §8).

## 6. What AMF Is Not

- **Not a prompt library.** Roles are contracts with authority and ownership, not phrasing.
- **Not a project template.** Instances hold knowledge; project scaffolding is the project's business.
- **Not tooling.** v1.0 is conventions and procedure; its conventions are machine-checkable so tooling can come later without redesign.
- **Not a runtime.** AMF governs what and why; the hosting runtime (Claude Code in v1.0) governs how. The binding is a thin, replaceable adapter ([ADOPTION_GUIDE.md §3](../operations/ADOPTION_GUIDE.md)).
- **Not bureaucracy for its own sake.** Every component exists to close a named failure mode; profiles shrink the surface for small projects. A component that stops earning its place is deprecated (P9).

## 7. Navigating AMF

The [Manifest](../AMF_MANIFEST.md) is the entry point; orientation paths:

- **New human reader:** this document → [AI_CONSTITUTION.md](AI_CONSTITUTION.md) → [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md) → skim the module specs as they exist.
- **AI session working on the framework:** [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) (the design contract) → the phase brief being executed → the documents that phase depends on (§15 writing order).
- **AI session working on a project:** never starts here — it starts at the project's bootstrap (CLAUDE.md → INSTANCE.md) per [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md) Stage 1.
- **Any terminology doubt:** [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md), always.

## 8. Composition and Status

AMF v1.0 comprises 66 normative documents across the seven modules plus root (inventory: [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §7), built in eight phases (§16 there). Current position: **all phases complete — AMF v1.0.0 released** (gate G6, Human Owner approval). All seven modules, the Manifest and the Schema Registry are ACTIVE; certification status C0 — Audited ([CERTIFICATION.md](../operations/CERTIFICATION.md)).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial identity document |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 2 | Module map: knowledge ACTIVE; position updated (D1 registry edits) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 3 | Module map: agents ACTIVE; position updated (D1 registry edits) |
| 1.0.3 | 2026-07-12 | Architect (AI), Phase 4-5 | Module map: communication and quality ACTIVE (D1 registry edits) |
| 1.0.4 | 2026-07-12 | Architect (AI), Phase 8 | Module map complete; v1.0.0 release recorded; swept Phase 6-8 references (R8.3) |
| 1.0.5 | 2026-07-13 | Architect (AI), Phases 8-10 | Operations module completed through Phase 10; certification status recorded |

## Future Extension Notes

- §5 and §8 now track releases, not phases; §7's deep navigation is the Manifest's (done).
- If AMF is ever published for third-party adopters, this document gains an audience section (who AMF serves) — additive.
