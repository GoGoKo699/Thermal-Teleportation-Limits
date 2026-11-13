# Useful cooling and Bell decoding

The supplied collective antiferromagnet supports a constant physical-qubit teleportation advantage only at temperatures of order $`1/N`$. This necessity holds even when the receiver controls every spin except the sender's spin. A decoder using disjoint helper Bell measurements achieves the same cooling order. The much higher temperature at which one physical spin first becomes entangled with the rest is a different threshold.

This page develops that operational statement for the [model and task](model.md). The [thermal spectrum](thermal-spectrum.md) supplies the inherited spin-sector identities, and [rare sectors](rare-sectors.md) explains the sharper suppression at small raw inverse temperature.

## 1. One temperature parameter

Let $`N=2n`$ be even, with collective spin and an extensively normalized Hamiltonian

```math
\mathbf J=\frac12\sum_{i=1}^{N}\boldsymbol{\sigma}_i,
\qquad
H_N=\frac{g}{N}\mathbf J^2,
\qquad
b=\frac{g}{Nk_{\mathrm B}T}.
```

Here $`g>0`$ is fixed. The supplied source is

```math
\rho_N(b)=\frac{e^{-b\mathbf J^2}}{Z_N(b)}.
```

The sender holds one physical source spin $`A`$ and later receives an unknown Haar-distributed input qubit. The receiver must produce a qubit output at the fixed physical spin $`B`$. Every outcome contributes to the average fidelity. The strongest comparison below grants the receiver joint control of the other $`N-1`$ source spins, while the sender and receiver communicate classically. There is no quantum communication across this sender–receiver cut.

The source copy is supplied. The theorem concerns its use, rather than the time, work or apparatus required to prepare and cool it. The interaction is two body and all to all; the factor $`1/N`$ matters to every physical-temperature statement.

## 2. A uniform upper bound for every receiver strategy

Write $`\nu_N(b)=(\|\rho_N(b)^{T_A}\|_1-1)/2`$ for the source negativity across the sender versus receiver cut. The [teleportation bound](teleportation-bounds.md) gives

```math
F_N^{\mathrm{glob}}(b)
\le \frac23+\frac23\,\nu_N(b).
```

It applies to the complete deterministic teleportation protocol, including adaptation after the input arrives. It is not restricted to first extracting a two-qubit resource.

The spin-sector calculation gives a particularly simple uniform bound. In a receiver spin-$`j`$ block, set $`x=2j+1`$. Since $`N-1`$ is odd, $`j\ge 1/2`$ and $`x\ge2`$. The normalized block negativity satisfies

```math
\nu_j(b)\le\frac1x.
```

It can be positive only when

```math
bx>\ln(x+1)\ge\ln3.
```

Consequently every contributing block has $`1/x<b/\ln3`$. Averaging the normalized, orthogonal receiver blocks proves

```math
\nu_N(b)\le
\min\left\{\frac12,\frac{b}{\ln3}\right\},
\qquad
F_N^{\mathrm{glob}}(b)
\le
\frac23+\frac{2b}{3\ln3}.
\tag{1}
```

