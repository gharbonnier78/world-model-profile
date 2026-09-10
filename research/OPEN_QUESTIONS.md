# Open Questions and Manuscript Obligations

These items do **not** modify the accepted v0.4 spine.

## 1. Prior-art check for the policy-exposure bound

The review established, by convexity of the IPM mixture geometry,

`delta_inv^latent <= delta_alias`.

Before presenting this as an original observation, search the relevant literature on mixture diameters, probability metrics, state aggregation, soft aggregation, and policy-dependent aggregation. Until that search is complete, treat the inequality as an elementary derived observation rather than a novelty claim.

## 2. Three-history `rho_pol` witness

The current two-history witness is degenerate in an important sense: `rho_pol` largely reduces to the spread of the behaviour-policy weights. Add a three-or-more-history witness where the same or similar behaviour-weight spread exposes different fractions of aliasing depending on the geometry of the member transition laws.

Purpose: demonstrate the diagnostic value of `rho_pol`, not create a new profile axis.

## 3. Operational L2.O witness

Construct a clean example where model error is low on the planner-induced query distribution but larger off prior, so an apparently adequate model+search pair is revealed as globally inadequate by declared off-prior coverage or concentrability analysis.

## 4. L1_int or L3 witness

If a clean example can be produced without artificial complexity, add at least one finite or controlled demonstration of either:

- interventionally invalid abstraction despite observational/predictive adequacy; or
- system-level robustness under an explicitly declared shift class.

Do not populate every coordinate merely for symmetry.

## 5. Eliminativist comparison

The strongest current positive case for retaining `WMProfile` over a flat tuple is the **abstraction frontier**: reporting the richest tested abstraction that passes and a natural richer one that fails.

The manuscript should explicitly ask whether this organisation materially improves explanation, comparison, or falsification over reporting `(sigma, K, sufficiency class, shift class, ...)` directly.

## 6. Adaptive abstraction and MMALS

The accepted profile assumes a declared abstraction family `A`. A separate future question is whether an adaptive learner should revise it over time:

`A_t -> A_{t+1}`.

This is a candidate bridge to MMALS regime logic such as REUSE → ADAPT → FORK → NEW REGIME. It remains outside the accepted v0.4 definition.
