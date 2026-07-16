#!/usr/bin/env python3
"""
amf-lint — the AMF framework validator.

Implements the V1–V11 validation checks specified in
operations/FRAMEWORK_AUDIT.md §2. Runs against the framework repository
and exits non-zero on any failure, so it can gate a release
(FRAMEWORK_AUDIT.md §4) or run in CI.

Usage:
    python3 tools/amf-lint.py [--root PATH] [--quiet] [--only V1,V6,...]

No dependencies beyond the Python 3 standard library (AD-7: the
conventions were designed to be checkable without judgment).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# --- repository conventions (mirror FRAMEWORK_RULES.md) ----------------------

STATUSES = {"DRAFT", "ACTIVE", "DEPRECATED", "ARCHIVED"}
HEADER_FIELDS_FRAMEWORK = [
    "ID", "Document", "Module", "Class", "Version",
    "Status", "Owner", "Maintainer", "Authority",
]
ID_GRAMMAR = re.compile(r"^(ROOT|CORE|KNOW|AGNT|COMM|QUAL|WFLW|OPRN)-\d\d$")
# The user-supplied phase briefs live under md/ and are not framework docs.
EXCLUDE_DIRS = {"md", "tools", ".git"}
# AMF_ARCHITECTURE.md is frozen with its own header shape and GitHub-style TOC.
FROZEN = {"AMF_ARCHITECTURE.md"}


def is_framework_doc(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return rel.parts[0] not in EXCLUDE_DIRS


def framework_md_files(root: Path) -> list[Path]:
    out = []
    for f in sorted(root.rglob("*.md")):
        if is_framework_doc(f, root):
            out.append(f)
    return out


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def github_slug(heading: str) -> str:
    """Replicate GitHub's heading-anchor algorithm (does NOT collapse spaces)."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # drop punctuation incl. '&'
    s = s.replace(" ", "-")
    return s


class Report:
    def __init__(self, quiet: bool) -> None:
        self.quiet = quiet
        self.failures: dict[str, list[str]] = {}

    def fail(self, check: str, msg: str) -> None:
        self.failures.setdefault(check, []).append(msg)

    def check_done(self, check: str, title: str) -> None:
        n = len(self.failures.get(check, []))
        mark = "PASS" if n == 0 else "FAIL"
        if not self.quiet or n:
            print(f"  [{mark}] {check} — {title}" + (f" ({n})" if n else ""))
        for m in self.failures.get(check, []):
            print(f"         · {m}")


# --- checks ------------------------------------------------------------------

def load(files: list[Path]) -> dict[Path, str]:
    return {f: f.read_text(encoding="utf-8") for f in files}


def header_fields(text: str) -> list[tuple[str, str]]:
    out = []
    for m in re.finditer(r"^\|\s*([A-Za-z][\w /()]*?)\s*\|\s*(.*?)\s*\|\s*$", text, re.M):
        k, v = m.group(1).strip(), m.group(2).strip()
        if k in ("Field",) or set(k) <= {"-"}:
            continue
        out.append((k, v))
    return out


def header_map(text: str) -> dict[str, str]:
    d = {}
    for k, v in header_fields(text):
        d.setdefault(k, v)
    return d


def V1_links(root, docs, rep):
    for f, t in docs.items():
        for m in re.finditer(r"\]\(([^)#]+\.md)(#[^)]*)?\)", strip_code_fences(t)):
            if not (f.parent / m.group(1)).resolve().exists():
                rep.fail("V1", f"{f.relative_to(root)}: -> {m.group(1)}")


def V2_markers(root, docs, rep):
    ok = ("Architect (AI)", "ACTIVE (Phase", ", done)")
    for f, t in docs.items():
        if f.name in FROZEN:
            continue
        for i, line in enumerate(t.splitlines(), 1):
            if re.search(r"\(Phase \d+\)", line) and not any(o in line for o in ok):
                rep.fail("V2", f"{f.relative_to(root)}:{i}: {line.strip()[:70]}")


def V3_ids(root, docs, rep):
    seen = {}
    for f, t in docs.items():
        if f.name in FROZEN:
            continue
        m = re.search(r"^\|\s*ID\s*\|\s*(\S+)\s*\|", t, re.M)
        if not m:
            rep.fail("V3", f"{f.relative_to(root)}: no ID field")
            continue
        fid = m.group(1)
        if not ID_GRAMMAR.match(fid):
            rep.fail("V3", f"{f.relative_to(root)}: malformed ID '{fid}'")
        if fid in seen:
            rep.fail("V3", f"duplicate ID '{fid}': {seen[fid]} & {f.relative_to(root)}")
        seen[fid] = f.relative_to(root)


