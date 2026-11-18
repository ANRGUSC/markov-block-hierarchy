# Theorem 3 · Three-symbol rate and variance

[Guide](README.md) · [Supporting calculations](supporting-calculations.md)

## Source mapping

**SOURCE-MAPPED.** This status concerns source mapping only; it is not a validity verdict.

### Frozen statement and assumptions

Take a symmetric chain with $0<p<1/2$. The three branches, thresholds $D_{\rm FS}(3),D_2$, normalizers, two variances and scalar equations are those of the linked theorem. The nonzero-rate range ends at $D<1/2$.

The exact quantified statement and all displayed formulas are in the [audited manuscript](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L291-L314). Its notation and units govern throughout.

**Background used.** The symmetric law and class moments (13)–(16), the inverse-prior criterion, and stationarity on the probability simplex.

### Source inventory

| Source | Passage | Role | Placement |
|---|---|---|---|
| Contract | [L291–314](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L291-L314) | Theorem statement | ⟨1⟩1 |
| SRC-001 | [L691–695](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L691-L695) | Reduce the eight words to three classes. | ⟨2⟩1 |
| SRC-002 | [L696–696](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L696-L696) | Order the support changes. | ⟨2⟩2 |
| SRC-003 | [L698–698](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L698-L698) | Locate the first zero. | ⟨2⟩3 |
| SRC-004 | [L700–700](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L700-L700) | Solve the six-word branch. | ⟨2⟩4 |
| SRC-005 | [L700–700](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L700-L700) | Locate the transition to two words. | ⟨2⟩5 |
| SRC-006 | [L309–317](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L309-L317) | Evaluate the two-word branch and both moments. | ⟨2⟩6 |

### Structured proof

**⟨1⟩1.** Assume the hypotheses of the frozen statement. Prove the stated result under those hypotheses.

**⟨2⟩1. Reduce the eight words to three classes.** A complementary pair contributes $\alpha=(1+u^3)/2$ when it contains the input and $\beta=(u+u^2)/2$ otherwise. Thus $Z_i=\beta+(\alpha-\beta)h_i w_i$ with $h=(1,1/2,1)$.

**⟨2⟩2. Order the support changes.** Write $c_i=(\alpha-\beta)h_i$. Stationarity gives $w_i=[s_i/\eta-\beta/c_i]_+$. An active prefix is selected in descending order of $s_i h_i$. Its threshold increases with $u$.

**⟨2⟩3. Locate the first zero.** The alternating-word inverse probability is $[1-(2\rho-\rho^2)/(1-2D)^2]/8$. It vanishes at $D_{\rm FS}(3)=(1-\sqrt{1-4p^2})/2$.

**⟨2⟩4. Solve the six-word branch.** Setting $w_2=0$ yields $(Z_0,Z_1,Z_2)=(s_0 H/S_{01},s_1 H/(2S_{01}),\beta)$ where $H=\alpha+2\beta$. The envelope derivative gives $3D=s_2+u/(1+u)+S_{01}u(1+2u)/(1+u+u^2)$.

**⟨2⟩5. Locate the transition to two words.** At $w_1=0$, $s_1/(2\beta)=s_0/\alpha$, or $u/(1+u^2)=p$. Select the root $u_2=2p/(1+\sqrt{1-4p^2})$.

**⟨2⟩6. Evaluate the two-word branch and both moments.** For the two equiprobable constants the distance pairs are $(0,3)$ or $(1,2)$. Hence $3D=s_0\,3u^3/(1+u^3)+(1-s_0)(1+u/(1+u))$. At each optimizer evaluate the class mean and pairwise variance.

**⟨2⟩7. Q.E.D.** By ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩6 under the assumptions of ⟨1⟩1.

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
| ⟨2⟩7, ⟨1⟩2 | Contract and closing claims ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩6 | STRUCTURAL | IMPLICIT |

**Gap register.** No missing premise was identified in this numbered result under the stated scope. The two endpoint qualifications for surrounding prose are recorded in the supporting calculations.

**Handoff.** Both audits below use this same statement, labeled hierarchy and background. The mapping records provenance only.

</details>

## Forward audit

**PASS.** The steps establish the frozen statement under its hypotheses.

The theorem contract above is the forward goal. There are two levels and 9 labeled steps. The local assumptions are discharged before the outer conclusion.

