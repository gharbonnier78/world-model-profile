# Integrated Engineering Register — Method and Worked Passages

Companion to `13_ARXIV_DRAFT_PROSE_EXPANSION.md`. Same target: the 12-page arXiv draft.

## The recommendation, and the reservation

Yes — and there is a better route than the usual one. The usual route is intuition paragraphs
appended to definitions, and it fails predictably: the paragraph restates the formula in vaguer
terms, the theorist skips it, the engineer finds it too thin to act on, and the paper grows without
becoming clearer.

The route that works here is a **running register** rather than an added layer. This profile is,
structurally, an acceptance-and-qualification protocol: something is declared before measurement,
measured against budgets, and reported with a verdict that distinguishes *failed* from *not tested*.
That is not an analogy — the objects correspond one to one, which is why the vocabulary can be used
without hedging and without a single sentence of popularisation.

**The reservation.** The register makes claims sound more settled than they are. "Qualification
envelope" carries an implication of maturity that this framework has not earned. So it must be kept
out of the places where the paper concedes: the abstract, the eliminativist section, and the imported
theorems. Used there, it would convert honest uncertainty into procedural language, which is the one
tonal failure this manuscript cannot afford given how much of its credibility rests on §8 and §9.

A second, smaller risk: an ML audience tolerates ordinary engineering English and reacts badly to
certification jargon. The line is drawn below.

---

## The correspondence

Not a metaphor. Each row is the same object under two names.

| Profile | Test engineering | Function shared |
|---|---|---|
| declaration tuple 𝒟 | test contract fixed before measurement | prevents the claim being adjusted to the result |
| 𝔸 (query family) | characteristics under test | says what is being claimed, not just how well |
| Ω₀ | conditions of validity / declared envelope | bounds where the claim holds |
| ε, δ budgets | acceptance thresholds | separates "measured" from "acceptable" |
| pass / fail / not declared / not applicable | verdict codes | distinguishes failed from untested from inapplicable |
| non-vacuity certificate | a case the procedure must reject | proves the test can fail |
| 𝔸* frontier | qualification envelope | qualified to here, not beyond |
| case counts on `δ_roll(k)` | admissible-case coverage | an empty case set is not a pass |
| `δ_alias` vs `δ_fit` | floor vs residual | what is irreducible vs what is still open to work |
| `η_q` | traceability to an external reference | self-consistency is not accuracy |
| `ρ_pol`, ℬ | fault observability, available excitation | a fault you cannot excite is unobserved, not absent |
| `L2.O` vs `L2.G` | tested at self-selected operating points vs over the specified envelope | the classic acceptance failure |
| `C(ν‖µ_Π)` | coverage against the specified domain | how much of the envelope the test reached |
| `L3` compensation | redundancy masking a component fault | system pass with an internal fault unrepaired |

Where the correspondence is exact, use the vocabulary directly. Where it is not, say the thing
plainly instead — a forced correspondence is worse than none.

---

## Three integration devices, no new sections

**1. Failure-first framing.** Every definition currently arrives and is then explained. Reverse it:
state the failure the form prevents, then give the form as the answer. This buys more accessibility
per word than anything else available and costs one sentence per definition, because it replaces the
justification clause that is already there. It is also the device that keeps the paper rigorous: a
definition introduced as the answer to a stated failure cannot drift into decoration.

**2. Toy A as a recurring thread through §3.** The manuscript already contains a worked example and
uses it only in §4. Seeding it as a one-line instance under each L0 definition gives the reader a
concrete referent throughout, with no added structure and perhaps eight lines of total cost:

- §3.1 — "In Toy A the floor is zero: the two revealed histories genuinely do behave identically once
  projected to phase, so nothing here is an artefact of a badly fitted kernel."
- §3.2 — "Toy A's phase process is deterministic, so every admissible rollout is exact; the number
  worth reporting is not the zero but the count of cases behind it."
- §3.3 — the `k = 0` / `k = 1` / `k = 2` sequence, which carries both the mandatory `k = 0` term and
  the case-count rule at once.
- §3.4 — "phase passes, phase + mode fails; the separating query is the one the decision needs."
- §3.7 — "Toy A's comparator is the history-optimal policy; best-in-Π would give a different number."

