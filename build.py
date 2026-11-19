"""Build all thirteen figures and Tables 3 and 4 in an empty output directory."""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from figures import (
    BLUE,
    ORANGE,
    PURPLE,
    ROOT,
    TEAL,
    diagrams,
    histogram,
    read,
    regimes,
    save,
    short_curves,
    support,
    varentropy,
    write,
)
from model import critical, entropy, nu
from overview import draw_overview
from scipy.optimize import brentq
from short_blocks import at_weight

NAMES = [
    "construction",
    "overview",
    "regimes",
    "support",
    "ladder",
    "shortblocks",
    "recursion",
    "varentropy",
    "dependencies",
    "limit",
    "figure10",
    "sweep",
    "histogram",
]


def probe(t, p):
    # Dual objective per symbol in nats and standard deviation in bits/sqrt(symbol).
    u = np.exp(-t)
    d = u / (1 + u)
    switch = (1 - np.sqrt(1 - 2 * p)) / 2
    if d <= switch:
        f = (1 + entropy(p)) * np.log(2) / 2 - np.log1p(u)
        variance = nu(p) / 2
    else:
        z = (1 + u * u) / 2
        f = -((1 - p) * np.log(z) - p * t) / 2
        variance = p * (1 - p) * ((np.log(z) + t) / np.log(2)) ** 2 / 2
    return f, np.sqrt(variance)


def enclosure(d, p):
    dc = critical(p)
    if d <= dc:
        return nu(p), nu(p)
    switch = (1 - np.sqrt(1 - 2 * p)) / 2
    if d <= switch:
        u = d / (1 - d)
    else:
        error = (d - p / 2) / (1 - p)
        u = np.sqrt(error / (1 - error))
    optimum = -np.log(u)

    def level(t):
        return probe(t, p)[0] - t * d

    cutoff = level(optimum) - (1 - entropy(p)) * np.log(2) / 2
    end = np.log(2) / d

    def objective(t):
        return level(t) - cutoff

    lo = 0 if objective(0) >= 0 else brentq(objective, 0, optimum)
    hi = end if objective(end) >= 0 else brentq(objective, optimum, end)
    allowance = (1 + np.sqrt(2)) * np.sqrt((1 - 2 * p) / 2) / np.log(2)
    return max(0, probe(lo, p)[1] - allowance) ** 2, (probe(hi, p)[1] + allowance) ** 2


