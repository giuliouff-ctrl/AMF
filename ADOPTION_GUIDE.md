# Adoption Guide

| Field | Value |
|---|---|
| ID | OPRN-01 |
| Document | ADOPTION_GUIDE.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Release Manager (content) / Architect (structure) |
| Maintainer | Release Manager |
| Authority | Normative procedure for bringing a project under AMF, and the runtime adapter specification. Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Install AMF into a project — new or existing — so the first real session starts from a consistent instance; and define what any runtime must provide to host AMF.
**Scope.** Instantiation mechanics, the runtime adapter (Claude Code binding for v1.0), the discovery-method binding, adoption verification, a dry-run example. The full bootstrap *session* is [WF_NEW_PROJECT.md](../workflows/WF_NEW_PROJECT.md) — it calls this guide at its step 1.
**Responsibilities.** Prerequisites; instantiation steps; runtime adapter spec + Claude Code binding; discovery binding; verification checklist; dry-run.
**Dependencies.** [PROFILES.md](PROFILES.md), [KNOWLEDGE_SYSTEM.md](../knowledge/KNOWLEDGE_SYSTEM.md), templates/*, [VERSIONING.md §4](../core/VERSIONING.md) (pinning), [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) Stage 1 (what the bootstrap serves).
**Consumers.** Human Owner and Orchestrator at adoption; future runtime implementers.
**Related documents.** [WF_NEW_PROJECT.md](../workflows/WF_NEW_PROJECT.md), [ARCHIVING.md](ARCHIVING.md) (the other end of the lifecycle).
**Update policy.** D2 (Architect); the instance directory contract it instantiates is frozen for 1.x ([VERSIONING.md §6](../core/VERSIONING.md)).

---

## 1. Prerequisites

- A project directory (empty for greenfield; the existing tree for adoption of a running codebase — nothing in it is touched except adding `CLAUDE.md` and `.amf/`).
- The Owner available for: profile choice, discovery (WF_NEW_PROJECT step 2), and the founding constraints.
- A framework version to pin — normally the latest release.

## 2. Instantiation Steps

1. **Choose the profile** with the Owner ([PROFILES.md §4](PROFILES.md) guidance; when in doubt, one lighter). Configuration is D3-backed: the choice gets its D-NNN once DECISIONS exists (step 3 bootstraps the file; the record lands as D-001).
2. **Create the instance skeleton** (frozen contract, architecture §6.2):
   ```text
   <project>/
   ├── CLAUDE.md                      # bootstrap pointer (§3.2)
   └── .amf/
       ├── INSTANCE.md
       ├── knowledge/                 # active documents per profile
       ├── sessions/
       │   ├── SESSION_LOG.md
       │   └── handovers/
       └── archive/
   ```
3. **Instantiate each active document** from its template's Skeleton block (templates/*): header filled (`Standard: v<template version>`, `Updated` stamped with this session), `Next ID:` counters at 001, no empty content sections beyond what INSTANCE.md's design allows.
4. **Fill INSTANCE.md**: identity, `amf_version` pin, profile, role collapsing in effect (from [PROFILES.md §3](PROFILES.md)), active-documents checklist, `Deviations: None.`
5. **Write CLAUDE.md** per §3.2.
6. **Verify** per §6, then proceed with [WF_NEW_PROJECT.md](../workflows/WF_NEW_PROJECT.md) steps 2+ (discovery onward).

## 3. Runtime Adapter

### 3.1 What any runtime must provide

AMF is runtime-agnostic (AD-4); a runtime adapter is the thin binding that supplies:

1. **Bootstrap injection** — the hosted agent reads a project-root pointer file at session start, unprompted.
2. **File access** — read/write over the project tree and `.amf/`.
3. **Session boundary** — a discernible start and end, so the seven stages can anchor.
4. **Role execution** — at minimum sequential role assumption (single-instance topology); optionally parallel agents.

Nothing else. Anything a runtime adds (memory systems, tools, subagents) is welcome but never *required* by the framework.

### 3.2 Claude Code binding (v1.0 reference adapter)

Claude Code reads `CLAUDE.md` automatically — that file *is* the bootstrap. Canonical content:

```markdown
# <Project Name>

This project runs under AMF v<X.Y.Z> (AI Multi-Agent Framework).

**Every session starts here, then immediately:**
1. Read `.amf/INSTANCE.md` — profile, pinned framework version, active documents.
2. Follow the framework's session lifecycle: `<path-to-framework>/core/SESSION_MANAGEMENT.md`
   (seven stages; interruption check first — an unclosed session log entry means recovery).
3. Reading order and budget: `<path-to-framework>/knowledge/CONTEXT_RECONSTRUCTION.md`.

The framework is read-only during project work. Project truth lives in `.amf/knowledge/`.

## Project-specific runtime notes
<dev server commands, build caveats, machine constraints — runtime facts only;
 project knowledge belongs in .amf/knowledge/, not here>
```

Rules: `<path-to-framework>` is an absolute or workspace-relative path to the AMF repository; CLAUDE.md carries **runtime facts only** — the moment project knowledge appears here, Article III is violated (one home per fact: the instance). Claude Code subagents may map to roles (multi-instance topology) but the default binding is single-instance.

## 4. Discovery Binding (MADRE)

WF_NEW_PROJECT step 2 needs a discovery method. The Owner's standing method is **MADRE** (`Lavoro/MADRE/MADRE_v1.1.md`): batched questions with proposed defaults, must-know vs nice-to-have separation, standing stack defaults applied without asking. The binding:

- The Product Analyst runs MADRE's discovery blocks (identity, business & goals, constraints, scope level, branding, design direction, references, UX flow, structure, features, content model) as its E22 interview structure.
- MADRE's output maps: its `PROJECT.md` sections → the instance's PROJECT.md (goals, scope, constraints, success criteria) and ARCHITECTURE.md (stack, data model, media strategy — as the Architect's D2 inputs, not as decisions already made); its `AGENT_PROMPT.md` conventions → ARCHITECTURE §Conventions candidates; its standing stack (Section 9) → founding D2 defaults, still recorded as Decision Records (a default applied is still a decision made — Article VI).
- Where MADRE and AMF overlap (DoD-like checklists, decision logging), **AMF governs** — MADRE is the interview script, not a parallel authority (Article II).

## 5. Adopting an Existing Codebase

Steps 1–6 identical, plus: ARCHITECTURE.md is written by *reverse-engineering, verified against the tree* — unknowns marked unknown; KNOWN_ISSUES (or its fold) seeded honestly with what is already known broken; a WF_CODE_REVIEW audit seeded in the backlog ([WF_NEW_PROJECT.md](../workflows/WF_NEW_PROJECT.md) abort notes). The existing stack is recorded as founding constraints, not re-decided.

## 6. Adoption Verification Checklist

Binary, all must hold before the instance is declared live:

| # | Check |
|---|---|
| A.1 | Directory contract matches §2.2 exactly |
| A.2 | INSTANCE.md complete: pin, profile, collapsing, checklist matches the files on disk — no more, no fewer |
| A.3 | Every active document instantiated from its current template, header stamped, counters at 001 |
| A.4 | CLAUDE.md present, framework path resolves, no project knowledge smuggled in |
| A.5 | D-001 (profile/configuration) recorded |
| A.6 | First session-log entry open, adoption events logged (E27) |

## 7. Dry-Run — "Trattoria Da Mario" (Minimal, fictional)

The Phase 7 exit criterion, walked: a one-page restaurant site adopted at Minimal.

- **Instantiate**: 8 files — INSTANCE, PROJECT, ARCHITECTURE, CURRENT_STATUS, TASKS, DECISIONS, SESSION_LOG (+ `handovers/`). D-001: "Minimal profile — single-page site, one milestone" (Owner).
- **Discovery** (MADRE blocks, 15 minutes of Owner time): goals → PROJECT ("G1: diners find menu+hours+phone in one screen — success: call/visit conversions"); constraints → free hosting, no build step; backlog fold → PROJECT §Scope/Backlog ("P1: menu section; P1: contact+map; P2: photo strip").
- **Founding D2s** → DECISIONS: D-002 "single-file vanilla HTML/CSS/JS, no framework" (options considered: Astro, plain HTML — plain wins per constraints); ARCHITECTURE: one component, conventions (dark theme tokens in `:root`), invariants ("no external JS deps"), deploy (static host).
- **First feature session** (WF_FEATURE, all folds in action): task T-001 "menu section" from the PROJECT backlog fold; G0 criteria in the task row; G1 design = one logged paragraph, checked by Orchestrator (Minimal gate table); G2/G3+G4 merged check by Architect; issue found → I-001 in CURRENT_STATUS §Doesn't work; G5; handover.
- **Release**: G6 package to the Owner (scope, evidence, rollback = "restore previous index.html from git tag"); approval → D-003 carrying the change summary (RELEASE_HISTORY fold); CURRENT_STATUS §Health: "deployed <date>".

Every knowledge category exercised; zero documents beyond eight; the folds carried it. This is the shape a real Minimal adoption should feel like — if it feels heavier, something is being done wrong (P8).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 7 | Initial guide: instantiation, runtime adapter + Claude Code binding, MADRE binding, checklist, dry-run |

## Future Extension Notes

- A second runtime adapter splits §3 into `operations/adapters/` (architecture §14.2 — deliberately not before a second runtime is real).
- If MADRE versions move, only §4's mapping table needs review — the binding is by section role, not by wording.
