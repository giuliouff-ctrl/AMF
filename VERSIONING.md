# Versioning

| Field | Value |
|---|---|
| ID | CORE-08 |
| Document | VERSIONING.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Normative for version semantics of the framework, its documents, and instance pinning; for deprecation and migration policy; for the experimental track. Subordinate to [AI_CONSTITUTION.md](AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Define how AMF evolves as a product: what version numbers mean, how documents and the framework version together, how instances pin and upgrade, how components are deprecated and retired, and what stays compatible across releases.

**Scope.** The framework and its instances' relationship to framework versions. Not the versioning of project source code (each project's own concern, recorded in its instance) and not *who approves* changes ([FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §6).

**Responsibilities.** Version semantics (framework and document level); instance pinning; deprecation policy; migration policy; compatibility promise; experimental track; roadmap philosophy.

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md); [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) (approval authority).

**Consumers.** Architect (every framework change); Release Manager (releases); Orchestrator (instance upgrades); every role reading a `Version` field.

**Related documents.** [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §10 (update procedure), [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md), [ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md).

**Update policy.** Amendment process per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5 (class C).

---

## 1. Two Levels of Version

AMF versions at two levels, deliberately:

- **Framework version** — the product release (`AMF 1.0.0`). What instances pin. Tagged at release time by the Release Manager with Owner approval (gate G6).
- **Document version** — each document's own semver in its metadata header. What the update procedure bumps ([FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) R10.1).

Document versions move continuously between releases; the framework version aggregates them at release points. The mapping rule: any document MAJOR bump forces at least a framework MINOR; any change that breaks the instance contract (§6) forces a framework MAJOR — regardless of how small the edit.

## 2. Framework Version Semantics

`MAJOR.MINOR.PATCH`:

| Bump | Meaning | Requires |
|---|---|---|
| **MAJOR** | Breaking: instance structure, authority hierarchy, constitutional articles (non-additive), document contracts, role identities, gate identities, lifecycle classes | Migration path in [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md); Owner approval; impact analysis per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5 |
| **MINOR** | Additive: new workflows, roles, message types, knowledge domains, template fields with defaults, checklist items, profiles; behavior-clarifying spec changes | Architect approval per approval matrix; existing instances remain valid unchanged |
| **PATCH** | Corrections and clarifications with no behavioral change | Maintainer-level (D1) |

Pre-release identifiers: `-rc.N` for release candidates of a MAJOR/MINOR; the Phase 0 form `-arch.N` was specific to the architecture document and is retired. No other suffixes.

## 3. Document Version Semantics

Same triplet, scoped to the document: **MAJOR** — a normative statement changes meaning or is removed; **MINOR** — normative content added; **PATCH** — wording, formatting, link repair (D1). A document's version starts at 1.0.0 when it first becomes ACTIVE; DRAFT iterations do not bump versions.

## 4. Instance Pinning

- Every instance pins exactly one framework version: `amf_version` in its INSTANCE.md (standard: [templates/INSTANCE.md](../knowledge/templates/INSTANCE.md)).
- All sessions in that instance run under the pinned version's rules — even if a newer framework exists.
- Upgrading the pin is a deliberate act: a maintenance-type session following [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md), recorded in the session log and CHANGELOG. Never implicit, never partial (an instance is on one version, not a mixture).
- Skipping versions on upgrade is allowed MINOR-to-MINOR; MAJOR upgrades apply each MAJOR's migration in order.

## 5. Deprecation Policy

- Deprecation is announced, never silent: status `DEPRECATED`, header gains `Deprecated` (date) and `Replaced by` (link) per [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) R7.4. A replacement must exist and be named at deprecation time — deprecating without replacement is only allowed when the responsibility itself is retired, and that is a D3.
- **Grace period: one MAJOR version.** Deprecated in N, removable (→ ARCHIVED) no earlier than N+1.
- While DEPRECATED, a component still works: instances may rely on it until they upgrade past the removal version.
- Deprecation of anything in the compatibility promise (§6) is itself a MAJOR event.

## 6. Compatibility Promise (v1.x)

Stable for the entire 1.x series — changing any of these is a 2.0 event:

1. Instance directory contract: `.amf/` layout per architecture §6.2 (INSTANCE.md, `knowledge/`, `sessions/` with SESSION_LOG.md and `handovers/`, `archive/`).
2. The seven role identities and the domain ownership map's shape.
3. Decision classes D1/D2/D3 and their constitutional meaning.
4. Gate identities G0–G6.
5. The five lifecycle classes (C, S, T, I, A).
6. The message envelope field set.
7. Entity ID grammars ([FRAMEWORK_RULES.md](FRAMEWORK_RULES.md) §4) — additive extension allowed, reinterpretation not.
8. The four-status vocabulary and its transitions.

Everything else may evolve at MINOR level. The promise is to instances: a project adopted on 1.0 upgrades through 1.x without structural migration.

## 7. Experimental Track

- New components may ship inside a module's `experimental/` subdirectory, status `DRAFT`, clearly excluded from §6.
- Experimental components may change or vanish at MINOR level without deprecation process.
- **Promotion to stable requires evidence**: at least one real project having used the component, with the outcome recorded in that instance's lessons ledger and referenced in the promoting change's Decision Record (P9: progressive enhancement).
- Instances opt into experimental components explicitly in INSTANCE.md; silence means opted out.

## 8. Migration Policy

- Every MAJOR ships migration notes per breaking change: what changed, why, mechanical steps for an instance, verification checklist. Procedures live in [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md); the *obligation* is constitutional and lives here.
- Migrations must be executable by a cold AI session inside the instance being migrated (P5): no step may require memory of the framework's history.
- A failed migration rolls back to the pinned version; instances are never left between versions (Article VIII discipline applies to upgrade sessions like any other).

## 9. Roadmap Philosophy

- **Evidence-driven.** Future versions are built from what the ledgers show: recurring lessons, gate failure patterns, folding-map friction. Not from speculation (P10).
- **Each document carries its own future.** Growth expectations live in each document's Future Extension Notes; at release planning, the Architect aggregates them with instance evidence into the next version's scope.
- **No version without a migration story.** A change too disruptive to migrate is too disruptive to ship.
- **Anticipated directions** (non-binding, from architecture §14.2): tooling (`amf lint/init/upgrade`), second runtime adapter, metrics over ledgers, cross-project lessons library.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial version semantics, pinning, deprecation, compatibility promise, experimental track |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 2 | Swept Phase 2 forward reference to live link (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- [UPGRADE_GUIDE.md](../operations/UPGRADE_GUIDE.md) holds migration procedure (Phase 7, done); §8 holds policy only.
- If tooling lands (v2 direction), version bump mechanics (R10.1) become automatable; semantics here are unaffected.
- The compatibility promise (§6) is intended to be restated, not weakened, for 2.x: each MAJOR opens with its own promise section.
