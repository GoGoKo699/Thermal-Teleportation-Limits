# Model: a supplied collective thermal resource

The question is how much quantum communication can be extracted from one collective antiferromagnet after its equilibrium state has been supplied. The distinction between having entanglement and obtaining a fixed communication advantage is essential: an arbitrarily rare entangled spin sector can make a partial transpose negative while contributing almost nothing to an unconditional output score.

## Source and normalization

There are an even number $`N=2n\ge 2`$ of labelled, distinguishable spin-one-half systems. Write

```math
\mathbf J=\frac12\sum_{i=1}^{N}\boldsymbol\sigma_i,
\qquad
H_N=\frac gN\mathbf J^2,
\qquad g>0.
```

The factor $`1/N`$ is part of the model. It keeps the sum of pair-coupling strengths incident on a spin of order $`g`$ and the total spectral range of order $`gN`$. It must not be removed when comparing temperatures across system sizes. The gap between the total-spin-zero and total-spin-one sectors is $`2g/N`$.

At temperature $`T>0`$, the source supplies one copy of

```math
\rho_N(b)=\frac{e^{-b\mathbf J^2}}{Z_N(b)},
\qquad
Z_N(b)=\mathrm{Tr}e^{-b\mathbf J^2},
\qquad
b=\frac{g}{Nk_{\mathrm B}T}.
```

This is the Gibbs state on the entire $`2^N`$-dimensional Hilbert space. There is no hard projection onto total spin zero. At zero temperature its limit is the maximally mixed singlet,

```math
\rho_N^{(0)}=\frac{P_0^{(N)}}{D_N},
\qquad
D_N=\frac{1}{n+1}\binom{2n}{n}.
```

Neither a purification, a decomposition label, a singlet-pairing record, nor an entangled auxiliary state is supplied. In particular, a valence-bond decomposition used in a proof is not information available to a protocol. The collective Hamiltonian, its Schur decomposition, and the maximally mixed singlet are established objects; their use here is not a new source-preparation proposal. See the [thermal spectrum](thermal-spectrum.md) for the exact source weights and their attribution.

## Communication task

Fix two physical source spins, $`A`$ and $`B`$, before the experiment. The source is used once. After it has been supplied, an independent unknown qubit $`Q`$ is delivered to the sender at $`A`$. Its pure state is Haar distributed and is not revealed to any party. The protocol must return one qubit at the fixed physical receiver $`B`$.

For the induced trace-preserving channel $`\mathcal T:Q\to B`$, the score is

```math
F(\mathcal T)=\int d\psi\,
\langle\psi|\mathcal T(|\psi\rangle\langle\psi|)|\psi\rangle.
```

Every measurement outcome, unsuccessful filter, and fallback branch contributes to this average. Heralding cannot remove a failed attempt from the denominator. Parties may always ignore the source and use optimal classical measure-and-prepare transmission, so the attainable baseline is $`F_{\mathrm{cl}}=2/3`$. A **fixed quantum advantage** means $`F\ge 2/3+\delta`$ for a prescribed $`0\lt \delta\lt 1/3`$ independent of $`N`$. This is stronger than asking for a positive excess that may vanish with system size.

The late independent input rules out using prior knowledge of the state to be transmitted as an uncharged reference or source-preparation resource. Helpers may act before or after that input arrives; the converse includes input-dependent adaptation.

## Access models

The same source and output score are compared under distinct control permissions.

| Access model | Quantum operations allowed | Communication between separate laboratories |
|---|---|---|
| Singleton access | Each party controls one physical source spin. The sender also controls $`Q`$. | Arbitrary classical communication; no quantum communication. |
| Fixed paired helpers | The $`N-2`$ helpers are partitioned in advance into disjoint pairs and any remaining singleton helpers. Quantum operations within a helper pair are allowed. The target parties $`A`$ and $`B`$ remain separate. | Arbitrary classical communication between the resulting laboratories; no quantum communication. |
| Global receiver benchmark | The sender controls $`A`$ and $`Q`$. A single receiver laboratory controls all $`N-1`$ other source spins, including $`B`$. | Arbitrary classical communication across the sender–receiver cut; no quantum communication across that cut. |

The global receiver benchmark permits a joint irrep measurement and decoder on all spins except $`A`$, followed by transfer of its decoded qubit to $`B`$ inside that laboratory. It is strictly stronger than allowing helpers to collaborate jointly while keeping $`B`$ in a separate laboratory. The matching rare-sector teleportation exponent is established for this bipartite benchmark. It is not asserted for either more separated access model.

Conversely, an upper bound for the global receiver benchmark also bounds every protocol with more separated helpers. The fixed-score cooling lower construction uses only disjoint helper-pair Bell measurements and therefore works in the weaker paired-helper model. The [helper-access account](helper-access.md) states the exact singleton result and the scope of a fixed pair-budget converse.

## Supplied controls and charged boundaries

All parties receive a common Cartesian reference frame and may use ideal local controls, local measurements, product-state ancillary systems, and classical randomness. Classical communication and classical processing are unrestricted. No extra nonlocal entanglement or quantum communication is supplied across any laboratory boundary in the selected access model.

A full Bell measurement resolves all four Bell states. It is a stronger operation than the rotation-invariant two-outcome singlet-versus-triplet measurement. Shared axes and full triplet resolution are therefore explicit resources, even though the Gibbs input is rotationally invariant.

The source cost counted here is one supplied Gibbs-state copy at the stated physical temperature. The results do not establish a cooling algorithm, equilibrium preparation time, refrigeration power, source repetition rate, or hardware gate count. The law $`T=\Theta(g/[k_{\mathrm B}N])`$ is a necessary and sufficient temperature order for a fixed one-copy score in the stated ideal model. It is not an end-to-end runtime or heat-cost advantage.

The source is exactly permutation invariant and collective-$`SU(2)`$ invariant. Anisotropy, a field, nonuniform couplings, loss of a source spin, local readout errors, and local quantum noise define different source or control models. Bounds derived for this exact family are not silently extended to those perturbations. In particular, a global white-noise mixture and independent local noise have different effects on a parity decoder.

## Parameter limits

Finite-$`N`$ theorems use the actual $`b=g/(Nk_{\mathrm B}T)`$. The rare-sector result first takes even $`N\to\infty`$ at each fixed $`b>0`$, then takes $`b\downarrow0`$. Thus its physical temperature already scales as $`1/N`$ in the inner limit. It is not a fixed-positive-temperature thermodynamic limit.

The account also gives a sufficient simultaneous regime in the [rare-sector analysis](rare-sectors.md). Outside an explicitly stated joint regime, no exchange of limits is implied. The optimal fidelity need not have an established $`N\to\infty`$ limit: the operational rate is stated using its lower and upper limit envelopes.
