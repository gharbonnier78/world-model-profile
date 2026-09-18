#!/usr/bin/env python3
"""
Toy C v0.1 — State sufficiency vs model structure.

Exact finite verification using fractions only.

Environment
-----------
Hidden state S_t in {0,1}.
Observation O_t in {0,1} with P(O_t = S_t)=3/4.
Action 0: identity transition.
Action 1: stochastic anti-persistence:
    P(S_{t+1}=1 | S_t=1,a=1)=1/4
    P(S_{t+1}=1 | S_t=0,a=1)=3/4

Agent C keeps the Bayesian belief b_t=P(S_t=1|h_t) and the full
transition/observation model.

Agent B keeps the predictive state
    q_t=P(O_{t+1}=1 | h_t, a_t=0)
and updates/predicts directly in q-space. It never needs an explicit hidden
state at runtime.

Agent A receives the exact current belief from an oracle but has no transition,
observation, update, or rollout operator. Its online state estimate is exact,
but future-query interfaces are intentionally absent.

Control D is a finite one-step lookup table populated only on training support.
It is exact on that support but undefined on held-out histories. This is a
support/generalization control, not a proof about modelhood.
"""

from fractions import Fraction
from itertools import product
import json

F = Fraction


def fstr(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def obs_prob1_from_b(b):
    return F(1, 4) + F(1, 2) * b


def trans_b(b, a):
    if a == 0:
        return b
    return F(1, 4) * b + F(3, 4) * (1 - b)


def pred_obs1_C(b, a):
    return obs_prob1_from_b(trans_b(b, a))


def bayes_b(prior_b, o):
    if o == 1:
        num = F(3, 4) * prior_b
        den = num + F(1, 4) * (1 - prior_b)
    else:
        num = F(1, 4) * prior_b
        den = num + F(3, 4) * (1 - prior_b)
    return num / den


def update_C(b, a, o):
    return bayes_b(trans_b(b, a), o)


def q_from_b(b):
    return obs_prob1_from_b(b)


def b_from_q(q):
    return 2 * q - F(1, 2)


def pred_obs1_B(q, a):
    if a == 0:
        return q
    return F(3, 4) - F(1, 2) * q


def update_B(q, a, o):
    r = pred_obs1_B(q, a)
    if o == 1:
        return 1 - F(3, 16) / r
    return F(3, 16) / (1 - r)


def initial_b(o0):
    return bayes_b(F(1, 2), o0)


def enumerate_reachable(H):
    states = []
    for o0 in (0, 1):
        b = initial_b(o0)
        q = q_from_b(b)
        hist = (o0,)
        states.append((0, hist, b, q))
        frontier = [(hist, b, q)]
        for t in range(H):
            new = []
            for hist, b, q in frontier:
                for a, o in product((0, 1), (0, 1)):
                    b2 = update_C(b, a, o)
                    q2 = update_B(q, a, o)
                    nh = hist + (a, o)
                    states.append((t + 1, nh, b2, q2))
                    new.append((nh, b2, q2))
            frontier = new
    return states


def branch_compose_C(b, action_obs_seq):
    for a, o in action_obs_seq:
        b = update_C(b, a, o)
    return b


def branch_compose_B(q, action_obs_seq):
    for a, o in action_obs_seq:
        q = update_B(q, a, o)
    return q


def open_loop_obs_C(b, actions):
    p = b
    for a in actions:
        p = trans_b(p, a)
    return obs_prob1_from_b(p)


def open_loop_obs_B(q, actions):
    r = q
    for a in actions:
        r = pred_obs1_B(r, a)
    return r


def expected_target_reward_C(b, a):
    return trans_b(b, a)


def expected_target_reward_B(q, a):
    if a == 0:
        return 2 * q - F(1, 2)
    return 1 - q


def greedy_action(vals):
    return 0 if vals[0] >= vals[1] else 1


def main():
    H = 4
    states = enumerate_reachable(H)

    counts_by_t = {}
    for t, _, _, _ in states:
        counts_by_t[t] = counts_by_t.get(t, 0) + 1

    rep_checks = 0
    one_step_checks = 0
    update_checks = 0
    decision_checks = 0
    all_exact = True

    for t, h, b, q in states:
        rep_checks += 1
        all_exact &= q == q_from_b(b)
        if t < H:
            for a in (0, 1):
                one_step_checks += 1
                all_exact &= pred_obs1_B(q, a) == pred_obs1_C(b, a)
                rc = {a_: expected_target_reward_C(b, a_) for a_ in (0, 1)}
                rb = {a_: expected_target_reward_B(q, a_) for a_ in (0, 1)}
                decision_checks += 1
                all_exact &= rc == rb
                all_exact &= greedy_action(rc) == greedy_action(rb)
                for o in (0, 1):
                    update_checks += 1
                    b2 = update_C(b, a, o)
                    q2 = update_B(q, a, o)
                    all_exact &= q2 == q_from_b(b2)

    branch_checks = 0
    for t, h, b, q in states:
        if t <= 1:
            for flat in product((0, 1), repeat=6):
                seq = list(zip(flat[0::2], flat[1::2]))
                bc = branch_compose_C(b, seq)
                qb = branch_compose_B(q, seq)
                branch_checks += 1
                all_exact &= qb == q_from_b(bc)

    open_loop_checks = 0
    for t, h, b, q in states:
        if t <= 1:
            for k in range(1, 5):
                for actions in product((0, 1), repeat=k):
                    pc = open_loop_obs_C(b, actions)
                    pb = open_loop_obs_B(q, actions)
                    open_loop_checks += 1
                    all_exact &= pc == pb

    lookup = {}
    for t, h, b, q in states:
        if t <= 1:
            for a in (0, 1):
                lookup[(h, a)] = pred_obs1_C(b, a)

    lookup_train_checks = 0
    lookup_train_exact = True
    for t, h, b, q in states:
        if t <= 1:
            for a in (0, 1):
                lookup_train_checks += 1
                lookup_train_exact &= lookup[(h, a)] == pred_obs1_C(b, a)

    heldout_total = 0
    heldout_defined = 0
    for t, h, b, q in states:
        if t == 2:
            for a in (0, 1):
                heldout_total += 1
                heldout_defined += int((h, a) in lookup)

    q_values = sorted({q for _, _, _, q in states})
    result = {
        "toy": "Toy C v0.1",
        "horizon_enumerated": H,
        "reachable_history_counts": {str(k): v for k, v in sorted(counts_by_t.items())},
        "exact_equivalence": {
            "all_checks_pass": bool(all_exact),
            "representation_checks": rep_checks,
            "one_step_prediction_checks": one_step_checks,
            "posterior_update_checks": update_checks,
            "decision_query_checks": decision_checks,
            "branch_conditioned_length3_checks": branch_checks,
            "open_loop_action_sequence_checks": open_loop_checks,
        },
        "predictive_state_range": {
            "min_q": fstr(min(q_values)),
            "max_q": fstr(max(q_values)),
            "distinct_q_values": len(q_values),
        },
        "lookup_control_D": {
            "training_support_time_depth": "<=1",
            "training_entries": len(lookup),
            "training_checks": lookup_train_checks,
            "exact_on_training_support": bool(lookup_train_exact),
            "heldout_time_depth": 2,
            "heldout_queries": heldout_total,
            "heldout_queries_defined": heldout_defined,
            "heldout_coverage": f"{heldout_defined}/{heldout_total}",
        },
        "agent_A_structural_fact": {
            "exact_current_belief": True,
            "owns_transition_operator": False,
            "owns_observation_operator": False,
            "owns_recursive_update_operator": False,
            "owns_rollout_operator": False,
            "note": "This is an architectural capability distinction, not a numerical error claim.",
        },
        "scope": {
            "establishes": [
                "In this finite process, explicit hidden-state ontology is not required for exact action-conditioned prediction, recursive update, rollout, or the declared one-step decision query.",
                "An exact current sufficient belief can be provided without providing a future-generating model.",
                "Exact one-step fit on finite training support does not by itself provide off-support compositional coverage.",
            ],
            "does_not_establish": [
                "A necessary-and-sufficient definition of world model.",
                "That recursive latent-state update is universally necessary for modelhood.",
                "Independent interventional validity beyond action conditioning; the action is the sole intervention point here.",
                "Robustness under distribution or regime shift.",
                "That the predictive state q is a nontrivial compression relative to belief; here it is an affine bijection.",
            ],
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
