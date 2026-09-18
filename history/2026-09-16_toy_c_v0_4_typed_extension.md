# Chronicle — 16 September 2026

## Toy C v0.4 — typed extension after model possession vs access

**Event type:** deliberately mechanical falsification continuation  
**Evidence status:** exact finite construction; exploratory interpretation  
**Affected program:** World Model Profile / MMALS bridge / Minimal Sufficient Dynamic Inference

## Post-review audit addendum — 18 September 2026

**Purpose:** repair the scientific record without rewriting the contemporaneous v0.4 narrative below.

The independent v0.9 review (`review/INDEPENDENT_REVIEW_V0_9_CLAUDE.md`) judged the Chronicle **COHERENT WITH DRIFT RISK — REPAIR BEFORE NEXT STUDY**. The original text below is intentionally preserved as the record of what was believed when v0.4 was run. The following corrections now govern its interpretation:

1. **H5 was not pre-registered.** The scalar-extension candidate was formulated at v0.4 as an over-reading of v0.3. It should not be presented as if it belonged to the standing H1-H4 set before the experiment.
2. **The pre-registered decision-relevance test was deferred.** Toy C v0.3 and Chronicle 1 had already named the next gate: test whether the capability contract changes a concrete engineering evaluation or decision beyond a flat technical description. v0.4 substituted a different mechanical construction without recording that deferral. This is the first exact drift point identified by review.
3. **Agent H contains predictive structure.** The FLIP-parity rule is the exact task-specific action-conditioned predictive operator `K` in closed form. H is therefore not evidence for long-horizon prediction without model structure. Its cleaner role is to separate predictive propagation `K` from observation-assimilation/update `U`.
4. **Branch-conditioned F required a verifier repair.** The original v0.4 code assigned `f = m` on that domain. The repaired verifier now exercises the delegated F path independently and checks source removal. H/G are recorded as `NOT_IMPLEMENTED` on that interface rather than as measured failures.
5. **The typed-extension tuple is not a new taxonomy.** Most of its directions are already components of the accepted declaration tuple `D` (query family, horizon, support, intervention, shift). Source/system-boundary provenance remains useful extra evaluation metadata from v0.3.
6. **The MMALS bridge remains hypothetical.** Toy C does not change the abstraction family. The source MMALS lifecycle is restored as `REUSE -> ADAPT -> FORK -> CANDIDATE NEW REGIME -> VERIFY -> REMEMBER`, with later merge/prune/retire decisions.

**Restored next gate:** no Toy C v0.5 and no regime-change study yet. First run the v0.3 decision-relevance / eliminativist test with its stop condition intact: if capability-contract metadata changes no engineering decision beyond the flat technical description, the mechanical Toy C chain stops and the eliminativist alternative is strengthened.

---

### Trigger

Toy C v0.3 had weakened the idea that local model possession can be inferred from correct future-query behaviour. A local model owner, a delegated oracle client and a finite compiled answer table were exactly equivalent on the declared finite benchmark. They separated only when the evaluation contract added source removal and query-domain extension.

The next mechanical question was therefore:

> Is “ability to extend beyond the finite benchmark” itself a meaningful scalar discriminator of model-like structure?

Toy C v0.4 attacks that candidate directly without changing the environment.

The accepted v0.4 framework spine remains frozen. No new framework layer is introduced.

---

## Agent H — a factorised task-query program

The same task POMDP is retained. For each reachable conditioning history through depth 2, Agent H stores one scalar

`q(h) = P(Y_next=1 | h, STAY)`.

There are exactly `292` such history seeds.

H has no declared hidden-state model, nuisance model, observation-update rule, recursively stored latent state, or external model service. It only applies one algebraic identity specific to the declared endpoint query:

- even number of `FLIP` actions -> return `q(h)`;
- odd number of `FLIP` actions -> return `1-q(h)`.

This works because the task dynamics are deterministic under `STAY/FLIP`: repeated action composition depends only on FLIP parity.

The experiment deliberately does not decide whether H should be called a model. It measures what H can and cannot extend.

---

## Exact baseline

On the same `D0` benchmark used in v0.3 — every history through depth 2 crossed with future action-sequence lengths 1, 2 and 3 — the verifier checks exactly `4088` queries.

All four mechanisms agree with the environment-derived truth:

