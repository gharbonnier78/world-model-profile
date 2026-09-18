# Toy C v0.4 — Review-repaired interpretation: predictive operator without filtering closure

**Status:** exact finite research construction; post-v0.6 exploratory evidence; interpretation repaired after independent review.  
**Relationship to accepted spine:** does **not** modify or reopen the frozen v0.4 framework.  
**Parent:** Toy C v0.3.  
**Purpose:** preserve the exact v0.4 construction while correcting what it actually establishes.

Toy C v0.3 showed that exact finite answer behaviour does not identify local model possession: a local model owner, a delegated oracle client, and a compiled finite answer table can be identical on a declared finite domain. Query-domain extension then separated the compiled table from mechanisms with wider predictive access.

At v0.4 we formulated, **at v0.4 itself**, a candidate over-reading of that result:

> perhaps **extension capability** is a scalar discriminator of model-like structure.

This was **not** a pre-registered H5 from the earlier hypothesis set. Independent review showed that Agent H does not demonstrate prediction without model structure: its FLIP-parity rule is the exact task-specific action-conditioned predictive operator `K` in closed form. What H lacks is the observation-assimilation/update machinery `U`.

The repaired result is therefore a finite decomposition of **prediction versus filtering/update**, plus an audit of source dependence and supported query interfaces. It is not a definition of *world model*, and it does not justify a new extension taxonomy or framework layer.

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

This is not a full generative simulator or filtering architecture, but it **does own an exact task-specific predictive operator**: the parity rule is `K` in closed form for the declared task coordinate.

In the provisional object `M = (sigma, U, K, Q)`, H is best described as carrying supported `sigma`, `K`, and endpoint query semantics `Q`, while lacking an implemented observation-assimilation/update operator `U` for new evidence.

The experiment deliberately does not decide whether H “counts as a world model”. The scientific claim is the component decomposition.

---

## 4. What v0.4 actually tests after review

v0.3 separated the finite table G from M/F by asking a longer-horizon question not present in G.

v0.4 then explored a candidate over-reading: that extension beyond the compiled domain might itself identify richer model-like structure. The independent review rejects the strongest version of that interpretation because H already contains the exact predictive operator `K` for the task subsystem.

H contains no per-query answers for horizons 4, 5 or 6. Once a seed `q(h)` is available, its closed-form `K` composes endpoint predictions at every tested longer horizon — and analytically at any finite horizon in this deliberately simple involutive dynamics.

The informative separation is therefore:

`predictive propagation K != evidence assimilation/update U`.

The horizon, history-support, and branch-conditioned checks remain useful as interface probes, but they are not three independent discoveries and they do not define modelhood.

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

A distinct query asks the system to absorb a *hypothetical future observation* before continuing:

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

M exposes the required conditional update locally. F delegates the same branch-conditioned query through its external model service, so the repaired verifier exercises that delegated path independently and also removes the service to test source dependence.

H and G do not implement this branch-conditioned interface. The verifier reports that fact as **NOT_IMPLEMENTED**, not as a measured failure score.

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

The full query table G contains 4088 query-answer entries. H stores one seed for each of the 292 supported histories plus its predictive rule.

There are `2+4+8=14` baseline action sequences per supported conditioning history, so

\[
4088 = 292\times 14
\]

is an identity induced by the benchmark construction. It is **not an independently measured compression ratio** and carries no Kolmogorov-complexity, MDL, or other complexity claim.

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

The repaired verifier measures the two implemented paths independently:

\[
M=\frac{2336}{2336},
\qquad
F+O=\frac{2336}{2336}.
\]

After removing the external service,

\[
\mathrm{coverage}(F,\text{branch}\mid O\text{ removed})=\frac{0}{2336}.
\]

G and H do not implement the required branch-conditioned interface; this is recorded as an interface status, not as a failure count.

The scoped distinction is between open-loop predictive propagation and evidence assimilation/filtering.

### 6.5 Source removal

After removing the external service O:

- F becomes undefined on `D0` and on the branch-conditioned delegated path;
- H remains exact on `D0`;
- H remains exact on all 32704 longer-horizon queries through its own closed-form predictive operator `K`.

Thus H combines local availability and exact long-horizon predictive propagation while lacking the `U`-like machinery needed to assimilate new evidence and construct new supported states.

The correct interpretation is therefore **prediction without filtering/update closure**, not prediction without model structure.

---

## 7. Relation to the accepted declaration tuple

v0.3 established that finite answer equivalence does not identify internal mechanism and made source/boundary provenance explicit.

