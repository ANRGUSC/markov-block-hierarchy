# Supporting calculations and scope of the claims

The numbered proof files use the following arguments. Step numbers restart in each section. Source links point to the audited revision. All logarithms used in the score comparison and concentration arguments are natural logarithms. The final variance in the manuscript is in bits squared per symbol.

## A. Optimality and the entropy-equality branch

**⟨1⟩1. Fix the slope.** For a finite alphabet, minimizing conditional relative entropy to a prior $q$ plus $\tau E d$ gives $W(y\mid x)=q(y)e^{-\tau d(x,y)}/Z(x)$. Minimizing over $q$ returns the output marginal. With $P_K(x)>0$ and $0<u=e^{-\tau}<1$, the binary Hamming kernel is invertible by its tensor factorization. Strict concavity of the log in the normalizers then makes the optimal prior unique.

**⟨1⟩2. Test every column.** The simplex gradient has components $c(y)=\sum_xP_K(x)u^{d(x,y)}/Z(x)$. Its average under $q$ is one. The directional derivative toward any vertex is $c(y)-1$. Concavity proves necessity and sufficiency of $c(y)\le1$ everywhere, with equality on the support.

**⟨1⟩3. Attain the entropy bound.** Write $E=X\oplus Y$. The conditional entropy of $X$ given $Y$ is at most $K h_2(D)$ by subadditivity, concavity, and monotonicity up to $1/2$. Equality requires independent Bernoulli$(D)$ errors independent of $Y$. Invert the product crossover matrix to obtain the candidate $q_D$. When it is nonnegative it is normalized and $Z=(1+u)^K P_K$ at $u=D/(1-D)$. Conversely, if all columns are tight then inverting the column equations gives this same normalizer. At this slope the centered score equals centered self-information.

**⟨1⟩4. Scope check at a biased endpoint.** Take independent Bernoulli$(1/4)$ symbols and $D=D_0=1/4$. The inverse prior puts mass one on the all-zero word. At the backward-channel slope $\lambda=\log_2 3$, the two one-symbol scores differ by $\log_2 3$. Their variance per symbol is $(3/16)\log_2^2 3$. At the paper's chosen endpoint slope $\lambda=0$, both scores equal zero. The rate is zero under both choices. The “first zero” sentence following equation (8) therefore needs the interior scope of Section 2.1, or an explicit statement of which supporting slope is used. Theorem 6 assumes the score identity holds; Proposition 10 stays strictly below the symmetric zero-rate endpoint.

**Forward and reverse check.** Steps 1–3 establish the interior equality and also cover an interior support threshold by continuity. Step 4 gives a counterexample to extending the *assigned* variance formula to every biased zero-rate endpoint. [Sections 2.1–2.3](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L132-L183)

## B. Independent blocks, symmetry and finite computations

