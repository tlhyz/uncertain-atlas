#!/usr/bin/env python3
"""P3-3: measure CometBFT KB snapshot branches vs the current worktree.

Does not delete remotes. Does not merge parallel branches.

Usage:
  python3 uncertain-atlas/tools/snapshot_branch_inventory.py
  python3 uncertain-atlas/tools/snapshot_branch_inventory.py --json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ATLAS = Path(__file__).resolve().parents[1]

UNIQUE_STEMS = (
    "cifields-vs-notes",
    "cinotes-vs-order",
    "exectxevents-vs-header",
    "extappgen-vs-signed",
    "extcinotes-vs-order",
    "extviusage-vs-expose",
    "prepevents-vs-finalize",
    "validatorusage-vs-gates",
    "viusageavail-vs-extractpath",
)

SUCCESSOR = {
    "finfields": "ffields-not* / finfields-vs-equiv (407 / 1109–1111)",
    "htmatch": "htmt-not* / htmatch-vs-header (417 / 1097–1099)",
    "finlock": "finlock-vs-commitlock + finlock-not*",
    "procaccept": "procaccept-shouldaccept / default / liveness",
    "verifyaccept": "verifyaccept-shouldaccept / default / liveness",
    "finempty": "finempty-not*",
    "finexec": "finexecbv-not*",
    "finfill": "finfill-not* / finfill-bundled",
    "finht": "finht-not*",
    "finnewfields": "finnewfields-not*",
    "finproc": "finprocgua-not*",
    "finreward": "finreward-notslashed",
    "fincand": "fincand-not* / fincand-bundled",
    "finvaldelay": "fndelay-not*",
    "misbheighttime": "misbehavior-nottime / misbehavior-vs-enum",
    "misbtvp": "misbehavior-not* / finmisbeh-notvoteinfo",
    "misbtype": "misbehavior-notslashed / misbehavior-vs-enum",
    "misbvalidator": "misbehavior-not* / finmisbeh-notvoteinfo",
    "proccand": "proccand-*-notcommitted",
    "procfull": "procfull-not*",
    "procht": "procht-not*",
}


def run(args: list[str]) -> str:
    return subprocess.check_output(args, cwd=REPO, text=True)


def remotes() -> list[str]:
    out = run(
        [
            "git",
            "for-each-ref",
            "--format=%(refname:short)",
            "refs/remotes/origin/cursor/cometbft-*",
        ]
    )
    return [ln for ln in out.splitlines() if ln]


def is_ancestor(ref: str) -> bool:
    return subprocess.run(
        ["git", "merge-base", "--is-ancestor", ref, "HEAD"],
        cwd=REPO,
    ).returncode == 0


def atlas_files(ref: str) -> list[str]:
    out = run(["git", "ls-tree", "-r", "--name-only", ref])
    return [p for p in out.splitlines() if p.startswith("uncertain-atlas/")]


def worktree_atlas() -> set[str]:
    found: set[str] = set()
    for p in ATLAS.rglob("*"):
        if p.is_file():
            found.add(str(p.relative_to(REPO)))
    return found


def classify(path: str) -> tuple[str, str]:
    name = Path(path).name
    for stem in UNIQUE_STEMS:
        if stem in name or stem.replace("-vs-", "-") in name:
            return "unique", "no successor on HEAD; recover (do not fill 439–446 mid-README)"
        key = stem.split("-")[0]
        if name.startswith(f"worked-example-{key}") or name.startswith(key) or f"-{key}-" in name or name.startswith(f"name-the-{key}") or name.startswith(f"name-the-{key.replace('ext', 'ext-')}"):
            if any(s in name for s in UNIQUE_STEMS) or any(
                token in name
                for token in (
                    "cifields",
                    "cinotes",
                    "exectxevents",
                    "extappgen",
                    "extcinotes",
                    "extviusage",
                    "prepevents",
                    "validatorusage",
                    "viusageavail",
                    "ci-fields",
                    "ci-notes",
                    "exectx-events",
                    "ext-appgen",
                    "ext-ci-notes",
                    "ext-vi-usage",
                    "prepevents-retention",
                    "validatorusage-gates",
                    "vi-usageavail",
                )
            ):
                return "unique", "no successor on HEAD; recover (do not fill 439–446 mid-README)"
    for prefix, note in SUCCESSOR.items():
        if prefix in name.replace("-", ""):
            return "superseded", note
        if prefix in name:
            return "superseded", note
    return "superseded", "later alternate prefix or already-unbundled sibling on HEAD"


def inventory() -> dict:
    refs = remotes()
    contained = [r for r in refs if is_ancestor(r)]
    parallel = [r for r in refs if r not in contained]
    rich: list[tuple[int, str]] = []
    for r in parallel:
        rich.append((len(atlas_files(r)), r))
    rich.sort(reverse=True)
    tip = rich[0][1] if rich else ""
    tip_files = set(atlas_files(tip)) if tip else set()
    missing = sorted(tip_files - worktree_atlas())
    buckets = {"unique": [], "superseded": []}
    for m in missing:
        kind, note = classify(m)
        buckets[kind].append({"path": m, "note": note})
    return {
        "head": run(["git", "rev-parse", "--short", "HEAD"]).strip(),
        "remote_cometbft": len(refs),
        "contained": len(contained),
        "parallel": len(parallel),
        "tip": tip,
        "tip_atlas": len(tip_files),
        "missing": len(missing),
        "unique": len(buckets["unique"]),
        "superseded": len(buckets["superseded"]),
        "top_parallel": [{"ref": r, "atlas_files": n} for n, r in rich[:5]],
        "unique_files": buckets["unique"],
        "superseded_files": buckets["superseded"],
        "do_not": [
            "do not delete the 285 remotes this wake",
            "do not merge the 74 parallel branches (conflict surface)",
            "do not git checkout the 107 missing files wholesale",
            "do not copy superseded finfields/htmatch/finlock/procaccept-vs-req3/verifyaccept-vs-req6 duplicates",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Inventory CometBFT snapshot branches")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    data = inventory()
    if args.json:
        json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0
    print(f"HEAD {data['head']}")
    print(f"remote cometbft branches: {data['remote_cometbft']}")
    print(f"contained in HEAD:        {data['contained']}")
    print(f"parallel (not ancestor):  {data['parallel']}")
    print(f"richest parallel tip:     {data['tip']} ({data['tip_atlas']} atlas files)")
    print(f"missing from worktree:    {data['missing']}")
    print(f"unique (recover):         {data['unique']}")
    print(f"superseded (skip copy):   {data['superseded']}")
    print("unique files:")
    for row in data["unique_files"]:
        print(f"  {row['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
