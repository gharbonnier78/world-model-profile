# Toy C v0.3 — Model possession vs model access

**Status:** exact finite research construction; post-v0.6 exploratory evidence.  
**Relationship to accepted spine:** does **not** modify or reopen the frozen v0.4 framework.  
**Parent:** Toy C v0.2.  
**Purpose:** attack the strongest candidate left after v0.2:

> a model-like system internally owns a mechanism able to answer declared future, action-indexed queries away from the currently realised trajectory.

Toy C v0.3 asks whether **internal ownership** is actually identifiable or necessary at the system level once model-derived answers may be delegated, compiled, or cached.

This construction is a falsification exercise, not a definition of *world model*.

---

## 1. Environment

Toy C v0.3 reuses the exact finite environment from v0.2.

The hidden state is

\[
S_t=(X_t,N_t),\qquad X_t,N_t\in\{0,1\}.
\]

The action

\[
a_t\in\{\mathrm{STAY},\mathrm{FLIP}\}
\]

acts only on the task-relevant component:

\[
X_{t+1}=
\begin{cases}
X_t,& a_t=\mathrm{STAY},\\
1-X_t,& a_t=\mathrm{FLIP}.
\end{cases}
\]

The nuisance state evolves independently:

\[
P(N_{t+1}=N_t)=\frac23,
\qquad
P(N_{t+1}\neq N_t)=\frac13.
\]

The observation is

\[
O_t=(Y_t,Z_t),
\]

with

\[
P(Y_t=X_t)=\frac34,
\qquad
P(Z_t=N_t)=\frac45.
\]

The initial hidden variables are independent and uniform.

The reuse of the v0.2 environment is deliberate. v0.3 changes the **location and form of predictive capability**, not the underlying stochastic process.

---

## 2. Declared future-query domain

The principal benchmark domain is finite:

\[
\mathcal D_0
=
\left\{
(h_t,a_{t:t+k-1}) :
t\le2,\; k\in\{1,2,3\}
\right\}.
\]

For each query, the required answer is

\[
Q(h_t,a_{t:t+k-1})
=
P(Y_{t+k}=1\mid h_t,a_{t:t+k-1}).
\]

The verifier enumerates every reachable history through depth 3 exactly. The declared benchmark contains

\[
|\mathcal D_0|=4088
\]

future queries.

A separate extension domain is

\[
\mathcal D_+
=
\left\{
(h_t,a_{t:t+3}) :
t\le2
\right\},
\]

i.e. the same history support but action-sequence length 4. It contains

\[
|\mathcal D_+|=4672
\]

queries.

`D+` is not part of the compiled cache described below.

---

## 3. Agent M — local model possession

Agent M is the local model-owning reference.

It contains the task-relevant `X/Y` dynamics inside the declared local system boundary. For every query it reconstructs the current `X` belief from the complete history and propagates it through the requested future action sequence.

It therefore computes

\[
Q_M(h_t,a_{t:t+k-1})
=
P(Y_{t+k}=1\mid h_t,a_{t:t+k-1})
\]

without consulting any external model service.

Agent M is implementation-equivalent in future-query capability to Agent E from v0.2: persistent recursively stored state is not required.

---

## 4. Agent F — delegated model access

Agent F deliberately contains **no local task transition model, observation model, recursive state-update model, or rollout operator**.

Instead, while an external exact model service `O` is available, F forwards the pair

\[
(h_t,a_{t:t+k-1})
\]

to that service and returns the answer:

\[
Q_F(h_t,a_{t:t+k-1})
=
O(h_t,a_{t:t+k-1}).
\]

The external service itself implements the same exact task dynamics as Agent M.

At the **local agent boundary**, F has access to model-derived answers but does not possess the model mechanism.

At the **expanded system boundary** that includes `F + O`, the composite system does contain a future-generating model service.

This boundary distinction is part of the experiment rather than a terminological afterthought.

---

## 5. Agent G — compiled finite answer object

