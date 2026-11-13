# Thermal Teleportation Limits

**When does entanglement in a collective thermal state provide a fixed teleportation advantage between two physical spins?**

For an extensively normalized collective antiferromagnet, the temperature at which one physical spin first becomes entangled with the rest is much higher than the temperature needed for a nonvanishing one-copy communication advantage. The distinction remains even if every spin on the receiver side can be processed jointly.

The supplied resource is one Gibbs state of

```math
H_N=\frac gN\mathbf J^2,\qquad
\mathbf J=\frac12\sum_{i=1}^{N}\boldsymbol\sigma_i,\qquad
b=\frac{g}{Nk_{\mathrm B}T},
```

with even $`N`$. An independent unknown qubit arrives at a fixed sender spin, and one output qubit is required at a specified receiver spin. The score is average Haar fidelity, including every measurement and failure outcome. The optimal classical baseline is $`2/3`$.

| Question | Supported answer |
|---|---|
| When is one physical spin entangled with the rest? | Exactly when $`T\lt g/[k_{\mathrm B}\ln(N+1)]`$. This specializes the known invariant-spin partial-transpose criterion. |
| How cold must the source be for a fixed excess $`\delta\in(0,1/3)`$ above classical teleportation? | The largest usable temperature is $`\Theta_\delta(g/[k_{\mathrm B}N])`$. The converse permits a globally controlled receiver; disjoint helper-pair measurements attain the order. |
| What if every helper remains a singleton laboratory? | At every temperature, $`F_N^{\mathrm{single}}\le2/3+1/[3(N-1)]`$. The zero-temperature maximally mixed singlet attains equality. |
| How much does a fixed partition into $`k`$ helper pairs help at zero temperature? | $`F_{N,k}-2/3\le1/[3(N-2k-1)]`$. This is a converse, with attainment established at the singleton and fully paired endpoints. |

The positive singlet teleportation protocol is established prior work: [Barjaktarevic et al. (2005)](https://doi.org/10.1103/PhysRevLett.95.230501), with an explicit helper-measurement formulation in [Gray et al. (2016)](https://doi.org/10.1103/PhysRevB.94.195136). The contribution here is the quantitative access and cooling account, including how rare entangled spin sectors constrain a complete output score. The [related-work account](references/related-work.md) distinguishes the inherited source, spectrum, entanglement tools and decoder from those conclusions.

## Why the two temperatures differ

For small $`b`$, the first entangled receiver sectors have spin dimension of order $`\ln(1/b)/b`$, far above the thermally typical order $`b^{-1/2}`$. Their Gibbs weight is extremely small. In the ordered limit of large even $`N`$ at fixed $`b`$, followed by $`b\downarrow0`$, the best teleportation excess in the global receiver benchmark has logarithm

```math
\ln\Delta=-\left(\frac14+o(1)\right)
\frac{[\ln(1/b)]^2}{b}.
```

This rate holds for both the lower and upper large-$`N`$ envelopes of the optimal excess; existence of its fixed-$`b`$ limit is not assumed. A receiver-only filter supplies a matching lower estimate on this logarithmic scale. The [rare-sector proof](science/rare-sectors.md) also gives a uniform finite-size bound and a sufficient simultaneous regime. This is not a fixed-positive-physical-temperature limit.

## Read the science

Start with the [task and allowed laboratories](science/model.md), then use the [science map](science/README.md).

| To understand | Read |
|---|---|
| The exact finite Gibbs spectrum, negativity and NPT onset | [Thermal spectrum](science/thermal-spectrum.md) |
| A bound for every complete teleportation protocol and an explicit all-outcome decoder | [Teleportation bounds](science/teleportation-bounds.md) |
| Why fixed fidelity requires cooling of order $`1/N`$ | [Cooling and paired decoding](science/cooling-and-decoding.md) |
| The sharp rare-sector logarithmic law and its limits | [Rare spin sectors](science/rare-sectors.md) |
| The exact singleton result and fixed helper-pair participation requirement | [Helper access](science/helper-access.md) |
| A worked comparison and the physical meaning of the resource boundaries | [Interpretation](science/interpretation.md) |
| Attribution, primary versions and comparison scope | [Related work](references/related-work.md) and [source evidence](references/source-evidence.md) |

[The LLM reading guide](llms.txt) maps scientific questions to their authoritative files.

## Learn the project

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source bridge](learning/anchor-and-bridge.md) identifies the relevant sections, translates the fidelity and channel conventions, and supplies the collective-spin and thermal connections needed here.

The [30-milestone map](learning/milestones.md) builds the task and its prerequisites before connecting the access bounds, cooling law and rare-sector mechanism. Use the [learning entrypoint](learning/README.md) to follow that route; the direct science links above remain the authoritative proof route.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/run_all.py
```

The checks construct finite physical Gibbs matrices and receiver spin blocks, compare their partial transposes with the stated spectrum, and verify all-outcome decoder and singleton-attainment identities. Exact arithmetic checks the multiplicity products. These diagnostics supplement the analytical proofs; finite enumeration does not establish an asymptotic theorem. See [verification](verification/README.md) for the tested scope and numerical tolerances.

## Physical scope

This is a one-copy task with a supplied equilibrium state, ideal controls and a common reference frame. Classical communication is unrestricted. The sharp rare-sector operational matching grants one receiver laboratory joint control of all other source spins, including the output spin. Its upper bound also applies to more separated helper models; the matching decoder need not be available in those models.

The factor $`1/N`$ in the Hamiltonian is retained throughout. The temperature requirement does not price cooling time, refrigeration power or Gibbs-state preparation. Independent local noise and errors in the symmetry or controls require a different analysis. No many-copy rate or hardware implementation advantage follows from the one-copy fidelity comparison.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
