# AMF — AI Multi-Agent Framework

| Field | Value |
|---|---|
| ID | ROOT-02 |
| Document | README.md |
| Module | root |
| Class | S — Stable spec (non-normative content) |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Human Owner |
| Maintainer | Orchestrator |
| Authority | None — human-facing introduction. Everything stated here is owned, normatively, elsewhere. |

---

**AMF v1.0.0** turns an AI coding agent (Claude Code today) into a structured engineering organization for real software projects: sites, web apps, tools.

Instead of one assistant improvising, you get:

- **Seven roles** — Orchestrator, Product Analyst, Architect, Engineer, Reviewer, QA Engineer, Release Manager — with explicit authority and hard prohibitions. The one that writes code never approves it; nothing deploys without your yes.
- **A memory that survives sessions** — every project gets a `.amf/` folder: status, tasks, decisions with their rationale, session logs, handovers. A brand-new session reads a handful of files and continues exactly where the last one stopped.
- **Decisions with a paper trail** — three classes: routine ones just happen, structural ones get recorded with alternatives and rationale, and anything irreversible or costly waits for you.
- **Objective quality gates** — work passes seven binary checkpoints (requirements → design → build → review → verify → record → release). "Mostly done" doesn't exist.
- **Three sizes** — Minimal (a restaurant site: 8 documents, 3 roles), Standard (a client app), Full (a long-running product). Same rules, proportional paper.

## Try it

1. Read the 5-minute tour: [core/AMF_OVERVIEW.md](core/AMF_OVERVIEW.md)
2. See it at project scale: the dry-run in [operations/ADOPTION_GUIDE.md §7](operations/ADOPTION_GUIDE.md)
3. Adopt it: [operations/ADOPTION_GUIDE.md](operations/ADOPTION_GUIDE.md) → your first session runs [workflows/WF_NEW_PROJECT.md](workflows/WF_NEW_PROJECT.md)

Everything else: [AMF_MANIFEST.md](AMF_MANIFEST.md) — the entry point and full document registry.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-07-12 | Architect (AI), Phase 8 | Initial README at release v1.0.0 |

## Future Extension Notes

Stays short forever; anything growing here belongs in the Manifest or the Overview.
