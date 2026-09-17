# Independent Review — research draft v0.9 / Toy C v0.1–v0.4

**Reviewer:** Claude, acting as independent adversarial reviewer under
`review/CLAUDE_FULL_REVIEW_HANDOFF_V0_9.md`.
**Repository:** `gharbonnier78/world-model-profile`, branch `research/state-sufficiency-vs-world-modelhood`.
**Pinned evidence target:** `c209b7adbbee3444319cb775c99ce572f301d37e`.
**Review date:** 2026-09-17.
**Nothing in the repository was edited during this review.**

Post-pin commits verified as documentation-only:
`git diff --stat c209b7a..HEAD` → `STATUS.md`, `paper/README.md`, `review/README.md` only
(commits `d5004ad`, `64eb150`, `720a35b`). No scientific change after the pin.

---

## 1. Dispositions

### A. Manuscript / evidence

**`ACCEPT WITH CHANGES`**

All four verifiers reproduce byte-identically, every domain count is independently
confirmed by arithmetic, and the computation path derives its truths from the explicit
finite environment in exact rational arithmetic. Three defects block acceptance as a
clean snapshot: one result in the headline table is not an independent measurement
(§12.1), the prior art the construction is closest to is uncited (§12.2), and one
section heading claims falsification the text correctly declines to claim (§12.3).

### B. Chronicle / trajectory

**`COHERENT WITH DRIFT RISK — REPAIR BEFORE NEXT STUDY`**

The Chronicle is more honest than most published research records: the v0.1 limitation
is recorded at v0.1 rather than after v0.2 repaired it, abandoned hypotheses are
preserved with their disposition, the eliminativist competitor is kept alive at every
step, and the MMALS source note is represented faithfully — I verified this against
`gharbonnier78/mmals` directly. It is not manufacturing coherence.

But three specific repairs are needed before the next study. Hypothesis **H5 first
appears in the same documents that refute it** (§6.3). The test v0.3 actually
pre-registered was **not the test v0.4 ran**, and Chronicle 2's Trigger substitutes one
for the other without saying so (§6.4). The capability-contract tuple appears in **three
mutually inconsistent forms** across three documents (§6.5).

I did not choose `TRAJECTORY DRIFT — REFRAME` because the extension axis *was*
pre-registered in `research/toy_c_v0_3/TOY_C_V0_3_SPEC.md` §13, and because the object
under study has not actually left the original question — see §5.2, where Agent H turns
out to be the research note's own candidate object minus one component.

### C. Overall next step

**Stop the mechanical Toy C chain. Do not run Toy C v0.5 as another construction in the
same environment. Run the test v0.3 already pre-registered, before any new environment.**

Chronicle 1 ends with the right next step and an explicit stop condition:

> whether a **capability contract** can make experimentally different predictions or
> change an engineering decision […] If that contract adds no decision-relevant
> information beyond a flat technical description, the eliminativist alternative becomes
> stronger.

That test was skipped. It is cheaper than a regime-change experiment and it is decisive
in either direction. Running a regime-change study first would add a fifth construction
before the fourth has been cashed out.

---

## 2. Executive assessment

The mechanical work is sound. Four verifiers, byte-identical regeneration, exact
`Fraction` arithmetic throughout, no hard-coded answers on the computation path, and
every one of the six domain counts in the handoff reproduces from first principles.
On reproducibility this package is in better shape than most preprints.

The scientific reading is weaker than the package presents it. The central claim of
v0.4 — that Agent H shows long-horizon extension without a full generative model, so
extension is not a scalar discriminator — survives only under a naming choice the
handoff explicitly warned against. Agent H stores 292 exact posteriors plus the exact
closed-form action-conditioned transition operator of the task subsystem. In the
project's own notation (`research/STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md` §6,
`M = (σ, U, K, Q)`), **H is that object minus `U`**. The parity rule is not an
alternative to a model of the X-dynamics; it is that model, solved in closed form.
`terminal_y_probability_from_bx` computes the ground truth by iterating `trans_x`;
`answer_H` applies the closed form of the same involution. The 148920 checks confirm
that a ℤ/2 action composes by parity.

So the scoped finding is real but different from the stated one: **open-loop endpoint
prediction needs a belief and a transition operator; assimilating new evidence needs the
observation model; these are separable.** That is the classical prediction-versus-filtering
split. It is a correct, cleanly witnessed instance — and it is not news about extension.

The environment does most of the work. Horizon extension is free by construction because
the task dynamics are a deterministic involution; history extension is impossible by
construction because no update rule was written. One axis is trivial and the other is
unreachable, both by design. This is the same pattern flagged against Toy A in the v0.2
spine cycle: a separation engineered by declaration. The project has now repeated it.

