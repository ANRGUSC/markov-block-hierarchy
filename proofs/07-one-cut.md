# Lemma 7 · One cut at a common multiplier

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

For a symmetric stationary chain with $0<p<1/2$, adjacent lengths $i,j\ge1$ and a common $\tau\ge0$, prove independence of the two short scores under the true joint law and an uncentered squared-error bound $\rho$ for their sum versus the joint score.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L524-L529). Its notation and units govern throughout.

**Background used.** The finite-optimum column test, complement symmetry, independent flips, and the elementary exponential inequality in Appendix B.1.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L524–529](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L524-L529) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L737–738](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L737-L738) | Factor the product-law optimum. | ⟨2⟩1 |
| SRC-002 | [L738–741](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L738-L741) | Test each prior at the other optimum. | ⟨2⟩2 |
| SRC-003 | [L742–742](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L742-L742) | Bound the uncentered error. | ⟨2⟩3 |
| SRC-004 | [L744–747](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L744-L747) | Identify the independent quantities. | ⟨2⟩4 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Factor the product-law optimum.** Let $P$ be the joint law and $Q$ the product of the two marginals. The product of the two short optimal priors passes every column test for $Q$. Its normalizer is the product of the two short normalizers.

**⟨2⟩2. Test each prior at the other optimum.** With $\Delta=\ln(Z_Q/Z_P)$, averaging optimal columns gives $E_Pe^\Delta\le1$ and $E_Q e^{-\Delta}\le1$. The boundary likelihood ratio takes the values $2p,2(1-p)$.

**⟨2⟩3. Bound the uncentered error.** The pointwise inequality $t^2\le e^t+e^{-t}-2$ gives $E_P\Delta^2\le1+2(1-p)-2=\rho$.

**⟨2⟩4. Identify the independent quantities.** Complement symmetry removes the initial spin from each component score. Each score depends only on its internal flips, and the two sets of flips are disjoint and independent.

**⟨2⟩5. Q.E.D.** By ⟨2⟩3, ⟨2⟩4 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩5, ⟨1⟩2 | Contract and closing claims ⟨2⟩3, ⟨2⟩4 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 7 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Factor the product-law optimum. | Contract and stated background | The factorization uses both the tensor Hamming kernel and the product law. At $\tau=0$ every normalizer equals one even though the prior can be nonunique. | OK |
| ⟨2⟩2 · Test each prior at the other optimum. | ⟨2⟩1 | Only the transition across the cut changes. In particular $E_Pe^{-\Delta}\le2(1-p)E_Qe^{-\Delta}$; reversing that likelihood ratio would not give the claimed constant. | OK |
| ⟨2⟩3 · Bound the uncentered error. | ⟨2⟩2 | The joint score minus the sum of the component scores equals $\Delta$ with these definitions. | OK |
| ⟨2⟩4 · Identify the independent quantities. | ⟨2⟩1 | The stationary symmetric path is generated from a fair initial bit and independent Bernoulli flips. Independence is asserted for the scores; the adjacent source words still share dependence. | OK |
| ⟨2⟩5 · local conclusion | ⟨2⟩3, ⟨2⟩4 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩3, ⟨2⟩4. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩3, ⟨2⟩4 | Root, by local closure | Discharged |
| ⟨2⟩1 · Factor the product-law optimum. | ⟨2⟩2, ⟨2⟩4 | P1 | Major claim, SRC-001 | Discharged |
| P1 · The factorization uses both the tensor Hamming kernel and the product law. At $\tau=0$ every normalizer equals one even though the prior can be nonunique. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Test each prior at the other optimum. | ⟨2⟩3 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · Only the transition across the cut changes. In particular $E_Pe^{-\Delta}\le2(1-p)E_Qe^{-\Delta}$; reversing that likelihood ratio would not give the claimed constant. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Bound the uncentered error. | C0 | ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · The joint score minus the sum of the component scores equals $\Delta$ with these definitions. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Identify the independent quantities. | C0 | ⟨2⟩1, P4 | Major claim, SRC-004 | Discharged |
| P4 · The stationary symmetric path is generated from a fair initial bit and independent Bernoulli flips. Independence is asserted for the scores; the adjacent source words still share dependence. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
