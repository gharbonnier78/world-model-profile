#!/usr/bin/env python3
"""
Toy C v0.2 — Nontrivial task-relative predictive quotient and a falsifier for
persistent recursive-state necessity.

Exact finite verification using fractions only.
"""

from fractions import Fraction
from itertools import product
import json

F = Fraction
ACTIONS = (0, 1)
OBS = tuple(product((0, 1), (0, 1)))  # (y,z)


def fstr(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def x_obs_prob1_from_b(bx):
    return F(1, 4) + F(1, 2) * bx


def n_obs_prob1_from_b(bn):
    return F(1, 5) + F(3, 5) * bn


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


def update_C(bx, bn, a, obs):
    y, z = obs
    bx_prior = trans_x(bx, a)
    bn_prior = trans_n(bn)
    bx2 = bayes_binary(bx_prior, y, F(3, 4))
    bn2 = bayes_binary(bn_prior, z, F(4, 5))
    return bx2, bn2


def pred_y_C(bx, a):
    return x_obs_prob1_from_b(trans_x(bx, a))


def pred_z_C(bn):
    return n_obs_prob1_from_b(trans_n(bn))


def q_from_bx(bx):
    return x_obs_prob1_from_b(bx)


def bx_from_q(q):
    return 2 * q - F(1, 2)


def pred_y_B(q, a):
    return q if a == 0 else 1 - q


def update_B(q, a, obs):
    y, _z = obs
    r = pred_y_B(q, a)
    if y == 1:
        return 1 - F(3, 16) / r
    return F(3, 16) / (1 - r)


def reward_x1_C(bx, a):
    return trans_x(bx, a)


def reward_x1_B(q, a):
    return bx_from_q(pred_y_B(q, a))


def greedy_action(vals):
    return 0 if vals[0] >= vals[1] else 1


def initial_beliefs(obs0):
    y, z = obs0
    bx = bayes_binary(F(1, 2), y, F(3, 4))
    bn = bayes_binary(F(1, 2), z, F(4, 5))
    return bx, bn


def enumerate_reachable(H):
    # history: ((y0,z0), a0, (y1,z1), ...)
    states = []
    for o0 in OBS:
        bx, bn = initial_beliefs(o0)
        q = q_from_bx(bx)
        h = (o0,)
        states.append((0, h, bx, bn, q))
        frontier = [(h, bx, bn, q)]
        for t in range(H):
            new = []
            for h, bx, bn, q in frontier:
                for a, o in product(ACTIONS, OBS):
                    bx2, bn2 = update_C(bx, bn, a, o)
                    q2 = update_B(q, a, o)
                    h2 = h + (a, o)
                    states.append((t + 1, h2, bx2, bn2, q2))
                    new.append((h2, bx2, bn2, q2))
            frontier = new
    return states


def branch_B(q, seq):
    for a, o in seq:
        q = update_B(q, a, o)
    return q


def branch_C(bx, bn, seq):
    for a, o in seq:
        bx, bn = update_C(bx, bn, a, o)
    return bx, bn


def open_loop_y_B(q, actions):
    r = q
    for a in actions:
        r = pred_y_B(r, a)
    return r


def open_loop_y_C(bx, actions):
    p = bx
    for a in actions:
        p = trans_x(p, a)
    return x_obs_prob1_from_b(p)


# Agent E: no persistent recursive state. Every query starts from raw history.
def bx_from_full_history(h):
    bx, _ = initial_beliefs(h[0])
    i = 1
    while i < len(h):
        a = h[i]
        y, _z = h[i + 1]
        bx = bayes_binary(trans_x(bx, a), y, F(3, 4))
        i += 2
    return bx


def pred_y_E(h, a):
    return pred_y_C(bx_from_full_history(h), a)


def open_loop_y_E(h, actions):
    return open_loop_y_C(bx_from_full_history(h), actions)


def main():
    H = 3
    states = enumerate_reachable(H)
    counts = {}
    for t, *_ in states:
        counts[t] = counts.get(t, 0) + 1

    exact = True
    rep_checks = one_checks = update_checks = decision_checks = 0
    for t, h, bx, bn, q in states:
        rep_checks += 1
        exact &= q == q_from_bx(bx)
        exact &= bx_from_full_history(h) == bx
        if t < H:
            for a in ACTIONS:
                one_checks += 1
                exact &= pred_y_B(q, a) == pred_y_C(bx, a) == pred_y_E(h, a)
                rc = {aa: reward_x1_C(bx, aa) for aa in ACTIONS}
                rb = {aa: reward_x1_B(q, aa) for aa in ACTIONS}
                decision_checks += 1
                exact &= rc == rb and greedy_action(rc) == greedy_action(rb)
                for o in OBS:
                    update_checks += 1
                    bx2, _bn2 = update_C(bx, bn, a, o)
                    q2 = update_B(q, a, o)
                    exact &= q2 == q_from_bx(bx2)

    branch_checks = 0
    for t, h, bx, bn, q in states:
        if t <= 1:
            for actions in product(ACTIONS, repeat=2):
                for obs_seq in product(OBS, repeat=2):
                    seq = list(zip(actions, obs_seq))
                    bx2, _bn2 = branch_C(bx, bn, seq)
                    q2 = branch_B(q, seq)
                    branch_checks += 1
                    exact &= q2 == q_from_bx(bx2)

    open_checks = 0
    for t, h, bx, bn, q in states:
        if t <= 1:
            for k in range(1, 5):
                for actions in product(ACTIONS, repeat=k):
                    pc = open_loop_y_C(bx, actions)
                    pb = open_loop_y_B(q, actions)
                    pe = open_loop_y_E(h, actions)
                    open_checks += 1
                    exact &= pc == pb == pe

    groups = {}
    for t, h, bx, bn, q in states:
        groups.setdefault((t, q), []).append((h, bx, bn))

    collision_pairs = 0
    max_z_gap = F(0)
    example = None
    for (t, q), members in groups.items():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                h1, bx1, bn1 = members[i]
                h2, bx2, bn2 = members[j]
                if bn1 != bn2:
                    collision_pairs += 1
                    gap = abs(pred_z_C(bn1) - pred_z_C(bn2))
                    if gap > max_z_gap:
                        max_z_gap = gap
                        example = (t, q, h1, bn1, pred_z_C(bn1), h2, bn2, pred_z_C(bn2))

    max_y_gap = F(0)
    for (_t, _q), members in groups.items():
        vals = [pred_y_C(bx, 0) for _h, bx, _bn in members]
        if vals:
            max_y_gap = max(max_y_gap, max(vals) - min(vals))

    lookup = {}
    for t, h, bx, bn, q in states:
        if t <= 1:
            for a in ACTIONS:
                lookup[(h, a)] = pred_y_C(bx, a)
    train_exact = all(
        lookup[(h, a)] == pred_y_C(bx, a)
        for t, h, bx, bn, q in states if t <= 1 for a in ACTIONS
    )
    heldout_total = heldout_defined = 0
    for t, h, bx, bn, q in states:
        if t == 2:
            for a in ACTIONS:
                heldout_total += 1
                heldout_defined += int((h, a) in lookup)

    qvals = sorted({q for *_, q in states})
    result = {
        "toy": "Toy C v0.2",
        "horizon_enumerated": H,
        "reachable_history_counts": {str(k): v for k, v in sorted(counts.items())},
        "task_query_equivalence_B_C_E": {
            "all_exact_checks_pass": bool(exact),
            "representation_and_history_recompute_checks": rep_checks,
            "one_step_Y_prediction_checks": one_checks,
            "recursive_update_checks_B_vs_C": update_checks,
            "decision_query_checks": decision_checks,
            "branch_conditioned_length2_checks_B_vs_C": branch_checks,
            "open_loop_action_sequence_checks_B_C_E": open_checks,
        },
        "nontrivial_predictive_quotient": {
            "full_belief_coordinates": "(bX,bN)",
            "predictive_state_coordinate": "q=P(Y_next=1 | h, STAY)",
            "distinct_q_values": len(qvals),
            "same_q_different_bN_pairs": collision_pairs,
            "max_task_Y_alias_gap_within_q_cell": fstr(max_y_gap),
            "max_nuisance_Z_next_alias_gap_within_q_cell": fstr(max_z_gap),
            "witness": None if example is None else {
                "time": example[0],
                "q": fstr(example[1]),
                "history_1": repr(example[2]),
                "bN_1": fstr(example[3]),
                "P_Znext1_1": fstr(example[4]),
                "history_2": repr(example[5]),
                "bN_2": fstr(example[6]),
                "P_Znext1_2": fstr(example[7]),
            },
            "interpretation": "q is sufficient for Q_task but provably not sufficient for the broader nuisance query Z_next; this is a query-relative quotient, not a reconstruction of the full hidden ontology."
        },
        "agent_E_direct_history_model": {
            "persistent_recursive_state": False,
            "owns_XY_transition_observation_structure": True,
            "recomputes_from_full_history_per_query": True,
            "open_loop_exact_checks": open_checks,
            "interpretation": "Persistent recursive state storage is not required to answer the declared future action-sequence queries exactly in this finite construction. This challenges a strong reading of H2, but does not settle terminology about world-modelhood."
        },
        "lookup_control_D": {
            "training_support_time_depth": "<=1",
            "training_entries": len(lookup),
            "exact_on_training_support": bool(train_exact),
            "heldout_time_depth": 2,
            "heldout_queries": heldout_total,
            "heldout_queries_defined": heldout_defined,
            "heldout_coverage": f"{heldout_defined}/{heldout_total}",
        },
        "agent_A_structural_fact": {
            "exact_current_full_belief": True,
            "owns_future_generating_operator": False,
            "owns_rollout_operator": False,
            "note": "Exact current epistemic state is intentionally separated from possession of a future-query mechanism."
        },
        "hypothesis_status": {
            "H1_sufficiency_alone_insufficient": "supported as an architectural separation example, not a terminology theorem",
            "H2_recursive_closure_necessary": "weakened/counterexample candidate: Agent E is exact without persistent recursive state",
            "H3_action_indexed_future_consequences": "survives this toy as the common capability of B,C,E",
            "H4_breadth_as_profile_frontier": "supported by exact Q_task sufficiency and exact failure of q for nuisance Z prediction"
        },
        "scope": {
            "establishes": [
                "For Q_task, a one-dimensional predictive state is exactly equivalent to the full generative model for the tested prediction/update/decision/rollout queries.",
                "The one-dimensional predictive state is a non-injective quotient of the full two-coordinate belief: histories can share q while differing in nuisance belief bN.",
                "The same q-cell can have zero aliasing for the task query Y and positive aliasing for the broader nuisance query Z.",
                "A direct-history model can answer the same declared future action-sequence queries exactly without storing a persistent recursively updated state.",
                "Finite one-step lookup fit on memorized support still provides no held-out compositional coverage."
            ],
            "does_not_establish": [
                "A necessary-and-sufficient definition of world model.",
                "That recursive computation is never useful or that no internal sufficient statistic is formed transiently by Agent E.",
                "Independent causal/interventional validity beyond the declared action semantics.",
                "Robustness under regime shift.",
                "That Q_task is broad enough to deserve the word world in world model."
            ]
        }
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
