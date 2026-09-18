# Manuscript Workspace

The accepted v0.4 framework spine is frozen under `../framework/accepted-v0.4/`. The manuscript is built **around** that spine rather than editing the accepted artifact in place.

## Preserved milestones and snapshots

- v0.6 published/preserved milestone: [`world_model_arxiv_draft_v0_6/`](world_model_arxiv_draft_v0_6/)
- v0.7 preserved research snapshot: [`world_model_profile_research_v0_7/`](world_model_profile_research_v0_7/)
- v0.8 preserved research snapshot: [`world_model_profile_research_v0_8/`](world_model_profile_research_v0_8/)
- v0.9 independently reviewed snapshot: [`world_model_profile_research_v0_9/`](world_model_profile_research_v0_9/)

v0.9 remains preserved exactly as the evidence target reviewed in `../review/INDEPENDENT_REVIEW_V0_9_CLAUDE.md`.

## Current repairs-only package: v0.9.1

The current exploratory authoring package is:

- [`world_model_profile_research_v0_9_1/`](world_model_profile_research_v0_9_1/)
- [PDF](world_model_profile_research_v0_9_1/world_model_profile_research_v0_9_1.pdf)
- [LaTeX](world_model_profile_research_v0_9_1/world_model_profile_research_v0_9_1.tex)
- [SHA-256 manifest](world_model_profile_research_v0_9_1/SHA256SUMS.txt)

**v0.9.1 is repairs-only.** It introduces no new Toy C experiment and does not reopen the accepted v0.4 spine.

The repair:
- independently exercises delegated Agent F on branch-conditioned queries and source removal;
- reinterprets H correctly as owning the task-specific predictive operator `K` while lacking observation-assimilation/update `U`;
- changes “falsifying” language to “weakening” / candidate-criterion language;
- adds PSR, Dyna and classical prediction/filtering prior art at point of use;
- records that the scalar-extension candidate was formulated at v0.4, not pre-registered;
- recognises that most proposed typed-extension directions are already contained in declaration tuple `D`;
- preserves the original Chronicle and adds a dated post-review audit addendum instead of rewriting history;
- restores the pre-registered decision-relevance / eliminativist test as the next gate.

The v0.9.1 build completed successfully in GitHub Actions run `35302749759`.

Current checksums:
- TeX: `901ad01adb74915aff8b223be52c61374d7d01760a45be855cb28f619eda943f`
- PDF: `5c28530580928eb092f3d1f732fff4ec7b3d47786a34800397ea2ca35961d5ef`

## Current research direction

Toy C has decomposed several candidate binary “modelhood” boundaries into technical components rather than converging on one necessary-and-sufficient predicate. The next question is therefore deliberately decision-relative:

> Does the capability contract add engineering decision value beyond a flat technical description such as `(sigma, U, K, Q, boundary, source, ...)`?

No Toy C v0.5 and no regime-change construction should be opened before that gate is resolved.

See:
- `../review/INDEPENDENT_REVIEW_V0_9_CLAUDE.md`
- `../review/RESPONSE_TO_INDEPENDENT_REVIEW_V0_9.md`
- `../research/OPEN_QUESTIONS.md`
- Chronicle under `../history/`.
