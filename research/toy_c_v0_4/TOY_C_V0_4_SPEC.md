# Toy C v0.4 — Typed extension: horizon generalisation without full generative closure

**Status:** exact finite research construction; post-v0.6 exploratory evidence.  
**Relationship to accepted spine:** does **not** modify or reopen the frozen v0.4 framework.  
**Parent:** Toy C v0.3.  
**Purpose:** perform the next deliberately mechanical falsification step after v0.3.

Toy C v0.3 showed that exact finite answer behaviour does not identify local model possession: a local model owner, a delegated oracle client, and a compiled finite answer table can be identical on a declared finite domain. Query-domain extension then separated the compiled table from the mechanisms that could answer a longer horizon.

Toy C v0.4 attacks a tempting over-reading of that result:

> perhaps **extension capability** itself is the remaining discriminator of model-like structure.

The experiment shows that this is still too coarse. A task-specific answer program can extrapolate exactly to arbitrarily long future action sequences on a fixed conditioning-history support while lacking any declared observation-update rule, nuisance model, or capability to extend to newly conditioned histories.

The result is not a definition of *world model*. It is a refinement of what must be declared when saying that a predictive capability “extends”.

---

## 1. Environment

v0.4 reuses the exact finite POMDP from v0.2 and v0.3.

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
X_t,&a_t=\mathrm{STAY},\\
1-X_t,&a_t=\mathrm{FLIP}.
\end{cases}
\]

The nuisance process is independent:

\[
P(N_{t+1}=N_t)=\frac23,
\qquad
P(N_{t+1}\neq N_t)=\frac13.
\]

Observation is

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

Reusing the same environment is intentional. The only new object is the **form of the query mechanism**.

---

## 2. Reference query

As in v0.3, the principal query is an open-loop endpoint prediction

\[
Q(h_t,a_{t:t+k-1})
=
P(Y_{t+k}=1\mid h_t,a_{t:t+k-1}).
\]

The baseline domain is unchanged:

\[
\mathcal D_0
=
\{(h_t,a_{t:t+k-1}):t\le2,\;k\in\{1,2,3\}\}.
\]

It contains exactly

\[
|\mathcal D_0|=4088
\]

queries.

Agents M, F and G are retained from v0.3:

- **M:** local model-owning reference;
- **F:** delegated access to exact external model service O;
- **G:** finite table containing the exact answers on `D0` only.

---

## 3. Agent H — factorised task-query program

v0.4 adds **Agent H**.

For each conditioning history through depth 2, H stores one scalar seed

\[
q(h)
=
P(Y_{t+1}=1\mid h,\mathrm{STAY}).
\]

There are only

\[
4+32+256=292
\]

such conditioning histories.

H does **not** declare:

- a hidden-state model;
- an observation model;
- a nuisance-state model;
- a Bayesian update rule for a newly observed future \(Y\);
- a recursive latent transition state;
- an external model service.

Instead, H contains one task-specific algebraic rule. Because `STAY` leaves \(X\) unchanged and `FLIP` complements \(X\), any finite action sequence affects \(X\) only through the parity of the number of `FLIP` actions.

Therefore

\[
Q_H(h,a_{t:t+k-1})
=
\begin{cases}
q(h), & \text{even number of FLIPs},\\
1-q(h), & \text{odd number of FLIPs}.
\end{cases}
\]

This is a **query program**, not a full generative simulator.

The experiment deliberately does not decide whether H “counts as a model”. The only scientific claim is about its measurable capabilities.

---

## 4. Why this attacks v0.3 rather than merely extending it

v0.3 separated the finite table G from M/F by asking a longer-horizon question that was not present in G.

A weak reading would be:

\[
\text{can answer longer horizons}
\quad\Longrightarrow\quad
\text{has model-like generative structure}.
\]

H is designed as a counterexample candidate to that reading.

H contains no per-query answers for horizons 4, 5 or 6. Yet once a seed \(q(h)\) is available, the parity rule gives the exact endpoint answer at every tested longer horizon — and analytically at any finite horizon for this environment.

So “extension” must itself be typed.

---

## 5. Exact tests

