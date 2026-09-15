# Toy C v0.2 — Nontrivial predictive quotient and a falsifier for persistent recursive-state necessity

**Status:** exact finite research construction; post-v0.6 exploratory evidence.  
**Relationship to accepted spine:** does **not** modify or reopen the frozen v0.4 framework.  
**Parent:** Toy C v0.1.  
**Purpose:** attack two weaknesses deliberately left open by v0.1:

1. in v0.1 the predictive state `q` was an affine bijection of the full belief, so the “model without ontology” claim did not yet involve a nontrivial quotient;
2. v0.1 did not test whether a **persistently stored recursively updated state** is actually necessary for future-generating model behaviour.

This construction is a falsification exercise, not a definition of *world model*.

---

## 1. Environment

Let the hidden state contain a task-relevant component and an independently evolving nuisance component:

\[
S_t=(X_t,N_t),\qquad X_t,N_t\in\{0,1\}.
\]

The agent chooses

\[
a_t\in\{\mathrm{STAY},\mathrm{FLIP}\}.
\]

The action affects only `X`:

\[
X_{t+1}=\begin{cases}
X_t,& a_t=\mathrm{STAY},\\
1-X_t,& a_t=\mathrm{FLIP}.
\end{cases}
\]

The nuisance state evolves independently:

\[
P(N_{t+1}=N_t)=\frac23,\qquad
P(N_{t+1}\neq N_t)=\frac13.
\]

At each time the observation is a pair

\[
O_t=(Y_t,Z_t),
\]

with conditionally independent noisy sensors

\[
P(Y_t=X_t)=\frac34,
\qquad
P(Z_t=N_t)=\frac45.
\]

The initial state is factorised and uniform:

\[
P(X_0=1)=P(N_0=1)=\frac12.
\]

The full Bayesian posterior therefore factorises as

\[
b_t=(b^X_t,b^N_t)
=
\big(P(X_t=1\mid h_t),P(N_t=1\mid h_t)\big).
\]

---

## 2. Declared query families

Toy C v0.2 makes query breadth explicit.

The **task query family** concerns only the action-relevant `X/Y` subsystem:

\[
\mathcal Q_{\rm task}
=
\{P(Y_{t+k}=1\mid h_t,a_{t:t+k-1}),\;E[R_{t+1}\mid h_t,a_t]\},
\]

where

\[
R_{t+1}=\mathbf 1\{X_{t+1}=1\}.
\]

The **broader query family** additionally contains nuisance prediction:

\[
\mathcal Q_{\rm full}
=
\mathcal Q_{\rm task}
\cup
\{P(Z_{t+1}=1\mid h_t)\}.
\]

This is intentional: the experiment tests whether an internal predictive representation can be exact for a declared task while remaining an information-losing quotient of the full hidden state.

---

## 3. Agent A — exact current full belief, no future-generating model

Agent A receives the exact pair

\[
(b^X_t,b^N_t)
\]

from an oracle at each real time step.

It owns no transition operator, observation operator, recursive update rule, or rollout interface.

Therefore Agent A has an exact current epistemic state but, by construction, cannot internally answer a hypothetical future-action query.

This remains an **architectural separation example** only. It does not prove that every accepted use of the term *world model* must include a future-generating operator.

---

## 4. Agent B — one-dimensional recursive predictive quotient

Define the predictive state

\[
q_t
=
P(Y_{t+1}=1\mid h_t,a_t=\mathrm{STAY}).
\]

Because the `Y` sensor has accuracy `3/4`,

\[
q_t=\frac14+\frac12 b^X_t.
\]

Agent B stores only `q_t`. It has no representation of `b^N_t` and does not use `Z_t` when updating its task state.

For the two actions,

\[
P(Y_{t+1}=1\mid q_t,\mathrm{STAY})=q_t,
\]

\[
P(Y_{t+1}=1\mid q_t,\mathrm{FLIP})=1-q_t.
\]

Let

\[
r_t=P(Y_{t+1}=1\mid q_t,a_t).
\]

After observing `Y_{t+1}`, the next predictive state can be updated directly in `q`-space:

\[
q_{t+1}=\begin{cases}
1-\dfrac{3}{16r_t},&Y_{t+1}=1,\\[1.2ex]
\dfrac{3}{16(1-r_t)},&Y_{t+1}=0.
\end{cases}
\]

The nuisance observation `Z_{t+1}` is ignored.

