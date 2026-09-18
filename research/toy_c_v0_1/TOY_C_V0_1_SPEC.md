# Toy C v0.1 — State without model / predictive model without ontology

**Status:** exploratory exact finite construction.  
**Research branch:** `research/state-sufficiency-vs-world-modelhood`  
**Relationship to accepted framework:** does **not** modify or reopen the frozen v0.4 framework spine.  
**Purpose:** test the narrow post-v0.6 question: what measurable structure separates a sufficient current state from an internal model that can generate future consequences?

This toy follows two prior research threads:

- `research/STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md`
- MMALS `docs/program/MMALS_DYNAMIC_MINIMAL_INFERENCE_PROGRAM_2026-08-24.md`

The latter motivates minimal sufficient dynamic inference, observability/reconstruction, local geometry, and intrinsic dynamic dimension. Toy C v0.1 deliberately does **not** introduce those richer tools yet. It first isolates what must be preserved.

---

## 1. Environment

Let the hidden state be

\[
S_t\in\{0,1\}.
\]

The observation is binary and noisy:

\[
P(O_t=S_t)=\frac34,
\]

equivalently,

\[
P(O_t=1\mid S_t=1)=\frac34,
\qquad
P(O_t=1\mid S_t=0)=\frac14.
\]

There are two actions \(a_t\in\{0,1\}\).

For \(a=0\), the state is preserved:

\[
P(S_{t+1}=1\mid S_t=1,a=0)=1,
\qquad
P(S_{t+1}=1\mid S_t=0,a=0)=0.
\]

For \(a=1\), the dynamics are stochastic and anti-persistent:

\[
P(S_{t+1}=1\mid S_t=1,a=1)=\frac14,
\qquad
P(S_{t+1}=1\mid S_t=0,a=1)=\frac34.
\]

The initial prior is

\[
P(S_0=1)=\frac12.
\]

The conventional belief state is the scalar

\[
b_t=P(S_t=1\mid h_t),
\]

with history

\[
h_t=(o_{\le t},a_{<t}).
\]

The hidden process therefore has a one-dimensional belief state.

---

## 2. Agent A — Oracle current state, no model

Agent A receives the exact current belief

\[
b_t
\]

from an oracle after each real observation.

It is **not** given:

- the transition law \(T\);
- the observation law \(O\);
- a Bayesian/filtering update rule;
- a future prediction operator;
- a rollout operator.

Agent A can answer current-state queries exactly, e.g.

\[
P(S_t=1\mid h_t)=b_t.
\]

But between oracle refreshes it has no internal mechanism for computing

\[
P(O_{t+1}\mid h_t,a_t)
\]

or for rolling the state forward under hypothetical action sequences.

This is a controlled **state-without-model** edge case. Its lack of future capability is architectural, not a numerical prediction error.

---

## 3. Agent C — Full generative model

Agent C owns the conventional hidden-state model and belief filter.

For action \(a=0\),

\[
b^-_{t+1}=b_t.
\]

For action \(a=1\),

\[
b^-_{t+1}
=
\frac14 b_t+\frac34(1-b_t)
=
\frac34-\frac12 b_t.
\]

The next-observation probability is

\[
P(O_{t+1}=1\mid h_t,a_t)
=
\frac14+\frac12 b^-_{t+1}.
\]

After observation \(o_{t+1}\), Agent C applies the exact Bayesian update.

For \(o=1\),

\[
b_{t+1}
=
\frac{3b^-_{t+1}}{1+2b^-_{t+1}}.
\]

For \(o=0\),

\[
b_{t+1}
=
\frac{b^-_{t+1}}{3-2b^-_{t+1}}.
\]

This is the conventional **generative-model + belief-state** reference.

---

## 4. Agent B — Recursive predictive state, no explicit hidden-state ontology

Define the predictive state

\[
q_t
=
P(O_{t+1}=1\mid h_t,a_t=0).
\]

Because action \(0\) preserves the current hidden state,

\[
q_t
=
\frac14+\frac12 b_t.
\]

Hence \(q_t\in[1/4,3/4]\). The mapping is invertible:

\[
b_t=2q_t-\frac12.
\]

In Toy C v0.1 this means \(q_t\) is **not** a nontrivial compression of the belief state. It is deliberately an alternative predictive coordinate.

### 4.1 Action-conditioned one-step prediction

Agent B predicts directly in \(q\)-space.

For action \(0\),

\[
R_0(q)=q.
\]

For action \(1\),

\[
R_1(q)
=
\frac34-\frac12 q.
\]

Thus

\[
P(O_{t+1}=1\mid q_t,a_t)
=
R_{a_t}(q_t).
\]

No hidden state needs to appear in the runtime representation.

### 4.2 Recursive update after new evidence

Let

\[
r=R_a(q_t)
\]

be the predicted probability of observing \(1\) after the chosen action.

Then Agent B updates directly:

for \(o_{t+1}=1\),

\[
q_{t+1}
=
1-\frac{3}{16r},
\]

and for \(o_{t+1}=0\),

\[
q_{t+1}
=
\frac{3}{16(1-r)}.
\]

These equations are exactly Bayes-equivalent to Agent C after the affine change of coordinates \(q=1/4+b/2\).

Therefore Agent B can recursively update, branch on hypothetical observations, and roll forward under action sequences while never requiring an explicit runtime variable interpreted as the hidden physical state \(S_t\).

This is the controlled **predictive-model-without-explicit-ontology** edge case.

---

## 5. Declared future query and decision

To test decision support without adding an unrelated reward model, declare the one-step target query

