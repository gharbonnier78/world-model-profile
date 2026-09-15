# Changelog — arXiv Draft v0.2

## Scientific spine

No change. The frozen v0.4 framework remains:

`<L0[rho_pol], L1_int, L2.G, L2.O, L3>`.

Finite claims remain only:

- `L0 ⇏ L2` in Toy A;
- `L2.G ⇏ L0` in Toy B.

## Manuscript changes

1. Introduction now starts from two carefully scoped contrasting system types rather than from a bibliography.
2. The adaptive-history compression question appears in the introduction and becomes the closing research question.
3. Related work states the state-abstraction / AIS / VE boundary earlier and more explicitly.
4. L0 now explains:
   - compression failure versus learned-kernel fit;
   - why sup-based aliasing and fit are linked;
   - why projected-dynamics metrics are self-consistency checks;
   - why `eta_q` is the external reference;
   - why conditional rollout and case counts matter;
   - why L0 is reported as a frontier.
5. `rho_pol` now includes the sharper mixture-diameter bound
   `d_F(K_beta,K_beta') <= 1/2 ||w_beta-w_beta'||_1 delta_alias`,
   explicitly without novelty claim.
6. L1_int explains conditioning versus intervention and avoids automatically treating collapse to transition fit as `not applicable`.
7. L2.G/L2.O now explains the endogenous, self-confirming query-distribution loop.
8. L3 explicitly distinguishes system-level robustness from component-level model validity.
9. Toy A foregrounds value of information and direct regret.
10. Toy B foregrounds why nuisance-blind value classes erase nuisance transition errors from Bellman updates.
11. A short subsection explains why the two non-implications form a pair without overclaiming non-degenerate orthogonality.
12. Three-history `rho_pol` diagnostic is presented geometrically.
13. L2.O toy explicitly derives the safe-only query distribution from the model's own erroneous ranking.
14. Eliminativist section is strengthened and ranks the current positive arguments by evidential strength.
15. MMALS section is reframed around adaptive quotient revision `A_t -> A_{t+1}` rather than classification of MMALS.
16. Limitations now include the self-referential nature of projected L0 metrics.
17. Conclusion ends on the adaptive-history distinction question.

## Presentation

- 14 pages (previous draft: 12).
- Compiled twice with pdfLaTeX.
- Rendered and visually inspected page-by-page via contact sheet.
- PDF preflight: openable, unencrypted, non-scanned, no XFA.
