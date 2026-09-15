# Final Guard Review Handoff — Authoring Revision 0.6

## Requested scope

Verify one change only.

`verify_finite_separations.py` must fail loudly if the exact query-head solver is ever applied to a non-binary query.

Expected source guard:

```python
if set(truth) - {0, 1}:
    raise RuntimeError("exact binary-head solver assumes a binary query")
```

It must appear before `q0 = truth.get(0, 0.0)`.

## Regression expectation

No scientific or manuscript output may change.

The following must regenerate byte-identically to Revision 0.5:

- `finite_separation_results.json`
- `toy_a_grid.csv`
- `supporting_diagnostics_results.json`

The manuscript `.tex` and `.pdf` are expected to be byte-identical to Revision 0.5.

## Desired disposition

`READY — FINAL MAINTENANCE GUARD CLOSED`

or one concrete reproducible defect in this guard.
