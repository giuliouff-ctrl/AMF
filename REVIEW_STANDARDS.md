# Review Standards

| Field | Value |
|---|---|
| ID | QUAL-04 |
| Document | REVIEW_STANDARDS.md |
| Module | quality |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | QA Engineer (content) / Architect (model) |
| Maintainer | Architect |
| Authority | Normative for how reviews are conducted and what makes findings valid — the written standard the Reviewer re-reads at every assumption (A2.3). Subordinate to [QUALITY_SYSTEM.md](QUALITY_SYSTEM.md). |

---

## Document Contract

**Purpose.** Make reviews reproducible: two different reviewers applying this document to the same work should reach the same verdict. This is the document AD-10's procedural separation leans on.
**Scope.** Review method, standards per review type, findings validity, the separation-of-duties procedure. Who reviews is [AGENT_SYSTEM.md](../agents/AGENT_SYSTEM.md)'s (§4 + the Reviewer contract); report format is [MESSAGE_TYPES.md §2.3](../communication/MESSAGE_TYPES.md)'s.
**Responsibilities.** The method; code, design and documentation review standards; findings rules; the separation procedure.
**Dependencies.** [roles/REVIEWER.md](../agents/roles/REVIEWER.md), [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md), [FRAMEWORK_PRINCIPLES.md](../core/FRAMEWORK_PRINCIPLES.md), [AI_CONSTITUTION.md Article IX](../core/AI_CONSTITUTION.md).
**Consumers.** Reviewer (every assumption — the mandatory re-read is *of this document*); authors preparing work; QA Engineer (G4 shares the findings rules).
**Related documents.** [QUALITY_GATES.md](QUALITY_GATES.md) (G1/G3 cite these standards), templates/TECHNICAL_DEBT.md, templates/KNOWN_ISSUES.md.
**Update policy.** D2 (Architect); never negotiated mid-review (Article XI — propose after, apply as written during).

---

## 1. The Method

Every review, regardless of type:

1. **Ritual first** (the separation procedure, §5) — without it, what follows is reading, not reviewing.
2. **Standard, then work**: know what you're checking against before looking at what you're checking — criteria (G0's), design (G1's), this document's applicable section.
3. **Findings against references**: every finding cites what it violates (§4). Hunt in order of blast radius: correctness → integrity (silent D2/debt) → conventions → maintainability.
4. **Verdict last, binary**: PASS / PASS_WITH_NOTES (only NOTE-severity findings) / FAIL (any BLOCKING finding). The verdict follows the findings mechanically — no gestalt overrides.

## 2. Code Review Standard (G3)

Checked in this order:

| Area | The standard |
|---|---|
| **Correctness** | Does what the design and criteria say — logic, boundaries, data flow traced, not skimmed. Edge and error paths per DoD F.3/B.3. |
| **Design fidelity** | Matches the G1-approved design; every deviation has its D-NNN or is a finding (silent D2 — the first canonical smell). |
| **Integrity** | No undeclared debt (second canonical smell); no smuggled scope (R.2); dependency changes have E12+D-NNN. |
| **Security basics** | No secrets in code; input validated at boundaries; injection surfaces (queries, HTML, shell) handled; authz checks where the design requires them. Findings here are BLOCKING by default. |
| **Conventions** | ARCHITECTURE §Conventions followed — naming, structure, idiom; the diff reads like the codebase's best (C.2). |
| **Maintainability** | P7 applied: would a cold session understand this? Complexity earned? Duplication justified? Comments state constraints, not narration. |
| **Cleanliness** | DoD F.4-equivalents: no new warnings/errors/dead code introduced. |

## 3. Design Review Standard (G1)

| Area | The standard |
|---|---|
| **Fit** | Serves every G0 criterion, traceably (1.1); solves the actual problem, not a grander one (P9/P10 — speculative structure is a finding). |
| **Invariants** | ARCHITECTURE §Invariants intact (1.2); data ownership unambiguous; single source of truth preserved (Article III at design level). |
| **Coupling** | New edges justified; boundaries cohesive (P3); the design doesn't thicken reference traffic across an existing boundary. |
| **Failure thinking** | What breaks under partial failure, bad input, concurrent use — addressed or explicitly scoped out. |
| **Decisions** | Every D2 recorded with real options (1.3); consequences honest, including what's foreclosed. |
| **Simplicity** | The simplest design the criteria allow (1.6): a finding names the simpler alternative, or it's taste, not a finding. |

## 4. Findings Rules

- **F4.1** A valid finding = **reference + location + severity**: what it violates (a criterion, a DoD item, a §2/§3 row, an invariant, an article), where (file:line / section), and `BLOCKING` or `NOTE`.
- **F4.2** `BLOCKING`: correctness, integrity, security, invariant, or DoD violations — anything that makes the work wrong, dishonest, or unsafe. `NOTE`: real but non-blocking (a P7 improvement, a naming inconsistency worth a follow-up).
- **F4.3** "I would have done it differently" without a violated reference is not a finding (the Reviewer contract's taste prohibition, operationalized).
- **F4.4** Findings route on report ([MESSAGE_TYPES.md §2.3](../communication/MESSAGE_TYPES.md)): defects → E13; undeclared debt → E24 flag; knowledge drift → E31. Unresolved BLOCKINGs convert before handover (P3.3).
- **F4.5** No praise-padding, no hedged failures (Article XIII): findings are flat statements; the verdict carries no adjectives.

## 5. Separation-of-Duties Procedure (AD-10)

The procedure that makes single-instance review real — all four steps, every review, no exceptions:

1. **Assume explicitly**: `as Reviewer: G3 for T-NNN` logged (A2.1).
2. **Re-read this document** — the applicable section at minimum, every assumption (A2.3). Standards drift; memory drifts faster.
3. **Verify non-authorship** (A2.4): this session-thread did not author the artifact under any role. If it did — at Full profile the review waits for a session that didn't; at collapsed profiles the C8.3 cross-check assignment applies.
4. **Produce the distinct artifact**: a Review Report per [MESSAGE_TYPES.md §2.3](../communication/MESSAGE_TYPES.md) — findings, verdict, refs. An inline "looks good" passes nothing (Q2.3: unrecorded = didn't happen).

Documentation reviews (framework or instance documents as the work product) use the method (§1) + the K-items of the [DoD](DEFINITION_OF_DONE.md) as their standard, with §4 findings rules unchanged.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 5 | Initial standards: method, code/design/docs standards, findings rules, separation procedure |

## Future Extension Notes

- Per-technology review annexes (framework-specific smells, stack-specific security surfaces) attach under §2 as annex tables — additive.
- If structural separation becomes available (multi-instance), §5 step 3 gains the "structural when available" preference flagged in the Constitution's future notes.
