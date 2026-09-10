# World Model Profile

A research repository for defining, formalizing, and empirically testing layered world-model capabilities, with explicit evidence, review, and falsification criteria.

## Current status

The framework spine reached **`ACCEPT AS FRAMEWORK SPINE`** at v0.4 after successive independent-review cycles.

The accepted profile is intentionally not presented as a unique or necessary-and-sufficient definition of a world model. It is an evaluation/explication framework that separates:

- **L0** — predictive abstraction / closure, reported as an abstraction frontier;
- **L1_int** — interventional validity;
- **L2.G / L2.O** — decision-relative global and operational adequacy;
- **L3** — robustness under a declared shift class.

Acquisition-policy exposure `rho_pol` is retained as an attribution diagnostic **inside L0**, not as an independent axis.

Two exact finite constructions currently establish only the scoped non-identity claims:

- `L0 ⇏ L2`;
- `L2.G ⇏ L0`.

The eliminativist alternative — report the underlying technical tuple directly and retire “world model” as a predicate — remains open.

## Repository structure

```text
framework/
  accepted-v0.4/   Frozen accepted framework spine, executable evidence,
                   review handoff, reviewer lineage, and acceptance review.

history/
  v0.1/            Initial working definition and first review cycle.
  v0.2/            First L0–L3 formalisation and finite toy.
  v0.3/            Bidirectional-separation revision and reviewer package.

paper/
  README.md        Manuscript work starts here; accepted spine remains frozen.

research/
  OPEN_QUESTIONS.md
                   Manuscript-only obligations and unresolved research questions.
```

## Reproducibility

The accepted package contains the executable verification script and machine-readable results. The reviewer independently reran the v0.4 package and returned `ACCEPT AS FRAMEWORK SPINE`.

Start with:

1. [`framework/accepted-v0.4/16_INDEPENDENT_REVIEW_V0_4_SPINE_ACCEPTED.md`](framework/accepted-v0.4/16_INDEPENDENT_REVIEW_V0_4_SPINE_ACCEPTED.md)
2. [`framework/accepted-v0.4/01_LAYERED_PROFILE_V0_4_FORMAL_SPEC.md`](framework/accepted-v0.4/01_LAYERED_PROFILE_V0_4_FORMAL_SPEC.md)
3. [`framework/accepted-v0.4/12_LAYERED_PROFILE_V0_4_NOTE.pdf`](framework/accepted-v0.4/12_LAYERED_PROFILE_V0_4_NOTE.pdf)
4. [`framework/accepted-v0.4/03_verify_v0_4.py`](framework/accepted-v0.4/03_verify_v0_4.py)

## Relation to MMALS

This work emerged from questions raised by MMALS about state, history compression, dynamic inference, regime change, and adaptive abstraction. The present repository is intentionally separate because the world-model definition/profile problem has become an autonomous research object.

Related repository: https://github.com/gharbonnier78/mmals

## Claim discipline

This repository does **not** currently claim:

- a new general theory of world models;
- necessary and sufficient conditions for all world models;
- novelty of classical state abstraction, bisimulation, AIS, or value-equivalence phenomena;
- that MMALS is a world model;
- that the layered profile has defeated the eliminativist alternative.

The accepted spine is frozen. New work belongs in `paper/` or `research/` unless a new review cycle is explicitly opened.
