#!/usr/bin/env python3
"""Check the curated native-map source set and artifact without modifying them."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent


def admitted_files(root):
    paths = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=root
    ).decode().split("\0")
    return sorted(p for p in paths if p and (
        p.startswith(("linux/", "libretro/", "3ds/core/"))
        or p in ("docs/POCKET.md", "LICENSE", "NOTICE")
    ))


def check(root, manifest):
    actual = admitted_files(root)
    expected = sorted(manifest["files"])
    problems = []
    if actual != expected:
        problems.append("admitted source file set changed")
    for name, digest in manifest["files"].items():
        path = root / name
        if path.is_symlink() or not path.is_file():
            problems.append("missing/nonregular source: " + name)
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            problems.append("changed source: " + name)
    artifact = root / "docs/floorplan/index.html"
    if hashlib.sha256(artifact.read_bytes()).hexdigest() != manifest["html_sha256"]:
        problems.append("map artifact changed")
    return problems


def main():
    manifest = json.loads((BASE / "manifest.json").read_text())
    problems = check(ROOT, manifest)
    if problems:
        raise SystemExit("STALE: " + "; ".join(problems))
    print("PASS: curated native source set and map artifact match; not device qualification")


if __name__ == "__main__":
    main()
