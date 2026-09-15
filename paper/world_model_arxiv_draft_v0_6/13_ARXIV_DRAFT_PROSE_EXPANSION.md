# Prose Expansion — arXiv Draft v0.1 (12 pp.)

Target: `world_model_profile_arxiv_draft_v0_1.pdf`. Section numbers follow that draft.

The draft's problem is not that anything is wrong. It is that almost every paragraph states a
result and then moves on, so the reader is never told *why* a quantity has the form it has, *what*
defect it catches, or *what* it structurally cannot catch. Sections 3 and 4 are the worst offenders:
§3 is a wall of definitions with roughly one clause of explanation each, and §4 states the toy
outcomes without ever explaining the mechanism that produces them.

What follows is expanded prose for the sections where explanation is missing, and argument
scaffolding for the four sections the rewrite guide reserves for the author's own voice. Nothing here
changes the frozen spine: the coordinates remain `L0[ρ_pol], L1_int, L2.G, L2.O, L3`, ρ_pol remains a
diagnostic inside L0, and the finite claims remain only `L0 ⇏ L2` and `L2.G ⇏ L0`.

Per the rewrite guide's step 5, each block carries a marker: **[imported]**, **[finite]**,
**[proposal]**, **[interpretation]**, **[open]**.

---

## §1 Introduction

> **Author's voice — scaffolding only.** The guide reserves this section. What follows is the
> *technical* opening move, which is argument rather than voice; the motivational paragraph is left
> as a prompt.

**The hook the draft is missing.** [interpretation] The paper currently opens with a survey of who
used the term and how. It would open far better with two systems that are both routinely called
world models and that fail *opposite* tests.

Take a high-fidelity video predictor. Given a history of frames it produces the next frames
accurately; it is, in a perfectly reasonable sense, predictively closed at the level of observations.
Now ask it which of two available actions leads to a better outcome. It has nothing to say — not
because it predicts badly, but because nothing in its training made the decision-relevant
distinctions survive.

Now take MuZero. Its latent dynamics do not reconstruct the environment; they are demonstrably
inaccurate when asked to evaluate policies outside the region the search prior visits. By any
predictive-closure standard it is a poor model of its environment. It also plans at superhuman level.

A binary predicate must either admit both systems or exclude both, and neither is right. The two
systems are not at different points on one scale. They are at different *coordinates*: one is strong
where the other is weak, and the two strengths are not comparable because they answer different
questions. That observation is the entire motivation for a profile, and it takes one paragraph.

> **Prompt for the author.** After that paragraph, one short paragraph on why the binary form
> bothered you specifically — presumably from the MMALS side: you were not asking "is this a world
> model?", you were asking whether a learner may discard part of its history. Say that in the first
> person, briefly, and then drop it. Reviewers forgive one sentence of motivation; they do not
> forgive three paragraphs.

**Then the four questions**, which the draft already has and which are good — but they should be
introduced as *the four things the two examples just came apart on*, not as a list arriving from
nowhere. And the contribution list should be trimmed: five bullets is two too many. The three that
survive scrutiny are the frontier formulation, the L2.G/L2.O split, and the bidirectional finite
separations. The other two are corollaries.

---

## §2 Lineage and related work

The draft's §2 reads as a bibliography with connective tissue. Rewritten, it should make three moves
in order, because the third is the one that determines whether a referee thinks the paper is honest.

**Move 1 — the idea is old, and the citation should be modest.** [imported] Craik's proposal that
nervous systems carry internal models that parallel external events, and Conant and Ashby's
regulator-model theorem, are the conceptual ancestry of every system in this literature. They are
cited here as lineage and nothing more. The good-regulator theorem in particular is routinely
over-cited: it holds under specific assumptions about the regulator's information and the optimality
criterion, and it does not license the general claim that any competent controller contains a model
of what it controls. Saying that explicitly costs one sentence and buys a great deal of credibility,
because a referee who knows the theorem is already suspicious by the time it appears.

