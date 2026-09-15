#!/usr/bin/env python3
"""Executable verification for the L0/L1b/L2/L3 v0.4 framework spine.

Changes from v0.3:
  * behaviour-policy exposure is no longer an independent L1 axis;
    delta_inv^latent is reported only through rho_pol = delta_inv/delta_alias;
  * a minimal witness makes rho_pol non-vacuous under a restricted B;
  * every horizon-indexed budget carries case counts;
  * empty case sets return NOT_APPLICABLE, never a perfect zero;
  * Toy A and Toy B remain exactly enumerable and unchanged in substance.

TV convention:
    d_TV(mu, nu) = sum_x |mu(x)-nu(x)|
(the L1 convention used in the reviewed package; halve for half-normalised TV).
"""
from __future__ import annotations
import itertools
import json
import csv
from pathlib import Path

OUTDIR = Path(__file__).resolve().parent
MODES = (0, 1)
PRIOR = {0: 0.5, 1: 0.5}

def tv(p, q):
    keys = set(p) | set(q)
    return sum(abs(p.get(k, 0.0) - q.get(k, 0.0)) for k in keys)

def mix(weights, laws):
    out = {}
    for w, law in zip(weights, laws):
        for k, p in law.items():
            out[k] = out.get(k, 0.0) + w * p
    return out

# ---------------------------------------------------------------------------
# TOY A: L0 pass at A_phase, L2 contingent fail
# ---------------------------------------------------------------------------

def actions_phase(phase):
    if phase == "u":
        return ("commit0", "commit1", "probe")
    if phase == "r":
        return ("commit0", "commit1")
    return ()

def step_probe(mode, phase, action, c):
    if action == "probe":
        assert phase == "u"
        return "r", str(mode), -c
    assert action in ("commit0", "commit1")
    tgt = int(action[-1])
    return "T", "-", float(mode == tgt)

HIST = {
    (): "u",
    (("probe", "0"),): "r",
    (("probe", "1"),): "r",
}

def true_phase(hist):
    return HIST[hist]

def modes_consistent(hist):
    if hist == ():
        return [0, 1]
    return [int(hist[0][1])]

def sigma_C(hist):
    return true_phase(hist)

K_C = {
    ("u", "probe"): {"r": 1.0},
    ("u", "commit0"): {"T": 1.0},
    ("u", "commit1"): {"T": 1.0},
    ("r", "commit0"): {"T": 1.0},
    ("r", "commit1"): {"T": 1.0},
}

def projected_next_law(hist, action, c):
    ms = modes_consistent(hist)
    law = {}
    for m in ms:
        nph, _, _ = step_probe(m, true_phase(hist), action, c)
        law[nph] = law.get(nph, 0.0) + 1.0 / len(ms)
    return law

def compose_K(z, seq):
    law = {z: 1.0}
    for a in seq:
        nxt = {}
        for zz, w in law.items():
            if (zz, a) not in K_C:
                return None
            for z2, p in K_C[(zz, a)].items():
                nxt[z2] = nxt.get(z2, 0.0) + w * p
        law = nxt
    return law

def true_k_step_latent_law(hist, seq, c):
    law = {}
    ms = modes_consistent(hist)
    for m in ms:
        ph = true_phase(hist)
        for a in seq:
            if a not in actions_phase(ph):
                return None
            ph, _, _ = step_probe(m, ph, a, c)
        law[ph] = law.get(ph, 0.0) + 1.0 / len(ms)
    return law

def true_k_step_query_law(hist, seq, c, query):
    law = {}
    ms = modes_consistent(hist)
    for m in ms:
        ph = true_phase(hist)
        for a in seq:
            if a not in actions_phase(ph):
                return None
            ph, _, _ = step_probe(m, ph, a, c)
        val = ph if query == "phase" else m
        law[val] = law.get(val, 0.0) + 1.0 / len(ms)
    return law

def admissible_sequences(hist, k):
    if k == 0:
        return [()]
    alphabet = ("commit0", "commit1", "probe")
    out = []
    for seq in itertools.product(alphabet, repeat=k):
        ph = true_phase(hist)
        ok = True
        for a in seq:
            if a not in actions_phase(ph):
                ok = False
                break
            ph = "r" if (ph == "u" and a == "probe") else "T"
        if ok:
            out.append(seq)
    return out

