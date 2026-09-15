# Author Response to Independent Review of v0.3 Spine

**Reviewer disposition:** `PARTIAL ACCEPT / REQUEST CHANGES`  
**Revision target:** v0.4 candidate framework spine

## Overall

We accept all four requested changes.

The reviewer independently verified the package, re-ran the executable byte-for-byte, re-derived both toys by a separate code path, and cleared the v0.2 executable blocker. The remaining issue is structural rather than numerical: latent-conditioned behaviour invariance is bounded by L0 aliasing and therefore cannot remain an independent coordinate.

## 1. Demote L1.a to rho_pol — ACCEPTED / DONE

The reviewer proves

\[
\delta_{\rm inv}^{\rm latent}\le\delta_{\rm alias},
\]

with equality when the behaviour class can concentrate on each member history in a latent cell.

v0.4 therefore removes behaviour invariance from the profile axes.

For declared restricted B and delta_alias > 0, it now reports

\[
\rho_{\rm pol}
=
\delta_{\rm inv}^{\rm latent}/\delta_{\rm alias}
\in[0,1]
\]

inside the L0 report.

Interpretation: fraction of existing compression aliasing exposed by changes in the declared behaviour/acquisition class.

L1 is now interventional validity only.

## 2. Add non-vacuous witness — ACCEPTED / DONE

The executable contains a two-history witness:

- delta_alias = 2;
- restricted B gives delta_inv = 1 and rho_pol = 0.5;
- rich B containing simplex vertices gives delta_inv = 2 and rho_pol = 1.

This demonstrates usefulness as an attribution ratio without pretending it is independent of L0.

## 3. Empty-sup / shrinking-support artifact — ACCEPTED / DONE

All horizon-indexed budgets now carry case counts.

- empty case set -> `NOT_APPLICABLE`, never `0`;
- mode-query output additionally carries `query_bearing_case_count`;
- at k=2 Toy A has numerical error 0 but zero mode-bearing starting histories, so status is `NOT_INFORMATIVE`;
- k=3 is `NOT_APPLICABLE`.

The package no longer allows a reader to infer that mode decodability improved with horizon.

## 4. Scope non-identity claim — ACCEPTED / DONE

The spine now says only:

> finite examples establish L0/L2 non-identity.

It explicitly says that non-collinearity in a non-degenerate regime is not established.

The arXiv manuscript gate therefore still includes a future stronger separation if a stronger contribution claim is desired.

## Minor arXiv-blocking hygiene also fixed

- LaTeX now contains point-of-use `\cite{...}` commands;
- all bibliography entries used in argumentation are linked;
- the certification sentence now reads "certified directly by regret rather than inferred from failure of an AIS sufficient-condition bound";
- verification stdout regenerated without the foreign daemon stack trace.

## Claim status

Retained:
- Toy A arithmetic and direct-regret separation;
- Toy B reverse separation;
- abstraction-frontier idea.

Changed:
- L1.a independent coordinate -> withdrawn;
- rho_pol diagnostic -> added;
- long-horizon mode zero -> audit-only / non-informative;
- framework claim -> narrowed.

Still open:
- empirical L1 interventional separation;
- L3 separation;
- non-degenerate L0/L2 separation;
- eliminativist alternative.
