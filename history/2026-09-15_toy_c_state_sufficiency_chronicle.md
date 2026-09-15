# Chronicle — 15 September 2026

## From state sufficiency to future-generating model structure: Toy C v0.1 -> v0.3

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

## Toy C v0.3 — model possession versus model access

v0.3 attacks the remaining word **internally** rather than adding more hidden-state complexity.

The environment is kept identical to v0.2. Three future-query systems are compared on the same finite domain:

- **M — local model owner:** task-relevant dynamics are inside the declared local boundary;
- **F — delegated access:** the local agent owns no predictive mechanism and forwards queries to an external exact model service `O`;
- **G — compiled finite answer object:** all exact answers for the finite benchmark domain are precomputed into a table, with no declared transition, update, rollout-composition or extrapolation rule.

The declared benchmark `D0` contains every reachable history through depth 2 crossed with every future action sequence of length 1, 2 or 3: exactly `4088` queries of the form

`P(Y_{t+k}=1 | h_t, a_{t:t+k-1})`.

The exact verifier gives:

- M: `4088/4088` exact;
- F with the external oracle available: `4088/4088` exact;
- G on its compiled domain: `4088/4088` exact.

Therefore answer correctness on this finite domain cannot identify where, or even in what computational form, the predictive capability resides.

The experiment then changes the evaluation contract in two ways.

### Query-domain extension

For the same history support but horizon-4 action sequences (`4672` queries):

- M: `4672/4672` exact;
- F with oracle: `4672/4672` exact;
- G: `0/4672` coverage, because those queries were never compiled and G has no extrapolation rule.

### External-source removal

When `O` is removed:

- M remains `4088/4088` exact on `D0`;
- F has `0/4088` defined answers;
- G remains `4088/4088` exact on the finite compiled domain, but still cannot extend to the horizon-4 domain.

This produces an operational distinction between **local possession**, **delegated access**, and **finite compilation**, but only after boundary/source dependence and extension are made part of the test contract.

---

## Finite behavioural non-identifiability

v0.3 records an elementary observation without novelty claim.

For any finite declared query set `D` and deterministic exact answer mechanism `M:D -> Y`, the mapping can be compiled into a finite table containing one exact answer for each element of `D`.

Therefore:

> finite behavioural equivalence alone cannot prove internal generative or predictive structure.

This does not make the structures equivalent outside the declared domain. It instead says that an evaluation must include something beyond finite answer matching if the scientific claim concerns **possession of mechanism** rather than **availability of answers**.

Candidate discriminators include domain extension, source removal, interventions on dependencies, architectural inspection, compositional constraints, resource scaling, latency and robustness.

---

## System boundary becomes explicit

Toy C v0.3 exposes a boundary dependence that had remained implicit.

At the **local agent boundary**, F has model access but not model possession.

At an **expanded `F + O` system boundary**, the composite system does contain the external predictive model service.

Therefore the sentence

> “the system has a world model”

is under-specified unless the evaluated boundary is declared.

This is not a new framework layer. For now it is better treated as explicit attribution metadata attached to a capability claim.

---

## Current hypothesis disposition after v0.3

- **H1 — sufficiency alone is insufficient:** unchanged; still only an architectural separation example.
- **H2 — persistent recursive state is necessary:** remains weakened by Agent E in v0.2.
- **H3 — internally owned action-indexed future mechanism:** weakened as a system-level necessity; delegated access reproduces the same declared answers while the local agent owns no model.
- **H4 — breadth is a profile/frontier property:** retained, now complemented by explicit system-boundary and capability-source metadata.

The surviving technical question is now less ontological:

> What future-query capability is available, over which query family, from which source, inside which declared boundary, and how does that capability behave under extension, source removal, intervention and shift?

No accepted framework axis changes.

---

## Relation to the earlier handwritten / MMALS notes

The earlier notes about local models, local-to-global constraints, divergence/conservation analogies, differential geometry, intrinsic dimension, Takens/delay embedding and local charts are now positioned more cleanly.

They are **not ingredients to inject into Toy C merely to make it sophisticated**.

Toy C first asks what structure must be preserved and how that capability is attributed. Only after that question survives falsification do the earlier mathematical bridges become relevant to the harder engineering question:

> How can a high-dimensional, partially observed, multi-regime system discover and maintain the smallest local predictive structures, transition rules and domains of validity needed for those future queries?

v0.3 adds one MMALS-relevant refinement: reusable predictive capability need not sit inside one monolithic internal object. It may be local, delegated, compiled, retrieved or reconstructed. What must remain explicit is the **domain of validity, provenance, dependency, system boundary and extension behaviour** of that capability.

This preserves the MMALS principle: complexity only on evidence.

---

## Next candidate falsification

Do not create a new profile layer from Toy C v0.3.

The next useful target, if pursued, is no longer “what implementation counts as a model?” but whether a **capability contract** can make experimentally different predictions or change an engineering decision:

`(query family, boundary, source, coverage, extension, availability, intervention, shift)`.

If that contract adds no decision-relevant information beyond a flat technical description, the eliminativist alternative becomes stronger.

If it does, the contribution is not a metaphysical definition of world model but an auditable way to qualify future-generating capability in adaptive systems.
