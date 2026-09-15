# Mechanical Verification — Authoring Revision 0.6

## Scope

This pass verifies only the final binary-query domain guard requested after the Revision 0.5 ultimate review. It does not reopen the scientific spine or manuscript.

## 1. Binary-query assumption is now enforced

The exact Toy A query-head solver is specialised to deterministic latent rollouts and a binary query.

Revision 0.5 already raised on a non-deterministic latent rollout. Revision 0.6 adds the corresponding explicit binary-query guard:

```python
if set(truth) - {0, 1}:
    raise RuntimeError("exact binary-head solver assumes a binary query")
```

The check occurs immediately before `q0 = truth.get(0, 0.0)`.

## 2. Guard smoke test

A synthetic third mode-bearing history with query value `2` was inserted into an imported copy of the packaged verifier, and `eta_query(0.10, "mode", 0)` was called.

Result:

- guard triggered: `True`;
- exact message: `exact binary-head solver assumes a binary query`.

The packaged source was not mutated by this smoke test.

## 3. Normal regression outputs

Both packaged verification scripts were run from the Revision 0.6 directory after deleting their generated outputs.

All regenerated artifacts are byte-identical to Revision 0.5:

| Artifact | Byte-identical | SHA-256 |
|---|---:|---|
| `finite_separation_results.json` | True | `91f728d0d05252306dc85f92433080a5a51db61c1ef2a24145637f70098acf5a` |
| `toy_a_grid.csv` | True | `0a025671c5c9a974513bfec488647bc222316429a044f22f237a7555e28f7f97` |
| `supporting_diagnostics_results.json` | True | `8dd83f4f2e11526da177b2cd32f4db306b6f8cef4871d71ed4cbcb4fac37c7db` |

## 4. Manuscript regression

- LaTeX body/source byte-identical to Revision 0.5: `True`;
- PDF byte-identical to Revision 0.5: `True`;
- therefore page count, layout, references, Appendix A/Table 2, Appendix B, and all manuscript claims are unchanged.

## 5. Scientific impact

None.

This is a defensive domain guard on an exact solver. It changes no currently reachable calculation because Toy A has `MODES = (0, 1)`.