**⟨1⟩1. Change the unit of coding.** For $m$ independent $K$-words, use one word as a memoryless letter. Its rate is $R_K(KD)$ and its tilted variance is $V_K(KD)$. Divide the rate for $m$ such letters by $K$. This yields $r_K+\sqrt{v_K/(mK)}Q^{-1}(\epsilon)$ with the stated fixed-$K$ remainder under the regularity conditions cited in the draft. The memoryless theorem is used only for independent words. [Kostina and Verdú, Theorem 12](https://www.its.caltech.edu/~vkostina/pdfs/2012KostinaVerdu-lossycomp.pdf)

**⟨1⟩2. Count symmetric flips.** With $0<p<1/2$, a fair first bit and $K-1$ independent flips generate the source. On the branch in A.3, centering removes the initial-bit contribution and the entropy offset. The centered score is $(T-(K-1)p)\log_2((1-p)/p)$, and $T$ has variance $(K-1)p(1-p)$. Complement and reversal preserve source law and kernel. For score values $-\log_2 Z_i$ with masses $s_i$, one half the expected squared difference of two independent draws gives $\sum_{i<j}s_i s_j\log_2^2(Z_i/Z_j)$.

**⟨1⟩3. Transform the exceptional sources.** XOR by the alternating mask carries $p>1/2$ to $1-p$ while preserving every distortion and permuting every normalizer. At $p=1/2$ the fair product source has constant tilted score. At $p=0,1$ one fair bit determines the block. A binary test channel achieves $1-h_2(D)$; averaging the coordinate conditional-entropy bounds gives the reverse inequality, also for the alternating path after unmasking.

**⟨1⟩4. Compute the moments.** Applying the two-by-two Hamming kernel in each tensor coordinate gives each multiplication in $O(K2^K)$ time and $O(2^K)$ storage. At the selected distortion, substituting the normalizers in the score gives equation (25). On a certified two-constant branch the two distances are $w,K-w$. The last-bit/weight recursion has $O(i)$ entries at stage $i$, hence the advertised quadratic preprocessing and linear storage. This shortcut requires an all-column test.

**⟨1⟩5. Check the examples outside the named statements.** In the biased anti-persistent example $u=1/2$ and equal mass on $01,10$ give $Z=(1/2,5/8,5/8,1/2)$. The unused-column gains are $491/520$ and $431/520$, both below one. On the four-symbol constant branch the test against the next even class reduces to $p/(1-p)\le2u^2/(1+u^4)$; the test against every odd-class transfer is the one-sided test $G(1)\ge0$. Either test alone is insufficient.

**Forward and reverse check.** The memoryless normalization uses step 1 alone. The exact short-block formulas use steps 2–3 and part A. Their computational evaluation uses steps 4–5. [Source, Sections 2–4](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L155-L416)

## C. The finite rate bracket and the common-slope mean

**⟨1⟩1. Upper bound.** Use the short optimal channels independently given their respective input segments. The conditional output entropies add, and joint output entropy is at most the sum of the marginals. Optimize over the distortion allocations.

**⟨1⟩2. Lower bound.** For an arbitrary joint channel, $H(X^K\mid Y^K)\le\sum_j H(X_j^{\rm seg}\mid Y_j^{\rm seg})$. A stationary one-step chain loses exactly $I_0$ bits of input mutual information per cut when the marginal entropies are added. Thus subtract $(m-1)I_0$ from the sum of short rates and minimize over feasible allocations. Convexity makes equal allocation optimal for equal lengths.

**⟨1⟩3. Take limits.** For $K=mk$, divide by $K$ and send $m$ to infinity to get $0\le r_k-R\le I_0/k$. The identical one-cut comparison for the penalized objective, in nats, gives $F_i+F_j-J_0\le F_{i+j}\le F_i+F_j$. Subadditivity supplies the limit $f$; taking multiples gives $0\le f_k-f\le J_0/k$ uniformly in the multiplier.

**Forward and reverse check.** The source entropy loss enters the *lower* bound. Both limits use the existence of the rate or subadditive-cost limit before passing to multiples. These steps give the bounded centering correction for Proposition 10 and the objective estimate in Theorem 8. [Rate bracket](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L478-L485) · [Penalized cost](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L756-L758)

## D. Positive slope at fixed distortion and finite-length positivity

**⟨1⟩1. Concentration of distance to a fixed word.** Expose the source spins in order. Changing the current spin changes the conditional future mismatch probability at lag $h$ by at most $\rho^h$. For a fixed past, the range of each martingale increment is at most $c=(1-\rho)^{-1}$. Each coordinate is fair. The conditional centered Hoeffding bound, multiplied over the $K$ increments, gives $\ln E\exp[-t(d-K/2)]\le Kt^2c^2/8$.

**⟨1⟩2. Convert concentration into a rate bound.** Use the relative-entropy variational inequality with test function $-t(d-K/2)$ conditional on $Y=y$, and then average. If $E d\le KD$, then $I/K\ge t(1/2-D)-t^2 c^2/8$ in nats. Maximizing over $t\ge0$ gives $I/K\ge2(1-\rho)^2(1/2-D)^2$.

**⟨1⟩3. Bound any supporting slope.** At $1/2$ the rate is zero. Evaluating a supporting line based at $D<1/2$ there gives slope magnitude at least $2(1-\rho)^2(1/2-D)>0$. The inequality holds for the limiting rate by passage to the limit. Combining it with Corollary 9 and (33) yields the stated finite-length lower estimate, which may itself be negative for small $K$.

**⟨1⟩4. Distinguish strict positivity at a finite length.** For $K\ge2$ and an interior multiplier, constant $Z$ would force uniform $q$ by inversion, then uniform $P_K$ by the active column equations. A persistent two-state source is nonuniform at these lengths. For $K=1$ the source is fair, and its variance is identically zero.

**Forward and reverse check.** Steps 1–3 give positivity of the *slope*. Strict positivity of the limiting variance then needs the separate common-slope lower bound of Corollary 9. Step 4 separately establishes strict positivity at finite $K\ge2$. [Appendix B.2](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L783-L796)

## E. Slope enclosures, solver residuals and stopping

**⟨1⟩1. Localize the slope.** For $j\le K$, both finite objectives differ from the limiting one by one-sided errors between zero and $J_0/j$. Thus $|f_j-f_K|\le J_0/j$. Comparing a maximizer of each objective gives a tolerance $2J_0/j$ at probe length $j$. If $j$ divides $K$, the finite comparison is one-sided and only $J_0/j$ is needed. Against the limit itself the one-sided bound also suffices.

**⟨1⟩2. Enclose the variance.** At the same slope $\tau_K$, Theorem 8 bounds the difference of normalized standard deviations at $b,K$ by $(1+\sqrt2)\sqrt\rho(b^{-1/2}+K^{-1/2})$. Take extrema of the probe over the admissible slopes, widen by this amount, truncate the lower endpoint at zero, then square and divide by $(\ln2)^2$. At a limiting-rate corner, this argument locates subsequential variances at attained slopes. It does not assert all their values agree.

**⟨1⟩3. Bound solver error.** Let $\Delta=\ln(Z^*/\hat Z)$ at one multiplier. Testing the trial prior against optimal columns gives $Ee^{-\Delta}\le1$; testing the optimum against all trial columns gives $Ee^\Delta\le C_{\max}$. Thus $0\le E\Delta\le\ln C_{\max}$ and $E\Delta^2\le C_{\max}-1$. Centering and normalizing bound the error in $\omega_b$ by $\sqrt{(C_{\max}-1)/b}$. An interval certificate needs positive divisors and an outward upper bound for every column.

**⟨1⟩4. Cover the grid gaps.** The cost per symbol of each channel is affine with slope between zero and one, so $g_j$ is 1-Lipschitz. A grid with covering radius $h$ needs retention tolerance $2J_0/j+h+2\delta_f$ when each objective evaluation is accurate to $\delta_f$. Comparing optimal columns at slopes separated by at most $h$ bounds the two exponential score-ratio moments by $1$ and $e^{bh}$. Repeating step 3 gives a grid allowance $\sqrt{(e^{bh}-1)/b}$. Use both solver and grid allowances before squaring.

**⟨1⟩5. Check uniqueness for the direct finite solve.** Two different maximizing slopes would force the optimal penalized cost to be affine between them. The cost of a prior optimal at their midpoint is concave, lies above that affine function and agrees at an interior point. It must coincide on the whole segment. Its second derivative is the negative expected conditional variance of distance. An active word and its complement both have positive mass; on the positive-probability input equal to that word, distances $0,K$ occur with positive probability. This contradicts affinity. Unique optimizing prior at a positive slope gives a unique attained distortion by the envelope derivative.

**⟨1⟩6. Scope of the stopping assertions.** On the low-distortion interval use the exact answer. Above it the uniform-cutoff paragraph assumes interior differentiability of $R$. On a compact slope range, separated near-maximizers would have separated limiting maximizers at a common distortion. At $D=1/2$, the uniform-prior estimate strictly excludes every positive maximizing slope. Uniform continuity and the two cut allowances then force the additive enclosure widths to zero as the probe grows. For relative error at fixed $D$, shrinking widths and a strictly positive target yield $U-L\le2\eta L$. At $K=1$ the criterion $L>0$ cannot fire; the exact value is zero. Positive variance by itself does not collapse a set of distinct possible limits at a nondifferentiability point.

**Forward and reverse check.** The exact finite enclosure needs steps 1–2; a numerical certificate additionally needs steps 3–4 and certified rounding. Step 5 justifies the direct solve. Uniform stopping in step 6 uses the differentiability assumption in the same paragraph. Treat relative stopping at $K=1$ by the direct solution. The finite-precision derivation gives a prescription; the published plots are floating-point evaluations. [Section 5](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L552-L584) · [Appendix B.3](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L798-L823)

## F. The remaining operational question

**⟨1⟩1. Condition on one realized path.** An independent random codebook of $M$ i.i.d. words from $q_n$ misses its distortion ball with probability $(1-q_n(B_D(x)))^M$.

**⟨1⟩2. Identify the missing input.** A sufficiently sharp lower bound on this ball mass for typical *fixed source paths*, combined with the appropriate quantile law for $J_n$, would give an achievability route. The backward representation instead fixes the reproduction and then draws errors. It supplies no such covering bound on its own. Above $D_c$, the path distributional step also remains open.

**Audit status.** Conjecture 1 is explicitly proposed without a proof. There is no proof to convert or to pass to either audit. Neither the numerical sweep nor the limit of the block variances discharges the covering obligation. [Section 6](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex#L673-L682)