def V4_headers(root, docs, rep):
    for f, t in docs.items():
        if f.name in FROZEN:
            continue
        keys = [k for k, _ in header_fields(t)][: len(HEADER_FIELDS_FRAMEWORK)]
        if keys[:2] != ["ID", "Document"]:
            rep.fail("V4", f"{f.relative_to(root)}: header does not start ID,Document")
            continue
        for want in HEADER_FIELDS_FRAMEWORK:
            if want not in keys:
                rep.fail("V4", f"{f.relative_to(root)}: header missing '{want}'")


def V5_sections(root, docs, rep):
    for f, t in docs.items():
        if f.name in FROZEN or f.name == "README.md":
            continue
        for sec in ("## Document Contract", "## Revision History", "## Future Extension Notes"):
            if sec not in t:
                rep.fail("V5", f"{f.relative_to(root)}: missing '{sec}'")


def V6_registry(root, docs, rep):
    man = root / "AMF_MANIFEST.md"
    if man not in docs:
        rep.fail("V6", "AMF_MANIFEST.md not found")
        return
    for row in re.finditer(
        r"\|\s*([A-Z]{4}-\d\d)\s*\|\s*\[([^\]]+)\]\([^)]+\)\s*\|\s*\S+\s*\|\s*([\d.]+(?:-\S+)?)\s*\|",
        docs[man],
    ):
        fid, path, ver = row.groups()
        target = root / path
        if not target.exists():
            rep.fail("V6", f"registry row {fid}: file {path} missing")
            continue
        hv = header_map(target.read_text(encoding="utf-8")).get("Version")
        if hv != ver:
            rep.fail("V6", f"{fid} {path}: registry {ver} != header {hv}")


def V7_status(root, docs, rep):
    for f, t in docs.items():
        if f.name in FROZEN:
            continue
        st = header_map(t).get("Status", "")
        base = st.split(" ")[0]
        if base not in STATUSES:
            rep.fail("V7", f"{f.relative_to(root)}: status '{st}' not in vocabulary")


def V8_ownership(root, docs, rep):
    # (a) every framework doc names an Owner (no orphans)
    for f, t in docs.items():
        if f.name in FROZEN or f.name == "README.md":
            continue
        if "Owner" not in header_map(t):
            rep.fail("V8", f"{f.relative_to(root)}: no Owner")
    # (b) knowledge-domain ownership uniqueness: each instance document appears
    #     exactly once in the KNOWLEDGE_SYSTEM registry with exactly one owner.
    ks = root / "knowledge/KNOWLEDGE_SYSTEM.md"
    if ks.exists():
        seen = {}
        for row in re.finditer(
            r"^\|\s*([A-Z_]+(?:\.md)?)\s*\|\s*KNOW-\d\d\s*\|\s*[IA]\s*\|\s*([^|]+?)\s*\|",
            ks.read_text(encoding="utf-8"), re.M,
        ):
            fname, owner = row.group(1).strip(), row.group(2).strip()
            if fname in seen and seen[fname] != owner:
                rep.fail("V8", f"instance doc {fname}: two owners ({seen[fname]} & {owner})")
            seen[fname] = owner
        if len(seen) < 20:
            rep.fail("V8", f"KNOWLEDGE_SYSTEM registry parsed only {len(seen)} instance docs (<20)")