By §4 the reader has met the construction five times and the section can move straight to the
mechanism instead of re-introducing the environment.

**3. Operational first sentence.** Open each subsection with the question in operational terms and
let the formalism answer it. This is pure reordering — no added length — and it is what makes a
formula-dense section readable.

What to avoid: labelled "Intuition:" paragraphs, boxes, sidebars, a glossary, "in plain terms"
restatements, and any announcement that a second reading is on offer. The register should be
invisible; the reader should simply find the paper unusually concrete.

---

## Worked passages

Draft-ready prose in the register. These replace existing text rather than adding to it.

### §3.1 — self-consistency and traceability

> Two of the three L0 quantities compare the system with itself. `δ_alias` asks whether histories
> that σ merges behave alike after projection; `δ_fit` asks whether `K` reproduces the projected law.
> Both comparisons take place inside the latent space, on both sides of the metric. Whatever σ
> discarded is absent from both sides, so neither quantity can register its loss: a compression can be
> perfectly self-consistent and still have destroyed everything that mattered.
>
> This is the ordinary distinction between self-consistency and traceability. An instrument that
> repeats itself is repeatable, not accurate; accuracy is established against an external reference.
> `η_q` is that reference — the only L0 quantity that compares the model against something the model
> did not produce, namely the true value `q(S)` of a declared query. Its cost is the usual cost of
> traceability: labelled or oracle access. That cost is the reason the abstraction level must be
> declared rather than inferred, and it sets a limit worth stating plainly — the queries one can
> afford to check are the queries one is entitled to claim.

### §3.1 — floor and residual

> `δ_alias` and `δ_fit` are not two estimates of the same error. `δ_alias` is a property of the
> compression alone and bounds what any kernel can achieve; `δ_fit` is where the current kernel sits.
> The relation `δ_alias ≤ 2δ_fit` shows they cannot be independent under a supremum, but the useful
> reading is directional: σ sets the floor, `K` sets the residual, and only the gap between them is
> available to further training. A report giving `δ_fit` alone leaves the reader unable to distinguish
> an undertrained model from a compression that has already thrown the information away — and those
> two situations call for opposite responses.

### §3.3 — why `k = 0` is mandatory

> A rollout-only report conflates two capabilities. A model may reproduce the *distribution* of a
> query at every future step and still be unable to state its value now: forecasting that half the
> units will be out of tolerance is not the same as measuring this unit. The `k = 0` term is what
> separates them.
>
> Toy A shows both halves. At the phase level every retention error is zero. At the richer level
> including the mode query, `η_{q_mode}(0) = η_{q_mode}(1) = 1` under the L1-TV convention: the coarse
> latent cannot decode the mode at the revealed histories, now or one step out. At `k = 2` the number
> returns to zero — not because decodability was recovered, but because the revealed histories have
> terminated and left the case set. The surviving path begins before the probe, where the
> uninformative forecast is the correct one. Reported without the case count, that zero would read as
> a pass.

### §3.4 — the frontier as an envelope, and the negative case

> An L0 claim is meaningful only relative to a declared 𝔸, and an impoverished 𝔸 makes the claim
> automatic. Declaring 𝔸 = {q_phase} over Toy A's deterministic protocol means the pass follows from
> the protocol and not from anything the representation achieved.
>
> A report consisting only of passes is therefore incomplete in a specific way: it does not establish
> that the procedure could have produced a failure. We require a non-vacuity certificate — a natural
> richer level at which the same representation fails — for the same reason an acceptance procedure
> includes a case it is expected to reject. Absent that, a pass is evidence about the choice of 𝔸
> rather than about the system.
>
> Reported this way an L0 result is an envelope rather than a verdict: closed at phase level, not
> closed once the mode query is added, with the separating query named. That is also the form in which
> the result is comparable across systems, since two systems that both "pass L0" at undeclared levels
> cannot be compared at all.

### §3.5 — observability of a compression defect