**Move 2 — the formal machinery already exists, in three distinct traditions.** [imported] Classical
state abstraction asks when two states may be merged: Givan, Dean and Greig formalised stochastic
bisimulation and model minimisation, Ferns, Panangaden and Precup replaced the equivalence with a
metric and bounded value differences by it, and Li, Walsh and Littman organised the resulting notions
into a taxonomy running from model-irrelevance through value-, action- and policy-irrelevance.
Approximate information states ask the same question from the history side and, crucially, attach
*guarantees*: a compression that approximately preserves one-step reward and next-statistic
prediction supports an approximate dynamic program with an explicit error recursion. Value
equivalence asks it from the model side: a model is adequate if it induces the same Bellman updates
over declared policy and value-function classes.

**Move 3 — state the boundary before the reader does.** [interpretation] Nothing in L0 is a new
theory of state abstraction. L0's closest classical relative is a reward-free, model-level
abstraction claim, augmented by an explicitly declared query family. Toy A is close to the textbook
observation that an abstraction preserving the transition structure need not preserve `Q*` once
rewards are reintroduced; Toy B is a noisy-TV example. The paper claims neither phenomenon as new.

What it claims is narrower and should be stated in exactly these terms: **these three traditions are
never reported together, so a claim established in one register is routinely read in another.** A
system demonstrated to be value-equivalent on a narrow class gets described as "having a world
model"; a video model demonstrated to be closed at the observation level gets described the same
way; and the two descriptions are then compared as though they were commensurable. The contribution
on offer is a reporting discipline, not a theorem. A paper that says this plainly in §2 is much
harder to reject than one that leaves the reader to discover it in §6.

---

## §3 The profile

This is the section that most needs prose. The pattern to apply to every quantity is the same four
beats: **what it measures, what defect it catches, what it structurally cannot catch, and why this
form rather than the obvious alternative.** The draft currently supplies the first beat only.

### 3.1 Aliasing floor and kernel fit

[proposal] `δ_alias` and `δ_fit` answer two different questions that are easy to conflate. `δ_alias`
asks whether the *compression* is dynamically coherent: if σ merges two histories, do those histories
actually behave the same way once projected? `δ_fit` asks whether the *learned operator* is right
given that compression. The first is a property of σ alone; the second is a property of `K` given σ.

The draft states the relation
`δ_alias ≤ 2 δ_fit`, `δ_alias/2 ≤ inf_K δ_fit(K) ≤ δ_alias`
and calls it an elementary triangle-inequality consequence, which it is. What it does not say is what
that relation *means for reporting*, and this is the paragraph the reader needs:

[interpretation] Under the supremum form given here, the two quantities are not independent. If
`δ_fit = 0` then `δ_alias = 0` necessarily, so a reader may reasonably ask why both are reported. The
answer is that no model is ever trained against a supremum. Training minimises an average, and
against an averaged fit loss the two quantities come apart sharply: a kernel can match the *mean*
next-latent law inside a cell while the histories inside that cell disagree violently with each other
and with the mean. `δ_alias` is then the floor that no further training can remove — it is what the
compression has already destroyed — while `δ_fit` is where the model currently sits. The gap between
them is exactly what more optimisation can still buy. That is the operational reading, and it should
be stated, because it converts an inequality into a diagnostic.

[interpretation] The limitation must be stated in the same breath. Both `P_σ(·|h,a)` and `K(·|σ(h),a)`
are pushed through σ on both sides of the comparison. Any distinction σ destroys is therefore
invisible to `δ_alias`, `δ_fit` and `δ_roll` **by construction** — these are self-referential criteria,
and no amount of measuring them can reveal what the representation threw away. The only quantity in
L0 with an external anchor is the query-retention term `η_q`, which requires oracle access to `q(S)`.
This is not a defect to be hidden; it is precisely why L0 is formulated as a frontier over declared
query families rather than as an absolute closure claim, and saying so here makes §3.3 land instead
of arriving unmotivated.

### 3.2 Conditional rollout closure

[proposal] The important word in `δ_roll(k)` is *conditional*, and the draft asserts its importance
without demonstrating it. One sentence fixes this: a model that ignores its starting state entirely
but reproduces the environment's long-run distribution has zero *marginal* rollout error and produces
rollouts that are useless for planning, because every rollout claim is a claim about where you end up
**from here, under this action sequence**. Marginal agreement is compatible with total conditional
disagreement. That is why the comparison is conditioned on the starting history and the action
sequence, and it is worth the sentence.

