# Framework Rules

| Field | Value |
|---|---|
| ID | CORE-05 |
| Document | FRAMEWORK_RULES.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.1.1 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Normative for all operational conventions: naming, structure, metadata, identifiers, statuses, cross-references, markdown. Subordinate to [AI_CONSTITUTION.md](AI_CONSTITUTION.md); enforced through Article XI. |

---

## Document Contract

**Purpose.** Define the exceptionless conventions every AMF document and artifact follows, so that any reader — human or AI — can predict where things are, what they are called, and what their metadata means, in any AMF repository or instance.

**Scope.** All framework documents and all instance documents. Source code conventions of individual projects are out of scope (they belong to each project's own standards, recorded in its instance).

**Responsibilities.** Language and encoding; naming; directory conventions; identifier grammars; metadata headers; document contract sections; status vocabulary and transitions; cross-reference rules; markdown standards; update procedure; conformance.

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md) (Articles III, V, XI); [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md) (terms used here).

**Consumers.** Every role, every time any document is created or updated.

**Related documents.** [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) (who authorizes what), [VERSIONING.md](VERSIONING.md) (version semantics), [SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md) (when updates happen).

**Update policy.** Amendment process per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5 (class C). Additive convention entries (e.g. a new ID type) are D2 per the approval matrix.

---

## 1. Language, Encoding, Dates

