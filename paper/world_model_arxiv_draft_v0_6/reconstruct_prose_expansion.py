#!/usr/bin/env python3
"""Reconstruct the exact prose-expansion memo from connector-safe byte parts."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
PARTS = [
    ROOT / "_source_parts/13_ARXIV_DRAFT_PROSE_EXPANSION.md.part00",
    ROOT / "_source_parts/13_ARXIV_DRAFT_PROSE_EXPANSION.md.part01",
    ROOT / "_source_parts/13_ARXIV_DRAFT_PROSE_EXPANSION.md.part02",
]
OUT = ROOT / "13_ARXIV_DRAFT_PROSE_EXPANSION.md"
EXPECTED_SHA256 = "cfaefe605ec5109907f14004eb6a61b8ebb2212148db04e64108e32d85ac1cdc"

payload = b"".join(p.read_bytes() for p in PARTS)
actual = hashlib.sha256(payload).hexdigest()
if actual != EXPECTED_SHA256:
    raise SystemExit(f"source checksum mismatch: {actual} != {EXPECTED_SHA256}")
OUT.write_bytes(payload)
print(f"wrote {OUT.name}: {len(payload)} bytes; sha256={actual}")
