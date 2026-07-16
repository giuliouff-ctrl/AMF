# Framework Audit

| Field | Value |
|---|---|
| ID | OPRN-07 |
| Document | FRAMEWORK_AUDIT.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.1.1 |
| Status | ACTIVE |
| Owner | Architect (audit design) / Release Manager (execution cadence) |
| Maintainer | Architect |
| Authority | Normative for the framework auditing itself: validation checks, audit catalog, cadence, and the evolution loop that keeps AMF consistent across releases. Governance authority remains [FRAMEWORK_GOVERNANCE.md](../core/FRAMEWORK_GOVERNANCE.md); this document is its inspection arm. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Keep the framework as honest as it demands its projects to be: objective, evidence-based procedures for validating and auditing AMF itself, and the formalized loop by which findings become releases.
**Scope.** Framework-level validation and audit. *Instance* audits are [WF_DOCUMENTATION.md](../workflows/WF_DOCUMENTATION.md)'s; *who approves* changes is the [governance matrix](../core/FRAMEWORK_GOVERNANCE.md)'s; *version semantics* are [VERSIONING.md](../core/VERSIONING.md)'s.
**Responsibilities.** Governance-structure mapping; the validation check set; the audit catalog; the release audit gate; the evolution loop.
**Dependencies.** [FRAMEWORK_GOVERNANCE.md](../core/FRAMEWORK_GOVERNANCE.md), [VERSIONING.md](../core/VERSIONING.md), [SCHEMA_REGISTRY.md §4](../SCHEMA_REGISTRY.md) (validation taxonomy the checks instantiate), [AMF_MANIFEST.md](../AMF_MANIFEST.md) (registry under audit).
**Consumers.** Architect (runs audits), Release Manager (release gate), Human Owner (audit outcomes at release approval).
**Related documents.** [CERTIFICATION.md](CERTIFICATION.md) (field validation — the other half of proving the framework), [PLAYBOOK_INDEX.md](PLAYBOOK_INDEX.md).
**Update policy.** D2 (Architect); new checks/audits are the expected additive change.

---

## 1. Governance Structure (mapped, not multiplied)

The brief-level boards (governance board, architecture board, standards committee, quality board, release authority, audit authority) map onto the existing authority structure — the same consolidation argument as [AGENT_LIBRARY.md §1](../agents/AGENT_LIBRARY.md): committees without independent authority would be theater.

| Board function | Held by |
|---|---|
| Framework Owner | **Human Owner** (Article I) |
| Governance / architecture / standards authority | **Architect** within the [approval matrix](../core/FRAMEWORK_GOVERNANCE.md); Owner above it |
| Quality authority | QA Engineer (content) / Architect (model) — the quality module's own ownership |
| Release authority | Release Manager executing; **Owner approving** (G6) |
| Audit authority | Architect designs and runs; findings route through governance — **the Architect never approves fixes to its own audit findings above D1** (Article IX applied to the framework itself: the Owner sees the audit record at release) |
| Review frequency | §4 cadence |

## 2. Validation Checks (machine-checkable)

The framework's invariants, each an instance of the [SCHEMA_REGISTRY.md §4](../SCHEMA_REGISTRY.md) taxonomy. All are **executable now** via `python3 tools/amf-lint.py` — the shipped validator that implements V1–V11 (AD-7 realized):

| # | Check | Kind | Pass criterion |
|---|---|---|---|
| V1 | Every cross-reference resolves (code fences excluded) | Reference | Zero broken links |
| V2 | No stale forward markers: `(Phase N)` absent outside revision histories | Reference | Zero markers |
| V3 | Document IDs unique, grammar-conformant (R3) | Identity | Zero duplicates/violations |
| V4 | Headers complete and field-ordered (R5.1) | Presence | Every framework file conformant |
| V5 | Contract + footer sections present (R6.1–6.2) | Presence | idem |
| V6 | Registry ↔ header consistency (Manifest §4 vs. files) | Integrity | Zero mismatches |
| V7 | Status values from the closed vocabulary; only legal transitions in histories | Vocabulary | Zero violations |
| V8 | Ownership uniqueness: every document exactly one Owner row ([GOVERNANCE §3](../core/FRAMEWORK_GOVERNANCE.md)); every knowledge domain exactly one owner ([KNOWLEDGE_SYSTEM §3](../knowledge/KNOWLEDGE_SYSTEM.md)) | Integrity | Zero orphans, zero overlaps |
| V9 | Every workflow has its reading row (C3.3) and its index row; every message type has all format rows; every E-code cited exists in the matrix | Integrity | Total coverage |
| V10 | Version sanity: revision history's last row matches the header version | Integrity | Zero mismatches |
| V11 | No reserved-term synonyms in normative text (glossary R1.4; e.g. *handoff* for *handover*) | Vocabulary | Zero collisions |

