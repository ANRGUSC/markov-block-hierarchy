# Theorem 8 · Positive variance limit

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

For $0<p<1/2$ prove uniform convergence of $\omega_k(\tau)$ to a continuous limit with error $(1+\sqrt2)\sqrt{\rho/k}$ for $\tau\ge0$, zero at the origin and positive elsewhere. At differentiable $0<D<1/2$ prove the positive fixed-distortion limit in bits squared per symbol.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L531-L540). Its notation and units govern throughout.

**Background used.** Lemma 7, the finite-alphabet convex rate–distortion duality used in Section 5, and supporting calculations C and D. Step 5 imports the gain argument in Corollary 9 using only step 3 of this proof.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L531–540](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L531-L540) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L542–543](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L542-L543) | Reduce the common-slope estimate to one cut. | ⟨2⟩1 |
| SRC-002 | [L744–749](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L744-L749) | Sum along dyadic lengths. | ⟨2⟩2 |
| SRC-003 | [L750–754](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L750-L754) | Identify the dyadic limits for every starting length. | ⟨2⟩3 |
| SRC-004 | [L755–756](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L755-L756) | Check continuity, including zero. | ⟨2⟩4 |
| SRC-005 | [L542–543](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L542-L543) | Establish strict positivity at a common slope. | ⟨2⟩5 |
| SRC-006 | [L545–551](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L545-L551) | Control the objective and optimizing slopes. | ⟨2⟩6 |
| SRC-007 | [L549–550](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L549-L550) | Select the limiting slope at fixed distortion. | ⟨2⟩7 |
| SRC-008 | [L549–550](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L549-L550) | Return to the variance in bits. | ⟨2⟩8 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Reduce the common-slope estimate to one cut.** Write $\sigma_n=\sqrt n\,\omega_n$. Lemma 7 and the reverse triangle inequality give $|\sigma_{n+k}-(\sigma_n^2+\sigma_k^2)^{1/2}|\le B$, with $B=\sqrt\rho$.

**⟨2⟩2. Sum along dyadic lengths.** Doubling changes $\omega_n$ by at most $B/\sqrt{2n}$. The telescoping geometric bound is $(1+\sqrt2)B/\sqrt n$.

**⟨2⟩3. Identify the dyadic limits for every starting length.** Join $t$ equal pieces of length $2^j n$. The unnormalized error is at most $(t-1)B$ because $x\mapsto\sqrt{x^2+c^2}$ is 1-Lipschitz on $x\ge0$. Divide by $\sqrt{t2^jn}$ and send $j$ to infinity.

**⟨2⟩4. Check continuity, including zero.** Compactness and uniqueness give continuity for each finite optimizer at positive $\tau$. The score is between zero and $k\tau$, so $\omega_k$ tends to zero at the origin for each fixed $k$. Uniform convergence preserves continuity.

**⟨2⟩5. Establish strict positivity at a common slope.** Appendix B.2 bounds the gain from joining blocks on both sides, yielding the positive lower bound for $\omega_\infty(\tau)$ at $\tau>0$.

**⟨2⟩6. Control the objective and optimizing slopes.** The one-cut mean bound yields $0\le f_k-f\le J_0/k$. Finite duality gives the maximizing objective $f_k(\tau)-\tau D$. A uniform prior and the value at zero confine every maximizer to $[0,\ln 2/D]$.

**⟨2⟩7. Select the limiting slope at fixed distortion.** At a differentiability point every limiting maximizer equals $\tau(D)=-(\ln2)R'(D)$. Appendix B.2 gives a strictly positive lower bound at this interior distortion.

**⟨2⟩8. Return to the variance in bits.** Use $\tau_K\to\tau(D)$, uniform approximation at $\tau_K$, and continuity at $\tau(D)$. Then $v_K(D)=\omega_K(\tau_K)^2/(\ln2)^2$ tends to the claimed positive limit.

**⟨2⟩9. Q.E.D.** By ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7, ⟨2⟩8 under the assumptions of ⟨1⟩1.

**⟨1⟩2. Q.E.D.** By ⟨1⟩1.

<details><summary>Mapping ledger and frozen audit handoff</summary>

