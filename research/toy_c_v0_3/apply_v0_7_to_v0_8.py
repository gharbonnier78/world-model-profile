#!/usr/bin/env python3
"""Transform the checksum-pinned v0.7 research TeX into v0.8 with Toy C v0.3."""

from pathlib import Path
import hashlib

SRC = Path("paper/world_model_profile_research_v0_7/world_model_profile_research_v0_7.tex")
DST_DIR = Path("paper/world_model_profile_research_v0_8")
DST = DST_DIR / "world_model_profile_research_v0_8.tex"
EXPECTED_SRC_SHA256 = "5e03cf0186a95afc7d9c315c9a01620866b149d52dc8d0d08d8eda88b2b0217e"

raw = SRC.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
if sha != EXPECTED_SRC_SHA256:
    raise SystemExit(f"Unexpected v0.7 TeX SHA256: {sha}")

text = raw.decode("utf-8")


def replace_once(old, new, label):
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {n}")
    text = text.replace(old, new, 1)


replace_once(
    r"""\large Post-v0.6 Research Draft with Toy C Extensions}""",
    r"""\large Post-v0.6 Research Draft with Toy C v0.1--v0.3 Extensions}""",
    "title",
)

replace_once(
    r"""Toy C v0.1 separates an oracle-supplied exact belief from owned predictive dynamics; Toy C v0.2 constructs a non-injective one-dimensional predictive quotient that is exact for a declared task-query family while provably insufficient for a richer nuisance query, and adds a direct-history predictor that challenges persistent recursive state storage as a necessary implementation condition. We do not claim""",
    r"""Toy C v0.1 separates an oracle-supplied exact belief from owned predictive dynamics; Toy C v0.2 constructs a non-injective one-dimensional predictive quotient that is exact for a declared task-query family while provably insufficient for a richer nuisance query, and adds a direct-history predictor that challenges persistent recursive state storage as a necessary implementation condition. Toy C v0.3 then separates local model possession from delegated model access and finite compilation: all three can be exactly answer-equivalent on a declared finite query domain, while source removal and query-domain extension expose different capability provenance and coverage. We do not claim""",
    "abstract",
)

replace_once(
    r"""\item In a post-v0.6 falsification cycle, Toy C separates current-state sufficiency from future-query capability, then tests a genuinely information-losing predictive quotient and a direct-history sequence predictor before any new framework layer is considered.""",
    r"""\item In a post-v0.6 falsification cycle, Toy C separates current-state sufficiency from future-query capability, tests a genuinely information-losing predictive quotient and a direct-history sequence predictor, then distinguishes local model possession from delegated access and finite compiled answers before any new framework layer is considered.""",
    "contribution bullet",
)

anchor = r"""\section{Illustrative diagnostics}"""
insert = r"""
\subsection{Toy C v0.3: model possession versus model access}

Toy C v0.3 attacks the strongest implementation-specific candidate left after v0.2: that a model-like system must \emph{internally own} the action-indexed future-query mechanism. The stochastic environment is unchanged. Instead, the location and form of predictive capability are varied.

Declare the finite benchmark
\[
\mathcal D_0
=
\{(h_t,a_{t:t+k-1}):t\le2,\;k\in\{1,2,3\}\},
\]
with query
\[
Q(h_t,a_{t:t+k-1})
=
P(Y_{t+k}=1\mid h_t,a_{t:t+k-1}).
\]
Exact enumeration gives $|\mathcal D_0|=4088$ queries.

Three systems are compared. Agent M owns the task-relevant dynamics inside the declared local boundary and computes the query from history. Agent F owns no local transition, observation, update or rollout mechanism; while an external exact model service O is available, F simply delegates the query to O. Agent G is a finite compiled answer object containing one exact answer for every element of $\mathcal D_0$, with no declared transition, update, composition or extrapolation rule.

On the declared finite domain all three are exactly answer-equivalent:
\[
M=\frac{4088}{4088},
\qquad
F+O=\frac{4088}{4088},
\qquad
G=\frac{4088}{4088}.
\]
Thus finite answer correctness alone cannot identify whether predictive structure is locally possessed, externally accessed, or compiled into a finite query table.

The distinction becomes observable only after changing the qualification contract. On the horizon-four extension domain $\mathcal D_+$, containing 4672 queries, M and F+O remain exact,
\[
M=\frac{4672}{4672},
\qquad
F+O=\frac{4672}{4672},
\]
whereas G has zero coverage,
\[
\mathrm{coverage}(G,\mathcal D_+)=\frac{0}{4672}.
\]
If the external service O is removed, M remains exact on $\mathcal D_0$, F has zero defined answers, and G retains only its finite compiled domain. Source removal therefore distinguishes local possession from delegated access; query extension distinguishes a finite compiled answer object from a mechanism with wider predictive access.

The construction also makes the system boundary explicit. At the local-agent boundary, F has model \emph{access} but not model \emph{possession}. At an expanded boundary containing F+O, the composite system does contain the external predictive mechanism. We therefore treat model-location claims as boundary-relative attribution claims rather than as a new framework layer.

An elementary finite-compilation observation explains why this matters. For any finite declared query set $D$ and deterministic exact map $M:D\to\mathcal Y$, the table
\[
T_M=\{(d,M(d)):d\in D\}
\]
is observationally equivalent to M on $D$. We make no novelty claim for this fact. Its methodological consequence is that finite behavioural agreement cannot by itself establish internal generative structure. Tests of mechanism possession need additional declarations such as extension, dependency removal, architectural inspection, compositional constraints, or robustness.

Toy C v0.3 therefore weakens the strong H3-like candidate that \emph{internal ownership} is necessary for system-level future-query capability. What survives is better expressed as a capability contract: which future queries can be answered, over what domain, from what source, within which declared system boundary, and with what behaviour under extension, source removal, intervention and shift.

\section{Illustrative diagnostics}"""
replace_once(anchor, insert, "Toy C v0.3 insertion")

