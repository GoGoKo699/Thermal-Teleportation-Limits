#!/usr/bin/env python3
"""Independent finite-matrix checks for the thermal resource and block decoder.

The analytic proofs are authoritative. This script checks finite instances by
constructing Pauli/spin matrices, not by comparing two copies of a scalar formula.
It also checks common-axis helper attainment on the full singlet projector.
"""

from __future__ import annotations

import json
import math

import numpy as np


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)
PAULIS = (SX, SY, SZ)
PHI_MINUS = np.array([1, 0, 0, -1], dtype=complex) / math.sqrt(2)
SINGLET = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)
TRIPLET_ZERO = np.array([0, 1, 1, 0], dtype=complex) / math.sqrt(2)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def partial_transpose_first(rho: np.ndarray, da: int, db: int) -> np.ndarray:
    return rho.reshape(da, db, da, db).transpose(2, 1, 0, 3).reshape(da * db, da * db)


def negativity(rho: np.ndarray, da: int, db: int) -> float:
    eigenvalues = np.linalg.eigvalsh(partial_transpose_first(rho, da, db))
    return float(-np.minimum(eigenvalues, 0).sum())


def multiplicity(number: int, twice_spin: int) -> int:
    if twice_spin < 0 or twice_spin > number or (number - twice_spin) % 2:
        return 0
    k = (number - twice_spin) // 2
    return math.comb(number, k) - (math.comb(number, k - 1) if k else 0)


def local_operator(op: np.ndarray, site: int, number: int) -> np.ndarray:
    result = np.array([[1]], dtype=complex)
    for i in range(number):
        result = np.kron(result, op if i == site else I2)
    return result


def total_spin_square(number: int) -> np.ndarray:
    components = [sum(local_operator(p, i, number) for i in range(number)) / 2 for p in PAULIS]
    return sum(component @ component for component in components)