| Item | Source | Mapping | Support |
|---|---|---|---|
| Statement | Contract | NORMALIZED | EXPLICIT |
| ⟨1⟩1 | Contract | STRUCTURAL | IMPLICIT |
| ⟨2⟩1 | SRC-001 | NORMALIZED | EXPLICIT |
| ⟨2⟩2 | SRC-002 | NORMALIZED | EXPLICIT |
| ⟨2⟩3 | SRC-003 | NORMALIZED | EXPLICIT |
| ⟨2⟩4 | SRC-004 | NORMALIZED | EXPLICIT |
| ⟨2⟩5 | SRC-005 | NORMALIZED | EXPLICIT |
| ⟨2⟩6 | SRC-006 | NORMALIZED | EXPLICIT |
| ⟨2⟩7 | SRC-007 | NORMALIZED | EXPLICIT |
| ⟨2⟩8 | SRC-008 | NORMALIZED | EXPLICIT |
| ⟨2⟩9, ⟨1⟩2 | Contract and closing claims ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7, ⟨2⟩8 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 11 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Reduce the common-slope estimate to one cut. | Contract and stated background | The comparison is under the true law. Independent short scores add their variances and centering contracts the error in $L^2$. | OK |
| ⟨2⟩2 · Sum along dyadic lengths. | ⟨2⟩1 | This first supplies a limit for each dyadic sequence at fixed $\tau$. The error bound contains no $\tau$. | OK |
| ⟨2⟩3 · Identify the dyadic limits for every starting length. | ⟨2⟩1, ⟨2⟩2 | For fixed integers $t,n$ this equates the limits from $tn$ and $n$. Taking $n=1$ gives a single limit. The dyadic tail estimate now bounds each original $\omega_k$. | OK |
| ⟨2⟩4 · Check continuity, including zero. | ⟨2⟩3 | The bound $\sqrt{k}\tau$ is needed only at fixed $k$. Uniform convergence comes from the cut estimate, so continuity at zero requires no unique optimum at $\tau=0$. | OK |
| ⟨2⟩5 · Establish strict positivity at a common slope. | ⟨2⟩3 | Use steps 1–5 of the Corollary 9 companion. That argument uses only the common-slope convergence from step 3, so the dependency does not loop through fixed-distortion positivity. | OK |
| ⟨2⟩6 · Control the objective and optimizing slopes. | Contract and stated background | Apply the rate-bracket argument to penalized costs. Uniform convergence on the compact interval lets the maxima converge to $R(D)\ln2$ and puts every cluster point in the limiting maximizing set. | OK |
| ⟨2⟩7 · Select the limiting slope at fixed distortion. | ⟨2⟩6 | For a maximizing slope the affine dual term supports the rate as a function of distortion. The positive rate lower bound and the zero rate at $1/2$ exclude slope zero. See supporting calculations for the martingale estimate. | OK |
| ⟨2⟩8 · Return to the variance in bits. | ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7 | Centering removes the deterministic tilt. Squaring and conversion from nats are performed after taking the standard-deviation limit. This conclusion contains no coding achievability assertion. | OK |
| ⟨2⟩9 · local conclusion | ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7, ⟨2⟩8 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7, ⟨2⟩8. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7, ⟨2⟩8 | Root, by local closure | Discharged |
| ⟨2⟩1 · Reduce the common-slope estimate to one cut. | ⟨2⟩2, ⟨2⟩3 | P1 | Major claim, SRC-001 | Discharged |
| P1 · The comparison is under the true law. Independent short scores add their variances and centering contracts the error in $L^2$. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Sum along dyadic lengths. | ⟨2⟩3 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · This first supplies a limit for each dyadic sequence at fixed $\tau$. The error bound contains no $\tau$. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Identify the dyadic limits for every starting length. | ⟨2⟩4, ⟨2⟩5, ⟨2⟩8, C0 | ⟨2⟩1, ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · For fixed integers $t,n$ this equates the limits from $tn$ and $n$. Taking $n=1$ gives a single limit. The dyadic tail estimate now bounds each original $\omega_k$. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Check continuity, including zero. | ⟨2⟩8, C0 | ⟨2⟩3, P4 | Major claim, SRC-004 | Discharged |
| P4 · The bound $\sqrt{k}\tau$ is needed only at fixed $k$. Uniform convergence comes from the cut estimate, so continuity at zero requires no unique optimum at $\tau=0$. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩5 · Establish strict positivity at a common slope. | ⟨2⟩8, C0 | ⟨2⟩3, P5 | Major claim, SRC-005 | Discharged |
| P5 · Use steps 1–5 of the Corollary 9 companion. That argument uses only the common-slope convergence from step 3, so the dependency does not loop through fixed-distortion positivity. | ⟨2⟩5 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩6 · Control the objective and optimizing slopes. | ⟨2⟩7 | P6 | Major claim, SRC-006 | Discharged |
| P6 · Apply the rate-bracket argument to penalized costs. Uniform convergence on the compact interval lets the maxima converge to $R(D)\ln2$ and puts every cluster point in the limiting maximizing set. | ⟨2⟩6 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩7 · Select the limiting slope at fixed distortion. | ⟨2⟩8, C0 | ⟨2⟩6, P7 | Major claim, SRC-007 | Discharged |
| P7 · For a maximizing slope the affine dual term supports the rate as a function of distortion. The positive rate lower bound and the zero rate at $1/2$ exclude slope zero. See supporting calculations for the martingale estimate. | ⟨2⟩7 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩8 · Return to the variance in bits. | C0 | ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩7, P8 | Major claim, SRC-008 | Discharged |
| P8 · Centering removes the deterministic tilt. Squaring and conversion from nats are performed after taking the standard-deviation limit. This conclusion contains no coding achievability assertion. | ⟨2⟩8 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
