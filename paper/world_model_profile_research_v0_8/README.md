# World Model Profile — post-v0.6 research draft v0.8

**Status:** exploratory post-publication research draft. It does not reopen the accepted v0.4 framework spine and does not rewrite the preserved v0.6 milestone or v0.7 research draft.

This package integrates Toy C v0.1-v0.3 into the manuscript and keeps the exact finite evidence beside the LaTeX/PDF.

Key post-v0.6 findings under falsification:

- v0.1 separates exact current-state knowledge from possession of a future-generating mechanism.
- v0.2 makes the predictive quotient genuinely non-injective: task-query aliasing is exactly `0`, while the richer nuisance-query aliasing gap is exactly `19/129`; it also weakens persistent recursive-state necessity.
- v0.3 separates local model possession, delegated external access, and finite compiled answers. All are exact on the declared 4088-query finite domain, but horizon extension and external-source removal distinguish their provenance and coverage.
- These are finite scoped results, not a necessary-and-sufficient definition of world model.

Reproduce the exact Toy C evidence with:

```bash
python verify_toy_c_v0_1.py
python verify_toy_c_v0_2.py
python verify_toy_c_v0_3.py
```

The v0.8 LaTeX source is deterministically transformed from the checksum-pinned v0.7 source by `research/toy_c_v0_3/apply_v0_7_to_v0_8.py`, then compiled by the repository workflow.
