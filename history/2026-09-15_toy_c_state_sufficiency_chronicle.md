# Chronicle — 15 September 2026

## From state sufficiency to future-generating model structure: Toy C v0.1 -> v0.2

**Event type:** post-publication research transition / falsification cycle  
**Evidence status:** exact finite constructions; exploratory interpretation  
**Affected program:** World Model Profile / MMALS bridge / minimal sufficient dynamic inference

### Trigger

After publishing the v0.6 World Model Profile milestone, the next question was deliberately narrowed:

> When does a sufficient representation of history become an actual internal model of the world — and is that transition a real technical boundary or only a naming convention?

The question reconnects with the earlier MMALS program note on **Minimal Sufficient Dynamic Inference** (24 August 2026): seek the smallest explainable inference system that remains dynamically sufficient, increase structure only when evidence requires it, and distinguish state compression from explicit predictive transition dynamics.

The accepted v0.4 profile remains frozen. This cycle does not introduce a new layer.

---

## Toy C v0.1 — first separation

Toy C v0.1 used the smallest binary partially observed process that could distinguish:

- **Agent A:** exact current belief supplied by an oracle, but no owned transition/update/rollout mechanism;
- **Agent B:** compact recursive predictive state with exact action-conditioned prediction and rollout but no explicit hidden-state ontology;
- **Agent C:** full generative transition/observation model and Bayesian belief update;
- **Control D:** exact one-step lookup on finite memorised support.

The verifier established exact B/C equivalence for the declared prediction, update, rollout and one-step decision queries. It also showed that exact one-step lookup fit on finite support does not provide held-out compositional coverage.

The important limitation was immediately recorded: in v0.1 the predictive state `q` was an affine bijection of the full binary belief. Therefore the result did **not** yet demonstrate a genuinely information-losing predictive quotient.

---

## Toy C v0.2 — attack the limitation instead of extending the claim

v0.2 introduces a two-component hidden state

`S_t = (X_t, N_t)`

with:

- `X`: task-relevant, action-controlled dynamics;
- `N`: independently evolving nuisance dynamics;
- `Y`: noisy observation of `X`;
- `Z`: noisy observation of `N`.

The full posterior is two-coordinate:

`(bX_t, bN_t)`.

The task predictive state remains one-dimensional:

`q_t = P(Y_{t+1}=1 | h_t, STAY)`.

This creates an actual quotient: histories can have the same `q_t` while carrying different nuisance beliefs `bN_t`.

The exact verifier enumerates all reachable histories through depth 3 and reports:

- all `Q_task` B/C/E checks exact;
- zero task-query aliasing inside every `q` cell;
- positive nuisance-query aliasing, with maximum exact gap `19/129` for `P(Z_{t+1}=1)`;
- a witness with the same `q = 21/82` but nuisance beliefs `17/129` and `112/129`;
- one-step lookup control D exact on 72 memorised entries but with `0/512` held-out depth-2 coverage.

Thus the same internal representation is exactly sufficient for the declared task query family and provably insufficient for a richer query family. This reinforces the **abstraction/query frontier** interpretation rather than a global reconstruction requirement.

---

## Agent E and the first attempted falsification of H2

v0.2 adds **Agent E**, a direct-history sequence model.

Agent E owns the exact task-relevant dynamics but stores no persistent recursively updated latent state. For each hypothetical future query it recomputes the relevant posterior from the complete history and evaluates the requested action sequence.

It is exact on all 1080 tested open-loop action-sequence queries.

This weakens the strong candidate hypothesis:

> “modelhood requires a persistently stored recursively updateable internal state.”

The surviving candidate is weaker and more implementation-neutral:

> a model-like system internally owns a mechanism able to answer declared future, action-indexed queries away from the currently realised trajectory.

This mechanism may be recursive, generative, predictive-state based, or computed directly from history.

This is **not yet a definition**.

---

## Current hypothesis disposition

- **H1 — sufficiency alone is insufficient:** retained only as an architectural separation example; Agent A has exact current belief but no future-generating interface.
- **H2 — recursive closure is necessary:** weakened by Agent E; persistent recursive state storage is not necessary in this finite construction.
- **H3 — action-indexed future consequences:** survives v0.2 as the common capability of B, C and E.
- **H4 — breadth is better treated as a profile/frontier:** strengthened by exact task sufficiency and exact nuisance-query failure under the same quotient.

No accepted framework axis changes.

---

## Relation to the earlier handwritten / MMALS notes

The earlier notes about local models, local-to-global constraints, divergence/conservation analogies, differential geometry, intrinsic dimension, Takens/delay embedding and local charts are now positioned more cleanly.

They are **not ingredients to inject into Toy C merely to make it sophisticated**.

Toy C first asks what structure must be preserved. Only after that question survives falsification do the earlier mathematical bridges become relevant to the harder engineering question:

> How can a high-dimensional, partially observed, multi-regime system discover and maintain the smallest local predictive structures, transition rules and domains of validity needed for those future queries?

This preserves the MMALS principle: complexity only on evidence.

---

## Next candidate falsification

Do not add Toy C v0.3 automatically.

If the programme continues, attack the remaining H3-like candidate by separating:

- **possession of an internal future-query mechanism**;
- **access to answers derived elsewhere from such a mechanism**.

Candidate controls could include an external oracle, cached planner answers, or a policy/value object that supports decisions without exposing predictive dynamics.

The question becomes:

> What observable technical property distinguishes owning a model from merely having access to model-derived answers?

Until that distinction is experimentally useful, the eliminativist option remains live: report the technical tuple and query frontier rather than force a binary “world model” predicate.
