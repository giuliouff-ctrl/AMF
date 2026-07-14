# Extending AMF

| Field | Value |
|---|---|
| ID | OPRN-04 |
| Document | EXTENDING_AMF.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Release Manager (content) / Architect (structure) |
| Maintainer | Release Manager |
| Authority | Normative procedures for growing AMF through its extension points — the operational side of [FRAMEWORK_GOVERNANCE.md §7](../core/FRAMEWORK_GOVERNANCE.md). Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Make additive growth routine and shadow structure impossible (Article XII): one procedure per extension point, each ending in full integration.
**Scope.** The six extension points. What *cannot* extend (amendment territory) is [FRAMEWORK_GOVERNANCE.md §7](../core/FRAMEWORK_GOVERNANCE.md)'s boundary — additions extend, alterations amend.
**Responsibilities.** The common procedure; per-point integration checklists.
**Dependencies.** [FRAMEWORK_GOVERNANCE.md](../core/FRAMEWORK_GOVERNANCE.md) (§6 approvals, §7 boundary), [ROLE_TEMPLATE.md](../agents/ROLE_TEMPLATE.md), [MESSAGE_TYPES.md §1](../communication/MESSAGE_TYPES.md), [CONTEXT_RECONSTRUCTION.md](../knowledge/CONTEXT_RECONSTRUCTION.md) C3.3, [VERSIONING.md §7](../core/VERSIONING.md) (experimental track).
**Consumers.** Architect (executes extensions); any role proposing one.
**Related documents.** [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md), [KNOWLEDGE_SYSTEM.md](../knowledge/KNOWLEDGE_SYSTEM.md), [PROFILES.md](PROFILES.md).
**Update policy.** D2 (Architect); a new extension *point* (a seventh kind of thing) is governance territory, not this document's.

---

## 1. The Common Procedure

Every extension, regardless of point:

1. **Proposal** ([MESSAGE_TYPES.md §2.9](../communication/MESSAGE_TYPES.md)): the addition, the problem it solves, the evidence it rests on (P9 — a second real use case, a recurring M5.1 gap, a ledger pattern; speculation is declined by default).
2. **Approval** per the [matrix](../core/FRAMEWORK_GOVERNANCE.md): D2 Architect; roles and knowledge domains additionally "Owner informed".
3. **Integration** per the point's checklist (§2) — all boxes, or the thing does not exist yet.
4. **Registration**: glossary entry if it names a concept (R1.4); document ID (R3.4); Manifest registry row; framework MINOR at next release.
5. **Consider experimental** ([VERSIONING.md §7](../core/VERSIONING.md)): default for anything unproven — `experimental/` in its module, DRAFT, promoted on one real project's recorded outcome.

## 2. Integration Checklists per Point

**New role** — [ROLE_TEMPLATE.md](../agents/ROLE_TEMPLATE.md) owns the full checklist (contract, ownership without overlap, E-codes, gate map amendment preserving Article IX, escalation rows, roster row, profile collapsing behavior, glossary, ID).

**New workflow**
1. Reading row in [CONTEXT_RECONSTRUCTION.md §3](../knowledge/CONTEXT_RECONSTRUCTION.md) *first* (C3.3 — no workflow without its budget).
2. The WF_ file per the established shape: trigger, T1 by reference, roles per step, messages, E-codes, gates by reference, aborts.
3. Catalog row + a selection rule **positioned deliberately** in the ordered list ([WORKFLOW_INDEX.md §3](../workflows/WORKFLOW_INDEX.md) — order is priority).
4. Gate subset validated against [QUALITY_SYSTEM.md](../quality/QUALITY_SYSTEM.md) (no invented gates).

**New knowledge domain / instance document**
1. Template in `knowledge/templates/` per the established standard shape (spec table, structure, skeleton).
2. Registry row ([KNOWLEDGE_SYSTEM.md §2](../knowledge/KNOWLEDGE_SYSTEM.md)) + exactly one owner in the §3 map (no overlap — the one-owner invariant is the point).
3. [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) rows: which E-codes feed it (new E-codes as needed, sequentially).
4. Profile placement + folding row in [PROFILES.md §2](PROFILES.md) — a document without a Minimal folding is not done (P8).
5. Reading-tier default; T1 rows updated where workflows should read it.

**New message type**
1. Every row of the [§1 format](../communication/MESSAGE_TYPES.md): route, body, lifecycle, persistence target, response, conversion — a type missing any is malformed by definition.
2. Ledger-feeding map updated; escalation matrix row if it routes upward.

**New profile**
1. Complete column: document activation, role collapsing satisfying C8.1–C8.5, gate table satisfying Q5, full folding coverage.
2. Selection guidance row; INSTANCE.md value documented.

**Quality annex** (per-technology checklists)
1. Attaches under [QUALITY_GATES.md](../quality/QUALITY_GATES.md) as `G4-annex-<tech>` (its future-notes pattern) or under [REVIEW_STANDARDS.md §2](../quality/REVIEW_STANDARDS.md) as an annex table.
2. Never modifies the gate model or the DoD core — annexes add criteria rows, only ever scoped to their technology.

## 3. Anti-Patterns (each one is Article XII in action)

- A WF_ file without an index row and reading row — a workflow nobody can select is shadow structure.
- An instance document type invented inside one project — that's a Proposal, not an improvisation; until accepted, the content lives in AI_NOTES or its nearest owned home.
- A "temporary" message type or status value — the vocabularies are closed (R7.1, the ten types); temporary means Proposal + experimental, or nothing.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 7 | Initial procedures: common path + six per-point checklists |

## Future Extension Notes

The first expected extensions, from the future-notes trail across modules: WF_INCIDENT and WF_MIGRATION (workflows), UX Designer / Data Engineer (roles), PERFORMANCE_BUDGET / CONTENT_INVENTORY (knowledge domains) — all awaiting the evidence bar of §1.1.
