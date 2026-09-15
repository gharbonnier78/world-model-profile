# Manuscript Changelog — Authoring Revision 0.4

This revision applies the external-reader and reproducibility corrections requested after mechanical review of the 14-page manuscript. The scientific framework, finite constructions, equations, and Table 2 values are unchanged.

## Corrections applied

1. **Repository-internal wording removed from the manuscript body.**
   - Abstract: `manuscript-level diagnostics` -> `illustrative diagnostics`.
   - Policy-exposure paragraph: replaced the circumstance `used during framework review` with the mathematical property of the two-history latent cell.
   - Section title: `Manuscript-level diagnostics beyond the accepted spine` -> `Illustrative diagnostics`.
   - Section opening no longer refers to an `accepted profile`.
   - Three-history paragraph no longer refers to a `reviewer concern`.

2. **Appendix B rewritten in the present tense around concrete reproducibility materials.**
   - `verify_finite_separations.py` regenerates `finite_separation_results.json` and `toy_a_grid.csv`.
   - `verify_supporting_diagnostics.py` regenerates `supporting_diagnostics_results.json`.
   - `SHA256SUMS.txt` identifies the distributed files.
   - No future-tense `should include` wording remains.

3. **Title-page version collision removed.**
   - `Draft v0.3 -- 9 September 2026` -> `9 September 2026`.
   - The package may carry an internal authoring revision number, but the PDF title page does not compete with arXiv's own v1/v2 numbering.

4. **Previously repaired scientific-domain conditions preserved and mechanically rechecked.**
   - Richens–Everitt wording retains `local interventions on all environment variables` at both points of use.
   - `delta_inv^latent` remains restricted to common support, with the explicit reason that one conditional kernel may otherwise be undefined.

5. **No scientific-result change.**
   - The accepted profile coordinates are unchanged.
   - Toy A, Toy B, the three-history illustration, and the minimal L2.O illustration retain the same reported values.
   - Table 2 values are unchanged.
