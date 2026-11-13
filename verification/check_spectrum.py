#!/usr/bin/env python3
"""Independent finite diagnostics for the stated thermal spectrum.

Dense checks construct J^2 on the physical tensor product and transpose a
physical qubit. Scalar checks use binomial multiplicities and exact Fraction
products. These diagnostics do not prove an arbitrary-size theorem or certify
an asymptotic limit.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction

import numpy as np
from scipy.linalg import expm


def multiplicity(spins: int, twice_spin: int) -> int:
    if twice_spin < 0 or twice_spin > spins or (spins - twice_spin) % 2:
        return 0
    lower = (spins - twice_spin) // 2
    return math.comb(spins, lower) - (
        math.comb(spins, lower - 1) if lower > 0 else 0
    )


def scalar_negativity(spins: int, beta_scaled: float) -> float:
    partition = sum(
        (2 * total + 1)
        * multiplicity(spins, 2 * total)
        * math.exp(-beta_scaled * total * (total + 1))
        for total in range(spins // 2 + 1)
    )
    numerator = 0.0
    for width in range(2, spins + 1, 2):
        exponent = -beta_scaled * width * (width - 2) / 4
        threshold_log = math.log(width + 1) - beta_scaled * width
        positive_difference = (
            math.exp(exponent) * (-math.expm1(threshold_log))
            if threshold_log < 0
            else 0.0
        )
        numerator += (
            multiplicity(spins - 1, width - 1)
            * (width - 1)
            / width
            * positive_difference
        )
    return numerator / partition


def tensor_product(factors: list[np.ndarray]) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def dense_spin_squared(spins: int) -> np.ndarray:
    identity = np.eye(2)
    paulis = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.diag([1, -1]).astype(complex),
    )
    collective = []
    for pauli in paulis:
        operator = np.zeros((2**spins, 2**spins), dtype=complex)
        for site in range(spins):
            operator += tensor_product(
                [pauli if index == site else identity for index in range(spins)]
            ) / 2
        collective.append(operator)
    return sum(operator @ operator for operator in collective)


def dense_negativity(spin_squared: np.ndarray, beta_scaled: float) -> float:
    dimension = spin_squared.shape[0]
    state = expm(-beta_scaled * spin_squared)
    state /= np.trace(state)
    partial_transpose = (
        state.reshape(2, dimension // 2, 2, dimension // 2)
        .transpose(2, 1, 0, 3)
        .reshape(dimension, dimension)
    )
    eigenvalues = np.linalg.eigvalsh(partial_transpose)
    return float(-eigenvalues[eigenvalues < 0].sum())


def check_exact_multiplicities() -> int:
    count = 0
    for spins in range(2, 66, 2):
        half = spins // 2
        catalan = multiplicity(spins, 0)
        assert sum(
            (2 * total + 1) * multiplicity(spins, 2 * total)
            for total in range(half + 1)
        ) == 2**spins
        for total in range(half + 1):
            product = Fraction((2 * total + 1) * (half + 1), half + total + 1)
            for index in range(total):
                product *= Fraction(half - index, half + index + 1)
            assert product == Fraction(multiplicity(spins, 2 * total), catalan)
            assert product <= 2 * total + 1
            count += 1
        for level in range(1, half + 1):
            product = Fraction(level * (half + 1), half + level)
            for index in range(1, level):
                product *= Fraction(half - index, half + index)
            assert product == Fraction(
                multiplicity(spins - 1, 2 * level - 1), catalan
            )
            assert product <= level
            count += 1
    return count


def main() -> None:
    exact_cases = check_exact_multiplicities()
    dense_cases = []
    maximum_error = 0.0
    for spins in (2, 4, 6, 8):
        spin_squared = dense_spin_squared(spins)
        onset = math.log(spins + 1) / spins
        values = sorted({0.1, 0.5, 2.0, 0.95 * onset, onset, 1.05 * onset})
        for beta_scaled in values:
            scalar = scalar_negativity(spins, beta_scaled)
            dense = dense_negativity(spin_squared, beta_scaled)
            error = abs(scalar - dense)
            assert error < 2e-11, (spins, beta_scaled, scalar, dense)
            assert scalar <= min(0.5, beta_scaled / math.log(3)) + 1e-13
            maximum_error = max(maximum_error, error)
            dense_cases.append(
                {
                    "N": spins,
                    "b": beta_scaled,
                    "scalar_negativity": scalar,
                    "dense_negativity": dense,
                    "absolute_error": error,
                }
            )
        assert scalar_negativity(spins, 0.95 * onset) == 0
        assert scalar_negativity(spins, 1.05 * onset) > 0

    uniform_bound_cases = 0
    for spins in (16, 32, 64, 128):
        for beta_scaled in (0.05, 0.08, 0.12, 0.2, 0.25, 0.5, 2.0):
            value = scalar_negativity(spins, beta_scaled)
            bound = min(0.5, beta_scaled / math.log(3))
            if beta_scaled <= 0.25:
                logarithm = math.log(1 / beta_scaled)
                rare_bound = (logarithm + 4) / (2 * beta_scaled) * math.exp(
                    -(logarithm**2) / (8 * beta_scaled)
                )
                bound = min(bound, rare_bound)
            assert value <= bound * (1 + 1e-11) + 1e-15
            uniform_bound_cases += 1

    print(
        json.dumps(
            {
                "passed": True,
                "exact_multiplicity_cases": exact_cases,
                "dense_cases": len(dense_cases),
                "maximum_dense_absolute_error": maximum_error,
                "uniform_bound_cases": uniform_bound_cases,
                "dense_results": dense_cases,
                "scope": (
                    "Independent physical-matrix partial-transpose diagnostics "
                    "at N=2,4,6,8; exact finite multiplicity identities through "
                    "N=64; finite scalar bound checks through N=128. No "
                    "arbitrary-size, optimal-teleportation or asymptotic proof "
                    "is supplied by this program."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
