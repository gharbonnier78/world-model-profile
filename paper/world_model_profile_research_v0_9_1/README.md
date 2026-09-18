# World Model Profile — post-v0.6 research draft v0.9.1

**Status:** repairs-only revision after the independent v0.9 review. No new Toy C experiment is introduced and the accepted v0.4 framework spine remains frozen.

This package:
- preserves v0.9 as the independently reviewed snapshot;
- repairs the delegated F branch-conditioned verifier path and source-removal check;
- reinterprets Agent H as owning the task-specific predictive operator K while lacking observation-assimilation/update U;
- adds PSR, Dyna, and classical partial-observation/filtering prior art at point of use;
- records that the v0.4 scalar-extension candidate was formulated at v0.4 rather than pre-registered;
- preserves the original Chronicle narrative and adds a dated review addendum rather than rewriting history;
- restores the pre-registered decision-relevance / eliminativist test as the next research gate.

Reproduce the exact Toy C evidence with:

```bash
python verify_toy_c_v0_1.py
python verify_toy_c_v0_2.py
python verify_toy_c_v0_3.py
python verify_toy_c_v0_4.py
```

v0.9.1 is deterministically transformed from the checksum-pinned v0.9 TeX by `research/v0_9_1_repairs/apply_v0_9_to_v0_9_1.py`.
