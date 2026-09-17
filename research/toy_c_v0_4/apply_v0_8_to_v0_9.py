#!/usr/bin/env python3
"""Transform the checksum-pinned v0.8 research TeX into v0.9 with Toy C v0.4."""

from pathlib import Path
import hashlib

SRC = Path("paper/world_model_profile_research_v0_8/world_model_profile_research_v0_8.tex")
DST_DIR = Path("paper/world_model_profile_research_v0_9")
DST = DST_DIR / "world_model_profile_research_v0_9.tex"
EXPECTED_SRC_SHA256 = "35846deddf39facc84794a569c9ac886f5f6862dd84eb0a496ec38058588e903"

raw = SRC.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
if sha != EXPECTED_SRC_SHA256:
    raise SystemExit(f"Unexpected v0.8 TeX SHA256: {sha}")

text = raw.decode("utf-8")


def replace_once(old, new, label):
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {n}")
    text = text.replace(old, new, 1)


replace_once(
    r"\large Post-v0.6 Research Draft with Toy C v0.1--v0.3 Extensions}",
    r"\large Post-v0.6 Research Draft with Toy C v0.1--v0.4 Extensions}",
    "title",
)

replace_once(
    r"\date{15 September 2026}",
    r"\date{17 September 2026}",
    "date",
)

replace_once(
    "Toy C v0.3 then separates local model possession from delegated model access and finite compilation: all three can be exactly answer-equivalent on a declared finite query domain, while source removal and query-domain extension expose different capability provenance and coverage.",
    "Toy C v0.3 then separates local model possession from delegated model access and finite compilation: all three can be exactly answer-equivalent on a declared finite query domain, while source removal and query-domain extension expose different capability provenance and coverage. Toy C v0.4 attacks the remaining scalar reading of extension itself: a task-specific factorised query program extrapolates exactly to longer future action horizons while failing newly conditioned-history support and hypothetical-evidence assimilation, showing that extension must be declared by axis rather than as a single modelhood discriminator.",
    "abstract",
)

replace_once(
    r"\item In a post-v0.6 falsification cycle, Toy C separates current-state sufficiency from future-query capability, tests a genuinely information-losing predictive quotient and a direct-history sequence predictor, then distinguishes local model possession from delegated access and finite compiled answers before any new framework layer is considered.",
    r"\item In a post-v0.6 falsification cycle, Toy C separates current-state sufficiency from future-query capability, tests a genuinely information-losing predictive quotient and a direct-history sequence predictor, distinguishes local model possession from delegated access and finite compiled answers, and finally shows that extension/generalisation must itself be typed by axis before any new framework layer is considered.",
    "contribution bullet",
)

anchor = r"\section{Illustrative diagnostics}"
insert = r"""
\subsection{Toy C v0.4: typed extension without full generative closure}

Toy C v0.4 deliberately keeps the environment fixed and attacks a tempting over-reading of v0.3. In v0.3, a longer-horizon query domain separated the finite compiled table G from mechanisms M and F that could answer beyond the compiled support. That does not imply that \emph{extension capability} is a scalar discriminator of model-like structure.

Agent H is a task-specific factorised query program. For each supported conditioning history through depth 2, it stores one scalar seed
\[
q(h)=P(Y_{t+1}=1\mid h,\mathrm{STAY}).
\]
There are exactly 292 such seeds. H declares no hidden-state model, nuisance model, observation-update rule, recursively stored latent state, or external model service. It uses only the algebraic identity induced by the deterministic task dynamics: an even number of future \texttt{FLIP} actions preserves the task belief and an odd number complements it. Hence
\[
Q_H(h,a_{t:t+k-1})=
\begin{cases}
q(h), & \text{even number of FLIPs},\\
1-q(h), & \text{odd number of FLIPs}.
\end{cases}
\]
The construction intentionally does not decide whether H should be called a model.

On the baseline domain $\mathcal D_0$ from v0.3, all four mechanisms are exact:
\[
M=F+O=G=H=\frac{4088}{4088}.
\]
The compiled table G contains 4088 query-answer entries, while H uses 292 history seeds plus one rule. The ratio $4088/292=14$ is bookkeeping only; we make no compression, Kolmogorov-complexity, or MDL claim because the description length of H's rule is not included.

The first extension changes only the future action horizon. Keeping the same conditioning histories, action-sequence lengths 4, 5 and 6 produce 32704 new endpoint queries. M and F remain exact, G has no entries, and H remains exact without new per-query cache entries:
\[
M=F+O=H=\frac{32704}{32704},
\qquad
\mathrm{coverage}(G)=\frac{0}{32704}.
\]
The parity identity is additionally checked by exact rational arithmetic for all 292 supported histories and all binary action sequences of lengths 1 through 8, giving $148920/148920$ exact comparisons.

The second extension changes a different axis. Returning to action lengths 1--3 but conditioning on newly observed histories at depth 3 yields 28672 queries. M and F can reconstruct the task belief from the new history, whereas neither G nor H has a corresponding entry or update rule:
\[
M=F+O=\frac{28672}{28672},
\qquad
G=H=\frac{0}{28672}\text{ defined}.
\]
Thus future-horizon extension and conditioning-history extension are distinct capabilities in this finite construction.

A third query makes the distinction sharper by requiring assimilation of hypothetical future evidence before prediction continues:
\[
P(Y_{t+2}=1\mid h_t,a_0,Y_{t+1}=y_1,a_1).
\]
The domain contains 2336 branch-conditioned queries. M and F are exact on all of them; G and H expose no such interface. Open-loop endpoint extrapolation is therefore distinct from branch-conditioned evidence assimilation.

Source removal also ceases to be a scalar discriminator. Once the external oracle O is removed, F becomes undefined on the baseline domain, but H remains exact on both the 4088 baseline queries and the 32704 longer-horizon queries. Local availability plus source independence plus long-horizon extrapolation still does not identify a full generative/update model under the declared interface.

The methodological residue is a typed extension contract rather than a new layer:
\[
E=(E_{\rm horizon},E_{\rm history},E_{\rm query},E_{\rm branch},E_{\rm source},E_{\rm intervention},E_{\rm shift}).
\]
This tuple is exploratory metadata. Toy C v0.4 weakens the hypothesis that generic ``extension beyond the benchmark'' is a scalar modelhood discriminator. It does not establish a universal taxonomy of extension axes, causal validity, regime-shift robustness, or a necessary-and-sufficient definition of world model.

\section{Illustrative diagnostics}"""
replace_once(anchor, insert, "Toy C v0.4 insertion")