The `E` tuple is not a new taxonomy. Six of its seven axes are components of the
accepted declaration tuple `D` under different names (§7.2). That is good news — it
means no `L4` is warranted and v0.4 supports the frozen spine — but the manuscript
presents `E` as new exploratory metadata without noticing it is largely `D`.

On the eliminativist question, Toy C v0.1–v0.4 strengthens the competitor. Every result
is expressible in `(σ, K, Q, boundary, source)`, and the one genuinely new axis —
source/boundary provenance, from v0.3 — is a systems-engineering attribute, not a
world-model attribute. The positive residue after four constructions is "declare which
axis you extended," which is advice about reporting.

---

## 3. Mechanical verification

### 3.1 Commands run

```bash
git clone https://github.com/gharbonnier78/world-model-profile.git
git checkout research/state-sufficiency-vs-world-modelhood
python3 research/toy_c_v0_1/verify_toy_c_v0_1.py   → diff vs results_v0_1.json
python3 research/toy_c_v0_2/verify_toy_c_v0_2.py   → diff vs results_v0_2.json
python3 research/toy_c_v0_3/verify_toy_c_v0_3.py   → diff vs results_v0_3.json
python3 research/toy_c_v0_4/verify_toy_c_v0_4.py   → diff vs results_v0_4.json
```

| Verifier | Exit | Output vs committed |
|---|---|---|
| `verify_toy_c_v0_1.py` | 0 | byte-identical |
| `verify_toy_c_v0_2.py` | 0 | byte-identical |
| `verify_toy_c_v0_3.py` | 0 | byte-identical |
| `verify_toy_c_v0_4.py` | 0 | byte-identical |

### 3.2 Pinned artifact hashes

| Artifact | Recomputed | Matches `review/README.md` |
|---|---|---|
| `world_model_profile_research_v0_9.pdf` | `979b06b1…33dd3` | yes |
| `world_model_profile_research_v0_9.tex` | `7ea5b0f4…be691` | yes |

`SHA256SUMS.txt` in the v0.9 package: 23/23 OK. PDF opens, 19 pages, zero unresolved
`??` markers in extracted text.

### 3.3 Independent count arithmetic

Not string comparison — recomputed from the branching structure
(4 initial observations; ×8 per step for action×observation):

| Quantity | Derivation | Value | Handoff |
|---|---|---|---|
| histories depth 0/1/2/3 | 4, 4·8, 32·8, 256·8 | 4, 32, 256, 2048 | ✓ |
| conditioning histories `t ≤ 2` | 4+32+256 | **292** | ✓ (H seed count) |
| `D0` | 292 · (2+4+8) | **4088** | ✓ |
| horizon 4/5/6 | 292 · (2⁴+2⁵+2⁶) | **32704** | ✓ |
| depth-3 history extension | 2048 · (2+4+8) | **28672** | ✓ |
| parity non-regression | 292 · Σ₁⁸2ᵏ = 292·510 | **148920** | ✓ |
| branch-conditioned | 292 · 2·2·2 | **2336** | ✓ |

All seven agree. Source removal (`answer_F(..., service_available=False)` → `None`) and
H's continued local availability confirmed in `results_v0_4.json`.

### 3.4 Code inspection — is anything hard-coded?

No. In `verify_toy_c_v0_4.py` the ground truth for every domain comes from
`terminal_y_probability_from_bx(bx, actions)` with `bx` from the forward enumeration
(`enumerate_reachable`), while `answer_M` independently recomputes `bx` via
`bx_from_full_history(h)`. `Fraction` throughout; no floats; no expected-value
constants on the computation path. This is materially better than the script rejected in
the v0.2 spine cycle.

**One exception, at `verify_toy_c_v0_4.py:240–244`** — see §12.1.

---

## 4. Claim-by-claim Toy C review

### 4.1 Toy C v0.1 — state vs future-generating structure

- **Hypothesis attacked:** H1, that current-state sufficiency identifies modelhood.
- **Does it falsify or exploit a definitional choice?** Neither exactly. Agent A's
  incapacity is *stipulated*, not measured: the spec (§2) says "Its lack of future
  capability is architectural, not a numerical prediction error." So v0.1 does not
  falsify H1; it exhibits that the two capabilities can be separately specified. The
  spec is honest about this. The Chronicle is too.
- **Real content:** the B/C equivalence — a predictive-state agent and a full generative
  agent are exactly equivalent on the declared queries — is the substantive result, and
  it is genuine.
- **Recorded limitation:** `q` is an affine bijection of `b`, so no information-losing
  quotient yet. **Recorded at v0.1, not retrofitted.** Credit where due.
- **Verdict:** informative, correctly scoped.

### 4.2 Toy C v0.2 — non-injective quotient + Agent E

- **Hypotheses attacked:** the v0.1 limitation, and H2 (persistent recursive state
  necessary).
