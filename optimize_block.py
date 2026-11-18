"""Compute a fixed-distortion optimum and test every reproduction column."""

import numpy as np
from model import analytic, kernel, threshold, words
from scipy.optimize import brentq, least_squares, minimize


class BlockProblem:
    def __init__(self, p, k):
        self.p = p
        self.k = k
        self.source, _ = words(p, k)
        self.last_q = self.source.copy()

    def initial(self, u):
        # Choose a feasible initialization using the objective at this multiplier.
        q = self.source
        constants = np.zeros_like(q)
        constants[0] = constants[-1] = 0.5
        candidates = [q, constants]
        if u / (1 + u) < threshold(self.p, self.k) + 0.075:
            inverse = np.maximum(kernel(q, -u), 0.0)
            candidates.append(inverse / inverse.sum())
        return min(candidates, key=lambda prior: -q @ np.log(kernel(prior, u)))

    def optimum(self, u, seed):
        # Homogeneous extension: minimizing sum(q)-E log(Aq) enforces sum(q)=1.
        # Start with likely active words, then price every remaining column.
        source = self.source
        q = seed.copy()
        tol = 1.5e-7
        for attempt in range(90):
            z = kernel(q, u)
            col = kernel(source / z, u)
            gap = col.max() - 1
            if gap <= tol:
                break
            active = q > max(1e-16, q.max() * 1e-12)
            # A full-support seed at large K is compressed before optimization.
            if (
                attempt == 0
                and len(q) > 4096
                and active.mean() > 0.8
                and np.array_equal(q, self.source)
            ):
                active = q >= max(q.max() * 1e-5, np.partition(q, -1024)[-1024])
            threshold_col = max(1 + tol * 0.15, col.max() - 0.6 * gap)
            active |= col >= threshold_col
            indices = np.flatnonzero(active)
            q = np.where(active, q, 0.0)
            q /= q.sum()
            # Diagonal preconditioning scales rare reproduction words.
            scale = np.sqrt(
                np.maximum.reduce(
                    [q[indices], source[indices], np.full(len(indices), 1e-8)]
                )
            )
            candidate = np.zeros_like(q)

            def loss(x):
                candidate[indices] = x * scale
                normal = kernel(candidate, u)
                if normal.min() <= 0:
                    return 1e20, -1e6 * scale
                gradient = 1 - kernel(source / normal, u)[indices]
                return candidate.sum() - source @ np.log(normal), gradient * scale

            fit = minimize(
                loss,
                q[indices] / scale,
                jac=True,
                method="L-BFGS-B",
                bounds=[(0.0, None)] * len(indices),
                options=dict(ftol=1e-15, gtol=2e-10, maxiter=350, maxcor=12, maxls=40),
            )
            q[indices] = np.maximum(0.0, fit.x * scale)
            q /= q.sum()
            if fit.nit < 3 and attempt > 1:
                # Multiplicative step preserves symmetry and improves the objective.
                q *= kernel(source / kernel(q, u), u)
                q /= q.sum()
        z = kernel(q, u)
        adjacent = np.zeros_like(z)
        for j in range(self.k):
            v = z.reshape(-1, 2, 1 << j)
            w = adjacent.reshape(v.shape)
            w[:, 0] += v[:, 1]
            w[:, 1] += v[:, 0]
        expected = u / (1 - u * u) * (source @ (adjacent / z) / self.k - u)
        score = -np.log2(z)
        gap = max(0.0, kernel(source / z, u).max() - 1)
        return q, dict(
            method="tensor optimization",
            u=u,
            D_actual=expected,
            variance=source @ (score - source @ score) ** 2 / self.k,
            rate=expected * np.log2(u) + source @ score / self.k,
            column_violation=gap,
        )

    def fixed_distortion(self, target):
        # For long words a short-block solve gives an inexpensive initial slope.
        memo = {}

        def objective(u):
            if u == 0:
                return -target
            if u == 1:
                return 0.5 - target
            if u not in memo:
                seed = self.initial(u) if not memo else self.last_q
                if memo:
                    seed = memo[min(memo, key=lambda x: abs(x - u))][0]
                memo[u] = self.optimum(u, seed)
            return memo[u][1]["D_actual"] - target

        lo, hi = 0.0, 1.0
        if self.k >= 16:
            guess = calculate(self.p, 10, target)["u"]
            step = 0.018
            for _ in range(8):
                lo = max(0.0, guess - step)
                hi = min(1.0, guess + step)
                if objective(lo) <= 0 <= objective(hi):
                    break
                step *= 2
        root = brentq(objective, lo, hi, xtol=1e-10)
        self.last_q, result = memo[root]
        if abs(result["D_actual"] - target) > 1e-9 and self.k <= 14:
            result = self.refine_active(self.last_q, root, target)
        if result["column_violation"] > 1e-5 or abs(result["D_actual"] - target) > 2e-5:
            raise ArithmeticError(f"K={self.k}, p={self.p}, D={target}: {result}")
        return result

    def refine_active(self, q, u, target):
        """Solve the active column equalities and the distortion equation together."""
        active = np.flatnonzero(q > 1e-9)
        if len(active) > 128:
            raise ArithmeticError(
                "Distortion refinement requires a smaller active set."
            )
        x = np.arange(len(q), dtype=np.uint32)
        distances = np.bitwise_count(x[:, None] ^ active).astype(float)

        def evaluate(theta):
            logq = np.r_[theta[:-1], 0.0]
            weights = np.exp(logq - logq.max())
            weights /= weights.sum()
            slope = np.exp(theta[-1])
            matrix = np.exp(-slope * distances)
            z = matrix @ weights
            col = (self.source / z) @ matrix
            distortion = ((self.source / z) @ (matrix * distances)) @ weights / self.k
            return col, distortion, z, weights, slope

        def residual(theta):
            col, distortion, *_ = evaluate(theta)
            return np.r_[col[:-1] - col[-1], distortion - target]

        seed = np.r_[np.log(q[active[:-1]] / q[active[-1]]), np.log(-np.log(u))]
        fit = least_squares(residual, seed, ftol=1e-14, gtol=1e-14, xtol=1e-14)
        _, d, z, weights, slope = evaluate(fit.x)
        u = np.exp(-slope)
        gap = max(0.0, kernel(self.source / z, u).max() - 1.0)
        score = -np.log2(z)
        if abs(d - target) > 5e-9 or gap > 2e-7:
            raise ArithmeticError("Active-set refinement failed its all-column check.")
        return dict(
            method="tensor optimization",
            u=u,
            D_actual=d,
            variance=self.source @ (score - self.source @ score) ** 2 / self.k,
            rate=d * np.log2(u) + self.source @ score / self.k,
            column_violation=gap,
        )


def calculate(p, k, d):
    result = analytic(p, k, d)
    return result if result is not None else BlockProblem(p, k).fixed_distortion(d)