[proposal] The case-count requirement deserves its own short paragraph rather than a clause. In
finite or episodic systems the admissible conditioning set typically shrinks with horizon. A zero at
large `k` can therefore mean either genuine agreement or simply that the histories on which the model
would have failed have terminated. The count is not bookkeeping; it is the denominator of the claim.
An empty set is `NOT_APPLICABLE`, and a non-empty set with no query-bearing histories is
`NOT_INFORMATIVE`. This distinction is one of the strongest pieces of the profile because it makes a
common evaluation pathology impossible to hide behind a scalar.

### 3.3 Query retention

[proposal] `η_q(k)` is the external-reference term. Its role is to ask whether the latent process
retains enough information to reconstruct a declared property of the underlying state, not merely
whether the latent process is self-consistent. The mandatory `k = 0` term is especially important:
without it a model can appear to preserve a query over future rollouts while being unable to state the
query's value at the current time.

[interpretation] The simplest example is the distinction between predicting a population frequency
and identifying an individual case. A latent can correctly predict that half the next states satisfy a
query while containing no information about whether *this* state satisfies it. Distributional
forecasting and state information are different capabilities. `k = 0` isolates the second.

[proposal] The same shrinking-support semantics must be carried over from rollout error. If the total
admissible set is empty, the query is not applicable; if histories remain but none still carry the
query, the numerical value may be audited but not interpreted as recovered decodability. The draft's
Toy A is valuable precisely because it contains this pattern: failure at `k = 0` and `k = 1`, followed
by a numerical zero at `k = 2` only because the mode-bearing histories have disappeared.

### 3.4 The abstraction frontier

[proposal] This is the strongest profile-level object in the paper, and the draft undersells it. A
single L0 pass is meaningless without the declared abstraction level, because the evaluator can make
the claim trivially true by choosing a query family coarse enough to ignore every failure. The right
object is therefore not a Boolean but a frontier: the finest tested abstraction that passes, together
with a natural richer abstraction that fails when such a comparator is available.

[interpretation] The negative side matters as much as the positive one. A system that passes
`𝔸 = {phase}` and fails `𝔸' = {phase, mode}` tells us what information the representation discarded.
A system reported only at `{phase}` tells us merely that the evaluator chose not to ask about mode.
This is why a frontier-style claim needs a richer tested level or another non-vacuity certificate. It
is not that every pass without a failure witness is false; it is that the *frontier claim* is
incomplete without evidence that the evaluation could have rejected the representation.

### 3.5 Policy exposure inside L0

[proposal] The role of `ρ_pol` is easiest to understand once it is explicitly separated from the
amount of aliasing. `δ_alias` measures how different the merged histories can be. Behaviour policies
determine which histories inside the cell are actually sampled and with what weights. A change in
behaviour can therefore expose more or less of an existing defect, but it cannot create a defect that
is not already present.

The basic convexity relation is
`δ_inv^latent ≤ δ_alias`, hence `ρ_pol ∈ [0,1]` when `δ_alias > 0`.
There is also a sharper mixture-diameter inequality: for two mixture weights `w,w'` over the same
cell,

`d_F(Σ_i w_i P_i, Σ_i w'_i P_i) ≤ ½ ||w-w'||_1 · δ_alias`.

[interpretation] This is elementary but useful because it shows exactly what `ρ_pol` can add. With
two member histories and point-mass laws, the bound is tight and the ratio is just the weight spread;
`ρ_pol` then says nothing about latent geometry. With three or more member laws, the displacement of
the mixture can be strictly smaller than the weight spread times the diameter because the laws may
lie inside one another's convex hull. The ratio then reports something about how the behaviour class
interacts with the geometry of the latent cell, not just how broad the behaviour class is.

[open] The draft is right not to claim novelty for this inequality until a dedicated prior-statement
search has been done. Its value here is diagnostic organisation, not ownership of the convexity fact.

