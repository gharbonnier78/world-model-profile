# Independent Review — Layered World-Model Profile, v0.4 Framework Spine

| Field | Value |
| --- | --- |
| Reviewed package | `world_model_v0_4_REVIEWER_FULL_PACKAGE.zip` |
| Announced SHA-256 | `8d1536436e7b8bc2fb29d59da38a8acfbafa2ac9813e9879274e07df87b8a3c1` |
| SHA-256 as received | **matches exactly** |
| Review date | 2026-09-08 |
| Parent | v0.3 `PARTIAL ACCEPT / REQUEST CHANGES`, four repairs requested |
| **Disposition** | **`ACCEPT AS FRAMEWORK SPINE`** |

The spine is coherent, its claim is now proportionate to its evidence, and the structural defect identified in v0.3 is repaired correctly rather than papered over. Two non-blocking observations are recorded in §4; neither justifies withholding acceptance, and neither should be treated as a further spine change.

---

## 1. Verification log

**Integrity.** ZIP SHA-256 matches the announced value. 22 files. All 21 entries in `SHA256SUMS.txt` verify `OK`, 0 failures.

**Provenance.** `14_INDEPENDENT_REVIEW_V0_3_SPINE.md` and `15_reviewer_check_v0_3.py` are carried **byte-identical** into the package. The parent review has not been edited to fit the response.

**Reproduction.** `03_verify_v0_4.py` re-run in a clean directory, 13 s, exit 0. `04_RESULTS_V0_4.json` and `04_TOY_A_GRID_V0_4.csv` regenerate **byte-identical** to the shipped artifacts.

**Toys unchanged.** Independently re-derived quantities are identical to v0.3 and to my own separate implementation: Toy A `δ_alias = δ_fit = 0`, `η_q_mode(0) = 1`, `V_hist(0.10) = 0.9`, `V_coarse(0.10) = 0.5`, regret `0.40`, 61-point grid matching `max(0, ½−c)` with zero mismatches; Toy B `δ_fit = 1.5`, x-marginal error `0`, max Bellman gap `0` over 256 policies.

**PDF preflight.** 5 pages, unencrypted, openable, not scanned, no XFA.

## 2. The four requested repairs

### R1 — `ρ_pol` demoted to an L0 attribution ratio: **satisfied**

The profile now reads `⟨L0[ρ_pol], L1_int, L2.G, L2.O, L3⟩`. The text states in the body that behaviour-policy exposure is no longer a separate axis and gives the reason. The declaration tuple assigns only `I` to `L1_int`. The results JSON carries the bound `0 ≤ δ_inv^latent ≤ δ_alias` and the convention that `ρ_pol` is undefined when `δ_alias = 0`.

**Handoff item A — the bound survives falsification attempts.** Independently re-derived: it follows from convexity of the IPM in the mixing weights, with the supremum attained at simplex vertices. My v0.3 stress test (20,000 random cells) found 0 violations and exact equality under a vertex-containing behaviour class.

**Handoff item B — witness independently reproduced.** `δ_alias = 2.0`; restricted `B = {(0.25,0.75),(0.75,0.25)}` gives `δ_inv = 1.0`, `ρ_pol = 0.5`; rich `B = {(0,1),(1,0)}` gives `δ_inv = 2.0`, `ρ_pol = 1.0`. Exact match.

### R2 — shrinking-support semantics: **satisfied, precisely**

Every horizon-indexed budget now carries `case_count`, and query budgets additionally carry `query_bearing_case_count`. Verified in the regenerated JSON:

| k | `η_q_mode` raw | cases | query-bearing | status |
| --- | --- | --- | --- | --- |
| 0 | 1.0 | 3 | 2 | `FAIL` |
| 1 | 1.0 | 7 | 4 | `FAIL` |
| 2 | 0.0 | 2 | **0** | `NOT_INFORMATIVE` |
| 3 | `None` | 0 | 0 | `NOT_APPLICABLE` |

`δ_roll(3)` likewise returns `None` / `NOT_APPLICABLE` on the empty case set. No horizon-indexed metric returns a silent zero. The k = 2 entry carries an explicit interpretation string warning against reading the zero as recovered decodability, and the `frontier_statement` states that k ≥ 2 is not used to infer recovery. This is exactly the requested repair.

### R3 — claim scoping: **satisfied**

The abstract and the `scope` key now assert only `L0 ⇏ L2` and `L2.G ⇏ L0` in finite constructions, and explicitly disclaim non-collinearity in a non-degenerate regime, novelty of the abstraction phenomena, and necessity/sufficiency of L0–L3.

### R4 — citation hygiene: **satisfied**

All 13 bibliography entries now carry point-of-use `\cite`, verified key by key. Spot-checked anchors are appropriate: state abstraction at the prior-work boundary, AIS and VE/PVE/AVE in §L2, MuZero at the L2.G/L2.O split, causal abstraction at the interventional guard, Richens–Everitt at L3.

**Handoff item E — the Richens records are not conflated.** `richens2024` is the ICLR causal-world-models paper; `richens2025` is the ICML/PMLR record with the PMLR title, authors and page range. The v0.1-cycle ERR-02 defect does not recur.

**Also fixed.** The ambiguous certification string now reads that L2 failure is certified directly by positive regret rather than inferred from failure of an AIS sufficient-condition bound. AP1 failing as well is no longer implicitly denied.

## 3. Handoff item F — the eliminativist test

The profile is accepted as a manuscript spine, not as a defeat of the eliminativist alternative, which the package correctly declines to claim.

What the profile organises that the flat tuple does not remains the **abstraction frontier** — the ordered pair (finest `A` that passes, natural richer `A` that fails) — now joined by `ρ_pol` as an attribution ratio *within* L0. Both are profile-level objects with no natural slot in `(σ, K, sufficiency class, shift class)`. The evidence is thin and the document says so. That combination — a small live claim plus an honest statement of its size — is what a spine gate is for.

## 4. Non-blocking observations for the manuscript

### O-1 — the supplied `ρ_pol` witness is the one case where the diagnostic cannot demonstrate its own value

With two member histories carrying point-mass laws, `d(mix(w), mix(w')) = |w₁ − w'₁| · δ_alias` exactly, so `ρ_pol` reduces to the spread of the declared weight set and is **independent of the laws**. Measured over random instances (mean absolute deviation of `ρ_pol` from `spread(W)`):

| member histories | deviation |
| --- | --- |
| 2 | 7 × 10⁻¹⁵ |
| 3 | 0.60 |
| 4 | 0.67 |

So the diagnostic does carry genuine information about the mixture geometry once m ≥ 3 — but the only witness shipped is m = 2, where it reports a property of `B` rather than of `σ`. Handoff item B asks whether `ρ_pol` adds attribution or is redundant notation; the honest answer is that it adds attribution, and that the current witness cannot show it. A three-history witness is cheap and would close this.

### O-2 — three of five profile entries still have no finite witness

`L1_int`, `L2.O` and `L3` are well-posed but uninstantiated. The document records this for `L1_int` in the interventional section. `L2.O` in particular is the entry motivated by the MuZero result, and the off-prior/concentrability repair remains untested by any toy. Appropriate at spine stage; it becomes a manuscript obligation.

## 5. Standing note

The v0.3 review's §2 proposition was proved analytically and stress-tested numerically, but has not been checked against the literature for prior statement. The manuscript should perform that check before presenting the bound as its own observation.

## 6. Reviewer disclosure

AI-assisted, single session. The package was checksum-verified, the executable re-run from a clean directory, and the witness plus both toys re-derived by an independent implementation. Every quantity reported above was recomputed, not read from the author's artifacts.