def delta_alias(c):
    vals = []
    for h1, h2 in itertools.combinations(HIST, 2):
        if sigma_C(h1) != sigma_C(h2):
            continue
        common = set(actions_phase(true_phase(h1))) & set(actions_phase(true_phase(h2)))
        for a in common:
            vals.append(tv(projected_next_law(h1,a,c),
                           projected_next_law(h2,a,c)))
    return {
        "error": max(vals) if vals else None,
        "case_count": len(vals),
        "status": "PASS" if vals and max(vals) == 0.0 else ("NOT_APPLICABLE" if not vals else "MEASURED"),
    }

def delta_fit(c):
    vals = []
    for h in HIST:
        for a in actions_phase(true_phase(h)):
            vals.append(tv(projected_next_law(h,a,c), K_C[(sigma_C(h),a)]))
    return {
        "error": max(vals) if vals else None,
        "case_count": len(vals),
        "status": "PASS" if vals and max(vals) == 0.0 else ("NOT_APPLICABLE" if not vals else "MEASURED"),
    }

def delta_roll(c, k):
    vals = []
    for h in HIST:
        for seq in admissible_sequences(h,k):
            truth = true_k_step_latent_law(h,seq,c)
            model = compose_K(sigma_C(h),seq)
            if truth is None or model is None:
                continue
            vals.append(tv(truth,model))
    return {
        "error": max(vals) if vals else None,
        "case_count": len(vals),
        "status": "NOT_APPLICABLE" if not vals else ("PASS" if max(vals)==0.0 else "MEASURED"),
    }

def eta_query(c, query, k):
    """Return error plus audit counts.

    'query_bearing_case_count' counts cases whose starting history resolves the
    hidden mode when query == 'mode'. It prevents a zero error at long horizons
    from being read as improved mode decodability after all such histories have
    terminated and dropped out of the case set.
    """
    cases = []
    bearing = 0
    for h in HIST:
        seqs = admissible_sequences(h,k)
        for seq in seqs:
            truth = true_k_step_query_law(h,seq,c,query)
            model = compose_K(sigma_C(h),seq)
            if truth is None or model is None:
                continue
            cases.append((model,truth))
            if query != "mode" or len(modes_consistent(h)) == 1:
                bearing += 1

    if not cases:
        return {
            "error": None,
            "case_count": 0,
            "query_bearing_case_count": 0,
            "status": "NOT_APPLICABLE",
            "interpretation": "empty admissible case set",
        }

    if query == "phase":
        worst = 0.0
        for model,truth in cases:
            worst = max(worst,tv(dict(model),truth))
        return {
            "error": worst,
            "case_count": len(cases),
            "query_bearing_case_count": len(cases),
            "status": "PASS" if worst==0.0 else "MEASURED",
        }

    # For the abstraction-frontier claim we only interpret mode retention when
    # at least one mode-resolving starting history remains in the case set.
    grid = [i/100 for i in range(101)]
    latents = ("u","r","T")
    best = float("inf")
    for pu in grid:
        for pr in grid:
            for pT in grid:
                head = {
                    "u": {0:pu,1:1-pu},
                    "r": {0:pr,1:1-pr},
                    "T": {0:pT,1:1-pT},
                }
                worst = 0.0
                for model,truth in cases:
                    pred = {}
                    for z,w in model.items():
                        for v,p in head[z].items():
                            pred[v] = pred.get(v,0.0)+w*p
                    worst = max(worst,tv(pred,truth))
                    if worst >= best:
                        break
                best = min(best,worst)

    if bearing == 0:
        return {
            "error": best,
            "case_count": len(cases),
            "query_bearing_case_count": 0,
            "status": "NOT_INFORMATIVE",
            "interpretation": "no mode-resolving starting history remains; do not read the zero as improved decodability",
        }

    return {
        "error": best,
        "case_count": len(cases),
        "query_bearing_case_count": bearing,
        "status": "FAIL" if best > 0.0 else "PASS",
    }

