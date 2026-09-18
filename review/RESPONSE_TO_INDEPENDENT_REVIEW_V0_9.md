# Response to Independent Review — v0.9

**Reviewed target:** `c209b7adbbee3444319cb775c99ce572f301d37e`  
**Review:** `review/INDEPENDENT_REVIEW_V0_9_CLAUDE.md`  
**Disposition:** manuscript `ACCEPT WITH CHANGES`; Chronicle `COHERENT WITH DRIFT RISK — REPAIR BEFORE NEXT STUDY`  
**Response artifact:** v0.9.1 repairs-only  
**No new experiment:** yes

## Response principle

The independently reviewed v0.9 package is preserved unchanged as the review target. v0.9.1 does not reinterpret history by replacing the v0.9 snapshot; it creates a new repairs-only package and adds a dated Chronicle audit addendum.

The accepted v0.4 framework spine remains frozen.

## Blocking findings

### 12.1 — delegated F branch-conditioned result was not independently measured

**Accepted.**

Original defect: the branch path in `verify_toy_c_v0_4.py` assigned `f = m`, so the delegated dependency could not be exercised independently.

**Repair:**
- added a branch-conditioned external oracle path and an `answer_F_branch(..., service_available=...)` wrapper;
- F is now independently evaluated on all 2336 branch queries;
- with O available: `2336/2336` exact;
- with O removed: `0/2336` defined;
- H/G are reported as `NOT_IMPLEMENTED` on this interface rather than scored as failures.

Artifacts:
- `research/toy_c_v0_4/verify_toy_c_v0_4.py`
- `research/toy_c_v0_4/results_v0_4.json`
- v0.9.1 finite-results table and reproducibility section.

### 12.2 — missing PSR / Dyna and prediction-vs-filtering prior art

**Accepted.**

**Repair:** v0.9.1 adds point-of-use references to:
- Sutton, *Dyna, an integrated architecture for learning, planning, and reacting* (1991);
- Littman, Sutton & Singh, *Predictive Representations of State* (2001);
- Åström, *Optimal Control of Markov Processes with Incomplete State Information* (1965);
- Striebel, *Sufficient Statistics in the Optimum Control of Stochastic Systems* (1965).

The Toy C section now identifies Agent B with the predictive-state lineage and v0.4 with the classical prediction/filtering distinction.

### 12.3 — “falsifying” overstated a self-authored candidate criterion

**Accepted.**

**Repair:** `Agent E: falsifying...` is retitled `Agent E: weakening...`. v0.9.1 explicitly states that H1–H4 and the v0.4 candidate are project-authored candidate criteria; the toys are finite counterexamples / weakening evidence, not falsifications of a general theory in the literature.

### 12.4 — H5 was presented as if pre-registered

**Accepted.**

**Repair:** the v0.4 spec, results, manuscript and Chronicle addendum now state that the scalar-extension candidate was formulated **at v0.4** as a candidate over-reading of v0.3. It is not presented as a standing pre-registered H5.

### 12.5 — the pre-registered v0.3 decision-relevance test was deferred without being recorded

**Accepted. This is treated as the key trajectory repair.**

**Repair:** the original 16 September Chronicle remains untouched below a new dated 18 September audit addendum. The addendum records:
- the decision-relevance test was already the registered next gate after v0.3;
- v0.4 substituted a mechanical extension test without contemporaneously recording that deferral;
- the decision-relevance / eliminativist test is restored as the next research gate with its stop condition intact.

No Toy C v0.5 or regime-change study is opened before that gate.

## Main interpretation repair — Agent H

The review's central interpretation is accepted.

H's parity rule is the exact task-specific action-conditioned predictive operator `K` in closed form. H therefore does **not** demonstrate long-horizon prediction without predictive model structure.

In the provisional decomposition

`M = (sigma, U, K, Q)`

H is best read as having supported `sigma`, `K`, and endpoint query semantics `Q`, but no implemented observation-assimilation/update operator `U` for new evidence.

The repaired v0.4 conclusion is therefore:

> **predictive propagation K and filtering/update U are separable components in this finite construction.**

This is narrower than the original typed-extension interpretation and is consistent with classical partial-observation filtering.

## Non-blocking findings

### `4088/292 = 14`

**Accepted.** It is now described as the identity `2+4+8`, the number of baseline action sequences per supported history. No compression/MDL significance is implied.

### `E` versus accepted declaration tuple `D`

**Accepted.** v0.9.1 does not defend `E` as a new taxonomy. Horizon, history support, query family, intervention and shift are mapped back to existing declaration components. Source/system-boundary provenance remains useful extra systems-engineering metadata exposed by v0.3.

No L4 is proposed.

### Three inconsistent capability-contract forms

**Reconciled by retiring the independent `E` taxonomy.** The current decision-relevance test will compare:
- the flat technical description;
- the accepted declaration/profile information;
- additional source/boundary provenance where relevant.

It will not treat the successive historical tuple spellings as an established taxonomy.

### H history-extension and branch failures share missing `U`

**Accepted.** v0.9.1 states this explicitly and does not present them as independent discoveries.

### Separation-by-construction risk

**Accepted as a methodological warning.** The Chronicle addendum and v0.9.1 framing stop the mechanical Toy C chain rather than creating another same-environment separation.

### MMALS fidelity

**Accepted.** The lifecycle is restored as:

`REUSE -> ADAPT -> FORK -> CANDIDATE NEW REGIME -> VERIFY -> REMEMBER`

with later merge/prune/retire decisions. The `A_t -> A_{t+1}` bridge remains a future hypothesis; Toy C did not itself adapt the abstraction family.

### Actual through-line

**Accepted.** v0.9.1 explicitly acknowledges that repeated candidate binary boundaries decomposed into separate technical components and that the research object began to shift from “what makes a model?” toward “how should future-query capability be qualified?”. The decision-relevance test is now required to determine whether that shift adds value or should terminate in an eliminativist conclusion.

## Mechanical closure

GitHub Actions run `35302749759` completed successfully:
- all Toy C v0.1–v0.4 exact outputs reproduced against their committed JSON;
- the pinned v0.9 TeX was deterministically transformed into v0.9.1;
- v0.9.1 compiled successfully to PDF;
- the package manifest was generated and the package committed.

v0.9.1 hashes:
- TeX: `901ad01adb74915aff8b223be52c61374d7d01760a45be855cb28f619eda943f`
- PDF: `5c28530580928eb092f3d1f732fff4ec7b3d47786a34800397ea2ca35961d5ef`

## Next gate / stop condition

Next experiment: **Decision-Relevance Test v0.1**.

Question:

> Does capability-contract metadata change a concrete engineering evaluation or decision beyond what a flat technical description already determines?

Stop condition:

> If it changes no decision-relevant outcome beyond the flat description, the eliminativist alternative is strengthened and the mechanical Toy C chain stops.

A regime-change / adaptive-abstraction experiment is deferred until this gate is resolved.