| Step and goal | Legal dependencies | Justification checked | Status |
|---|---|---|---|
| ⟨1⟩1 · local implication | Frozen contract | Local goal uses exactly the original hypotheses. | OK |
| ⟨2⟩1 · Reduce the eight words to three classes. | Contract and stated background | Complement and reversal preserve source law and kernel. The one-flip orbit contains two complementary pairs; the other two orbits contain one each. | OK |
| ⟨2⟩2 · Order the support changes. | ⟨2⟩1 | For a fixed active set the threshold is $\sum_{I}s_i/((1-u)^2/u+\sum_I1/h_i)$. It is continuous at a zero weight. Since $s_0>s_1/2>s_2$, a dropped class cannot return. | OK |
| ⟨2⟩3 · Locate the first zero. | ⟨2⟩2 | Pair correlations scale by $(1-2D)^2$ under independent crossover. Odd moments vanish by complement symmetry. On the feasible branch use the binomial flip count for both moments. | OK |
| ⟨2⟩4 · Solve the six-word branch. | ⟨2⟩1, ⟨2⟩2 | The active mass derivatives multiply equal marginal gains and sum to zero. The last fraction is the mean exponent in $1+u+u^2$, strictly increasing with $\log u$ by its positive variance. | OK |
| ⟨2⟩5 · Locate the transition to two words. | ⟨2⟩4 | The other root exceeds one. Inserting $u_2$ in the constant-output distortion gives the stated $D_2$ and assigns the zero-mass class to the correct side of the boundary. | OK |
| ⟨2⟩6 · Evaluate the two-word branch and both moments. | ⟨2⟩1, ⟨2⟩4, ⟨2⟩5 | Both summands strictly increase for $u>0$. Since $1+u$ divides $1+u^3$, the last branch needs only a cubic; the middle denominators also have product of degree three. Two distinct normalizers give $s_0(1-s_0)\log_2^2(\alpha/\beta)$. | OK |
| ⟨2⟩7 · local conclusion | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩6 | The cited assertions cover the quantified conclusion and its cases. | OK |
| ⟨1⟩2 · theorem conclusion | ⟨1⟩1 | The closed parent assertion is visible here. | OK |

**Outstanding obligations.** None for this theorem. No proof repair is required on the audited route.

## Reverse audit

Starting at the exact conclusion linked above, the primary route requires **all** of ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩6. An arrow in the table points to the premises needed for that claim. Case branches must all close.

| Claim or obligation | Needed by | Primary route (AND) | Classification and support | Status |
|---|---|---|---|---|
| C0 · exact theorem | Root | ⟨2⟩2, ⟨2⟩3, ⟨2⟩4, ⟨2⟩5, ⟨2⟩6 | Root, by local closure | Discharged |
| ⟨2⟩1 · Reduce the eight words to three classes. | ⟨2⟩2, ⟨2⟩4, ⟨2⟩6 | P1 | Major claim, SRC-001 | Discharged |
| P1 · Complement and reversal preserve source law and kernel. The one-flip orbit contains two complementary pairs; the other two orbits contain one each. | ⟨2⟩1 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩2 · Order the support changes. | ⟨2⟩3, ⟨2⟩4, C0 | ⟨2⟩1, P2 | Major claim, SRC-002 | Discharged |
| P2 · For a fixed active set the threshold is $\sum_{I}s_i/((1-u)^2/u+\sum_I1/h_i)$. It is continuous at a zero weight. Since $s_0>s_1/2>s_2$, a dropped class cannot return. | ⟨2⟩2 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩3 · Locate the first zero. | C0 | ⟨2⟩2, P3 | Major claim, SRC-003 | Discharged |
| P3 · Pair correlations scale by $(1-2D)^2$ under independent crossover. Odd moments vanish by complement symmetry. On the feasible branch use the binomial flip count for both moments. | ⟨2⟩3 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩4 · Solve the six-word branch. | ⟨2⟩5, ⟨2⟩6, C0 | ⟨2⟩1, ⟨2⟩2, P4 | Major claim, SRC-004 | Discharged |
| P4 · The active mass derivatives multiply equal marginal gains and sum to zero. The last fraction is the mean exponent in $1+u+u^2$, strictly increasing with $\log u$ by its positive variance. | ⟨2⟩4 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩5 · Locate the transition to two words. | ⟨2⟩6, C0 | ⟨2⟩4, P5 | Major claim, SRC-005 | Discharged |
| P5 · The other root exceeds one. Inserting $u_2$ in the constant-output distortion gives the stated $D_2$ and assigns the zero-mass class to the correct side of the boundary. | ⟨2⟩5 | Local verification | Algebraic/logical step under the listed background | Discharged |
| ⟨2⟩6 · Evaluate the two-word branch and both moments. | C0 | ⟨2⟩1, ⟨2⟩4, ⟨2⟩5, P6 | Major claim, SRC-006 | Discharged |
| P6 · Both summands strictly increase for $u>0$. Since $1+u$ divides $1+u^3$, the last branch needs only a cubic; the middle denominators also have product of degree three. Two distinct normalizers give $s_0(1-s_0)\log_2^2(\alpha/\beta)$. | ⟨2⟩6 | Local verification | Algebraic/logical step under the listed background | Discharged |

**FOLLOWS.** The conclusion-reachable obligations close on the supplied route under the frozen contract.
