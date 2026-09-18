# Independent Review Handoff — post-v0.6 research draft v0.9 / Toy C v0.1-v0.4

**Reviewer target:** Claude, acting as an independent adversarial scientific reviewer.  
**Repository:** `gharbonnier78/world-model-profile`  
**Branch:** `research/state-sufficiency-vs-world-modelhood`  
**Review mode:** evidence-first, falsification-oriented, no manuscript rewriting during review.

## Requested dispositions

Return **two separate dispositions** plus one overall recommendation.

### A. Manuscript / evidence disposition

Return one:

- `ACCEPT AS RESEARCH SNAPSHOT`
- `ACCEPT WITH CHANGES`
- `REJECT RESEARCH SNAPSHOT`

### B. Chronicle / trajectory disposition

Return one:

- `COHERENT — CONTINUE`
- `COHERENT WITH DRIFT RISK — REPAIR BEFORE NEXT STUDY`
- `TRAJECTORY DRIFT — REFRAME BEFORE CONTINUING`

### C. Overall next-step recommendation

State whether the project should:

- stop the mechanical Toy C chain here and move to a genuinely changed regime/query/action/observation experiment;
- run one more falsification first;
- or revisit the framing before any new experiment.

Do **not** choose a disposition for politeness. A clear rejection or pause is useful if justified.

---

## Start here — required reading order

1. `STATUS.md`
2. `README.md`
3. accepted frozen spine:
   - `framework/accepted-v0.4/01_LAYERED_PROFILE_V0_4_FORMAL_SPEC.md`
   - `framework/accepted-v0.4/16_INDEPENDENT_REVIEW_V0_4_SPINE_ACCEPTED.md`
4. published/preserved manuscript milestone:
   - `paper/world_model_arxiv_draft_v0_6/world_model_profile_arxiv_draft_v0_6.pdf`
   - `paper/world_model_arxiv_draft_v0_6/CLAIM_EVIDENCE_MAP.md`
   - `paper/world_model_arxiv_draft_v0_6/FINAL_GUARD_REVIEW_HANDOFF_V0_6.md`
5. post-v0.6 research framing:
   - `research/STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md`
   - `research/OPEN_QUESTIONS.md`
6. Toy C exact specifications and evidence, in order:
   - `research/toy_c_v0_1/TOY_C_V0_1_SPEC.md`
   - `research/toy_c_v0_1/verify_toy_c_v0_1.py`
   - `research/toy_c_v0_1/results_v0_1.json`
   - `research/toy_c_v0_2/TOY_C_V0_2_SPEC.md`
   - `research/toy_c_v0_2/verify_toy_c_v0_2.py`
   - `research/toy_c_v0_2/results_v0_2.json`
   - `research/toy_c_v0_3/TOY_C_V0_3_SPEC.md`
   - `research/toy_c_v0_3/verify_toy_c_v0_3.py`
   - `research/toy_c_v0_3/results_v0_3.json`
   - `research/toy_c_v0_4/TOY_C_V0_4_SPEC.md`
   - `research/toy_c_v0_4/verify_toy_c_v0_4.py`
   - `research/toy_c_v0_4/results_v0_4.json`
7. complete Chronicle:
   - `history/2026-09-15_toy_c_state_sufficiency_chronicle.md`
   - `history/2026-09-16_toy_c_v0_4_typed_extension.md`
   - `history/README.md`
8. current integrated manuscript package:
   - `paper/world_model_profile_research_v0_9/world_model_profile_research_v0_9.pdf`
   - `paper/world_model_profile_research_v0_9/world_model_profile_research_v0_9.tex`
   - `paper/world_model_profile_research_v0_9/SHA256SUMS.txt`
   - `paper/world_model_profile_research_v0_9/README.md`

For historical review style, use the repository's earlier handoff as a methodological precedent:

- `recovery/textcore-salvage/framework/accepted-v0.4/08_REVIEW_HANDOFF_V0_4.md`

The accepted v0.4 spine is **frozen**. Do not silently revise it as part of this review. If post-v0.6 evidence exposes a real contradiction with it, identify the contradiction explicitly and recommend opening a separate formal review cycle.

---

## 1. Mechanical / executable verification

Run, independently:

```bash
python research/toy_c_v0_1/verify_toy_c_v0_1.py > /tmp/v01.json
diff -u research/toy_c_v0_1/results_v0_1.json /tmp/v01.json

python research/toy_c_v0_2/verify_toy_c_v0_2.py > /tmp/v02.json
diff -u research/toy_c_v0_2/results_v0_2.json /tmp/v02.json

python research/toy_c_v0_3/verify_toy_c_v0_3.py > /tmp/v03.json
diff -u research/toy_c_v0_3/results_v0_3.json /tmp/v03.json

python research/toy_c_v0_4/verify_toy_c_v0_4.py > /tmp/v04.json
diff -u research/toy_c_v0_4/results_v0_4.json /tmp/v04.json
```

Also inspect the code rather than trusting assertions. Confirm that the results are derived from the explicit finite environment and not merely hard-coded expected outputs.

