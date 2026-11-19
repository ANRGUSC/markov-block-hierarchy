"""Draw the paper's overview using the six-source variance series."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch


@plt.rc_context(
    {
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "pdf.fonttype": 42,
        "mathtext.fontset": "dejavusans",
    }
)
def draw_overview(destination, series_file):
    """Write the vector figure; use the same operating points as the six-source plot."""
    w, h = (496, 529)
    fig = plt.figure(figsize=(w / 72, h / 72), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, w), ylim=(h, 0))
    ax.axis("off")
    ink = "#162e3b"
    gray = "#41555e"
    hair = "#bacace"
    teal = "#196c61"
    blue = "#265785"
    ochre = "#994b24"

    def text(x, y, msg, size=9, color=ink, weight="normal", align="left", font=None):
        return ax.text(
            x,
            y,
            msg,
            fontsize=size,
            color=color,
            fontweight=weight,
            ha=align,
            va="center",
            fontfamily=font,
            linespacing=1.34,
        )

    def line(x, y, X, Y, color=hair, lw=0.7, ls="-"):
        ax.plot([x, X], [y, Y], color=color, lw=lw, ls=ls, solid_capstyle="round")

    def words(x, y, bits):
        for j, b in enumerate(bits):
            px = x + 14 * j
            if j:
                line(px - 10, y, px - 4, y, gray, 1)
            ax.add_patch(
                Circle(
                    (px, y),
                    5.25,
                    facecolor=ink if b == "1" else "white",
                    edgecolor=ink,
                    lw=0.7,
                )
            )
            text(px, y + 0.2, b, 6.8, "white" if b == "1" else ink, "bold", "center")

    def panel(x, y, width, height, fill):
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0,rounding_size=5",
                ec="none",
                fc=fill,
            )
        )

    def body(x, y, lines, size=9, color=ink, step=13):
        for i, label in enumerate(lines):
            text(x, y + step * i, label, size, color)

    text(
        16,
        21,
        "What do longer Markov blocks reveal?",
        19,
        ink,
        "bold",
        font="DejaVu Serif",
    )
    text(16, 43, "Binary sources under Hamming distortion", 10, gray)
    line(16, 57, 480, 57, ink, 1)
    text(16, 73, "Exact results for short blocks", 13, ink, "bold", font="DejaVu Serif")
    for x, bits, label, description in [
        (
            16,
            "01",
            "Two symbols",
            [
                "First support loss at any bias.",
                "With positive persistence, both",
                "rate and variance are explicit.",
            ],
        ),
        (
            177,
            "001",
            "Three symbols",
            [
                "Symmetric, persistent chain.",
                "Support shrinks from 8 to 6 to 2.",
                "At most one cubic per distortion.",
            ],
        ),
        (
            341,
            "0011",
            "Four symbols",
            [
                "Symmetric, persistent chain.",
                "Six word classes reduce the",
                "calculation to two scalar searches.",
            ],
        ),
    ]:
        words(x + 5, 96, bits)
        text(x, 114, label, 10.3, ink, "bold")
        body(x, 132, description, 8.2, gray, 11.1)
    line(16, 169, 480, 169)
    text(
        16,
        188,
        "One optimization at any block length",
        13,
        ink,
        "bold",
        font="DejaVu Serif",
    )
    text(
        16,
        207,
        "A tensor calculation gives the mean and variance. What happens as the block grows?",
        9.8,
        gray,
    )
    line(248, 219, 248, 226, gray, 1)
    line(126, 226, 365, 226, gray, 1)
    for x in (126, 365):
        ax.annotate(
            "",
            xy=(x, 237),
            xytext=(x, 225),
            arrowprops=dict(arrowstyle="-|>", lw=1, color=gray),
        )
    panel(16, 238, 225, 104, "#e9f4ef")
    panel(251, 238, 229, 104, "#eaf0f7")
    text(27, 253, "Rate per symbol", 10.7, teal, "bold")
    text(263, 253, "Variance per symbol", 10.7, blue, "bold")
    text(27, 274, "$r_K(D)=\\mathrm{E}[\\jmath_K]/K$", 12, ink)
    text(263, 274, "$v_K(D)=\\mathrm{Var}[\\jmath_K]/K$", 12, ink)
    body(
        27,
        294,
        [
            "Discarding a boundary removes at most",
            "one adjacent pair's mutual information.",
            "This bounds the error in the rate",
        ],
        8.25,
        gray,
        11,
    )
    text(27, 330, "$0\\leq r_K(D)-R(D)\\leq I(X_1;X_2)/K.$", 9.7, teal)
    body(
        263,
        294,
        [
            "On the full-support branch this equals the",
            "block varentropy divided by K. For symmetric",
            "persistent chains, short blocks also bound",
            "the variance at longer block lengths.",
        ],
        8.25,
        gray,
        11,
    )
    text(
        16,
        364,
        "The variance can rise and fall as it approaches its limit",
        12.4,
        ink,
        "bold",
        font="DejaVu Serif",
    )
    lengths, variances = np.loadtxt(series_file, skiprows=1, unpack=True)
    values = dict(zip(lengths, variances, strict=True))
    left, right = (31, 182)
    top, base = (387, 417)

    def length_x(k):
        return left + (k - 2) * (right - left) / 10

    def variance_y(v):
        return base - v / 0.3 * (base - top)

    line(left, base, right, base, "#bacace")
    ax.plot(
        [length_x(k) for k in lengths],
        [variance_y(v) for v in variances],
        color=blue,
        lw=1.55,
        marker="o",
        ms=3.1,
    )
    text(
        left - 4,
        variance_y(values[2]) - 11,
        f"{values[2]:.3f}",
        7.3,
        blue,
        align="left",
    )
    text(
        length_x(6),
        variance_y(values[6]) - 7,
        f"{values[6]:.3f}",
        7.3,
        blue,
        align="center",
    )
    text(
        right,
        variance_y(values[12]) - 7,
        f"{values[12]:.3f}",
        7.3,
        blue,
        align="center",
    )
    for k in [2, 6, 12]:
        text(
            length_x(k), 425, f"K={k}" if k == 2 else str(k), 7.2, gray, align="center"
        )
    text(107, 438, "Variance (bits$^2$/symbol), $p=D=0.10$", 8, gray, align="center")
    body(
        206,
        381,
        [
            "For symmetric persistent chains, $v_K(D)$ has a positive limit",
            "at every interior distortion where $R(D)$ is differentiable.",
            "The full-support thresholds decrease to Gray's $D_c$.",
            "For $0<D\\leq D_c$, $v_K(D)=(1-1/K)\\,\\nu(p)$, where $\\nu(p)$ is",
            "the source varentropy rate.",
        ],
        8.6,
        ink,
        12.2,
    )
    line(16, 451, 480, 451, ink, 1)
    text(16, 470, "Coding one uninterrupted path", 13, ink, "bold", font="DejaVu Serif")
    text(16, 493, "PROVED", 8, teal, "bold")
    text(
        79,
        493,
        "For $0<D\\leq D_c$, $\\sqrt{\\nu(p)}\\,Q^{-1}(\\epsilon)$ bounds the second-order rate from below.",
        9,
    )
    text(16, 512, "OPEN", 8, ochre, "bold")
    text(
        79,
        512,
        "Is the limiting variance the operational dispersion? Matching achievability is open.",
        8.75,
    )
    fig.savefig(
        destination, metadata={"Title": "A block hierarchy for binary Markov sources"}
    )
    plt.close(fig)
