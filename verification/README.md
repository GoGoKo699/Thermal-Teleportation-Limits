# Reproduce the finite calculations

From the repository root, install the numerical dependencies and run:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/run_all.py
```

The command writes a JSON report to standard output and returns a nonzero exit code if a required identity or tolerance fails. It does not modify the scientific files. Setting one BLAS thread keeps these small dense calculations inexpensive and reproducible across common environments.

## What is checked

| Program | Independent calculation | Tested scope |
|---|---|---|
| [Spectrum](check_spectrum.py) | Builds collective Pauli operators and the finite Gibbs matrix, then partially transposes a physical qubit and compares its eigenvalues with the spin-sector formula | 24 dense cases at $`N=2,4,6,8`$, including both sides of the exact NPT onset; 1,088 exact rational multiplicity identities through $`N=64`$; 28 scalar bound cases through $`N=128`$ |
| [Receiver decoder](check_decoder.py) | Builds spin-$`j`$ matrices, explicitly projects the two middle magnetic levels, and checks the retained branch matrix, probability and unconditional fidelity gain | 16 block cases; 24 full thermal-state cases through $`N=8`$; common-axis helper attainment for four singlet sizes |
| [Cooling decoder](check_cooling.py) | Sums every physical helper Bell-measurement branch and its target Pauli correction, comparing the complete output density matrix with the stated Werner state | 16 dense decoder cases at $`N=2,4,6,8`$; exact rational certificate for the uniform $`b\ge2`$ fidelity bound |

The cooling check also evaluates the rational geometric-sum inequality on a finite grid. The proof for the whole interval is the elementary estimate in [cooling and decoding](../science/cooling-and-decoding.md#5-every-fixed-fidelity-excess-has-the-same-cooling-order); the finite grid does not replace that proof.

## Recorded validation

The combined suite passed on Python **3.12.14**, NumPy **2.3.5** and SciPy **1.17.0**. The largest absolute discrepancies were:

| Quantity | Observed discrepancy |
|---|---:|
| Dense partial transpose versus scalar source negativity, spectrum check | $`2.78\times10^{-16}`$ |
| Source negativity in the independent decoder check | $`5.56\times10^{-16}`$ |
| Spin-block projected matrix | Zero at the tested numerical precision |
| All-outcome singleton helper fidelity identity | $`2.23\times10^{-16}`$ |
| Complete paired-helper thermal output matrix | $`5.56\times10^{-16}`$ |
| Sum of all paired-helper branch probabilities | $`1.00\times10^{-15}`$ |

The physical dense comparisons use tolerances of order $`10^{-11}`$, far above the observed roundoff. Exact multiplicity and finite Taylor/rational certificates use integer or `Fraction` arithmetic. Small numerical differences across supported dependency versions are expected within the documented tolerances.

## What remains analytical

The arbitrary-protocol teleportation converse, arbitrary-size singleton optimum, fixed disjoint-pair budget bound, uniform temperature order and sharp rare-sector asymptotic are proved in the [scientific account](../science/README.md). Finite matrix checks can expose sign, normalization, basis-order and failure-probability mistakes; they cannot certify an asymptotic limit or establish exhaustive novelty.

These programs do not execute a quantum device, prepare a Gibbs state, test local-noise robustness, optimize an intermediate helper partition, or measure a hardware runtime. Their scope matches the finite algebra used by the supplied-state model.
