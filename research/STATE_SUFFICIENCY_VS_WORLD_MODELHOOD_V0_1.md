# State Sufficiency vs World-Modelhood — Research Note v0.1

**Status:** exploratory research note.  
**Relationship to the accepted framework:** this note does **not** modify or reopen the frozen v0.4 framework spine.  
**Purpose:** isolate the next question revealed by the v0.6 milestone: when, if ever, does a sufficient representation of history become an internal model of the world?

---

## 1. Genesis of the question

The original line of inquiry did not begin with a proposed definition of *world model*. It began with a simpler state-estimation question:

\[
h_t=(o_{\le t},a_{<t}),\qquad z_t=\sigma(h_t).
\]

If the current internal state \(z_t\) preserves everything relevant for prediction or decision, why retain the full history?

POMDP theory gives an important reference case. Under the standard model assumptions, the belief state

\[
b_t=P(S_t\mid h_t)
\]

can serve as a sufficient information state for control. This immediately raises the distinction that motivates the present note:

> a sufficient state representation is not obviously identical to a world model.

The accepted v0.4 framework then separated predictive closure (L0), interventional validity (L1_int), decision-relative adequacy (L2.G/L2.O), and robustness under shift (L3). The finite Toy A and Toy B constructions established only scoped non-identity between L0 and L2. They did not answer what additional structure, if any, turns a sufficient state into a *model*.

---

## 2. Literature anchors: the term already spans different objects

The literature does not appear to support one single operational object under the phrase *world model*.

### 2.1 Learned environment dynamics

Sutton's Dyna line explicitly learns a model of the effects of actions on the world and uses it for planning. This suggests a model is not merely the current state estimate: it contains a transition-generating mechanism that can be used away from the current real trajectory.

- Sutton, **Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming** (1990).
- Sutton, **Dyna, an integrated architecture for learning, planning, and reacting** (1991).

### 2.2 Compressed generative latent dynamics

Ha & Schmidhuber's *World Models* learns a compressed spatial and temporal representation of an environment and can generate imagined trajectories in which a controller is trained.

- Ha & Schmidhuber, **World Models** (2018), arXiv:1803.10122.

PlaNet and Dreamer continue this line: encode observations into a compact latent state, learn action-conditioned latent dynamics, and use those dynamics for planning or imagined behaviour learning.

- Hafner et al., **Learning Latent Dynamics for Planning from Pixels** (2019).
- Hafner et al., **Dream to Control: Learning Behaviors by Latent Imagination** (2020).
- Hafner et al., **Mastering diverse control tasks through world models** (Nature, 2025).

DreamerV3 is especially explicit: the world model encodes sensory inputs and predicts future representations and rewards for possible actions.

### 2.3 Planning-sufficient rather than reconstruction-complete models

MuZero is a key counterweight to the idea that a world model must reconstruct the world. It learns an iterable model that predicts quantities relevant to planning — reward, policy, and value — without needing to reproduce the observed environment state exactly.

- Schrittwieser et al., **Mastering Atari, Go, chess and shogi by planning with a learned model** (Nature, 2020).

Value-equivalence theory pushes this further: a model may deliberately ignore aspects of the environment and still be sufficient for planning if the relevant Bellman computations are preserved.

- Grimm et al., **The Value Equivalence Principle for Model-Based Reinforcement Learning** (2020).
- Grimm et al., **Proper Value Equivalence** (2021).

This directly supports the v0.4 decision to keep predictive and decision-relative adequacy separate.

### 2.4 Predictive state without latent ontological state

Predictive State Representations show that a dynamical system can be represented through action-conditional predictions of future observations rather than a posterior over hidden physical states.

- Littman, Sutton & Singh, **Predictive Representations of State** (2001).

Therefore a world-model candidate should probably not be defined by the requirement that it recover a privileged hidden physical state \(S_t\).

### 2.5 Information state and recursive sufficiency

The information-state literature gives a particularly sharp comparison. Subramanian et al. define an information state as a function of history sufficient for expected reward and prediction and, equivalently, recursively updateable while sufficient for reward and next-observation prediction.