def long_figures(out, data, source_dir):
    p = 0.35
    dc = critical(p)
    fig, (ax, bx) = plt.subplots(
        1, 2, figsize=(8.5, 3.3), width_ratios=[1.45, 1], layout="constrained"
    )
    for k, color, style in [(2, BLUE, "-"), (4, ORANGE, "--")]:
        curve = [
            at_weight(p, k, u) for u in np.r_[0, np.linspace(0.001, 0.995, 321), 1.0]
        ]
        ax.plot(
            [r[0] for r in curve],
            [r[2] for r in curve],
            style,
            color=color,
            label=f"$K={k}$",
        )
    table = read(source_dir / "limit.csv")
    for k, color, marker in [(8, TEAL, "^"), (16, PURPLE, "d")]:
        rows = [r for r in table if int(r["K"]) == k]
        ax.plot(
            [float(r["D_actual"]) for r in rows],
            [float(r["variance"]) for r in rows],
            marker=marker,
            ls="--" if k == 8 else ":",
            ms=2.6,
            color=color,
            label=f"$K={k}$",
        )
    ax.plot([0, dc], [nu(p)] * 2, "k-", label=r"$\nu(p)$")
    ax.axvline(dc, color=".65", ls=":", lw=0.8)
    ax.legend(frameon=False, ncol=2, fontsize=8)
    ax.set(
        xlim=(0, 0.5),
        ylim=(0, 0.21),
        xlabel="Distortion $D$",
        ylabel="Variance (bits² per symbol)",
    )
    ds = np.r_[np.linspace(0, dc, 24), np.linspace(dc + 1e-10, 0.5 - 1e-12, 220)]
    bounds = np.array([enclosure(d, p) for d in ds])
    write(data / "enclosure.csv", ["D", "lower", "upper"], zip(ds, *bounds.T))
    bx.fill_between(ds, bounds[:, 0], bounds[:, 1], color="#deebf2")
    bx.plot(ds[24:], bounds[24:, 1], color=BLUE)
    bx.plot([0, dc], [nu(p)] * 2, "k-")
    bx.text(0.28, 0.65, "Two-symbol\nenclosure", color=BLUE, ha="center")
    bx.set(
        xlim=(0, 0.5),
        ylim=(0, 3),
        xlabel="Distortion $D$",
        ylabel="Limiting variance (bits² per symbol)",
    )
    save(fig, out, "limit")
    rows = read(source_dir / "sweep.csv")
    fig, axes = plt.subplots(
        2, 4, figsize=(9.2, 4.6), layout="constrained", sharex=True, sharey=True
    )
    for p, ax in zip([0.01, 0.05, 0.1, 0.2, 0.35, 0.45, 0.49], axes.flat):
        for d, color, marker in zip([0.05, 0.2, 0.35], [BLUE, ORANGE, TEAL], "os^"):
            series = [r for r in rows if float(r["p"]) == p and float(r["D"]) == d]
            ax.semilogy(
                [int(r["K"]) for r in series],
                [float(r["variance"]) for r in series],
                color=color,
                marker=marker,
                ms=2.8,
                lw=1.1,
                label=f"$D={d:.2f}$",
            )
        ax.set(title=f"$p={p:.2f}$", xticks=[2, 8, 16, 24], ylim=(1e-5, 1.5))
        ax.grid(axis="y", alpha=0.25)
        if p == 0.49:
            ax.text(
                0.50,
                0.65,
                "All three curves coincide",
                ha="center",
                transform=ax.transAxes,
                fontsize=7,
            )
    axes.flat[-1].axis("off")
    axes.flat[-1].legend(
        *axes.flat[0].get_legend_handles_labels(), loc="center", frameon=False
    )
    fig.supxlabel("Block length $K$", fontsize=10)
    fig.supylabel("Variance (bits² per symbol)", fontsize=10)
    save(fig, out, "sweep")
    index = {
        (float(r["p"]), float(r["D"]), int(r["K"])): float(r["variance"]) for r in rows
    }
    counts = [2, 8, 10, 12, 18, 22]
    write(
        data / "table3.csv",
        ["p", *counts],
        [
            [
                p,
                *[
                    f"{index[p, 0.2, k]:.5f}" if (p, 0.2, k) in index else ""
                    for k in counts
                ],
            ]
            for p in [0.1, 0.2]
        ],
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("build"))
    parser.add_argument(
        "--from-solves",
        action="store_true",
        help="Use long-block CSVs from recompute.py and rerun all six-source solves.",
    )
    args = parser.parse_args()
    out = args.out.resolve()
    data = out / "data"
    data.mkdir(exist_ok=True, parents=True)
    diagrams(out)
    regimes(out, data)
    support(out, data)
    short_curves(out, data)
    varentropy(out, data)
    histogram(out, data)
    source_dir = data if args.from_solves else ROOT / "data"
    long_figures(out, data, source_dir)
    six = out / "six-source"
    command = [
        sys.executable,
        str(ROOT / "six_sources" / "reproduce.py"),
        "--out",
        str(six),
    ]
    if args.from_solves:
        command.append("--recompute")
    subprocess.run(command, check=True)
    with (six / "build-transcript.txt").open("w") as transcript:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "figure10.tex"],
            cwd=six,
            stdout=transcript,
            check=True,
        )
    draw_overview(out / "overview.pdf", six / "series-3.dat")
    shutil.copyfile(six / "figure10.pdf", out / "figure10.pdf")
    shutil.copyfile(six / "table4.csv", data / "table4.csv")
    print(f"Generated {len(NAMES)} PDFs in {out}")


if __name__ == "__main__":
    main()