For the declared reward query,

\[
E[R_{t+1}\mid q_t,a_t]
=
2P(Y_{t+1}=1\mid q_t,a_t)-\frac12.
\]

Thus Agent B supports exact recursive task prediction, rollout and the declared one-step decision query using a single scalar.

---

## 5. Agent C — full generative model

Agent C keeps the full posterior

\[
(b^X_t,b^N_t)
\]

and owns the complete transition and observation model for both hidden components and both observation channels.

It can answer every query in `Q_task` and `Q_full`.

The role of Agent C is not to define the “true” form of a world model. It is the full-generative reference against which the task-relative quotient is checked exactly.

---

## 6. Agent D — finite one-step lookup control

Agent D memorises exact one-step `Y` predictions on all histories up to time depth `1`:

\[
(h_t,a_t)\mapsto P(Y_{t+1}=1\mid h_t,a_t).
\]

It has no rule outside that finite support.

The purpose is unchanged from v0.1: distinguish **exact fit on memorised one-step support** from a model that answers novel compositional future queries.

---

## 7. Agent E — direct-history sequence model with no persistent recursive state

Agent E owns the exact `X/Y` dynamics but stores no persistent recursively updated latent state between queries.

For each query it starts again from the raw complete history

\[
h_t=(o_{\le t},a_{<t}),
\]

recomputes the task-relevant posterior implied by that history, and then evaluates an arbitrary candidate future action sequence.

Operationally it exposes a map of the form

\[
F_E(h_t,a_{t:t+k-1})
=
P(Y_{t+k}=1\mid h_t,a_{t:t+k-1}).
\]

The implementation may perform recursive arithmetic *inside the query computation*, but there is no persistent state satisfying

\[
z_{t+1}=U(z_t,a_t,o_{t+1})
\]

that must be carried from one real time step to the next.

This distinction targets a strong reading of hypothesis H2 from the post-v0.6 research note:

> persistent recursive state closure may be a convenient implementation property rather than a necessary condition for exact future-generating model behaviour.

Toy C v0.2 does **not** claim that recursion is unnecessary computationally in general, only that persistent recursive state storage is not logically required in this finite construction.

---

## 8. Exact tests

The verifier enumerates every reachable history through time depth `3` using rational arithmetic only.

### 8.1 `Q_task` equivalence

For every enumerated history it checks:

1. `q_t = 1/4 + (1/2)b^X_t`;
2. Agent E recomputes the exact `b^X_t` from the full history;
3. B, C and E agree on one-step `Y` prediction;
4. B and C agree after every possible action and next observation `(Y,Z)`;
5. B and C give the same expected reward and greedy decision;
6. B and C remain identical for all branch-conditioned action/observation sequences of length `2` from states at depth `<=1`;
7. B, C and E agree for every open-loop action sequence of length `1..4` from states at depth `<=1`.

### 8.2 Nontrivial quotient test

Histories are grouped by `(time,q_t)`.

Within each `q`-cell the verifier searches for histories with different nuisance posterior `b^N_t`.

It reports two exact aliasing quantities:

\[
\Delta_Y(q)=
\max_{h,h':q(h)=q(h')}
\left|
P(Y_{t+1}=1\mid h,\mathrm{STAY})
-
P(Y_{t+1}=1\mid h',\mathrm{STAY})
\right|,
\]

and

\[
\Delta_Z(q)=
\max_{h,h':q(h)=q(h')}
\left|
P(Z_{t+1}=1\mid h)
-
P(Z_{t+1}=1\mid h')
\right|.
\]

For a successful task-relative quotient we expect

\[
\Delta_Y=0
\]

while

\[
\Delta_Z>0.
\]

This gives an exact abstraction-frontier witness: the same quotient is closed for `Q_task` and insufficient for the richer `Q_full`.

### 8.3 Lookup support control

Agent D is checked for exactness on all memorised histories at depth `<=1` and then queried on histories at depth `2`. Coverage, rather than an invented numerical prediction, is reported when the lookup has no entry.

---

## 9. Exact results

The machine-readable result is generated by `verify_toy_c_v0_2.py`.

The exhaustive enumeration contains:

- depth 0: `4` histories;
- depth 1: `32` histories;
- depth 2: `256` histories;
- depth 3: `2048` histories.

All exact `Q_task` equivalence checks pass:

- `2340` representation / history-recomputation checks;
- `584` one-step prediction checks;
- `2336` recursive B-vs-C update checks;
- `584` decision checks;
- `2304` branch-conditioned length-2 checks;
- `1080` open-loop B/C/E action-sequence checks.

The nontrivial quotient is explicit:

\[
\max \Delta_Y=0,
\]

but

\[
\max \Delta_Z=\frac{19}{129}>0.
\]

One maximal witness occurs at depth `3` with the same

\[
q=\frac{21}{82}
\]

but nuisance posteriors

\[
b^N=\frac{17}{129}
\qquad\text{and}\qquad
b^N=\frac{112}{129},
\]

which induce

\[
P(Z_{t+1}=1)=\frac{55}{129}
\qquad\text{and}\qquad
P(Z_{t+1}=1)=\frac{74}{129}.
\]

Thus `q` is an exact predictive state for the declared task queries while being provably unable to reconstruct or predict the nuisance channel globally.

Agent D remains exact on its `72` memorised training entries and has

\[
0/512
\]

coverage on held-out depth-2 queries.

---

## 10. What v0.2 changes relative to v0.1

### 10.1 The “no ontology required” result is now nontrivial

In v0.1,

\[
q=\frac14+\frac12b
\]

was an affine bijection of the entire binary belief. A critic could therefore say that the predictive state merely renamed the full belief.

In v0.2, the full posterior has two task-independent coordinates

\[
(b^X,b^N),
\]

while `q` depends only on `b^X`.

Different full beliefs collapse to the same predictive state, and that lost information is measurable through the positive `Z` aliasing gap.

The result is therefore genuinely **query-relative compression**, not a coordinate change.

### 10.2 Strong H2 is weakened

Agent E answers all declared open-loop future-action queries exactly while carrying no persistent recursively updated state.

Therefore the strong candidate claim

> “a model must carry a recursively updateable persistent internal state”

is not supported by Toy C v0.2.

A weaker candidate survives:

> a model-like system internally owns a mechanism that can answer declared future, action-indexed queries away from the current realised trajectory.

That mechanism can be implemented recursively, generatively, through a predictive state, or by direct recomputation from history.

This is a materially different hypothesis and should be tested rather than promoted to a definition.

---

## 11. Hypothesis disposition after v0.2

### H1 — sufficiency alone is insufficient

**Status:** still supported only as an architectural separation example.

Agent A has the exact current full belief but no future-generating interface.

### H2 — recursive closure may be necessary

**Status:** **weakened / counterexample candidate.**

Agent E has no persistent recursive state yet answers the declared future-action sequence queries exactly.

### H3 — modelhood is tied to action-indexed future consequences

**Status:** survives Toy C v0.2 as the common capability shared by B, C and E and absent from A and off-support D.

This remains a candidate discriminator, not a definition.

### H4 — breadth is a profile property

**Status:** strengthened in this finite example.

The same `q` representation is exact for `Q_task` but has irreducible aliasing for the richer nuisance query in `Q_full`.

This directly supports reporting an abstraction/query frontier rather than silently turning one task-relative success into a global “world” claim.

---

## 12. Scope discipline

Toy C v0.2 establishes only the following finite facts:

1. a one-dimensional predictive quotient can exactly preserve the declared task dynamics and decisions while discarding another genuinely varying component of the full posterior;
2. hidden-state reconstruction is not required for exact task-relative prediction and rollout in this construction;
3. persistent recursive state storage is not required for exact declared sequence prediction in this construction;
4. one-step memorisation remains distinct from off-support compositional coverage;
5. predictive sufficiency is explicitly relative to a query family.

It does **not** establish:

- a necessary-and-sufficient definition of world model;
- that recursive computation is unnecessary in general;
- interventional validity beyond the declared action semantics;
- robustness under regime shift;
- that `Q_task` is sufficiently broad to justify the word “world”.

---

## 13. Next falsification target

The next useful test should no longer add hidden-state complexity for its own sake.

Toy C v0.3, if pursued, should attack the remaining candidate:

> **internally owned action-indexed future-query capability**.

Possible falsifiers include a system with no internally represented dynamics that nevertheless supports the same hypothetical action-sequence queries through an external oracle, cached planner, or policy/value object. The key issue would be to distinguish *model possession* from *access to model-derived answers* without relying on anthropomorphic notions such as “understanding”.

Until that distinction survives a controlled falsification attempt, no new framework layer should be added.