replace_once(
    "Toy C v0.3 further shows that local possession, delegated access and finite compiled answers can be indistinguishable on a declared finite query domain, so model-location claims require an explicit system boundary and capability source.",
    "Toy C v0.3 further shows that local possession, delegated access and finite compiled answers can be indistinguishable on a declared finite query domain, so model-location claims require an explicit system boundary and capability source. Toy C v0.4 then shows that even extension beyond that domain is not a scalar property: a small task-specific query program can extrapolate indefinitely along one declared axis while being unable to absorb one new conditioning observation or answer a branch-conditioned query.",
    "conclusion",
)

replace_once(
    r"    \item The abstraction frontier is externally declared. Adaptive abstraction discovery and revision remain future work.",
    r"    \item The abstraction frontier is externally declared. Adaptive abstraction discovery and revision remain future work.\n    \item Toy C v0.4 relies on a deliberately simple parity factorisation; it demonstrates axis-specific extension in this finite system, not a general factorisation theorem or formal complexity advantage.",
    "limitations",
)

replace_once(
    r"Toy C v0.3 & delegated F after oracle removal & $0/4088$ defined \\",
    r"Toy C v0.3 & delegated F after oracle removal & $0/4088$ defined \\\nToy C v0.4 & H exact on baseline $D_0$ & $4088/4088$ \\\nToy C v0.4 & H exact on horizon-4/5/6 extension & $32704/32704$ \\\nToy C v0.4 & H on new depth-3 conditioning histories & $0/28672$ defined \\\nToy C v0.4 & M/F branch-conditioned evidence queries & $2336/2336$ each \\\nToy C v0.4 & H/G branch-conditioned interface & unsupported \\",
    "finite results table",
)

replace_once(
    r"The post-v0.6 package adds \path{verify_toy_c_v0_1.py} with \path{results_v0_1.json}, \path{verify_toy_c_v0_2.py} with \path{results_v0_2.json}, and \path{verify_toy_c_v0_3.py} with \path{results_v0_3.json}. All use exact rational arithmetic. Toy C v0.2 exhaustively enumerates the declared finite horizon, checks the B/C/E task-query equalities, computes the non-injective quotient witness and exact nuisance alias gap $19/129$, and reports lookup coverage rather than inventing outputs when the finite lookup control is undefined. Toy C v0.3 evaluates 4088 finite future queries under local possession, delegated access and compilation, then separates them with a 4672-query horizon extension and external-source removal. No Monte Carlo estimate is used for Toy C.\n\nThe v0.6 release remains a frozen historical milestone. The v0.7 research draft remains preserved. This v0.8 research draft is the post-v0.6 extension through Toy C v0.3 and does not rewrite the accepted v0.4 framework spine.",
    r"The post-v0.6 package adds \path{verify_toy_c_v0_1.py} with \path{results_v0_1.json}, \path{verify_toy_c_v0_2.py} with \path{results_v0_2.json}, \path{verify_toy_c_v0_3.py} with \path{results_v0_3.json}, and \path{verify_toy_c_v0_4.py} with \path{results_v0_4.json}. All use exact rational arithmetic. Toy C v0.2 exhaustively enumerates the declared finite horizon, checks the B/C/E task-query equalities, computes the non-injective quotient witness and exact nuisance alias gap $19/129$, and reports lookup coverage rather than inventing outputs when the finite lookup control is undefined. Toy C v0.3 evaluates 4088 finite future queries under local possession, delegated access and compilation, then separates them with horizon extension and external-source removal. Toy C v0.4 evaluates 4088 baseline queries, 32704 longer-horizon endpoint queries, 28672 newly conditioned-history queries, 2336 branch-conditioned hypothetical-evidence queries, and an additional 148920 exact parity non-regression checks. No Monte Carlo estimate is used for Toy C.\n\nThe v0.6 release remains a frozen historical milestone. The v0.7 and v0.8 research drafts remain preserved. This v0.9 research draft is the post-v0.6 extension through Toy C v0.4 and does not rewrite the accepted v0.4 framework spine.",
    "reproducibility",
)

DST_DIR.mkdir(parents=True, exist_ok=True)
DST.write_text(text, encoding="utf-8")
print(hashlib.sha256(DST.read_bytes()).hexdigest())