### 5.1 Baseline `D0`

For every query in `D0`, compare:

\[
M,\quad F+O,\quad G,\quad H
\]

against the exact environment-derived answer.

### 5.2 Future-horizon extension

Keep the same conditioning-history support \(t\le2\), but ask new action-sequence lengths

\[
k\in\{4,5,6\}.
\]

This creates

\[
32704
\]

new queries.

G has no entries for them.

H receives no new seed entries and uses only the same 292 history seeds plus the parity rule.

### 5.3 Conditioning-history extension

Instead of extending the future horizon, extend the history support to newly conditioned histories at depth 3 while returning to action-sequence lengths 1–3:

\[
t=3,\qquad k\in\{1,2,3\}.
\]

This creates

\[
28672
\]

queries.

M and F can reconstruct the current task belief from the new history.

G has no corresponding entries.

H has no seed for these histories and no observation-update rule from which to generate one.

### 5.4 Branch-conditioned future query

A distinct query asks the model to absorb a *hypothetical future observation* before continuing:

\[
P(
Y_{t+2}=1
\mid
h_t,
a_t=a_0,
Y_{t+1}=y_1,
a_{t+1}=a_1
).
\]

This is not the same operation as open-loop endpoint prediction.

M/F expose the required conditional update.

H deliberately does not.

The verifier reports unsupported interfaces as unsupported rather than inventing outputs.

### 5.5 Parity identity non-regression

For all 292 supported conditioning histories, every binary action sequence of lengths 1 through 8 is exhaustively checked with exact rational arithmetic.

This gives

\[
148920
\]

exact comparisons.

The finite checks guard the implementation. The underlying identity is elementary:

\[
X\mapsto X
\quad\text{or}\quad
X\mapsto1-X
\]

composes according to FLIP parity.

No novelty is claimed for this algebraic fact.

---

## 6. Exact results

### 6.1 Baseline equivalence

On `D0`:

\[
M=F+O=G=H=\frac{4088}{4088}.
\]

The full query table G contains 4088 query-answer entries.

H stores only 292 history seeds plus its rule.

The entry-count ratio is

\[
\frac{4088}{292}=14.
\]

This is only bookkeeping. The rule/code description length is not included, so this is **not** a formal compression, Kolmogorov-complexity, or MDL claim.

### 6.2 Future-horizon extension

For lengths 4, 5 and 6:

\[
M=\frac{32704}{32704},
\qquad
F+O=\frac{32704}{32704},
\]

\[
G:\frac{0}{32704}\text{ defined},
\]

but

\[
H=\frac{32704}{32704}.
\]

So H extends perfectly along the **future-horizon axis** without any new per-query cache entries.

### 6.3 Conditioning-history extension

For newly conditioned depth-3 histories:

\[
M=\frac{28672}{28672},
\qquad
F+O=\frac{28672}{28672},
\]

whereas

\[
G:\frac{0}{28672}\text{ defined},
\qquad
H:\frac{0}{28672}\text{ defined}.
\]

H therefore has strong future-horizon extension and zero conditioning-history extension under the declared interface.

### 6.4 Branch-conditioned future evidence

The branch-conditioned domain contains

\[
2336
\]

queries.

M/F are exact on all of them:

\[
M=F+O=\frac{2336}{2336}.
\]

G and H do not expose the required interface.

This separates:

\[
\text{open-loop endpoint extrapolation}
\]

from

\[
\text{hypothetical evidence assimilation + continued prediction}.
\]

### 6.5 Source removal

After removing the external service O:

- F becomes undefined on `D0`;
- H remains exact on `D0`;
- H remains exact on all 32704 longer-horizon queries.

Thus H combines:

1. local availability;
2. source independence;
3. exact future-horizon extension;

while still lacking conditioning-history and branch-conditioned extension.

This directly weakens any scalar notion of “extension capability”.

---

## 7. What v0.4 changes relative to v0.3

v0.3 established that finite answer equivalence does not identify internal mechanism and that a longer-horizon domain can separate a full finite table from wider mechanisms.

v0.4 shows that even this separation must be interpreted carefully.