- **Real content:** `Δ_Y = 0`, `Δ_Z = 19/129` with an explicit witness (`q = 21/82`,
  `b^N ∈ {17/129, 112/129}`). This is a clean, exact demonstration that sufficiency is
  query-relative, and it is the strongest single result in the Toy C chain.
- **Agent E:** exact on 1080 open-loop queries with no persistent state. This weakens
  H2 — but H2 was the project's own candidate, not a formal theory. See §12.3.
- **Motivated by the previous failure?** Yes, directly and correctly: v0.2 attacks
  v0.1's recorded limitation rather than building on it.
- **Verdict:** the best step in the chain.

### 4.3 Toy C v0.3 — possession vs access vs compilation

- **Hypothesis attacked:** H3, that local internal ownership is necessary.
- **Real content:** M = F = G = 4088/4088 on `D0`; G = 0/4672 on horizon-4; F = 0/4088
  after source removal. Exact and correct.
- **Is the lesson stronger than the construction?** Slightly. The finite-compilation
  observation (`TOY_C_V0_3_SPEC.md` §8) is elementary and labelled as such — good. But
  "answer-equivalence cannot identify internal model possession" is the definition of
  extensional equivalence, not a finding. The construction's genuine contribution is
  narrower: **it makes provenance and boundary into declared test-contract elements.**
  That is a systems-engineering contribution, and it is the first point at which the
  object of study starts sliding from *modelhood* toward *qualification*.
- **Verdict:** sound, correctly scoped, and the first drift-risk point.

### 4.4 Toy C v0.4 — typed extension / Agent H

- **Hypothesis attacked:** H5, extension capability as scalar discriminator.
- **Problem:** H5 is introduced by the same document that refutes it (§6.3).
- **Does the construction falsify it?** It refutes a claim nobody made, in an
  environment built so that one axis is free and another unreachable. See §5.
- **Is the next toy motivated by the previous failure?** The *axis* was pre-registered
  at v0.3 §13. The *test* was not the one pre-registered (§6.4).
- **Bookkeeping or informative?** Closer to bookkeeping than the chain's earlier steps.
  The genuine content is the prediction/update separation (§5.2), which is worth
  stating — under its own name.
- **Verdict:** technically exact, scientifically the weakest link in the chain.

---

## 5. Toy C v0.4 adversarial findings

### 5.1 Agent H — is the model hidden in the parity rule?

The handoff asks for a precise answer across four distinctions. Here it is.

- **No declared full generative model:** *true.* H has no observation model, no nuisance
  model, no filtering rule. `results_v0_4.json` and the code confirm this.
- **Possession of a task-specific law:** *true, and this is the crux.* Under
  `STAY/FLIP`, X evolves by a deterministic involution; the induced action of any finite
  sequence is determined by FLIP parity. The parity rule is the **exact closed-form
  action-conditioned transition operator of the task subsystem**, expressed in the
  coordinate `q = ¼ + b/2` that absorbs the emission channel.
- **Possession of a predictive mechanism:** *true*, at unbounded horizon.
- **Semantic disagreement over "model":** *this is where the claim actually lives* — and
  the handoff's warning applies. The paper obtains its result by calling K a "query
  program."

The demonstration is internal to the code. `terminal_y_probability_from_bx(bx, actions)`
computes the truth by iterating `trans_x` — i.e. by *running* the operator. `answer_H`
applies its closed form. The 148920 parity checks verify that these agree, which is the
statement that a ℤ/2 action composes by parity. The spec says so
(`TOY_C_V0_4_SPEC.md` §5.5: "No novelty is claimed for this algebraic fact"). But the
*conclusion* drawn from it — that horizon extension does not indicate model-like
structure — does not survive the observation that H holds the operator.

**The model is not hidden in the parity rule. The parity rule is the model.** What H
lacks is `U`, not `K`.

### 5.2 The scoped statement the construction actually supports

Using the project's own object from `STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md` §6,
`M = (σ, U, K, Q)`:

| Agent | σ | U | K | Q |
|---|---|---|---|---|
| A (oracle belief) | ✓ | — | — | current-state only |
| B / C | ✓ | ✓ | ✓ | full |
| E | recomputed | n/a | ✓ | open-loop |
| G (compiled) | — | — | — | `D0` only |
| **H** | ✓ on 292 histories | **—** | **✓ (closed form)** | endpoint |

H is `(σ, K, Q)` without `U`. Therefore the finding is:

> Open-loop endpoint prediction requires a belief and an action-conditioned transition
> operator. Assimilating a new observation requires the observation model. A mechanism
> can hold the first without the second.

That is the **prediction-versus-filtering decomposition**, standard since Åström (1965)
and Striebel (1965) and present in every POMDP treatment. Toy C v0.4 is a clean finite
witness for it. Stated that way it is defensible, modest, and correctly attributable —
and it makes the "conditioning-history extension" result inevitable rather than
surprising: H fails on new histories *because it has no filter*, which is the same fact
as "H lacks U", which is also why it has no branch interface. **The three axes v0.4
separates are not three independent findings. Two of them are one missing component.**

