# Independent Review Handoff — v0.4 Framework Spine

## Requested disposition

Return one:

- `ACCEPT AS FRAMEWORK SPINE`
- `PARTIAL ACCEPT / REQUEST CHANGES`
- `REJECT FRAMEWORK SPINE`

The four requested v0.3 repairs are the acceptance target.

## Start here

1. `12_LAYERED_PROFILE_V0_4_NOTE.pdf`
2. `01_LAYERED_PROFILE_V0_4_FORMAL_SPEC.md`
3. `06_AUTHOR_RESPONSE_TO_V0_3_REVIEW.md`
4. run `python 03_verify_v0_4.py`
5. compare with `04_RESULTS_V0_4.json`
6. parent review: `14_INDEPENDENT_REVIEW_V0_3_SPINE.md`
7. parent independent code: `15_reviewer_check_v0_3.py`

## A. Structural repair

Falsify:

\[
0\le\delta_{\rm inv}^{latent}\le\delta_{\rm alias}.
\]

Check that `rho_pol` is used only as an L0 attribution ratio, never as an independent axis.

Check the declared convention when delta_alias = 0 (`NOT_APPLICABLE`).

## B. Witness

Independently reproduce:

- delta_alias = 2;
- restricted B {0.25,0.75}: delta_inv = 1, rho_pol = 0.5;
- rich B {0,1}: delta_inv = 2, rho_pol = 1.

Ask whether this diagnostic adds useful attribution or merely redundant notation.

## C. Shrinking support

Inspect `eta_q_mode_if_added`.

Expected:

- k=0: FAIL, error 1, query-bearing count 2;
- k=1: FAIL, error 1, query-bearing count 4;
- k=2: NOT_INFORMATIVE, raw error 0, query-bearing count 0;
- k=3: NOT_APPLICABLE, empty case set.

No horizon-indexed metric may return a silent perfect zero for an empty set.

## D. Scope

The document must claim only finite non-identity of L0 and L2.

It must not claim non-collinearity in a non-degenerate regime.

## E. Citation hygiene

Inspect the `.tex`:

- point-of-use citations must exist;
- no bibliography item used substantively should be left disconnected;
- PMLR and retitled arXiv Richens records must not be conflated.

## F. Eliminativist test

Does the abstraction frontier plus attribution diagnostic now justify keeping the profile as a manuscript spine, while the text still honestly admits the evidence is thin?

If not, reject the framework rather than requesting cosmetic changes.
