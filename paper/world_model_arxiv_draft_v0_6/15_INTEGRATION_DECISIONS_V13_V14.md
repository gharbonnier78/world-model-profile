# 15 — Integration Decisions for v13 / v14

**Target:** next author-owned arXiv rewrite  
**Status:** integration memo, not a manuscript revision  
**Frozen scientific spine:** v0.4 `ACCEPT AS FRAMEWORK SPINE`

## Decision summary

- **v13 prose expansion:** integrate broadly, but revise several overstatements before use.
- **v14 engineering register:** integrate selectively as an invisible writing register, not as a second conceptual layer.
- **Do not change the accepted spine.**
- **Do not turn the sharper `rho_pol` inequality into a novelty claim.**

---

## 1. v13 — adopt

### §3 four-beat explanation pattern

For every quantity:
1. what it measures;
2. which failure it catches;
3. which failure it structurally cannot catch;
4. why this form is used instead of the obvious alternative.

This materially improves the paper.

### L0 self-consistency vs external reference

Keep the distinction:

- `delta_alias`, `delta_fit`, `delta_roll` operate inside the projected representation;
- `eta_q` is the external anchor against a declared query.

This is one of the clearest explanations of L0's limitation.

### Toy A mechanism

Keep and foreground:

> the hidden mode affects reward but not the projected phase dynamics; the probe makes the discarded distinction actionable.

Direct regret, not AP1 failure, remains the certificate.

### Toy B mechanism

Keep:

> Bellman updates integrate the declared value function over the next-state law; if the value class is constant in nuisance `n`, errors in the `n` marginal disappear from the update.

### L2.G / L2.O self-confirming loop

Keep strongly:

> the model can influence the query distribution under which its own accuracy is measured.

This is the best intuitive justification for the global/operational split.

### Eliminativist steelman

Keep. The paper is stronger if it states that the profile may add reporting structure without adding information.

---

## 2. v13 — adapt before use

### Introduction video-predictor example

Do **not** write that a video predictor necessarily "has nothing to say" about actions.

Use a restricted example:

> a passive or non-action-conditioned video predictor may be predictively strong at observation level while providing no declared intervention or decision semantics.

### MuZero hook

Do **not** write:

> "By any predictive-closure standard it is a poor model."

Too strong.

Use:

> MuZero's learned dynamics need not be a faithful environment simulator across unseen policies, yet can support strong planning on the query distribution induced by search.

### Abstraction frontier language

Replace:

> "A pass with no exhibited failure is not a pass."

with:

> "For a frontier-style L0 claim, a pass without a tested richer level or other non-vacuity certificate is incomplete."

The first wording sounds like a theorem; the second matches the framework's reporting rule.

### `rho_pol` sharper inequality

The inequality

`rho_pol <= 1/2 ||w - w'||_1`

is useful, but present it as an elementary mixture-diameter consequence, not a new proposition, unless a dedicated prior-art search establishes novelty.

### L1_int online case

Avoid automatically reporting `not applicable` whenever conditioning and intervention coincide. The safer distinction is:

- if the intended L1 question adds no information beyond ordinary transition fit in the declared setting, record that explicitly;
- use `not applicable` only when the intervention claim itself is outside scope.

---

## 3. v14 — adopt selectively

The strongest insight is that the framework has the structure of an **evaluation discipline**:

- scope is declared before measurement;
- budgets are explicit;
- coverage is reported;
- `fail`, `not declared`, and `not applicable` are distinct;
- self-consistency is separated from external reference;
- a system can select the operating points on which it appears accurate.

This register makes the formalism easier to reason about without adding an "intuition layer".

Useful terms:
- declared scope / validity envelope;
- budget / threshold;
- coverage / admissible cases;
- external reference / traceability;
- fault observability / excitation;
- self-selected operating points;
- component failure masked by system-level compensation.

---

## 4. v14 — do not overclaim the correspondence

Do **not** retain:

> "Not a metaphor. Each row is the same object under two names."

The mathematical objects and engineering concepts are not literally identical.

Prefer:

> "The profile follows a reporting discipline structurally similar to engineering qualification: scope is declared before measurement, budgets and coverage are explicit, and untested conditions are not reported as passes."

This keeps the precision without inviting an argument about ontology.

Also keep the register:
- out of the abstract;
- out of related-work theorem statements;
- out of the eliminativist concession;
- free of certification standards/acronyms and domain-specific examples.

---

## 5. Reference checks triggered by v13

Verified as distinct 2026 records:

- **Xinyuan Chen et al.**, *A Definition and Roadmap for World Models*, arXiv:2607.06401 (7 Jul 2026).
- **Santiago Cifuentes**, *General Agents Contain World Models, even under Partial Observability and Stochasticity*, arXiv:2602.03146 (3 Feb 2026).

Cifuentes is distinct from:
- the ICML/PMLR three-author paper *General agents need world models*;
- the later four-author arXiv version *General agents contain world models*.

Keep the bibliographic records separate.

---

## 6. Recommended rewrite shape

### Introduction
Use the binary-label problem, but with carefully scoped contrasting examples. Bring the motivating MMALS question in one short paragraph:

> which distinctions between histories may an adaptive learner safely discard?

### Related work
Stay entirely in the literature's vocabulary. State the state-abstraction boundary early.

### Formal profile
Use v13's failure-first explanatory rhythm plus selected v14 operational language.

### Finite evidence
Toy A as value-of-information; Toy B as declared-value-class blindness.

### Diagnostics
Three-history `rho_pol` geometry; L2.O closed-loop illustration. Clearly label both manuscript-only illustrations.

### Eliminativist section
No engineering register. Steelman the flat tuple.

### MMALS / future work
Prefer the stronger research question over an attempt to classify MMALS:

`A_t -> A_{t+1}`

How should an adaptive learner revise which distinctions are retained as tasks, evidence channels, interventions, or regimes change?

---

## 7. Current strongest ending question

> **Which distinctions between histories should an adaptive learner preserve, and which may it safely quotient away as its actions, evidence channels, tasks, and operating regimes change?**

This is more scientifically durable than ending on the definition of "world model".
