# Beyond “Has a World Model?” — Authoring Revision 0.6

## Status

**Authoring manuscript, not submission-ready.**

The PDF title page uses only the calendar date. `0.6` is a local authoring revision for package traceability and is not intended to compete with arXiv's own version numbering.

## Main manuscript

- `world_model_profile_arxiv_draft_v0_6.pdf` — rendered manuscript
- `world_model_profile_arxiv_draft_v0_6.tex` — LaTeX source

## Reproducibility materials named in Appendix B

- `verify_finite_separations.py`
- `finite_separation_results.json`
- `toy_a_grid.csv`
- `verify_supporting_diagnostics.py`
- `supporting_diagnostics_results.json`
- `SHA256SUMS.txt`

`verify_finite_separations.py` derives the two finite separation results from explicit environments and exact policy enumeration. It now uses a shared phase-transition helper and an exact binary-head minimax calculation for Toy A query retention; no 0.01 grid approximation remains.

`verify_supporting_diagnostics.py` derives the three-history `rho_pol` illustration and the minimal L2.O illustration, then checks the derived values against explicit expected values as a non-regression guard. The assertions are checks in addition to, not substitutes for, derivation.

`finite_separation_results.json` also contains the two-history policy-exposure witness discussed in Appendix B. The three-history values reported in Table 2 remain separate supporting diagnostics.

## Revision 0.6 focus

- adds the missing explicit domain guard for the exact binary-query minimax solver;
- raises `RuntimeError("exact binary-head solver assumes a binary query")` if a target law contains support outside `{0,1}`;
- leaves the manuscript, scientific values, Table 2, and all machine-readable outputs unchanged.

See `CHANGELOG_V0_6.md`.

## Scientific boundaries retained

The manuscript does **not** claim:

- a unique definition of world models;
- necessary and sufficient conditions;
- novelty of classical state-abstraction or value-equivalence phenomena;
- non-collinearity of L0 and L2 in a non-degenerate regime;
- that the eliminativist alternative has been defeated;
- that MMALS is a world model.

The mixture bound for `rho_pol` remains presented as an elementary consequence, with no novelty claim pending a dedicated prior-statement search.