For Toy C v0.4, independently reproduce or challenge at minimum:

- baseline `D0`: M/F/G/H exact `4088/4088`;
- Agent H seed count: `292`;
- horizon-4/5/6 extension: H exact `32704/32704`, G defined `0/32704`;
- newly conditioned depth-3 histories: H and G defined `0/28672`, M/F exact `28672/28672`;
- branch-conditioned hypothetical-evidence queries: M/F exact `2336/2336`, H/G interface unsupported;
- parity non-regression: `148920/148920` exact checks;
- source removal: delegated F becomes undefined while H remains locally available on its declared interfaces.

Check the arithmetic behind all domain counts rather than merely comparing strings in JSON.

---

## 2. Toy C chain — adversarial scientific review

Reconstruct the chain without using the manuscript's conclusion as your premise:

`v0.1 state vs future-generating structure`
→ `v0.2 non-injective predictive quotient + direct-history Agent E`
→ `v0.3 possession vs delegated access vs finite compilation`
→ `v0.4 typed extension / Agent H`.

For each step answer:

1. What exact candidate hypothesis was being attacked?
2. Does the construction genuinely falsify/weaken that hypothesis, or only exploit a definitional choice?
3. Is the next toy logically motivated by the previous failure, or does the sequence become post-hoc?
4. Is the claimed lesson stronger than what the finite construction establishes?
5. Is the construction scientifically informative despite being deliberately simple, or has it become bookkeeping/triviality by construction?

Pay special attention to the word **falsification**. If a toy is only a counterexample to an informal candidate criterion rather than falsification of a formal theory, require the manuscript/chronicle to say so.

---

## 3. Toy C v0.4 — specific falsification targets

Attempt to reject the following interpretations.

### A. Horizon extension

Does Agent H really demonstrate that long-horizon endpoint generalisation can exist without a full generative/update model, or has the model merely been hidden inside the parity rule / seed construction?

Give a precise answer. Distinguish:

- no declared full generative model;
- possession of a task-specific law;
- possession of a predictive mechanism;
- semantic disagreement over whether that mechanism deserves the word `model`.

The paper must not obtain a result merely by renaming a model as a `query program`.

### B. Typed extension

Does the construction support only the scoped statement

> future-horizon extension, conditioning-history extension, and branch-conditioned evidence assimilation are distinct capabilities in this finite system

or something stronger?

Challenge the exploratory tuple

`E = (horizon, history, query, branch, source, intervention, shift)`.

Ask whether these axes are independent, complete, redundant with the accepted declaration tuple, or simply useful metadata. Do not accept a new taxonomy because it is convenient.

### C. Complexity / compression

Verify that `4088/292 = 14` is used only as entry-count bookkeeping. Reject any language that implies an MDL, Kolmogorov complexity, or formal compression result without accounting for the rule/program description length.

### D. Scope

Confirm that Toy C v0.4 does **not** establish:

- that H is or is not a world model;
- a universal set of extension axes;
- causal/interventional validity beyond the declared action semantics;
- robustness to regime shift;
- superiority of a capability-contract framework;
- a necessary-and-sufficient definition of world model.

---

## 4. Full Chronicle audit — mandatory

This is not a prose-editing task. Review the Chronicle as a scientific audit trail from the original question to v0.4.

Read both Chronicle files completely, then compare them against:

- the accepted v0.4 spine;
- the preserved v0.6 manuscript;
- `research/STATE_SUFFICIENCY_VS_WORLD_MODELHOOD_V0_1.md`;
- `research/OPEN_QUESTIONS.md`;
- every Toy C spec/result/verifier.

Reconstruct the actual genealogy:

1. history compression / sufficient state;
2. belief state as reference case;
3. predictive closure vs decision adequacy in the accepted profile;
4. question: sufficient state vs model structure;
5. failure of persistent-state necessity;
6. failure of local-possession necessity at system boundary;
7. finite behavioural non-identifiability;
8. failure of scalar extension/generalisation as discriminator;
9. emerging capability-contract / typed-extension language;
10. proposed bridge back to adaptive abstraction / MMALS.

Then answer explicitly:

### Chronicle coherence test

- Does every transition follow from evidence actually obtained?
- Are any later concepts retroactively projected onto earlier work?
- Have hypotheses been recorded when they were proposed, or only after a result made them convenient?
- Are failures and abandoned intuitions preserved rather than rewritten as if the current view had always been intended?
- Are finite counterexamples being inflated into general claims?
- Is `world model` gradually being replaced by an engineering qualification contract without the manuscript explicitly acknowledging that change of research object?

### Drift test

The original post-v0.6 question was:

> When does a sufficient representation of history become an actual internal model of the world — and is that transition a real technical boundary or only a naming convention?

Judge whether Toy C v0.1-v0.4 is still answering that question.

If the programme has legitimately discovered that the question itself dissolves into boundary/query/capability declarations, explain the evidential chain that justifies that shift.

If instead the project has drifted from a world-model question into an unrelated qualification taxonomy, identify **the first exact step where the drift occurs**.

Do not accept the MMALS bridge merely because it is thematically attractive.