replace_once(
    r"""Toy C v0.2 in particular makes query breadth observable through an exact zero-versus-positive aliasing frontier and weakens a strong recursive-state necessity hypothesis before it can harden into a definition.""",
    r"""Toy C v0.2 in particular makes query breadth observable through an exact zero-versus-positive aliasing frontier and weakens a strong recursive-state necessity hypothesis before it can harden into a definition. Toy C v0.3 further shows that local possession, delegated access and finite compiled answers can be indistinguishable on a declared finite query domain, so model-location claims require an explicit system boundary and capability source.""",
    "conclusion",
)

replace_once(
    r"""Toy C v0.2 & lookup D held-out coverage & $0/512$ \\""",
    r"""Toy C v0.2 & lookup D held-out coverage & $0/512$ \\
Toy C v0.3 & M/F/G exact on declared $D_0$ & $4088/4088$ each \\
Toy C v0.3 & M/F exact on horizon-4 extension & $4672/4672$ each \\
Toy C v0.3 & compiled G horizon-4 coverage & $0/4672$ \\
Toy C v0.3 & delegated F after oracle removal & $0/4088$ defined \\""",
    "finite table",
)

replace_once(
    r"""The post-v0.6 package adds \path{verify_toy_c_v0_1.py} with \path{results_v0_1.json}, and \path{verify_toy_c_v0_2.py} with \path{results_v0_2.json}. Both use exact rational arithmetic. Toy C v0.2 exhaustively enumerates the declared finite horizon, checks the B/C/E task-query equalities, computes the non-injective quotient witness and exact nuisance alias gap $19/129$, and reports lookup coverage rather than inventing outputs when the finite lookup control is undefined. No Monte Carlo estimate is used for Toy C.

The v0.6 release remains a frozen historical milestone. This v0.7 research draft is a post-publication extension and does not rewrite the accepted v0.4 framework spine.""",
    r"""The post-v0.6 package adds \path{verify_toy_c_v0_1.py} with \path{results_v0_1.json}, \path{verify_toy_c_v0_2.py} with \path{results_v0_2.json}, and \path{verify_toy_c_v0_3.py} with \path{results_v0_3.json}. All use exact rational arithmetic. Toy C v0.2 exhaustively enumerates the declared finite horizon, checks the B/C/E task-query equalities, computes the non-injective quotient witness and exact nuisance alias gap $19/129$, and reports lookup coverage rather than inventing outputs when the finite lookup control is undefined. Toy C v0.3 evaluates 4088 finite future queries under local possession, delegated access and compilation, then separates them with a 4672-query horizon extension and external-source removal. No Monte Carlo estimate is used for Toy C.

The v0.6 release remains a frozen historical milestone. The v0.7 research draft remains preserved. This v0.8 research draft is the post-v0.6 extension through Toy C v0.3 and does not rewrite the accepted v0.4 framework spine.""",
    "reproducibility",
)

DST_DIR.mkdir(parents=True, exist_ok=True)
DST.write_text(text, encoding="utf-8")
print(hashlib.sha256(DST.read_bytes()).hexdigest())
