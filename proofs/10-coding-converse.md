# Proposition 10 · Low-distortion converse for one path

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

For $0<p<1/2$, $0<D\le D_c$ and fixed $0<\epsilon<1$, show $\liminf_n\sqrt n(R^*(n,D,\epsilon)-R(D))\ge\sqrt{\nu(p)}Q^{-1}(\epsilon)$ under the uninterrupted stationary source law.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L596-L602). Its notation and units govern throughout.

**Background used.** Proposition 5, the binomial score identity, the finite rate bracket, the binomial central limit theorem, and [Kostina–Verdú, Theorem 7](https://www.its.caltech.edu/~vkostina/pdfs/2012KostinaVerdu-lossycomp.pdf).

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L596–602](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L596-L602) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L585–590](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L585-L590) | Center the one-path score. | ⟨2⟩1 |
| SRC-002 | [L591–594](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L591-L594) | Apply the nonasymptotic converse to a whole word. | ⟨2⟩2 |
| SRC-003 | [L603–605](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L603-L605) | Use the low-distortion distribution. | ⟨2⟩3 |
| SRC-004 | [L603–605](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L603-L605) | Exclude a violating subsequence. | ⟨2⟩4 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Center the one-path score.** The path score $J_n$ has mean $R_n(nD)$. The rate bracket gives $0\le EJ_n-nR(D)\le I_0$.

**⟨2⟩2. Apply the nonasymptotic converse to a whole word.** Any code of size $M$ has excess-distortion probability at least $\Pr[J_n\ge\log_2 M+\gamma]-2^{-\gamma}$.

**⟨2⟩3. Use the low-distortion distribution.** Proposition 5 keeps every length on the entropy-equality branch including $D=D_c$. The centered score equals $(T-(n-1)p)\log_2((1-p)/p)$ with $T$ binomial. Dividing by $\sqrt{n\nu(p)}$ gives a standard normal limit.

**⟨2⟩4. Exclude a violating subsequence.** If the liminf were smaller, some subsequence would place the normalized log code size at least $2\delta$ below $Q^{-1}(\epsilon)$. Choose $\gamma=\log_2 n$. Eventually the tested threshold is at most $Q^{-1}(\epsilon)-\delta$.

**⟨2⟩5. Q.E.D.** By ⟨2⟩4 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩5, ⟨1⟩2 | Contract and closing claims ⟨2⟩4 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 7 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Center the one-path score. | Contract and stated background | Subtracting this bounded bias on a $\sqrt n$ scale has vanishing effect. The units of the score here are bits. | OK |
| ⟨2⟩2 · Apply the nonasymptotic converse to a whole word. | Contract and stated background | Kostina–Verdú, Theorem 7, applies to the single random object $X^n$. Its alphabet is finite, Hamming distortion is bounded, $D>0$ exceeds the minimum, and the full-support-branch backward channel gives an attaining optimizer with a unique interior marginal and channel. Normalizing distance by $n$ changes the slope scale only. | OK |
| ⟨2⟩3 · Use the low-distortion distribution. | ⟨2⟩1 | Here $\nu(p)>0$. The central limit theorem applies to the independent flips inside one path. No block-independence approximation is needed. | OK |
| ⟨2⟩4 · Exclude a violating subsequence. | ⟨2⟩2, ⟨2⟩3 | The penalty $1/n$ vanishes and normal continuity gives a limiting tail strictly above $\epsilon$. This contradicts the code constraint for every $0<\epsilon<1$, including when the target quantile is negative. | OK |
| ⟨2⟩5 · local conclusion | ⟨2⟩4 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩4. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩4 | Root, by local closure | Discharged |
| ⟨2⟩1 · Center the one-path score. | ⟨2⟩3 | P1 | Major claim, SRC-001 | Discharged |
| P1 · Subtracting this bounded bias on a $\sqrt n$ scale has vanishing effect. The units of the score here are bits. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Apply the nonasymptotic converse to a whole word. | ⟨2⟩4 | P2 | Major claim, SRC-002 | Discharged |
| P2 · Kostina–Verdú, Theorem 7, applies to the single random object $X^n$. Its alphabet is finite, Hamming distortion is bounded, $D>0$ exceeds the minimum, and the full-support-branch backward channel gives an attaining optimizer with a unique interior marginal and channel. Normalizing distance by $n$ changes the slope scale only. | ⟨2⟩2 | Local verification | Named theorem, Theorem 7 and its hypotheses | Discharged |
| ⟨2⟩3 · Use the low-distortion distribution. | ⟨2⟩4 | ⟨2⟩1, P3 | Major claim, SRC-003 | Discharged |
| P3 · Here $\nu(p)>0$. The central limit theorem applies to the independent flips inside one path. No block-independence approximation is needed. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Exclude a violating subsequence. | C0 | ⟨2⟩2, ⟨2⟩3, P4 | Major claim, SRC-004 | Discharged |
| P4 · The penalty $1/n$ vanishes and normal continuity gives a limiting tail strictly above $\epsilon$. This contradicts the code constraint for every $0<\epsilon<1$, including when the target quantile is negative. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
