# From thermal entanglement to a communication score

A negative partial transpose can be caused by a sector whose probability is too small to deliver a fixed unconditional output advantage. The collective antiferromagnet makes this difference explicit because the total-spin decomposition is exact at finite size.

The two temperature statements answer different questions. Across one physical spin and all remaining spins, entanglement is present below $`g/[k_{\mathrm B}\ln(N+1)]`$. Obtaining $`F\ge2/3+\delta`$ for a fixed $`\delta>0`$ instead requires temperature of order $`g/(k_{\mathrm B}N)`$. The latter necessity permits arbitrary processing of the receiver's entire side, so it cannot be attributed only to an inefficient helper measurement.

## A finite comparison

Take $`N=100`$ and measure temperatures in units of $`g/k_{\mathrm B}`$. The exact one-spin NPT threshold is $`1/\ln101\approx0.2167`$. The paired-helper construction has a rigorous uniform fidelity guarantee above $`0.8939`$ at $`b\ge2`$, which here means temperature at most $`0.005`$.

For a target fidelity of $`0.85`$, the negativity converse requires

```math
T\le\frac{40g}{11\ln3\,k_{\mathrm B}N}
\approx0.0331\,\frac g{k_{\mathrm B}}\quad(N=100).
```

Thus $`0.005`$ is a sufficient temperature in this example, while temperatures above approximately $`0.0331`$ cannot meet that target under any global receiver protocol. These are bounds, not an exact finite-size fidelity threshold. Both are much lower than the temperature at which an arbitrarily small NPT contribution first appears.

At the same system size, singleton helper access is at most

```math
\frac23+\frac1{297}\approx0.6700,
```

even at zero temperature. Cooling and quantum cooperation therefore constrain different aspects of the same task. Full helper-pair access has the established perfect singlet endpoint; singleton operations cannot exploit the unobserved mixture as if its singlet matching were known.

## What causes the rare-sector law

The thermal weights decrease roughly as a Gaussian in total spin. When $`b`$ is small, the typical spin is of order $`b^{-1/2}`$. An entangled qubit–spin block instead requires $`bx>\ln(x+1)`$, where $`x`$ is the rest-spin dimension. Its first possible contributors have $`x`$ of order $`\ln(1/b)/b`$.

Reaching those sectors pays an essential Boltzmann suppression. An explicit two-level receiver projection loses only a polynomial factor in $`x`$, so it preserves the leading logarithmic exponent. This is why a matching operational statement is possible without knowing the exact optimal fidelity or its fixed-$`b`$ thermodynamic limit.

The [rare-sector theorem](rare-sectors.md) takes large even $`N`$ at fixed $`b`$ before sending $`b`$ to zero, and states a separate sufficient simultaneous regime. Holding $`b`$ fixed already makes physical temperature proportional to $`1/N`$. The theorem does not assert the same exponent at fixed positive physical temperature or at the finite-size NPT edge.

## Which operations make the comparison meaningful

The singleton theorem permits arbitrary local ancillas, classical communication and adaptation after the unknown input arrives. Its limitation comes from which laboratories can act jointly, rather than a restriction to a convenient helper basis. A hidden matching is used only in the converse; no matching record is supplied to either protocol.

The paired-helper construction requires a full Bell measurement, including triplet resolution and common axes. It is stronger than a rotation-invariant singlet–triplet test. The global receiver benchmark permits even more: a joint spin decomposition, filtering and transfer of the decoded qubit to the physical output spin inside one laboratory. Only the upper bounds transfer automatically to more separated laboratory arrangements.

The Gibbs source, its temperature and its ideal symmetry are supplied conditions. Preparing that state and implementing the controls have physical costs, but the present task does not determine them. Keeping those costs separate prevents a temperature law from being mistaken for a cooling-time or end-to-end communication-rate advantage.
