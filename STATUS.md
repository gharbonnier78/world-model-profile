# Research Status

**Framework spine:** v0.4 — `ACCEPT AS FRAMEWORK SPINE`  
**Accepted artifact:** `framework/accepted-v0.4/`  
**Published / preserved manuscript milestone:** v0.6 under `paper/world_model_arxiv_draft_v0_6/`  
**Current exploratory cycle:** state sufficiency vs world-modelhood / Toy C  
**Current research draft:** v0.8 under `paper/world_model_profile_research_v0_8/` on the research branch  
**Spine policy:** frozen unless a new formal review cycle is explicitly opened

## Review trajectory

- **v0.1** — working definition; independent review `PARTIALLY ACCEPT`.
- **v0.2** — first layered L0–L3 formalisation and finite separation; `PARTIAL ACCEPT / REQUEST CHANGES`.
- **v0.3** — executable repair, reverse separation, abstraction frontier; `PARTIAL ACCEPT / REQUEST CHANGES`.
- **v0.4** — policy-exposure quantity moved inside L0 as `rho_pol`, support accounting fixed, claims narrowed, citations repaired; **`ACCEPT AS FRAMEWORK SPINE`**.
- **v0.6 manuscript milestone** — preserved as published authoring state; no retroactive Toy C rewrite.
- **v0.7 research draft** — post-v0.6 exploratory extension carrying Toy C v0.1/v0.2 into LaTeX/PDF; preserved as a research snapshot.
- **v0.8 research draft** — extends the falsification cycle through Toy C v0.3 (model possession vs model access / finite compilation); not an accepted framework revision.

## Accepted core

```text
WMProfile_D = < L0[rho_pol], L1_int, L2.G, L2.O, L3 >
```

The components are not claimed to form a hierarchy.

## Exact finite results retained

- `L0 ⇏ L2` in Toy A.
- `L2.G ⇏ L0` in Toy B.

These are finite non-identity results, not a general non-collinearity theorem.

## Post-v0.6 Toy C evidence

Toy C does not add a framework axis. It attacks candidate modelhood boundaries.

- **Toy C v0.1:** exact current belief can be supplied without giving the system an owned future-generating mechanism; the predictive-state and full-generative agents are exactly equivalent on the declared finite queries; finite lookup fit does not imply held-out compositional coverage.
- **Toy C v0.2:** the task predictive state is a genuinely non-injective quotient of a richer full belief. Exact task-query aliasing is `0`, while the richer nuisance-query aliasing gap is exactly `19/129`.
- **Agent E (v0.2):** exact declared action-sequence prediction is possible without a persistently stored recursively updated state, weakening a strong recursive-state necessity hypothesis.
- **Toy C v0.3:** local model possession (M), delegated external model access (F), and a finite compiled answer object (G) are exactly answer-equivalent on all `4088` declared finite queries. On the horizon-4 extension, M and F remain exact on `4672/4672` queries while G has `0/4672` coverage. After external-source removal, M remains exact while F has `0/4088` defined answers. This makes capability provenance and system boundary explicit.

The previous candidate — internally owned future-query mechanism — is therefore weakened as a system-level necessity. The current technical question is better expressed as a capability contract: **which future queries can be answered, over what domain, from what source, inside which declared boundary, and with what behaviour under extension, source removal, intervention and shift?** This is **not** a definition of world model and does not add a new accepted layer.

Chronicle: `history/2026-09-15_toy_c_state_sufficiency_chronicle.md`.
