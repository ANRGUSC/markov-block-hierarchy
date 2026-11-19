# A Block Hierarchy for Rate-Distortion and Dispersion of Binary Markov Sources

Code, reference data, and manuscript source for Bhaskar Krishnamachari's [arXiv:2603.07435](https://arxiv.org/abs/2603.07435). This repository builds all thirteen figures and the numerical values in Tables 3 and 4. The [compiled manuscript](paper/manuscript.pdf) uses the figure files in [paper/figures](paper/figures) and draws Figure 11 directly in LaTeX.

The [proof companion](proofs/) gives a Lamport-style proof and a step-by-step audit for each of the ten numbered results.

## Build the figures

Use Python 3.12 and pdfLaTeX with PGFPlots. The numerical environment is pinned in `requirements.txt`. Run the following in the repository root, preferably inside a virtual environment.

```sh
python -m pip install -r requirements.txt
python build.py
python verify.py
```

The thirteen PDFs are written to `build/`. This command computes the analytic curves and distributions and draws the larger numerical figures using the solver outputs included in the repository. It also writes the underlying analytic values, the limiting-variance enclosure, and both numerical tables to `build/data/`.

## Repeat the numerical experiments

```sh
python recompute.py --workers 2 --out build/data
python build.py --from-solves
python verify.py --solves build/data
```

The first command recomputes the 204 Figure 12 points and the 68 plotted vertices for the two longer block lengths in Figure 10. Some vertices coincide at plot resolution. The largest numerical optimization uses all 4,194,304 binary words of length 22. Lower the worker count on a memory-constrained machine. Completed points are checkpointed individually under `build/data/work/`. Use a new output directory for a fresh calculation. For example, run `python recompute.py --out fresh/data`, then `python build.py --from-solves --out fresh` and `python verify.py --build fresh --solves fresh/data`.

The second command also recomputes all 36 six-source variance values and the 15 standardized quantiles. The fair independent source has zero variance and thus has no standardized quantiles. The paper reports Figure 11 coordinates to eight decimals and Table 4 to three. The six-source solver writes achieved distortion, optimization gap, and convergence status for each point to `build/six-source/solver-diagnostics.csv`. Three of the six-source reference runs exceed their target gap of `2e-8` bits per block.

## Figure guide

| Figure | Calculation or diagram | Implementation or data |
| --- | --- | --- |
| 1 | Dependence across a boundary between two three-symbol blocks | `diagrams` in [figures.py](figures.py) |
| 2 | Full-support thresholds, the exact low-distortion variance curve, and the one-path coding result | `regimes` in [figures.py](figures.py), with `threshold` and `nu` in [model.py](model.py) |
| 3 | Overview of the results from short blocks to one Markov path | [overview.py](overview.py), using the six-source variance data |
| 4 | First loss of two-symbol support in bias/persistence and transition-probability coordinates | `support` in [figures.py](figures.py) |
| 5 | Four-symbol support ladder at flip probability 0.1 | Class allocation and transition searches in [short_blocks.py](short_blocks.py) |
| 6 | Per-symbol rate and variance curves through four symbols, including support-change markers | [short_blocks.py](short_blocks.py) |
| 7 | Prefix recursion below and above the critical distortion | `regimes` in [figures.py](figures.py) |
| 8 | Finite-block varentropy and its first-order correction for a biased chain | `varentropy` in [figures.py](figures.py) |
| 9 | Dependencies among the variance-limit and coding results | `diagrams` in [figures.py](figures.py) |
| 10 | Short-block curves, longer-block optimized points, low-distortion plateau, and two-symbol enclosure | [build.py](build.py), [long-block data](data/limit.csv) |
| 11 | Six stationary sources at common distortion 0.10 | [PGFPlots source and six-source calculation](six_sources/) |
| 12 | Seven sources, three distortions, 204 evaluated block problems | [solver](optimize_block.py), [pointwise results](data/sweep.csv) |
| 13 | Centered tilted-information distributions on all 4,096 length-12 inputs at distortions 0.002 and 0.35 | `histogram` in [figures.py](figures.py) |

Table 3 selects two sources from the Figure 12 sweep. Table 4 uses the weighted discrete quantiles of the Figure 11 calculation. The remaining manuscript tables describe the method, list four-symbol classes, or state the workshop stabilization criteria.

## Data provenance and numerical checks

The [reference directory](reference/) preserves the earlier figure artwork. The Figure 10 and Figure 12 CSVs there recover plotting coordinates from vector paths at the artwork's precision. They specify the sampling grid and give an independent comparison for the recalculation. Figure 10's trial multipliers were recovered from the curves and checked by forward calculation. The solver uses the source law, Hamming distance, block length and the target distortion or trial multiplier. It does not fit the plotted variances.

The [data directory](data/) holds fresh solver outputs in bits squared per symbol. The Figure 12 sweep uses the entropy/varentropy formula at 75 points, a verified two-constant reproduction law at 75, and tensor optimization at 54. For a numerical solve, the last column records the maximum positive violation over all reproduction words, including zero-mass words. Full-support rows use the analytic feasibility test. A two-constant candidate must pass the same all-column test before its variance is accepted. The numerical enclosure in Figure 10 is evaluated in floating point.

`verify.py` checks the two grids against the earlier artwork, the solver diagnostics, all displayed entries in Tables 3 and 4, the four-symbol thresholds, the varentropy limit and correction, and the probability normalization and centering in Figure 13.

## Compile the manuscript

From `paper/`, run `pdflatex -halt-on-error Block_Hierarchy_General_K.tex` twice. The bibliography is embedded in the source. Figure 11 uses PGFPlots. The twelve external figures are included as PDFs.
