# Layered World-Model Profile — v0.4 Candidate Framework Spine

**Status:** revision after independent review of v0.3.  
**Parent disposition:** `PARTIAL ACCEPT / REQUEST CHANGES`.  
**Goal of this revision:** close the four requested items for `ACCEPT AS FRAMEWORK SPINE`.  
**Claim discipline:** explication/evaluation framework only; no unique natural-kind definition and no claim that the elementary mixture bound below is novel.

## 0. v0.3 review result and v0.4 repair

The v0.3 reviewer:

- verified package integrity and reproduced both toys independently;
- cleared the executable-evidence blocker;
- established a structural relation:
  \[
  \delta_{\rm inv}^{\rm latent}\le \delta_{\rm alias},
  \]
  with equality when the declared behaviour-policy class can concentrate on each history inside a latent cell;
- found a shrinking-case-set artifact in horizon-indexed budgets;
- judged the current evidence sufficient for **non-identity** of L0 and L2, but not for non-collinearity in a non-degenerate regime;
- found bibliography entries unlinked in the LaTeX.

v0.4 therefore makes four substantive changes:

1. `δ_inv^latent` is **removed as an independent axis** and becomes the L0 attribution ratio
   \[
   \rho_{\rm pol}=\delta_{\rm inv}^{\rm latent}/\delta_{\rm alias}\in[0,1]
   \]
   when \(\delta_{\rm alias}>0\);
2. a finite witness reports \(\rho_{\rm pol}=1/2\) under a restricted \(\mathcal B\), and \(1\) under a rich \(\mathcal B\);
3. all horizon-indexed budgets carry case counts; empty sets are `NOT_APPLICABLE`, and zero-error values with no query-bearing histories are explicitly `NOT_INFORMATIVE`;
4. the framework claim is scoped to **non-identity established; non-collinearity in the non-degenerate regime not established**.

The LaTeX is also repaired with point-of-use citations and the verification stdout is regenerated cleanly.

---

# 1. Profile and declaration tuple

Let

\[
h_t=(o_{\le t},a_{<t}),\qquad z_t=\sigma(h_t),
\]

and let \(d_{\mathcal F}\) be a declared integral probability metric.

The v0.4 profile is

\[
\mathrm{WMProfile}_{\mathcal D}(X)
=
\left\langle
L0[\rho_{\rm pol}],\,
L1_{\rm int},\,
L2.G,\,
L2.O,\,
L3
\right\rangle .
\]

The behaviour-policy quantity is no longer a separate L1 coordinate.

Declare

\[
\mathcal D=
\Big(
\underbrace{\mathbb A,H_{\mathbb A},\Omega_0,\mathcal F,\mathcal B}_{L0};
\underbrace{\mathcal I}_{L1_{\rm int}};
\underbrace{\mathcal T,H,\Pi,\pi_{\rm ref},\mathcal U,\varepsilon,R,\mathcal N}_{L2};
\underbrace{\Delta,\pi_{\rm ref}}_{L3}
\Big).
\]

Statuses are:

- `pass (budget reported)`;
- `fail`;
- `not declared`;
- `not applicable`.

---

# 2. L0 — Predictive closure at a declared abstraction frontier

Define

\[
P_\sigma(\cdot\mid h,a)
=
\mathrm{Law}\big(\sigma(H_{t+1})\mid H_t=h,A_t=a\big)
\]

and candidate latent kernel \(K(\cdot\mid z,a)\).

## 2.1 Aliasing floor

