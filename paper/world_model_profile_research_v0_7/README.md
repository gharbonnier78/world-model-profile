# World Model Profile — post-v0.6 research draft v0.7

**Status:** exploratory post-publication research draft. It does not reopen the accepted v0.4 framework spine and does not rewrite the preserved v0.6 milestone.

This package integrates Toy C v0.1 and v0.2 into the manuscript and keeps the exact finite evidence beside the LaTeX/PDF.

Key post-v0.6 findings under falsification:

- Toy C v0.1 separates exact current-state knowledge from possession of a future-generating mechanism.
- Toy C v0.2 makes the predictive quotient genuinely non-injective: task-query aliasing is exactly `0`, while the richer nuisance-query aliasing gap is exactly `19/129`.
- Agent E answers all declared future action-sequence queries exactly without carrying a persistent recursively updated state, weakening a strong recursive-state necessity hypothesis.
- These are finite scoped results, not a necessary-and-sufficient definition of world model.

Reproduce the exact Toy C evidence with:

```bash
python verify_toy_c_v0_1.py
python verify_toy_c_v0_2.py
```

The LaTeX source is reconstructed from the checksum-verified v0.6 source and the versioned patch parts in `research/toy_c_v0_2/`, then compiled by the repository workflow.