The spin-$`j`$ partial-transpose criterion is inherited from [Schliemann](../references/related-work.md#spin-sectors-and-thermal-entanglement). Its use here turns the thermal source's entanglement into a bound on the stated output task.

For a requested fixed excess $`\delta\in(0,1/3)`$, attaining $`F_N^{\mathrm{glob}}\ge2/3+\delta`$ therefore requires

```math
b\ge\frac{3\delta\ln3}{2},
\qquad
T\le
\frac{2g}{3\delta\ln3\,Nk_{\mathrm B}}.
\tag{2}
```

Thus the raw parameter cannot vanish when the desired fidelity excess stays fixed. The sharper finite bounds and ordered essential rate in [rare sectors](rare-sectors.md) explain how strongly usefulness is suppressed when it does vanish.

## 3. Disjoint helper Bell measurements

A constructive protocol uses less receiver cooperation. Fix two physical target spins $`A,B`$. Partition the remaining $`N-2`$ helper spins into disjoint pairs. Each pair performs one complete Bell measurement, reading its commuting $`X_iX_j`$ and $`Z_iZ_j`$ eigenvalues. The products of these outcomes specify a Pauli correction on $`B`$.

For a total-spin-zero input, the global identities

```math
X^{\otimes N}=Z^{\otimes N}=(-1)^{N/2}
```

fix both corrected target Bell parities. Every nonzero-probability branch then gives an exact Bell pair. This is the singlet Bell-subspace teleportation endpoint of [Barjaktarevic et al. (2005)](https://doi.org/10.1103/PhysRevLett.95.230501), with the helper-pair formulation explicit in [Gray et al. (2016)](https://doi.org/10.1103/PhysRevB.94.195136). The wider parity-unlocking mechanism is inherited [Smolin and stabilizer machinery](../references/related-work.md#bell-parities-and-helper-cooperation).

For the full thermal state, define the spin multiplicity

```math
d_N(J)=
\binom{N}{n-J}-\binom{N}{n-J-1},
\qquad J=0,1,\ldots,n,
```

with a binomial coefficient outside its range interpreted as zero. Then

```math
Z_N(b)=
\sum_{J=0}^{n}
d_N(J)(2J+1)e^{-bJ(J+1)}.
```

After averaging all helper outcomes and applying their target corrections, the exact target state is

```math
\omega_N(b)=
R_N(b)|s\rangle\langle s|
+\bigl(1-R_N(b)\bigr)\frac{I_4}{4},
\tag{3}
```

where $`|s\rangle`$ is the two-qubit singlet and

```math
R_N(b)=
\frac{
\displaystyle\sum_{J=0}^{n}
d_N(J)(-1)^J e^{-bJ(J+1)}
}{
\displaystyle\sum_{J=0}^{n}
d_N(J)(2J+1)e^{-bJ(J+1)}
}.
\tag{4}
```

To obtain (4), a collective rotation by $`\pi`$ has spin-$`J`$ character $`(-1)^J`$. Hence its thermal expectation is the numerator divided by $`Z_N`$, after removing the known $`(-1)^{N/2}`$ phase. Multiplying the helper Bell parities transfers this expectation to each corrected target correlation:

```math
\langle X_AX_B\rangle_{\omega_N}
=
\langle Y_AY_B\rangle_{\omega_N}
=
\langle Z_AZ_B\rangle_{\omega_N}
=-R_N.
```

The corrected output commutes with both target Bell parities and has vanishing one-spin Bloch vectors. These correlations therefore determine (3).

Standard teleportation with (3), together with classical fallback if that gives a higher score, achieves

```math
F_N^{\mathrm{pair}}(b)
\ge
\max\left\{
\frac23,\frac{1+R_N(b)}2
\right\}.
\tag{5}
```

This is an all-outcome protocol. It uses $`(N-2)/2`$ joint helper measurements and reliable classical parity communication. The pair interaction size is two, while the total number of joint helper measurements is extensive.

## 4. A finite, uniform performance guarantee

Let $`D_N=d_N(0)`$. The exact multiplicity ratio obeys

```math
\frac{d_{2n}(J)}{D_{2n}}
=
(2J+1)\frac{n+1}{n+J+1}
\frac{(n!)^2}{(n-J)!(n+J)!}
\le 2J+1.
\tag{6}
```

For $`b\ge2`$, use $`q=e^{-4}<1/50`$ and

```math
e^{-bJ(J+1)}\le q^J
\qquad (J\ge1).
```

The numerator of (4), divided by $`D_N`$, is at least $`1-S_1`$, and the denominator is at most $`1+S_2`$, where

```math
S_1=\sum_{J\ge1}(2J+1)q^J
=\frac{q(3-q)}{(1-q)^2},
```

```math
S_2=\sum_{J\ge1}(2J+1)^2q^J
=\frac{q(9-2q+q^2)}{(1-q)^3}.
```

Both sums increase with $`q`$. Substituting $`q=1/50`$ gives $`S_1\le149/2401`$ and $`S_2\le22401/117649`$. Therefore, for every even $`N`$,

```math
R_N(b)\ge\frac{55174}{70025},
\qquad
F_N^{\mathrm{pair}}(b)
\ge\frac{125199}{140050}>0.8939
\qquad (b\ge2).
\tag{7}
```

The guaranteed excess over $`2/3`$ is $`95497/420150>0.2272`$. These rational bounds are finite guarantees. For example, $`e^4>50`$ follows already from its positive Taylor sum through degree seven.

## 5. Every fixed fidelity excess has the same cooling order

The explicit bound (7) is one convenient operating point. Every fixed $`\delta\in(0,1/3)`$ can be treated uniformly in $`N`$.

Set

```math
q_\delta=
\frac{1-3\delta}{72(1+3\delta)},
\qquad
b_\delta=\frac12\ln\frac1{q_\delta}.
\tag{8}
```

For $`b\ge b_\delta`$, put $`q=e^{-2b}\le q_\delta<1/2`$. Equation (6) gives an excited-sector weight relative to the singlet sector of at most

```math
S_2(q)\le72q
\le\frac{1-3\delta}{1+3\delta}.
```

Thus the singlet-sector probability satisfies

```math
p_0\ge\frac1{1+S_2(q)}
\ge\frac{1+3\delta}{2}.
```

The spin-$`J`$ contribution to $`R_N`$ is $`(-1)^J/(2J+1)\ge-1/3`$ for every $`J\ge1`$. Consequently

```math
R_N\ge p_0-\frac{1-p_0}{3}
\ge\frac13+2\delta,
\qquad
F_N^{\mathrm{pair}}\ge\frac23+\delta.
\tag{9}
```

Combining necessity (2) and sufficiency (8)–(9) proves the claimed cooling order:

```math
T=\Theta_\delta\!\left(\frac{g}{Nk_{\mathrm B}}\right)
```

for a fixed nonzero target excess. This statement concerns the order in $`N`$; the displayed upper and lower constants are not asserted optimal. The upper bound allows a joint receiver laboratory, while the construction uses only disjoint helper Bell measurements followed by ordinary target teleportation.

## 6. The fixed-parameter rotor limit

For each fixed $`J`$, the ratio in (6) tends to $`2J+1`$ as even $`N\to\infty`$. Its polynomial upper bound times the fixed-$`b`$ Gaussian weight is summable. Dominated convergence yields

```math
R_N(b)\longrightarrow R_\infty(b)
=
\frac{
\displaystyle\sum_{J=0}^{\infty}
(-1)^J(2J+1)e^{-bJ(J+1)}
}{
\displaystyle\sum_{J=0}^{\infty}
(2J+1)^2e^{-bJ(J+1)}
}
\qquad (b>0\ \text{fixed}).
\tag{10}
```

For orientation, $`R_\infty(2)\approx0.81123466`$, giving this decoder a fidelity of approximately $`0.90561733`$. These decimals are numerical evaluations of the convergent series; (7) supplies the finite certified guarantee.

Fixing $`b`$ in (10) already means physical temperature $`T_N=g/(Nk_{\mathrm B}b)`$. It is not a fixed-physical-temperature thermodynamic limit.

## 7. Entanglement presence and useful output

The inherited spin-block criterion gives an exact finite-$`N`$ threshold:

```math
\rho_N(b)\ \text{is NPT across }A:\mathrm{rest}
\quad\Longleftrightarrow\quad
b>\frac{\ln(N+1)}N.
```

For the stated Kac normalization this is

```math
T<\frac{g}{k_{\mathrm B}\ln(N+1)}.
\tag{11}
```

At equality the cut is PPT. In this qubit–spin family the PPT blocks are also separable, as established by the product-state twirls used in the spin-sector analysis.

The temperature in (11) marks the first presence of entanglement across a target cut. Equations (2) and (9) ask for a fixed advantage in an output task. Their scale is $`1/N`$, rather than $`1/\ln N`$. The [rare-spin analysis](rare-sectors.md) resolves the mechanism: the first negative blocks can carry too little weight to support useful deterministic teleportation.

Reliable operations and records are part of this ideal use model. The finite-temperature theorem concerns the Gibbs state above; it does not by itself establish tolerance of independent errors on every source spin or a preparation-time advantage.

---

[Model and task](model.md) · [Thermal spectrum](thermal-spectrum.md) · [Rare sectors](rare-sectors.md) · [Teleportation bounds](teleportation-bounds.md) · [Helper access](helper-access.md) · [Related work](../references/related-work.md)

