# Certification

| Field | Value |
|---|---|
| ID | OPRN-08 |
| Document | CERTIFICATION.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect (protocol) / Human Owner (certification grants) |
| Maintainer | Architect |
| Authority | Normative protocol for proving AMF in the field: the reference-implementation mandate, the compliance evidence model, and the certification levels. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Turn "documented" into "proven" honestly: define what field validation of AMF means, how a reference implementation runs, what evidence certifies each component, and what v1.0.0's certification status actually is (Article IV applies to the framework's claims about itself).
**Scope.** Field validation. Static validation is [FRAMEWORK_AUDIT.md](FRAMEWORK_AUDIT.md)'s (the two are the halves of "proven").
**Responsibilities.** Certification levels; the reference-implementation mandate; the compliance evidence model; component validation criteria; the v1.0.0 statement.
**Dependencies.** [FRAMEWORK_AUDIT.md](FRAMEWORK_AUDIT.md), [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md), [AGENT_LIBRARY.md §6](../agents/AGENT_LIBRARY.md) (the KPIs the evidence feeds), all workflows (the procedures under test).
**Consumers.** Human Owner (grants certification, picks the reference project); Architect (runs the protocol); future adopters (reading the certification status before trusting the framework).
**Related documents.** [VERSIONING.md §9](../core/VERSIONING.md) (evidence-driven roadmap — certification findings are its richest source).
**Update policy.** D2 (Architect); level definitions are stable, findings sections append per certification run.

---

## 1. Certification Levels

Honest, cumulative, per framework version:

| Level | Meaning | Evidence required |
|---|---|---|
| **C0 — Audited** | Statically consistent: all V1–V10 checks pass, judgment audits clean | [FRAMEWORK_AUDIT.md](FRAMEWORK_AUDIT.md) record |
| **C1 — Exercised** | Every mandatory workflow and every instance-document standard has executed at least once in a real project | The reference implementation's instance (§2) |
| **C2 — Proven** | A real project ran start-to-release under the framework with zero unrecorded deviations, and its post-release review found the framework helped more than it cost | Full compliance record (§3) + Owner's post-release judgment |
| **C3 — Hardened** | ≥3 projects across ≥2 profiles; KPI history exists; at least one framework MINOR shipped from harvested evidence | Aggregated usage audit |

A version's certification level is stated in the Manifest and never claimed above its evidence (Article IV).

## 2. The Reference Implementation Mandate

Field validation is a real project, not a staged demo — a fabricated "reference run" would certify nothing and violate the framework's own honesty rules. Therefore:

- **R2.1** The reference implementation is the **Owner's next real project** adopted under AMF (client site, WMS, tool — whatever reality supplies). Realism is the point; size selects the profile, and a Minimal-profile reference is a valid C1 (it exercises the folding map, which is the riskiest surface).
- **R2.2** The reference project runs AMF **exactly as written** — nothing bypasses the framework. Where the framework fails the project, the project does not silently improvise: the deviation protocol (§3.2) captures it. The framework bends *afterward*, through the loop.
- **R2.3** Every session of the reference project is also a measurement (§3.1) — at zero extra cost, because the evidence *is* the instance's normal records.
- **R2.4** Successive projects extend coverage toward C2/C3; the certification record (§5) appends per run.

## 3. Compliance Evidence Model

### 3.1 What the instance already proves

The evidence for every brief-level validation question is the instance itself — by design, no separate instrumentation:

| Validation target | Evidence source |
|---|---|
| Workflow effectiveness (clarity, recovery, coordination) | SESSION_LOG per workflow: first-pass completions, abort-path activations, WF_RECOVERY frequency |
| Knowledge continuity / context reconstruction | Stranger-test outcomes at each session start; E31 density; C4.5 findings |
| Agent/role validation (decision quality, review quality, documentation) | [AGENT_LIBRARY.md §6](../agents/AGENT_LIBRARY.md) KPIs read from DECISIONS (single-option smell, reopenings), Review Reports (escaped defects), gate records |
| Decision traceability | Every structural change traces to its D-NNN (V-check sampling on the instance) |
| Documentation quality | G5 first-pass rate; WF_DOCUMENTATION findings |
| Scalability / usability | Profile friction: folding-map pain points, reading-budget overruns (logged deviations) |

### 3.2 Deviation protocol

When the framework and reality collide, the reference project records — never hides — the collision:

1. The deviation is logged where it happens (session log, marked `DEVIATION:`) with what rule/procedure failed the situation and what was done instead.
2. It lands as a lesson (E26) with the framework document it implicates.
3. At harvest, each deviation becomes a Proposal or an explicit "framework was right, execution was wrong" finding — both are certification evidence.

**Zero deviations recorded ≠ perfect framework; it means nobody looked** (Article XIII). A credible C2 record contains deviations and their dispositions.

### 3.3 Post-release review

After the reference project's first G6 release: a retrospective session ([PLAYBOOK_INDEX.md §3.4](PLAYBOOK_INDEX.md)) answering, for the record: did the framework make this project more predictable, maintainable and resumable than it would have been — at a process cost the project could afford? The Owner's answer, verbatim, closes the C2 evidence.

## 4. v1.0.0 Certification Statement

Honest status at release (2026-07-13):

- **C0 — Audited: GRANTED.** V1–V10 executed at release: 0 broken links, 0 stale markers, 0 duplicate IDs, registry consistent with headers, headers conformant, ownership total with zero overlaps, workflow/message/E-code coverage total. Judgment audits (duplication, terminology, proportionality) performed during Phase 8 integration; findings fixed in-line (recorded in the revision histories).
- **C1–C3: PENDING.** No project has yet run under AMF. The framework is *designed and audited*, not yet *field-proven* — and says so. The paper dry-run ([ADOPTION_GUIDE.md §7](ADOPTION_GUIDE.md)) is orientation, not evidence.
- **Next step:** R2.1 — the Owner's next real project adopts AMF v1.0.0 as the reference implementation; its harvest drives v1.1.

## 5. Certification Record

Append-only; one entry per certification event.

| Date | Version | Level | Evidence | Granted by |
|---|---|---|---|---|
| 2026-07-13 | 1.0.0 | C0 | Release audit record (V1–V10 pass; Phase 8 integration audits) | Human Owner (release approval) |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-13 | Architect (AI), Phase 10 (Reference Implementation & Certification) | Initial protocol: levels, reference mandate, evidence model, honest v1.0.0 statement |

## Future Extension Notes

- The C1 entry lands when the first reference project completes; §5 rows and §4 are the only sections expected to change between framework versions.
- If AMF is ever published for third parties, C-levels become the public trust signal — designed for that from day one.
