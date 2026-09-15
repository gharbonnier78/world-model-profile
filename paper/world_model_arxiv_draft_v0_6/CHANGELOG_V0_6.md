# Changelog — Authoring Revision 0.6

## Scope

One non-blocking maintenance correction only. The scientific spine, manuscript text, PDF, Table 2, and published numerical results are unchanged.

## Correction

`verify_finite_separations.py` already failed loudly if the specialised `eta_query` minimax solver encountered a non-deterministic latent rollout. The solver documentation also assumes a binary query, but Revision 0.5 did not enforce that second domain assumption.

Immediately before reading the Bernoulli target mass with:

```python
q0 = truth.get(0, 0.0)
```

Revision 0.6 now checks:

```python
if set(truth) - {0, 1}:
    raise RuntimeError("exact binary-head solver assumes a binary query")
```

This prevents a future multi-valued mode query from being silently projected onto the probability of class `0` and producing a spuriously low minimax error.

## Verification

A targeted smoke test injects a synthetic third mode-bearing history with query value `2` and confirms that the new guard raises exactly:

`exact binary-head solver assumes a binary query`

The normal binary Toy A environment remains unchanged.

The regenerated artifacts are byte-identical to Revision 0.5:

- `finite_separation_results.json`
- `toy_a_grid.csv`
- `supporting_diagnostics_results.json`

The LaTeX source and PDF are also byte-identical to Revision 0.5; only their package filenames carry the local authoring revision number.
