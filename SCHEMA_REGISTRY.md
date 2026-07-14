# Schema Registry

| Field | Value |
|---|---|
| ID | ROOT-04 |
| Document | SCHEMA_REGISTRY.md |
| Module | root |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | The shared structural language of AMF: authoritative index of every official schema, and normative home of the cross-cutting vocabularies no single module owns. Everything created inside AMF follows a structure registered here. Subordinate to [core](core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Guarantee that no document, report, message or artifact invents its own structure: one registry of every official schema, each with exactly one owner — plus the universal vocabularies (statuses, priorities, severities) consolidated in one view.
**Scope.** Index and cross-cutting vocabularies. Every schema's *content* stays with its owning document (Article III) — this registry points, and only defines what nothing else owns.
**Responsibilities.** The schema catalog; the vocabulary consolidation; the validation-rule taxonomy; the no-orphan-structure rule.
**Dependencies.** [FRAMEWORK_RULES.md](core/FRAMEWORK_RULES.md) (metadata, naming, IDs, references — the base layer every schema inherits).
**Consumers.** Every agent producing any artifact; [EXTENDING_AMF.md](operations/EXTENDING_AMF.md) (new schemas register here); tooling (this registry is the future linter's table of contents).
**Related documents.** [AMF_MANIFEST.md](AMF_MANIFEST.md) (indexes documents; this indexes *structures*).
**Update policy.** D2 (Architect). A schema change happens in its owning document; the row here updates in the same change (R10.6 discipline).

---

## 1. The Rule

**S1.1 — No orphan structures.** Every recurring artifact type in AMF has exactly one registered schema. Producing an artifact outside a registered schema is Article XII shadow structure; needing a new one is an extension case ([EXTENDING_AMF.md §1](operations/EXTENDING_AMF.md)) that ends with a row here.

**S1.2 — Schemas inherit the base layer.** Every schema presumes [FRAMEWORK_RULES.md](core/FRAMEWORK_RULES.md): metadata headers (§5), naming (§2), identifiers (§3–4), statuses (§7), references (§8), markdown (§9). No schema restates or overrides them.

## 2. Schema Catalog

### 2.1 Framework document schemas

| Schema | Owner document |
|---|---|
| Framework document (header + contract + footer) | [FRAMEWORK_RULES.md §5–6](core/FRAMEWORK_RULES.md) |
| Role contract (five mandatory parts + skeleton) | [ROLE_TEMPLATE.md](agents/ROLE_TEMPLATE.md) |
| Workflow document (trigger/T1/roles/gates/steps/aborts) | established shape: [WORKFLOW_INDEX.md §1](workflows/WORKFLOW_INDEX.md); exemplar [WF_FEATURE.md](workflows/WF_FEATURE.md) |
| Migration note (what/why/steps/end-state/rollback) | [UPGRADE_GUIDE.md §4](operations/UPGRADE_GUIDE.md) |

### 2.2 Instance document schemas (the 22)

Each instance document's schema — purpose, structure, entry format, skeleton, validation rules — is its template standard in `knowledge/templates/` (registry: [KNOWLEDGE_SYSTEM.md §2](knowledge/KNOWLEDGE_SYSTEM.md)). Highlights by artifact kind:

| Artifact | Schema |
|---|---|
| Project identity | [templates/PROJECT.md](knowledge/templates/PROJECT.md) |
| Architecture | [templates/ARCHITECTURE.md](knowledge/templates/ARCHITECTURE.md) |
| Task (row + state model) | [templates/TASKS.md](knowledge/templates/TASKS.md) |
| Decision Record | [templates/DECISIONS.md](knowledge/templates/DECISIONS.md) (message form identical: [MESSAGE_TYPES.md §2.5](communication/MESSAGE_TYPES.md)) |
| Status snapshot | [templates/CURRENT_STATUS.md](knowledge/templates/CURRENT_STATUS.md) |
| Changelog / release record | [templates/CHANGELOG.md](knowledge/templates/CHANGELOG.md) / [templates/RELEASE_HISTORY.md](knowledge/templates/RELEASE_HISTORY.md) |
| Issue (bug) | [templates/KNOWN_ISSUES.md](knowledge/templates/KNOWN_ISSUES.md) |
| Risk | [templates/RISK_REGISTER.md](knowledge/templates/RISK_REGISTER.md) |
| Research entry | [templates/RESEARCH.md](knowledge/templates/RESEARCH.md) |
| Roadmap | [templates/ROADMAP.md](knowledge/templates/ROADMAP.md) |
| Debt entry | [templates/TECHNICAL_DEBT.md](knowledge/templates/TECHNICAL_DEBT.md) |
| Meeting/Owner input | [templates/MEETING_NOTES.md](knowledge/templates/MEETING_NOTES.md) |
| Session log entry / handover | [templates/SESSION_LOG.md](knowledge/templates/SESSION_LOG.md) / [templates/HANDOVER.md](knowledge/templates/HANDOVER.md) |

### 2.3 Communication schemas

| Artifact | Schema |
|---|---|
| Message envelope | [COMMUNICATION_PROTOCOL.md §2](communication/COMMUNICATION_PROTOCOL.md) |
| The ten message types (incl. Review Report, Escalation, Approval) | [MESSAGE_TYPES.md §2](communication/MESSAGE_TYPES.md) |
| Compact log form | [COMMUNICATION_PROTOCOL.md §5](communication/COMMUNICATION_PROTOCOL.md) |

### 2.4 Quality schemas

| Artifact | Schema |
|---|---|
| Gate checklists G0–G6 | [QUALITY_GATES.md](quality/QUALITY_GATES.md) |
| Definition of Done (per work type) | [DEFINITION_OF_DONE.md](quality/DEFINITION_OF_DONE.md) |
| Review method + findings format | [REVIEW_STANDARDS.md §1/§4](quality/REVIEW_STANDARDS.md) |

## 3. Universal Vocabularies (consolidated view)

Each vocabulary is owned where cited; this table is the one place to see them together. All are closed sets — extending any is D2 through its owner.

| Vocabulary | Values | Owner |
|---|---|---|
| Document status | DRAFT · ACTIVE · DEPRECATED · ARCHIVED | [FRAMEWORK_RULES.md §7](core/FRAMEWORK_RULES.md) |
| Task state | TODO · IN_PROGRESS · BLOCKED · DONE | [templates/TASKS.md](knowledge/templates/TASKS.md) |
| Issue status / severity | OPEN · INVESTIGATING · RESOLVED · WONTFIX / CRITICAL · MAJOR · MINOR | [templates/KNOWN_ISSUES.md](knowledge/templates/KNOWN_ISSUES.md) |
| Risk status / scores | OPEN · MITIGATING · CLOSED · OCCURRED / L · M · H | [templates/RISK_REGISTER.md](knowledge/templates/RISK_REGISTER.md) |
| Priority bands | P1 · P2 · P3 | [templates/BACKLOG.md](knowledge/templates/BACKLOG.md) |
| Message status | PENDING · RESOLVED · ESCALATED | [COMMUNICATION_PROTOCOL.md §3](communication/COMMUNICATION_PROTOCOL.md) |
| Review verdict / finding severity | PASS · PASS_WITH_NOTES · FAIL / BLOCKING · NOTE | [REVIEW_STANDARDS.md §4](quality/REVIEW_STANDARDS.md) |
| Decision classes | D1 · D2 · D3 | [AI_CONSTITUTION.md Art. VI](core/AI_CONSTITUTION.md) |
| Assumption status | WORKING · VALIDATED · INVALIDATED | [templates/ASSUMPTIONS.md](knowledge/templates/ASSUMPTIONS.md) |
| Debt status | CARRIED · REPAYING · RETIRED | [templates/TECHNICAL_DEBT.md](knowledge/templates/TECHNICAL_DEBT.md) |

## 4. Validation Taxonomy

Every schema's validation rules fall into five machine-checkable kinds (AD-7; the future linter's rule classes):

| Kind | Checks | Example |
|---|---|---|
| **Presence** | Required fields/sections exist | Header fields per R5; contract sections per R6.1 |
| **Vocabulary** | Values from the closed sets of §3 | A task state outside the four is invalid |
| **Identity** | IDs match grammars, never reused, resolve in their home | R3–R4; R4.4 |
| **Reference** | Links resolve; refs bidirectional where required (P7.1) | R8.4 |
| **Integrity** | Cross-document consistency | Registry rows match headers; snapshot vs ledger (M4.1); INSTANCE checklist matches disk |

A schema introducing a rule outside these kinds extends the taxonomy first (D2 here).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 6 (Template & Schema System) | Initial registry: catalog, consolidated vocabularies, validation taxonomy |

## Future Extension Notes

New schemas add a row via the extension procedure; the taxonomy (§4) is the stable surface tooling will build on. If per-technology artifact schemas appear (e.g. API spec templates), they register under §2.2 as instance-document extensions.