def V9_coverage(root, docs, rep):
    # every WF_* has a reading row in CONTEXT_RECONSTRUCTION and an index row
    wf = [f.stem for f in docs if f.name.startswith("WF_")]
    cr = (root / "knowledge/CONTEXT_RECONSTRUCTION.md")
    idx = (root / "workflows/WORKFLOW_INDEX.md")
    crt = cr.read_text(encoding="utf-8") if cr.exists() else ""
    idxt = idx.read_text(encoding="utf-8") if idx.exists() else ""
    for w in wf:
        if w not in crt:
            rep.fail("V9", f"{w}: no reading-list row in CONTEXT_RECONSTRUCTION.md")
        if w not in idxt:
            rep.fail("V9", f"{w}: no catalog row in WORKFLOW_INDEX.md")
    # every E-code cited anywhere is defined in the matrix
    mtx = (root / "knowledge/UPDATE_MATRIX.md")
    defined = set(re.findall(r"^\|\s*(E\d\d)\s*\|", mtx.read_text(encoding="utf-8"), re.M)) if mtx.exists() else set()
    cited = set()
    for t in docs.values():
        cited |= set(re.findall(r"\bE\d\d\b", t))
    for e in sorted(cited - defined):
        rep.fail("V9", f"E-code {e} cited but not defined in UPDATE_MATRIX.md")
    # message-type coverage: the ten types each define a persistence target
    mt = (root / "communication/MESSAGE_TYPES.md")
    if mt.exists():
        mtt = mt.read_text(encoding="utf-8")
        types = re.findall(r"^###\s+2\.\d+\s+(.+)$", mtt, re.M)
        if len(types) != 10:
            rep.fail("V9", f"MESSAGE_TYPES.md defines {len(types)} types, expected 10")
        # each type block must state where it persists
        blocks = re.split(r"^###\s+2\.\d+\s+", mtt, flags=re.M)[1:]
        for b in blocks:
            name = b.splitlines()[0].strip()
            if "Persists to" not in b:
                rep.fail("V9", f"message type '{name}': no 'Persists to' row")


# Reserved terms whose synonyms are forbidden in normative text (glossary rule
# R1.4 / one-term-per-concept). A line is exempt when it *documents* the term
# rather than using it (definitions, fix notes, changelog/revision rows).
RESERVED_SYNONYMS = {
    r"\bhand-?off\b": "handover",
    r"\bhandoffs\b": "handovers",
}
_TERM_EXEMPT = ("handover", "never handoff", "Contract", "Note",
                "->", "→", "Client delivery", "delivery", "synonym", "Synonyms")


def V11_terms(root, docs, rep):
    for f, t in docs.items():
        if f.name in FROZEN:
            continue
        body = strip_code_fences(t)
        for i, line in enumerate(body.splitlines(), 1):
            if any(x in line for x in _TERM_EXEMPT):
                continue
            for pat, good in RESERVED_SYNONYMS.items():
                if re.search(pat, line, re.I):
                    rep.fail("V11", f"{f.relative_to(root)}:{i}: reserved-term synonym -> use '{good}': {line.strip()[:60]}")


def V10_version(root, docs, rep):
    for f, t in docs.items():
        if f.name in FROZEN:
            continue
        hv = header_map(t).get("Version")
        rows = re.findall(r"^\|\s*([\d.]+(?:-\S+)?)\s*\|\s*20\d\d-\d\d-\d\d\s*\|", t, re.M)
        if hv and rows and hv != rows[-1]:
            rep.fail("V10", f"{f.relative_to(root)}: header {hv} != last revision {rows[-1]}")


CHECKS = [
    ("V1", "cross-references resolve", V1_links),
    ("V2", "no stale phase markers", V2_markers),
    ("V3", "document IDs unique & well-formed", V3_ids),
    ("V4", "headers complete & ordered", V4_headers),
    ("V5", "contract + footer sections present", V5_sections),
    ("V6", "registry ↔ header consistency", V6_registry),
    ("V7", "status vocabulary", V7_status),
    ("V8", "ownership present", V8_ownership),
    ("V9", "workflow / E-code / message-type coverage", V9_coverage),
    ("V10", "header version == last revision", V10_version),
    ("V11", "no reserved-term synonyms", V11_terms),
]


def main() -> int:
    ap = argparse.ArgumentParser(description="AMF framework validator (V1–V11).")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--quiet", action="store_true", help="only print failures")
    ap.add_argument("--only", default="", help="comma list, e.g. V1,V6")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    only = {c.strip().upper() for c in args.only.split(",") if c.strip()}
    files = framework_md_files(root)
    docs = load(files)
    rep = Report(args.quiet)

    print(f"amf-lint · {len(files)} framework documents · root {root}")
    for cid, title, fn in CHECKS:
        if only and cid not in only:
            continue
        fn(root, docs, rep)
        rep.check_done(cid, title)

    total = sum(len(v) for v in rep.failures.values())
    print()
    if total:
        print(f"FAIL — {total} issue(s) across {len(rep.failures)} check(s).")
        return 1
    print("PASS — framework is consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
