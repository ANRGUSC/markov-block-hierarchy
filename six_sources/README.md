# Figure 11 and Table 4

These files reproduce the six-source comparison in *A Block Hierarchy for Rate-Distortion and Dispersion of Binary Markov Sources*. Each calculation enumerates all stationary binary Markov words of length `K`, with Hamming distortion 0.10 per symbol. The parameters `a` and `b` are the probabilities of transitions from 0 to 1 and from 1 to 0, respectively.

Use Python 3.12 and NumPy. Compiling the figure also requires pdfLaTeX with PGFPlots and geometry. From this directory, run

```text
python -m pip install -r requirements.txt
python reproduce.py --out published
cd published
pdflatex -halt-on-error figure10.tex
```

This draws the manuscript's PGFPlots figure using its printed coordinates and writes Table 4 to `published/table4.csv`. The standard normal row comes from the inverse normal CDF.

To recompute the figure and table from the source laws, return to the directory containing `reproduce.py` and run

```text
python reproduce.py --recompute --out fresh
cd fresh
pdflatex -halt-on-error figure10.tex
```

The fresh run performs 36 independent calculations. It uses the exact tilted-information formula for the two independent sources and a tensor Blahut–Arimoto iteration for the other four. It computes each standardized quantile from the first tilted-information value whose cumulative source probability reaches the specified level. The fair independent source has zero variance, so its standardized quantiles are undefined.

`figure10.csv` contains the manuscript coordinates, the earlier numerical estimates, achieved distortions, and solver gaps. `table4.csv` contains the manuscript's 15 standardized quantiles, the earlier estimates, and the cumulative probabilities immediately below and at each quantile (grouping scores within the original study's numerical tolerance). These reference values are used for comparison after the solve. The numerical inputs are the transition probabilities, block lengths, and target distortion.

`fresh/solver-diagnostics.csv` records the fresh values alongside their references. The solver uses at most 3,000 iterations per multiplier and targets a gap of `2e-8` bits per block. In the reference calculation, the biased persistent source at lengths 10 and 12 and the anti-persistent source at length 12 exceeded this target. The script checks all 15 quantiles at the paper's three-decimal precision and compares the 36 plotted variances with an absolute tolerance of 0.0000033 bits squared per symbol. This tolerance describes numerical agreement with the plot. The dual gap measures optimization error in the objective.