### 3.6 Interventional validity

[proposal] `L1_int` exists to block a common equivocation: observational next-state prediction under
the behaviour distribution is not the same claim as prediction under an intervention. If the action
or variable of interest is confounded with the history that produced it, a conditional predictor can
fit `P(Y|A=a)` perfectly and still be wrong about `P(Y|do(A=a))`.

[interpretation] This layer should be declared only when the system is being asked to support an
interventional claim. If, in the declared setting, intervention coincides with ordinary action
conditioning and no additional causal information is required, the report should say that L1 adds no
independent information there rather than silently upgrading a transition-fit result into a causal
one. `NOT_APPLICABLE` is for settings in which the intervention claim itself is outside scope, not for
settings where the claim collapses to something already measured.

### 3.7 Decision adequacy: global and operational

[proposal] The `L2.G/L2.O` split is the profile's other genuinely useful reporting move. A model can
be accurate on the trajectories its own planner chooses and badly wrong elsewhere. If the planner
uses the model to decide where to look, the evaluation distribution is endogenous: model error can
steer the system away from states or actions that would reveal that same error.

[interpretation] This creates a self-confirming loop. The model undervalues an action; the planner
therefore does not select it; the operational query distribution places negligible mass there; and the
model then receives a low operational error. Nothing in that chain is fraudulent. The problem is only
in reading the resulting `L2.O` pass as a global adequacy statement.

[proposal] `L2.G` therefore asks for adequacy over a declared broader family, while `L2.O` reports the
error under the planner-induced distribution together with a coverage or concentrability diagnostic
against the broader family. A single hand-picked off-prior distribution is not enough if it can be
selected with knowledge of the model's strengths. Either the family itself must be declared or the
coverage coefficient must make the gap visible.

### 3.8 Robustness under shift

[proposal] `L3` is a system-level entry. It should not be interpreted as saying that the internal
world model remains valid after a shift. The system may preserve reward or regret through adaptation,
memory, replanning, redundancy, or another component that compensates for model error.

[interpretation] This distinction matters because successful compensation can hide a broken
component. In engineering terms, system-level robustness is compatible with an unrepaired internal
fault. The profile therefore records L3 at the system level and keeps component-level model validity
as a separate diagnostic question.

---

## §4 Finite separations

### 4.1 Toy A: L0 does not imply L2

[finite] The numerical result is already correct; what is missing is the mechanism. The hidden mode
changes reward but not the projected phase dynamics. L0 is reward-free, so the phase abstraction is
genuinely closed: `δ_alias = δ_fit = 0` is not a fitting accident. The representation has discarded a
distinction that is dynamically irrelevant at the declared abstraction.

[interpretation] That alone would not create regret. If the mode cannot be learned before the
commitment, both actions are worth one half and the coarse representation is optimal. The probe is
the load-bearing part of the construction because it makes the hidden distinction *acquirable* before
the decision. For cost `c < 1/2`, the history-aware policy probes, learns the mode, and commits
correctly; the coarse policy cannot exploit the information because the mode is outside the
representation. The regret is the value of the discarded information net of its price,
`max(0, 1/2 - c)`.

[finite] This is why direct regret is the certificate. Failure of an AIS sufficient-condition bound
would not be enough, because a sufficient condition can fail while the policy remains optimal. The
toy avoids that ambiguity by enumerating policies and showing a positive value gap directly.

### 4.2 Toy B: L2.G does not imply L0

[finite] Again the numbers are correct and the mechanism is missing. The candidate model gets the
next-state law of a nuisance variable `n` wrong, so full-state transition fit fails. But the declared
value-function class ignores `n` entirely. Bellman updates integrate `V` over the next-state law, and
if `V` is constant in `n`, then errors in the `n` marginal vanish from the integral. The model is
therefore value-equivalent on that declared class despite being a bad predictor of the full state.

[interpretation] The limitation should follow immediately: value equivalence is a property of a
model *paired with a declared value class*, not of a model. Enlarge the class until it contains a
function sensitive to `n` and the equivalence dissolves. This is simultaneously the toy's mechanism
and its limitation, and stating both in the same paragraph is more convincing than putting the
limitation in §9 where it reads as a concession.