\[
\delta_{\rm alias}
=
\sup_{\substack{h,h'\in\Omega_0\\\sigma(h)=\sigma(h')}}
\sup_{a\in A(h)\cap A(h')}
d_{\mathcal F}
\left(
P_\sigma(\cdot\mid h,a),
P_\sigma(\cdot\mid h',a)
\right).
\]

## 2.2 Worst-case latent-kernel fit

\[
\delta_{\rm fit}
=
\sup_{h\in\Omega_0}
\sup_{a\in A(h)}
d_{\mathcal F}
\left(
K(\cdot\mid \sigma(h),a),
P_\sigma(\cdot\mid h,a)
\right).
\]

Under the declared IPM/sup form,

\[
\delta_{\rm alias}\le 2\delta_{\rm fit},
\qquad
\frac{\delta_{\rm alias}}2
\le
\inf_K\delta_{\rm fit}(K)
\le
\delta_{\rm alias}.
\]

Thus \(\delta_{\rm alias}\) is an irreducible compression floor, not an independent success axis.

## 2.3 Conditional rollout

For legal action sequence \(a_{t:t+k-1}\),

\[
\delta_{\rm roll}(k)
=
\sup
d_{\mathcal F}\left(
K^k(\cdot\mid\sigma(h),a_{t:t+k-1}),
P_\sigma^k(\cdot\mid h,a_{t:t+k-1})
\right).
\]

Every reported \(\delta_{\rm roll}(k)\) must include its admissible case count. An empty case set is `NOT_APPLICABLE`; it is never scored as zero.

## 2.4 Query retention and frontier

For \(q\in\mathbb A\),

\[
\eta_q(k)
=
\inf_{g_q}
\sup
d_q\left(
\mathrm{Law}(g_q(\hat Z_{t+k})),
\mathrm{Law}(q(S_{t+k})\mid h,a_{t:t+k-1})
\right),
\]

for \(0\le k\le H_{\mathbb A}\).

Every \(\eta_q(k)\) report must include:

- total admissible case count;
- a query-bearing case count when the query can become uninformative because relevant histories terminate or leave support.

If the total set is empty: `NOT_APPLICABLE`.

If the total set is nonempty but no query-bearing histories remain: the numerical error may be reported for audit, but status is `NOT_INFORMATIVE`, never interpreted as recovered decodability.

An L0 claim is a **frontier**:

\[
\mathbb A^\star=\text{finest tested abstraction that passes},
\]

plus a natural richer \(\mathbb A'\) that fails when available.

This frontier is the main profile-level object presently not naturally captured by a single flat pass/fail predicate.

## 2.5 Classical baseline

L0 is positioned against, not above, the classical state-abstraction literature:

- stochastic bisimulation/model minimisation;
- model/value/action/policy abstraction;
- bisimulation metrics.

The current contribution is the profile syntax, abstraction frontier, and cross-layer localisation — not invention of abstraction theory.

---

# 3. Policy exposure of L0 aliasing — diagnostic, not axis

For behaviour policy \(\beta\), define

\[
K_\beta^\sigma(\cdot\mid z,a)
=
\int
P_\sigma(\cdot\mid h,a)\,
dP_\beta(h\mid z,a).
\]

Then

\[
\delta_{\rm inv}^{\rm latent}
=
\sup_{\beta,\beta'\in\mathcal B}
d_{\mathcal F}
\left(
K_\beta^\sigma(\cdot\mid z,a),
K_{\beta'}^\sigma(\cdot\mid z,a)
\right).
\]

Inside a latent cell the \(K_\beta^\sigma\) are mixtures of member-history projected laws. By convexity of an IPM in mixture weights,

\[
0\le\delta_{\rm inv}^{\rm latent}\le\delta_{\rm alias}.
\]

If \(\mathcal B\) is rich enough to concentrate on each member history, equality is attained.

Therefore `δ_inv^latent` is not an independent world-model coordinate.

For a declared restricted \(\mathcal B\) and \(\delta_{\rm alias}>0\), report instead

\[
\boxed{
\rho_{\rm pol}
=
\frac{\delta_{\rm inv}^{\rm latent}}
{\delta_{\rm alias}}
\in[0,1]
}
\]

as an **attribution ratio**:

> what fraction of the compression-induced aliasing can a change in the declared acquisition/behaviour policy expose?

If \(\delta_{\rm alias}=0\), \(\rho_{\rm pol}\) is `NOT_APPLICABLE`.

This quantity lives inside the L0 report.

## 3.1 Finite witness

Two histories \(h_0,h_1\) are merged into one latent cell, with projected successor laws

\[
P_0=\delta_A,\qquad P_1=\delta_B.
\]

Under L1-TV,

\[
\delta_{\rm alias}=2.
\]

For restricted behaviour mixtures \(p\in\{0.25,0.75\}\),

\[
\delta_{\rm inv}^{\rm latent}=1,\qquad
\rho_{\rm pol}=1/2.
\]

For the rich class containing the vertices \(p\in\{0,1\}\),

\[
\delta_{\rm inv}^{\rm latent}=2,\qquad
\rho_{\rm pol}=1.
\]

The witness shows the ratio is non-vacuous while confirming it is bounded by L0 aliasing.

---

# 4. L1_int — Interventional validity

The only independent L1 coordinate retained is interventional calibration.

A claim is asserted only when \(\sigma\) is compatible with a declared causal abstraction / exact-transformation relation for intervention family \(\mathcal I\).

When well posed,

\[
\delta_{\rm do}
=
\sup_{z,a}
d_{\mathcal F}
\left(
K(\cdot\mid z,a),
\mathrm{Law}(\sigma(H_{t+1})\mid z_t=z,\mathrm{do}(A_t=a))
\right).
\]

In an unconfounded online setting where \(A_t\) is the sole intervention point, this can collapse to ordinary transition fit. Independent content appears under confounded offline data or interventions beyond the agent action.

No dedicated L1_int toy is claimed in v0.4.

---

# 5. L2 — Decision-relative sufficiency

L2 remains non-constitutive and decision-relative.

## 5.1 AIS route

AIS asks when a history statistic supports approximate dynamic programming through reward and transition-prediction conditions. With matched IPM/kernel choices, L0 kernel fit corresponds to the transition-prediction component; reward prediction and theorem assumptions remain separate.

## 5.2 VE route

VE asks whether declared Bellman computations are preserved over policy/function classes.

AIS and VE are related but quantify different objects and remain separate routes.

## 5.3 Global vs operational adequacy

L2.G evaluates the declared class.

L2.O evaluates the actual model+search pair under \(\mu_\Pi\), but must additionally report either

\[
\sup_{\nu\in\mathcal N}E_\nu[\ell]
\]

or a declared coverage/concentrability coefficient.

Regret always names \(\pi_{\rm ref}\).

---

# 6. L3 — Robustness under declared shift

\[
\sup_{\delta\in\Delta}
\mathrm{Regret}_\delta(\pi;\pi_{\rm ref})
\le\rho.
\]

L3 is system-level. It does not imply robustness of a particular latent kernel.

When importing causal-world-model results, source conditions and extractability scope must be preserved exactly.

---

# 7. Finite evidence and its exact scope

## 7.1 Toy A

At

\[
\mathbb A_{\rm phase}=\{q_{\rm phase}\},
\]

Toy A has exact projected closure and zero phase-query error.

At

\[
\mathbb A'=\{q_{\rm phase},q_{\rm mode}\},
\]

mode-query error is 1 at \(k=0,1\) under L1-TV, so the richer abstraction fails.

The direct policy enumeration gives

\[
\mathrm{Regret}(c)=\max(0,1/2-c)
\]

and regret \(0.4\) at \(c=0.1\).

The AP1 error is a diagnostic only; L2 failure is certified directly by positive regret.

## 7.2 Toy B

Toy B has

\[
\delta_{\rm fit}^{\rm full}=1.5
\]

while the Bellman gap is exactly zero on the declared \(V_x\) class for all 256 deterministic stationary policies.

Thus the finite package establishes

\[
L0\not\Rightarrow L2
\qquad\text{and}\qquad
L2.G\not\Rightarrow L0.
\]

## 7.3 Scope restriction demanded by review

The correct conclusion is:

> **non-identity of L0 and L2 is established in the finite examples.**

The stronger statement is **not established**:

> L0 and L2 are non-collinear in a non-degenerate regime.

Toy A uses a very coarse phase abstraction; Toy B deliberately uses a value class blind to nuisance noise. A future manuscript needs at least one non-degenerate separation if it wants a stronger framework claim.

---

# 8. Eliminativist alternative

The eliminativist alternative remains live:

\[
(\sigma,K,\text{sufficiency class},\text{shift class},\ldots)
\]

may ultimately be clearer than retaining the term *world model*.

The current profile adds one demonstrably useful organisational object: the abstraction frontier

\[
(\mathbb A^\star\text{ passes},\ \mathbb A'\text{ fails}).
\]

This is real but thin. v0.4 therefore does **not** claim that the layered profile has defeated the eliminativist alternative.

---

# 9. Scope toward MMALS

Adaptive abstraction discovery/revision

\[
\mathbb A_t\rightarrow\mathbb A_{t+1}
\]

remains outside the framework spine.

That is still the stronger prospective bridge to MMALS: learning when the current quotient of histories should be REUSED, ADAPTED, FORKED, or replaced by a NEW REGIME.