### 5.3 The environment engineers the conclusion

Horizon extension is free because X-dynamics are a deterministic involution — the
unique nontrivial structure for which a scalar seed plus a parity bit suffices. Make the
X-dynamics stochastic and H collapses immediately. History extension is impossible
because no `U` was implemented. So one axis is trivial by construction and another is
unreachable by construction, and "extension is multi-axis" follows from the design
rather than from the experiment.

This is the same objection raised against Toy A in the v0.2 spine cycle (a separation
obtained by declaring an abstraction that excludes exactly what the task needs). The
recurrence is worth naming in the Chronicle, because a research programme that keeps
producing separations-by-construction is at risk of measuring its own design choices.

*Interpretation disagreement, not factual defect.* The numbers are right.

### 5.4 Complexity / compression — `4088/292 = 14`

`TOY_C_V0_4_SPEC.md` §6.1 correctly refuses an MDL reading. It does not go far enough.
`14 = 2+4+8` is exactly the number of action sequences of length 1–3. The ratio is
therefore an **identity, not a measurement**: it would be 14 for any mechanism storing
one entry per conditioning history, regardless of the environment, the rule, or the
answers. The caveat should say "this is not a ratio between two independently determined
quantities" rather than "this is not MDL."

*Factual defect in framing, trivially repaired: delete the ratio or restate it as
|action sequences|.*

### 5.5 Scope confirmations requested by the handoff §3D

I confirm Toy C v0.4 does **not** establish: that H is or is not a world model; a
universal set of extension axes; causal/interventional validity beyond the declared
action semantics; robustness to regime shift; superiority of a capability-contract
framework; or a necessary-and-sufficient definition. `TOY_C_V0_4_SPEC.md` §11 already
says all six, accurately. No overreach found in the scope section itself.

---

## 6. Full Chronicle audit

### 6.1 Genealogy reconstruction

I reconstructed the chain from the spine, the v0.6 package, the research note and the
Toy C artifacts **before** reading either Chronicle, as instructed. The reconstructed
genealogy matches the handoff's ten-step list at steps 1–8. Steps 9 and 10 — "emerging
capability-contract / typed-extension language" and "proposed bridge back to adaptive
abstraction" — are where the record and the evidence diverge; see §6.3–6.5.

### 6.2 What the Chronicle does well

These are not courtesies; they are checks that passed and that commonly fail.

- **The v0.1 limitation is recorded at v0.1.** "The important limitation was immediately
  recorded: in v0.1 the predictive state `q` was an affine bijection of the full binary
  belief." Cross-checked against `TOY_C_V0_1_SPEC.md` §4 — it is there, in the original
  spec, not retrofitted.
- **Failures are preserved with dispositions.** H1–H3 carry "unchanged", "remains
  weakened", "weakened as a system-level necessity" across both Chronicle files.
- **Eliminativism is kept alive at every step**, including the stop condition at the end
  of Chronicle 1.
- **No inflation of finite counterexamples into general claims** in the Chronicle text
  itself. Each result is stated with its domain.
- **The MMALS note is represented faithfully** — verified against source (§8).

I looked specifically for retroactive projection of v0.4 concepts onto v0.1–v0.3 and
**found none**. The Chronicle is not manufacturing coherence.

### 6.3 Finding — H5 is created by the document that refutes it

`grep -rn "H5"` returns first occurrences in exactly four places, all v0.4 artifacts:

```text
research/toy_c_v0_4/TOY_C_V0_4_SPEC.md:458        (commit 5074c26)
research/toy_c_v0_4/verify_toy_c_v0_4.py:355      (commit ce78c00)
research/toy_c_v0_4/results_v0_4.json             (commit 56363ae)
history/2026-09-16_toy_c_v0_4_typed_extension.md:131 (commit 52f76c3)
```

H5 appears in neither `STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md` §5 (which lists
H1–H4), nor `TOY_C_V0_3_SPEC.md`, nor Chronicle 1. It is numbered as though it belonged
to the pre-registered series, and `TOY_C_V0_4_SPEC.md` §8 lists it alongside H1/H2/H3 in
a "Hypothesis disposition" table, which invites the reader to believe it was standing
before the experiment.

This is the canonical post-hoc pattern, and it is the one thing in the record that could
fairly be called manufactured coherence. It is also easy to repair honestly: say that
v0.4 formulated H5 as a candidate over-reading of v0.3 and then tested it.

*Factual defect in the record.*

### 6.4 Finding — the pre-registered test was replaced, silently

Chronicle 1 closes with an explicit next target and stop condition:

> whether a **capability contract** can make experimentally different predictions or
> change an engineering decision […] If that contract adds no decision-relevant
> information beyond a flat technical description, the eliminativist alternative becomes
> stronger.

`TOY_C_V0_3_SPEC.md` §13 says the same: test whether the contract "changes practical
evaluation decisions."

Chronicle 2's Trigger instead reads:

> The next mechanical question was therefore: Is "ability to extend beyond the finite
> benchmark" itself a meaningful scalar discriminator of model-like structure?

That is a different question. The pre-registered test was never run, and the
substitution is not acknowledged. The extension *axis* was pre-registered; the
*decision-relevance test* was the pre-registered experiment, and it was skipped in favour
of a fourth construction in the same environment.

This matters more than it looks: the skipped test is the one with a declared stop
condition. Skipping a test that could have ended the programme, in favour of one that
could not, is the structural signature of drift even when every individual step is
honest.

*Factual defect in the record; the first exact point of drift.*

### 6.5 Finding — the capability tuple has three incompatible forms

| Source | Tuple |
|---|---|
| `TOY_C_V0_3_SPEC.md` §13 | (query family, boundary, source, coverage, extension, availability, shift) |
| Chronicle 1, final section | (query family, boundary, source, coverage, extension, availability, intervention, shift) |
| `TOY_C_V0_4_SPEC.md` §7 / Chronicle 2 | (horizon, history, query, branch, source, intervention, shift) |

Between the first and second, `intervention` appears with no stated reason. Between the
second and third, four of eight entries are dropped (`boundary`, `coverage`,
`availability`, `extension`) and four new ones appear (`horizon`, `history`, `branch`,
and `extension` promoted from an entry to the name of the whole tuple).

A taxonomy that changes half its entries per document, with no derivation and no
recorded reason, is being fitted to the most recent construction. The handoff says "do
not accept a new taxonomy because it is convenient." I do not accept this one — see
§7.2 for what it actually is.

*Factual defect in the record.*

### 6.6 Drift test — explicit answer

**Is Toy C v0.1–v0.4 still answering the original question?**

> When does a sufficient representation of history become an actual internal model of
> the world — and is that transition a real technical boundary or only a naming
> convention?

Partly, and better than the record claims. The strongest available reading of the whole
chain is that it **answers the second half in the affirmative, by decomposition**: A has
σ; E has σ and K without persistence; F has access to K without possession; G has Q
without σ, U or K; H has σ, K and Q without U. Each candidate binary boundary fails
because "model" was never one component. That is a real result about the original
question, and it is the through-line the manuscript does not state.