Agent G is generated offline by evaluating the exact future-query map on every element of `D0` and storing the answers:

\[
G
=
\left\{
((h,a_{0:k-1}),Q(h,a_{0:k-1}))
:
(h,a_{0:k-1})\in\mathcal D_0
\right\}.
\]

It therefore contains exactly `4088` query-answer entries.

G has:

- no declared transition operator;
- no observation model;
- no recursive update rule;
- no rollout composition rule;
- no extrapolation rule outside its compiled keys.

On `D0`, however, it is by construction capable of returning exactly the same answer as a generative or predictive model.

Whether one wishes to call such a finite compiled object a "model" is left open. The scientific point is narrower: **finite input-output behaviour alone cannot recover the internal computational structure that produced it.**

---

## 6. Exact tests

### 6.1 Finite observational equivalence

For every query in `D0`, the verifier compares:

1. Agent M — local model possession;
2. Agent F — external model access;
3. Agent G — compiled finite answers;
4. the exact environment-derived truth.

All calculations use rational arithmetic.

The question is whether

\[
Q_M=Q_F=Q_G=Q_{\rm true}
\]

for all `4088` declared queries.

### 6.2 Query-domain extension

The agents are then queried on `D+`, which contains horizon-4 action sequences never compiled into G.

The test reports exactness for M and F and **coverage** for G. G is not assigned an invented extrapolation.

### 6.3 External-source removal

The external oracle `O` is removed while the declared local-agent boundary is kept fixed.

The test asks which capabilities remain:

- M should remain able to answer because the predictive mechanism is local;
- F should become undefined because it had delegated the mechanism;
- G should retain exact cached answers on `D0` but remain unable to answer `D+`.

This is an operational distinction between **possession**, **delegated access**, and **finite compilation**.

---

## 7. Exact results

The verifier reports the same reachable-history counts as v0.2:

- depth 0: `4`;
- depth 1: `32`;
- depth 2: `256`;
- depth 3: `2048`.

### 7.1 On the declared finite domain `D0`

All three systems are exactly observationally equivalent by answer correctness:

\[
M:\frac{4088}{4088},
\qquad
F+O:\frac{4088}{4088},
\qquad
G:\frac{4088}{4088}.
\]

Therefore no test that observes only these answers can identify whether the capability came from:

- locally owned dynamics;
- an external model service;
- a compiled finite answer table.

This is a finite identifiability limitation, not a claim that the internal objects are semantically identical.

### 7.2 On the extension domain `D+`

For horizon-4 queries:

\[
M:\frac{4672}{4672},
\qquad
F+O:\frac{4672}{4672},
\]

while the compiled object has

\[
\mathrm{coverage}(G,\mathcal D_+)=\frac{0}{4672}.
\]

Thus finite compilation can imitate model behaviour on a declared finite domain without providing the same extension capability.

### 7.3 After external-source removal

Removing `O` leaves:

\[
M:\frac{4088}{4088}
\]

on `D0`, while F has

\[
\mathrm{coverage}(F,\mathcal D_0\mid O\text{ removed})
=
\frac{0}{4088}.
\]

G still answers its compiled domain exactly:

\[
G:\frac{4088}{4088},
\]

but it still has zero coverage on `D+`.

The distinction is therefore not visible in the original finite benchmark alone; it appears when the evaluation contract includes **source dependence** and **domain extension**.

---

## 8. Elementary finite-compilation observation

Let `D` be any finite declared query set and let an exact deterministic query mechanism be

\[
M:D\rightarrow\mathcal Y.
\]

Then the finite table

\[
T_M=\{(d,M(d)):d\in D\}
\]

is observationally equivalent to `M` on `D`.

Toy C v0.3 instantiates this elementary fact exactly.

No novelty is claimed for the observation itself. Its role is methodological:

> exact finite behavioural agreement cannot, by itself, establish that an evaluated component internally possesses generative or predictive structure.

