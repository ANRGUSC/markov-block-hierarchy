# Theorem 2 · Persistent two-symbol source

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

Assume $\rho>0$, arbitrary stationary bias, $S=A+B$. Compute the rate, variance and active constant words in all three distortion regimes, with the zero supporting slope at and above $D_0$. The linked statement specifies every branch.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L236-L253). Its notation and units govern throughout.

**Background used.** The entropy bound and column test in supporting calculation A, Proposition 1, the binary entropy inequality, and the mutual-information chain rule.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L236–253](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L236-L253) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L254–255](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L254-L255) | Full-support branch. | ⟨2⟩1 |
| SRC-002 | [L255–256](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L255-L256) | Solve the problem with only constant outputs. | ⟨2⟩2 |
| SRC-003 | [L257–262](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L257-L262) | Compute the two active masses and the score. | ⟨2⟩3 |
| SRC-004 | [L261–262](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L261-L262) | Check the two unused columns. | ⟨2⟩4 |
| SRC-005 | [L250–263](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L250-L263) | Close at zero rate. | ⟨2⟩5 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Full-support branch.** The backward binary symmetric channel attains the entropy lower bound through the first zero. The rate is $H(P_2)-2h_2(D)$ and the variance is the varentropy of $P_2$.

**⟨2⟩2. Solve the problem with only constant outputs.** A flip input always incurs one error. Given a constant input, an incorrect output incurs two errors. The conditional error budget is $\delta=(D-C)/S$. Chain rule gives the lower bound $S[h_2(B/S)-h_2(\delta)]$.

**⟨2⟩3. Compute the two active masses and the score.** With $u^2=\delta/(1-\delta)$ the masses are $(A-Bu^2,B-Au^2)/(S(1-u^2))$. The three normalizers are $A(1+u^2)/S,u,B(1+u^2)/S$.

**⟨2⟩4. Check the two unused columns.** Set $x=u/(1+u^2)$. Their column value is $2Sx+C/x$. It is at most one between the roots $C/S$ and $1/2$.

**⟨2⟩5. Close at zero rate.** The mass boundary $\delta=\min(A,B)/S$ gives $D=D_0$. At a biased endpoint only the more frequent constant attains zero rate, and the zero-slope convention gives zero variance.

**⟨2⟩6. Q.E.D.** By ⟨2⟩1, ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩6, ⟨1⟩2 | Contract and closing claims ⟨2⟩1, ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 8 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Full-support branch. | Contract and stated background | Proposition 1 identifies the boundary. Since $C=(1-\rho)\pi_0\pi_1<\pi_0\pi_1$, this boundary is strictly below $D_0$, including at biased parameters. | OK |
| ⟨2⟩2 · Solve the problem with only constant outputs. | Contract and stated background | Drawing the flip-input output from the same marginal as the optimal binary channel makes the output independent of the constant-input indicator. Equality holds in the conditional binary entropy bound. | OK |
| ⟨2⟩3 · Compute the two active masses and the score. | ⟨2⟩2 | The weights sum to one. Substitution in the kernel and taking the variance of $-\log_2 Z$ under $(A,2C,B)$ gives the stated second branch. | OK |
| ⟨2⟩4 · Check the two unused columns. | ⟨2⟩2, ⟨2⟩3 | At the change point $x=C/S$. The function $u/(1+u^2)$ increases on $(0,1)$. Positivity of both masses is equivalent to $\delta<\min(A,B)/S$. | OK |
| ⟨2⟩5 · Close at zero rate. | ⟨2⟩3, ⟨2⟩4 | At zero rate output is independent of input. In every coordinate, using the less frequent symbol increases expected distortion strictly for a biased source. The fair endpoint needs no uniqueness claim. | OK |
| ⟨2⟩6 · local conclusion | ⟨2⟩1, ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩1, ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩1, ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 | Root, by local closure | Discharged |
| ⟨2⟩1 · Full-support branch. | C0 | P1 | Major claim, SRC-001 | Discharged |
| P1 · Proposition 1 identifies the boundary. Since $C=(1-\rho)\pi_0\pi_1<\pi_0\pi_1$, this boundary is strictly below $D_0$, including at biased parameters. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Solve the problem with only constant outputs. | ⟨2⟩3, ⟨2⟩4, C0 | P2 | Major claim, SRC-002 | Discharged |
| P2 · Drawing the flip-input output from the same marginal as the optimal binary channel makes the output independent of the constant-input indicator. Equality holds in the conditional binary entropy bound. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Compute the two active masses and the score. | ⟨2⟩4, ⟨2⟩5, C0 | ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · The weights sum to one. Substitution in the kernel and taking the variance of $-\log_2 Z$ under $(A,2C,B)$ gives the stated second branch. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Check the two unused columns. | ⟨2⟩5, C0 | ⟨2⟩2, ⟨2⟩3, P4 | Major claim, SRC-004 | Discharged |
| P4 · At the change point $x=C/S$. The function $u/(1+u^2)$ increases on $(0,1)$. Positivity of both masses is equivalent to $\delta<\min(A,B)/S$. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩5 · Close at zero rate. | C0 | ⟨2⟩3, ⟨2⟩4, P5 | Major claim, SRC-005 | Discharged |
| P5 · At zero rate output is independent of input. In every coordinate, using the less frequent symbol increases expected distortion strictly for a biased source. The fair endpoint needs no uniqueness claim. | ⟨2⟩5 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
