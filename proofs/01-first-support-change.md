# Proposition 1 · First support change

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

For a stationary binary chain with positive transition probabilities, determine the first zero of the two-symbol inverse prior. Retain the separate positive-, negative- and zero-persistence cases and the equal-bias tie in the statement.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L213-L219). Its notation and units govern throughout.

**Background used.** Finite binary Markov probabilities, the pair-mass identities (9), and the inverse-prior criterion (7).

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L213–219](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L213-L219) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L220–225](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L220-L225) | Invert the two-bit channel. | ⟨2⟩1 |
| SRC-002 | [L226–227](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L226-L227) | Case $\rho>0$. | ⟨2⟩2 |
| SRC-003 | [L226–227](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L226-L227) | Case $\rho<0$. | ⟨2⟩3 |
| SRC-004 | [L226–227](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L226-L227) | Case $\rho=0$. | ⟨2⟩4 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Invert the two-bit channel.** In word order $00,01,10,11$, the inverse masses have common denominator $(1-u)^2$. Their numerators are $A-2Cu+Bu^2$, $C(1+u^2)-(A+B)u$ twice, and $B-2Cu+Au^2$.

**⟨2⟩2. Case $\rho>0$.** Both constant quadratics have negative discriminant. The transition words reach zero together at $D(1-D)=C$.

**⟨2⟩3. Case $\rho<0$.** The smaller constant mass reaches zero at $u_*=(C-\sqrt{C^2-AB})/\max(A,B)$. Both constants vanish together at equal bias. The transition numerator there is $(1-u_*^2)\sqrt{C^2-AB}$.

**⟨2⟩4. Case $\rho=0$.** The inverse prior is a product with one-probability $(\pi_1-D)/(1-2D)$ for $D<D_0$.

**⟨2⟩5. Q.E.D.** By ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩5, ⟨1⟩2 | Contract and closing claims ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 7 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Invert the two-bit channel. | Contract and stated background | The denominator is positive for $0\le u<1$. At $u=0$ all entries are positive, so their first zero controls loss of support. | OK |
| ⟨2⟩2 · Case $\rho>0$. | ⟨2⟩1 | Use $AB-C^2=\rho\pi_0\pi_1$ and $u=D/(1-D)$. The smaller root $(1-\sqrt{1-4C})/2$ is the one reached from zero. | OK |
| ⟨2⟩3 · Case $\rho<0$. | ⟨2⟩1 | The constant numerators differ by $(A-B)(1-u^2)$. The transition polynomial is reciprocal with positive constant term, so it has at most one crossing in $(0,1)$ and cannot have crossed before this positive value. The threshold is $u_* /(1+u_*)$. | OK |
| ⟨2⟩4 · Case $\rho=0$. | ⟨2⟩1 | Both numerator and complementary numerator $\pi_0-D$ are positive. The three signs of $\rho$ exhaust the cases. | OK |
| ⟨2⟩5 · local conclusion | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩2, ⟨2⟩3, ⟨2⟩4. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | Root, by local closure | Discharged |
| ⟨2⟩1 · Invert the two-bit channel. | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | P1 | Major claim, SRC-001 | Discharged |
| P1 · The denominator is positive for $0\le u<1$. At $u=0$ all entries are positive, so their first zero controls loss of support. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Case $\rho>0$. | C0 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · Use $AB-C^2=\rho\pi_0\pi_1$ and $u=D/(1-D)$. The smaller root $(1-\sqrt{1-4C})/2$ is the one reached from zero. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Case $\rho<0$. | C0 | ⟨2⟩1, P3 | Major claim, SRC-003 | Discharged |
| P3 · The constant numerators differ by $(A-B)(1-u^2)$. The transition polynomial is reciprocal with positive constant term, so it has at most one crossing in $(0,1)$ and cannot have crossed before this positive value. The threshold is $u_* /(1+u_*)$. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Case $\rho=0$. | C0 | ⟨2⟩1, P4 | Major claim, SRC-004 | Discharged |
| P4 · Both numerator and complementary numerator $\pi_0-D$ are positive. The three signs of $\rho$ exhaust the cases. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
