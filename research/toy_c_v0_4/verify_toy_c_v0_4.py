#!/usr/bin/env python3
"""
Toy C v0.4 — review-repaired exact finite verification.

Exact finite verification using fractions only.

Purpose:
- preserve the v0.4 finite construction while repairing its interpretation after
  independent review;
- verify that H owns an exact task-specific action-conditioned predictive operator
  in closed form (the FLIP-parity rule) on a fixed history support;
- separate that predictive operator K from the observation-assimilation/update
  machinery U that H does not implement;
- independently exercise delegated Agent F on branch-conditioned queries, including
  source removal.

The project-authored candidate criteria tested by Toy C are counterexample targets,
not formal theories from the literature and not a definition of world-modelhood.
"""

from fractions import Fraction
from itertools import product
import json

F = Fraction
ACTIONS = (0, 1)  # 0=STAY, 1=FLIP
OBS = tuple(product((0, 1), (0, 1)))  # (Y,Z)


def fstr(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def trans_x(bx, a):
    return bx if a == 0 else 1 - bx


def trans_n(bn):
    return F(1, 3) + F(1, 3) * bn


def bayes_binary(prior, obs, accuracy):
    if obs == 1:
        num = accuracy * prior
        den = num + (1 - accuracy) * (1 - prior)
    else:
        num = (1 - accuracy) * prior
        den = num + accuracy * (1 - prior)
    return num / den


def initial_beliefs(obs0):
    y, z = obs0
    bx = bayes_binary(F(1, 2), y, F(3, 4))
    bn = bayes_binary(F(1, 2), z, F(4, 5))
    return bx, bn


def update_full(bx, bn, a, obs):
    y, z = obs
    bx2 = bayes_binary(trans_x(bx, a), y, F(3, 4))
    bn2 = bayes_binary(trans_n(bn), z, F(4, 5))
    return bx2, bn2


def enumerate_reachable(H):
    states = []
    for o0 in OBS:
        bx, bn = initial_beliefs(o0)
        h = (o0,)
        states.append((0, h, bx, bn))
        frontier = [(h, bx, bn)]
        for t in range(H):
            new = []
            for h, bx, bn in frontier:
                for a, o in product(ACTIONS, OBS):
                    bx2, bn2 = update_full(bx, bn, a, o)
                    h2 = h + (a, o)
                    states.append((t + 1, h2, bx2, bn2))
                    new.append((h2, bx2, bn2))
            frontier = new
    return states


def bx_from_full_history(h):
    bx, _bn = initial_beliefs(h[0])
    i = 1
    while i < len(h):
        a = h[i]
        y, _z = h[i + 1]
        bx = bayes_binary(trans_x(bx, a), y, F(3, 4))
        i += 2
    return bx


def terminal_y_probability_from_bx(bx, actions):
    p = bx
    for a in actions:
        p = trans_x(p, a)
    return F(1, 4) + F(1, 2) * p


# M — local model-owning reference.
def answer_M(h, actions):
    return terminal_y_probability_from_bx(bx_from_full_history(h), actions)


# O/F — exact external model service and delegated-access wrapper.
def external_oracle_O(h, actions):
    return answer_M(h, actions)


def answer_F(h, actions, service_available=True):
    if not service_available:
        return None
    return external_oracle_O(h, actions)


def make_query_domain(states, depth_predicate, lengths):
    domain = []
    for t, h, bx, bn in states:
        if depth_predicate(t):
            for k in lengths:
                for actions in product(ACTIONS, repeat=k):
                    truth = terminal_y_probability_from_bx(bx, actions)
                    domain.append((t, h, tuple(actions), truth))
    return domain


def q_seed_from_bx(bx):
    # P(Y_next=1 | h, STAY)
    return terminal_y_probability_from_bx(bx, (0,))


def answer_H(seed_table, h, actions):
    """
    H — factorised endpoint-query compiler.

    H stores one task-predictive scalar q(h) for each supported conditioning
    history and applies only the parity identity induced by STAY/FLIP:
      even number of FLIPs -> q
      odd number of FLIPs  -> 1-q

    It has no declared observation-update rule and no seed for unseen histories.
    """
    q = seed_table.get(h)
    if q is None:
        return None
    return q if (sum(actions) % 2 == 0) else 1 - q


def branch_truth_from_bx(bx, a0, y1, a1):
    """P(Y_{t+2}=1 | current bx, a0, hypothetical Y_{t+1}=y1, a1)."""
    prior = trans_x(bx, a0)
    post = bayes_binary(prior, y1, F(3, 4))
    return terminal_y_probability_from_bx(post, (a1,))


def external_oracle_branch_O(h, a0, y1, a1):
    """Exact delegated branch-conditioned service used by Agent F."""
    return branch_truth_from_bx(bx_from_full_history(h), a0, y1, a1)


def answer_F_branch(h, a0, y1, a1, service_available=True):
    if not service_available:
        return None
    return external_oracle_branch_O(h, a0, y1, a1)


def main():
    states = enumerate_reachable(3)
    counts = {}
    for t, *_ in states:
        counts[t] = counts.get(t, 0) + 1

    # Same finite domain as v0.3.
    D0 = make_query_domain(states, lambda t: t <= 2, (1, 2, 3))

    # Horizon extension: same conditioning histories, substantially longer
    # action sequences. H has no additional per-query entries for this domain.
    D_horizon = make_query_domain(states, lambda t: t <= 2, (4, 5, 6))

    # History-support extension: newly conditioned histories at depth 3, with
    # the same query lengths used in D0.
    D_history = make_query_domain(states, lambda t: t == 3, (1, 2, 3))

    # G from v0.3: full finite table on D0 only.
    compiled_G = {(h, actions): truth for _t, h, actions, truth in D0}

    # H: one q seed for each conditioning history through depth 2.
    seed_table_H = {
        h: q_seed_from_bx(bx)
        for t, h, bx, _bn in states
        if t <= 2
    }

    # Baseline equivalence on D0.
    baseline = {"M": 0, "F": 0, "G": 0, "H": 0}
    all_baseline_equal = True
    for _t, h, actions, truth in D0:
        vals = {
            "M": answer_M(h, actions),
            "F": answer_F(h, actions, True),
            "G": compiled_G.get((h, actions)),
            "H": answer_H(seed_table_H, h, actions),
        }
        for k, v in vals.items():
            baseline[k] += int(v == truth)
        all_baseline_equal &= all(v == truth for v in vals.values())

    # Horizon extension.
    horizon = {"M": 0, "F": 0, "G_defined": 0, "H_defined": 0, "H_exact": 0}
    for _t, h, actions, truth in D_horizon:
        horizon["M"] += int(answer_M(h, actions) == truth)
        horizon["F"] += int(answer_F(h, actions, True) == truth)
        g = compiled_G.get((h, actions))
        if g is not None:
            horizon["G_defined"] += 1
        hv = answer_H(seed_table_H, h, actions)
        if hv is not None:
            horizon["H_defined"] += 1
            horizon["H_exact"] += int(hv == truth)

    # History-support extension.
    hist_ext = {"M": 0, "F": 0, "G_defined": 0, "H_defined": 0}
    for _t, h, actions, truth in D_history:
        hist_ext["M"] += int(answer_M(h, actions) == truth)
        hist_ext["F"] += int(answer_F(h, actions, True) == truth)
        hist_ext["G_defined"] += int(compiled_G.get((h, actions)) is not None)
        hist_ext["H_defined"] += int(answer_H(seed_table_H, h, actions) is not None)

    # Stronger finite non-regression check of the parity identity on all
    # supported histories and action lengths 1..8.
    parity_checks = parity_exact = 0
    for t, h, bx, _bn in states:
        if t <= 2:
            for k in range(1, 9):
                for actions in product(ACTIONS, repeat=k):
                    parity_checks += 1
                    parity_exact += int(
                        answer_H(seed_table_H, h, actions)
                        == terminal_y_probability_from_bx(bx, actions)
                    )

    # Branch-conditioned future query. M computes locally. F must actually
    # traverse its delegated external-service path so source dependence is
    # measurable rather than copied from M. H/G have no implemented branch API.
    branch_total = 0
    branch_M_exact = 0
    branch_F_with_oracle_exact = 0
    branch_F_without_oracle_defined = 0
    for t, h, bx, _bn in states:
        if t <= 2:
            for a0, y1, a1 in product(ACTIONS, (0, 1), ACTIONS):
                branch_total += 1
                truth = branch_truth_from_bx(bx, a0, y1, a1)
                m = branch_truth_from_bx(bx_from_full_history(h), a0, y1, a1)
                f_on = answer_F_branch(h, a0, y1, a1, True)
                f_off = answer_F_branch(h, a0, y1, a1, False)
                branch_M_exact += int(m == truth)
                branch_F_with_oracle_exact += int(f_on == truth)
                branch_F_without_oracle_defined += int(f_off is not None)

    # Source removal.
    f_removed_defined_D0 = 0
    for _t, h, actions, truth in D0:
        f_removed_defined_D0 += int(answer_F(h, actions, False) is not None)

    seed_count = len(seed_table_H)
    result = {
        "toy": "Toy C v0.4",
        "subtitle": "Review repair: task-specific predictive operator K without observation-update U",
        "environment": "same finite POMDP as Toy C v0.2/v0.3",
        "reachable_history_counts": {str(k): v for k, v in sorted(counts.items())},
        "agent_H_factorised_query_program": {
            "supported_conditioning_history_depth": "<=2",
            "predictive_seed_entries": seed_count,
            "seed": "q(h)=P(Y_next=1 | h, STAY)",
            "future_action_rule": "return q for even FLIP parity, 1-q for odd FLIP parity",
            "owns_declared_hidden_state_model": False,
            "owns_declared_observation_update_rule": False,
            "owns_declared_nuisance_model": False,
            "owns_action_conditioned_predictive_operator_K": True,
            "predictive_operator_form": "closed-form FLIP-parity action on q(h)",
            "uses_external_model_service": False,
            "note": (
                "Independent review identified the parity rule as the exact task-specific "
                "predictive operator K in closed form. H therefore witnesses prediction "
                "without an implemented observation-assimilation/update operator U; the "
                "experiment does not decide whether H should be called a world model."
            )
        },
        "baseline_D0": {
            "history_depth": "<=2",
            "future_action_lengths": [1, 2, 3],
            "queries": len(D0),
            "all_answers_equal": bool(all_baseline_equal),
            "M_exact": f"{baseline['M']}/{len(D0)}",
            "F_with_oracle_exact": f"{baseline['F']}/{len(D0)}",
            "G_compiled_exact": f"{baseline['G']}/{len(D0)}",
            "H_factorised_exact": f"{baseline['H']}/{len(D0)}",
            "G_query_entries": len(compiled_G),
            "H_seed_entries": seed_count,
            "query_sequences_per_supported_history": 14,
            "entry_count_note": (
                "4088/292=14 is the identity 2+4+8, the number of baseline action "
                "sequences per supported history. It is not an independently measured "
                "compression ratio and carries no MDL or complexity claim."
            )
        },
        "typed_extension": {
            "future_horizon_extension": {
                "conditioning_history_depth": "<=2",
                "new_action_lengths": [4, 5, 6],
                "queries": len(D_horizon),
                "M_exact": f"{horizon['M']}/{len(D_horizon)}",
                "F_with_oracle_exact": f"{horizon['F']}/{len(D_horizon)}",
                "G_defined": f"{horizon['G_defined']}/{len(D_horizon)}",
                "H_defined": f"{horizon['H_defined']}/{len(D_horizon)}",
                "H_exact_when_defined": f"{horizon['H_exact']}/{horizon['H_defined']}",
                "interpretation": (
                    "H owns the exact task-specific action-conditioned predictive operator "
                    "K in closed form and therefore composes endpoint predictions to longer "
                    "horizons on its fixed supported histories. This does not test absence "
                    "of predictive model structure; it separates prediction from filtering/update."
                )
            },
            "conditioning_history_extension": {
                "new_history_depth": 3,
                "future_action_lengths": [1, 2, 3],
                "queries": len(D_history),
                "M_exact": f"{hist_ext['M']}/{len(D_history)}",
                "F_with_oracle_exact": f"{hist_ext['F']}/{len(D_history)}",
                "G_defined": f"{hist_ext['G_defined']}/{len(D_history)}",
                "H_defined": f"{hist_ext['H_defined']}/{len(D_history)}",
                "interpretation": (
                    "H has no seed for newly conditioned histories and no observation-update "
                    "rule that would generate one. Extension is therefore axis-specific."
                )
            },
            "branch_conditioned_query": {
                "description": "P(Y_{t+2}=1 | h_t, a0, hypothetical Y_{t+1}=y1, a1)",
                "queries": branch_total,
                "M_exact": f"{branch_M_exact}/{branch_total}",
                "F_with_oracle_exact": f"{branch_F_with_oracle_exact}/{branch_total}",
                "F_without_oracle_defined": f"{branch_F_without_oracle_defined}/{branch_total}",
                "G_interface_status": "NOT_IMPLEMENTED",
                "H_interface_status": "NOT_IMPLEMENTED",
                "interpretation": (
                    "M and the independently exercised delegated F path can assimilate "
                    "hypothetical future evidence when the oracle is available; F becomes "
                    "undefined when that source is removed. H/G do not implement this "
                    "branch-conditioned interface. The scoped distinction is prediction "
                    "versus observation-assimilation/filtering, not model versus non-model."
                )
            }
        },
        "parity_identity_nonregression": {
            "histories": seed_count,
            "action_lengths_checked": "1..8",
            "exact_checks": f"{parity_exact}/{parity_checks}",
            "analytic_identity": (
                "For any finite STAY/FLIP sequence in this deterministic X dynamics, the "
                "terminal X belief equals the initial belief after an even number of FLIPs "
                "and its complement after an odd number. Hence the declared endpoint Y query "
                "depends only on q(h) and FLIP parity."
            ),
            "novelty_claim": False
        },
        "external_source_removal": {
            "F_defined_on_D0_after_oracle_removal": f"{f_removed_defined_D0}/{len(D0)}",
            "H_exact_on_D0_without_external_source": f"{baseline['H']}/{len(D0)}",
            "H_exact_on_horizon_extension_without_external_source": f"{horizon['H_exact']}/{len(D_horizon)}",
            "interpretation": (
                "H combines local availability and future-horizon extension, yet remains "
                "limited to a fixed conditioning-history/query interface."
            )
        },
        "hypothesis_status_after_v0_4": {
            "H1_sufficiency_alone_insufficient": "unchanged",
            "H2_persistent_recursive_state_necessary": "remains weakened",
            "H3_local_internal_model_ownership_necessary": "remains weakened by v0.3",
            "v0_4_candidate_H5_status": (
                "H5 was formulated at v0.4 as a candidate over-reading of v0.3, not "
                "pre-registered. Independent review shows H already owns predictive K, "
                "so v0.4 is better interpreted as prediction-vs-filtering decomposition."
            ),
            "declaration_relation": (
                "Most proposed extension directions are already components of the accepted "
                "declaration tuple D (query family, horizon, history support, intervention, "
                "shift). Source/boundary provenance remains separate evaluation metadata."
            )
        },
        "scope": {
            "establishes": [
                "A task-specific factorised query program can exactly match the model-owning reference on D0.",
                "H owns an exact task-specific predictive operator K in closed form and composes it exactly to longer future horizons on fixed supported histories.",
                "H lacks an implemented observation-assimilation/update operator U, so prediction and filtering/update are separable components in this construction.",
                "The delegated F branch-conditioned path is exact when its external oracle is available and undefined when that source is removed.",
                "H/G do not implement the branch-conditioned hypothetical-evidence interface; this is an interface fact, not a measured failure score."
            ],
            "does_not_establish": [
                "That H is or is not a world model.",
                "A formal complexity, MDL, or minimal-description-length superiority of H over G or M.",
                "That parity-style factorisation exists in general environments.",
                "Independent causal/interventional validity beyond the declared action semantics.",
                "Robustness to regime or distribution shift.",
                "A necessary-and-sufficient definition of world model."
            ]
        }
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
