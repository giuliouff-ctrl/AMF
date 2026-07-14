# Standard — DEPENDENCIES.md

| Field | Value |
|---|---|
| ID | KNOW-16 |
| Document | templates/DEPENDENCIES.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `DEPENDENCIES.md` — external components and services the project relies on. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the dependency inventory: everything external the project stands on — packages, services, platforms — with versions, constraints and reasons.
**Scope.** Structure and rules of `DEPENDENCIES.md`; not why a dependency was chosen (DECISIONS), not how it is wired (ARCHITECTURE §Integrations).
**Responsibilities.** Specification, structure, entry rules, skeleton.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4.
**Consumers.** Engineer (owner), WF_MAINTENANCE (T1 primary), Architect (constraint review).
**Related documents.** templates/ARCHITECTURE.md, templates/RISK_REGISTER.md; [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E12.
**Update policy.** D2 (Architect) for this standard.

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/knowledge/DEPENDENCIES.md` |
| Class | I — Snapshot |
| Knowledge domain | Implementation facts |
| Owner (role) | Engineer |
| Default read tier | T1 (WF_MAINTENANCE; WF_BUGFIX when dependency-related), T2 otherwise |
| Profile | Standard+ (Minimal: folds into ARCHITECTURE §Stack per the [folding map](../../operations/PROFILES.md)) |
| Update triggers | E12 (added/updated/removed) — same session as the change |
| Required inputs | Actual manifest state (package.json etc.); service accounts in use |
| Expected outputs | A maintenance-ready inventory: what to update, what never to touch blindly |
| Archive policy | Removed entries rotate to `archive/DEPENDENCIES_<YYYY>.md` with removal reason (K7.3) |

## Structure

1. **Header** — per standard.
2. **Packages** — table: name · version (pin) · purpose · constraint ("why this version / why pinned") · risk notes · license.
3. **Services** — table: service · plan/tier · purpose · limits that matter (quota, rate, storage) · account/owner · failure posture.
4. **Update policy** — the project's stance per dependency class: auto-update patch? hold majors? (project D2, D-ref).

Rules: mirrors the manifests, never replaces them — the package manifest is the implementation fact; this document adds *meaning* (purpose, constraint, risk) the manifest cannot carry. Divergence is E31 with the manifest presumed true. Free-tier limits that shape design (e.g. Firestore quotas) are recorded under Services *and* referenced from ARCHITECTURE — one sentence + link, the numbers live here.

## Skeleton

```markdown
# Dependencies — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-16 |
| Document | DEPENDENCIES.md |
| Class | I — Snapshot |
| Profile-tier | Standard+ |
| Owner | Engineer |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Packages
| Package | Version | Purpose | Constraint | Risk | License |
|---|---|---|---|---|---|

## Services
| Service | Tier | Purpose | Limits that matter | Account | On failure |
|---|---|---|---|---|---|

## Update policy
- <class>: <stance> (D-NNN)
```

## Maintenance Notes

WF_MAINTENANCE's home ground: the constraint column is what makes an update session safe — "pinned: v5 breaks App Router" saves the exact hour it took to learn. An empty constraint column on a pinned version is a question waiting.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

License compliance reporting (if client work demands it) would formalize the license column into a checked field — additive.
