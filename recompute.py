"""Recompute the long-block points in Figures 10 and 12 from the Markov law."""

import argparse
import csv
import json
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

# A single fit uses matrix-vector operations. Parallelize across independent fits.
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
from model import analytic, threshold
from optimize_block import BlockProblem, calculate

ROOT = Path(__file__).resolve().parent


def jobs():
    points = []
    for name in ("sweep", "limit"):
        with (ROOT / "reference" / f"{name}.csv").open() as f:
            for index, row in enumerate(csv.DictReader(f)):
                k = int(row["K"])
                d = float(row["D"])
                p = float(row.get("p", 0.35))
                if name == "limit" and abs(d - threshold(p, k)) < 5e-8:
                    d = threshold(p, k)
                trial = row.get("trial_u")
                points.append((name, index, p, k, d, float(trial) if trial else None))
    return points


def run(job):
    name, index, p, k, d, u = job
    if u is None:
        result = calculate(p, k, d)
    else:
        result = analytic(p, k, d)
        if result is None:
            problem = BlockProblem(p, k)
            _, result = problem.optimum(u, problem.initial(u))
        if abs(result["D_actual"] - d) > 3e-5 or result["column_violation"] > 1e-5:
            raise ArithmeticError(f"Figure 10 point {index}: {result}")
    return dict(figure=name, index=index, p=p, K=k, D=d, **result)


def assemble(points, cache, out):
    out.mkdir(exist_ok=True, parents=True)
    for name in ("limit", "sweep"):
        files = [cache / f"{n}-{i}.json" for n, i, *_ in points if n == name]
        if not all(f.exists() for f in files):
            continue
        rows = [json.loads(f.read_text()) for f in files]
        with (out / f"{name}.csv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0])
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--out", type=Path, default=Path("build/data"))
    parser.add_argument("--min-k", type=int, default=1)
    parser.add_argument("--max-k", type=int, default=24)
    args = parser.parse_args()
    cache = args.out / "work"
    cache.mkdir(parents=True, exist_ok=True)
    points = jobs()
    todo = [
        job
        for job in points
        if args.min_k <= job[3] <= args.max_k
        and not (cache / f"{job[0]}-{job[1]}.json").exists()
    ]
    # Only a few high-K points need a large working set; cap workers on small machines.
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        pending = {pool.submit(run, job): job for job in todo}
        for future in as_completed(pending):
            row = future.result()
            target = cache / f"{row['figure']}-{row['index']}.json"
            temp = target.with_suffix(".part")
            temp.write_text(json.dumps(row, allow_nan=False))
            temp.replace(target)
            print(
                f"{len(todo) - len(pending) + 1}/{len(todo)} {row['figure']} K={row['K']} D={row['D']:.6f} {row['method']}",
                flush=True,
            )
            del pending[future]
    assemble(points, cache, args.out)
