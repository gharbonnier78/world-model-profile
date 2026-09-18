#!/usr/bin/env python3
"""Create the v0.9.1 repairs-only TeX from the pinned v0.9 source.

This script intentionally performs no new experiment. It applies only the
independent-review repairs documented in review/INDEPENDENT_REVIEW_V0_9_CLAUDE.md.
"""

from pathlib import Path
import hashlib

SRC = Path("paper/world_model_profile_research_v0_9/world_model_profile_research_v0_9.tex")
OUT = Path("paper/world_model_profile_research_v0_9_1/world_model_profile_research_v0_9_1.tex")
EXPECTED_SHA256 = "7ea5b0f41374722e73591fd777436749c594d70ed704ae654e49ceaf076be691"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one match, got {text.count(old)}")
    return text.replace(old, new, 1)


def replace_between(text: str, start: str, end: str, replacement: str, label: str) -> str:
    i = text.find(start)
    if i < 0:
        raise RuntimeError(f"{label}: start marker not found")
    j = text.find(end, i + len(start))
    if j < 0:
        raise RuntimeError(f"{label}: end marker not found")
    return text[:i] + replacement.rstrip() + "\n\n" + text[j:]


def main() -> None:
    raw = SRC.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != EXPECTED_SHA256:
        raise RuntimeError(f"pinned v0.9 TeX SHA mismatch: {got}")

    t = raw.decode("utf-8")

    t = replace_once(
        t,
        r"\large Post-v0.6 Research Draft with Toy C v0.1--v0.4 Extensions}",
        r"\large Post-v0.6 Research Draft v0.9.1 --- Independent-Review Repairs Only}",
        "title",
    )
    t = replace_once(t, r"\date{17 September 2026}", r"\date{18 September 2026}", "date")

    abstract = r"""
\begin{abstract}
The term \emph{world model} is used for systems that differ substantially in what they represent, predict, how they are queried, and what decisions or shifts they support. Rather than impose a binary predicate, we use a declared layered evaluation profile: L0 predictive closure at an abstraction frontier; $L1_{\rm int}$ interventional validity; L2.G class-level decision adequacy; L2.O operational model--search adequacy; and L3 robustness under declared shift. Two exact finite constructions establish only that L0 and L2 are non-identical coordinates under explicit declarations. A post-v0.6 Toy C cycle then probes a different question: when, if ever, does a sufficient representation of history become an internal model of the world? Toy C v0.1 separates current-state knowledge from future-query machinery; v0.2 gives a genuinely non-injective task-predictive quotient and challenges persistent-state necessity; v0.3 separates local possession, delegated access and finite compilation. This v0.9.1 repair preserves the exact v0.4 evidence but narrows its interpretation after independent review: Agent H's FLIP-parity rule is itself the exact task-specific action-conditioned predictive operator $K$ in closed form, so v0.4 witnesses a prediction-versus-filtering/update decomposition rather than long-horizon prediction without model structure. The repaired delegated Agent F branch path is exact on all 2336 branch-conditioned queries when its oracle is available and undefined on all 2336 when the source is removed. Most proposed ``extension axes'' are already directions encoded in the accepted declaration tuple; source/system-boundary provenance remains separate evaluation metadata. We therefore do not claim a new taxonomy, a new framework coordinate, or a necessary-and-sufficient definition of world model. The next gate is the previously recorded decision-relevance test: if the capability contract changes no engineering decision beyond a flat technical description, the eliminativist alternative is strengthened and the mechanical Toy C chain stops.
\end{abstract}
"""
    t = replace_between(t, r"\begin{abstract}", r"\paragraph{Scope and evidence.}", abstract, "abstract")

    t = replace_once(
        t,
        r"\item In a post-v0.6 falsification cycle, Toy C separates current-state sufficiency from future-query capability, tests a genuinely information-losing predictive quotient and a direct-history sequence predictor, distinguishes local model possession from delegated access and finite compiled answers, and finally shows that extension/generalisation must itself be typed by axis before any new framework layer is considered.",
        r"\item In a post-v0.6 candidate-criterion cycle, Toy C separates current-state sufficiency from future-query capability, tests a genuinely information-losing predictive quotient and a direct-history sequence predictor, distinguishes local possession from delegated access and finite compilation, and in v0.4 separates task-specific predictive propagation $K$ from observation-assimilation/update $U$. These are counterexamples to project-authored candidate criteria, not falsifications of a general theory.",
        "intro contribution",
    )

    t = replace_once(
        t,
        "Toy A and Toy B separate predictive and decision-relative adequacy. They do not answer a different question exposed by the POMDP belief-state comparison: if a statistic of history is already sufficient, what additional technical property, if any, turns that state into a model? Toy C attacks that question through finite counterexamples rather than by adding another profile coordinate.",
        "Toy A and Toy B separate predictive and decision-relative adequacy. They do not answer a different question exposed by the POMDP belief-state comparison: if a statistic of history is already sufficient, what additional technical property, if any, turns that state into a model? Toy C attacks that question through finite counterexamples to project-authored candidate criteria rather than by adding another profile coordinate. Dyna provides a classical learned-model/planning reference point~\\cite{sutton1991}, while predictive state representations show that action-conditional predictions can themselves serve as state~\\cite{littman2001}.",
        "Toy C opener citations",
    )

    t = replace_once(
        t,
        "can be updated and rolled forward directly in $q$-space.",
        "can be updated and rolled forward directly in $q$-space, matching the predictive-state idea of representing dynamical state by action-conditional predictions rather than by a privileged latent ontology~\\cite{littman2001}.",
        "PSR point-of-use",
    )

    t = replace_once(
        t,
        r"\subsection{Agent E: falsifying a strong recursive-state requirement}",
        r"\subsection{Agent E: weakening a strong recursive-state requirement}",
        "Agent E heading",
    )

    repaired_v04 = r"""
\subsection{Toy C v0.4: review-repaired prediction versus filtering decomposition}

Toy C v0.4 kept the v0.2/v0.3 environment fixed and explored a candidate over-reading of v0.3: whether extension beyond a compiled finite benchmark could itself act as a scalar discriminator of model-like structure. That candidate was formulated at v0.4; it was not pre-registered as part of H1--H4.

Agent H stores one scalar seed for each supported conditioning history through depth two,
\[
q(h)=P(Y_{t+1}=1\mid h,\mathrm{STAY}),
\]
giving 292 seeds. Under the deterministic task dynamics, \texttt{STAY} is the identity and \texttt{FLIP} is an involution. H therefore applies the exact closed-form action-conditioned predictive operator
\[
Q_H(h,a_{t:t+k-1})=
\begin{cases}
q(h), & \text{even number of FLIPs},\\
1-q(h), & \text{odd number of FLIPs}.
\end{cases}
\]
Independent review correctly identified that this parity rule is not an alternative to predictive dynamics: it \emph{is} the task-specific operator $K$ in closed form. In the provisional object $\mathcal M=(\sigma,U,K,\mathcal Q)$, H is best read as carrying supported $\sigma$, $K$, and endpoint-query semantics while lacking the observation-assimilation/update operator $U$ needed to incorporate new evidence. This is the classical distinction between predictive propagation and filtering/state update in partially observed control~\cite{astrom1965,striebel1965}.

The exact baseline remains unchanged:
\[
M=F+O=G=H=\frac{4088}{4088}.
\]
For action-sequence lengths 4, 5 and 6, H composes its owned $K$ exactly on the fixed supported histories:
\[
M=F+O=H=\frac{32704}{32704},
\qquad
\mathrm{coverage}(G)=\frac{0}{32704}.
\]
The additional $148920/148920$ parity checks verify this closed-form composition for all supported histories and action sequences of lengths one through eight. The identity $4088=292(2+4+8)$ is only benchmark arithmetic, not an independently measured compression ratio.

When the conditioning support is extended to new depth-three histories, H has no implemented update route from the new observations to a supported seed:
\[
M=F+O=\frac{28672}{28672},
\qquad
G=H=\frac{0}{28672}\text{ defined}.
\]
This is therefore not surprising evidence for a new ``extension axis''; it is a direct consequence of H possessing $K$ but not $U$.

The branch-conditioned query
\[
P(Y_{t+2}=1\mid h_t,a_0,Y_{t+1}=y_1,a_1)
\]
contains 2336 cases. The repaired verifier now exercises the delegated F path independently rather than assigning its result from M:
\[
M=\frac{2336}{2336},
\qquad
F+O=\frac{2336}{2336},
\qquad
\mathrm{coverage}(F\mid O\text{ removed})=\frac{0}{2336}.
\]
G and H do not implement this branch-conditioned interface; that is recorded as an interface status, not a measured failure score.

The earlier typed-extension tuple is also narrowed. Most proposed directions are already components of the accepted declaration tuple $\mathcal D$: query family $\mathbb A$, horizon $H_{\mathbb A}$, support $\Omega_0$, intervention family $\mathcal I$, and shift class $\Delta$. Source/system-boundary provenance, exposed by v0.3, remains useful separate evaluation metadata. No new taxonomy or L4 is warranted.

The repaired conclusion of v0.4 is therefore modest: predictive propagation $K$ and evidence assimilation/update $U$ are separable components in this finite construction, and delegated capability must be qualified by source/boundary. It does not show prediction without model structure, does not establish a universal extension taxonomy, and does not settle whether H should be called a world model.
"""
    t = replace_between(
        t,
        r"\subsection{Toy C v0.4: typed extension without full generative closure}",
        r"\section{Illustrative diagnostics}",
        repaired_v04,
        "Toy C v0.4 subsection",
    )

    t = replace_once(
        t,
        r"\item Toy C v0.4 relies on a deliberately simple parity factorisation; it demonstrates axis-specific extension in this finite system, not a general factorisation theorem or formal complexity advantage.",
        r"\item Toy C v0.4 relies on a deliberately simple involutive task dynamics. Its parity rule is the exact task-specific predictive operator $K$; the repaired result is a finite prediction-versus-filtering/update decomposition, not a general factorisation theorem, generalisation theorem, or formal complexity advantage.",
        "limitations v0.4",
    )

    old_conclusion = """The post-v0.6 Toy C cycle adds a different lesson: exact current-state sufficiency, task-relative predictive closure, full hidden-state reconstruction, and persistent recursive-state storage should not be silently identified. Toy C v0.2 in particular makes query breadth observable through an exact zero-versus-positive aliasing frontier and weakens a strong recursive-state necessity hypothesis before it can harden into a definition. Toy C v0.3 further shows that local possession, delegated access and finite compiled answers can be indistinguishable on a declared finite query domain, so model-location claims require an explicit system boundary and capability source. Toy C v0.4 then shows that even extension beyond that domain is not a scalar property: a small task-specific query program can extrapolate indefinitely along one declared axis while being unable to absorb one new conditioning observation or answer a branch-conditioned query."""
    new_conclusion = """The post-v0.6 Toy C cycle adds a different lesson: exact current-state sufficiency, task-relative predictive closure, full hidden-state reconstruction, persistent recursive-state storage, model location, and source provenance should not be silently identified. Toy C v0.2 in particular makes query breadth observable through an exact zero-versus-positive aliasing frontier and weakens a strong recursive-state necessity candidate before it can harden into a definition. Toy C v0.3 shows that local possession, delegated access and finite compiled answers can be indistinguishable on a declared finite query domain, so model-location claims require an explicit system boundary and capability source. The v0.9.1 repair narrows Toy C v0.4: Agent H already owns the exact task-specific predictive operator $K$ in closed form; what it lacks is the $U$-like filtering/update machinery for assimilating new evidence. Thus v0.4 is a clean finite witness of component decomposition, not evidence for long-horizon prediction without model structure."""
    t = replace_once(t, old_conclusion, new_conclusion, "conclusion Toy C paragraph")

    decision_para = r"""
The Toy C sequence also exposed a change in research object that is now made explicit. The original question asked when a sufficient state becomes a model; after several candidate binary boundaries dissolved into separate components, the work began to ask how future-query capability should be qualified and reported. That move may be useful, but it must earn its keep. The next experiment is therefore not Toy C v0.5: it is the previously recorded decision-relevance test. If capability-contract metadata changes no concrete engineering evaluation or decision beyond the flat technical description $(\sigma,U,K,\mathcal Q,\text{boundary},\text{source},\ldots)$, the eliminativist alternative is strengthened and the mechanical Toy C chain stops.
"""
    t = replace_once(
        t,
        "\nWhether this deserves the name ``world-model profile'' remains an open explanatory question.",
        "\n" + decision_para + "\nWhether this deserves the name ``world-model profile'' remains an open explanatory question.",
        "research-object shift",
    )

    t = replace_once(
        t,
        r"Toy C v0.4 & H exact on horizon-4/5/6 extension & $32704/32704$ \\",
        r"Toy C v0.4 & H closed-form $K$ on horizon-4/5/6 & $32704/32704$ \\",
        "table H horizon",
    )
    t = replace_once(
        t,
        r"Toy C v0.4 & H on new depth-3 conditioning histories & $0/28672$ defined \\",
        r"Toy C v0.4 & H without update $U$ on new depth-3 histories & $0/28672$ defined \\",
        "table H history",
    )
    t = replace_once(
        t,
        r"Toy C v0.4 & M/F branch-conditioned evidence queries & $2336/2336$ each \\",
        r"Toy C v0.4 & M branch-conditioned evidence queries & $2336/2336$ \\",
        "table branch M",
    )
    t = replace_once(
        t,
        r"Toy C v0.4 & H/G branch-conditioned interface & unsupported \\",
        r"""Toy C v0.4 & delegated F branch: with O / O removed & $2336/2336$ / $0/2336$ defined \\
Toy C v0.4 & H/G branch-conditioned interface & not implemented \\""".rstrip(),
        "table branch F/HG",
    )

    t = replace_once(
        t,
        "Toy C v0.4 evaluates 4088 baseline queries, 32704 longer-horizon endpoint queries, 28672 newly conditioned-history queries, 2336 branch-conditioned hypothetical-evidence queries, and an additional 148920 exact parity non-regression checks. No Monte Carlo estimate is used for Toy C.",
        "Toy C v0.4 evaluates 4088 baseline queries, 32704 longer-horizon endpoint queries, 28672 newly conditioned-history queries, 2336 branch-conditioned hypothetical-evidence queries, and an additional 148920 exact parity non-regression checks. In v0.9.1 the delegated F branch-conditioned path is independently exercised with the external oracle available and removed; H/G are reported as interface-not-implemented rather than assigned failure scores. No Monte Carlo estimate is used for Toy C.",
        "repro v0.4",
    )

    t = replace_once(
        t,
        "The v0.6 release remains a frozen historical milestone. The v0.7 and v0.8 research drafts remain preserved. This v0.9 research draft is the post-v0.6 extension through Toy C v0.4 and does not rewrite the accepted v0.4 framework spine.",
        "The v0.6 release remains a frozen historical milestone. The v0.7, v0.8 and independently reviewed v0.9 research drafts remain preserved. This v0.9.1 package is a repairs-only revision: it corrects the Toy C v0.4 delegated branch path, prior-art citations, candidate-criterion wording, Chronicle interpretation and manuscript framing without opening a new experiment or rewriting the accepted v0.4 framework spine.",
        "repro version",
    )

    bib_insert = r"""
\bibitem{sutton1991}
R. S. Sutton.
Dyna, an integrated architecture for learning, planning, and reacting.
\emph{ACM SIGART Bulletin}, 2(4):160--163, 1991.
doi:10.1145/122344.122377.

\bibitem{littman2001}
M. L. Littman, R. S. Sutton, and S. Singh.
Predictive Representations of State.
In \emph{Advances in Neural Information Processing Systems 14}, 2001.

\bibitem{astrom1965}
K. J. \AA str\"om.
Optimal Control of Markov Processes with Incomplete State Information.
\emph{Journal of Mathematical Analysis and Applications}, 10:174--205, 1965.
doi:10.1016/0022-247X(65)90154-X.

\bibitem{striebel1965}
C. Striebel.
Sufficient Statistics in the Optimum Control of Stochastic Systems.
\emph{Journal of Mathematical Analysis and Applications}, 12(3):576--592, 1965.
doi:10.1016/0022-247X(65)90027-2.

"""
    t = replace_once(
        t,
        r"\bibitem{ha2018}",
        bib_insert + r"\bibitem{ha2018}",
        "bibliography insert",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(t, encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"sha256={hashlib.sha256(OUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