\[
Q_{t+1}=\mathbf 1\{S_{t+1}=1\}.
\]

Agent C evaluates

\[
E[Q_{t+1}\mid b_t,a]
=
P(S_{t+1}=1\mid b_t,a).
\]

Agent B evaluates the same query directly from \(q_t\):

for action \(0\),

\[
E[Q_{t+1}\mid q_t,a=0]
=
2q_t-\frac12,
\]

and for action \(1\),

\[
E[Q_{t+1}\mid q_t,a=1]
=
1-q_t.
\]

The exact greedy decision is therefore

\[
a^\star=
\begin{cases}
0,&q_t\ge\frac12,\\
1,&q_t<\frac12.
\end{cases}
\]

Agent A can know the exact current belief but cannot derive this prospective action value unless additional transition knowledge is supplied.

---

## 6. Control D — Exact one-step lookup on finite support

A fourth system is included only as an anti-overclaim control.

Control D memorizes the exact one-step observation prediction

\[
(h_t,a_t)\mapsto P(O_{t+1}=1\mid h_t,a_t)
\]

for a finite declared training support.

It contains no rule outside that support.

In the executable witness:

- all histories at depths \(t\le1\) are memorized exactly;
- all one-step queries on that support are exact;
- histories at depth \(t=2\) are held out.

This control tests a narrow point:

> exact one-step fit on a finite observed support does not by itself certify compositional or off-support model coverage.

It is **not** used to claim that table-based or full-history predictors can never be models. A sufficiently complete autoregressive history model could be composable; Toy C v0.1 does not rule that out.

---

## 7. Exact verification contract

`verify_toy_c_v0_1.py` uses Python `Fraction` arithmetic only.

It enumerates all reachable histories through horizon 4:

| time depth | reachable histories |
|---:|---:|
| 0 | 2 |
| 1 | 8 |
| 2 | 32 |
| 3 | 128 |
| 4 | 512 |

The verifier checks:

1. **representation equivalence**
   \[
   q_t=\frac14+\frac12 b_t
   \]
   on every reachable history;

2. **one-step predictive equivalence**
   \[
   P_B(O_{t+1}=1\mid q_t,a)
   =
   P_C(O_{t+1}=1\mid b_t,a);
   \]

3. **recursive update equivalence**
   after both possible observations;

4. **branch-conditioned composition**
   for all action/observation branches of length 3 from every state at depths 0 and 1;

5. **open-loop action-sequence prediction**
   for every action sequence of lengths 1 through 4 from every state at depths 0 and 1;

6. **decision-query equivalence**
   for the declared one-step target reward;

7. **lookup-control support**
   exactness on memorized depth \(\le1\) histories and coverage at held-out depth 2.

---

## 8. v0.1 result

The exact verifier reports:

- all Agent B / Agent C checks pass exactly;
- 682 representation checks;
- 340 one-step prediction checks;
- 680 posterior-update checks;
- 340 decision-query checks;
- 640 branch-conditioned length-3 composition checks;
- 300 open-loop action-sequence checks.

Control D is exact on all 20 memorized one-step entries and defines none of the 64 held-out depth-2 one-step queries.

The machine-readable result is stored in `results_v0_1.json`.

---

## 9. What Toy C v0.1 establishes

Within this exact finite construction:

1. **Current-state sufficiency and future-generating model structure are separable architectural capabilities.**  
   Agent A has the exact current belief but no internally owned dynamics.

2. **An explicit hidden-state ontology is not required for exact predictive use in this process.**  
   Agent B and Agent C are exactly equivalent for the declared prediction, recursive-update, rollout, and one-step decision queries.

3. **Finite one-step fit is weaker than demonstrated compositional/off-support coverage.**  
   Control D is exact where memorized but undefined outside that support.

These are scoped witness statements, not general theorems.

---

## 10. What Toy C v0.1 does not establish

Toy C v0.1 does **not** establish:

- a necessary-and-sufficient definition of *world model*;
- that recursive latent-state update is universally necessary for modelhood;
- that an explicit latent ontology is never useful;
- that Agent B is a nontrivial lower-dimensional compression of Agent C;
- independent interventional validity beyond ordinary action conditioning;
- robustness under regime shift;
- any MMALS architectural superiority;
- that the term *world model* should be retained rather than eliminated in favor of a technical capability tuple.

The action is the sole intervention point in this toy, so \(L1_{\rm int}\) is not independently separated. L3 is not exercised.

---

## 11. Current research consequence

Toy C v0.1 sharpens the post-v0.6 question.

The evidence does **not** support

\[
\text{world model}=\text{explicit reconstruction of a hidden physical world}.
\]

It also does not support

\[
\text{world model}=\text{current sufficient state}.
\]

What survives as a candidate technical boundary is narrower:

> an internally owned predictive structure that can be used away from the current real trajectory to generate declared future consequences under candidate actions.

This remains a hypothesis about **model-like structure**, not a definition of *world model*.

The next research task should try to falsify that boundary rather than decorate it.

---

## 12. Link back to MMALS

The August MMALS program note asked for the smallest explainable inference system that remains dynamically sufficient while adapting with the least justified structural growth.

Toy C v0.1 contributes only the primitive question:

> what future-generating structure must survive compression?

Only after this is clear should the richer MMALS tools be introduced:

- delay embeddings / observability;
- intrinsic dynamical dimension;
- local models and transition maps;
- local-to-global compatibility constraints;
- regime-aware adaptation;
- retained history versus active reacquisition.

Those are intentionally deferred from Toy C v0.1.
