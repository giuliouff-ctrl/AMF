# Agent Library

| Field | Value |
|---|---|
| ID | AGNT-10 |
| Document | AGENT_LIBRARY.md |
| Module | agents |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Normative mapping of the full engineering-organization surface onto AMF's seven roles: job-title mapping, the specialization mechanism, collaboration patterns, and the agent performance model. Subordinate to [AGENT_SYSTEM.md](AGENT_SYSTEM.md). |

---

## Document Contract

**Purpose.** Answer, completely, "where does agent X live in AMF?" — for every function a software organization has, from CEO to support engineer — without multiplying roles beyond the seven the architecture deliberately fixed.
**Scope.** Title mapping, specializations, collaboration patterns, performance model. Role contracts stay in `roles/`; the universal contract stays in [AGENT_SYSTEM.md §1](AGENT_SYSTEM.md) + [ROLE_TEMPLATE.md](ROLE_TEMPLATE.md).
**Responsibilities.** The mapping table; the specialization mechanism; pattern-to-workflow mapping; KPIs and the maturity note.
**Dependencies.** [AGENT_SYSTEM.md](AGENT_SYSTEM.md), the seven contracts, [WORKFLOW_INDEX.md](../workflows/WORKFLOW_INDEX.md), [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md).
**Consumers.** Anyone asking for a specialist ("we need a DevOps agent"); adopters comparing AMF to conventional org charts; the extension process (deciding mapping vs. new role).
**Related documents.** [ROLE_TEMPLATE.md](ROLE_TEMPLATE.md), [../AMF_ARCHITECTURE.md](../AMF_ARCHITECTURE.md) §9 (why seven).
**Update policy.** D2 (Architect); new mapping rows are the cheap change, new *roles* go through [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md).

---

## 1. The Design Position

A conventional software organization has dozens of job titles. AMF deliberately does not (architecture §9.1: fewer roles merges duties that must stay separated; more creates owners without territory). The resolution of that tension is this library's three mechanisms:

1. **Mapping** (§2) — most titles are *authority-equivalent* to one of the seven roles: a CTO and a Database Architect differ in specialty, not in the class of decisions they own. Titles map; authority doesn't multiply.
2. **Specialization** (§3) — where the difference is real expertise, a role runs *specialized*: `Engineer[frontend]`, `Architect[security]`. Same contract, same authority, declared domain lens.
3. **Extension** (§4) — where a genuine new territory with a genuine owner appears, the organization grows properly ([ROLE_TEMPLATE.md](ROLE_TEMPLATE.md) + [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md)) — never by informal manual.

## 2. Title Mapping

Every title of a conventional org, mapped. **Bold** = the authority home; notes state what the title adds as specialization or where it actually lives.

### 2.1 Executive & business

| Title | Maps to | Notes |
|---|---|---|
| CEO | **Human Owner** | Strategy, spending, scope — D3 territory is the executive suite, and it is human (Article I) |
| CTO / Engineering Director | **Architect** (+ Owner for strategy) | All D2 = the CTO's technical authority; strategic technology bets are D3 |
| Product Manager / Product Owner | **Product Analyst** | Same territory: goals, scope, backlog, stakeholder capture |
| Business Analyst | **Product Analyst**[analysis] | Requirements elicitation and assumption discipline are PA duties already |
| Project Manager / Scrum Master | **Orchestrator** | Planning, routing, unblocking, process integrity — the contract is a PM's |

### 2.2 Architecture & design

| Title | Maps to | Notes |
|---|---|---|
| Solution / Software / System Architect | **Architect** | The D2 monopoly is one seat by design |
| Cloud / Database / Security Architect | **Architect**[cloud \| data \| security] | Specializations; boundary-delegation is in the Architect contract's future notes |
| UI / UX Designer, UX Researcher | **Engineer**[design] for execution; **Product Analyst** for user goals; design *decisions* with structural weight are D2 | Flagged as the first real new-role candidate (UX Designer) in [AGENT_SYSTEM.md](AGENT_SYSTEM.md) future notes — pending evidence |

### 2.3 Engineering

| Title | Maps to | Notes |
|---|---|---|
| Tech Lead | **Engineer**[lead] + escalation posture | Technical leadership *within* a task cluster; cross-cutting calls stay D2 |
| Backend / Frontend / Full-stack / Mobile / API / Database / AI Engineer | **Engineer**[domain] | The contract is domain-agnostic by design; the specialty is a lens |
| Automation / Integration Engineer | **Engineer**[automation \| integration] | idem |

### 2.4 Quality & operations

| Title | Maps to | Notes |
|---|---|---|
| QA / Test Engineer | **QA Engineer** | Verification strategy and defect truth |
| Reviewer / peer reviewer | **Reviewer** | The independence seat |
| Security / Performance Engineer | **QA Engineer**[security \| performance] for verification; **Architect**[·] for design side | Two lenses on two existing seats |
| DevOps / SRE / Release Engineer | **Release Manager**[platform] + **Engineer**[infra] for build work | Ship-path ownership vs. pipeline implementation, split as authority splits |
| Documentation Engineer / Technical Writer | Every role for its own domain (P4: the record is part of the work) + **WF_DOCUMENTATION** as the dedicated session type | Documentation is constitutionally nobody's afterthought, so it is deliberately no one's exclusive job |

