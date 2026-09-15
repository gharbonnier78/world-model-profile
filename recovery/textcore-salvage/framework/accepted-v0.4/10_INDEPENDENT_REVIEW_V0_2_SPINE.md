# Independent Review — L0–L3 v0.2 Formal Spine + Finite-POMDP Separation

**Artifact reviewed:** `07_LAYERED_PROFILE_V0_2_NOTE.pdf` (7 pp.), `01_LAYERED_PROFILE_V0_2_FORMAL_SPEC.md`,
`02_TOY_F2_LAYER_SEPARATION.md`, `03_toy_f2_layer_separation.py`, `04_*`, `06_SOURCE_NOTES.md`.
**Review date:** 2026-09-08.
**Evidence produced by this review:** `independent_check.py`, `independent_check_output.json`
(recomputation built from the POMDP, not reusing the package's code path).

---

## Disposition

**PARTIAL ACCEPT / REQUEST CHANGES.**

Proposition 1 is arithmetically correct — every number in the package reproduces under an
independent enumeration. The formal spine is a real improvement on v0.1 and the claim discipline
is unusually honest. Three things block acceptance as a framework spine:

1. the shipped verification script does not test the claim it asserts (§E.1);
2. `δ_inv` (L1.a) is identically zero as defined, so L1.a has no content in the population setting (§B.1);
3. the toy does not yet defeat the eliminativist option the paper itself sets up in §10/§11 (§F).

None of the three is fatal. (2) is a definition repair, (1) is a rewrite of ~40 lines, and (3) is
roughly a page of additional work that the package is already positioned to do. I would expect to
return **ACCEPT AS FRAMEWORK SPINE** on a v0.3 that closes B1, E1, E3 and F1.

---

## E. Toy separation — independent recomputation

I rebuilt the environment as an explicit POMDP over states `(mode, phase)`, enumerated the three
reachable non-terminal histories, computed the projected latent laws from the environment rather
than from a declared kernel, and brute-forced **all 12 history-measurable and all 6 σ_C-measurable
deterministic policies** at each probe cost. IPM convention: `d_TV(μ,ν) = Σ|μ−ν|` (the L1
convention used in JMLR 23(12)); halve for the ½-normalised convention.

| Quantity | Package | This review |
|---|---|---|
| `δ_alias` | 0 | 0 |
| `δ_fit` | 0 | 0 |
| `δ_roll(1)`, `δ_roll(2)` | 0, 0 | 0, 0 |
| `η_{q_phase}(k)` | 0 | 0 |
| minimax AIS-AP1 error at `r` | ≥ ½ | ½ (exact) |
| `V*` at `c = 0.10` | 0.90 | 0.90 |
| `V_C*` at `c = 0.10` | 0.50 | 0.50 |
| Regret at `c = 0.10` | 0.40 | 0.40 |
| Regret law on `c ∈ [0, 0.60]` | `max(0, ½ − c)` | zero mismatches on the 61-point grid |

**No hidden use of task information was found in the L0 declaration.** 𝔸 = {q_phase} is reward-free,
and the coarse representation's L0 pass does not depend on the reward function or on `c`. The
separation is sound as stated.

### E.1 — BLOCKING: the executable artifact does not verify its central claim

`03_toy_f2_layer_separation.py` hard-codes its conclusions:

- `verify_l0_coarse()` computes the aliasing check as
  `next0 = next_coarse("r", action); next1 = next_coarse("r", action)`. These are the *same call*.
  `next_coarse` never receives the mode, so no two distinct histories are ever constructed and the
  test `next0 != next1` cannot fail for any environment. The `δ_alias = 0` assertion is `assert True`.
- `sigma_coarse` is defined and never called.
- `full_value(c)` and `coarse_value(c)` return the closed forms `max(0.5, 1−c)` and `max(0.5, 0.5−c)`.
  `run_grid` then asserts that their difference equals `max(0, 0.5 − c)` — an algebraic identity
  between two expressions written by hand. No history, no hidden mode, and no policy is enumerated.
- The module docstring nevertheless states "the environment and values are enumerated exactly."

The results are correct; the script is not evidence for them. Under this programme's own
preregistration and executable-verification discipline this is the most serious defect in the
package, and it is the kind of thing that, once noticed by a referee, casts retrospective doubt on
every computational claim in the project. **Required:** replace with an enumeration that constructs
the mode-distinguished histories, derives the projected laws from the environment, and brute-forces
the policy classes. `independent_check.py` in this review is one such implementation and is offered
for reuse.

### E.2 — The separation is real but weaker than the framing suggests

Two distinct failures are bundled under "L2 fails":

- the **AP1 reward-prediction** failure (`ε ≥ ½`) holds for *any* environment where a hidden variable
  enters the reward and not the projected dynamics. No probe is needed; this part is immediate from
  L0 being reward-free.
- the **regret** failure (`½ − c > 0`) genuinely requires the information-gathering action. Without
  `probe`, both commits are worth ½ and the coarse representation is optimal — regret 0.

Only the second is interesting, and it is the one the paper should foreground. As written,
Proposition 1 lets the reader take the AP1 line as the certificate of L2 failure; it is not one —
AIS Theorem 9 is a sufficient condition for *adequacy*, so a large `ε` proves nothing about regret
on its own. I checked the direction of the bound numerically: `α₁ = ½`, policy bound `2α₁ = 1.0`,
actual regret `0.40`. The bound holds and is loose by 0.6. **Required:** state that L2 failure is
certified by the direct regret computation, and report the AP1 lower bound as a separate diagnostic.

### E.3 — RECOMMENDED: report L0 as a frontier over 𝔸, not a point

The declared 𝔸 = {q_phase} guarantees the L0 pass, since a deterministic protocol phase is closed by
construction. This is not circular, but it is uninformative on its own. The informative statement is
where the pass *stops*. I computed the retention error for a richer level 𝔸′ = {q_phase, q_mode}:

```
η_{q_mode}(1) = 1.0   (TV/L1 convention; 0.5 half-normalised)
η_{q_mode}(2) = 0.0
```

So σ_C **fails L0 at 𝔸′**, and it fails at `k = 1` out of the revealed histories. Reporting
"passes L0 at 𝔸, fails L0 at 𝔸′, and the query separating them is exactly the one L2 needs" turns
the toy from a definitional observation into a statement with predictive content. This is the
cheapest available upgrade in the whole package.

Related: `η_q(k)` is defined for rollouts, but the failure above is really about **decodability at
the present step**. The clause should explicitly admit `k = 0`; otherwise a representation can
retain a query along every rollout while being unable to decode it now.

---

## A. L0

**A.1 — `δ_alias` is not independent of `δ_fit` as defined.** IPMs satisfy the triangle inequality,
so for any `K`,

```
δ_alias ≤ 2 δ_fit,     and    δ_alias/2  ≤  inf_K δ_fit(K)  ≤  δ_alias.
```

Under the sup-norm definitions in §3.1 there is no configuration where `δ_fit` is small and
`δ_alias` is large: the second quantity catches nothing the first misses, and `δ_fit = 0` forces
`δ_alias = 0` (as the toy shows). The stated motivation — preventing "a favourable average
transition conditional on `z`" from hiding distinctions — only bites when `δ_fit` is measured **in
expectation**, which is how every trained model is actually measured. **Recommended:** keep both,
but define `δ_alias` as the *irreducible floor* of `δ_fit` (the part no choice of `K` can remove) and
say plainly that the separation is informative only against an averaged fit loss.

**A.2 — the requested aliasing counterexample is structural, not incidental.** Both `P_σ(·|h,a)` and
`K(·|σ(h),a)` are pushed through σ on *both* sides. Every L0.a and L0.b quantity is therefore
invariant to anything σ destroys, so the answer to review target A.1 is "yes, always": a
representation can destroy an arbitrarily large projected future and keep `δ_alias = δ_roll = 0`,
because the discarded distinction is not in the space where the comparison happens. This yields a
proposition worth stating outright:

> **L0 holds exactly iff (i) the σ-projected process is Markov on Ω₀, (ii) `K` equals its kernel,
> and (iii) every `q ∈ 𝔸` is decodable from `z` along rollouts.**

Consequently `δ_roll` (target A.2) cannot rule out wrong state-contingent futures on its own, and
**all** of L0's discriminating power sits in 𝔸 and the oracle access L0.c requires. The paper
half-says this ("a labelled/oracle query is required"); it should say it as a result, because it is
the honest characterisation of what L0 is.

**A.3 — minimum admissibility condition on 𝔸 (target A.4).** 𝔸 is not so unconstrained that
*anything* passes — the degenerate `z ≡ 0` fails L0.c — but the passing class is very large. I would
require two things of any declaration:

1. a **non-vacuity certificate**: exhibit at least one natural competitor representation that fails
   L0 at the declared 𝔸;
2. the **finest 𝔸\*** at which the system still passes, so the claim is a frontier and not a point.

**A.4 — passive systems (target A.5).** The singleton-action convention is coherent and preferable to
deleting the action argument. But under it, L1's behaviour-policy class and L2's information-action
closure are not merely undeclared, they are *inapplicable*. Add `not applicable` to the four status
values in §8, or passive systems will be reported as if they had simply skipped a test.

---

## B. L1

**B.1 — BLOCKING: `δ_inv` is identically zero.** Given the full history `h` and action `a`, the law
of the next observation — hence of `σ_{t+1}(H_{t+1})` — is fixed by the environment. A behaviour
policy β influences *which* `(h,a)` are visited, not the conditional law given `(h,a)`. So for any
`β, β′` whose common support contains `(h,a)`, `P_β^σ(·|h,a) = P_{β′}^σ(·|h,a)` exactly, and
`δ_inv = 0` in every well-specified model. It becomes non-zero only through (i) finite-sample
estimation, or (ii) a behaviour policy that is not `h`-measurable (latent-dependent behaviour, i.e.
confounding).

The stated rationale inverts the situation. "Using the full history in this comparison avoids
hiding policy-dependent differences behind a second averaging over a potentially aliased latent `z`"
— but policy-dependent aliasing *is* that averaging. Conditioning on `h` removes precisely the
effect L1.a is meant to detect.

**Required:** make L1.a a pair.
- `δ_inv^latent := sup d_F(K_β(·|z,a), K_{β′}(·|z,a))` over kernels fitted from data collected under
  each behaviour policy — this is where policy-dependent aliasing appears, and it answers target B.1
  in favour of latent-conditioned invariance;
- the history-conditioned comparison retained explicitly as a **support / estimation-consistency
  check**, with a note that its population value is zero by construction.

**B.2 — `δ_do` collapses to `δ_fit` in the interactive case (target B.2).** When the agent's action is
the only intervention point and the behaviour policy is `h`-measurable, `do(A_t = a)` and
conditioning on `A_t = a` coincide, so `δ_do = δ_fit` and L1.b carries no information beyond L0.a.2.
L1.b has genuine content only under (i) confounded offline data, or (ii) interventions on non-action
variables. The distinction between `δ_inv` and `δ_do` is correct in principle but, as written, is
not yet sufficient to prevent observational invariance being reported as causal validity, because in
the common case both quantities are measuring the same thing. State the condition under which
`δ_do ≠ δ_fit`.

**B.3 — the missing quotient condition (target B.3).** `do` on a lossy quotient is not well defined in
general. The condition you need is that σ be a **causal abstraction** in the exact-transformation
sense — Rubenstein et al. (UAI 2017), *Causal Consistency of Structural Equation Models*, or
Beckers & Halpern (AAAI 2019), *Abstracting Causal Models* (constructive abstraction). Without one of
these, `Law(σ(H_{t+1}) | do(A_t = a))` is a coincidence of the particular σ chosen, not a property of
the intervention. Adding this is a two-sentence fix and closes a real hole.

---

## C. L2

**C.1 — AIS and VE are kept sufficiently distinct (target C.1).** Yes. I would add one sentence on
the *relation* rather than only the separation: both are decision-relative sufficiency notions
differing in what is quantified — AIS compresses the history into a statistic; VE constrains the
model class by the Bellman updates it induces. Asserting only that they are different invites the
question of why both are needed.

**C.2 — AIS Theorem 9 is reproduced faithfully (target C.2).** Verified line by line against the
primary source (see §Provenance). Definition 7, AP1, AP2, the recursion `α_{T+1} = 0`,
`α_t = ε_t + ρ_F(V̂_{t+1})δ_t + α_{t+1}`, the value bound `α_t`, and the policy bound `2α_t` are all
correct, and the finite-horizon choice is the right one for a finite-horizon toy. Two additions
worth making if the bound is ever used quantitatively: the source's **Remark 11** gives a tighter
`Δ*_t(V̂_{t+1})` in place of `ρ_F(V̂_{t+1})δ_t`, and **Remark 12** gives an alternative recursion in
`ρ_F(V_{t+1})`. In this toy the Theorem 9 policy bound is `2α₁ = 1.0` against an actual regret of
`0.40`, so the looseness is not hypothetical.

**C.3 — the L2.G / L2.O split is useful, not duplicative (target C.3).** Keep it. It is the part of
the framework most likely to survive the eliminativist objection, because the He et al. result gives
it an empirical anchor that the flat tuple does not naturally express.

**C.4 — one declared `ν_off` is not enough (target C.4).** A single off-prior distribution is chosen
by the same party reporting the number, so it is gameable in exactly the way the MuZero finding
warns about. **Required:** either a supremum over a declared class `N`, or a stated concentrability
coefficient `sup_{z,a} ν(z,a)/μ_Π(z,a) ≤ C` reported alongside `E_off`. Without one of these,
`E_off` measures the reporter's imagination.

**C.5 — information-action closure is at the right level (target C.5)**, but the declaration tuple is
incomplete. §6 requires that the comparator policy be declared; §2's `D` has no slot for it, and L2's
regret is meaningless without saying whether the comparator is the history-optimal policy (as in the
toy) or the best member of Π. **Required:** add `π_ref` to the L2 and L3 components of `D`.

---

## D. L3

**D.1 — correctly treated as system-level (target D.1).** Yes, and the explicit list of alternative
mechanisms (adaptation, memory, policy switching, planner compensation) is the right guard.

**D.2 — Richens–Everitt is stated faithfully but under-qualified (target D.2).** "Must have learned an
approximate causal model" is the source's own abstract phrasing, so the wording is defensible. Two
tightenings are needed. First, the source's stated limitation is more specific than "a sufficiently
rich set of distribution shifts": Theorems 1 and 2 require robustness to **local interventions on all
environment variables**. Use that phrasing, since it is the condition a project's Δ must actually
instantiate. Second, what licenses the "has learned" reading is that the model is *extractable from
the agent's policy*; without that clause, the sentence reads as a claim about internal
representation, which the theorem does not make.

**D.3 — one unearned relation, in the direction of too little rather than too much (target D.3).** §7
asserts default orthogonality, but `L0.a.2` with `δ_fit ≤ δ` **is** AIS-AP2 for the compression σ. So
`L0 ⇒ AIS-AP2` holds and should be stated. The paper currently notes only the converse
non-implication. Claiming the entailment strengthens the framework: it shows the profile connects to
imported results rather than sitting beside them.

---

## F. Contribution boundary — the section that decides the paper

**As it stands, the eliminativist option wins on the evidence in this package.** Everything in
Proposition 1 is expressible as an AIS report: `ε = ½` at the revealed phase, `δ = 0`, exact regret
`max(0, ½ − c)`. Three numbers, no layers. Worse for the framing, the coarse representation is
*literally* an instance of the imported source's own §3.3 Example 2 ("state abstraction in MDPs"),
so a referee can reasonably say the toy re-derives a worked example of a result the paper imports.
`(σ, K, sufficiency class, shift class)` survives the toy unscathed.

Two changes would flip this, and both are within a page of work.

**F.1 — publish the reverse separation (L2 pass / L0 fail).** This is the direction that shows the
layers are not a ladder, and §7 asserts orthogonality without exhibiting it. It is nearly free: take
a noisy-TV MDP with state `(x, n)`, reward and `x`-dynamics independent of `n`, and a model that
mispredicts `n′`. Declare the value class as functions of `x` only. I verified this numerically:

```
δ_fit(model) = 1.5          (TV/L1)   → L0 fails
max Bellman gap on declared V class = 0.0  → L2.G-VE passes exactly
```

Provenance is clean — this is Feinberg (2005) / the Noisy-TV problem, cited as Example 4 in the AIS
paper you already import. With both directions published, orthogonality becomes a demonstrated
property instead of a stipulation, and the "is this just a taxonomy?" objection loses its force.

**F.2 — make L0 a frontier over 𝔸 (see §E.3).** The claim worth making is not "σ_C passes L0" but
"the finest 𝔸 at which σ_C passes L0 is strictly coarser than the 𝔸 that L2 sufficiency requires,
and the gap is exactly the reward-relevant query." That is a statement about layer structure that
the flat tuple does not naturally make.

If neither is done in v0.3, I would recommend the eliminativist option in §11 on schedule rather
than carrying the taxonomy forward.

---

## Provenance check

Every record below was verified against the primary source, not against the handoff.

| Cited | Status |
|---|---|
| Subramanian, Sinha, Seraj & Mahajan, JMLR **23(12):1–83**, 2022 | ✅ correct (ACM pagination 483–565 for the same article) |
| AIS **Definition 7**, AP1 / AP2 as quoted | ✅ verbatim match |
| AIS **Theorem 9**: `α_{T+1}=0`, `α_t = ε_t + ρ_F(V̂_{t+1})δ_t + α_{t+1}`; value ≤ `α_t`; policy ≤ `2α_t` | ✅ correct, assumptions preserved |
| Grimm, Barreto, Singh & Silver, VE, NeurIPS 33, 2020 | ✅ author order correct |
| Grimm, Barreto, Farquhar, Silver & Singh, PVE, NeurIPS 34, 2021 (pp. 7773–7786) | ✅ |
| Grimm, Barreto & Singh, AVE, NeurIPS 35, 2022 | ✅ |
| Ni, Eysenbach, Seyedsalehi, Ma, Gehring, Mahajan & Bacon, ICLR 2024, arXiv:2401.08898 | ✅ all seven authors correct |
| He, Moerland, de Vries & Oliehoek, ECAI 2024, arXiv:2306.00840 | ✅ — add **pp. 1599–1606**, FAIA vol. 392, DOI 10.3233/FAIA240666 |
| MuZero finding as rendered in §5.2 | ✅ faithful to the source abstract |
| Richens & Everitt, ICLR 2024, arXiv:2402.10877 | ✅ — qualify the shift class as *local interventions on all environment variables* (see D.2) |
| Richens, Everitt & Abel, PMLR **267:51659–51687**, ICML 2025 | ✅ record exact **as cited** |

⚠ **One provenance trap.** The arXiv version of the last entry (2506.01622) has been **retitled**
*General agents contain world models* and lists **four** authors (Richens, Abel, Bellot, Everitt).
The PMLR record is the three-author "need" version. `06_SOURCE_NOTES.md` cites the PMLR record and is
correct; if the arXiv link is ever added, the title and author list must be changed to match.

⚠ **Missing prior work — the largest submission risk in the package.** The classical state-abstraction
taxonomy is absent from both the spine and the source notes:

- Li, Walsh & Littman (ISAIM 2006), *Towards a Unified Theory of State Abstraction for MDPs* —
  `φ_model` (model-irrelevance) through `φ_Q*`, `φ_a*`, `φ_π*`;
- Givan, Dean & Greig (Artificial Intelligence 147(1–2):163–223, 2003) — stochastic bisimulation and
  model minimisation;
- Ferns, Panangaden & Precup (UAI 2004) — bisimulation metrics.

Under the characterisation in §A.2, L0 is close to `φ_model` with the reward component dropped and a
declared label set 𝔸 added, and Proposition 1 is close to the textbook fact that a reward-blind
model-irrelevance abstraction need not be `Q*`-irrelevant. The AIS paper you import discusses exactly
this literature in its §2.5 and §3.8, so its absence here will be noticed. The paper's genuine delta
over that literature is the **value-of-information** structure — the probe makes the discarded
distinction decision-relevant without making it dynamics-relevant — and that is what should be
foregrounded in §9, with the classical taxonomy cited as the baseline it improves on.

---

## Required modifications, in priority order

**Blocking**

1. Replace `03_toy_f2_layer_separation.py` with a real enumeration (§E.1).
2. Redefine `δ_inv` on latent-conditioned kernels fitted per behaviour policy; keep the
   history-conditioned form as a support check and state that its population value is zero (§B.1).
3. Certify L2 failure by the regret computation; demote the AP1 lower bound to a diagnostic (§E.2).
4. Add the classical state-abstraction citations and position L0 against `φ_model` (§Provenance).

**Strongly recommended**

5. Publish the reverse separation, L2 pass / L0 fail (§F.1).
6. Report L0 as a frontier over 𝔸, including `η_{q_mode}(1) = 1.0` for σ_C at 𝔸′ (§E.3, §F.2).
7. Restate `δ_alias` as the irreducible floor of `δ_fit`, with the `δ_alias ≤ 2δ_fit` relation (§A.1).
8. Add the L0 characterisation proposition (§A.2).
9. Require a coverage or concentrability condition on `ν_off` (§C.4).
10. Add `π_ref` to the declaration tuple `D` (§C.5).
11. Require σ to be a causal abstraction (Rubenstein et al. 2017 / Beckers & Halpern 2019) before
    `δ_do` is well posed (§B.3).
12. Qualify Richens–Everitt as local interventions on all environment variables, and note the
    extraction-from-policy clause (§D.2).

**Minor**

13. Admit `k = 0` in `η_q(k)` (§E.3).
14. State `L0 ⇒ AIS-AP2` rather than asserting blanket orthogonality (§D.3).
15. Add `not applicable` to the §8 status values, for passive systems (§A.4).
16. Add page range and DOI for He et al.; one sentence relating AIS and VE (§C.1, §Provenance).

---

## What the review did not find

No error in the arithmetic. No hidden task information in the L0 declaration. No overstatement of the
imported theorems beyond the two qualifications in D.2. No fabricated citation. The claim-discipline
section of `00_README.md` is accurate about what the package does and does not establish — which,
given how rarely that is true of framework papers, is worth saying explicitly.