> [after the mixture bound]
>
> The bound has a direct operational reading. A change of acquisition policy cannot create a
> compression defect; it can only make some fraction of an existing one visible, and the fraction is
> capped by the weight spread the declared behaviour class can produce. This is the familiar situation
> of a fault that the available excitation cannot excite: it is not absent, it is unobserved.
> Reporting `ρ_pol` next to `δ_alias` keeps two different statements apart — how much compression loss
> exists, and how much of it the declared acquisition class is able to reveal. Only the second changes
> when the behaviour class changes, which is precisely why this is a diagnostic inside L0 and not a
> coordinate of its own.

### §3.7 — an evaluation the system selects for itself

> `µ_Π` is not chosen by the evaluator. A planner steered by the model's own value estimates avoids
> regions the model reports as unpromising — including regions the model reports as unpromising
> because it is wrong about them. Error measured under `µ_Π` therefore partly measures the system's own
> avoidance behaviour, and the loop closes: the model determines where it is examined, and it is
> examined where it is accurate.
>
> This is an acceptance test conducted only at operating points the system selects for itself. Such a
> test passes, and the pass carries little information about the specified envelope. `L2.O` exists so
> that such a result is not read as `L2.G`. It also explains why a single hand-picked off-prior
> distribution is insufficient: chosen by the same party, it inherits the same selection problem.
> Either a supremum over a declared family or an explicit coverage coefficient is required, and the
> coefficient should be reported even when it is unflattering, since an unreported coverage figure is
> indistinguishable from a coverage figure of one.

### §3.8 — a system-level pass with an internal fault

> A system can meet a regret bound under shift through online adaptation, through memory that
> identifies the regime, through replanning that corrects a wrong model at query time, or through a
> second component that compensates for the first. Each produces a system-level pass with an
> unrepaired internal fault — redundancy masking a component failure during acceptance. An `L3` pass
> therefore licenses a claim about the system and about nothing inside it, and the profile records it
> as a system-level entry for that reason rather than as a property of `K`.

### §4.1 — Toy A, mechanism and reading

> The mechanism is that the hidden mode enters the reward and does not enter the projected phase
> dynamics. L0 is reward-free, so a variable that moves only the reward is invisible to it; the phase
> process is genuinely closed and its closure is not an artefact.
>
> That alone would produce no regret. Without the probe both commitments are worth ½ and the coarse
> representation is optimal — a distinction unknowable at decision time costs nothing to discard. The
> probe is load-bearing: it makes the discarded distinction acquirable, and the gap it opens is the
> value of the discarded information net of its price. Below `c = ½` the measurement is worth taking
> and the representation cannot take it; above, the measurement does not repay its cost and the loss is
> free.
>
> The construction is therefore not an example of a coarse representation performing badly. It locates
> the condition under which a distinction irrelevant to the projected dynamics becomes
> decision-relevant: when the decision class contains an action that acquires it.

---

## Vocabulary

**Use** — each carries shared structure: declared envelope, conditions of validity; acceptance
threshold, budget; verdict; a case the procedure must reject; coverage, admissible cases; floor and
residual; traceability, external reference; observability, excitation; operating point; redundancy
masking a fault.

**Do not use** — ornament, or audience-narrowing: standards names and certification acronyms
(DO-178C, ISO 26262, IEC 61508, V&V, IV&V, TRL); "shall" requirement phrasing; anything drawn from
EO/IR, biometrics, or any specific programme; and any metaphor that is not a structural
correspondence — no maps, no blueprints, no "think of the model as".

**Do not apply the register at all** in the abstract; in §2, which should stay in the ML literature's
own voice or the paper will look unfamiliar with its field; in the statements of imported theorems,
which must be given in their sources' terms; and in §6, where the paper concedes and must sound like
it means it.

---

## Cost

Roughly one page on twelve. Failure-first framing and operational first sentences are reorderings and
replacements, not additions. The Toy A thread costs about eight lines. The passages above are net
neutral to slightly negative in length against what they replace, because concrete formulations are
usually shorter than the abstract ones they displace.

The gain is not only readability. Three of these passages — traceability in §3.1, observability in
§3.5, self-selected operating points in §3.7 — state limitations of the framework more precisely than
the current text does. That is the argument for the register that matters: it is not a second reading
laid over the paper, it is a sharper way of saying what the paper already means.
