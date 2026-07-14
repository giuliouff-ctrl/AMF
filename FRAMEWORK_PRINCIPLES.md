# Framework Principles

| Field | Value |
|---|---|
| ID | CORE-04 |
| Document | FRAMEWORK_PRINCIPLES.md |
| Module | core |
| Class | C — Constitutional |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Architect |
| Authority | Governs engineering judgment wherever no explicit rule decides. Subordinate to [AI_CONSTITUTION.md](AI_CONSTITUTION.md); informs, but never overrides, [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md). |

---

## Document Contract

**Purpose.** Define the engineering philosophy of AMF: the principles that guide design and implementation decisions — in the framework itself and in every project built under it — wherever explicit rules end.

**Scope.** Judgment calls: design trade-offs, structure choices, documentation depth, when to add and when to refrain. Not behavior constraints (Constitution) and not conventions (Rules).

**Responsibilities.** The twelve principles; their relation to the Constitution and Rules; the conflict rule between principles.

**Dependencies.** [AI_CONSTITUTION.md](AI_CONSTITUTION.md).

**Consumers.** All roles, most intensively the Architect (design), Engineer (implementation) and Reviewer (assessing whether work honors the principles).

**Related documents.** [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md), [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md), [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §2 (the failure modes these principles answer).

**Update policy.** Amendment process per [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §5 (class C).

---

## 1. How Principles Bind

- The **Constitution** says what must and must never happen. **Rules** say exactly how routine things are done. **Principles** govern everything in between: they are the tiebreakers of design.
- Principles justify decisions; they never excuse rule-breaking (Constitution, Article XI).
- When two principles genuinely conflict in a concrete decision, the decision is at least a D2: the trade-off is made consciously by the competent authority and recorded with the rationale. "The principles conflicted" is never a reason for an unrecorded choice.

## 2. The Principles

### P1 — Single Responsibility

**Statement.** Every unit — document, module, role, workflow, function — has exactly one responsibility, and every responsibility has exactly one unit.

**Rationale.** Overlap is where duplication, contradiction and orphaned ownership breed. One-to-one mapping makes both directions of every question answerable: "what does this own?" and "who owns this?".

**In practice.**
- Before creating anything, name its single responsibility in one sentence; if the sentence needs "and", split it.
- Before adding to something existing, check the addition belongs to *its* responsibility; otherwise place it where it does belong (Constitution, Article III).
- Never merge unrelated responsibilities to save a file.

### P2 — Modularity and Composition

**Statement.** Capability grows by composing small, self-contained parts — never by widening existing parts.

**Rationale.** Parts with narrow surfaces can be understood, replaced and versioned independently; wide parts entangle every change with every reader.

**In practice.**
- New needs → new module/document/section wired through existing interfaces (see the extension points, [FRAMEWORK_GOVERNANCE.md](FRAMEWORK_GOVERNANCE.md) §7).
- Each part declares purpose, dependencies and consumers explicitly (its contract).
- A part that cannot state what it depends on is not done.

### P3 — Low Coupling, High Cohesion

**Statement.** Minimize what parts must know about each other; maximize how tightly a part's contents belong together.

**Rationale.** Coupling is the cost of change; cohesion is the value of a boundary. Every dependency edge is a promise that must be kept forever or migrated.

**In practice.**
- Depend downward only (architecture §8: layered dependency rule; no cycles ever).
- Reference by link, not by copy — a copy is covert coupling to a stale version.
- When a document keeps needing content from another, the boundary is wrong: propose moving the content, not thickening the reference traffic.

### P4 — Documentation-Driven Development

**Statement.** The record is part of the work, not a report about it. Work is complete only when its documentation is (Definition of Done, quality module).

**Rationale.** In an AI-operated project the documentation *is* the system's memory and coordination medium; undocumented work is functionally lost work (failure modes F2, F5).

**In practice.**
- Plans before execution (session PLAN stage); decisions recorded when made, not reconstructed later.
- Update the owning document in the same session as the change (Constitution, Article V).
- Documentation debt is technical debt: registered, owned, scheduled.

### P5 — AI-First Engineering

**Statement.** Optimize every structure for a stateless reader with a finite context budget: predictable locations, explicit metadata, bounded reading paths, no implied context.

**Rationale.** The primary reader of an AMF project is a cold AI session. What a human colleague would infer from hallway memory, an AI session must find in a file — or it does not exist.

**In practice.**
- Everything findable from the entry point in a bounded number of hops (Manifest → module → document).
- State what a document assumes the reader has read (its contract), so reading order is computable.
- Front-load the load-bearing facts; a reader that stops after the header and first section should leave with the truth, just less detail.
- Never rely on "the previous session will remember".

### P6 — Human Readability

**Statement.** AI-first never means human-hostile. Every artifact remains plainly readable by a human with standard tools.

**Rationale.** The Human Owner audits, approves and overrides. A memory system the human cannot inspect cannot be trusted, and trust is the product.

**In practice.**
- Plain language, complete sentences for reasoning, tables for enumerable facts.
- No encoded blobs, no private shorthand, no structure that requires tooling to decode.
- Jargon only from the [FRAMEWORK_GLOSSARY.md](FRAMEWORK_GLOSSARY.md).

### P7 — Maintainability Over Cleverness

**Statement.** Choose the solution that is easiest to understand, verify and change — not the one that is most elegant, most general, or most impressive.

**Rationale.** Every artifact will be read many more times than written, by sessions with no access to its author's intent.

**In practice.**
- Boring and explicit beats clever and compact.
- Generality must be earned by a second real use case, not anticipated by a first.
- If explaining it takes longer than redoing it simply, redo it simply.

### P8 — Scalability by Subtraction

**Statement.** The framework scales down as deliberately as it scales up. Fitting a small project is a design requirement, not a degraded mode.

**Rationale.** A methodology that punishes small projects gets abandoned there, and an abandoned framework governs nothing (failure mode F7). AMF's profiles exist exactly for this (architecture AD-2).

**In practice.**
- Prefer folding granularity (fewer, denser documents) over dropping knowledge categories.
- Process weight must be justified by project weight; when in doubt, start one profile lighter and upgrade on evidence.
- Never design a feature that only works at Full profile without defining its Minimal folding.

### P9 — Progressive Enhancement

**Statement.** Start with the minimum that is correct and complete; add only when evidence demands it.

**Rationale.** Speculative structure is debt with no borrower: it must be maintained, read and honored by every future session while serving no one.

**In practice.**
- New framework components enter as experimental ([VERSIONING.md](VERSIONING.md) §7) and earn promotion through real use.
- Empty sections and placeholder documents are forbidden — create them when they have content.
- The ledgers tell you what to build next; build from evidence, not anticipation.

### P10 — Future-Proofing Without Speculation

**Statement.** Prepare for change by keeping doors open (extension points, stable contracts, versioning), never by building rooms nobody asked for.

**Rationale.** The future is accommodated structurally — additive growth, migration paths — not predictively. Predictions rot; open doors don't.

**In practice.**
- Contracts and IDs stable; additions additive; removals through deprecation with grace periods.
- Every document carries Future Extension Notes: where it expects to grow, so growth lands prepared.
- The second use case triggers the abstraction, not the first (see P7).

### P11 — Explicitness Over Implicitness

**Statement.** Everything that matters is written: assumptions, ownership, status, authority, reading prerequisites, known gaps.

**Rationale.** Implicit knowledge is inaccessible to exactly the reader AMF serves (P5) and unverifiable by exactly the authority AMF answers to (P6). Ambiguity is the raw material of every framework failure.

**In practice.**
- Declare assumptions in the assumptions record; mark the unknown as unknown (Constitution, Article IV).
- No ambient conventions: if it's a convention, it's in [FRAMEWORK_RULES.md](FRAMEWORK_RULES.md).
- Metadata is never optional (headers, IDs, statuses — Rules §5).

### P12 — Professional Craftsmanship

**Statement.** Every artifact is built as if it will be maintained for years by strangers — because it will be.

**Rationale.** The framework's authority rests on its own quality: sloppy framework documents license sloppy projects. Craftsmanship is the compound interest of all other principles.

**In practice.**
- Production quality always; there are no throwaway artifacts inside an instance (scratch work stays outside it).
- Review your own work against the standards before offering it for review (then Article IX review still applies).
- Leave everything you touch at least as consistent as you found it — via the owning document, never via drive-by edits (Article V).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 1 | Initial twelve principles with binding and conflict rules |

## Future Extension Notes

- Candidate principle for v1.1 pending evidence: economy of context (token/reading budgets as first-class design constraint) — currently distributed across P5 and the knowledge module; may deserve its own principle if practice shows it under-weighted.
- Per-technology engineering principles (e.g. web performance, data integrity) belong in quality-module annexes (Phase 5+), never here; this document stays technology-agnostic.
