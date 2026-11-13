# Teleportation bounds and an explicit spin-block decoder

The source's single-spin negativity controls what can be transmitted across a physical sender cut. A matching lower estimate is needed to interpret a small negativity as an operational resource rather than only an entanglement witness. Here a simple receiver projection supplies that estimate. Its failure probability is included in the score.

The party model throughout this page is the [global receiver benchmark](model.md#access-models): the sender owns the physical source qubit $`A`$ and the independent late input; the receiver jointly owns all other source spins and decodes onto the fixed physical qubit $`B`$. The upper bounds also apply to more separated helpers. The lower decoder on this page is not claimed implementable by singleton or helper-only collaboration.

## A universal upper bound from the source cut

Let

```math
\nu_N(b)=\operatorname{Neg}_{A:A^c}(\rho_N(b))
=\frac{\|\rho_N(b)^{T_A}\|_1-1}{2}.
```

For any deterministic protocol in the benchmark,

```math
F_N^{\mathrm{glob}}(b)-\frac23\le\frac23\nu_N(b).
```

To prove this for the complete protocol, give the sender half of a Bell pair $`RQ`$ instead of a sampled pure input. The reference $`R`$ remains at the sender. Initially this Bell pair is entirely local to the sender side, so the entanglement across sender versus receiver is exactly that of the supplied source. Negativity cannot increase under the trace-preserving LOCC protocol, including its measurement records and every branch. After discarding unused systems, its normalized channel Choi state $`\tau_{RB}`$ therefore has negativity at most $`\nu_N(b)`$.

For any two-qubit state and fixed Bell projector $`\Phi`$,

```math
\operatorname{Tr}(\Phi\tau)
=\operatorname{Tr}(\Phi^{T_B}\tau^{T_B})
\le \frac12\|\tau^{T_B}\|_1
=\frac12+\operatorname{Neg}(\tau).
```

The operator norm of $`\Phi^{T_B}`$ is $`1/2`$. The Haar-average channel identity $`F=(2F_{\mathrm e}+1)/3`$ then gives the bound. This proof includes protocols that act on the unknown input during helper processing; it does not assume that a target Bell pair is first localized. Negativity monotonicity and this teleportation relation are established tools, credited in the [references](../references/related-work.md).

## Locally flagged qubit–spin blocks

The receiver may measure the total spin $`j`$ and multiplicity label of its $`N-1`$ spins. These are operations wholly inside the receiver laboratory. For even $`N`$,

```math
j=\frac12,\frac32,\ldots,\frac{N-1}{2},
\qquad x=2j+1\in\{2,4,\ldots,N\}.
```

Each multiplicity copy carries the unnormalized operator

```math
X_j=a_xP_-+c_xP_+,
\qquad
a_x=e^{-b x(x-2)/4},
\qquad
c_x=e^{-b x(x+2)/4},
```

where $`P_-`$ and $`P_+`$ project onto the coupled spins $`j-1/2`$ and $`j+1/2`$. Define

```math
z_j=(x-1)a_x+(x+1)c_x,
\qquad
\widehat\rho_j=\frac{X_j}{z_j}.
```

With Pauli matrices on the sender and spin-$`j`$ operators on the receiver,

```math
X_j=\alpha_j I+\beta_j\boldsymbol\sigma\cdot\mathbf J_j,
\qquad
\alpha_j=\frac{z_j}{2x},
\qquad
\beta_j=\frac{c_x-a_x}{x}\le0.
```

The inherited invariant-spin partial-transpose spectrum, derived in the [thermal-spectrum account](thermal-spectrum.md), gives

```math
\nu_j=\operatorname{Neg}(\widehat\rho_j)
=\frac{(x-1)[a_x-(x+1)c_x]_+}{x z_j}.
```

Here $`[u]_+=\max\{u,0\}`$. The block is NPT exactly when $`a_x>(x+1)c_x`$, equivalently $`bx>\ln(x+1)`$.

## Middle-level projection

Within a flagged spin-$`j`$ irrep, the receiver projects onto its two middle magnetic levels,

```math
\Pi_j=|j,-\tfrac12\rangle\langle j,-\tfrac12|
+|j,+\tfrac12\rangle\langle j,+\tfrac12|.
```

They exist because $`j`$ is half integral. Map the two retained levels isometrically to a qubit and, inside the receiver laboratory, place that output at $`B`$. The receiver marginal of $`\widehat\rho_j`$ is $`I_x/x`$, so this projection succeeds with probability

```math
q_j=\frac2x.
```

In the ordered basis $`(|\uparrow,-1/2\rangle,|\uparrow,+1/2\rangle,|\downarrow,-1/2\rangle,|\downarrow,+1/2\rangle)`$, the unnormalized successful operator before division by $`z_j`$ is

```math
\begin{pmatrix}
\alpha_j-\beta_j/2&0&0&\beta_jx/2\\
0&\alpha_j+\beta_j/2&0&0\\
0&0&\alpha_j+\beta_j/2&0\\
\beta_jx/2&0&0&\alpha_j-\beta_j/2
\end{pmatrix}.
```

The successful state is Bell diagonal. Its largest Bell eigenvalue before normalization is $`\alpha_j-\beta_j(x+1)/2`$. If $`f_j`$ denotes its normalized Bell fraction, elementary simplification gives

```math
q_j\left(f_j-\frac12\right)
=\frac{a_x-(x+1)c_x}{x z_j}
=\frac{\nu_j}{x-1}
\quad\text{when }\nu_j>0.
```

Consequently the projection gives a teleportation-useful two-qubit state under **exactly** the original block's NPT condition. No sender filter or uncharged postselection is required. In an NPT block, use standard Bell-measurement teleportation after a successful projection and optimal classical transmission after failure. In a PPT block, use classical transmission from the outset. The resulting unconditional block score is

```math
F_j-\frac23=\frac{2\nu_j}{3(x-1)}.
```

For $`j=1/2`$, the projection is the identity and this reduces to the usual Bell-diagonal two-qubit formula. For larger $`j`$, it makes the information loss explicit: the receiver selects two levels with probability $`2/x`$ and still gains a fraction $`1/(x-1)`$ of the block's negativity in the all-outcome Bell-overlap excess.

## Finite operational sandwich

Let $`d_{N-1}(j)`$ be the multiplicity of the rest-spin-$`j`$ irrep. Its probability is $`p_j=d_{N-1}(j)z_j/Z_N`$. Applying the preceding decoder independently in each local flag yields the achievable excess

```math
\Delta_N^{\mathrm{dec}}(b)
=\frac{2}{3Z_N(b)}
\sum_{\substack{x=2,4,\ldots,N}}
\frac{d_{N-1}((x-1)/2)}{x}
[a_x-(x+1)c_x]_+.
```

Thus the optimal deterministic global-receiver excess $`\Delta_N^{\mathrm{glob}}=F_N^{\mathrm{glob}}-2/3`$ obeys

```math
\boxed{
\Delta_N^{\mathrm{dec}}(b)
\le\Delta_N^{\mathrm{glob}}(b)
\le\frac23\nu_N(b).
}
```

A looser but simple finite-size consequence is

```math
\frac{2\nu_N(b)}{3(N-1)}
\le\Delta_N^{\mathrm{glob}}(b)
\le\frac23\nu_N(b).
```

The exact decoder sum is preferable for asymptotic rates: a single chosen spin block loses only its own factor $`x-1`$, rather than a factor of the full system size. The sandwich does not identify the exact optimal fidelity at finite $`N`$.

## Ordered rare-sector rate

The [rare-sector analysis](rare-sectors.md) proves, first at fixed $`b>0`$ as even $`N\to\infty`$, convergence of the source negativity to $`\nu_\infty(b)>0`$ and of the explicit decoder sum to

```math
\Delta_\infty^{\mathrm{dec}}(b)
=\frac{1}{3S(b)}
\sum_{\substack{x\ge2\\x\text{ even}}}
[a_x-(x+1)c_x]_+>0.
```

Here $`S(b)=\sum_{J\ge0}(2J+1)^2e^{-bJ(J+1)}`$ is the limiting partition function relative to $`D_N`$. Both quantities have the same small-$`b`$ logarithmic rate,

```math
\lim_{b\downarrow0}
\frac{b}{[\ln(1/b)]^2}\ln\nu_\infty(b)
=
\lim_{b\downarrow0}
\frac{b}{[\ln(1/b)]^2}
\ln\Delta_\infty^{\mathrm{dec}}(b)
=-\frac14.
```

The reason the decoder preserves the exponent is explicit. A contributing rare spin has $`x`$ of order $`\ln(1/b)/b`$. Removing its factor $`x-1`$ changes the logarithm only by order $`\ln(1/b)+\ln\ln(1/b)`$, negligible compared with $`[\ln(1/b)]^2/b`$.

No limit of the optimal $`F_N^{\mathrm{glob}}(b)`$ is needed or asserted. Set

```math
\underline\Delta(b)=\liminf_{\substack{N\to\infty\\N\text{ even}}}
\Delta_N^{\mathrm{glob}}(b),
\qquad
\overline\Delta(b)=\limsup_{\substack{N\to\infty\\N\text{ even}}}
\Delta_N^{\mathrm{glob}}(b).
```

The finite sandwich gives $`\Delta_\infty^{\mathrm{dec}}\le\underline\Delta\le\overline\Delta\le2\nu_\infty/3`$. Hence each optimal-fidelity envelope has the same outer logarithmic rate $`-1/4`$. The sufficient simultaneous finite-size regime in the rare-sector account yields the same rate directly along its allowed sequences. These statements do not apply to a fixed-positive-physical-temperature limit, or establish this matching rate for singleton or paired-helper access.

## Attribution and limits

The Bell fraction–fidelity relation, the negativity converse, the collective-spin decomposition, and invariant qubit–spin partial transposition are established methods. The middle-level projection above supplies an explicit operational lower estimate for this thermal family. It does not replace the known singlet Bell-subspace decoder of [Barjaktarevic et al. (2005)](https://doi.org/10.1103/PhysRevLett.95.230501), whose perfect endpoint is used separately in the paired-helper cooling construction.

The results concern one source copy, unrestricted ideal local processing inside each allowed laboratory, classical communication, and an unconditional qubit score. They do not claim an optimal finite-size decoder, a distillable rate per source spin, a source-preparation method, or a quantum-versus-classical computational speedup.
