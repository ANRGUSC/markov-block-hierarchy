"""Check the generated PDFs and point tables against the manuscript and reference plots."""

import argparse
from collections import Counter
from pathlib import Path

import numpy as np
import pymupdf
from build import NAMES
from figures import ROOT, read


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(build, solves):
    for name in NAMES:
        with pymupdf.open(build / (name + ".pdf")) as doc:
            require(
                len(doc) == 1 and len(doc[0].get_text().strip()) > 10,
                f"Empty or invalid {name}.pdf",
            )
    data = build / "data"
    for name, expected, tolerance in [("sweep", 204, 2e-5), ("limit", 68, 5e-6)]:
        rows = read(solves / (name + ".csv"))
        ref = read(ROOT / "reference" / (name + ".csv"))
        require(len(ref) == len(rows) == expected, f"Incomplete {name}")
        for row, original in zip(rows, ref, strict=True):
            require(
                int(row["K"]) == int(original["K"]), f"{name} block length mismatch"
            )
            require(
                abs(float(row["D"]) - float(original["D"])) < 5e-8,
                f"{name} distortion mismatch",
            )
            if name == "sweep":
                require(float(row["p"]) == float(original["p"]), "Source mismatch")
        errors = [
            abs(float(row["variance"]) - float(r["plot_variance"]))
            for row, r in zip(rows, ref)
        ]
        max_column = max(float(r["column_violation"]) for r in rows)
        d_error = max(abs(float(r["D_actual"]) - float(r["D"])) for r in rows)
        print(
            f"{name}: {len(rows)} points; maximum absolute difference from reference artwork "
            f"{max(errors):.6g}; maximum positive column violation {max_column:.6g}; "
            f"maximum distortion difference {d_error:.6g}."
        )
        require(
            np.isfinite(errors).all() and max(errors) < tolerance,
            f"{name} variance mismatch",
        )
        require(
            max_column < 1e-5 and d_error < (1e-7 if name == "sweep" else 3e-5),
            f"{name} solver check failed",
        )
        if name == "sweep":
            require(
                Counter(r["method"] for r in rows)
                == {"full support": 75, "two constants": 75, "tensor optimization": 54},
                "Unexpected sweep branch counts",
            )
    table = read(data / "table3.csv")
    require(
        [[r[str(k)] for k in [2, 8, 10, 12, 18, 22]] for r in table]
        == [
            ["0.00809", "0.04067", "0.08513", "0.07272", "0.05960", "0.06177"],
            ["0.02845", "0.10852", "0.11180", "0.11059", "0.10849", ""],
        ],
        "Table 3 mismatch",
    )
    t4 = read(data / "table4.csv")
    ref = read(ROOT / "six_sources" / "table4.csv")
    for r in ref:
        row = next(x for x in t4 if x["source"] == r["source"])
        col = f"{round(100 * float(r['alpha']))}th"
        require(row[col] == r["paper_quantile"], "Table 4 mismatch")
    changes = [r for r in read(data / "support-changes.csv") if int(r["K"]) == 4]
    require(
        [r["class_removed"] for r in changes]
        == ["0101", "0010", "0110", "0001", "0011"],
        "Support order mismatch",
    )
    np.testing.assert_allclose(
        [float(r["D"]) for r in changes],
        [0.0058345, 0.010672, 0.03385, 0.059816, 0.097508],
        atol=5.1e-7,
        rtol=0.0,
    )
    for r in read(data / "varentropy.csv")[:1]:
        np.testing.assert_allclose(
            [float(r["limit"]), float(r["leading_gap"])],
            [1.1930, 1.12039],
            atol=5e-5,
            rtol=0.0,
        )
    for d in (0.002, 0.35):
        mass = [r for r in read(data / "histogram.csv") if float(r["D"]) == d]
        require(
            len(mass) == (12 if d == 0.002 else 7), "Wrong number of histogram atoms"
        )
        np.testing.assert_allclose(
            sum(float(r["mass"]) for r in mass), 1.0, atol=1e-12, rtol=0.0
        )
        np.testing.assert_allclose(
            sum(float(r["mass"]) * float(r["centered_score_bits"]) for r in mass),
            0.0,
            atol=1e-11,
        )
    enc = read(data / "enclosure.csv")
    require(
        all(0 <= float(r["lower"]) <= float(r["upper"]) for r in enc),
        "Invalid enclosure",
    )
    print(
        "Verified thirteen figure PDFs, both numerical tables, the support ladder, varentropy, and both probability distributions."
    )


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--build", type=Path, default=Path("build"))
    cli.add_argument("--solves", type=Path, default=ROOT / "data")
    args = cli.parse_args()
    verify(args.build, args.solves)