- Subramanian et al., **Approximate information state for approximate planning and reinforcement learning in partially observed systems** (2020/2022).

This is extremely close to what one might be tempted to call a minimal world-model core — but whether the two concepts should be identified is exactly the question to test rather than assume.

### 2.6 Explicit architecture-level separation of state estimation and world model

LeCun's 2022 position paper provides a useful architectural contrast: the perception module estimates the current state of the world, while the world-model module predicts possible future world states as a function of imagined action sequences.

- LeCun, **A Path Towards Autonomous Machine Intelligence** (2022).

This suggests a clean conceptual separation:

\[
\text{current-state estimate}\neq\text{future-generating world model}.
\]

---

## 3. Four objects that should not yet be collapsed

For the next research cycle, keep four objects distinct.

### A. History statistic / representation

\[
z_t=\sigma(h_t).
\]

It is simply a function of history. No sufficiency or dynamics is implied.

### B. Information state / sufficient state

A representation is sufficient relative to declared queries, rewards, or decisions if the discarded history no longer changes the corresponding conditional quantities beyond a declared tolerance.

This is already relative to a task or query family.

### C. Recursive state

There exists an update mechanism such as

\[
z_{t+1}=U(z_t,a_t,o_{t+1})
\]

or a stochastic counterpart, so the state need not be recomputed from the entire history.

Recursive updateability is stronger than static sufficiency but still may not amount to world-modelhood.

### D. Generative / predictive model structure

There exists an action-indexed predictive operator such as

\[
K(\cdot\mid z_t,a_t)
\]

that can be iterated to answer declared future queries under candidate action sequences.

This operator may predict latent states, observations, rewards, values, or other declared quantities. It need not reconstruct every physical detail of the environment.

---

## 4. The decisive edge cases

### Edge case 1 — oracle belief without model

Suppose an oracle supplies the exact belief

\[
b_t=P(S_t\mid h_t)
\]

at every time step, but the agent is not given the transition law, observation law, filtering update, or any generative operator.

The agent has an excellent current epistemic state. Does it possess a world model?

**Current intuition:** probably not. The belief is the *runtime state of inference*; the model is the structure that says how worlds evolve and how evidence updates that state.

This intuition must be challenged, not promoted to definition by fiat.

### Edge case 2 — perfect finite lookup predictor

A finite lookup table maps every encountered history-action pair to the exact next observation distribution. It has perfect empirical one-step prediction on its finite support but no compositional or portable structure.

Does exact L0 closure on that support imply world-modelhood?

If yes, world-modelhood may be a purely behavioural/evaluative concept. If no, we need to state what extra property is missing without smuggling in subjective notions such as "understanding".

### Edge case 3 — decision-perfect but globally wrong model

Toy B already approximates this case: a model may preserve every computation needed for a declared decision class while being predictively wrong outside it.

If such a model is still legitimately called a world model, then world models need not approximate the world globally. If it is not, we need a principled breadth criterion.

### Edge case 4 — predictive state with no latent ontology

A predictive-state representation may recursively encode exactly the action-conditional predictions needed to characterize the system while never representing a posterior over a hidden physical state.

If this qualifies, then "world model" cannot require recovery of an ontological latent state.

---

## 5. Candidate hypotheses for falsification

These are **not definitions**.

### H1 — Sufficiency alone is insufficient

A static sufficient statistic of history is not enough for world-modelhood.

Potential falsifier: a compelling accepted use of *world model* in which no internal transition/predictive structure exists beyond the current sufficient statistic.

### H2 — Recursive closure may be necessary but not sufficient

A model-like representation should support recursive update or prediction without replaying the full history.

Potential falsifier: a legitimate model architecture that recomputes from full history each time yet is uncontroversially a world model.

### H3 — Modelhood is tied to action-indexed future consequences

A stronger candidate core is:

> a recursively usable internal representation together with an action-conditioned operator that supports declared future predictions or queries.

This remains weaker than interventional validity: ordinary action conditioning belongs to L0; causal/interventional claims remain L1_int.

### H4 — Breadth is a profile property, not a binary threshold

