# Role Template

| Field | Value |
|---|---|
| ID | AGNT-02 |
| Document | ROLE_TEMPLATE.md |
| Module | agents |
| Class | S — Stable spec |
| Version | 1.1.0 |
| Status | ACTIVE |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Canonical template for defining new role contracts. Subordinate to [AGENT_SYSTEM.md](AGENT_SYSTEM.md). |

---

## Document Contract

**Purpose.** Make the organization extensible without amendment: the fixed form a new role contract must take, and the integration duties its creation triggers.
**Scope.** New roles only; modifying the seven v1.0 roles is D3 (compatibility promise, [VERSIONING.md §6](../core/VERSIONING.md)).
**Responsibilities.** The contract skeleton; the integration checklist.
**Dependencies.** [AGENT_SYSTEM.md](AGENT_SYSTEM.md) (the system a new role must fit), [FRAMEWORK_GOVERNANCE.md §7](../core/FRAMEWORK_GOVERNANCE.md) (extension boundary).
**Consumers.** Architect, when extending the organization (D2, Owner informed per the approval matrix).
**Related documents.** roles/* (the seven exemplars), [AGENT_LIBRARY.md](AGENT_LIBRARY.md) (mapping vs. new-role test, §3.4 there), [EXTENDING_AMF.md](../operations/EXTENDING_AMF.md).
**Update policy.** D2 (Architect).

## Integration Checklist

A new role does not exist until every box is closed — a contract file alone is shadow structure (Article XII):

1. Contract written from the skeleton below, all five mandatory parts filled (identity, ownership, authority, prohibitions, escalation duties — [AGENT_SYSTEM.md §1](AGENT_SYSTEM.md)).
2. Ownership: new knowledge domains (if any) added to [KNOWLEDGE_SYSTEM.md §3](../knowledge/KNOWLEDGE_SYSTEM.md) — no overlap with existing owners; new documents get templates + registry rows.
3. Update matrix: E-code rows added or reassigned for what this role records.
4. Gate authority: [AGENT_SYSTEM.md §4](AGENT_SYSTEM.md) map amended if the role authors or checks any gate (Article IX invariant preserved).
5. Escalation: matrix rows added where the role is a route; §1 roster row added.
6. Profiles: collapsing behavior defined — which role absorbs this one at Standard/Minimal (C8 constraints).
7. Glossary entry; AGNT-NN ID assigned (R3.4); Manifest registry ([AMF_MANIFEST.md](../AMF_MANIFEST.md)).

## Contract Skeleton

```markdown
# Role — <NAME>

| Field | Value |
|---|---|
| ID | AGNT-NN |
| Document | roles/<NAME>.md |
| Module | agents |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | DRAFT |
| Owner | Architect |
| Maintainer | Architect |
| Authority | Contract for the <Name> role. Subordinate to [AGENT_SYSTEM.md](../AGENT_SYSTEM.md). |

## Document Contract
<the seven fields, per R6.1>

## Identity
<who this role is; its professional mindset; what it optimizes for; in one line, what the org loses if it is absent>

## Ownership
<knowledge domains and documents owned — cite KNOWLEDGE_SYSTEM §3; E-codes recorded; work artifacts owned>

## Authority
<decision classes it exercises in its territory; gates authored/checked per AGENT_SYSTEM §4; what it may declare>

## Responsibilities
<duties per session stage and per workflow involvement; ongoing duties>

## Prohibitions
<hard nevers — each traceable to an article or a system rule>

## Escalation Duties
<when this role MUST escalate; to whom; what it must never sit on>

## KPIs
<how this role's health is read from the ledgers — per AGENT_LIBRARY.md §6's model; measurable, no self-grading>

## Anti-patterns
<the failure modes specific to this role, named — each traceable to the article or rule it violates>

## Assumption Notes
<single-instance: when sessions typically assume it; special re-read duties, if any>

## Revision History / Future Extension Notes
<per R6.2>
```

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 3 | Initial template + integration checklist |
| 1.0.1 | 2026-07-12 | Architect (AI), Phase 8 | Swept Phase 6-8 forward references to live links (R8.3) |
| 1.1.0 | 2026-07-12 | Architect (AI), Phase 7 (Agent Library) | Skeleton gains KPIs and Anti-patterns sections (Phase 7 universal-contract fields); library cross-ref |

## Future Extension Notes

[EXTENDING_AMF.md](../operations/EXTENDING_AMF.md) wraps this template in the full procedure (proposal → integration → activation); this file stays the *form*, that one the *process*.