A system can pass:

\[
E_{\rm horizon}
\]

while failing:

\[
E_{\rm history}
\]

and exposing no

\[
E_{\rm branch}.
\]

So a single flag such as

> “generalises beyond the benchmark”

is underspecified.

A more precise contract distinguishes at least:

\[
E=
(
E_{\rm horizon},
E_{\rm history},
E_{\rm query},
E_{\rm branch},
E_{\rm source},
E_{\rm intervention},
E_{\rm shift}
).
\]

This tuple is exploratory metadata, **not a proposed new accepted layer**.

---

## 8. Hypothesis disposition after v0.4

### H1 — current-state sufficiency alone identifies modelhood

**Status:** unchanged / unsupported as a criterion.

The architectural Agent A example still separates exact current epistemic state from future-query machinery.

### H2 — persistent recursive state is necessary

**Status:** remains weakened by Agent E in v0.2.

### H3 — local internal ownership of a future mechanism is necessary

**Status:** remains weakened by delegated Agent F in v0.3.

### H5 — extension capability is a scalar discriminator

**Status:** **weakened by v0.4.**

H has exact future-horizon extension and local source independence while failing extension along other declared axes.

The surviving methodological requirement is:

> when claiming extension or generalisation, declare **which axis of the query contract has been extended**.

---

## 9. Relation to the World Model Profile

No accepted coordinate changes.

v0.4 is best read as a refinement of declaration discipline around L0/L2-style claims rather than as evidence for a new `L4` or a new constitutive criterion.

The construction reinforces three ideas already present in the programme:

1. sufficiency is query-relative;
2. a capability claim is boundary- and support-relative;
3. “generalisation” without a declared direction can hide qualitatively different mechanisms.

The accepted v0.4 framework spine remains frozen.

---

## 10. Relation to MMALS

For MMALS, v0.4 is relevant because a minimal inference mechanism need not scale uniformly in every direction.

A compact rule may generalise indefinitely over one axis while being unable to assimilate one new observation or one newly relevant variable.

That suggests a more precise version of the earlier *Minimal Sufficient Dynamic Inference* intuition:

> preserve the smallest structure that is sufficient for the currently declared query contract, but track **which extensions it can support without reconstruction, reacquisition, or model replacement**.

This is compatible with the later adaptive question

\[
\mathbb A_t\rightarrow\mathbb A_{t+1},
\]

because refinement pressure can be triggered by failure on a specific extension axis rather than by an undifferentiated notion of model error.

---

## 11. Scope discipline

Toy C v0.4 establishes only the following finite/scoped facts:

1. H matches the local model reference exactly on all 4088 baseline queries;
2. H answers all 32704 new horizon-4/5/6 endpoint queries exactly without adding per-query entries;
3. H has no coverage for the 28672 newly conditioned depth-3-history queries;
4. M/F are exact on all 2336 branch-conditioned hypothetical-observation queries, while H/G expose no such interface;
5. local source independence plus future-horizon extension does not uniquely identify a full generative/update model in this construction;
6. “extension” is operationally multi-axis.

It does **not** establish:

- that H is or is not a world model;
- a universal taxonomy of extension axes;
- any formal complexity advantage of H;
- that parity factorisation exists outside this deliberately simple dynamics;
- independent causal validity beyond the action semantics already declared;
- robustness to regime shift;
- a necessary-and-sufficient definition of world model.

---

## 12. Next stopping point

v0.4 completes the deliberately mechanical continuation of the Toy C falsification chain:

\[
\text{state}
\rightarrow
\text{recursive dynamics}
\rightarrow
\text{direct history model}
\rightarrow
\text{delegated access}
\rightarrow
\text{finite compilation}
\rightarrow
\text{typed extension}.
\]

The useful residue is no longer a plausible single architectural predicate.

The next scientifically different step would be to introduce an actual **change of regime, action semantics, observation channel, or query family** and test whether the capability contract predicts which mechanism must be adapted, refined, reacquired, or replaced.

That would no longer be merely another mechanical extension of the same finite construction; it would begin to connect Toy C to adaptive abstraction and MMALS.
