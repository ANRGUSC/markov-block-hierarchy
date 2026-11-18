"""Closed branches and Hamming-kernel operations for a symmetric Markov source."""

import numpy as np
from numba import njit
from scipy.optimize import brentq
from scipy.special import xlogy


def entropy(p):
    p = np.asarray(p)
    return -(xlogy(p, p) + xlogy(1 - p, 1 - p)) / np.log(2)


def nu(p):
    return p * (1 - p) * np.log2((1 - p) / p) ** 2


def critical(p):
    r = 1 - 2 * p
    return 0.5 * (1 - 2 * np.sqrt(r) / (1 + r))


def feasible(p, distortion, k):
    z = 1 - 2 * distortion
    h = 0.0
    for _ in range(k - 1):
        if h >= z:
            return False
        h = (1 - 2 * p) * (1 - z * h) / (z - h)
    return h <= z


def threshold(p, k):
    lo, hi = 0.0, 0.5
    for _ in range(53):
        mid = (lo + hi) / 2
        if feasible(p, mid, k):
            lo = mid
        else:
            hi = mid
    return lo


@njit(cache=True)
def kernel(v, u):
    result = v.copy()
    stride = 1
    while stride < len(v):
        for base in range(0, len(v), 2 * stride):
            for i in range(base, base + stride):
                a, b = result[i], result[i + stride]
                result[i] = a + u * b
                result[i + stride] = b + u * a
        stride *= 2
    return result


def words(p, k):
    x = np.arange(1 << k, dtype=np.uint32)
    flips = np.bitwise_count((x ^ (x >> 1)) & ((1 << (k - 1)) - 1))
    return 0.5 * p ** flips.astype(float) * (1 - p) ** (
        k - 1 - flips.astype(float)
    ), np.bitwise_count(x)


def constant(p, k, target, verify=True):
    # Weight law by last bit; columns 0 and k are the two reproductions.
    prev = np.zeros((2, k + 1))
    prev[0, 0] = prev[1, 1] = 0.5
    for _ in range(1, k):
        step = np.zeros_like(prev)
        step[0] = (1 - p) * prev[0] + p * prev[1]
        step[1, 1:] = p * prev[0, :-1] + (1 - p) * prev[1, :-1]
        prev = step
    mass = prev.sum(axis=0)
    w = np.arange(k + 1)
    if mass @ np.minimum(w, k - w) / k >= target:
        return None

    def evaluate(u):
        a, b = u**w, u ** (k - w)
        return mass @ ((w * a + (k - w) * b) / (a + b)) / k

    u = brentq(lambda u: evaluate(u) - target, 1e-13, 1.0, xtol=5e-15)
    z = (u**w + u ** (k - w)) / 2
    violation = 0.0
    if verify:
        source, weight = words(p, k)
        violation = max(0.0, kernel(source / z[weight], u).max() - 1.0)
        if violation > 2e-9:
            return None
    score = -np.log2(z)
    return dict(
        method="two constants",
        D_actual=evaluate(u),
        u=u,
        variance=mass @ (score - mass @ score) ** 2 / k,
        rate=target * np.log2(u) + mass @ score / k,
        column_violation=violation,
    )


def analytic(p, k, target):
    if target >= 0.5:
        return dict(
            method="zero rate",
            D_actual=0.5,
            u=1.0,
            variance=0.0,
            rate=0.0,
            column_violation=0.0,
        )
    if target <= threshold(p, k) + 5e-13:
        return dict(
            method="full support",
            D_actual=target,
            u=target / (1 - target),
            variance=(k - 1) * nu(p) / k,
            rate=(1 + (k - 1) * entropy(p)) / k - entropy(target),
            column_violation=0.0,
        )
    return constant(p, k, target)