An experiment that wishes to distinguish such structures must declare additional tests: extension, interventions on the source, resource constraints, latency, compositionality, or architectural inspection.

---

## 9. System-boundary dependence

Toy C v0.3 exposes a boundary problem.

At the local-agent boundary:

| system | capability source |
|---|---|
| M | local predictive dynamics |
| F | external model access |
| G | finite compiled answers |

At a larger boundary containing `F + O`, the composite system *does* contain the predictive model service.

Therefore a statement such as

> "the system possesses a world model"

is incomplete unless the system boundary is explicit.

This does **not** mean that every external service should be considered part of a world model. It means that attribution cannot be made independently of the boundary at which the claim is evaluated.

---

## 10. Hypothesis disposition after v0.3

### H1 — sufficiency alone is insufficient

**Status:** unchanged.

Agent A from v0.1/v0.2 remains an architectural separation example: exact current state can be supplied without a future-query mechanism.

### H2 — persistent recursive state is necessary

**Status:** remains weakened.

Agent E from v0.2 already answers exact future queries without persistent recursive-state storage.

### H3 — internally owned action-indexed future mechanism is necessary

**Status:** **weakened as a system-level necessity.**

Agent F reproduces every declared answer exactly while the local agent owns no predictive mechanism. What it has is **delegated access**.

If the claim is made about the expanded `F+O` boundary, the composite system again contains a model mechanism. Therefore the distinction is partly one of attribution and boundary declaration.

### H4 — breadth is a profile/frontier property

**Status:** retained.

v0.2 showed query-family breadth. v0.3 adds a second declaration dimension:

\[
\text{query breadth}
\quad+\quad
\text{system boundary / capability source}.
\]

This is currently better treated as explicit evaluation metadata than as a new framework layer.

---

## 11. What survives the falsification cycle

After v0.1-v0.3, increasingly implementation-specific candidate definitions have weakened:

1. **current sufficient state** is not enough to distinguish model possession;
2. **explicit hidden-state ontology** is not necessary for exact task-relative future prediction;
3. **persistent recursive state** is not necessary;
4. **local internal ownership** is not necessary for exact system-level future-query behaviour if delegated model access is allowed;
5. **finite exact behaviour** cannot by itself identify generative structure because it can be compiled.

The surviving technical question is therefore less ontological:

> What future-query capability is available, over which query family, from which source, inside which declared system boundary, and how does that capability behave under extension, source removal, intervention, and shift?

This increasingly favours the profile/contract view over a binary world-model predicate.

---

## 12. Scope discipline

Toy C v0.3 establishes only the following finite facts:

1. M, F and G are exactly answer-equivalent on the declared finite domain `D0`;
2. answer-equivalence on a finite domain does not identify internal model possession in this construction;
3. external model access can exactly substitute for local model possession while the external source remains available;
4. query extension separates finite compilation from mechanisms with wider generative access;
5. source removal separates delegated access from local possession;
6. attribution depends on the declared system boundary.

It does **not** establish:

- that lookup tables should or should not count as world models;
- that local and remote models are operationally equivalent under latency, privacy, cost, reliability, security, or robustness constraints;
- a universal definition of modelhood;
- independent causal/interventional validity;
- robustness under regime or distribution shift.

---

## 13. Next research target

Do not add another layer to the accepted profile from this result.

A useful next step is to test whether the remaining contract can be sharpened around **capability provenance and extension** rather than model terminology:

\[
(\text{query family},
\text{boundary},
\text{source},
\text{coverage},
\text{extension},
\text{availability},
\text{shift})
\]

and ask whether this changes practical evaluation decisions.

For the MMALS bridge, the important implication is that reusable predictive capability need not be stored in one monolithic internal object. It may be local, delegated, compiled, retrieved, or reconstructed — but its **domain of validity, provenance, dependencies and extension behaviour must remain auditable**.

This is compatible with the earlier Minimal Sufficient Dynamic Inference principle and with the Chronicle's insistence that complexity should grow only when evidence requires it.
