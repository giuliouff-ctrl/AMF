# Quality System

| Field | Value |
|---|---|
| ID | QUAL-01 |
| Document | QUALITY_SYSTEM.md |
| Module | quality |
| Class | S — Stable spec |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | QA Engineer (content) / Architect (model) |
| Maintainer | Architect |
| Authority | Normative for the quality model: what gates are, how they run, how they fail, and how profiles may merge them. Gate identities G0–G6 are part of the v1.x compatibility promise ([VERSIONING.md §6](../core/VERSIONING.md)). Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Operationalize [Article X](../core/AI_CONSTITUTION.md): quality as objective, binary, evidence-based gates — so the bar never depends on a session's mood or phrasing.

**Scope.** The gate model and its mechanics. Per-gate checklists ([QUALITY_GATES.md](QUALITY_GATES.md)), completion definitions ([DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md)), review method ([REVIEW_STANDARDS.md](REVIEW_STANDARDS.md)); role authority is [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md)'s.

**Responsibilities.** Quality philosophy; the gate model; evidence rules; failure handling; profile merging constraints; the module's division of labor.

**Dependencies.** [AI_CONSTITUTION.md](../core/AI_CONSTITUTION.md) (Articles IV, IX, X), [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md) (§4 authority map), [COMMUNICATION_PROTOCOL.md](../communication/COMMUNICATION_PROTOCOL.md) (Review Report, Approval), [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §12.

**Consumers.** All roles; every workflow (each invokes its gate subset by reference).

**Related documents.** [QUALITY_GATES.md](QUALITY_GATES.md), [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md), [REVIEW_STANDARDS.md](REVIEW_STANDARDS.md), [PROFILES.md](../operations/PROFILES.md).

**Update policy.** D2 (Architect); gate identities are D3.

---

## 1. Philosophy

Three commitments, all constitutional in origin:

1. **Binary** (Article X). A gate passes or fails. `PASS_WITH_NOTES` exists only inside Review Reports for genuinely non-blocking findings — the *gate* still either passed or didn't. "Mostly passed", "passed in spirit", "will pass after this small thing" are not states.
2. **Objective.** Every criterion is checkable from artifacts and evidence — never from confidence, seniority, or optimism. If a criterion needs judgment, the checklist names *whose* judgment and against *what written standard*.
3. **Evidence-based** (Article IV). A gate record without evidence refs is void. "Checked" means "here is what was run/read/compared, and here is what it showed".

The system's economy: gates are **proportional in effort, never in rigor** — a one-page site's G4 might be a ten-minute checklist pass; it is still binary, evidenced, and separated by duty.

## 2. The Gate Model

Seven gates, identities fixed (architecture §12), authority per [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md), criteria per [QUALITY_GATES.md](QUALITY_GATES.md):

```text
G0 Requirements ready ─ the work is defined
G1 Design approved ──── the approach is sound        (skippable only where no design content exists)
G2 Implementation done ─ the maker says done, with evidence
G3 Review passed ─────── fresh eyes say done
G4 Verification passed ─ behavior says done
G5 Knowledge updated ─── the instance says what happened
G6 Release approved ──── the Owner says ship          (D3, never delegated, never profiled away)
```

- **Q2.1** Workflows invoke the subset they need (WF_FEATURE: G0–G5, +G6 when shipping; WF_BUGFIX: G2–G5; the binding lists live in each workflow). A workflow may not invent gates or criteria ad hoc (Article X).
- **Q2.2** Gates run in order within a work item; a later gate presumes the earlier ones' records exist.
- **Q2.3** Gate results are recorded in the session log (Approval / Review Report per [MESSAGE_TYPES.md](../communication/MESSAGE_TYPES.md)) with evidence refs — the record *is* the passage; an unrecorded pass didn't happen (Article V).

## 3. Evidence Rules

- **Q3.1** Evidence is a pointer to something inspectable: command output, a diff, a checklist walked with results, a criterion-by-criterion comparison. Prose claims ("tested thoroughly") are not evidence.
- **Q3.2** Evidence lives where the gate record points — session log inline for small items, or the artifact it naturally produced (G4's verification notes, G6's package).
- **Q3.3** Self-declared G2 has the strictest evidence duty, precisely because it is self-declared: what was built, what was self-checked, what was *not* checked (honest gaps, Article IV).

## 4. Failure Handling

- **Q4.1** A failed gate returns work with findings (Review Report's findings[], or the checker's criterion-level record). Failure is routine, not exceptional — the system exists to catch things.
- **Q4.2** **Second failure, same cause → mandatory escalation** ([AGENT_SYSTEM.md §5.1](../agents/AGENT_SYSTEM.md)): the pattern is the problem (bad criteria, bad design, bad scoping) and re-grinding won't fix it.
- **Q4.3** Work past a voided gate rolls back to the gate (Article X consequences): anything built on an invalid pass is untrusted until re-gated.
- **Q4.4** Gate friction is signal: recurring near-misses on a criterion feed a Proposal (change the criterion through governance) or a lesson — never a quiet local waiver (Article XI).

## 5. Profile Merging Constraints

Profiles may merge gate *execution*, never gate *meaning* (AD-2; application in [PROFILES.md](../operations/PROFILES.md)):

- **Q5.1** Mergeable: G3+G4 into one review-and-verify pass at Minimal (one checker, both checklists, both recorded).
- **Q5.2** Never mergeable: G2 with G3/G4 (self-check is not a check — Article IX); anything with G6 (C8.5: the Owner's gate is identical at every profile).
- **Q5.3** Merged gates keep both identities in records ("G3+G4: PASS") — merging is an execution economy, not a criteria discount.
- **Q5.4** Article IX holds through every merge: the merged checker didn't author the work (C8.3's cross-check assignments).

## 6. Division of Labor (this module)

| Question | Answered by |
|---|---|
| What must be true to pass gate N? | [QUALITY_GATES.md](QUALITY_GATES.md) |
| What does "done" mean for this work type? | [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) |
| How is a review conducted, and what makes findings valid? | [REVIEW_STANDARDS.md](REVIEW_STANDARDS.md) |
| Who authors/checks each gate? | [AGENT_SYSTEM.md §4](../agents/AGENT_SYSTEM.md) (by reference, never restated here) |
| When does each gate run? | Each workflow ([WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md)) |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 5 | Initial model: philosophy, gate mechanics, evidence rules, failure handling, merging constraints |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- Per-technology checklist annexes (web performance, data integrity, a11y depth) attach under [QUALITY_GATES.md](QUALITY_GATES.md) as annexes without touching the model (architecture §5.6 scalability note).
- If tooling lands, Q2.3 gate records become lintable (evidence-ref presence); the model is unchanged.
