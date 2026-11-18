"""Optimal class allocations and their rate/variance for K=1,2,3,4."""

from functools import lru_cache

import numpy as np
from model import entropy
from scipy.optimize import brentq


@lru_cache(None)
def classes(p, k):
    x = np.arange(2**k, dtype=np.uint32)
    flips = np.bitwise_count((x ^ (x >> 1)) & ((1 << (k - 1)) - 1)).astype(int)
    prob = 0.5 * p**flips * (1 - p) ** (k - 1 - flips)
    distance = np.bitwise_count(x[:, None] ^ x).astype(int)
    labels = {
        1: ["0"],
        2: ["00", "01"],
        3: ["000", "001", "010"],
        4: ["0000", "0011", "0110", "0101", "0001", "0010"],
    }[k]
    groups = []
    for word in labels:
        n = int(word, 2)
        rev = int(word[::-1], 2)
        mask = 2**k - 1
        groups.append(sorted({n, rev, n ^ mask, rev ^ mask}))
    return prob, distance, labels, groups, np.array([prob[g].sum() for g in groups])


def allocate(s, k, L, m):
    # Active prefixes are sorted by s_i*k_i.  For each prefix solve sum(w)=m.
    order = np.argsort(-(s * k))
    den = m + np.cumsum(L / k[order])
    eta = np.max(np.cumsum(s[order]) / den)
    return np.maximum(s / eta - L / k, 0.0), eta


def at_weight(p, k, u):
    prob, dist, labels, groups, s = classes(p, k)
    if u == 0:
        mean = prob @ (-np.log2(prob))
        return 0.0, mean / k, prob @ ((-np.log2(prob) - mean) ** 2) / k, s
    if u == 1:
        return 0.5, 0.0, 0.0, np.zeros_like(s)
    if k == 1:
        d = u / (1 + u)
        return d, 1 - entropy(d), 0.0, np.array([1.0])
    if k == 2:
        # Invert the binary symmetric channel on each side until a mass vanishes.
        switch = (1 - np.sqrt(1 - 2 * p)) / 2
        d = u / (1 + u)
        w = np.array([1.0, 0.0])
        if d < switch:
            transition = (p / 2 * (1 + u * u) - (1 - p) * u) / (1 - u) ** 2
            w = np.array([1 - 2 * transition, 2 * transition])
    elif k == 3:
        beta = (u + u * u) / 2
        gain = (1 + u**3) / 2 - beta
        w, _ = allocate(s, gain * np.array([1.0, 0.5, 1.0]), beta, 1.0)
    else:
        chi = u * u
        beta = (u + u**3) / 2
        gain = (1 - u * u) ** 2 / 2

        def split(theta):
            L = chi * theta + beta * (1 - theta)
            M = chi * (1 - theta) + beta * theta
            even, eta = allocate(s[:4], np.full(4, gain), L, theta)
            odd, xi = allocate(s[4:], np.full(2, gain / 2), M, 1 - theta)
            derivative = (
                eta
                - xi
                + (chi - beta)
                * (
                    np.sum(s[:4] / (L + gain * even))
                    - np.sum(s[4:] / (M + gain / 2 * odd))
                )
            )
            return np.r_[even, odd], derivative

        if split(1.0)[1] >= 0:
            theta = 1.0
        elif split(0.0)[1] <= 0:
            theta = 0.0
        else:
            theta = brentq(lambda t: split(t)[1], 0, 1, xtol=1e-14)
        w = split(theta)[0]
    q = np.zeros(len(prob))
    for weight, group in zip(w, groups):
        q[group] = weight / len(group)
    q /= q.sum()
    channel = u**dist
    z = channel @ q
    d = prob @ (((channel * dist) @ q) / z) / k
    score = -np.log2(z)
    return (
        d,
        d * np.log2(u) + prob @ score / k,
        prob @ (score - prob @ score) ** 2 / k,
        w,
    )


def transitions(p, k):
    labels = classes(p, k)[2]
    result = []
    for index, label in enumerate(labels):

        def present(u):
            return at_weight(p, k, u)[3][index] > 1e-12

        lo, hi = 0.0, 0.998
        if present(hi):
            continue
        for _ in range(45):
            mid = (lo + hi) / 2
            if present(mid):
                lo = mid
            else:
                hi = mid
        result.append((at_weight(p, k, (lo + hi) / 2)[0], label, (lo + hi) / 2))
    return sorted(result)