The difference between a narrow task model and a broad world model may be better represented through the abstraction/query frontier than through an arbitrary binary predicate.

This would support retaining the profile approach and also keeps the eliminativist option alive.

---

## 6. Candidate minimal formal object

A provisional *weak modelhood* object could be written

\[
\mathcal M=(\sigma,U,K,\mathcal Q),
\]

where:

- \(\sigma\) maps history to internal state;
- \(U\) recursively updates the state when new evidence arrives;
- \(K\) predicts future internal/query-relevant quantities under candidate actions;
- \(\mathcal Q\) declares what future quantities the model is required to preserve.

A possible test is then whether, for declared horizon \(k\),

\[
P(Q_{t+k}\mid h_t,a_{t:t+k-1})
\approx
P_{\mathcal M}(Q_{t+k}\mid z_t,a_{t:t+k-1})
\]

for \(Q\in\mathcal Q\), while remaining recursively realizable.

This expression is deliberately **action-conditioned**, not automatically causal. Interventional validity remains a separate question.

The important open issue is whether this object is anything more than L0 written operationally. If it is not, then the new research direction may strengthen the eliminativist conclusion rather than define a new world-model predicate.

---

## 7. Proposed Toy C — state without model / model without ontology

The next controlled construction should not merely create another L0/L2 separation. It should attack the present question directly.

Construct the smallest partially observed process admitting the following systems:

1. **Oracle-State Agent:** receives the exact sufficient belief/state at each step but has no internal transition model and cannot roll it forward under candidate actions.
2. **Recursive Predictive Agent:** receives/computes a compact predictive state and owns an action-conditioned update/prediction operator, but never reconstructs the hidden physical state.
3. **Full Generative Agent:** maintains a conventional latent-state transition/observation model and belief update.

Then compare them under identical declared queries:

- current-state estimation;
- one-step prediction;
- multi-step action-conditioned rollout;
- unseen action-sequence composition;
- decision support;
- intervention test where identifiable;
- regime shift.

The construction should be exact and finite if possible.

The key question is not which system "wins". It is whether any measurable distinction cleanly tracks the intuition that system 1 has a state but not a model, while systems 2 and 3 possess model-like structure for different reasons.

---

## 8. MMALS bridge — information loss under adaptive abstraction

The accepted framework freezes an abstraction family \(\mathbb A\). MMALS raises a harder question:

\[
\mathbb A_t\rightarrow\mathbb A_{t+1}.
\]

Suppose the learner previously compressed histories through \(\sigma_t\), then discovers that a finer distinction is now necessary. If the old quotient discarded that information, the current latent state alone may be unable to reconstruct it.

This suggests a separate conjecture:

> **adaptive quotient refinement requires retained information, external memory, reversible/overcomplete representation, or active reacquisition.**

Toy A already hints at the reacquisition route through a probing action. A later MMALS study could formalize when REUSE → ADAPT is possible from the present state alone and when FORK / NEW REGIME requires either historical memory or new evidence.

This is outside the present note's primary question but may become the strongest bridge from the world-model work back to MMALS.

---

## 9. Immediate research tasks

1. Verify terminology and non-equivalence across POMDP belief states, information states, predictive state representations, Dyna-style learned models, Dreamer-style latent world models, MuZero/value-equivalent models, and JEPA-style predictive world models.
2. Determine whether recursive updateability or counterfactual/action-sequence rollout has previously been proposed as a necessary condition for modelhood.
3. Build Toy C as an exact finite construction before adding another layer or axis to the accepted profile.
4. Try to falsify H1–H4 rather than defend them.
5. Keep the eliminativist alternative explicit: the result may be that `world model` is best treated as a family resemblance term and the profile/tuple is the more precise scientific object.

---

## 10. Current disposition

**DO NOT MODIFY v0.4.**  
**DO NOT CALL THIS A DEFINITION YET.**  
**NEXT EVIDENCE TARGET:** Toy C + literature matrix on state / update / prediction / rollout / planning / intervention / robustness.

The working question is:

> **When does a sufficient representation of history become an actual internal model of the world — and is that transition a real technical boundary or only a naming convention?**
