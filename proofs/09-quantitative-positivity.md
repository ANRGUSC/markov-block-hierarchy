# Corollary 9 · Quantitative positivity

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

For the same persistent symmetric source and every $\tau>0$ prove $\omega_\infty(\tau)\ge \rho\sqrt{p(1-p)}\,L(\tau)^4/2$, with $L(\tau)=2\ln\cosh(\tau/2)/\tau$.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L556-L562). Its notation and units govern throughout.

**Background used.** Lemma 7 and the common-slope convergence portion of Theorem 8 (steps 1–3), data processing, the conditional entropy chain rule, Jensen and Cauchy–Schwarz.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L556–562](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L556-L562) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L761–765](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L761-L765) | Describe the two boundary spins. | ⟨2⟩1 |
| SRC-002 | [L765–768](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L765-L768) | Bound the joining gain from below. | ⟨2⟩2 |
| SRC-003 | [L770–776](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L770-L776) | Bound the summed gains from above. | ⟨2⟩3 |
| SRC-004 | [L778–782](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L778-L782) | Lower-bound the average boundary correlation. | ⟨2⟩4 |
| SRC-005 | [L783–783](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L783-L783) | Match the two cut sums. | ⟨2⟩5 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Describe the two boundary spins.** Let $b_k=E[X_kY_k]$ under the optimal length-$k$ channel. Reversal identifies the first and last correlations. Complement symmetry gives $E[Y_k\mid X_k]=b_kX_k$.

**⟨2⟩2. Bound the joining gain from below.** Run the short channels independently conditional on their input pieces. Their total penalized cost decreases by the mutual information of their output blocks. Data processing to the fair boundary output spins gives $G_{i,j}\ge\rho^2 b_i^2b_j^2/2$.

**⟨2⟩3. Bound the summed gains from above.** Replace one boundary flip by a fair flip and test the original prior. The objective increase is bounded by $(1/2-p)$ times the difference of conditional mean scores. Sum over cut locations and apply Cauchy–Schwarz with the total flip count.

**⟨2⟩4. Lower-bound the average boundary correlation.** Discarding a terminal spin gives $F_k-F_{k-1}\ge\tau(1-b_k)/2$. Sum from $1$ to $N$ and compare $F_N/N$ to the uniform-prior cost $-\ln[(1+e^{-\tau})/2]$.

**⟨2⟩5. Match the two cut sums.** Sum the lower bound over $1\le i,j\le N$. Jensen gives at least $\rho^2N^2L^4/2$. Those cuts form a subset of all cuts of lengths through $2N$, each gain nonnegative. Sum the upper bound and use common-slope convergence.

**⟨2⟩6. Q.E.D.** By ⟨2⟩5 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩6, ⟨1⟩2 | Contract and closing claims ⟨2⟩5 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 8 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Describe the two boundary spins. | Contract and stated background | Uniqueness at positive $\tau$ licenses both symmetries. The boundary source spins have correlation $\rho$ and their two side channels are conditionally independent. | OK |
| ⟨2⟩2 · Bound the joining gain from below. | ⟨2⟩1 | The concatenated channel is feasible. Fair spins of correlation $c=\rho b_i b_j$ have information $\ln 2-h((1-c)/2)\ge c^2/2$ in nats. | OK |
| ⟨2⟩3 · Bound the summed gains from above. | Contract and stated background | For Bernoulli $B_i$, the conditional difference equals $\operatorname{Cov}(\ell,B_i)/(p(1-p))$. Since $\operatorname{Var}T=(k-1)p(1-p)$, the upper bound is $(1/2-p)\sqrt{k(k-1)}\,\omega_k/\sqrt{p(1-p)}$. | OK |
| ⟨2⟩4 · Lower-bound the average boundary correlation. | ⟨2⟩1 | The telescoping bound yields $\sum b_k/N\ge L(\tau)>0$. It needs no positivity assumption for the individual $b_k$. | OK |
| ⟨2⟩5 · Match the two cut sums. | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | After division by $N^2$, the weights $\sum_{k=2}^{2N}\sqrt{k(k-1)}/N^2$ tend to 2. With $1/2-p=\rho/2$ this gives exactly $\rho\sqrt{p(1-p)}L^4/2$. Only the convergence portion of Theorem 8 enters. | OK |
| ⟨2⟩6 · local conclusion | ⟨2⟩5 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩5. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩5 | Root, by local closure | Discharged |
| ⟨2⟩1 · Describe the two boundary spins. | ⟨2⟩2, ⟨2⟩4 | P1 | Major claim, SRC-001 | Discharged |
| P1 · Uniqueness at positive $\tau$ licenses both symmetries. The boundary source spins have correlation $\rho$ and their two side channels are conditionally independent. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Bound the joining gain from below. | ⟨2⟩5 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · The concatenated channel is feasible. Fair spins of correlation $c=\rho b_i b_j$ have information $\ln 2-h((1-c)/2)\ge c^2/2$ in nats. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Bound the summed gains from above. | ⟨2⟩5 | P3 | Major claim, SRC-003 | Discharged |
| P3 · For Bernoulli $B_i$, the conditional difference equals $\operatorname{Cov}(\ell,B_i)/(p(1-p))$. Since $\operatorname{Var}T=(k-1)p(1-p)$, the upper bound is $(1/2-p)\sqrt{k(k-1)}\,\omega_k/\sqrt{p(1-p)}$. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Lower-bound the average boundary correlation. | ⟨2⟩5 | ⟨2⟩1, P4 | Major claim, SRC-004 | Discharged |
| P4 · The telescoping bound yields $\sum b_k/N\ge L(\tau)>0$. It needs no positivity assumption for the individual $b_k$. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩5 · Match the two cut sums. | C0 | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, P5 | Major claim, SRC-005 | Discharged |
| P5 · After division by $N^2$, the weights $\sum_{k=2}^{2N}\sqrt{k(k-1)}/N^2$ tend to 2. With $1/2-p=\rho/2$ this gives exactly $\rho\sqrt{p(1-p)}L^4/2$. Only the convergence portion of Theorem 8 enters. | ⟨2⟩5 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