Failure of any check is a framework defect: D1/D2 fix by the responsible Maintainer, recorded normally.

## 3. Audit Catalog (judgment audits)

What scripts cannot check. Each audit: run by the Architect, findings recorded, dispositions through governance.

| Audit | Question | Evidence examined |
|---|---|---|
| **Architecture consistency** | Do the modules still respect the frozen design (layers, AD-1..10)? Has any document quietly acquired a second responsibility? | Dependency direction sampling; contract Scope sections vs. content |
| **Duplication** | Has any fact grown a second home (Article III)? | Cross-module reading of overlapping topics (statuses, gates, roles) |
| **Terminology** | Is the glossary still total — no term used normatively without an entry (R1.4)? | New-term scan vs. glossary |
| **Proportionality** | Is anything bloating (K8.1 for the framework itself)? Are Minimal-profile promises still honest (P8)? | Document growth between releases; folding map vs. template statements |
| **Usage** (once instances exist) | What do the ledgers say: recovery frequency, gate failure patterns, E31 density, lesson themes ([AGENT_LIBRARY.md §6](../agents/AGENT_LIBRARY.md) KPIs) | Instance ledgers, aggregated |

## 4. Cadence and the Release Audit Gate

- **Every framework release** (any MAJOR/MINOR): `python3 tools/amf-lint.py` must exit clean, and the audit record (its output plus any judgment-audit findings and dispositions) is part of the release package the Owner approves — **no release ships red**, mirroring G5/G6 at framework level.
- **Usage audit**: at release planning, over whatever instances exist (§3 last row) — it *is* the evidence-gathering step of the evolution loop.
- **Judgment audits** (§3 first four): at every MAJOR, and whenever a violation pattern suggests drift.
- PATCH releases: V1–V11 only.

## 5. The Evolution Loop (formalized)

One loop, already constitutionally plumbed — this section fixes its operating order:

1. **Capture** — instance lessons (E26), framework Proposals ([MESSAGE_TYPES.md §2.9](../communication/MESSAGE_TYPES.md)), audit findings (§2–3), Future Extension Notes across all documents.
2. **Harvest** — at release planning, the Architect aggregates all four sources ([VERSIONING.md §9](../core/VERSIONING.md)).
3. **Decide** — through the [approval matrix](../core/FRAMEWORK_GOVERNANCE.md): extensions D2, amendments D3; experimental for the unproven ([VERSIONING.md §7](../core/VERSIONING.md)).
4. **Ship** — versioned per [VERSIONING.md](../core/VERSIONING.md), migrations per [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md), audited per §4.
5. **Close the loop** — instances upgrade deliberately; their next lessons feed step 1.

Change classes (minor/major/breaking/emergency) map to the existing matrix; "emergency changes" get no special lane — a framework defect blocking real work is a PATCH/MINOR through the same gates, expedited by priority, not by skipped review (Article X does not have emergencies).

## 6. Declined Scope (recorded deliberately)

From the phase brief, declined with reasons (P9/P10 — revisit on evidence):
- **LTS / preview release channels** — one release line is all v1.x needs; channels multiply migration surfaces for zero current users.
- **Standing committees with review calendars** — cadence is event-driven (§4) at this scale; calendars are theater without teams.
- **Framework performance metrics dashboards** — the KPI *sources* exist (ledgers); dashboards are tooling-era work.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-13 | Architect (AI), Phase 9 (Governance, Validation, Audit & Evolution) | Initial audit system: V1–V10 checks, audit catalog, release gate, evolution loop |
| 1.1.0 | 2026-07-16 | Architect (AI), v1.1.0 | V1–V10 now shipped as tools/amf-lint.py; release gate names the command |
| 1.1.1 | 2026-07-16 | Architect (AI), v1.1.0 self-review | Added V11 (reserved-term guard); strengthened V8 (domain-ownership uniqueness) and V9 (message-type coverage) in the shipped linter |

## Future Extension Notes

- V1–V11 shipped as `tools/amf-lint.py` (v1.1.0–1.1.1); §4's release gate is a single command, CI-ready. Judgment audits (§3) remain human. New machine-checkable invariants become V-checks; V11 was promoted from the terminology judgment audit after it caught a real regression.
- The usage audit grows into the metrics program (architecture §14.2) as instance history accumulates; the maturity model ([AGENT_LIBRARY.md §6](../agents/AGENT_LIBRARY.md)) lands on the same evidence.
