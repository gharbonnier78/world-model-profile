# Changelog — arXiv Draft v0.3

## Scope

Manuscript-only revision after focused review of draft v0.2. The frozen framework spine is unchanged.

## Corrections

1. **Appendix float regression fixed.** Table 2 is now forced after the Appendix A heading (`[H]`), with a page break before the appendix. The appendix is no longer visually empty.
2. **External-facing status block rewritten.** The repository/version-control wording (`accepted v0.4 spine`, `Draft v0.2 adds...`) is removed from the manuscript. The replacement `Scope and evidence` paragraph states only the scientific evidence boundary visible to an external reader and does not imply peer review.
3. **Engineering-register apology removed.** The sentence after the structural engineering-qualification comparison was deleted; the comparison is left to stand on its own.
4. **Richens–Everitt scope restored.** Both related-work and L3 text now state the relevant robustness condition as local interventions on **all environment variables** under the theorem assumptions.
5. **Common-support condition restored for policy exposure.** `delta_inv^latent` is now explicitly defined only over latent–action pairs supported by both behaviour policies. This prevents comparison of undefined conditional kernels.
6. **Section 6 strengthened with a retrodiction.** He et al.'s MuZero analysis is identified as a retrospective example of why evaluation restricted to a search-induced region can miss poorer unseen-policy evaluation. It is explicitly labelled as a retrodiction, not a prediction of the framework.
7. **Cifuentes / Richens title collision resolved in provenance notes.** The Cifuentes 2026 paper and the Richens et al. ICML/arXiv records are separate works/records with distinct identifiers and author lists.

## What did not change

- profile coordinates;
- Toy A / Toy B finite results;
- `rho_pol` status as an L0 attribution diagnostic;
- non-identity-only claim scope;
- eliminativist alternative;
- MMALS as future-work motivation rather than a world-model classification claim.

## PDF verification

- 14 pages;
- compiled twice with pdfLaTeX;
- preflight openable / unencrypted / non-scanned / no XFA;
- rendered at 160 dpi and visually checked;
- Appendix A heading now precedes Table 2 on page 13.