v0.4 initially introduced a separate typed-extension tuple `E`. Independent review showed that this is largely redundant with the already accepted declaration tuple `D`:

- future horizon corresponds to declared `H_A`;
- history/support extension corresponds to `Omega_0`;
- query-family and branch type belong inside the declared abstraction/query family `A`;
- intervention corresponds to `I`;
- shift corresponds to `Delta`.

The genuinely additional systems-engineering metadata exposed by v0.3 is **capability source / system boundary**.

Accordingly, v0.4 does not introduce or defend a new taxonomy. It is better read as a reminder that existing declarations can be widened along different directions, with source/boundary provenance recorded separately.

---

## 8. Candidate-criterion disposition after v0.4

H1-H4 are project-authored candidate criteria, not formal theories attributed to the literature. The toys provide finite counterexamples or weakening evidence against those candidates; they are not claimed to falsify a general theory of world models.

### H1 — current-state sufficiency alone identifies modelhood

**Status:** unchanged / unsupported as a criterion.

### H2 — persistent recursive state is necessary

**Status:** remains weakened by Agent E in v0.2.

### H3 — local internal ownership of a future mechanism is necessary

**Status:** remains weakened by delegated Agent F in v0.3.

### v0.4 candidate over-reading — extension as a scalar discriminator

**Status:** repaired after independent review.

This candidate was formulated **at v0.4**, not pre-registered as part of H1-H4. The strongest intended reading is not supported because H already owns the exact predictive operator `K`. The useful residue is narrower:

> distinguish predictive propagation from observation assimilation/update, and state which already-declared support/query/horizon condition changed.

---

## 9. Relation to the World Model Profile

No accepted coordinate changes.

v0.4 is best read as an operational test pattern around existing L0/L2 declarations rather than as evidence for a new `L4` or constitutive criterion.

The repaired construction reinforces three ideas already present in the programme:

1. sufficiency is query-relative;
2. predictive propagation `K` and filtering/update `U` are distinct components;
3. source/boundary provenance must be explicit when capability is delegated.

The accepted v0.4 framework spine remains frozen.

---

## 10. Relation to MMALS

For MMALS, the repaired result is only a **possible bridge**, not evidence of adaptive abstraction itself. Toy C keeps the abstraction family fixed throughout.

A compact predictive operator `K` may remain adequate for open-loop queries while lacking the `U`-like machinery needed to assimilate new evidence. That suggests a future question about when an adaptive system must revise or reacquire its representation, but Toy C v0.4 does not establish such a transition.

The source MMALS lifecycle should be preserved in its careful form:

`REUSE -> ADAPT -> FORK -> CANDIDATE NEW REGIME -> VERIFY -> REMEMBER`

before any `MERGE / PRUNE / RETIRE` decision.

The possible bridge to `A_t -> A_{t+1}` therefore remains a hypothesis for later study, not a result of v0.4.

---

## 11. Scope discipline

Toy C v0.4 establishes only the following finite/scoped facts:

1. H matches the local model reference exactly on all 4088 baseline queries;
2. H contains an exact task-specific predictive operator `K` in closed form and composes it exactly over all 32704 tested longer-horizon endpoint queries;
3. H has no implemented update route for the 28672 newly conditioned depth-3-history queries;
4. M and the independently exercised delegated F path are exact on all 2336 branch-conditioned hypothetical-observation queries when O is available; F has 0/2336 defined answers when O is removed;
5. H/G do not implement the branch-conditioned interface;
6. prediction `K` and observation-assimilation/update `U` are separable components in this construction.

It does **not** establish:

- that H is or is not a world model;
- a universal taxonomy of extension axes;
- any formal complexity advantage of H;
- that parity factorisation exists outside this deliberately simple dynamics;
- independent causal validity beyond the action semantics already declared;
- robustness to regime shift;
- a necessary-and-sufficient definition of world model.

---

## 12. Restored next research gate

Toy C v0.3 had already pre-registered a different next test: determine whether the capability-contract description changes a **concrete engineering evaluation or decision** beyond what a flat technical description already determines.

That test was deferred when v0.4 was run; the substitution was not recorded contemporaneously and was identified by the independent review. v0.9.1 restores the earlier gate rather than opening Toy C v0.5 or a regime-change construction.

The stop condition is explicit:

> if capability-contract metadata changes no engineering decision that the flat technical description would not already change, the eliminativist alternative is strengthened and the mechanical Toy C chain stops.

A regime/action/observation change may still be scientifically useful later, but only after this decision-relevance gate is resolved.

