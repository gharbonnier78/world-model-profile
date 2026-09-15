#!/usr/bin/env python3
"""Reconstruct the exact v0.6 LaTeX source from connector-safe byte parts.

The split is an import transport detail only. The reconstructed file must match
SHA256SUMS.txt exactly.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
PARTS = [
    ROOT / "_source_parts/world_model_profile_arxiv_draft_v0_6.tex.part00",
    ROOT / "_source_parts/world_model_profile_arxiv_draft_v0_6.tex.part01a",
    ROOT / "_source_parts/world_model_profile_arxiv_draft_v0_6.tex.part01b",
    ROOT / "_source_parts/world_model_profile_arxiv_draft_v0_6.tex.part02",
]
OUT = ROOT / "world_model_profile_arxiv_draft_v0_6.tex"
EXPECTED_SHA256 = "048c1219599fa3106e397f5542c6c469efeb2bb001c9e9283a554491ea4148db"

payload = b"".join(p.read_bytes() for p in PARTS)
actual = hashlib.sha256(payload).hexdigest()
if actual != EXPECTED_SHA256:
    raise SystemExit(f"source checksum mismatch: {actual} != {EXPECTED_SHA256}")
OUT.write_bytes(payload)
print(f"wrote {OUT.name}: {len(payload)} bytes; sha256={actual}")
