# Knowledge System

| Field | Value |
|---|---|
| ID | KNOW-01 |
| Document | KNOWLEDGE_SYSTEM.md |
| Module | knowledge |
| Class | S — Stable spec |
| Version | 1.0.2 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Normative for the design of per-project memory: which documents exist in an instance, what each owns, who owns each domain, and how knowledge lives, ages and is archived. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Define the Knowledge System — the long-term memory of every AMF project — so that everything that matters exists in exactly one known place and a cold session can trust what it reads.

**Scope.** Instance knowledge: the 22 instance documents, their registry, domain ownership, lifecycle and archiving. Not reading order ([CONTEXT_RECONSTRUCTION.md](CONTEXT_RECONSTRUCTION.md)), not update events ([UPDATE_MATRIX.md](UPDATE_MATRIX.md)), not the per-document standards (templates/).

**Responsibilities.** System design; instance document registry; domain ownership map; instance header standard; ID counters; knowledge lifecycle; archiving policy; knowledge quality rules.

**Dependencies.** [AI_CONSTITUTION.md](../core/AI_CONSTITUTION.md) (Articles III, IV, V, VII), [FRAMEWORK_RULES.md](../core/FRAMEWORK_RULES.md) (R4, R5.2, §10), [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) (AD-8, §6.2, §7.3, §11).

**Consumers.** All roles in every project session; the workflows; operations (instantiation and folding).

