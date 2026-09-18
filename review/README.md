# Independent Review Gate — v0.9 closed by v0.9.1 repairs

The independent repo-wide review of the pinned v0.9 scientific target is preserved as:

- [`INDEPENDENT_REVIEW_V0_9_CLAUDE.md`](INDEPENDENT_REVIEW_V0_9_CLAUDE.md)

The reviewer handoff remains preserved for auditability:

- [`CLAUDE_FULL_REVIEW_HANDOFF_V0_9.md`](CLAUDE_FULL_REVIEW_HANDOFF_V0_9.md)

The author response / closure map is:

- [`RESPONSE_TO_INDEPENDENT_REVIEW_V0_9.md`](RESPONSE_TO_INDEPENDENT_REVIEW_V0_9.md)

## Review dispositions

- manuscript / evidence: **`ACCEPT WITH CHANGES`**
- Chronicle / trajectory: **`COHERENT WITH DRIFT RISK — REPAIR BEFORE NEXT STUDY`**
- recommendation: stop the mechanical Toy C chain, repair v0.9, then run the pre-registered decision-relevance test.

## Pinned reviewed target

- v0.9 scientific package commit: `c209b7adbbee3444319cb775c99ce572f301d37e`
- v0.9 build Run 2: `35244488222` — success
- v0.9 PDF SHA-256: `979b06b11af033e5523cd95e6908f48581b52c545b0b5a332919e719d5033dd3`
- v0.9 TeX SHA-256: `7ea5b0f41374722e73591fd777436749c594d70ed704ae654e49ceaf076be691`

v0.9 remains immutable as the reviewed snapshot.

## Repair closure: v0.9.1

The repairs-only package is under `paper/world_model_profile_research_v0_9_1/`.

Build run: `35302749759` — **success**.

Checksums:
- v0.9.1 TeX: `901ad01adb74915aff8b223be52c61374d7d01760a45be855cb28f619eda943f`
- v0.9.1 PDF: `5c28530580928eb092f3d1f732fff4ec7b3d47786a34800397ea2ca35961d5ef`

Review blockers are closed as follows:

1. **Delegated F branch path** — independently exercised; with O: `2336/2336` exact, without O: `0/2336` defined. H/G are `NOT_IMPLEMENTED`, not scored failures.
2. **Prior art** — PSR, Dyna, and classical prediction/filtering references added at point of use.
3. **“Falsifying” wording** — replaced by “weakening” / project-authored candidate-criterion framing.
4. **H5 chronology** — explicitly recorded as formulated at v0.4, not pre-registered.
5. **Deferred v0.3 gate** — recorded in the Chronicle addendum and restored as the next research target.

Key non-blocking findings were also reconciled: `4088/292=14` is identified as benchmark arithmetic, `E` is mapped back to existing `D` declarations, H is read as `K` without `U`, and the MMALS `CANDIDATE NEW REGIME -> VERIFY` wording is restored.

## Next research gate

**Do not open Toy C v0.5 or a regime-change toy yet.**

Next: **Decision-Relevance Test v0.1**.

Question:

> Does capability-contract metadata change a concrete engineering evaluation or decision beyond what the flat technical description already determines?

Stop condition:

> If it changes no decision-relevant outcome beyond the flat description, the eliminativist alternative is strengthened and the mechanical Toy C chain stops.