def spin_matrices(j: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m = np.arange(-j, j + 1, dtype=float)
    raising = np.zeros((len(m), len(m)), dtype=complex)
    for k, value in enumerate(m[:-1]):
        raising[k + 1, k] = math.sqrt((j - value) * (j + value + 1))
    lowering = raising.conj().T
    return (raising + lowering) / 2, (raising - lowering) / (2j), np.diag(m)


def scalar_source(number: int, b: float) -> tuple[float, float, float]:
    partition = sum(
        (2 * spin + 1) * multiplicity(number, 2 * spin) * math.exp(-b * spin * (spin + 1))
        for spin in range(number // 2 + 1)
    )
    neg_numerator = 0.0
    decoder_numerator = 0.0
    for x in range(2, number + 1, 2):
        a = math.exp(-b * x * (x - 2) / 4)
        c = math.exp(-b * x * (x + 2) / 4)
        positive = max(0.0, a - (x + 1) * c)
        mult = multiplicity(number - 1, x - 1)
        neg_numerator += mult * (x - 1) * positive / x
        decoder_numerator += mult * positive / x
    return partition, neg_numerator / partition, 2 * decoder_numerator / (3 * partition)


def concurrence(rho: np.ndarray) -> float:
    yy = np.kron(SY, SY)
    values = np.linalg.eigvals(rho @ yy @ rho.conj() @ yy)
    roots = np.sort(np.sqrt(np.maximum(values.real, 0)))[::-1]
    return max(0.0, float(roots[0] - roots[1:].sum()))


def check_blocks() -> dict[str, float | int]:
    maximum_neg_error = maximum_gain_error = maximum_matrix_error = 0.0
    count = 0
    for j in (0.5, 1.5, 3.5, 7.5):
        x = int(2 * j + 1)
        spin = spin_matrices(j)
        coupling = sum(np.kron(pauli, component) for pauli, component in zip(PAULIS, spin))
        for ratio in (1.0, x + 1.0, 1.01 * (x + 1), 10.0 * (x + 1)):
            a, c = ratio, 1.0
            z = (x - 1) * a + (x + 1) * c
            alpha, beta = z / (2 * x), (c - a) / x
            rho = (alpha * np.eye(2 * x) + beta * coupling) / z
            exact_neg = (x - 1) * max(0.0, a - (x + 1) * c) / (x * z)
            measured_neg = negativity(rho, 2, x)
            maximum_neg_error = max(maximum_neg_error, abs(measured_neg - exact_neg))
            require(abs(measured_neg - exact_neg) < 1e-11, "block partial transpose")
            low = int(j - 0.5)
            high = int(j + 0.5)
            indices = [low, high, x + low, x + high]
            projected = rho[np.ix_(indices, indices)]
            expected = np.diag([alpha - beta / 2, alpha + beta / 2, alpha + beta / 2, alpha - beta / 2]).astype(complex)
            expected[0, 3] = expected[3, 0] = beta * x / 2
            expected /= z
            maximum_matrix_error = max(maximum_matrix_error, float(np.max(np.abs(projected - expected))))
            require(np.max(np.abs(projected - expected)) < 1e-12, "middle projection matrix")
            success = float(np.trace(projected).real)
            require(abs(success - 2 / x) < 1e-12, "middle projection probability")
            fraction = float(np.vdot(PHI_MINUS, projected @ PHI_MINUS).real) / success
            weighted_gain = max(0.0, success * (fraction - 0.5))
            maximum_gain_error = max(maximum_gain_error, abs(weighted_gain - exact_neg / (x - 1)))
            require(abs(weighted_gain - exact_neg / (x - 1)) < 1e-12, "all-outcome Bell-fraction gain")
            count += 1
    return {"cases": count, "max_negativity_error": maximum_neg_error, "max_projected_matrix_error": maximum_matrix_error, "max_gain_identity_error": maximum_gain_error}


def check_sources_and_helpers() -> dict[str, float | int]:
    maximum_partition_error = maximum_neg_error = maximum_concurrence_error = maximum_fidelity_error = 0.0
    source_count = helper_count = 0
    for number in (2, 4, 6, 8):
        energies, vectors = np.linalg.eigh(total_spin_square(number))
        threshold = math.log(number + 1) / number
        for b in (0.08, 0.35, 1.0, 2.0, 0.99 * threshold, 1.01 * threshold):
            weights = np.exp(-b * energies)
            partition_direct = float(weights.sum())
            rho = (vectors * weights) @ vectors.conj().T / partition_direct
            partition, exact_neg, decoder = scalar_source(number, b)
            direct_neg = negativity(rho, 2, 2 ** (number - 1))
            maximum_partition_error = max(maximum_partition_error, abs(partition_direct - partition))
            maximum_neg_error = max(maximum_neg_error, abs(direct_neg - exact_neg))
            require(abs(partition_direct - partition) < 1e-9, "full source partition")
            require(abs(direct_neg - exact_neg) < 1e-10, "full source negativity")
            require(exact_neg <= min(0.5, b / math.log(3)) + 1e-12, "uniform cooling upper")
            require(2 * exact_neg / (3 * (number - 1)) <= decoder + 1e-12, "finite decoder lower sandwich")
            require(decoder <= 2 * exact_neg / 3 + 1e-12, "finite decoder upper sandwich")
            if b < threshold:
                require(exact_neg == 0.0 and direct_neg < 1e-10, "finite PPT side")
            else:
                require(exact_neg > 0.0, "finite NPT side")
            source_count += 1

        singlet_vectors = vectors[:, np.abs(energies) < 1e-8]
        rho_zero = singlet_vectors @ singlet_vectors.conj().T / singlet_vectors.shape[1]
        average_concurrence = average_excess = balanced_probability = 0.0
        for helper_word in range(2 ** (number - 2)):
            indices = [a * 2 ** (number - 1) + 2 * helper_word + b for a in (0, 1) for b in (0, 1)]
            branch = rho_zero[np.ix_(indices, indices)]
            probability = float(np.trace(branch).real)
            if probability < 1e-12:
                continue
            state = branch / probability
            average_concurrence += probability * concurrence(state)
            balanced = helper_word.bit_count() == (number - 2) // 2
            if balanced:
                balanced_probability += probability
                expected = (0.5 + 1 / number) * np.outer(SINGLET, SINGLET.conj()) + (0.5 - 1 / number) * np.outer(TRIPLET_ZERO, TRIPLET_ZERO.conj())
                require(np.max(np.abs(state - expected)) < 1e-10, "balanced helper branch")
                fraction = float(np.vdot(SINGLET, state @ SINGLET).real)
                average_excess += probability * (2 * fraction - 1) / 3
        maximum_concurrence_error = max(maximum_concurrence_error, abs(average_concurrence - 1 / (number - 1)))
        maximum_fidelity_error = max(maximum_fidelity_error, abs(average_excess - 1 / (3 * (number - 1))))
        require(abs(average_concurrence - 1 / (number - 1)) < 1e-7, "singleton average concurrence")
        require(abs(average_excess - 1 / (3 * (number - 1))) < 1e-10, "singleton average fidelity")
        require(abs(balanced_probability - number / (2 * (number - 1))) < 1e-10, "balanced helper probability")
        helper_count += 1
    return {"source_cases": source_count, "helper_sizes": helper_count, "max_partition_error": maximum_partition_error, "max_source_negativity_error": maximum_neg_error, "max_helper_concurrence_error": maximum_concurrence_error, "max_helper_fidelity_error": maximum_fidelity_error}


def main() -> None:
    print(json.dumps({"passed": True, "block_decoder": check_blocks(), "full_source_and_helpers": check_sources_and_helpers(), "scope": "Finite floating-point matrix identities through N=8; analytic all-size and asymptotic proofs remain separate."}, indent=2))


if __name__ == "__main__":
    main()
