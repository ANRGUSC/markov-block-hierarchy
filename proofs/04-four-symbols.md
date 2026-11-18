# Theorem 4 · Four-symbol rate and variance

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

For a symmetric persistent chain and $0<D<1/2$, determine the optimum over all four-bit outputs, the rate and the variance from the two scalar searches. Class order, exact endpoint rules and equations for $G$ and distortion are in the linked statement.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L349-L370). Its notation and units govern throughout.

**Background used.** The class table, the column conditions (6), the class moment identities and the finite-slope argument in supporting calculation E.5.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L349–370](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L349-L370) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L340–348](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L340-L348) | Reduce by parity and complementary pairs. | ⟨2⟩1 |
| SRC-002 | [L702–703](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L702-L703) | Optimize the class masses at fixed parity mass. | ⟨2⟩2 |
| SRC-003 | [L703–703](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L703-L703) | Handle an empty parity group. | ⟨2⟩3 |
| SRC-004 | [L705–705](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L705-L705) | Optimize the parity mass. | ⟨2⟩4 |
| SRC-005 | [L365–372](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L365-L372) | Select distortion and compute both moments. | ⟨2⟩5 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Reduce by parity and complementary pairs.** The averaged pair weights are $\alpha=(1+u^4)/2,\ \beta=(u+u^3)/2,\ \chi=u^2$. Within group $g$, $Z_i=L_g+k_gw_i$ where $L_g=\chi m_g+\beta(1-m_g)$, $k_E=\alpha-\chi$ and $k_O=k_E/2$.

**⟨2⟩2. Optimize the class masses at fixed parity mass.** The active derivative is $s_i k_g/Z_i=\eta_g$ and the inactive derivative is at most $\eta_g$. Thus $w_i=[s_i/\eta_g-L_g/k_g]_+$ and positive masses form a prefix.

**⟨2⟩3. Handle an empty parity group.** At $m_g=0$, the maximum prefix ratio is the largest prefix average times $k_g/L_g$. Class 1 attains it and all weights are zero.

**⟨2⟩4. Optimize the parity mass.** Transferring mass gives $G=\eta_E-\eta_O+(\chi-\beta)(\sum_E s_i/Z_i-\sum_O s_i/Z_i)$. Concavity gives the two endpoint signs or an interior zero.

**⟨2⟩5. Select distortion and compute both moments.** Keep the optimizing masses fixed when differentiating in $u$. The distortion is $4D=u\sum_i s_i(L'_g+k'_g w_i)/Z_i$. The mean and pairwise variance give the displayed answers.

**⟨2⟩6. Q.E.D.** By ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩6, ⟨1⟩2 | Contract and closing claims ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 8 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Reduce by parity and complementary pairs. | Contract and stated background | The three distance possibilities give these weights. The table counts all 16 words. Positivity of $L_g$ and $k_g$ is guaranteed by $0<u<1$. | OK |
| ⟨2⟩2 · Optimize the class masses at fixed parity mass. | ⟨2⟩1 | For any prefix of size $j$, its unclipped sum is at most $m_g$. Rearranging gives $\eta_g\ge\sum_{i\le j}s_i/(m_g+jL_g/k_g)$, with equality on the active set. | OK |
| ⟨2⟩3 · Handle an empty parity group. | ⟨2⟩1, ⟨2⟩2 | Taking this first marginal gain supplies the inward one-sided derivative even though there are no positive masses in that group. | OK |
| ⟨2⟩4 · Optimize the parity mass. | ⟨2⟩2, ⟨2⟩3 | The original objective is concave on all masses; mixing feasible allocations proves concavity of the profile. The derivatives of the two common offsets have opposite signs. | OK |
| ⟨2⟩5 · Select distortion and compute both moments. | ⟨2⟩1, ⟨2⟩4 | Appendix B.3 checks the interior slope by strict curvature at a midpoint optimum. Continuity of the column scores makes a newly active or disappearing class meet equality at the boundary. The theorem requires no universal order of losses as $p$ varies. | OK |
| ⟨2⟩6 · local conclusion | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5 | Root, by local closure | Discharged |
| ⟨2⟩1 · Reduce by parity and complementary pairs. | ⟨2⟩2, ⟨2⟩3, ⟨2⟩5 | P1 | Major claim, SRC-001 | Discharged |
| P1 · The three distance possibilities give these weights. The table counts all 16 words. Positivity of $L_g$ and $k_g$ is guaranteed by $0<u<1$. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Optimize the class masses at fixed parity mass. | ⟨2⟩3, ⟨2⟩4, C0 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · For any prefix of size $j$, its unclipped sum is at most $m_g$. Rearranging gives $\eta_g\ge\sum_{i\le j}s_i/(m_g+jL_g/k_g)$, with equality on the active set. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Handle an empty parity group. | ⟨2⟩4, C0 | ⟨2⟩1, ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · Taking this first marginal gain supplies the inward one-sided derivative even though there are no positive masses in that group. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Optimize the parity mass. | ⟨2⟩5, C0 | ⟨2⟩2, ⟨2⟩3, P4 | Major claim, SRC-004 | Discharged |
| P4 · The original objective is concave on all masses; mixing feasible allocations proves concavity of the profile. The derivatives of the two common offsets have opposite signs. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩5 · Select distortion and compute both moments. | C0 | ⟨2⟩1, ⟨2⟩4, P5 | Major claim, SRC-005 | Discharged |
| P5 · Appendix B.3 checks the interior slope by strict curvature at a midpoint optimum. Continuity of the column scores makes a newly active or disappearing class meet equality at the boundary. The theorem requires no universal order of losses as $p$ varies. | ⟨2⟩5 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