**Where does drift begin?** Not at v0.1 or v0.2. The first step where the object changes
is **v0.3**, where the question becomes *where the capability lives* rather than *what
structure constitutes it* — defensible, since H3 was pre-registered. The drift becomes
actual at **v0.4**, and the exact point is `history/2026-09-16_toy_c_v0_4_typed_extension.md`,
the **Trigger section**: that is where the pre-registered decision-relevance test is
replaced by an invented hypothesis, and where the output of the cycle stops being a
statement about modelhood and becomes a reporting requirement ("name the axis that
changed").

The programme has not drifted into an unrelated taxonomy. It has drifted from *asking
what a model is* to *specifying how to report what a mechanism can do* — and it has not
acknowledged that change of research object. The manuscript should say this in one
paragraph. It would cost nothing and it is true.

---

## 7. Accepted-spine compatibility

### 7.1 No silent `L4`, no redefinition of L0

Confirmed. `WMProfile_D = ⟨L0[ρ_pol], L1_int, L2.G, L2.O,L3⟩` is unchanged in the v0.9
`.tex` §3. Toy C appears in a separate §5 titled "Post-v0.6 extension". `TOY_C_V0_4_SPEC.md`
§9 explicitly declines a new coordinate. `STATUS.md` says "Toy C does not add a framework
axis." No constitutive claim for model possession or typed extension was found.

### 7.2 What v0.4 actually is: `E` is `D` re-read as directions of widening

The handoff asks whether `E` is a genuinely missing coordinate. It is not. Compare it
with the accepted declaration tuple:

`D = (𝔸, H_𝔸, Ω₀, F, ℬ ; I ; T, H, Π, π_ref, U, ε, R, N ; Δ, π_ref)`

| `E` axis | Component of `D` |
|---|---|
| `E_horizon` | `H_𝔸` — declared rollout horizon |
| `E_history` | `Ω₀` — declared support |
| `E_query` | `𝔸` — declared query family |
| `E_branch` | a query type inside `𝔸` |
| `E_intervention` | `I` — declared intervention family |
| `E_shift` | `Δ` — declared shift class |
| `E_source` | **not in `D`** |

Six of seven axes are components of `D` under other names. `E` is not a new taxonomy; it
is the accepted declaration tuple read as the set of directions in which a declaration
can be widened. The one genuinely new axis, `E_source`, arrived at **v0.3**, not v0.4.

This is the most useful thing v0.4 produces and the manuscript does not notice it. It
simultaneously (a) explains why no `L4` is warranted, (b) strengthens the spine by
showing `D` already anticipates extension typing, and (c) removes any need to defend a
new taxonomy. **Answer to handoff §6: declaration metadata around L0/L2 claims — and
metadata `D` already carries.**

I do not recommend a new accepted coordinate. No separate review cycle is needed.

---

## 8. MMALS bridge audit

I cloned `gharbonnier78/mmals` and read
`docs/program/MMALS_DYNAMIC_MINIMAL_INFERENCE_PROGRAM_2026-08-24.md` directly.

**Representation is faithful.** "Smallest explainable inference system that remains
dynamically sufficient" (source §1), "complexity only on evidence", and
`REUSE → ADAPT → FORK → NEW REGIME` (source §2) are all accurately rendered. The source
note's own line 145 — "This MMALS direction is world-model-like but is **not
automatically a world model**" — is exactly the separation the Chronicle preserves. No
retrofitting found.

**No circular reasoning found.** The bridge in both Chronicle files runs in the
permitted direction: Toy C exposes a capability that extends along one axis and not
another → therefore refinement pressure could be axis-specific → therefore a possible
relation to `𝔸_t → 𝔸_{t+1}`. It is not "MMALS needs adaptive abstraction, therefore the
profile should become adaptive abstraction."

**Two fidelity notes, both non-blocking:**

1. The source note writes step 4 as **CANDIDATE** NEW REGIME, with step 5 **VERIFY** —
   "a novelty or distance signal is only a hypothesis trigger; it does not prove a real,
   stable, or causal regime." The WM documents render the sequence as
   `REUSE → ADAPT → FORK → NEW REGIME`, dropping both the word *candidate* and the
   VERIFY gate. The source is more careful than the quotation.
2. The inference in Chronicle 2 — that `𝔸_t → 𝔸_{t+1}` "can be triggered by a specific
   contract failure" — is **suggested by** Toy C, not established by it. Toy C never
   revises an abstraction; `𝔸` is fixed throughout all four versions. The hedge "gives a
   cleaner route toward" is appropriate; the sentence following it is firmer than the
   evidence.

---

## 9. Eliminativist comparison

After v0.1–v0.4 the evidence **strengthens the eliminativist alternative**, by the
project's own declared criterion.

Every Toy C result is a statement about `(σ, U, K, Q, boundary, source)`. The decomposition
in §5.2 is precisely a flat technical description, and it is *more* informative than any
of the modelhood predicates it defeats. Four candidate boundaries were tested and all
four failed — not because the boundary was hard to locate, but because "model" was never
a single component to begin with.

The one axis Toy C adds that the accepted tuple lacks — `E_source`, provenance and
system boundary — is a systems-engineering attribute. It belongs in an evaluation
contract. It says nothing about world-modelhood.

Against that, the strongest surviving argument for retaining the profile is unchanged
from the v0.2 spine review: the **abstraction frontier** reports an interval where a flat
tuple reports a point. Toy C neither strengthens nor weakens that argument — it does not
exercise the frontier.

I am **not** declaring eliminativism victorious on fuzzy usage, which the handoff
rightly forbids. I am reporting that the programme's own stop condition (Chronicle 1) has
now been met in substance and not tested in form. The honest position is: run the
decision-relevance test. If the capability contract changes no engineering decision that
`(σ, K, Q, boundary, source)` would not have changed, retire the predicate.

---

## 10. Citation and prior-art findings

### 10.1 Blocking gap — the two anchors the project relies on are uncited

The bibliography of `world_model_profile_research_v0_9.tex` contains 22 entries. It does
**not** contain:

- **Littman, Sutton & Singh, *Predictive Representations of State* (2001)**
- **Sutton, *Dyna* (1990/1991)**

Both are cited in the project's own
`research/STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md` §2.1 and §2.4 as the anchors for
exactly this question. And Agent B in Toy C v0.1 is, literally, a predictive state
representation: `q_t = P(O_{t+1}=1 | h_t, a_t=0)` with a recursive update rule and no
latent ontology. A referee in this area will ask why a construction built on PSRs cites
no PSR paper.

### 10.2 The Toy C sections contain zero citations

`grep -o "\\cite{[^}]*}"` over lines 422–615 of the `.tex` — the entire Toy C section,
v0.1 through v0.4 — returns **nothing**. Every engagement with information-state
sufficiency, predictive state, extensional equivalence and prediction/filtering is
uncited at point of use.

### 10.3 Nearest prior art to the *interpretation*

The handoff asks for prior art on the interpretation, not the equations. The closest:

| Toy C object | Established terminology |
|---|---|
| Agent B | predictive state representation (Littman, Sutton & Singh 2001; Singh, James & Rudary 2004) |
| Agent E | history-based vs state-based agents; sufficiency ≠ recursive updateability |
| M/F/G equivalence on `D0` | extensional (behavioural) equivalence; the finite-table compilation argument |
| H's horizon extension | closed-form multi-step prediction under a group action; *k*-step / macro-action models |
| **horizon vs history vs branch axes** | **prediction vs filtering vs smoothing** — Åström (1965), Striebel (1965), standard POMDP |

The last row is the important one. "Typed extension" is, in substance, the prediction/
update separation. The manuscript should cite it and claim the finite witness, not the
concept.

### 10.4 Open checks

`chen2026` (arXiv:2607.06401) and `cifuentes2026` (arXiv:2602.03146) postdate what I can
verify and remain unchecked from my side; the `richens2025` / `cifuentes2026` title
collision was resolved correctly in an earlier cycle and the bibliography reflects it.
The remaining 20 entries were verified against primary sources in the v0.2–v0.4 spine
cycles and are unchanged.

---

## 11. PDF / LaTeX integration findings

**Clean.** 19 pages, zero unresolved reference markers, internal `SHA256SUMS.txt` 23/23,
both pinned hashes match.

Toy C v0.4 appears consistently in: abstract (line 29), Toy C section (§5.5, line 562),
finite-results table (four rows), limitations, conclusion (line 752), and reproducibility
boundary (line 805). No stale "v0.8 is current" language: line 807 correctly describes
v0.6 as a frozen milestone, v0.7/v0.8 as preserved, v0.9 as the current post-v0.6
extension.

**One integration defect.** The results table row

```text
Toy C v0.4 & M/F branch-conditioned evidence queries & $2336/2336$ each
```

presents two independent measurements where only one exists. See §12.1.

**One wording defect.** §5.3's heading reads "Agent E: falsifying a strong recursive-state
requirement" while the body correctly says "weakens". See §12.3.

I could not recompile the `.tex` (no TeX distribution available in my environment); I
verified the rendered PDF and both pinned hashes instead. Layout-warning claims in
`MECHANICAL_VERIFICATION` are therefore unverified from my side.

---

## 12. Blocking findings

### 12.1 The branch-conditioned F result is not an independent measurement

**File:** `research/toy_c_v0_4/verify_toy_c_v0_4.py:240–244`

```python
truth = branch_truth_from_bx(bx, a0, y1, a1)
m = branch_truth_from_bx(bx_from_full_history(h), a0, y1, a1)
f = m  # external oracle is exact by construction
branch_M_exact += int(m == truth)
branch_F_exact += int(f == truth)
```

`f` is assigned from `m`. No `answer_F`, no `external_oracle_O`, no `service_available`
flag is exercised anywhere in the branch domain. `branch_F_exact` therefore cannot
differ from `branch_M_exact` under any behaviour of the delegated path, and in
particular the one property that distinguishes F from M — source dependence — is not
testable there.

*To be precise and fair: I mutated line 242 to an independently wrong computation and the
count did drop to 0/2336, so this is not a pure self-comparison like the script rejected
in the v0.2 spine cycle. The defect is that no F code path exists to be wrong.*

Compounding it, `answer_H` and `compiled_G` are never called on this domain either, so
"H/G interface unsupported" is a property of what was implemented, not a measurement.
The 2336 domain contributes no discriminating evidence.

The result nevertheless appears in the headline results table of the manuscript and in
`STATUS.md`.

**Minimum repair:** route F through `answer_F(..., service_available=...)` for the branch
domain and report it with and without the oracle; report H/G as "interface not
implemented" rather than as a measured result; change the table row to name M alone.

### 12.2 Missing prior art: PSR and Dyna

**Files:** `world_model_profile_research_v0_9.tex` bibliography; Toy C section lines
422–615.

The manuscript's own research note anchors the question on Dyna and PSRs; Agent B *is* a
PSR; neither is cited, and the entire Toy C section carries no citations at all.

**Minimum repair:** add Littman, Sutton & Singh (2001) and Sutton (1990/1991); cite them
at point of use in §5.1; add the prediction/filtering anchor (§10.3) where typed
extension is introduced.

### 12.3 "Falsifying" claimed where a self-authored candidate was weakened

**Files:** `world_model_profile_research_v0_9.tex:494` (section heading);
`TOY_C_V0_4_SPEC.md` §8 (H1/H2/H3/H5 "Hypothesis disposition").

H1–H5 are candidate hypotheses the project wrote itself, not formal theories held in the
literature. The body text of §5.3 says "weakens" and is correct; the heading says
"falsifying". The handoff asks explicitly that this distinction be made.

**Minimum repair:** retitle the heading to "weakening"; add one sentence in §5 stating
that H1–H5 are the project's own candidate criteria and that the toys are counterexamples
to them, not falsifications of a formal theory.

### 12.4 H5 is presented as pre-registered

**Files:** `TOY_C_V0_4_SPEC.md` §8; `history/2026-09-16_toy_c_v0_4_typed_extension.md:131`.

H5 first appears in the v0.4 artifacts (§6.3). Listing it beside H1/H2/H3 in a disposition
table implies it was standing before the experiment.

**Minimum repair:** one sentence in both files: H5 was formulated at v0.4 as a candidate
over-reading of v0.3, then tested.

### 12.5 The pre-registered v0.3 test is unrun and the substitution unrecorded

**Files:** Chronicle 1 final section; `TOY_C_V0_3_SPEC.md` §13;
`history/2026-09-16_toy_c_v0_4_typed_extension.md` Trigger.

See §6.4. This is the drift point.

**Minimum repair:** record in Chronicle 2 that the pre-registered decision-relevance test
was deferred and why, and restore it as the next target with its stop condition intact.

---

## 13. Non-blocking findings

1. **`4088/292 = 14` is an identity, not a ratio** (§5.4). Restate or delete.
2. **The `E` tuple is `D`** (§7.2). Stating this would strengthen the paper; not stating
   it leaves a taxonomy to defend that need not be defended.
3. **Three incompatible tuple forms** (§6.5). Pick one and note the revision.
4. **Two of v0.4's three axes are one missing component** (§5.2). H fails history
   extension and branch queries for the same reason: no `U`.
5. **Separation-by-construction, twice** (§5.3). Worth a Chronicle line, since it is now
   a pattern rather than an incident.
6. **MMALS `CANDIDATE` / `VERIFY` dropped from the quoted sequence** (§8).
7. **`𝔸_t → 𝔸_{t+1}` inference is suggested, not established** (§8). `𝔸` is fixed in all
   four Toy C versions.
8. **The chain's actual through-line is unstated** (§6.6): every candidate binary
   boundary failed because "model" was never one component. This is the paper's best
   sentence and it is not in the paper.
9. Layout-warning claims unverified from my side (no TeX available) — §11.

---

## 14. What should be done next

**Do not run Toy C v0.5 as a fifth construction in the same environment.** The
environment has been exhausted: it has produced one genuinely strong result (v0.2's
`Δ_Y = 0`, `Δ_Z = 19/129`), two sound but elementary ones (v0.1, v0.3), and one that is
a finite witness for a textbook decomposition (v0.4).

**Do not jump straight to the regime-change experiment either**, which both Chronicle 2
and `TOY_C_V0_4_SPEC.md` §12 propose. That would add a fifth construction before the
fourth has been cashed out, and it is the expensive option.

**Run the test that was already pre-registered and skipped.** Chronicle 1 specifies it
and gives it a stop condition:

> Take two systems that the accepted tuple `(σ, K, sufficiency class, shift class)`
> describes identically, and ask whether the capability contract
> `(query family, boundary, source, coverage, extension, availability, intervention, shift)`
> changes an engineering decision — which ablation is run, which shift class is declared,
> which component is replaced. If it changes none, the eliminativist alternative wins by
> the project's own criterion.

This is cheap, decisive in both directions, and it is the only remaining step that can
end the programme rather than extend it. That is what makes it worth running first.

**Before that**, make the five repairs in §12 and add the two paragraphs the record is
missing: the decomposition in §5.2 (which is the chain's real result), and the
acknowledgement in §6.6 that the research object changed from *what a model is* to *how
to report what a mechanism does*.

If the decision-relevance test comes back negative, the right outcome is not failure. It
is a short, honest paper reporting that four candidate modelhood boundaries were tested
exactly and all four dissolved into a component decomposition — with the eliminativist
conclusion earned rather than conceded. That would be a better contribution than a fifth
toy.

---

## Appendix — separation of criticism types

| § | Finding | Type |
|---|---|---|
| 12.1 | branch-conditioned F not independently measured | factual defect |
| 12.2 | PSR / Dyna uncited; Toy C section uncited | factual defect |
| 12.3 | "falsifying" in heading | unsupported claim |
| 12.4 | H5 presented as pre-registered | factual defect (record) |
| 12.5 | pre-registered test skipped, unrecorded | factual defect (record) |
| 5.1 | parity rule *is* the transition operator | interpretation disagreement |
| 5.3 | environment engineers the conclusion | interpretation disagreement |
| 5.4 | `14` is an identity | factual defect (framing) |
| 6.5 | three tuple forms | factual defect (record) |
| 7.2 | `E` ⊂ `D` | interpretation disagreement (favourable) |
| 9 | eliminativist strengthened | interpretation disagreement |
| 14 | run decision-relevance test first | alternative research direction |

No preference for a different research programme has been recorded as a blocking defect.