- M local model owner: `4088/4088`;
- F with external oracle: `4088/4088`;
- G finite compiled answer table: `4088/4088`;
- H factorised query program: `4088/4088`.

G uses `4088` query-answer entries. H uses `292` history seeds plus one rule. The ratio `4088/292 = 14` is recorded only as entry-count bookkeeping; it is not presented as an MDL or complexity theorem because the description length of H's rule is not included.

---

## Extension is not one thing

### Future-horizon extension

The conditioning histories are held fixed, but future action-sequence lengths are extended to 4, 5 and 6. This produces exactly `32704` new queries.

Results:

- M: `32704/32704` exact;
- F with oracle: `32704/32704` exact;
- G: `0/32704` defined;
- H: `32704/32704` exact.

So H extrapolates perfectly to a substantially larger future horizon without receiving any new per-query table entries.

The implementation is also exhaustively checked for all 292 supported histories and all binary action sequences of lengths 1 through 8: `148920/148920` exact comparisons.

### Conditioning-history extension

The future-query lengths return to 1–3, but the conditioning support is extended to newly observed histories at depth 3. This produces exactly `28672` queries.

Results:

- M: `28672/28672` exact;
- F with oracle: `28672/28672` exact;
- G: `0/28672` defined;
- H: `0/28672` defined.

H has no seed for those new histories and no declared observation-update rule from which to generate one.

Therefore:

`future-horizon extension != conditioning-history extension`.

---

## Open-loop extension versus hypothetical evidence assimilation

v0.4 also introduces a branch-conditioned query:

`P(Y_{t+2}=1 | h_t, a0, hypothetical Y_{t+1}=y1, a1)`.

The domain contains `2336` queries.

M and F are exact on all `2336/2336` queries because they can assimilate the hypothetical new observation before continuing the prediction.

G and H expose no such interface.

This gives another distinction that a generic claim such as “supports long-horizon prediction” would hide:

- open-loop endpoint extrapolation;
- branch-conditioned evidence assimilation and continuation.

---

## Source removal no longer separates everything

v0.3 used external-source removal to distinguish delegated Agent F from local Agent M.

H now adds a useful counterpoint. When the external oracle is removed:

- F has `0/4088` defined answers on `D0`;
- H remains `4088/4088` exact on `D0`;
- H remains `32704/32704` exact on the horizon-extension domain.

So **local availability + source independence + long-horizon extension** still do not imply a full generative/update model under the declared interface.

---

## Hypothesis disposition after v0.4

- **H1 — current-state sufficiency alone:** unchanged as an insufficient architectural discriminator.
- **H2 — persistent recursive state is necessary:** remains weakened by Agent E from v0.2.
- **H3 — local internal ownership is necessary:** remains weakened by delegated Agent F from v0.3.
- **H5 — extension is a scalar modelhood discriminator:** weakened by Agent H. H passes future-horizon extension while failing conditioning-history and branch-conditioned extension.

The surviving methodological requirement is more precise:

> Any claim of generalisation or extension should name the axis that changed.

A provisional typed view is therefore:

`E = (horizon, conditioning-history, query-family, branch/evidence, source, intervention, shift)`.

This is metadata for qualification, not a new accepted layer.

---

## MMALS bridge

Toy C v0.4 reconnects directly with the Minimal Sufficient Dynamic Inference programme.

A small structure can generalise indefinitely in one direction while being unable to absorb one new observation or one newly relevant variable. The important engineering object is therefore not simply “minimal model” but:

> the smallest structure sufficient for the declared query contract, together with an auditable record of the extension axes it supports without reconstruction, reacquisition or replacement.

This gives a cleaner route toward adaptive abstraction:

`A_t -> A_{t+1}`

need not be triggered by undifferentiated prediction error. It can be triggered by a specific contract failure: new history support, new query, new action semantics, new evidence channel, intervention or regime shift.

---

## Next transition

Toy C v0.4 completes the deliberately mechanical chain:

`state -> recursive dynamics -> direct-history model -> delegated access -> finite compilation -> typed extension`.

A next step would be scientifically different rather than another bookkeeping extension: introduce an actual **regime change, altered action semantics, altered observation channel, or newly relevant query**, then test whether the typed capability contract predicts which mechanism must be adapted, refined, reacquired or replaced.

That is the natural point at which the World Model investigation reconnects with MMALS adaptive abstraction rather than continuing to search for a single architectural predicate.
