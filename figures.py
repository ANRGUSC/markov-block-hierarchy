"""Render the manuscript diagrams and compute the analytic figure data."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from model import constant, critical, nu, threshold, words
from short_blocks import at_weight, transitions

ROOT = Path(__file__).resolve().parent
BLUE, ORANGE, TEAL, PURPLE = "#275687", "#ad5024", "#177569", "#744773"
COLORS = [BLUE, ORANGE, TEAL, PURPLE]
plt.rcParams.update(
    {
        "font.family": "DejaVu Serif",
        "font.size": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "mathtext.fontset": "dejavuserif",
    }
)


def read(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write(path, header, rows):
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def save(fig, out, name):
    fig.savefig(out / (name + ".pdf"), bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def diagrams(out):
    fig, ax = plt.subplots(figsize=(7.3, 1.65))
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    for y, title, first, second in [
        (
            0.74,
            "Markov path",
            r"$X_1\ \to\ X_2\ \to\ X_3$",
            r"$X_4\ \to\ X_5\ \to\ X_6$",
        ),
        (
            0.23,
            "Independent blocks",
            r"$X^1_1\ \to\ X^1_2\ \to\ X^1_3$",
            r"$X^2_1\ \to\ X^2_2\ \to\ X^2_3$",
        ),
    ]:
        ax.text(0.22, y, title, ha="right", va="center")
        for x, label in ((0.39, first), (0.85, second)):
            ax.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                bbox=dict(boxstyle="round,pad=.45", fc="#eff4f6", ec=BLUE),
            )
    ax.annotate(
        "", (0.72, 0.74), (0.52, 0.74), arrowprops=dict(arrowstyle="->", color=ORANGE)
    )
    ax.text(0.62, 0.86, r"$I_0$ bits", ha="center", color=ORANGE)
    ax.text(0.62, 0.23, r"$\perp\!\!\!\perp$", ha="center")
    ax.text(0.62, 0.05, "0 bits", ha="center")
    save(fig, out, "construction")
    fig, ax = plt.subplots(figsize=(8.2, 2.95))
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    nodes = [
        (0.15, 0.87, "One-cut bound\nLemma 7"),
        (0.49, 0.87, "Variance limit\nat a common slope"),
        (0.15, 0.57, "Rate bracket\nand differentiability"),
        (0.85, 0.57, "Positive limit at fixed $D$\nTheorem 8"),
        (0.15, 0.29, "Gain across a cut\nAppendix B.2"),
        (0.49, 0.29, "Strict positivity\nCorollary 9"),
        (0.26, 0.045, "Binomial flip law and\ntilted-information converse"),
        (0.78, 0.045, "Pathwise converse for $0<D\\leq D_c$\nProposition 10"),
    ]
    boxes = []
    for i, (x, y, label) in enumerate(nodes):
        boxes.append(
            ax.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                bbox=dict(
                    boxstyle="round,pad=.42",
                    fc=[
                        "#edf3f7",
                        "#e4efec",
                        "#edf3f7",
                        "#dcece8",
                        "#edf3f7",
                        "#e4efec",
                        "#edf3f7",
                        "#faede1",
                    ][i],
                    ec="#8596a3",
                ),
            )
        )
    fig.canvas.draw()
    for a, b in [(0, 1), (1, 3), (2, 3), (4, 5), (5, 3), (6, 7)]:
        ax.annotate(
            "",
            nodes[b][:2],
            nodes[a][:2],
            arrowprops=dict(
                arrowstyle="->",
                color=BLUE,
                patchA=boxes[a].get_bbox_patch(),
                patchB=boxes[b].get_bbox_patch(),
            ),
        )
    save(fig, out, "dependencies")


def regimes(out, data):
    p = 0.35
    ks = np.arange(2, 25)
    ds = [threshold(p, k) for k in ks]
    dc = critical(p)
    write(
        data / "regimes.csv", ["K", "D_full", "D_critical"], zip(ks, ds, [dc] * len(ks))
    )
    # Both panels use actual integer block lengths for the same source.
    variance = nu(p)
    lengths = np.arange(1, ks[-1] + 1)
    fig = plt.figure(figsize=(7.35, 3.9))
    upper = fig.add_axes([0.088, 0.68, 0.396, 0.235])
    lower = fig.add_axes([0.088, 0.29, 0.396, 0.235])
    for ax in (upper, lower):
        ax.set_xlim(0.5, 24.5)
        ax.set_xticks([2, 8, 16, 24])
        ax.tick_params(length=2, width=0.7, labelsize=8)
        ax.spines[["bottom", "left"]].set_color("#667580")

    upper.fill_between(ks, 0, ds, color="#e2f0eb")
    upper.plot(ks, ds, ".-", color=TEAL, lw=1.5, ms=4)
    upper.axhline(dc, color="0.30", lw=1, ls="--")
    upper.set(ylim=(0, 0.255), yticks=[0, 0.1, 0.2], ylabel=r"Distortion $D$")
    upper.text(9, dc + 0.027, rf"$D_c={dc:.3f}$", color="0.20", fontsize=9)
    upper.set_xlabel(r"Block length $K$", fontsize=8.5, labelpad=1.5)

    lower.plot(lengths, (1 - 1 / lengths) * variance, ".-", color=BLUE, lw=1.5, ms=4)
    lower.axhline(variance, color="0.30", lw=1, ls="--")
    lower.set(ylim=(-0.007, 0.233), yticks=[0, 0.1, 0.2],
              ylabel=r"$v_K$ (bits$^2$/symbol)")
    lower.text(8, variance + 0.015, rf"Limit $={variance:.3f}$", color="0.20", fontsize=9)
    lower.set_xlabel(r"Block length $K$", fontsize=8.5, labelpad=1.5)

    text_x = 0.55
    fig.text(text_x, 0.90, "When does the exact formula apply?", fontsize=11,
             fontweight="bold", color=TEAL)
    fig.text(text_x, 0.848,
             "The upper edge of the shaded region is the\n"
             "full-support threshold. As blocks grow, it\n"
             "falls toward Gray's critical distortion, $D_c$.",
             fontsize=9.7, va="top", linespacing=1.35)
    fig.text(text_x, 0.512, "What happens to the variance?", fontsize=11,
             fontweight="bold", color=BLUE)
    fig.text(text_x, 0.458,
             r"At $D=0.05$, $v_K=(1-1/K)\,\nu(p)$." "\n"
             "A positive limit also exists at every interior\n"
             r"$D$ where the rate $R(D)$ is differentiable.",
             fontsize=9.7, va="top", linespacing=1.35)
    fig.add_artist(plt.Line2D([0.02, 0.985], [0.145, 0.145],
                              transform=fig.transFigure, color="#a5b2b4", lw=0.8))
    fig.text(0.023, 0.078, "One Markov path", fontsize=10.7, fontweight="bold",
             color=ORANGE)
    fig.text(0.285, 0.104,
             r"For $0<D\leq D_c$, the limit gives a second-order lower bound on rate." "\n"
             "Whether codes can attain this coefficient remains open.",
             fontsize=9.5, va="top", linespacing=1.3)
    save(fig, out, "regimes")
    fig, axes = plt.subplots(1, 2, figsize=(7, 2.8), layout="constrained")
    rows = []
    for d, ax in zip([0.05, 0.17], axes):
        z = 1 - 2 * d
        rho = 1 - 2 * p

        def update(h):
            return rho * (1 - z * h) / (z - h)

        x = np.linspace(0, z - 1e-5, 1600)
        ax.plot(x, update(x), color=BLUE)
        ax.plot([0, 1], [0, 1], ":", color=".3")
        ax.axvline(z, ls="--", color=TEAL)
        h = 0.0
        nodes = [(h, h)]
        for i in range(48):
            new = update(h)
            rows.append((d, i + 1, h, new))
            nodes.extend([(h, new), (new, new)])
            if new >= z or abs(new - h) < 1e-12:
                break
            h = new
        ax.plot(*zip(*nodes), color=ORANGE, lw=1.2)
        ax.set(
            xlim=(0, 1),
            ylim=(0, 1),
            aspect="equal",
            xlabel="$H_i$",
            ylabel="$H_{i+1}$",
            title=f"$D={d}$",
        )
    write(data / "recursion.csv", ["D", "i", "H_i", "H_next"], rows)
    save(fig, out, "recursion")


def support(out, data):
    x = np.linspace(-1, 1, 601)
    y = np.linspace(0.0001, 0.9999, 501)
    rho, pi = np.meshgrid(x, y)
    a = (1 - rho) * pi
    b = (1 - rho) * (1 - pi)
    valid = (a <= 1) & (b <= 1)
    kind = np.where(valid, np.where(rho < 0, np.where(pi > 0.5, 2, 1), 3), 0)
    kind[valid & (rho < 0) & np.isclose(pi, 0.5)] = 4  # Both constant words leave.
    kind[rho == 0] = 5  # Independent source reaches its zero-rate threshold.
    t = np.linspace(0.0001, 0.9999, 501)
    a, b = np.meshgrid(t, t)
    pi = a / (a + b)
    rho = 1 - a - b
    C = (1 - rho) * pi * (1 - pi)
    A = 1 - pi - C
    B = pi - C
    # Rationalized first root of the rarer constant-word quadratic.
    u = np.minimum(A, B) / (C + np.sqrt(np.maximum(0, C * C - A * B)))
    d = np.where(rho > 1e-12, (1 - np.sqrt(np.maximum(0, 1 - 4 * C))) / 2, u / (1 + u))
    d = np.where(abs(rho) < 1e-12, np.minimum(pi, 1 - pi), d)
    np.savez_compressed(
        data / "support.npz",
        rho_axis=x,
        pi1_axis=y,
        region=kind,
        transition_axis=t,
        D_first=d,
    )
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(8, 3.3), layout="constrained")
    ax.imshow(
        kind,
        extent=(-1, 1, 0, 1),
        origin="lower",
        aspect="auto",
        interpolation="nearest",
        cmap=ListedColormap(
            ["#e9e9e9", "#f7dfce", "#d7ebe6", "#d3e2f3", "#666666", "#666666"]
        ),
    )
    negative = x[x < 0]
    ax.plot(negative, 1 / (1 - negative), color=".5", lw=0.7)
    ax.plot(negative, 1 - 1 / (1 - negative), color=".5", lw=0.7)
    ax.axvline(0, color=".4", ls="--", lw=0.8)
    ax.axhline(0.5, color=".4", lw=0.8)
    for xx, yy, label in [
        (-0.2, 0.61, "00"),
        (-0.2, 0.39, "11"),
        (0.55, 0.75, "01, 10"),
        (0.55, 0.25, "01, 10"),
    ]:
        ax.text(
            xx,
            yy,
            label,
            ha="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1),
        )
    ax.set(
        xticks=[-1, -0.5, 0, 0.5, 1],
        xlabel=r"Persistence $\rho$",
        ylabel=r"Stationary bias $\pi_1$",
        title="(a) Two-symbol support",
    )
    im = bx.imshow(
        d,
        extent=(0, 1, 0, 1),
        origin="lower",
        aspect="auto",
        cmap="viridis",
        vmin=0,
        vmax=0.5,
    )
    bx.plot([0, 1], [0, 1], "w-", lw=0.8)
    bx.plot([0, 1], [1, 0], "w--", lw=0.8)
    bx.set(
        xlabel=r"$a=P(1\mid0)$",
        ylabel=r"$b=P(0\mid1)$",
        title="(b) First support threshold",
    )
    fig.colorbar(im, ax=bx)
    save(fig, out, "support")


def short_curves(out, data):
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.1), layout="constrained")
    rows = []
    changes = []
    p = 0.1
    for k, style, color in zip(
        range(1, 5), [":", "-", "--", "-."], [".55", BLUE, ORANGE, TEAL]
    ):
        marks = transitions(p, k) if k > 1 else []
        weights = sorted(
            set(
                [*np.linspace(0.00001, 0.997, 301), 0.0, 1.0, *(u for _, _, u in marks)]
            )
        )
        curve = np.array([at_weight(p, k, u)[:3] for u in weights])
        rows.extend([(k, u, *row) for row, u in zip(curve, weights)])
        changes.extend([(k, label, d, u) for d, label, u in marks])
        for i, ax in enumerate(axes):
            ax.plot(curve[:, 0], curve[:, i + 1], style, color=color, label=f"$K={k}$")
            for d, _, u in marks:
                ax.plot(d, at_weight(p, k, u)[i + 1], "o", color=color, ms=3)
            ax.set(
                xlim=(0, 0.5),
                xlabel="Distortion $D$",
                ylabel=["Rate (bits per symbol)", "Variance (bitsÂ² per symbol)"][i],
            )
    axes[0].legend(frameon=False)
    save(fig, out, "shortblocks")
    write(data / "shortblocks.csv", ["K", "u", "D", "rate", "variance"], rows)
    write(data / "support-changes.csv", ["K", "class_removed", "D", "u"], changes)
    four = [c for c in changes if c[0] == 4]
    fig, ax = plt.subplots(figsize=(7.7, 1.55))
    ax.set(xlim=(-0.3, 6.3), ylim=(-0.8, 1.45))
    ax.axis("off")
    for i, n in enumerate([16, 14, 10, 8, 4, 2]):
        ax.add_patch(
            plt.Rectangle(
                (i, 0),
                1,
                0.36,
                facecolor=plt.cm.BuGn(0.2 + i * 0.09),
                edgecolor="white",
            )
        )
        ax.text(i + 0.5, 0.18, str(n), ha="center", va="center")
    for i, (_, label, d, u) in enumerate(four, 1):
        ax.text(i, 0.58, label, ha="center", color=BLUE)
        ax.text(i, -0.15, f"{d:.5g}", ha="center", va="top")
    ax.text(0, -0.15, "0", ha="center", va="top")
    ax.text(6, -0.15, "0.5", ha="center", va="top")
    ax.text(3, 1.15, "Representative of the class removed", ha="center")
    save(fig, out, "ladder")


def varentropy(out, data):
    P = np.array([[0.9, 0.1], [0.3, 0.7]])
    pi = np.array([0.75, 0.25])
    rho = 0.6
    A = -np.log2(P)
    B = -np.log2(pi)
    edge = pi[:, None] * P
    ac = A - np.sum(edge * A)
    bc = B - pi @ B
    v0 = pi @ (bc**2)
    s2 = np.sum(edge * ac**2)
    gamma = np.einsum("i,ij,jk,ij,jk->", pi, P, P, ac, ac)
    kappa = np.sum(edge * bc[:, None] * ac)
    limit = s2 + 2 * gamma / (1 - rho)
    coeff = (
        v0
        - s2
        + 2 * kappa / (1 - rho)
        - 2 * gamma * (1 / (1 - rho) + 1 / (1 - rho) ** 2)
    )
    ks = np.arange(1, 101)
    vs = []
    for k in ks:
        n = k - 1
        h = np.arange(1, n)
        vs.append(
            (
                v0
                + n * s2
                + 2 * gamma * np.sum((n - h) * rho ** (h - 1))
                + 2 * kappa * np.sum(rho ** np.arange(n))
            )
            / k
        )
    write(
        data / "varentropy.csv",
        ["K", "variance", "limit", "leading_gap"],
        zip(ks, vs, [limit] * len(ks), -coeff / ks),
    )
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(8, 2.8), layout="constrained")
    ax.plot(ks[:15], vs[:15], ".-", color=BLUE)
    ax.axhline(limit, color=".4", ls="--", label="Varentropy rate")
    ax.legend(frameon=False)
    ax.set(
        xlabel="Block length $K$",
        ylabel="Variance (bitsÂ² per symbol)",
        title="(a) Full-support variance",
    )
    bx.loglog(ks, limit - np.asarray(vs), color=ORANGE, label="Exact gap")
    bx.loglog(ks, -coeff / ks, "--", color=".35", label=f"{-coeff:.5f}/$K$")
    bx.set(
        xlabel="Block length $K$",
        ylabel="Gap to varentropy rate",
        title="(b) Convergence",
    )
    bx.legend(frameon=False)
    save(fig, out, "varentropy")


def histogram(out, data):
    k = 12
    p = 0.1
    source, weight = words(p, k)
    bits = np.arange(2**k, dtype=np.uint32)
    flips = np.bitwise_count((bits ^ (bits >> 1)) & ((1 << (k - 1)) - 1)).astype(int)
    fig, axes = plt.subplots(1, 2, figsize=(8, 2.8), layout="constrained", sharey=True)
    rows = []
    for ax, d in zip(axes, [0.002, 0.35]):
        if d <= threshold(p, k):
            group = flips
            vals = (np.arange(k) - (k - 1) * p) * np.log2((1 - p) / p)
        else:
            u = constant(p, k, d)["u"]
            group = np.minimum(weight, k - weight)
            w = np.arange(k // 2 + 1)
            vals = -np.log2((u**w + u ** (k - w)) / 2)
        masses = np.bincount(group, weights=source)
        vals -= masses @ vals
        rows.extend((d, i, x, y) for i, (x, y) in enumerate(zip(vals, masses)))
        ax.vlines(vals, 0, masses, color=BLUE)
        ax.plot(vals, masses, ".", color=TEAL)
        ax.set(
            xlabel="Centered tilted information (bits)",
            title=f"$D={d}$ "
            + ("(full support)" if d == 0.002 else "(two reproductions)"),
        )
    axes[0].set_ylabel("Probability mass")
    save(fig, out, "histogram")
    write(data / "histogram.csv", ["D", "class", "centered_score_bits", "mass"], rows)
