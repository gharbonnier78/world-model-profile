# Import Manifest — World Model arXiv Draft v0.6

**Import date:** 2026-09-15  
**Source attachment:** `world_model_arxiv_draft_v0_6_FULL_PACKAGE(1).zip`  
**Source ZIP size:** 1,313,486 bytes  
**Source ZIP SHA-256:** `921c3394fb0965f2122c45823d9325da83ddcdc6cd155d44ac5a9014565ba461`  
**Import branch:** `import/world-model-v0.6-full-package`

## Preservation rule

Nothing in the pre-existing `import/world-model-lineage` branch was overwritten during import. The v0.6 package is staged in a dedicated branch and directory.

The source ZIP was unpacked before import and its packaged `SHA256SUMS.txt` was checked successfully for every listed artifact. Both verification scripts were then executed successfully from the unpacked package:

- `verify_finite_separations.py`
- `verify_supporting_diagnostics.py`

The scientific source/evidence files are preserved as Git text blobs or as exact byte parts with reconstruction scripts. Generated JSON/CSV artifacts are reproducible from the exact verification scripts.

## Exact source reconstruction

Two large source files are stored as connector-safe byte parts because the GitHub connector is text-oriented:

- `13_ARXIV_DRAFT_PROSE_EXPANSION.md` → `_source_parts/13_ARXIV_DRAFT_PROSE_EXPANSION.md.part*` + `reconstruct_prose_expansion.py`; expected SHA-256 `cfaefe605ec5109907f14004eb6a61b8ebb2212148db04e64108e32d85ac1cdc`.
- `world_model_profile_arxiv_draft_v0_6.tex` → `_source_parts/world_model_profile_arxiv_draft_v0_6.tex.part*` + `reconstruct_tex.py`; expected SHA-256 `048c1219599fa3106e397f5542c6c469efeb2bb001c9e9283a554491ea4148db`.

The reconstruction scripts fail if the reconstructed byte stream does not match the package checksum.

## Package inventory

The original package contained 29 files:

1. `13_ARXIV_DRAFT_PROSE_EXPANSION.md`
2. `14_ENGINEERING_REGISTER_INTEGRATION.md`
3. `15_INTEGRATION_DECISIONS_V13_V14.md`
4. `AUTHOR_REWRITE_GUIDE.md`
5. `CHANGELOG_V0_2.md`
6. `CHANGELOG_V0_3.md`
7. `CHANGELOG_V0_4.md`
8. `CHANGELOG_V0_6.md`
9. `CLAIM_EVIDENCE_MAP.md`
10. `FINAL_GUARD_REVIEW_HANDOFF_V0_6.md`
11. `FROZEN_ACCEPTED_SPINE_v0_4.pdf`
12. `INDEPENDENT_REVIEW_ACCEPT_AS_FRAMEWORK_SPINE.md`
13. `MECHANICAL_VERIFICATION_V0_6.md`
14. `PDF_PREFLIGHT_V0_5.txt`
15. `README.md`
16. `REFERENCE_VERIFICATION.md`
17. `REFERENCE_VERIFICATION_V0_3.md`
18. `REVIEW_ACTIONS_V0_3.md`
19. `SHA256SUMS.txt`
20. `fig_rho_three_history.png`
21. `fig_toy_a_regret.png`
22. `finite_separation_results.json`
23. `supporting_diagnostics_results.json`
24. `toy_a_grid.csv`
25. `verify_finite_separations.py`
26. `verify_supporting_diagnostics.py`
27. `world_model_profile_arxiv_draft_v0_3.pdf`
28. `world_model_profile_arxiv_draft_v0_6.pdf`
29. `world_model_profile_arxiv_draft_v0_6.tex`

## Rendered binary artifacts

The connector used for this import does not accept local binary files as file parameters. Therefore the canonical scientific content is preserved through the exact source, exact verification code/data, package checksums, and the existing accepted-v0.4 source/review lineage. The following rendered binary artifacts retain their source-package SHA-256 identities in `SHA256SUMS.txt`:

- `FROZEN_ACCEPTED_SPINE_v0_4.pdf` — `4f330dd91d20abcb2012995dba315a3bc10844bd3658136603c40b4aaffb3a64`
- `fig_rho_three_history.png` — `dad2b41e903a22040824617165fe3e1c2d5cb9f9ce6d74b6a80fd3a4d8bdce28`
- `fig_toy_a_regret.png` — `4d3332f2a4f0be9f0f5cf29d0f9be14ec46be228ff5f194227a4cf13d0aa7f6a`
- `world_model_profile_arxiv_draft_v0_3.pdf` — `5919bb8d589b2ea3abe01d44974832f4ff9562669258508c2c01dac5a870d770`
- `world_model_profile_arxiv_draft_v0_6.pdf` — `6b4e5a9e41fed8cb0f7872b8f2bbb27d58d252f7258d1f2ceb947fc69c965691`

These are treated as rendered/derived artifacts, not as the source of authority for claims. No binary checksum is silently replaced by a regenerated file.

## Scientific status preserved

Revision 0.6 is an **authoring manuscript, not submission-ready**. The only v0.6 change is the explicit binary-query guard in the exact Toy A solver. The manuscript, Table 2, scientific values, and machine-readable outputs are otherwise unchanged from v0.5.

The package continues to make no claim of:

- a unique world-model definition;
- necessary and sufficient conditions;
- general non-collinearity of L0 and L2;
- defeat of the eliminativist alternative;
- MMALS being a world model.

The accepted framework spine remains frozen at v0.4.
