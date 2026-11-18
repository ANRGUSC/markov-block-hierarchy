"""Independent finite checks used in the proof companion. Python standard library."""

from fractions import Fraction as F
from itertools import product
from math import isclose, log2


def word_law(k, a, b):
    transition = ((1 - a, a), (b, 1 - b))
    initial = (b / (a + b), a / (a + b))
    probabilities = {}
    for word in product(range(2), repeat=k):
        prob = initial[word[0]]
        for left, right in zip(word, word[1:]):
            prob *= transition[left][right]
        probabilities[word] = prob
    return probabilities


def inverse_mass_law(law, distortion):
    """Apply the inverse crossover kernel to each coordinate using exact rationals."""
    if not 0 <= distortion < F(1, 2):
        raise ValueError("inverse requires distortion below one half")
    values = dict(law)
    k = len(next(iter(values)))
    for i in range(k):
        previous = values
        values = {}
        for word, value in previous.items():
            other = word[:i] + (1 - word[i],) + word[i + 1:]
            numerator = (1 - distortion) * value - distortion * previous[other]
            values[word] = numerator / (1 - 2 * distortion)
    return values


def prefix_feasible(k, p, distortion):
    z, rho = 1 - 2 * distortion, 1 - 2 * p
    h = F(0)
    for _ in range(k - 1):
        if h >= z:
            return False
        h = rho * (1 - z * h) / (z - h)
    return h <= z


def check_prefixes():
    comparisons = 0
    for k, p, d in product(range(1, 8), (F(1, 10), F(8, 25), F(2, 5)),
                           (F(1, 200), F(1, 25), F(1, 10), F(1, 5), F(2, 5))):
        values = inverse_mass_law(word_law(k, p, p), d)
        assert sum(values.values()) == 1
        assert (min(values.values()) >= 0) == prefix_feasible(k, p, d)
        comparisons += 1
    # D(1-D)=p/2 gives an exact last-step zero. Extending once makes a mass negative.
    p, d = F(8, 25), F(1, 5)
    assert min(inverse_mass_law(word_law(2, p, p), d).values()) == 0
    assert min(inverse_mass_law(word_law(3, p, p), d).values()) < 0
    return comparisons


def covariance(law, left, right):
    mx = sum(float(w) * left(x) for x, w in law.items())
    my = sum(float(w) * right(x) for x, w in law.items())
    return sum(float(w) * (left(x) - mx) * (right(x) - my) for x, w in law.items())


def check_varentropy():
    comparisons = 0
    for a, b in ((F(1, 10), F(3, 10)), (F(3, 4), F(7, 8)), (F(1, 4), F(3, 4))):
        transition = ((1 - a, a), (b, 1 - b))
        pi = (b / (a + b), a / (a + b))
        triple = word_law(3, a, b)
        def initial(x):
            return -log2(pi[x[0]])
        def edge1(x):
            return -log2(transition[x[0]][x[1]])
        def edge2(x):
            return -log2(transition[x[1]][x[2]])
        v0 = covariance(triple, initial, initial)
        s2 = covariance(triple, edge1, edge1)
        gamma = covariance(triple, edge1, edge2)
        kappa = covariance(triple, initial, edge1)
        rho = float(1 - a - b)
        for k in range(1, 9):
            law = word_law(k, a, b)
            def info(x):
                return -log2(law[x])
            direct = covariance(law, info, info)
            n = k - 1
            formula = (v0 + n * s2 + 2 * gamma * sum((n-h)*rho**(h-1) for h in range(1, n))
                       + 2 * kappa * sum(rho**h for h in range(n)))
            assert isclose(formula, direct, abs_tol=1.e-12, rel_tol=1.e-12)
            comparisons += 1
    return comparisons


def check_endpoint():
    bias = F(1, 4)
    law = word_law(1, bias, 1-bias)
    prior = inverse_mass_law(law, bias)
    assert prior == {(0,): 1, (1,): 0}
    def info(x):
        return -log2(law[x])
    variance = covariance(law, info, info)
    assert isclose(variance, float(F(3, 16)) * log2(3)**2)
    # At slope zero every kernel entry equals one, hence every score is zero.
    assert sum(prior.values()) == 1
    return variance


if __name__ == "__main__":
    print(f"{check_prefixes()} exact inverse-prior comparisons and the boundary-zero test passed.")
    print(f"{check_varentropy()} direct word-enumeration variance comparisons passed.")
    print(f"Biased i.i.d. endpoint: backward-slope variance {check_endpoint():.8f}, zero-slope variance 0.")
