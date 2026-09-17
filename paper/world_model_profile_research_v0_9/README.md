# World Model Profile — post-v0.6 research draft v0.9

**Status:** exploratory post-publication research draft. It does not reopen the accepted v0.4 framework spine and does not rewrite the preserved v0.6 milestone or v0.7/v0.8 research snapshots.

This package integrates Toy C v0.1-v0.4 into the manuscript and keeps the exact finite evidence beside the LaTeX/PDF.

Key Toy C findings under falsification:

- v0.1 separates exact current-state knowledge from possession of future-generating machinery.
- v0.2 constructs a genuinely non-injective task-predictive quotient and weakens persistent recursive-state necessity.
- v0.3 separates local model possession, delegated access, and finite compiled answers.
- v0.4 shows that extension/generalisation is itself typed: Agent H is exact on `4088/4088` baseline queries and `32704/32704` longer-horizon endpoint queries, but has `0/28672` coverage on newly conditioned depth-3 histories and no branch-conditioned hypothetical-evidence interface.
- These are finite scoped results, not a necessary-and-sufficient definition of world model.

Reproduce the exact Toy C evidence with:

```bash
python verify_toy_c_v0_1.py
python verify_toy_c_v0_2.py
python verify_toy_c_v0_3.py
python verify_toy_c_v0_4.py
```

The v0.9 LaTeX source is deterministically transformed from the checksum-pinned v0.8 source by `research/toy_c_v0_4/apply_v0_8_to_v0_9.py`, then compiled by the repository workflow.
