# Profiles

| Field | Value |
|---|---|
| ID | OPRN-02 |
| Document | PROFILES.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Release Manager (content) / Architect (profiles design) |
| Maintainer | Release Manager |
| Authority | Normative definition of the three adoption profiles: active documents, collapsed roles, gate execution, and the complete folding map. Applies AD-2 within the constraints of [AGENT_SYSTEM.md §8](../agents/AGENT_SYSTEM.md) and [QUALITY_SYSTEM.md §5](../quality/QUALITY_SYSTEM.md) — it may never relax them. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Make AMF honest at every project size: define exactly what Minimal, Standard and Full activate — and where every folded document's content lives, so no knowledge category is ever unsupported (AD-2's promise).
**Scope.** Profile definitions, folding map, role collapsing application, per-profile gate tables, profile changes. Constraints it applies are owned elsewhere (C8, Q5) and cited, never restated.
**Responsibilities.** The three profiles; the folding map; collapsed-role gate assignments; selection guidance; upgrade/downgrade procedures.
**Dependencies.** [KNOWLEDGE_SYSTEM.md §2](../knowledge/KNOWLEDGE_SYSTEM.md) (registry with profile column), [AGENT_SYSTEM.md §8](../agents/AGENT_SYSTEM.md) (C8 constraints), [QUALITY_SYSTEM.md §5](../quality/QUALITY_SYSTEM.md) (Q5 merging), templates/* (each declares its own fold — this map consolidates them).
**Consumers.** Orchestrator at adoption and profile changes; every session (INSTANCE.md declares the active profile); [UPDATE_MATRIX.md](../knowledge/UPDATE_MATRIX.md) M5.2 (fold-target resolution).
**Related documents.** [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md), [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md).
**Update policy.** D2 (Architect); new profiles are an extension point; changing what an existing profile means for existing instances is D3.

---

## 1. The Three Profiles

| | **Minimal** | **Standard** | **Full** |
|---|---|---|---|
| For | Small sites, single-file apps, temporary projects | Client apps, WMS-class tools, anything maintained for months | Long-running platforms, multi-milestone products |
| Instance documents | 8 | 14 | 22 |
| Roles | 3 (collapsed per §3) | 5 | 7 |
| Gate execution | G3+G4 merged (Q5.1); full chain otherwise | Full chain | Full chain |
| Owner touchpoints | Identical everywhere: D3, G6, escalations (C8.5) | idem | idem |

Document activation per profile: the authoritative per-document column is [KNOWLEDGE_SYSTEM.md §2](../knowledge/KNOWLEDGE_SYSTEM.md); in summary — **Minimal**: INSTANCE, PROJECT, ARCHITECTURE, CURRENT_STATUS, TASKS, DECISIONS, SESSION_LOG, handovers. **Standard** adds: BACKLOG, ROADMAP, CHANGELOG, KNOWN_ISSUES, DEPENDENCIES, RELEASE_HISTORY. **Full** adds: TECHNICAL_DEBT, RISK_REGISTER, ASSUMPTIONS, OPEN_QUESTIONS, RESEARCH, MEETING_NOTES, LESSONS_LEARNED, AI_NOTES.

## 2. The Folding Map

The rule behind every row: **granularity folds, categories never drop** (P8). Entity IDs survive folding unchanged (R4.3); the E-code obligation is identical, targeting the folded location (M5.2). Each row matches the fold its template declares.

### 2.1 Absent at Minimal (present from Standard)

| Folded document | Content lives in | Notes |
|---|---|---|
| BACKLOG | PROJECT §Scope → subsection **Backlog** | Same three bands, same promotion rule (E03) |
| ROADMAP | PROJECT §Scope → milestone lines | "Reached means" still defined at creation |
| CHANGELOG | CURRENT_STATUS §Recent (user-visible lines marked) | At release, the G6 Decision Record carries the release's change summary |
| KNOWN_ISSUES | CURRENT_STATUS §Doesn't work, with I-NNN IDs kept | Severity vocabulary unchanged; CRITICAL still announces itself |
| DEPENDENCIES | ARCHITECTURE §Stack, gaining constraint/risk notes per entry | E12 targets the Stack table |
| RELEASE_HISTORY | The release's **G6 Decision Record** (D-NNN: scope, evidence refs, rollback path) + CURRENT_STATUS §Health deploy line | DECISIONS is append-only, so the audit-trail property survives the fold |

### 2.2 Absent at Minimal and Standard (present at Full)

| Folded document | Content lives in | Notes |
|---|---|---|
| TECHNICAL_DEBT | ARCHITECTURE → short **Debt** note adjacent to §Invariants | Entry fields compressed to one line each; D-NNN + trigger still mandatory (E24) |
| RISK_REGISTER | CURRENT_STATUS §Blocked/waiting, R-NNN lines | H/H risks still flag to the Owner |
| ASSUMPTIONS | Inline `assumed (A: …)` marks at the point of use + a **Assumptions** list in PROJECT §Constraints for load-bearing ones | Falsifiability rule unchanged; E18 invalidation still walks the lean-on refs |
| OPEN_QUESTIONS | CURRENT_STATUS §Blocked/waiting, Q-NNN lines; Owner-routed grouped | Routing mandatory as ever |
| RESEARCH | Findings land directly in the D-record or document they serve, with method noted in the Decision Record's rationale | The read-before duty shifts to the DECISIONS index |
| MEETING_NOTES | E22 conditionals applied directly (PROJECT/backlog-fold edits) with session refs; decision-bearing statements near-verbatim inside the D-record | Article I verbatim rule is profile-independent |
| LESSONS_LEARNED | SESSION_LOG entry lines marked **LESSON:** (L-NNN kept) | Harvestable for framework evolution exactly the same |
| AI_NOTES | SESSION_LOG one-liners marked **NOTE:** with suggested home | Triage duty rides WF_DOCUMENTATION unchanged |

## 3. Role Collapsing Applied

Canonical absorption per [C8.1](../agents/AGENT_SYSTEM.md); inheritance is total (C8.2 — ownership, E-codes, gates, escalation duties).

**Standard (5):** Orchestrator (+Product Analyst) · Architect · Engineer · Reviewer (+QA Engineer) · Release Manager.
**Minimal (3):** Orchestrator (+Product Analyst +Release Manager) · Architect (+Reviewer/QA functions) · Engineer.

Per-profile gate tables — each row satisfies C8.3 (checker ≠ author), C8.4 (Engineer never absorbs a check on its own code), C8.5 (G6 untouched):

| Gate | Full | Standard | Minimal |
|---|---|---|---|
| G0 | PA declares, Architect confirms | Orchestrator(PA) declares, Architect confirms | Orchestrator declares, **Architect confirms and checks** |
| G1 | Architect → Reviewer | Architect → Reviewer | Architect → **Orchestrator** (the C8.3 cross-check) |
| G2 | Engineer self + evidence | idem | idem |
| G3 | Reviewer | Reviewer(+QA) | **Architect** (merged G3+G4, both checklists, both recorded — Q5.3) |
| G4 | QA Engineer | Reviewer(+QA) | merged as above |
| G5 | Release Manager | Release Manager | Orchestrator(RM) authors → **Architect checks** |
| G6 | Human Owner | Human Owner | Human Owner |

## 4. Selection Guidance

- Default for doubt: **one profile lighter, upgrade on evidence** (P8; WF_NEW_PROJECT abort note). Signals you outgrew Minimal: folded sections dominating their host documents; issue lines crowding CURRENT_STATUS; a real release cadence. Signals for Full from day one: multiple milestones promised, risk exposure the Owner asks about, months-long horizon.
- Profile ≠ quality. The Constitution, the DoD and G6 are identical at every profile — Minimal is *less paper*, never *less true*.

## 5. Profile Changes

**Upgrade (e.g. Minimal → Standard)** — routine, run inside WF_MAINTENANCE:
1. E27 with its D-NNN (configuration change).
2. **Unfold**: instantiate each newly active document from its template and *move* the folded content into it (IDs unchanged); the folded section shrinks to a pointer for one session, then disappears.
3. INSTANCE.md updated (profile, active-documents checklist); G5.

**Downgrade** — D3 (Owner decides; it usually signals the project winding down): fold per §2 in reverse, nothing deleted (Article VII — full documents move to `archive/` with stubs after their content folds).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 7 | Initial profiles: definitions, complete folding map, gate tables, change procedures |

## Future Extension Notes

- The folding map is the framework's most evidence-hungry surface (flagged since AD-2): expect MINOR tuning from the first Minimal-profile projects — CURRENT_STATUS §Recent as a changelog fold is the row to watch.
- A fourth profile (e.g. "Solo" below Minimal) only if real single-evening projects demand it — P9 says not yet.
