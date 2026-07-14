# Archiving

| Field | Value |
|---|---|
| ID | OPRN-05 |
| Document | ARCHIVING.md |
| Module | operations |
| Class | S — Stable spec |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Release Manager (content) / Architect (structure) |
| Maintainer | Release Manager |
| Authority | Normative procedure for retiring a project instance — ending work while preserving everything (Article VII applied to whole projects). Subordinate to [core](../core/AI_CONSTITUTION.md). |

---

## Document Contract

**Purpose.** End projects cleanly: open threads dispositioned honestly, a terminal record written, the whole memory preserved — so a retired project can answer questions (or come back) years later.
**Scope.** Instance retirement and reactivation. Deleting anything is out of scope by constitution (deletion is D3 and archiving exists precisely so it stays rare).
**Responsibilities.** The retirement procedure; the terminal-state definition; reactivation.
**Dependencies.** [AI_CONSTITUTION.md Article VII](../core/AI_CONSTITUTION.md), [KNOWLEDGE_SYSTEM.md §7](../knowledge/KNOWLEDGE_SYSTEM.md) (archive mechanics), [SESSION_MANAGEMENT.md](../core/SESSION_MANAGEMENT.md) (the final session is still a session).
**Consumers.** Orchestrator (executes), Human Owner (retirement is D3 — a project ends when its Owner says so).
**Related documents.** [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) (the other end), [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md) (reactivation may need one).
**Update policy.** D2 (Architect).

---

## 1. When

Retirement is a **D3**: delivered-and-handed-off client work, a shelved product, a superseded tool — the Owner decides; the framework executes. (Dormancy is not retirement: a project merely paused needs nothing — its handover chain already holds; retirement is for *ended*.)

## 2. The Retirement Procedure

One final session, run to the same standard as any other (Article VIII — the last session still gets a handover):

1. **Disposition every open entity, honestly**: tasks → DONE, returned-to-backlog-fold, or explicitly `abandoned (retirement, D-NNN)`; questions → answered or `expired`; risks → CLOSED with outcome; PENDING anything per P3.3. Nothing left OPEN-by-silence (Article IV — a retired project's registers state how things actually ended).
2. **Terminal CURRENT_STATUS**: rewritten one last time as the project's epitaph — final state, what shipped, what never did (§Doesn't work stays honest to the end), where deployments live and who owns them now.
3. **Retirement Decision Record**: D-NNN with the Owner's decision verbatim, the reason, and any surviving obligations (a client site still running, a domain renewal, a data-retention duty) — each surviving obligation with its named owner.
4. **Final handover, marked terminal**: `Outcome: project retired (D-NNN)`; next-actions section replaced by the surviving-obligations list; the stranger test still applies — its stranger is whoever reopens this in three years.
5. **INSTANCE.md**: status note `ARCHIVED (D-NNN, date)` appended to the header; pin left as-is (the pin records what rules governed this project — history, not configuration).
6. **Preserve everything in place**: `.amf/` stays with the project tree, whole — ledgers, handovers, archive/ and all. Retirement moves *nothing* and deletes *nothing*; it only closes.

## 3. Terminal State (definition)

An instance is properly retired when: every register's entries are in a closed state or explicitly abandoned with the D-ref; CURRENT_STATUS is terminal; the final handover is marked terminal; INSTANCE carries the ARCHIVED note. A retired instance failing any of these was abandoned, not retired — and reopening it starts with WF_RECOVERY, exactly as if a session had been interrupted (because one was: the project's last).

## 4. Reactivation

1. Treat the terminal handover as the resumption point (that's why it was written for the three-years stranger).
2. If the framework moved on: [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md) first — reactivation runs under a current pin or deliberately under the old one, but decides (E28 or a logged stay-pinned decision).
3. Remove the ARCHIVED note (E27 with its D-NNN — reactivation is as deliberate as retirement was); first working session re-baselines CURRENT_STATUS against reality (things rot while archived — the epitaph is a starting hypothesis, not a current truth; Article IV).

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 7 | Initial procedure: retirement, terminal state, reactivation |

## Future Extension Notes

If a cross-project lessons library lands (architecture §14.2), retirement gains a harvest step: the instance's LESSONS_LEARNED (or its fold) contributed to the library before closing. Designed-for; not yet built (P9).
