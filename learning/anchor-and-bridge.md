# From Watrous to thermal teleportation limits

A sender receives an unknown qubit and wants to transmit it using a thermal spin resource and classical messages. The central issue is quantitative: a thermal state may contain an entangled component whose probability is too small to improve the unconditional output fidelity by a fixed amount.

The selected educational anchor is **John Watrous, _The Theory of Quantum Information_ (Cambridge University Press, 2018)**. The [official author page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the edition and provides the author-hosted manuscript. The section locators below were checked against that 2018 manuscript. This is the project's one educational anchor; the [primary research references](../references/related-work.md) supply attribution and specialized proof dependencies.

## 1. A focused route through the anchor

| Watrous section | Foundation it supplies | Connection developed in this project |
|---|---|---|
| §2.2, Quantum channels | Completely positive, trace-preserving maps and the Choi representation | The full experiment, including measurements and fallback, is one channel from the late input to the receiver. |
| §3.2, The fidelity function | State overlap and its mathematical conventions | The project's output score is an average pure-state overlap. Its relation to the book's unsquared fidelity is made explicit below. |
| §6.1.2, Separable maps and the LOCC paradigm | Which operations act locally across a declared partition | A joint receiver laboratory and individually separated helpers are different operational models. |
| §6.2.3, Bound entanglement and partial transposition | The PPT criterion and the role of entanglement constraints | The project evaluates the exact partial transpose of its qubit–spin blocks and bounds the amount contributing to teleportation. |
| §6.3.1, Teleportation and dense coding | Bell measurements, classical outcomes and corrections | The small example below fixes the input, resource, measurement and all-outcome score. |
| §7.1, Permutation-invariant vectors and operators | Register permutations and invariant operator structure | Collective-spin sectors and their multiplicities are derived locally; permutation invariance does not force support only in the fully symmetric subspace. |

These sections provide the necessary operator language. The project supplies the spin addition, Gibbs weights and rare-sector estimates that turn it into the thermal communication result. Reading the whole book is not a prerequisite for following the [milestone map](milestones.md).

## 2. Notation and normalization

A few conventions must be translated before using textbook formulas.

| Anchor notation or concept | Project notation and convention |
|---|---|
| A register with state space $`\mathcal X`$ and density operators $`\mathrm D(\mathcal X)`$ | Each physical spin is a qubit. $`A`$ is the sender's source qubit, $`Q`$ the late input, and $`B`$ the physical output spin. |
| Adjoint $`X^*`$ | Written $`X^\dagger`$ in the scientific account; it is the same operation. |
| A channel $`\Phi`$ | The complete input-to-output channel is often written $`\mathcal T:Q\to B`$. |
| Choi operator $`J(\Phi)`$ in §2.2 | Denote it here by $`J_{\mathrm W}(\Phi)`$ to distinguish it from collective spin $`\mathbf J`$. The book's channel Choi operator has trace equal to the input dimension. |
| The normalized channel Choi state | $`\tau_{RB}=(I_R\otimes\mathcal T)(\lvert\Phi^+\rangle\langle\Phi^+\rvert_{RQ})`$, with $`\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2`$. It is $`J_{\mathrm W}(\mathcal T)/2`$ after putting the tensor factors in the displayed $`R,B`$ order. |
| Partial transposition on one tensor factor | $`\rho^{T_A}`$, taken in the fixed computational basis of the sender qubit. |
| Trace norm | $`\lVert X\rVert_1=\mathrm{Tr}\sqrt{X^\dagger X}`$. The project uses it in the negativity $`\nu(\rho)=(\lVert\rho^{T_A}\rVert_1-1)/2`$. |
| Permutations of tensor factors | The project uses $`N`$ for the number of physical spins and $`n=N/2`$ for half that number. Neither is a local Hilbert-space dimension, which is two. |

### Fidelity is used in two different senses

Watrous's Definition 3.11 uses the unsquared fidelity

```math
F_{\mathrm W}(\rho,\sigma)
=\left\lVert\sqrt{\rho}\sqrt{\sigma}\right\rVert_1.
```

For a pure target, its square is the overlap:

```math
F_{\mathrm W}(\rho,|\psi\rangle\langle\psi|)^2
=\langle\psi|\rho|\psi\rangle.
```

The project's channel score is

```math
F(\mathcal T)=
\int d\psi\,
\langle\psi|\mathcal T(|\psi\rangle\langle\psi|)|\psi\rangle.
```

Thus it averages the **squared** textbook fidelity for each pure input. It is not the square of an average unsquared fidelity. The [model](../science/model.md#communication-task) fixes this convention throughout.

## 3. Which physical assumptions are added

The textbook allows channels and LOCC protocols on general finite-dimensional systems. This project fixes a particular resource and a particular laboratory partition:

```math
\mathbf J=\frac12\sum_{i=1}^{N}\boldsymbol\sigma_i,
\qquad
H_N=\frac gN\mathbf J^2,
\qquad
\rho_N(b)=\frac{e^{-b\mathbf J^2}}{Z_N(b)},
\qquad
b=\frac{g}{Nk_{\mathrm B}T}.
```

The state is supplied on the entire $`N`$-qubit space. A singlet-sector label, a purification and a hidden pairing record are not supplied. The interaction strength $`g`$ stays fixed as $`N`$ changes, and its factor $`1/N`$ is part of the physical-temperature model.

In the global receiver benchmark, the sender controls $`A,Q`$ while the receiver jointly controls the other $`N-1`$ spins. Classical communication is allowed across that cut; quantum communication is not. In the helper-access comparisons, the laboratory partition is finer. Grouping helper spins is an additional quantum operation resource, even though classical messages are unrestricted.

Every outcome is retained. If a local receiver filter succeeds with probability $`q`$, gives conditional fidelity $`F_{\mathrm{succ}}`$, and uses optimal classical transmission after failure, its actual score is

```math
F_{\mathrm{all}}
=qF_{\mathrm{succ}}+(1-q)\frac23.
```

The successful branch alone is not the task score. Source preparation, cooling dynamics and hardware implementation are outside this supplied-state model.

## 4. A complete two-spin example

Take $`N=2`$. There are no helper spins. The sender and receiver each hold one source qubit, and

```math
H_2=\frac g2\mathbf J^2.
```

The singlet $`|s\rangle=(|01\rangle-|10\rangle)/\sqrt2`$ has $`J=0`$ and energy zero. The three-dimensional triplet subspace has $`J=1`$ and energy $`g`$. Put $`b=\ln3`$, equivalently $`T=g/(2k_{\mathrm B}\ln3)`$. Then

```math
e^{-2b}=\frac19,
\qquad
Z_2=1+3e^{-2b}=\frac43.
```

Writing $`P_1=I_4-|s\rangle\langle s|`$, the supplied resource is exactly

```math
\rho_2=
\frac34|s\rangle\langle s|
+\frac1{12}P_1
=
\frac23|s\rangle\langle s|
+\frac13\frac{I_4}{4}.
\qquad\text{(1)}
```

The factor $`1/12`$ is the weight per triplet basis state; the total triplet probability is $`1/4`$. These are eigenweights of a mixed state, not a classical success flag available to the parties.

The source is already stationary under its own Hamiltonian:

```math
e^{-itH_2/\hbar}\rho_2e^{itH_2/\hbar}=\rho_2.
```

This specifies the equilibrium resource and its free evolution. It does not specify a process that prepares it from another state.

Now deliver an independent unknown pure qubit $`|\psi\rangle_Q`$ to the sender. The sender Bell-measures $`Q,A`$, sends the two-bit outcome, and the receiver applies the corresponding Pauli correction with the known singlet convention. The source marginal at $`A`$ is $`I_2/2`$, so each of the four Bell outcomes has probability $`1/4`$.

For (1), every corrected outcome has the same conditional channel:

```math
\mathcal T_m(|\psi\rangle\langle\psi|)
=
\frac23|\psi\rangle\langle\psi|
+\frac13\frac{I_2}{2}.
\qquad\text{(2)}
```

The conditional overlap is therefore

```math
F_m=
\frac23+\frac13\frac12
=\frac56.
```

All four outcomes are counted, giving

```math
F_{\mathrm{all}}
=\sum_{m=1}^{4}\frac14\,F_m
=\frac56.
\qquad\text{(3)}
```

There is no unsuccessful projection branch in this smallest example. The receiver's rest-spin block has $`j=1/2`$, so the [middle-level projection](../science/teleportation-bounds.md#middle-level-projection) retains its entire two-dimensional space and has $`q=1`$.

The same answer can be checked through the entanglement calculation. The partial-transpose eigenvalues of (1) are $`5/12,5/12,5/12,-1/4`$, hence $`\nu_2=1/4`$. The universal bound gives

```math
F\le\frac23+\frac23\nu_2=\frac56,
```

so this protocol reaches the optimum for the stated two-spin resource. Its Bell fraction is $`3/4`$, while its textbook unsquared fidelity to the singlet is $`\sqrt3/2`$. Keeping those quantities distinct reproduces (3).

This example specializes the [finite spectrum](../science/thermal-spectrum.md) and [teleportation proof](../science/teleportation-bounds.md). It illustrates normalization, measurements and averaging; it does not establish a large-$`N`$ rare-sector law.

## 5. The steps supplied locally

The remaining bridge has four connected parts.

First, [thermal spectrum](../science/thermal-spectrum.md) adds angular-momentum coupling to the anchor's tensor-product language. Coupling a sender spin one half to receiver spin $`j`$ produces total spins $`j\pm1/2`$. Their thermal weights and multiplicities determine a finite sum for source negativity. The specialized qubit–spin partial-transpose calculation is reconstructed and attributed there.

Second, [teleportation bounds](../science/teleportation-bounds.md) turns that source quantity into the full channel score. Feeding half a local Bell pair through the protocol produces a normalized channel Choi state. Negativity monotonicity bounds its Bell overlap, including every failed outcome. A receiver projection onto two magnetic levels supplies the matching operational lower estimate for the global receiver benchmark.

Third, [cooling and decoding](../science/cooling-and-decoding.md) translates the dimensionless parameter back into physical temperature. A fixed excess $`F-2/3\ge\delta>0`$ requires and is achievable at temperature order $`g/(Nk_{\mathrm B})`$. The constants depend on the requested excess. The separate entanglement-presence threshold is much higher, of order $`g/(k_{\mathrm B}\ln N)`$.

Finally, [rare sectors](../science/rare-sectors.md) explains the small score quantitatively. The relevant spin blocks lie beyond the typical thermally populated spins. Their Gaussian tail gives an essential suppression, and the explicit decoder loses only a polynomial factor, preserving the leading logarithmic rate. The theorem takes even $`N\to\infty`$ at each fixed $`b>0`$ before $`b\downarrow0`$, with optimal-fidelity lower and upper limit envelopes. A separately stated simultaneous regime has its own proof. Neither limit is silently replaced by fixed positive physical temperature.

The [30 milestones](milestones.md) connect these parts from the individual channel and spin block to the complete operational and asymptotic statement.

---

[Learning route](README.md) · [30 milestones](milestones.md) · [Scientific account](../science/README.md) · [Primary-source attribution](../references/related-work.md)