### 2.5 Growth & support

| Title | Maps to | Notes |
|---|---|---|
| Marketing / SEO / Copywriter | Not roles: **work types** — content and SEO tasks executed by **Engineer**[content \| seo] against goals the **Product Analyst** owns | Giving marketing *authority* seats would create owners without framework territory; their deliverables are tasks like any other |
| Customer Success / Community / Support Engineer | Inbound channel → **Product Analyst** (E22 capture) and **QA Engineer** (defect intake E13); support *work* is WF_BUGFIX / WF_MAINTENANCE | The org hears users through its existing ears |

## 3. Specialization Mechanism

- **L3.1** Syntax: `Role[specialty]`, logged exactly like any assumption (A2.1): `as Engineer[frontend]: T-042`.
- **L3.2** A specialization changes **expertise posture, never authority**: `Architect[security]` decides the same D2 class with a security lens — no new decision rights, no new ownership, no contract file.
- **L3.3** Specialties are free-form but stable per project: the instance's ARCHITECTURE §Conventions may name the ones in use; recurring cross-project specialties are glossary candidates.
- **L3.4** The test for "specialization vs. new role": does it need *ownership* (documents, domains, gates) that no current role holds? Ownership → [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md); expertise → a bracket.

## 4. Growing the Organization

The extension system (their creation, validation, registration, versioning, deprecation, compatibility, inheritance) is fully owned by [ROLE_TEMPLATE.md](ROLE_TEMPLATE.md) (form) + [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md) (process) + [VERSIONING.md §7](../core/VERSIONING.md) (experimental track, promotion on evidence). Inheritance is structural: every new role instantiates the universal contract shape (the five mandatory parts of [AGENT_SYSTEM.md §1](AGENT_SYSTEM.md)); "plug-in architecture" in AMF terms *is* the extension-point system (Article XII: no other plug mechanism exists).

## 5. Collaboration Patterns

Named patterns from conventional practice, mapped to what already executes them — patterns are workflow applications, not new machinery:

| Pattern | AMF execution |
|---|---|
| Pair programming | Single-instance topology *is* structured pairing: maker and checker roles alternating with logged assumption (A2.1–A2.4) |
| Parallel development | Multi-instance topology ([AGENT_SYSTEM.md §2.1](AGENT_SYSTEM.md)); per-document write serialization (M4.3) |
| Cross review | [WF_CODE_REVIEW.md](../workflows/WF_CODE_REVIEW.md) with non-authorship strictly applied |
| Architecture review board | [WF_ARCHITECTURE_REVIEW.md](../workflows/WF_ARCHITECTURE_REVIEW.md) (Architect audits, Reviewer independently checks the audit) |
| Release team | [WF_RELEASE.md](../workflows/WF_RELEASE.md): RM + QA + Orchestrator + Owner, each in contract |
| Incident response / hotfix team | [WF_BUGFIX.md](../workflows/WF_BUGFIX.md) with early Owner escalation (§5.1 triggers); dedicated WF_INCIDENT is the flagged future workflow |
| Research team | [WF_RESEARCH.md](../workflows/WF_RESEARCH.md) |
| Org-size presets (startup / SaaS / enterprise) | Profiles: Minimal ≈ startup trio, Standard ≈ product team, Full ≈ enterprise discipline ([PROFILES.md](../operations/PROFILES.md)) |

## 6. Performance Model

Measured from what the ledgers already record — no new bureaucracy (P9), no self-graded dashboards (Article IX's spirit):

| KPI | Read from |
|---|---|
| Context preservation | Recovery frequency (WF_RECOVERY sessions per N sessions — lower is better); stranger-test failures reported by successor sessions (E31) |
| Documentation quality | E31 density per session; G5 first-pass rate |
| Review quality | Defects found post-G4 that G3/G4 should have caught (escaped-defect count per release) |
| Delivery integrity | Gate first-pass rates; second-FAIL escalations (Q4.2 events) |
| Decision hygiene | Decisions reopened without new facts (should be zero); D-records with single options (Article XIII smell) |
| Error rate | I-NNN introduced per session, severity-weighted |

Continuous improvement is the existing loop: lessons (E26) → framework Proposals → MINOR releases ([VERSIONING.md §9](../core/VERSIONING.md)). An **agent maturity model** (graded capability levels) is deliberately deferred: it requires measurement history that does not exist yet — the KPIs above generate it (P9: evidence first).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 7 (Agent Library) | Initial library: full title mapping, specialization mechanism, collaboration patterns, performance model |

## Future Extension Notes

- The mapping table is expected to *promote* rows over time: when a bracket keeps needing its own territory (UX Designer is the flagged first), it graduates to a contract via the extension process — the row then points to the new role.
- The maturity model lands when two-plus projects of KPI history exist.