---

## 5. MMALS bridge — anti-convergence check

The World Model Profile is an autonomous research object. MMALS is a downstream motivation, not evidence for the World Model claims.

Check that the Chronicle/manuscript does not reason circularly:

`MMALS needs adaptive abstraction` → therefore `World Model Profile should become adaptive abstraction`.

The only acceptable bridge is evidence-based:

- Toy C reveals a specific failure mode or qualification axis;
- that failure makes a previously discarded distinction relevant;
- only then may the Chronicle note a possible relation to `A_t -> A_{t+1}` / REUSE → ADAPT → FORK → NEW REGIME.

If possible, cross-check the source MMALS programme note:

`gharbonnier78/mmals/docs/program/MMALS_DYNAMIC_MINIMAL_INFERENCE_PROGRAM_2026-08-24.md`

and determine whether the Chronicle represents it faithfully rather than retrofitting it.

---

## 6. Accepted profile compatibility

The accepted spine remains:

`WMProfile_D = < L0[rho_pol], L1_int, L2.G, L2.O, L3 >`.

Check that post-v0.6 work does not silently create an `L4`, redefine L0, or make model possession / typed extension constitutive.

Ask specifically whether Toy C v0.4 is best understood as:

- declaration metadata around L0/L2 claims;
- an operational testing pattern;
- a genuinely missing coordinate;
- or merely a flat technical description that strengthens the eliminativist alternative.

If you think a new accepted coordinate is warranted, do **not** add it. State the argument and recommend a separate formal review cycle.

---

## 7. Eliminativist test

The repository deliberately keeps the competitor alive:

> retire the binary `world model` predicate and report the technical tuple/capability contract directly.

After Toy C v0.1-v0.4, assess whether the evidence:

- strengthens the profile;
- strengthens the eliminativist alternative;
- or merely shows that the two are different presentation layers over the same information.

Do not protect the term `world model` if it adds no explanatory or experimental value.

Conversely, do not declare eliminativism victorious merely because the term has fuzzy usage. Require an experimentally or explanatorily meaningful argument.

---

## 8. Literature / citation hygiene

Check point-of-use citations in the current `.tex` for claims concerning:

- POMDP/information-state sufficiency;
- Predictive State Representations;
- Dyna / learned environment models;
- Ha & Schmidhuber / PlaNet / Dreamer;
- MuZero and value equivalence;
- self-predictive representations;
- causal abstraction / robust agents;
- recent `world model` definition/roadmap work.

Separate three statuses:

- verified citation;
- plausible but not independently verified;
- unsupported/overstated.

Do not invent references. If web access is unavailable, say which checks remain open.

Also search for nearest prior art to the *interpretation*, not only the equations: finite behavioural equivalence, predictive sufficiency under restricted query families, task-specific sufficient statistics, and different axes of generalisation may all have established terminology. The manuscript should not imply conceptual novelty where it has only constructed a clean finite witness.

---

## 9. Manuscript integration / PDF review

Inspect both `.tex` and rendered PDF.

Check that Toy C v0.4 appears consistently in:

- title/version language;
- abstract;
- contribution summary;
- main Toy C section;
- limitations;
- conclusion;
- finite-results appendix;
- reproducibility boundary.

Check for contradictions between v0.3 and v0.4 language, stale references to v0.8/v0.3 as current, broken table layout, overflow, citation errors, or PDF rendering defects.

Confirm that v0.6 remains described as a frozen historical milestone and that v0.9 is explicitly exploratory.

---

## 10. Required review output

Create a single review document:

`review/INDEPENDENT_REVIEW_V0_9_CLAUDE.md`

Do **not** edit manuscript, Chronicle, specifications, code, or results during the review.

Use this structure:

1. **Dispositions** — manuscript, Chronicle/trajectory, overall next step.
2. **Executive assessment** — max ~500 words.
3. **Mechanical verification** — commands run, exact matches/mismatches, independent count checks.
4. **Claim-by-claim Toy C review** — v0.1, v0.2, v0.3, v0.4.
5. **Toy C v0.4 adversarial findings** — especially Agent H and typed extension.
6. **Full Chronicle audit** — genealogy, omissions, retroactive framing, drift test.
7. **Accepted-spine compatibility**.
8. **MMALS bridge audit**.
9. **Eliminativist comparison**.
10. **Citation/prior-art findings**.
11. **PDF/LaTeX integration findings**.
12. **Blocking findings** — numbered, reproducible, minimum necessary repairs.
13. **Non-blocking findings** — clarity/future-work only.
14. **What should be done next** — one concrete research step, or a justified pause/reframe.

For every substantive criticism, cite the exact file/section/result that supports it. Separate:

- factual defect;
- unsupported claim;
- interpretation disagreement;
- alternative research direction.

Do not turn a preference for a different research programme into a blocking defect.

---

## Review principle

The aim is not to make v0.9 look stronger.

The aim is to decide whether the sequence has **earned** its current narrower conclusion, whether the Chronicle tells that sequence faithfully, and whether continuing from here still answers a scientifically meaningful question.