- **R1.1** Framework and instance documents are written in **English**. (Project deliverables — UI text, user-facing copy — follow the project's own language requirements and are out of scope.)
- **R1.2** Files are UTF-8, LF line endings, no BOM.
- **R1.3** Dates are ISO 8601 (`YYYY-MM-DD`). Where time matters, `YYYY-MM-DD HH:MM` in the instance's declared timezone (INSTANCE.md).
- **R1.4** Terminology per [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md): one term per concept, no synonyms. Introducing a new term requires a glossary entry first.

## 2. File and Directory Naming

- **R2.1** All framework and instance documents: `UPPER_SNAKE_CASE.md`. ASCII letters, digits, underscores only. No spaces, no hyphens in filenames.
- **R2.2** Module directories: lowercase, singular purpose (`core/`, `knowledge/`, `agents/`, `communication/`, `quality/`, `workflows/`, `operations/`).
- **R2.3** Reserved subdirectory names: `roles/` (agent contracts), `templates/` (instance document standards), `experimental/` (per [VERSIONING.md](VERSIONING.md) §7), `archive/` (instance tier-3 storage), `handovers/` (per-session handovers), `sessions/` (instance session records).
- **R2.4** Prefixes: workflows `WF_`; no other filename prefixes are defined in v1.0.
- **R2.5** Handover files are named by session ID: `S-YYYYMMDD-NN.md` (§4).
- **R2.6** A file is renamed only through deprecation (old name DEPRECATED with pointer, new name created) — never renamed in place once ACTIVE.

## 3. Document Identifiers

- **R3.1** Every framework document has a document ID: `<MODULE CODE>-<NN>`, two digits, assigned sequentially within the module, **never reused** — including after archiving.
- **R3.2** Module codes: `ROOT` (repository root), `CORE`, `KNOW` (knowledge), `AGNT` (agents), `COMM` (communication), `QUAL` (quality), `WFLW` (workflows), `OPRN` (operations).
- **R3.3** Current CORE assignments: CORE-01 AMF_OVERVIEW, CORE-02 AI_CONSTITUTION, CORE-03 FRAMEWORK_GOVERNANCE, CORE-04 FRAMEWORK_PRINCIPLES, CORE-05 FRAMEWORK_RULES, CORE-06 FRAMEWORK_GLOSSARY, CORE-07 SESSION_MANAGEMENT, CORE-08 VERSIONING. ROOT assignments: ROOT-01 AMF_MANIFEST, ROOT-02 README, ROOT-03 AMF_ARCHITECTURE.
- **R3.4** Later phases assign their module's IDs in their deliverable order and record them in the Manifest registry ([AMF_MANIFEST.md](../AMF_MANIFEST.md)).

## 4. Entity Identifiers (instance scope)

- **R4.1** Grammars — all scoped per instance, all immutable once assigned, none ever reused:

| Entity | Grammar | Example | Lives in |
|---|---|---|---|
| Session | `S-YYYYMMDD-NN` (NN = ordinal that day, 01-based) | S-20260712-01 | SESSION_LOG.md |
| Decision | `D-NNN` | D-014 | DECISIONS.md |
| Task | `T-NNN` | T-042 | TASKS.md |
| Risk | `R-NNN` | R-003 | RISK_REGISTER.md |
| Question | `Q-NNN` | Q-007 | OPEN_QUESTIONS.md |
| Issue | `I-NNN` | I-021 | KNOWN_ISSUES.md |
| Lesson | `L-NNN` | L-005 | LESSONS_LEARNED.md |
| Message | `M-NN` within session; cited `<S-ID>/M-NN` | S-20260712-01/M-03 | SESSION_LOG.md |

- **R4.2** `NNN` is zero-padded to three digits; on overflow, width grows (no renumbering).
- **R4.3** In Minimal profile, entities whose home document is folded keep their grammar; they live in the folded section (folding map: [PROFILES.md §2](../operations/PROFILES.md)).
- **R4.4** Every entity reference in prose uses its ID (e.g. "per D-014"), which must resolve in the owning ledger.

## 5. Metadata Header

- **R5.1** Every document begins with a single H1 title followed by the metadata table. Framework documents (classes C, S, T) require exactly these fields, in this order: `ID, Document, Module, Class, Version, Status, Owner, Maintainer, Authority`.
- **R5.2** Instance documents (classes I, A) require: `ID, Document, Class, Profile-tier, Owner (role), Updated (date + session ID), Status`. Exact form is fixed by each template standard in `knowledge/templates/` (general form: [KNOWLEDGE_SYSTEM.md §4](../knowledge/KNOWLEDGE_SYSTEM.md)), which may add fields but never remove these.
- **R5.3** `Authority` is one sentence stating what the document governs and what it is subordinate to.
- **R5.4** Class values are the five lifecycle classes defined in [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §7.1: `C, S, T, I, A`.

## 6. Document Contract Sections

- **R6.1** Every framework document contains, immediately after the metadata header, a **Document Contract** section with exactly: Purpose, Scope, Responsibilities, Dependencies, Consumers, Related documents, Update policy.
- **R6.2** Every framework document ends with **Revision History** (table: Version, Date, Author, Change) followed by **Future Extension Notes**.
- **R6.3** Body structure between contract and footer is the document's own, subject to §9.
- **R6.4** Instance documents follow the structure fixed by their template standard instead (`knowledge/templates/`); templates must include equivalents of purpose, update rules and revision tracking.

## 7. Status Vocabulary and Transitions

- **R7.1** Exactly four statuses: `DRAFT` (exists, not yet authoritative), `ACTIVE` (authoritative), `DEPRECATED` (superseded; replacement named in its header; still readable), `ARCHIVED` (historical; excluded from default reading).
- **R7.2** Legal transitions: DRAFT→ACTIVE, ACTIVE→DEPRECATED, DEPRECATED→ARCHIVED, DRAFT→ARCHIVED (abandoned). No others. Authorization per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §4.
- **R7.3** Only ACTIVE documents may be cited normatively. Citing DRAFT is allowed only inside the phase building it, marked "(DRAFT)".
- **R7.4** A DEPRECATED document's header gains two fields: `Deprecated` (date) and `Replaced by` (link).

## 8. Cross-References

- **R8.1** References are relative markdown links to the file, optionally with a section anchor: `[SESSION_MANAGEMENT.md](SESSION_MANAGEMENT.md)`, `[GOVERNANCE §5](FRAMEWORK_GOVERNANCE.md#5-amendment-process)`.
- **R8.2** **Reference, never copy** (Constitution, Article III): at most one summarizing sentence may accompany a link; quoting a normative rule verbatim elsewhere is forbidden — link to it.
- **R8.3** Forward references to documents that do not exist yet must carry a phase marker: "operations/adapters/CURSOR.md (v2)". When the target is created, its creating phase must sweep and de-mark these (each phase's exit criteria include this).
- **R8.4** A broken link is a defect (instance: I-NNN entry; framework: D2 fix by the Maintainer).
- **R8.5** Circular *normative* dependencies are forbidden (architecture §8.1). Informative mentions upward are allowed but must not carry obligations.

## 9. Markdown Standards

- **R9.1** One H1 per file (the title). Sections H2, subsections H3; no deeper than H4.
- **R9.2** Tables for enumerable, comparable facts; prose for reasoning; lists for sequences and rule sets. Never encode reasoning into table cells.
- **R9.3** Fenced code blocks with a language tag (` ```text ` for trees/diagrams without a better tag).
- **R9.4** No raw HTML. No images as normative content (diagrams are text: fenced trees or mermaid; a mermaid diagram must remain understandable from its source text).
- **R9.5** Bold marks a term at its definition point and field labels; italics sparingly for emphasis; inline code for literals (filenames, IDs, statuses, field values).
- **R9.6** Rule identifiers in this document (`R1.1`…) are stable and citable; the pattern is available to other normative documents.

## 10. Update Procedure

On every change to any document:

- **R10.1** Bump the document version per [VERSIONING.md](VERSIONING.md) §3.
- **R10.2** Append a revision-history row (framework docs) or stamp `Updated` with date + session ID (instance docs).
- **R10.3** Verify the document's outgoing links still resolve; fix or flag per R8.4.
- **R10.4** Confirm the change is within the editor's authority ([FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §6); if not, stop and route.
- **R10.5** Apply the [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) for any instance events the change implies.
- **R10.6** Registry: reflect status/version changes in the Manifest registry ([AMF_MANIFEST.md](../AMF_MANIFEST.md)).

## 11. Conformance

- **R11.1** Conventions in this document are exceptionless (Constitution, Article XI). A convention that proves wrong is changed through governance, not violated.
- **R11.2** All rules here are deliberately machine-checkable (architecture AD-7): a future linter must be able to verify each `R` rule from file content alone. New conventions must preserve this property.
- **R11.3** Nonconforming artifacts are brought to convention in the session that finds them, or logged as defects if out of that session's scope.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial conventions: naming, IDs, metadata, statuses, cross-references, markdown, update procedure |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 2 | Swept Phase 2 forward references to live links (R8.3) |
| 1.1.0 | 2026-07-12 | Architect (AI), Phase 4-5 | Added Message ID grammar M-NN (D2 additive, Phase 4) |
| 1.1.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- Phase 2 fixed instance-document header fields (R5.2) via `knowledge/templates/`; new entity types remain D2 additive per §4.
- A future `amf lint` (architecture §14.2) should implement §11.2 checks; rule IDs here are its intended error codes.
- If a project needs non-English instance documents, an amendment to R1.1 must define translation-of-authority rules; not designed speculatively (P10).
