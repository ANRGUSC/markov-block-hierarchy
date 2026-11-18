"""Stationary source enumeration and tensor Blahut-Arimoto solver for D=0.10."""

import numpy as np


def source_probabilities(a, b, k):
    words = np.arange(2**k, dtype=np.uint32)
    state = words & 1
    probabilities = np.where(state == 0, b / (a + b), a / (a + b))
    transition = np.array([[1 - a, a], [b, 1 - b]])
    for bit in range(1, k):
        following = (words >> bit) & 1
        probabilities *= transition[state, following]
        state = following
    return probabilities


def hamming_product(vector, weight, k, with_distance=False):
    """Apply the tensor kernel; optionally weight each entry by distance as well."""
    result = vector.copy()
    if with_distance:
        distance = np.zeros_like(vector)
    for bit in range(k):
        pairs = result.reshape(-1, 2, 1 << bit)
        left, right = pairs[:, 0].copy(), pairs[:, 1].copy()
        if with_distance:
            dp = distance.reshape(pairs.shape)
            dl, dr = dp[:, 0].copy(), dp[:, 1].copy()
            dp[:, 0] = dl + weight * dr + weight * right
            dp[:, 1] = dr + weight * dl + weight * left
        pairs[:, 0] = left + weight * right
        pairs[:, 1] = right + weight * left
    return (result, distance) if with_distance else result


GAP_TARGET = 2e-8


def tilted_distribution(a, b, k, distortion):
    p = source_probabilities(a, b, k)
    if abs(a + b - 1) < 1e-12:
        entropy = -distortion * np.log2(distortion) - (1 - distortion) * np.log2(
            1 - distortion
        )
        return p, -np.log2(p) - k * entropy, 0.0, distortion

    lower, upper = 0.0, 20.0
    for _ in range(24):
        slope = (lower + upper) / 2
        weight = np.exp(-slope)
        prior = np.full(len(p), 1 / len(p))
        for _ in range(3000):
            normalizer = hamming_product(prior, weight, k)
            columns = hamming_product(p / normalizer, weight, k)
            if np.log2(max(1.0, columns.max())) < GAP_TARGET:
                break
            prior *= columns
            prior /= prior.sum()
        normalizer, weighted_distance = hamming_product(
            prior, weight, k, with_distance=True
        )
        achieved = float(p @ (weighted_distance / normalizer)) / k
        if abs(achieved - distortion) < 2e-7:
            break
        if achieved > distortion:
            lower = slope
        else:
            upper = slope
    columns = hamming_product(p / normalizer, weight, k)
    gap = np.log2(max(1.0, columns.max()))
    tilted = (-np.log(normalizer) - slope * k * distortion) / np.log(2)
    return p, tilted, gap, achieved
