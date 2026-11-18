# Proposition 5 · Full-support threshold

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

Fix $0<p,D<1/2$ and $K\ge1$. Determine feasibility of the inverse crossover law, including zeros at the final step, and the decreasing limit of the finite-block thresholds.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L425-L436). Its notation and units govern throughout.

**Background used.** The inverse law (7), the one-transition spin identity, and composition of binary symmetric channels.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L425–436](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L425-L436) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L419–425](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L419-L425) | Track the signed prefix mass. | ⟨2⟩1 |
| SRC-002 | [L436–437](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L436-L437) | Maximize the magnitude at the next step. | ⟨2⟩2 |
| SRC-003 | [L436–437](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L436-L437) | Distinguish a final zero from an earlier zero. | ⟨2⟩3 |
| SRC-004 | [L438–439](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L438-L439) | Find the common feasibility range. | ⟨2⟩4 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Track the signed prefix mass.** For a prefix of positive mass $m$, let $\mu=E[X_iW_{i-1}]/m$ and $z=1-2D$. Its two extensions have masses $m(1+y\mu/z)/2$. Both are nonnegative exactly when $|\mu|\le z$.

**⟨2⟩2. Maximize the magnitude at the next step.** The positive child has predicted mean $\rho(\mu+y/z)/(1+y\mu/z)$. While $|\mu|<z$, the opposite spin attains $\rho(1-z|\mu|)/(z-|\mu|)$. An alternating prefix realizes this maximum successively.

**⟨2⟩3. Distinguish a final zero from an earlier zero.** At $|\mu|=z$ an extension has mass zero. If another symbol must follow, the zero-mass extension has nonzero signed spin moment and one of its extensions has negative mass.

**⟨2⟩4. Find the common feasibility range.** A fixed point satisfies $H^2-z(1+\rho)H+\rho=0$. For $z\ge2\sqrt\rho/(1+\rho)$ iteration increases to the smaller root below the pole. Otherwise it exits in finite time. Marginalization nests feasible lengths and channel composition nests distortions.

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
| ⟨2⟩1 · Track the signed prefix mass. | Contract and stated background | The initial signed mean is zero by stationarity and symmetry. The quotient is used only for positive-mass prefixes. | OK |
| ⟨2⟩2 · Maximize the magnitude at the next step. | ⟨2⟩1 | The extremal map has derivative $\rho(1-z^2)/(z-H)^2>0$. For a nonzero parent mean the maximizing choice reverses its sign, which validates iteration of the scalar maximum. | OK |
| ⟨2⟩3 · Distinguish a final zero from an earlier zero. | ⟨2⟩1, ⟨2⟩2 | Without dividing by zero, the predicted unnormalized moment of that child is $\rho m(\mu+y/z)/2$, nonzero for $z<1$. A negative marginal cannot be extended to a nonnegative joint measure. | OK |
| ⟨2⟩4 · Find the common feasibility range. | ⟨2⟩2, ⟨2⟩3 | The increasing map leaves the interval below the smaller root invariant, including at the double root. With negative discriminant a bounded increasing orbit below the pole could only limit to a fixed point or the pole; approaching the pole forces an exit. Transforming $z=1-2D$ gives the stated $D_c$. | OK |
| ⟨2⟩5 · local conclusion | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩2, ⟨2⟩3, ⟨2⟩4. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4 | Root, by local closure | Discharged |
| ⟨2⟩1 · Track the signed prefix mass. | ⟨2⟩2, ⟨2⟩3 | P1 | Major claim, SRC-001 | Discharged |
| P1 · The initial signed mean is zero by stationarity and symmetry. The quotient is used only for positive-mass prefixes. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Maximize the magnitude at the next step. | ⟨2⟩3, ⟨2⟩4, C0 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · The extremal map has derivative $\rho(1-z^2)/(z-H)^2>0$. For a nonzero parent mean the maximizing choice reverses its sign, which validates iteration of the scalar maximum. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Distinguish a final zero from an earlier zero. | ⟨2⟩4, C0 | ⟨2⟩1, ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · Without dividing by zero, the predicted unnormalized moment of that child is $\rho m(\mu+y/z)/2$, nonzero for $z<1$. A negative marginal cannot be extended to a nonnegative joint measure. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Find the common feasibility range. | C0 | ⟨2⟩2, ⟨2⟩3, P4 | Major claim, SRC-004 | Discharged |
| P4 · The increasing map leaves the interval below the smaller root invariant, including at the double root. With negative discriminant a bounded increasing orbit below the pole could only limit to a fixed point or the pole; approaching the pole forces an exit. Transforming $z=1-2D$ gives the stated $D_c$. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
