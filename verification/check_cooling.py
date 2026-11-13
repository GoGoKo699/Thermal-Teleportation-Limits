#!/usr/bin/env python3
"""Check the physical paired-helper decoder and exact cooling certificates.

The dense experiment sums every Bell-measurement branch of the full Gibbs
matrix. It checks the resulting two-qubit density matrix, rather than assuming
that its global-parity correlations determine the claimed answer.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math

import numpy as np


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
BELLS = tuple(
    np.array(v, dtype=complex) / math.sqrt(2)
    for v in ([1, 0, 0, 1], [1, 0, 0, -1], [0, 1, 1, 0], [0, 1, -1, 0])
)
SIGNS = ((1, 1), (-1, 1), (1, -1), (-1, -1))
SINGLET = np.outer(BELLS[3], BELLS[3].conj())


def tensor(factors):
    result = np.array([1.0], dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def multiplicity(number, spin):
    k = number // 2 - spin
    return math.comb(number, k) - (math.comb(number, k - 1) if k else 0)


def physical_spin_square(number):
    components = []
    for pauli in (X, Y, Z):
        components.append(
            sum(tensor([pauli if site == i else I for site in range(number)])
                for i in range(number)) / 2
        )
    return sum(component @ component for component in components)


def measured_output(state, number):
    output = np.zeros((4, 4), dtype=complex)
    probability = 0.0
    expected_parity = (-1) ** (number // 2)
    for outcomes in itertools.product(range(4), repeat=(number - 2) // 2):
        helper = tensor([BELLS[index] for index in outcomes])
        embedding = np.kron(np.eye(4), helper[:, None])
        branch = embedding.conj().T @ state @ embedding
        xx = expected_parity * math.prod(SIGNS[index][0] for index in outcomes)
        zz = expected_parity * math.prod(SIGNS[index][1] for index in outcomes)
        correction = (Z if xx == 1 else I) @ (X if zz == 1 else I)
        operator = np.kron(I, correction)
        output += operator @ branch @ operator.conj().T
        probability += float(np.trace(branch).real)
    return output, probability


def exact_certificates():
    q = Fraction(1, 50)
    first = q * (3 - q) / (1 - q) ** 2
    second = q * (9 - 2 * q + q * q) / (1 - q) ** 3
    coefficient = (1 - first) / (1 + second)
    fidelity = (1 + coefficient) / 2
    require(coefficient == Fraction(55174, 70025), "exact Werner lower bound")
    require(fidelity == Fraction(125199, 140050), "exact fidelity lower bound")
    require(sum(Fraction(4) ** k / math.factorial(k) for k in range(8)) > 50,
            "finite Taylor certificate for exp(4) > 50")
    # The all-delta proof bounds the geometric sum by 72 q on 0 <= q <= 1/2.
    for q in (Fraction(i, 100) for i in range(1, 51)):
        value = q * (9 - 2 * q + q * q) / (1 - q) ** 3
        require(value <= 72 * q, "uniform geometric-sum inequality")
    return {"fidelity_lower": str(fidelity), "q_grid_exact_cases": 50}


def main():
    max_error = max_probability_error = 0.0
    count = 0
    for number in (2, 4, 6, 8):
        eigenvalues, eigenvectors = np.linalg.eigh(physical_spin_square(number))
        for b in (0.05, 0.5, 2.0, 5.0):
            weights = np.exp(-b * eigenvalues)
            state = (eigenvectors * weights) @ eigenvectors.conj().T / weights.sum()
            output, probability = measured_output(state, number)
            denominator = sum(
                (2 * spin + 1) * multiplicity(number, spin)
                * math.exp(-b * spin * (spin + 1))
                for spin in range(number // 2 + 1)
            )
            numerator = sum(
                (-1) ** spin * multiplicity(number, spin)
                * math.exp(-b * spin * (spin + 1))
                for spin in range(number // 2 + 1)
            )
            coefficient = numerator / denominator
            expected = coefficient * SINGLET + (1 - coefficient) * np.eye(4) / 4
            error = float(np.max(np.abs(output - expected)))
            max_error = max(max_error, error)
            max_probability_error = max(max_probability_error, abs(probability - 1))
            require(error < 2e-11, "complete Gibbs/Bell-measurement output")
            require(abs(probability - 1) < 2e-11, "all branch probabilities retained")
            if b >= 2:
                require((1 + coefficient) / 2 >= 125199 / 140050,
                        "finite physical decoder meets certified lower bound")
            count += 1
    print(json.dumps({
        "passed": True,
        "dense_decoder_cases": count,
        "maximum_output_matrix_error": max_error,
        "maximum_probability_sum_error": max_probability_error,
        "exact_certificates": exact_certificates(),
        "scope": "Full finite Gibbs matrices, all helper Bell outcomes and corrections, "
                 "plus rational sufficient inequalities. No numerical claim proves "
                 "an arbitrary-size or asymptotic theorem.",
    }, indent=2))


if __name__ == "__main__":
    main()