**Related documents.** [CONTEXT_RECONSTRUCTION.md](CONTEXT_RECONSTRUCTION.md), [UPDATE_MATRIX.md](UPDATE_MATRIX.md), templates/* (22 standards), [PROFILES.md](../operations/PROFILES.md).

**Update policy.** D2 (Architect) for additive changes per [FRAMEWORK_GOVERNANCE.md](../core/FRAMEWORK_GOVERNANCE.md) §6; structural changes to the registry or ownership shape are D3 (compatibility promise, [VERSIONING.md](../core/VERSIONING.md) §6).

---

## 1. Design

The Knowledge System rests on four commitments:

1. **One home per fact** (Article III). The registry (§2) partitions all project knowledge; the ownership map (§3) partitions write authority. No fact can have two homes; no home can have two owners.
2. **Snapshot / ledger split** (AD-8). Class **I** documents describe *now* and are freely rewritten. Class **A** documents record *history* and are append-only. No document is both; snapshots may be rewritten precisely because ledgers preserve what they supersede.
3. **Bounded reconstruction** (AD-3). The system is navigable within a context budget: tiers and reading lists in [CONTEXT_RECONSTRUCTION.md](CONTEXT_RECONSTRUCTION.md).
4. **Event-driven maintenance** (Article V). Documents update when defined events occur — [UPDATE_MATRIX.md](UPDATE_MATRIX.md) — not when someone remembers.

## 2. Instance Document Registry

The complete set. Standards in `templates/`; profile presence per architecture §7.3 (folding map: [PROFILES.md §2](../operations/PROFILES.md)).

| Instance file | ID | Class | Owner (role) | Default tier | Profile |
|---|---|---|---|---|---|
| INSTANCE.md | KNOW-04 | I | Orchestrator | T0 | Minimal+ |
| PROJECT.md | KNOW-05 | I | Product Analyst | T1 | Minimal+ |
| ARCHITECTURE.md | KNOW-06 | I | Architect | T1 | Minimal+ |
| ROADMAP.md | KNOW-07 | I | Product Analyst | T2 | Standard+ |
| TASKS.md | KNOW-08 | I | Orchestrator | T1 | Minimal+ |
| BACKLOG.md | KNOW-09 | I | Product Analyst | T2 | Standard+ |
| DECISIONS.md | KNOW-10 | A | Architect | T1 (index) | Minimal+ |
| CURRENT_STATUS.md | KNOW-11 | I | Orchestrator | T0 | Minimal+ |
| CHANGELOG.md | KNOW-12 | A | Release Manager | T2 | Standard+ |
| KNOWN_ISSUES.md | KNOW-13 | I | QA Engineer | T1 | Standard+ |
| TECHNICAL_DEBT.md | KNOW-14 | I | Architect | T2 | Full |
| RISK_REGISTER.md | KNOW-15 | I | Orchestrator | T2 | Full |
| DEPENDENCIES.md | KNOW-16 | I | Engineer | T2 | Standard+ |
| ASSUMPTIONS.md | KNOW-17 | I | Product Analyst | T2 | Full |
| OPEN_QUESTIONS.md | KNOW-18 | I | Orchestrator | T2 | Full |
| RESEARCH.md | KNOW-19 | A | Architect | T2 | Full |
| MEETING_NOTES.md | KNOW-20 | A | Product Analyst | T2 | Full |
| LESSONS_LEARNED.md | KNOW-21 | A | Orchestrator | T3 | Full |
| RELEASE_HISTORY.md | KNOW-22 | A | Release Manager | T2 | Standard+ |
| AI_NOTES.md | KNOW-23 | A | any role | T3 | Full |
| SESSION_LOG.md | KNOW-24 | A | Orchestrator | T1 (recent) | Minimal+ |
| HANDOVER (per session) | KNOW-25 | A | Orchestrator | T0 (latest) | Minimal+ |

Registry rules:

- **K2.1** An instance contains exactly the files its profile activates — no extra document types (Article XII; new types are extension work), no placeholder files (P9).
- **K2.2** Instance documents carry the ID of their governing standard (they are typed by it); instance identity comes from the project, not the file.
- **K2.3** "Default tier" is the document's typical reading priority; the binding per-workflow lists live in [CONTEXT_RECONSTRUCTION.md](CONTEXT_RECONSTRUCTION.md).

## 3. Domain Ownership Map

One owner per knowledge domain; owners hold write authority, all other roles propose via messages ([COMMUNICATION_PROTOCOL.md](../communication/COMMUNICATION_PROTOCOL.md)).

| Domain | Owner (role) | Documents |
|---|---|---|
| Business: vision, goals, scope, stakeholders | Product Analyst | PROJECT, BACKLOG, ROADMAP, ASSUMPTIONS, MEETING_NOTES |
| Technical design: architecture, decisions, debt, research | Architect | ARCHITECTURE, DECISIONS, TECHNICAL_DEBT, RESEARCH |
| Implementation facts | Engineer | DEPENDENCIES (and the source tree itself) |
| Planning & session accountability | Orchestrator | INSTANCE, TASKS, CURRENT_STATUS, RISK_REGISTER, OPEN_QUESTIONS, LESSONS_LEARNED, SESSION_LOG, handovers |
| Verification & defects | QA Engineer | KNOWN_ISSUES |
| Shipping | Release Manager | CHANGELOG, RELEASE_HISTORY |
| Unhomed observations | any role (lowest authority) | AI_NOTES |

In Minimal profile, collapsed roles inherit the ownership of the roles they absorb ([PROFILES.md](../operations/PROFILES.md)); the map's shape is unchanged.

## 4. Instance Header Standard

Per [FRAMEWORK_RULES.md](../core/FRAMEWORK_RULES.md) R5.2, every instance document opens with one H1 and this table (templates fix per-document values; they may add fields, never remove):

| Field | Content |
|---|---|
| ID | Governing standard's ID (K2.2) |
| Document | Instance filename |
| Class | `I — Snapshot` or `A — Ledger` |
| Profile-tier | `Minimal+`, `Standard+`, or `Full` |
| Owner | Owning role per §3 |
| Standard | Governing template version (e.g. `v1.0.0`) — migration anchor |
| Updated | `YYYY-MM-DD · S-YYYYMMDD-NN` (last write) |
| Status | Per R7.1; instance docs are ACTIVE from instantiation |

## 5. ID Counters

- **K5.1** Every document that homes a numbered entity ([FRAMEWORK_RULES.md](../core/FRAMEWORK_RULES.md) §4) maintains a `Next ID:` line in a fixed position (its template shows where). Assign, then increment — no scanning, no reuse, even after archiving.
- **K5.2** Counters never reset — including across ledger rotations and profile changes.

## 6. Knowledge Lifecycle

| Stage | Rule |
|---|---|
| **Creation** | At adoption, per profile ([ADOPTION_GUIDE.md](../operations/ADOPTION_GUIDE.md)): instantiate each active template's skeleton, fill initial content — never commit empty sections (P9, K2.1). Mid-life activation (profile upgrade) follows the same rule. |
| **Validation** | New knowledge is validated by its domain owner before it becomes load-bearing: facts marked unverified stay marked (Article IV) until checked. The knowledge-health audit is a session type ([WF_DOCUMENTATION.md](../workflows/WF_DOCUMENTATION.md)). |
| **Update** | Event-driven per [UPDATE_MATRIX.md](UPDATE_MATRIX.md), in the same session as the event (Article V), stamped per §4. |
| **Historical preservation** | Ledgers append-only; corrections are appended entries referencing the original (Article VII). Snapshots may drop superseded content only if a ledger holds it. |
| **Archiving** | §7. Archived content is preserved, indexed, excluded from default reading (T3). |
| **Deprecation** | An instance document type deactivated by profile change: content folds per the folding map, the file moves to `archive/` with a stub note. Never deleted. |
| **Deletion** | D3, always (Article VII). Recorded as a Decision Record plus an in-place tombstone note stating what was removed and under which D-NNN. |

## 7. Archiving Policy

- **K7.1** Instance archive lives at `.amf/archive/`. Nothing in it is read by default (T3); everything in it remains readable.
- **K7.2** **Ledger rotation.** When a ledger becomes unwieldy (guide: > ~400 lines or > ~40 entries — judgment, not dogma), rotate its oldest entries to `archive/<NAME>_<YYYY>.md`, leaving in place a stub index: entry-ID range, date range, link. Rotation preserves entries verbatim.
- **K7.3** **Snapshot section rotation.** Closed items in snapshots (resolved issues, answered questions, done tasks older than the last handover, closed risks) move to their document's archive file on the same pattern. Open items never rotate.
- **K7.4** Handovers rotate by age: all but the last ~10 sessions' files may move to `archive/handovers/` (the latest never rotates — it is T0).
- **K7.5** Rotation is an ordinary DOCUMENT-stage act by the document's owner, logged in the session log. Deletion is not rotation (§6).

## 8. Knowledge Quality Rules

- **K8.1** **Density.** Front-load load-bearing facts (P5); a reader of any document's header plus first section leaves with the truth. No filler, no restating what a linked document owns.
- **K8.2** **Freshness declared.** Every instance document states when it was last touched (§4 `Updated`); CURRENT_STATUS.md additionally states what it is current *as of* in content.
- **K8.3** **Honest gaps.** "Unknown", "not verified", "assumed — see ASSUMPTIONS" are first-class content (Article IV). Silence about a gap is a defect.
- **K8.4** **Entity discipline.** Every tracked thing has its ID and lives in its home document (R4.4); prose elsewhere references the ID.
- **K8.5** **No orphan knowledge.** Information with no obvious home goes to AI_NOTES with a suggested home — and AI_NOTES is periodically triaged (its standard defines the rule) so it never becomes a shadow knowledge base.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial system design: registry, ownership map, header standard, lifecycle, archiving, quality rules |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 4-5 | Swept Phase 4 forward reference (R8.3) |
| 1.0.2 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

- New knowledge domains: add a template + registry row + ownership row + matrix rows (extension point, D2). Expected first candidates from real use: PERFORMANCE_BUDGET, CONTENT_INVENTORY (client-site projects).
- K7.2 thresholds are deliberately judgment-based in v1.0; if tooling lands, they become lint warnings, not hard rules.
- If instances ever span multiple repositories, the registry needs a location column — additive.
