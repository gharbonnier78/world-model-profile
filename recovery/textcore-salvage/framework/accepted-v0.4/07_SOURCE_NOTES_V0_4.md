# Source and Provenance Notes - v0.4

This file records the literature anchors needed by the revised spine. It is not a substitute for the primary papers; exact theorem statements must be copied from primary sources in the eventual manuscript.

## State abstraction baseline - newly explicit

1. **Givan, Robert; Dean, Thomas; Greig, Matthew (2003).**
   *Equivalence notions and model minimization in Markov decision processes.*
   Artificial Intelligence 147(1-2):163-223.
   DOI: 10.1016/S0004-3702(02)00376-4.
   Relevance: stochastic bisimulation / model minimisation.

2. **Ferns, Norm; Panangaden, Prakash; Precup, Doina (2004).**
   *Metrics for Finite Markov Decision Processes.*
   UAI 2004, pp. 162-169.
   Relevance: bisimulation metrics and value-related bounds.

3. **Li, Lihong; Walsh, Thomas J.; Littman, Michael L. (2006).**
   *Towards a Unified Theory of State Abstraction for MDPs.*
   ISAIM 2006.
   Relevance: hierarchy of state abstractions from model-level to decision/policy-level notions.

v0.4 does not claim L0 invented state abstraction. L0 is positioned as a reward-free predictive/query frontier on a history quotient and must be compared explicitly to this literature.

## Approximate information states / value equivalence

4. **Subramanian, Sinha, Seraj & Mahajan (2022).**
   *Approximate Information State for Approximate Planning and Reinforcement Learning in Partially Observed Systems.*
   JMLR 23(12):1-83.
   Relevance: AIS Definition 7, AP1/AP2, finite-horizon Theorem 9.

5. **Grimm, Barreto, Singh & Silver (2020).**
   *The Value Equivalence Principle for Model-Based Reinforcement Learning.*
   NeurIPS 33.

6. **Grimm et al. (2021).**
   *Proper Value Equivalence.*
   NeurIPS 34:7773-7786.

7. **Grimm, Barreto & Singh (2022).**
   *Approximate Value Equivalence.*
   NeurIPS 35.

AIS and VE are related decision-relative adequacy routes but quantify different objects and are kept distinct.

## Self-predictive representation

8. **Ni et al. (2024).**
   *Bridging State and History Representations: Understanding Self-Predictive RL.*
   ICLR 2024, arXiv:2401.08898.

Relevance: self-predictive / next-latent conditions and abstraction relationships.

## Model + search operational adequacy

9. **He, Moerland, de Vries & Oliehoek (2024).**
   *What Model Does MuZero Learn?*
   ECAI 2024, FAIA vol. 392, pp. 1599-1606.
   DOI: 10.3233/FAIA240666.
   arXiv:2306.00840.

Relevance: model errors outside the policy/search distribution and the rationale for L2.G vs L2.O.

## Causal abstraction

10. **Rubenstein, Weichwald, Bongers, Mooij, Janzing, Grosse-Wentrup & Schölkopf (2017).**
    *Causal Consistency of Structural Equation Models.*
    UAI 2017, paper 11.
    Relevance: exact transformations between causal models / intervention consistency across abstraction levels.

11. **Beckers & Halpern (2019).**
    *Abstracting Causal Models.*
    AAAI 33(01):2678-2685.
    DOI: 10.1609/aaai.v33i01.33012678.

Relevance: increasingly strong notions of abstraction for causal models.

## Robustness and extractability

12. **Richens & Everitt (2024).**
    *Robust Agents Learn Causal World Models.*
    ICLR 2024, arXiv:2402.10877.

Use with scope: the theorem conditions involve robustness to local interventions on all environment variables; the causal model is characterised via extractability, not necessarily explicit internal SCM storage.

13. **Richens, Everitt & Abel (2025).**
    *General agents need world models.*
    ICML 2025, PMLR 267:51659-51687.

Provenance trap: the arXiv version 2506.01622 was retitled *General agents contain world models* and lists Richens, Abel, Bellot, Everitt. Do not mix title/author lists.

## Noisy-TV / reverse separation

Toy B intentionally uses a nuisance-noise construction close to classical Noisy-TV/state-abstraction examples. The phenomenon itself is not claimed novel. Its role is purely to exhibit `L2.G pass / L0 fail` inside the proposed profile.

## Verification policy

For the full arXiv manuscript:

- verify author lists, titles, venue, year, pages, DOI/arXiv identifier;
- verify theorem wording and assumptions from the primary source;
- verify reviewer-supplied references exactly as author-supplied ones;
- keep PMLR and arXiv variants as separate bibliographic records where titles/authors differ.


## v0.4 reviewer-derived mixture bound

The relation

\[
\delta_{\rm inv}^{\rm latent}\le\delta_{\rm alias}
\]

and equality under behaviour classes containing the simplex vertices are included as an elementary consequence of mixture structure plus IPM convexity. **No novelty claim is made.** The v0.3 reviewer explicitly notes that this proposition has not been checked against the literature for prior statement; a full manuscript should conduct that check before presenting it as a named proposition.

## v0.4 citation hygiene

The candidate LaTeX now cites sources at point of use. Bibliographic provenance still follows the prior rule: exact author lists, title, venue, pages, DOI/arXiv identifier and theorem assumptions must be verified from primary sources before arXiv submission.