def value_history_policy(pi,c):
    total = 0.0
    for m in MODES:
        h,ph,ret = (), "u", 0.0
        while ph != "T":
            a = pi[h]
            nph,obs,r = step_probe(m,ph,a,c)
            ret += r
            if a == "probe":
                h = h + ((a,obs),)
            ph = nph
        total += PRIOR[m]*ret
    return total

def all_history_policies():
    for a0 in ("commit0","commit1","probe"):
        for ar0 in ("commit0","commit1"):
            for ar1 in ("commit0","commit1"):
                yield {():a0,(("probe","0"),):ar0,(("probe","1"),):ar1}

def all_coarse_policies():
    for a0 in ("commit0","commit1","probe"):
        for ar in ("commit0","commit1"):
            yield {():a0,(("probe","0"),):ar,(("probe","1"),):ar}

def minimax_reward_error(phase,c):
    worst = 0.0
    for a in actions_phase(phase):
        vals = []
        for h in HIST:
            if true_phase(h) != phase:
                continue
            ms = modes_consistent(h)
            vals.append(sum((1/len(ms))*step_probe(m,phase,a,c)[2] for m in ms))
        worst = max(worst,(max(vals)-min(vals))/2)
    return worst

def run_toy_a():
    c0 = 0.10
    da = delta_alias(c0)
    df = delta_fit(c0)
    dr = {str(k):delta_roll(c0,k) for k in (1,2,3)}
    ep = {str(k):eta_query(c0,"phase",k) for k in (0,1,2,3)}
    em = {str(k):eta_query(c0,"mode",k) for k in (0,1,2,3)}

    grid = []
    for i in range(61):
        c = i/100
        vh = max(value_history_policy(p,c) for p in all_history_policies())
        vc = max(value_history_policy(p,c) for p in all_coarse_policies())
        analytic = max(0.0,0.5-c)
        grid.append({
            "c":round(c,2),
            "V_history":vh,
            "V_coarse":vc,
            "regret":vh-vc,
            "analytic_regret":analytic,
        })
    mismatch = [r for r in grid if abs(r["regret"]-r["analytic_regret"])>1e-12]
    point = next(r for r in grid if r["c"]==0.10)
    eps_u = minimax_reward_error("u",c0)
    eps_r = minimax_reward_error("r",c0)

    return {
        "L0_phase_frontier": {
            "delta_alias": da,
            "delta_fit": df,
            "delta_roll": dr,
            "eta_q_phase": ep,
            "eta_q_mode_if_added": em,
            "frontier_statement": "A_phase passes; A_phase+mode fails at k=0 and k=1. k>=2 is not used to infer recovery when mode-bearing histories have left the case set.",
        },
        "L2_contingent": {
            "history_policies_enumerated": len(list(all_history_policies())),
            "coarse_policies_enumerated": len(list(all_coarse_policies())),
            "point_c_0.10": point,
            "grid_mismatches": mismatch,
            "AP1_reward_error_u": eps_u,
            "AP1_reward_error_r": eps_r,
            "AIS_alpha_1_diagnostic": eps_u+eps_r,
            "AIS_policy_bound_2alpha_diagnostic": 2*(eps_u+eps_r),
            "certification": "L2 failure is certified directly by positive regret rather than inferred from failure of an AIS sufficient-condition bound.",
        },
        "grid": grid,
    }

# ---------------------------------------------------------------------------
# TOY B: L2.G-VE pass while L0 fails
# ---------------------------------------------------------------------------

XS=(0,1)
NS=(0,1,2,3)
ACTS=("stay","flip")

def reward_noisy(x,n,a):
    return 1.0 if x==1 else 0.0

def true_noisy_next(x,n,a):
    nx=x if a=="stay" else 1-x
    return {(nx,nn):0.25 for nn in NS}

def model_noisy_next(x,n,a):
    nx=x if a=="stay" else 1-x
    return {(nx,0):1.0}

def x_pushforward(kernel):
    out={}
    for (x,n),p in kernel.items():
        out[x]=out.get(x,0.0)+p
    return out

def all_stationary_policies():
    states=[(x,n) for x in XS for n in NS]
    for bits in itertools.product(ACTS,repeat=len(states)):
        yield dict(zip(states,bits))

