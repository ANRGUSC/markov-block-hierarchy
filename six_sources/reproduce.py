"""Redraw the published values, or recompute them from the six source laws."""

import argparse
import csv
import shutil
from concurrent.futures import ProcessPoolExecutor
from itertools import groupby
from pathlib import Path
from statistics import NormalDist

import numpy as np
from solve import GAP_TARGET, tilted_distribution

ROOT = Path(__file__).resolve().parent
LEVELS = (0.90, 0.95, 0.99)


def read_csv(filename):
    with (ROOT / filename).open(newline="") as stream:
        return list(csv.DictReader(stream))


def compute(row):
    k = int(row["K"])
    p, tilted, gap, achieved = tilted_distribution(
        float(row["a"]), float(row["b"]), k, float(row["D"])
    )
    if abs(p.sum() - 1) > 1e-12:
        raise ValueError("Source probabilities do not sum to one")
    centered = tilted - p @ tilted
    variance = float(p @ (centered**2))
    if np.ptp(tilted) == 0:
        variance = 0.0
    percentiles = []
    if k == 12 and variance > 0:
        order = np.argsort(tilted)
        cumulative = np.cumsum(p[order])
        for alpha in LEVELS:
            index = order[np.searchsorted(cumulative, alpha, side="left")]
            percentiles.append(centered[index] / np.sqrt(variance))
    return variance / k, gap, achieved, percentiles


def write_panels(out, rows, percentiles):
    shutil.copyfile(ROOT / "figure10.tex", out / "figure10.tex")
    for series, points in groupby(rows, key=lambda row: row["series"]):
        with (out / f"series-{series}.dat").open("w") as stream:
            print("K variance", file=stream)
            for row in points:
                print(row["K"], row["variance"], file=stream)
    with (out / "table4.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["source", "a", "b", "90th", "95th", "99th"])
        writer.writerow(
            [
                "Standard normal",
                "",
                "",
                *(f"{NormalDist().inv_cdf(q):.3f}" for q in LEVELS),
            ]
        )
        for (source, a, b), values in percentiles.items():
            writer.writerow([source, a, b, *(f"{v:.3f}" for v in values)])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recompute", action="store_true", help="Run fresh numerical solves"
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--out", type=Path, default=Path("build"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rows = read_csv("figure10.csv")
    table = read_csv("table4.csv")
    percentiles = {}
    for row in table:
        key = row["source"], float(row["a"]), float(row["b"])
        percentiles.setdefault(key, []).append(float(row["paper_quantile"]))
    for row in rows:
        row["variance"] = row["paper_variance"]

    if args.recompute:
        errors = []
        matches = 0
        missed = 0
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            for row, (variance, gap, achieved, values) in zip(
                rows, pool.map(compute, rows)
            ):
                key = row["source"], float(row["a"]), float(row["b"])
                errors.append(abs(variance - float(row["paper_variance"])))
                row.update(
                    variance=variance,
                    fresh_gap_bits=gap,
                    fresh_target_met=gap <= GAP_TARGET,
                    fresh_achieved_D=achieved,
                )
                missed += int(gap > GAP_TARGET)
                if values:
                    matches += sum(
                        f"{v:.3f}" == f"{ref:.3f}"
                        for v, ref in zip(values, percentiles[key], strict=True)
                    )
                    percentiles[key] = values
                print(
                    f"{row['source']}, K={row['K']}, variance={variance:.8f}, gap={gap:.3g}",
                    flush=True,
                )
        with (args.out / "solver-diagnostics.csv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(
            f"Maximum absolute variance difference: {max(errors):.9g}. "
            f"Quantiles matching at printed precision: {matches}/15. Solver targets missed: {missed}/36."
        )
        if len(errors) != 36 or max(errors) > 3.3e-6 or matches != 15:
            raise SystemExit(
                "Comparison with the manuscript exceeded the reproduction tolerance."
            )
    write_panels(args.out, rows, percentiles)


if __name__ == "__main__":
    main()
