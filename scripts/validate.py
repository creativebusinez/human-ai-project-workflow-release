#!/usr/bin/env python3
"""Mechanical validation for the HAPW v0.2 public-candidate release package."""
from __future__ import annotations
import hashlib, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE_REL="core/HAPW-v0.2-public-candidate.md"
CORE=ROOT/CORE_REL
LICENSE_REL="LICENSE"
LICENSE=ROOT/LICENSE_REL
EXPECTED_VERSION="0.2-public-candidate"
EXPECTED_SIZE=33106
EXPECTED_SHA256="a00bfb2075081da51468ba06a87bdd19607f725f856e4f3d57265b8ac7050393"
EXPECTED_LICENSE_GIT_BLOB="137069b823873b8bcf42979bcf8e9371052d26a2"
REQUIRED=("README.md","QUICKSTART.md","CHANGELOG.md","VERSION",LICENSE_REL,CORE_REL,"templates/00_PROJECT.md","templates/01_STATE.md","templates/02_NEXT.md","templates/03_DECISIONS.md","templates/CHECKPOINT.md","templates/HANDOFF.md","adapters/README.md","adapters/local-filesystem.md","adapters/google-drive.md","adapters/github.md","docs/concepts.md","docs/authority-model.md","docs/recovery.md","docs/security.md","docs/limitations.md","examples/minimal-project/00_PROJECT.md","examples/minimal-project/01_STATE.md","examples/minimal-project/02_NEXT.md","examples/minimal-project/03_DECISIONS.md","scripts/validate.py",".github/workflows/validate.yml")
SECRET=re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|client[_-]?secret)\b\s*[:=]\s*[\"'][A-Za-z0-9_./+=:-]{16,}[\"']")
PRIVATE_KEY="-----BEGIN "+"PRIVATE KEY-----"
DRIVE=re.compile(r"drive\.google\.com/(?:file|drive|document|spreadsheets|presentation)")
LOCAL=re.compile(r"(?im)^\s*(?:/home/|/Users/|[A-Z]:\\Users\\)")
def fail(m): print("ERROR:",m); raise SystemExit(1)
def text(p): return (ROOT/p).read_text(encoding="utf-8")
def git_blob_sha1(data): return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def main():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    if missing: fail("missing required file(s): "+", ".join(missing))
    print(f"PASS: required release-candidate files={len(REQUIRED)}")
    data=CORE.read_bytes(); digest=hashlib.sha256(data).hexdigest()
    if len(data)!=EXPECTED_SIZE: fail(f"Core size {len(data)} != {EXPECTED_SIZE}")
    if digest!=EXPECTED_SHA256: fail(f"Core SHA-256 {digest} != {EXPECTED_SHA256}")
    if text("VERSION").strip()!=EXPECTED_VERSION: fail("VERSION mismatch")
    print(f"PASS: core bytes={len(data)} sha256={digest}"); print(f"PASS: version={EXPECTED_VERSION}")
    license_data=LICENSE.read_bytes(); license_blob=git_blob_sha1(license_data); license_sha256=hashlib.sha256(license_data).hexdigest()
    if license_blob!=EXPECTED_LICENSE_GIT_BLOB: fail(f"LICENSE Git blob {license_blob} != {EXPECTED_LICENSE_GIT_BLOB}")
    license_text=license_data.decode("utf-8")
    for marker in ("Apache License","Version 2.0, January 2004","END OF TERMS AND CONDITIONS"):
        if marker not in license_text: fail(f"LICENSE missing marker {marker!r}")
    print(f"PASS: license=Apache-2.0 bytes={len(license_data)} gitblob={license_blob} sha256={license_sha256}")
    md=sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    empty=[str(p.relative_to(ROOT)) for p in md if not p.read_bytes().strip()]
    if empty: fail("empty Markdown: "+", ".join(empty))
    print(f"PASS: non-empty Markdown files={len(md)}")
    markers={"README.md":("v0.2 public candidate","not HAPW 1.0",CORE_REL,"Apache License, Version 2.0","LICENSE"),"QUICKSTART.md":("about five minutes",CORE_REL,"does not imply HAPW 1.0"),"CHANGELOG.md":("0.2-public-candidate","not HAPW 1.0","Apache License, Version 2.0"),"adapters/README.md":("# HAPW Adapters","## Adapter selection rule","## Common adapter contract"),"docs/concepts.md":("# HAPW Concepts",),"docs/authority-model.md":("# HAPW Authority Model",),"docs/recovery.md":("# HAPW Recovery",),"docs/security.md":("# HAPW Security and Privacy",),"docs/limitations.md":("# HAPW Limitations","Apache License, Version 2.0")}
    for rel, req in markers.items():
        t=text(rel)
        for m in req:
            if m not in t: fail(f"{rel} missing marker {m!r}")
    if "works for any project" in (text("README.md")+text("QUICKSTART.md")+text("CHANGELOG.md")).lower(): fail("forbidden scope claim")
    for p in sorted(q for q in ROOT.rglob("*") if q.is_file() and ".git" not in q.parts and q.suffix.lower() in {".md",".py",".yml",".yaml",""}):
        t=p.read_text(encoding="utf-8"); rel=str(p.relative_to(ROOT))
        if PRIVATE_KEY in t: fail(f"{rel} contains private-key header")
        if SECRET.search(t): fail(f"{rel} appears to contain a hard-coded secret")
        if DRIVE.search(t) or LOCAL.search(t): fail(f"{rel} contains private/local reference pattern")
    print("PASS: generic publication-safety scan")
    print("PASS: HAPW v0.2 public-candidate licensed release package")
    return 0
if __name__=="__main__": sys.exit(main())
