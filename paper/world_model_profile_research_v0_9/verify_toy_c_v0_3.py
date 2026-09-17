#!/usr/bin/env python3
"""
Toy C v0.3 — Model possession vs model access.

Exact finite verification using fractions only.

Purpose:
- show that a locally model-owning system, an agent delegating to an external
  exact oracle, and a compiled finite answer table can be observationally
  identical on a declared finite query set;
- then separate them under source removal and query-domain extension.

This is a system-boundary / attribution falsification test, not a definition
of world-modelhood.
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


# M — local model owner. It has the task-relevant dynamics locally and can
# recompute from history. This is equivalent in capability to Agent E in v0.2.
def answer_M(h, actions):
    return terminal_y_probability_from_bx(bx_from_full_history(h), actions)


# O — exact external model service. This is deliberately outside Agent F's
# local boundary.
def external_oracle_O(h, actions):
    return answer_M(h, actions)


# F — delegated-access agent. Locally it has no transition/observation/update
# operator; with service_available=True it forwards the query to O.
def answer_F(h, actions, service_available=True):
    if not service_available:
        return None
    return external_oracle_O(h, actions)


def make_query_domain(states, max_history_depth, lengths):
    domain = []
    for t, h, bx, bn in states:
        if t <= max_history_depth:
            for k in lengths:
                for actions in product(ACTIONS, repeat=k):
                    truth = terminal_y_probability_from_bx(bx, actions)
                    domain.append((t, h, tuple(actions), truth))
    return domain


def main():
    H = 3
    states = enumerate_reachable(H)

    counts = {}
    for t, *_ in states:
        counts[t] = counts.get(t, 0) + 1

    # Declared benchmark domain D0:
    # all histories through depth 2, future open-loop action sequences length 1..3.
    D0 = make_query_domain(states, max_history_depth=2, lengths=(1, 2, 3))

    # Extension domain D+:
    # same current-history support but horizon 4, deliberately not compiled into G.
    Dplus = make_query_domain(states, max_history_depth=2, lengths=(4,))

    # G — compiled finite answer object. It stores exactly the answers on D0 and
    # has no transition/update rule or extrapolation rule outside those keys.
    compiled_G = {(h, actions): truth for _t, h, actions, truth in D0}

    # 1) Finite observational equivalence on D0.
    m_exact = f_exact = g_exact = 0
    all_equal = True
    for _t, h, actions, truth in D0:
        m = answer_M(h, actions)
        f = answer_F(h, actions, service_available=True)
        g = compiled_G.get((h, actions))
        m_exact += int(m == truth)
        f_exact += int(f == truth)
        g_exact += int(g == truth)
        all_equal &= (m == f == g == truth)

    # 2) Query-domain extension to a horizon not compiled into G.
    m_ext = f_ext = g_ext_defined = g_ext_exact = 0
    for _t, h, actions, truth in Dplus:
        m = answer_M(h, actions)
        f = answer_F(h, actions, service_available=True)
        g = compiled_G.get((h, actions))
        m_ext += int(m == truth)
        f_ext += int(f == truth)
        if g is not None:
            g_ext_defined += 1
            g_ext_exact += int(g == truth)

    # 3) Remove the external model service.
    f_after_removal_defined = f_after_removal_exact = 0
    for _t, h, actions, truth in D0:
        f = answer_F(h, actions, service_available=False)
        if f is not None:
            f_after_removal_defined += 1
            f_after_removal_exact += int(f == truth)

    # Local owner M is unaffected by external service removal.
    m_after_removal_exact = sum(
        int(answer_M(h, actions) == truth)
        for _t, h, actions, truth in D0
    )

    # G is also unaffected on the compiled domain, but still cannot extend.
    g_after_removal_exact = sum(
        int(compiled_G[(h, actions)] == truth)
        for _t, h, actions, truth in D0
    )

    # Elementary finite-compilation witness:
    # all values in D0 can be replaced by a table with one entry per query.
    # This does not claim semantic equivalence outside D0.
    distinct_outputs = sorted({truth for *_rest, truth in D0})

    result = {
        "toy": "Toy C v0.3",
        "environment": "same finite POMDP as Toy C v0.2",
        "reachable_history_counts": {str(k): v for k, v in sorted(counts.items())},
        "declared_query_domain_D0": {
            "history_depth": "<=2",
            "future_action_sequence_lengths": [1, 2, 3],
            "queries": len(D0),
            "query": "P(Y_{t+k}=1 | h_t, future action sequence)"
        },
        "extension_domain_Dplus": {
            "history_depth": "<=2",
            "future_action_sequence_lengths": [4],
            "queries": len(Dplus)
        },
        "agents": {
            "M_local_model_owner": {
                "owns_task_dynamics_inside_local_boundary": True,
                "uses_external_model_service": False,
                "persistent_recursive_state_required": False
            },
            "F_delegated_access": {
                "owns_task_dynamics_inside_local_boundary": False,
                "uses_external_model_service": True,
                "local_future_answer_without_service": False
            },
            "G_compiled_answer_object": {
                "owns_transition_or_update_operator": False,
                "compiled_entries": len(compiled_G),
                "declared_extrapolation_rule": False
            }
        },
        "finite_observational_equivalence_on_D0": {
            "all_answers_equal": bool(all_equal),
            "M_exact": f"{m_exact}/{len(D0)}",
            "F_with_oracle_exact": f"{f_exact}/{len(D0)}",
            "G_compiled_exact": f"{g_exact}/{len(D0)}",
            "distinct_exact_output_values": len(distinct_outputs),
            "interpretation": (
                "On the declared finite query set, external delegation and a compiled "
                "answer table are observationally indistinguishable from the locally "
                "model-owning reference by answer correctness alone."
            )
        },
        "query_domain_extension": {
            "M_exact": f"{m_ext}/{len(Dplus)}",
            "F_with_oracle_exact": f"{f_ext}/{len(Dplus)}",
            "G_defined": f"{g_ext_defined}/{len(Dplus)}",
            "G_exact_when_defined": f"{g_ext_exact}/{g_ext_defined}" if g_ext_defined else "NOT_APPLICABLE",
            "interpretation": (
                "The compiled finite answer object has no coverage on the uncompiled "
                "horizon-4 domain, while the local model and delegated oracle remain exact."
            )
        },
        "external_source_removal": {
            "M_local_model_exact_after_oracle_removal": f"{m_after_removal_exact}/{len(D0)}",
            "F_defined_after_oracle_removal": f"{f_after_removal_defined}/{len(D0)}",
            "F_exact_after_oracle_removal": (
                f"{f_after_removal_exact}/{f_after_removal_defined}"
                if f_after_removal_defined else "NOT_APPLICABLE"
            ),
            "G_compiled_exact_after_oracle_removal": f"{g_after_removal_exact}/{len(D0)}",
            "interpretation": (
                "Delegated access disappears when its source is removed; locally owned "
                "dynamics remain usable, while compiled answers survive only on their finite cache domain."
            )
        },
        "finite_compilation_observation": {
            "statement": (
                "For this finite declared domain D0, the exact input-output map can be "
                "compiled into one table entry per query. Therefore finite behavioral "
                "equivalence on D0 cannot by itself identify whether a generative/predictive "
                "mechanism is internally possessed."
            ),
            "novelty_claim": False
        },
        "boundary_attribution": {
            "local_agent_boundary": {
                "M": "internal model possession",
                "F": "external model access only",
                "G": "compiled finite answers"
            },
            "expanded_system_boundary_including_oracle": {
                "F_plus_O": "the composite system contains the external model service and has exact future-query capability"
            },
            "interpretation": (
                "Any claim about where the model resides is boundary-relative and should "
                "declare the evaluated system boundary."
            )
        },
        "hypothesis_status_after_v0_3": {
            "H1_sufficiency_alone_insufficient": "unchanged: still only an architectural separation example",
            "H2_persistent_recursive_state_necessary": "remains weakened by Toy C v0.2",
            "H3_internal_ownership_of_action_indexed_future_mechanism": (
                "weakened as a system-level necessity: delegated access reproduces the "
                "same declared behavior while the local agent owns no model"
            ),
            "H4_breadth_as_profile_frontier": (
                "retained and complemented by explicit system-boundary and source-dependence metadata"
            )
        },
        "scope": {
            "establishes": [
                "Exact answer behavior on a finite declared query set does not identify internal model possession in this construction.",
                "External model access can substitute exactly for local model possession while the service is available.",
                "A compiled finite query-answer table can match a model-owning system exactly on the compiled domain.",
                "Source removal and query-domain extension separate local possession, delegated access, and finite compilation operationally.",
                "Attribution of model possession depends on the declared system boundary."
            ],
            "does_not_establish": [
                "That a lookup table should or should not be called a world model.",
                "That external model services are equivalent to local models under latency, privacy, reliability, cost, or robustness constraints.",
                "A necessary-and-sufficient definition of world model.",
                "Interventional validity beyond the declared action semantics.",
                "Robustness to distribution or regime shift."
            ]
        }
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