### 4.3 What ties the two together

[interpretation] The draft reports the two separations as a pair without saying why they are a pair.
The unifying observation is that L0 and L2 quantify over different objects: L0 over a declared query
family, L2 over a declared value-function or policy class. Neither quantification dominates the other,
so a representation can satisfy one and fail the other in either direction. The bidirectionality is
not a coincidence of two clever constructions; it follows from the coordinates being defined over
different index sets. One sentence, and the section acquires a spine.

---

## §5 Manuscript-level diagnostics

### 5.1 The three-history witness

[finite] The draft gives four numbers and no picture. The picture is what makes the point, and it is
simple.

With only two member laws in a latent cell, every mixture over them lies on the segment joining them.
The distance between two mixtures is then forced: it is the weight difference times the diameter of
the cell. The ratio `ρ_pol` therefore recovers nothing except the behaviour-class weight spread, which
is exactly the reviewer objection the section is answering.

With three or more member laws the geometry stops being degenerate, because a member law can sit
*inside the convex hull of the others*. Moving behaviour weight onto such a law barely moves the
mixture, even when the cell's diameter is large. That is the whole content of the two geometries:

- Geometry 1, three mutually distinct point masses: `δ_alias = 2`, mixture distance `1`, so
  `ρ_pol = 0.5` — equal to the weight spread, bound tight, no information beyond ℬ.
- Geometry 2, third law `0.8δ_A + 0.2δ_B` inside the hull: same `δ_alias = 2`, same weight spread
  `0.5`, mixture distance now `0.2`, so `ρ_pol = 0.1` — strictly below the spread.

[proposal] With the sharper bound from §3.5 in hand, this stops being an anecdote and becomes a
statement: `ρ_pol ≤ ½‖w − w'‖₁`, with equality when the mixture displacement is aligned with a
diameter of the cell, and strict inequality when the cell's member laws are in general position.
`ρ_pol` measures the *slack* in that bound, and the slack is geometric. Framed this way §5.1 answers
the reviewer objection cleanly instead of gesturing at two numbers.

### 5.2 The `L2.O` witness

[interpretation] The example is arithmetically fine and reads as rigged, because one sentence is
missing: **`µ_Π` concentrates on the safe action *because* the model is wrong about the other one.**
The planner is not making an arbitrary choice that happens to flatter the model; the query
distribution is a downstream consequence of the very error being measured. Without that sentence a
referee sees a contrived assignment of numbers. With it, the example is a minimal instance of the
closed loop, which is exactly what it is for.

[open] The draft's own caveat — that this is diagnostic and not representative — should be sharpened
into a statement of what a real version would require: a learned model and a search procedure trained
jointly, so that the query distribution is genuinely endogenous rather than stipulated, and an
off-prior family broad enough that the coverage coefficient is not vacuous. Naming the missing
experiment is better than apologising for its absence.

---

## §6 What the profile adds beyond a flat tuple

> **Author's voice — scaffolding only.** The guide reserves this section, and rightly: it is the
> section a hostile referee reads first.

The structural problem with the current version is that it states the eliminativist objection
briefly, lists three advantages flatly, and ends with a shrug. The three moves it should make instead:

**Steelman first.** [interpretation] State the objection at full strength before answering it: every
entry in the profile is *derivable* from `(σ, K, sufficiency class, shift class, resources)`. The
profile adds no information. Naming a bundle of derived numbers does not create a natural kind, and
the history of this literature is not encouraging about labels that outrun their content. A reader
who sees the objection stated this well will extend credit for the answer.

**Then grade the three candidate additions honestly, rather than listing them as equals.**
- The *abstraction frontier* is the strongest, and it is strongest for a specific reason worth
  spelling out: the flat tuple reports a point — one declared level, one set of errors — whereas the
  frontier reports an interval, and the interesting information is at the endpoints. "Passes at
  phase, fails at phase+mode" is not derivable from a single-level report; it requires having tested
  a second level and said so.