def bellman(pi,V,kernel,gamma=0.9):
    out={}
    for x in XS:
        for n in NS:
            a=pi[(x,n)]
            exp=sum(p*V[s2] for s2,p in kernel(x,n,a).items())
            out[(x,n)]=reward_noisy(x,n,a)+gamma*exp
    return out

def run_toy_b():
    full=max(tv(true_noisy_next(x,n,a),model_noisy_next(x,n,a))
             for x in XS for n in NS for a in ACTS)
    xerr=max(tv(x_pushforward(true_noisy_next(x,n,a)),
                x_pushforward(model_noisy_next(x,n,a)))
             for x in XS for n in NS for a in ACTS)
    basis=[
        {(x,n):1.0 if x==0 else 0.0 for x in XS for n in NS},
        {(x,n):1.0 if x==1 else 0.0 for x in XS for n in NS},
    ]
    worst=0.0
    count=0
    for pi in all_stationary_policies():
        count+=1
        for V in basis:
            bt=bellman(pi,V,true_noisy_next)
            bm=bellman(pi,V,model_noisy_next)
            worst=max(worst,max(abs(bt[s]-bm[s]) for s in bt))
    return {
        "L0":{"delta_fit_full_state":full,"x_only_pushforward_error":xerr,
              "status":"FAIL for any budget < 1.5 under L1-TV"},
        "L2_G_VE":{"declared_value_class":"V_x={V:V(x,n)=v(x)}",
                   "policies_enumerated":count,
                   "basis_functions_checked":len(basis),
                   "max_bellman_gap":worst,
                   "status":"PASS exactly"},
    }

# ---------------------------------------------------------------------------
# L0 attribution diagnostic: policy-exposed aliasing
# ---------------------------------------------------------------------------

def policy_exposure_witness():
    """Two histories in one latent cell with distinct successor laws.

    Restricted B uses mixture weights p in {0.25,0.75}; rich B uses vertices
    p in {0,1}. Under L1-TV, delta_alias=2.
    """
    laws=[{"A":1.0},{"B":1.0}]
    d_alias=tv(laws[0],laws[1])

    def d_inv_for(ps):
        kernels={p:mix([p,1-p],laws) for p in ps}
        vals=[tv(kernels[p],kernels[q]) for p,q in itertools.combinations(ps,2)]
        return max(vals) if vals else 0.0

    d_restricted=d_inv_for((0.25,0.75))
    d_rich=d_inv_for((0.0,1.0))
    return {
        "delta_alias":d_alias,
        "restricted_B":{"mixture_weights":[0.25,0.75],
                        "delta_inv_latent":d_restricted,
                        "rho_pol":d_restricted/d_alias},
        "rich_B":{"mixture_weights":[0.0,1.0],
                  "delta_inv_latent":d_rich,
                  "rho_pol":d_rich/d_alias},
        "bound_checked":"0 <= delta_inv_latent <= delta_alias; rho_pol is defined only when delta_alias>0",
        "interpretation":"rho_pol is an attribution ratio for how much existing L0 aliasing can be exposed by the declared behaviour-policy class; it is not an independent world-model axis.",
    }

def main():
    A=run_toy_a()
    B=run_toy_b()
    W=policy_exposure_witness()
    out={
        "metric_convention":"TV/IPM uses L1 convention sum|p-q|; halve for half-normalised TV",
        "toy_A_L0_pass_L2_fail":A,
        "toy_B_L2_pass_L0_fail":B,
        "policy_exposure_attribution":W,
        "scope":"Finite toys establish L0/L2 non-identity. They do not establish non-collinearity in a non-degenerate regime.",
    }
    (OUTDIR/"04_RESULTS_V0_4.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
    with (OUTDIR/"04_TOY_A_GRID_V0_4.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["c","V_history","V_coarse","regret","analytic_regret"])
        w.writeheader(); w.writerows(A["grid"])
    print(json.dumps({
        "toy_A":{k:v for k,v in A.items() if k!="grid"},
        "toy_B":B,
        "policy_exposure_attribution":W,
    },indent=2))

if __name__=="__main__":
    main()
