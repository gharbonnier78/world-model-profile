# World-model lineage recovery audit — 2026-09-15

## Scope

This audit was performed on branch `recovery/world-model-lineage-audit`, forked from `rebuild/world-model-complete`. No changes were made to `main` or to the accepted v0.4 spine.

## What was recovered

The branch `rebuild/world-model-complete` already contains a non-destructive text-core salvage produced from the truncated staged ZIP under `recovery/textcore-salvage/`.

The salvage report records three damaged entries excluded from the persisted recovery:

- `archive/REPOSITORY_IMPORT_SHA256SUMS.txt`
- `framework/accepted-v0.4/11_independent_check.py`
- one duplicate bad-CRC copy of `TEXT_CORE_SHA256SUMS.txt`

The recovered text core includes executable and evidence material for v0.4, including `03_verify_v0_4.py`, `04_RESULTS_V0_4.json`, `04_TOY_A_GRID_V0_4.csv`, `05_VERIFY_STDOUT_V0_4.txt`, author response, source notes, review handoff and prior review lineage.

## Canonical snapshot inventory

The recovered snapshot inventory records 122 files before checksum/inventory generation:

- `archive/`: 7
- `framework/`: 26
- `history/`: 50
- `paper/`: 2
- `research/`: 3
- `research-agenda/`: 32
- plus root `README.md` and `STATUS.md`

The binary-artifact inventory identifies the canonical local snapshot as:

- filename: `world_model_repository_snapshot_2026-09-15.zip`
- SHA-256: `045cbb4112bd620ab504789d123e639073683d98d53d7e69d7f029a8c8d903b1`

That snapshot is not present as a complete file in the current Git tree.

## Target PDF status

The sought accepted note is explicitly recorded in the binary inventory:

- path: `framework/accepted-v0.4/12_LAYERED_PROFILE_V0_4_NOTE.pdf`
- size: `264444` bytes
- SHA-256: `5e8d1ccf018a6a219fb663630d4213d48fa598471e5f42b8996f174b5d7f7758`

The inventory also records `framework/accepted-v0.4/13_PARENT_V0_3_NOTE_REVIEWED.pdf` and the historical v0.1–v0.3 PDFs.

## Binary recovery attempt

The successful recovery workflow on `rebuild/world-model-complete` reconstructed a 48,000-byte `tar.xz` candidate from:

- `.recovery/tar.b64.part00`
- `import/world-model-lineage:.import/source-tree.tar.xz.b64.part01` … `part06`

The XZ stream remains corrupt. With `xz -dc --ignore-check`, only an 18,505-byte partial POSIX tar prefix could be recovered. Its complete members were limited to four text files under `history/v0.1-review-cycle/`:

- `SHA256SUMS.txt`
- `00_REVIEW_CYCLE_COVER.md`
- `06_linkedin_article_fr_after_independent_review.md`
- `07_linkedin_post_short_fr_after_independent_review.md`

No PDF member is reachable in that recovered prefix.

## Conclusion

1. The textual/reproducibility lineage is substantially recovered under `recovery/textcore-salvage/`.
2. The accepted v0.4 PDF is known exactly by path, size and SHA-256, but its bytes are not recoverable from the currently staged truncated ZIP or truncated/corrupt `tar.xz` prefix.
3. Re-running the existing import workflow cannot reconstruct the missing PDF because the source transport itself is incomplete.
4. The remaining recovery source must be one of:
   - the original canonical snapshot `world_model_repository_snapshot_2026-09-15.zip` matching SHA-256 `045cbb4112bd620ab504789d123e639073683d98d53d7e69d7f029a8c8d903b1`;
   - the original v0.4 reviewer package `archive/import-bundles/world_model_v0_4_REVIEWER_FULL_PACKAGE.zip` matching SHA-256 `8d1536436e7b8bc2fb29d59da38a8acfbafa2ac9813e9879274e07df87b8a3c1`;
   - another local/exported copy of `12_LAYERED_PROFILE_V0_4_NOTE.pdf` matching the recorded SHA-256.

## Preservation rule

Do not overwrite the frozen v0.4 spine with reconstructed or regenerated binaries unless their provenance is explicit. A regenerated PDF from textual sources is useful as a derivative artifact but must not be represented as byte-identical to the lost accepted PDF unless its SHA-256 matches the canonical hash above.