- *Bidirectional non-implication* is real but weak. It establishes that two coordinates are distinct,
  which the flat tuple also shows. Its value is defensive: it forecloses the reading that L0 and L2
  are two names for one condition.
- The *L2.G/L2.O split* is the most useful in practice, but it is a methodological point about
  evaluating model–search pairs. It would survive intact if the phrase "world model" were abandoned
  tomorrow. Say so.

**Then name the evidence that would settle it.** [open] The section currently ends without a
falsifier, which is out of character for the rest of the paper. Two concrete candidates: a case where
the profile's cross-layer localisation *predicts* a failure that a single-level report does not, or a
case where it changes an experimental design — which ablation gets run, which shift class gets
declared. Absent either, the section should say that the eliminativist option remains the default and
the burden is on the profile. That is a stronger position to occupy than a defended draw.

---

## §7 Implications for MMALS

> **Author's voice — scaffolding only.**

[interpretation] The structural risk is that in a general arXiv paper this section reads as motivated
reasoning: a framework proposed in the abstract and then discovered, conveniently, to be exactly what
one's own programme needs. Two coherent options, and the draft should pick one rather than hedge:

1. **Cut to a short future-work paragraph.** The profile stands on its own; MMALS becomes one
   sentence about where the question came from.
2. **Make it the driving question and move it forward.** The closing question — *which distinctions
   between histories may an adaptive learner safely quotient away, and which must be preserved
   because they can become relevant under future actions, evidence channels, tasks or regime shifts?*
   — is the best sentence in the paper. It is sharper than the definitional question the paper opens
   with, and it is the sentence a reader will remember.

Option 2 is the better paper, and it also resolves §1: the paper would then be about history
compression under regime change, with the profile as the instrument, rather than about the definition
of "world model" with MMALS appended. The `𝔸_t → 𝔸_{t+1}` problem is genuinely open and genuinely
interesting; it is currently buried on page 9.

---

## §§8–10 Process, limitations, conclusion

[interpretation] §8 is unusual and should be kept — a paper that reports that one of its own results
was initially supported by a non-evidential script, and that the script was replaced, is doing
something most papers do not. Keep it short and factual; the temptation to editorialise about process
quality should be resisted, since the facts make the point better than the commentary does.

The AI-assistance disclosure is well judged, in particular the explicit statement that AI-assisted
review is not human peer review. The rewrite guide flags whether it belongs in the paper or only in
repository metadata; the paper is the right place, because the alternative invites the inference that
it was placed where fewer people would read it.

[interpretation] §9's limitation list is honest and complete. One addition: the limitation identified
in §3.1 above — that `δ_alias`, `δ_fit` and `δ_roll` are self-referential and cannot detect what σ
destroyed — belongs there explicitly, since it is a structural property of the L0 coordinate and not
merely a property of the toys.

§10 should not restate §6. It should close on the research question from §7, which is where the work
is actually going.

---

## Three things to fix while rewriting

1. **The sharper `ρ_pol` bound** (§3.5). `ρ_pol ≤ ½‖w − w'‖₁` converts §5.1 from an illustration into
   a proposition and makes the demotion of behaviour-policy invariance self-evident. Both geometries
   in the draft satisfy it — geometry 1 tight at 0.5, geometry 2 slack at 0.1. Subject to the
   prior-statement search the guide already mandates.

2. **The missing sentence in §5.2.** State that `µ_Π` is induced by the model's own error. Without it
   the example reads as rigged rather than minimal.

3. **Two references I cannot vouch for.** Chen et al., *A Definition and Roadmap for World Models*
   (arXiv:2607.06401), and Cifuentes (arXiv:2602.03146) both postdate what I can verify, so they are
   outside the provenance check I ran on the rest of the bibliography. Two specific risks worth a
   careful look: the Cifuentes title is one word away from the retitled arXiv version of Richens,
   Abel, Bellot and Everitt — the PMLR record is *General agents need world models* with three
   authors, while the arXiv version is *General agents contain world models* with four — so confirm
   they are genuinely distinct works and that entries [21] and [22] are not two views of one paper.
   Everything else in the bibliography was checked against primary sources in the previous cycle.
