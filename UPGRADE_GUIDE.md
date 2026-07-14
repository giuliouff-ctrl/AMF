# Upgrade Guide

| Field | Value |
|---|---|
| ID | OPRN-03 |
| Document | UPGRADE_GUIDE.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Release Manager (content) / Architect (structure) |
| Maintainer | Release Manager |
| Authority | Normative procedure for migrating instances across framework versions, and the home of per-version migration notes. Applies the policy of [VERSIONING.md §8](../core/VERSIONING.md). Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** Make framework upgrades boring: a deliberate, verifiable, reversible procedure — never an implicit drift.
**Scope.** Instance migration procedure and the migration-notes register. Version *semantics* are [VERSIONING.md](../core/VERSIONING.md)'s; the session that executes upgrades is [WF_MAINTENANCE.md](../workflows/WF_MAINTENANCE.md)'s E28 path.
**Responsibilities.** The upgrade procedure; the migration-note format; the per-version register; verification.
**Dependencies.** [VERSIONING.md](../core/VERSIONING.md) (§4 pinning, §8 policy — cold-session-executable, rollback, never-between-versions), [WF_MAINTENANCE.md](../workflows/WF_MAINTENANCE.md).
**Consumers.** Orchestrator/Engineer during E28 sessions; the Architect when writing migration notes at release time.
**Related documents.** [PROFILES.md](PROFILES.md) (profile changes are not upgrades — different procedure).
**Update policy.** D2 (Architect); a new migration-notes section lands with every framework release that needs one (MAJORs always; MINORs when instances benefit from optional steps).

---

## 1. When to Upgrade

- Instances run their pinned version until upgrading is a deliberate choice ([VERSIONING.md §4](../core/VERSIONING.md)) — there is no obligation to chase releases.
- Worth upgrading when: a MINOR adds something the project will actually use; a PATCH fixes a rule the project keeps tripping on; a MAJOR — plan it like the structural change it is.
- MINOR-to-MINOR may skip versions; **MAJORs apply sequentially**, each with its migration (§4 register).

## 2. The Procedure

Runs as a [WF_MAINTENANCE.md](../workflows/WF_MAINTENANCE.md) session (E28 path); the whole upgrade is one session or it is rolled back (never between versions):

1. **Read** the migration notes (§4) for every version between the pin and the target.
2. **Snapshot the pin state**: note the current `amf_version` and touched-document versions in the session log — this is the rollback anchor.
3. **Apply** each version's steps in order, mechanically — the notes are written to be executable by a cold session inside the instance (P5; [VERSIONING.md §8](../core/VERSIONING.md)); each step's document updates stamped normally (R10.2).
4. **Bump the pin**: `amf_version` in INSTANCE.md (E28: INSTANCE, CHANGELOG line "framework upgraded to vX.Y.Z", SESSION_LOG).
5. **Verify** per §3.
6. On any failure → **rollback**: restore the anchor state (the instance's documents are files — revert them), pin unchanged, failure recorded; if the migration notes were wrong, that is a framework defect → Proposal (the notes get fixed before anyone else trips).

## 3. Post-Upgrade Verification

| # | Check |
|---|---|
| U.1 | `amf_version` matches the target; no document claims a `Standard:` version newer than its template at the target |
| U.2 | Every migration step's outcome present (the notes enumerate expected end-states — walk them) |
| U.3 | The instance passes an abbreviated WF_DOCUMENTATION consistency pass (steps 1–2 there): headers, stamps, links, entity refs |
| U.4 | A trivial next session can INITIALIZE cleanly (T0 reads resolve) |

## 4. Migration Notes Register

Format per entry (fixed): **What changed · Why · Steps (mechanical, ordered) · End-state checklist · Rollback specifics** — one entry per breaking or instance-relevant change, grouped by version, newest first.

### v1.0.0 — baseline

Initial release. No migrations exist or can exist (nothing precedes it). Instances adopted on 1.0.0 are the baseline population; the first entries land here with the first release that changes anything instance-visible.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 7 | Initial procedure, verification, empty register at baseline |

## Future Extension Notes

If tooling lands, §2 steps 3–4 become `amf upgrade` with §3 as its output — the notes register stays the human-readable source either way.
