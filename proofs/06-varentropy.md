# Theorem 6 · Finite-block varentropy

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

Take any positive stationary two-state chain. At each length choose a distortion on the branch where the entropy equality and its stated score apply. The target is the exact variance, its per-symbol limit and the first correction for $0<|\rho|<1$.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L450-L463). Its notation and units govern throughout.

**Background used.** The Markov chain rule, the two-state transition operator, elementary covariance algebra, and the branch hypothesis in the statement.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L450–463](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L450-L463) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L450–453](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L450-L453) | Decompose the information. | ⟨2⟩1 |
| SRC-002 | [L464–466](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L464-L466) | Propagate the two covariances. | ⟨2⟩2 |
| SRC-003 | [L454–466](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L454-L466) | Count pairs at each lag. | ⟨2⟩3 |
| SRC-004 | [L457–467](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L457-L467) | Extract the limit and correction. | ⟨2⟩4 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Decompose the information.** The lossless score is $B_0+\sum_{t=1}^{K-1}A_t$. On the stated branch the tilted score differs only by a deterministic constant.

**⟨2⟩2. Propagate the two covariances.** Condition at the end of the first edge. For $h\ge1$, $\operatorname{Cov}(A_1,A_{1+h})=\rho^{h-1}\gamma$. For $h\ge0$, $\operatorname{Cov}(B_0,A_{1+h})=\rho^h\kappa$.

**⟨2⟩3. Count pairs at each lag.** Set $N=K-1$. Obtain $\operatorname{Var}B_0+Ns^2+2\gamma\sum_{h=1}^{N-1}(N-h)\rho^{h-1}+2\kappa\sum_{h=0}^{N-1}\rho^h$.

**⟨2⟩4. Extract the limit and correction.** The limit is $\sigma_X^2=s^2+2\gamma/(1-\rho)$. For nonzero $\rho$, expanding the two sums gives $c_*=\operatorname{Var}B_0-s^2+2\kappa/(1-\rho)-2\gamma[(1-\rho)^{-1}+(1-\rho)^{-2}]$.

**⟨2⟩5. Q.E.D.** By ⟨2⟩1, ⟨2⟩3, ⟨2⟩4 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩5, ⟨1⟩2 | Contract and closing claims ⟨2⟩1, ⟨2⟩3, ⟨2⟩4 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS WITH MINOR ISSUES.** The variance calculation closes on the specified branch. The choice of slope at a biased zero-rate endpoint should be explicit when applying it.

The theorem contract above is the forward goal. There are two levels and 7 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Decompose the information. | Contract and stated background | Here $B_0=-\log_2\pi_{X_1}$ and $A_t=-\log_2P_{X_tX_{t+1}}$. No assumption of independence between transition scores is used. | MINOR |
| ⟨2⟩2 · Propagate the two covariances. | ⟨2⟩1 | A centered function of a binary state spans a one-dimensional space on which $P$ acts by $\rho$. The edge-to-edge gap uses $h-1$ transitions; the initial state to edge gap uses $h$. | OK |
| ⟨2⟩3 · Count pairs at each lag. | ⟨2⟩1, ⟨2⟩2 | There are $N-h$ edge pairs at lag $h$ and one initial-state pair per edge. At $K=1$ the sums and edge term vanish. | OK |
| ⟨2⟩4 · Extract the limit and correction. | ⟨2⟩3 | The weighted sum equals $N/(1-\rho)-(1-\rho^N)/(1-\rho)^2$ for $N\ge1$. The residual after division by $K$ is $O(\vert \rho\vert ^{K-1}/K)$. For independence the self-information is a sum of i.i.d. terms. See the separate endpoint note for the zero-slope convention. | OK |
| ⟨2⟩5 · local conclusion | ⟨2⟩1, ⟨2⟩3, ⟨2⟩4 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. For exposition, identify the interior or backward-channel slope explicitly at the first zero of the inverse prior. See supporting calculation A.4.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩1, ⟨2⟩3, ⟨2⟩4. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩1, ⟨2⟩3, ⟨2⟩4 | Root, by local closure | Discharged |
| ⟨2⟩1 · Decompose the information. | ⟨2⟩2, ⟨2⟩3, C0 | P1 | Major claim, SRC-001 | Discharged |
| P1 · Here $B_0=-\log_2\pi_{X_1}$ and $A_t=-\log_2P_{X_tX_{t+1}}$. No assumption of independence between transition scores is used. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Propagate the two covariances. | ⟨2⟩3 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · A centered function of a binary state spans a one-dimensional space on which $P$ acts by $\rho$. The edge-to-edge gap uses $h-1$ transitions; the initial state to edge gap uses $h$. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Count pairs at each lag. | ⟨2⟩4, C0 | ⟨2⟩1, ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · There are $N-h$ edge pairs at lag $h$ and one initial-state pair per edge. At $K=1$ the sums and edge term vanish. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Extract the limit and correction. | C0 | ⟨2⟩3, P4 | Major claim, SRC-004 | Discharged |
| P4 · The weighted sum equals $N/(1-\rho)-(1-\rho^N)/(1-\rho)^2$ for $N\ge1$. The residual after division by $K$ is $O(\vert \rho\vert ^{K-1}/K)$. For independence the self-information is a sum of i.i.d. terms. See the separate endpoint note for the zero-slope convention. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
