# Proof companion to *A Block Hierarchy for Rate–Distortion and Dispersion of Binary Markov Sources*

This companion gives structured proofs for the ten numbered results in the [manuscript](../paper/manuscript.pdf). Each proof links to the exact statement, identifies the source of each step, checks the argument from its assumptions forward, and traces the conclusion back to the steps it requires. The audit found support for all ten results under their stated hypotheses. Two scope qualifications in the surrounding text are discussed below. These are model-assisted mathematical audits; no proof-assistant kernel has checked them.

## Read the proofs

| Result | Forward audit | Reverse audit |
|---|---|---|
| [Proposition 1 · First support change](01-first-support-change.md) | PASS | FOLLOWS |
| [Theorem 2 · Persistent two-symbol source](02-persistent-pair.md) | PASS | FOLLOWS |
| [Theorem 3 · Three-symbol rate and variance](03-three-symbols.md) | PASS | FOLLOWS |
| [Theorem 4 · Four-symbol rate and variance](04-four-symbols.md) | PASS | FOLLOWS |
| [Proposition 5 · Full-support threshold](05-prefix-recursion.md) | PASS | FOLLOWS |
| [Theorem 6 · Finite-block varentropy](06-varentropy.md) | PASS WITH MINOR ISSUES | FOLLOWS |
| [Lemma 7 · One cut at a common multiplier](07-one-cut.md) | PASS | FOLLOWS |
| [Theorem 8 · Positive variance limit](08-variance-limit.md) | PASS | FOLLOWS |
| [Corollary 9 · Quantitative positivity](09-quantitative-positivity.md) | PASS | FOLLOWS |
| [Proposition 10 · Low-distortion converse for one path](10-coding-converse.md) | PASS | FOLLOWS |

The common-slope and fixed-distortion parts of Theorem 8 have different dependencies. To inspect that argument, read Lemma 7, then steps 1–4 of Theorem 8. Read Corollary 9 next, then return to steps 5–8 of Theorem 8. This order exposes exactly which part of convergence is needed to prove positivity. Proposition 10 has its own route through Proposition 5, the binomial flip count and a one-path converse.

[Supporting calculations](supporting-calculations.md) cover the column tests, independence and symmetry reductions, entropy and rate brackets, fixed-distortion slope bound, finite-precision enclosure, stopping criteria, and the covering question in Section 6. Conjecture 1 still requires matching achievability. Above the critical distortion, the proposed route also needs a distributional result for the path score.

## Two scope qualifications

- **Variance at a biased zero-rate endpoint.** The inverse-channel formula (8) uses a particular slope. For independent Bernoulli$(1/4)$ bits at $D=1/4$, it gives a variance of about $0.47102$ bits squared per symbol at the backward-channel slope. Section 2.1 assigns variance zero at that same distortion by choosing slope zero. The first-zero statement following (8) should specify an interior support threshold or name the chosen slope. Theorem 6 is stated on the branch where (8) holds. [Calculation A.4](supporting-calculations.md#a-optimality-and-the-entropy-equality-branch)
- **Relative error at block length one.** The fair one-symbol source has variance exactly zero, so the stopping test requiring a positive lower endpoint cannot fire there. The direct value handles this case. For long blocks, the relative-width argument at a fixed distortion uses a shrinking enclosure as well as positivity. The uniform-cutoff paragraph assumes interior differentiability of the limiting rate. [Calculation E.6](supporting-calculations.md#e-slope-enclosures-solver-residuals-and-stopping)

## Audit inputs and reproducible checks

The source links are pinned to the [audited manuscript revision](https://github.com/ANRGUSC/markov-block-hierarchy/blob/2ec774c3eb6f326f6ecf36819725d1be60a6b6ac/paper/Block_Hierarchy_General_K.tex). The accompanying revision adds the availability link to the manuscript. The audit used the conversion, forward and reverse skills from [WWresearch Lamport Proof v0.2.0](https://github.com/WWresearch/lamport-proof/tree/c5466f44d6ef0fff983ad67a46bc54e39858826f). A source-mapping verdict describes fidelity to the draft. Forward and reverse verdicts concern the mathematics of the supplied route. Accepted background includes the finite-alphabet entropy identities and convex optimality conditions used in the paper, elementary probability and analysis, and the specifically cited external coding theorem where its hypotheses are checked.

From the repository root, run the following with Python 3.

~~~sh
python proofs/check_examples.py
~~~

The script compares the prefix recursion with exact rational inverse-channel calculations at 105 parameter settings, tests an exact boundary zero and its negative extension, compares the covariance formula with direct word enumeration in 24 cases, and reproduces the biased endpoint calculation. These finite checks complement the general arguments above.
