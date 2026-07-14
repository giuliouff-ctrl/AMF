# Standard — INSTANCE.md

| Field | Value |
|---|---|
| ID | KNOW-04 |
| Document | templates/INSTANCE.md |
| Module | knowledge |
| Class | T — Template |
| Version | 1.0.1 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical standard for every instance's `INSTANCE.md` — the configuration root of a project under AMF. Subordinate to [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md). |

---

## Document Contract

**Purpose.** Define the standard for the instance configuration document: what binds a project to a framework version, a profile, and a document set.
**Scope.** Structure and rules of `INSTANCE.md`; not adoption procedure ([ADOPTION_GUIDE.md](../../operations/ADOPTION_GUIDE.md)).
**Responsibilities.** Specification, structure, skeleton, maintenance rules for INSTANCE.md.
**Dependencies.** [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4 (header standard), [VERSIONING.md](../../core/VERSIONING.md) §4 (pinning).
**Consumers.** Every session (T0 read #2); Orchestrator (writes); operations module.
**Related documents.** [UPDATE_MATRIX.md](../UPDATE_MATRIX.md) E27/E28, [PROFILES.md](../../operations/PROFILES.md).
**Update policy.** D2 (Architect); structure changes breaking instances are D3 (template class T rules).

## Specification

| Attribute | Value |
|---|---|
| Instance file | `.amf/INSTANCE.md` |
| Class | I — Snapshot |
| Knowledge domain | Planning & session accountability |
| Owner (role) | Orchestrator |
| Default read tier | **T0** (read #2, every session) |
| Profile | Minimal+ (always present) |
| Update triggers | E27 (configuration change — D3-backed), E28 (framework upgrade) |
| Required inputs | Profile choice and version pin from adoption; D-NNN refs for every change |
| Expected outputs | The session's binding configuration: rules version, profile, active documents |
| Archive policy | Never rotates; superseded configurations are visible via D-NNN records and E27/E28 log entries |

## Structure

1. **Header** — per [KNOWLEDGE_SYSTEM.md](../KNOWLEDGE_SYSTEM.md) §4.
2. **Identity** — project name, one-line description, adoption date, timezone (R1.3).
3. **Configuration** — `amf_version` pin; profile; experimental opt-ins (explicit, default none); topology (single-instance default).
4. **Role collapsing** — which roles are merged in this profile and who inherits what (from [PROFILES.md §3](../../operations/PROFILES.md)); "none" at Full.
5. **Active documents** — checklist of instantiated knowledge documents (must match profile; deviations forbidden without D3).
6. **Deviations** — approved deviations from framework defaults, each with its D-NNN. Empty section is stated as "None."

Rules: every change to §3–§6 requires a D-NNN reference (E27 is D3-backed); this is the only instance document allowed to state "None." explicitly for an empty section — its sections are configuration slots, not content (exception to the no-empty-sections rule, by design).

## Skeleton

```markdown
# Instance — <PROJECT NAME>

| Field | Value |
|---|---|
| ID | KNOW-04 |
| Document | INSTANCE.md |
| Class | I — Snapshot |
| Profile-tier | Minimal+ |
| Owner | Orchestrator |
| Standard | v1.0.0 |
| Updated | <YYYY-MM-DD> · <S-ID> |
| Status | ACTIVE |

## Identity
- **Project:** <name> — <one-line description>
- **Adopted:** <YYYY-MM-DD> · **Timezone:** <tz>

## Configuration
- **amf_version:** <X.Y.Z>
- **Profile:** <Minimal | Standard | Full>
- **Experimental opt-ins:** None.
- **Topology:** single-instance

## Role collapsing
<per profile, or "None (Full profile).">

## Active documents
<checklist per profile>

## Deviations
None.
```

## Maintenance Notes

The gatekeeper document: if INSTANCE.md disagrees with reality (documents present that aren't listed, profile that doesn't match practice), the instance is misconfigured — E31, fix before work. Keep it short; it is read every single session.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 2 | Initial standard |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |

## Future Extension Notes

Multi-repository projects would add a Locations section (registry note in KNOWLEDGE_SYSTEM). Runtime-adapter-specific settings belong in CLAUDE.md, never here.
