# Standard — HANDOVER

| Field | Value |
|---|---|
| ID | KNOW-25 |
| Document | templates/HANDOVER.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for per-session handover files (`sessions/handovers/S-*.md`) — the successor's starting point. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the handover: the artifact that makes session boundaries survivable — what a cold successor needs, prescribed exactly.
**Scope.** Structure and rules of handover files; not state description (CURRENT_STATUS) and not the session account (SESSION_LOG).
**Responsibilities.** Specification, structure, the stranger test operationalized, skeleton.
**Dependencies.** [SESSION_MANAGEMENT.md](../../core/SESSION_MANAGEMENT.md) Stage 7 (contract this implements).
**Consumers.** The next session (T0 read #4); WF_RECOVERY.
**Related documents.** templates/CURRENT_STATUS.md (division of labor: state vs. next actions), templates/SESSION_LOG.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E02.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/sessions/handovers/S-YYYYMMDD-NN.md` (one per session, named by R2.5) |
| Class | **A — Ledger** (each file written once, never edited; the set is the ledger) |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | **T0** (latest only); older handovers T3 |
| Profile | Minimal+ |
| Update triggers | E02 — every session end, no exception (Article VIII: no handover = interrupted) |
| Required inputs | True state of every piece of touched work; open risks; exact resumption knowledge |
| Expected outputs | A successor working productively without access to this session's conversation |
| Archive policy | K7.4 — all but last ~10 rotate to `archive/handovers/`; the latest never rotates |

## Structure

1. **Header** — session ID, date, workflow, outcome one-liner.
2. **Where work stands** — per touched task (T-NNN): exactly what is done, what is not, where the edge is. File paths and refs, not vibes.
3. **Next actions** — ordered, imperative, specific ("Run X, expect Y, then Z" — not "continue the feature"). The first action is the resumption point.
4. **Warnings** — traps the successor would otherwise rediscover: fragile areas, unverified changes, environmental quirks, half-truths in old docs pending E31 fixes.
5. **Worth re-reading** — the 1–3 references that most shaped this session (beyond the standard T1 row).
6. **Consistency confirmation** — explicit statement: update matrix applied, CURRENT_STATUS refreshed, no half-applied updates (or the exceptions, named).

**The stranger test, operationalized** (SESSION_MANAGEMENT Stage 7 exit): a competent cold session reading only T0 (which ends with this file) must be able to execute §3's first action without asking anything. Write §2–§4 for that reader: no references to "as discussed", no conversation-context, no unexplained abbreviations.

Rules: written once at Stage 7, never edited after (corrections belong to the next session's records); recovery-written handovers (on behalf of an interrupted session) are marked `**Reconstructed by:** S-...` in the header.

## Skeleton

```markdown
# Handover — S-YYYYMMDD-NN

- **Date:** <YYYY-MM-DD> · **Workflow:** <WF_*> · **Outcome:** <one line>

## Where work stands
- **T-NNN <title>:** <done: ... / not done: ... / edge: file:line, state>

## Next actions
1. <imperative, specific, verifiable>
2. ...

## Warnings
- <trap the successor would otherwise rediscover>

## Worth re-reading
- <ref — why>

## Consistency confirmation
Update matrix applied · CURRENT_STATUS refreshed · exceptions: <none | listed>
```

## Maintenance Notes

Quality bar: a short honest handover beats a long polished one written from a failing memory — which is why SESSION_MANAGEMENT §5 orders an abbreviated jump to HANDOVER when a hard stop approaches. The handover is the single highest-leverage artifact in AMF; when in doubt about what to include, include what *you* would curse a predecessor for omitting.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard: structure, stranger test operationalization |

## Future Extension Notes

If sessions gain budget declarations (SESSION_MANAGEMENT future note), handovers gain a budget-spent line — additive.
