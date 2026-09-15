#!/usr/bin/env python3
"""Exact verification for the illustrative diagnostics in Section 5.

The quantities are derived from the stated finite constructions. After the
derivation, explicit assertions pin the expected values as a non-regression
guard; those assertions are checks on the derived results, not their source.

No Monte Carlo estimation is used. Distances use the L1 total-variation/IPM
convention d(p,q)=sum_x |p(x)-q(x)|.
"""
from __future__ import annotations
import json
from pathlib import Path
OUTDIR = Path(__file__).resolve().parent

def l1(p, q):
    return sum(abs(p.get(k, 0.0) - q.get(k, 0.0)) for k in set(p) | set(q))

def mix(weights, laws):
    out = {}
    for w, law in zip(weights, laws):
        for k, v in law.items():
            out[k] = out.get(k, 0.0) + w * v
    return out

def rho_three_history():
    w = [0.5, 0.5, 0.0]
    wp = [0.0, 0.5, 0.5]
    spread = 0.5 * sum(abs(a-b) for a,b in zip(w,wp))
    geom1 = [{"A":1.0},{"B":1.0},{"C":1.0}]
    geom2 = [{"A":1.0},{"B":1.0},{"A":0.8,"B":0.2}]
    def evaluate(laws):
        alias = max(l1(laws[i], laws[j]) for i in range(3) for j in range(i+1, 3))
        exposed = round(l1(mix(w, laws), mix(wp, laws)), 12)
        rho = round(exposed/alias, 12)
        return {"delta_alias": alias, "delta_inv_latent": exposed, "rho_pol": rho}
    g1, g2 = evaluate(geom1), evaluate(geom2)
    assert abs(spread - 0.5) < 1e-12
    expected1={"delta_alias":2.0,"delta_inv_latent":1.0,"rho_pol":0.5}
    expected2={"delta_alias":2.0,"delta_inv_latent":0.2,"rho_pol":0.1}
    for key,val in expected1.items(): assert abs(g1[key]-val) < 1e-12
    for key,val in expected2.items(): assert abs(g2[key]-val) < 1e-12
    return {"behaviour_weights":{"w":w,"w_prime":wp},"half_L1_weight_spread":spread,"geometry_1":g1,"geometry_2":g2}

def l2_operational_witness():
    true_q={"safe":1.0,"unseen":2.0}; model_q={"safe":1.0,"unseen":0.0}
    planner_action=max(model_q,key=model_q.get)
    mu_pi={"safe":1.0,"unseen":0.0} if planner_action=="safe" else {"safe":0.0,"unseen":1.0}
    operational_error=sum(mu_pi[a]*abs(true_q[a]-model_q[a]) for a in true_q)
    uniform_off_prior_error=0.5*sum(abs(true_q[a]-model_q[a]) for a in true_q)
    global_best=max(true_q.values()); planner_true_value=true_q[planner_action]; regret=global_best-planner_true_value
    assert planner_action=="safe" and operational_error==0.0 and uniform_off_prior_error==1.0 and regret==1.0
    return {"true_returns":true_q,"model_returns":model_q,"planner_action":planner_action,"mu_Pi":mu_pi,"operational_absolute_error":operational_error,"uniform_off_prior_absolute_error":uniform_off_prior_error,"planner_true_value":planner_true_value,"global_optimal_true_value":global_best,"regret_vs_global_optimum":regret}

def main():
    out={"metric_convention":"L1 total-variation/IPM: sum_x |p(x)-q(x)|","rho_pol_three_history":rho_three_history(),"L2O_minimal_witness":l2_operational_witness()}
    (OUTDIR/'supporting_diagnostics_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
