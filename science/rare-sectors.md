# Rare spin sectors and the cost of a tiny teleportation advantage

At the exact NPT onset, a large collective spin sector can contain entanglement even though its Gibbs weight is very small. The relevant scale is therefore not only the sign of a partial-transpose eigenvalue. This page shows how the rare sector controls the amount of entanglement and the best teleportation advantage in the global benchmark.

The result has an essential suppression, with a logarithmic exponent $`-1/4`$. We state the order of limits explicitly. In particular, we do not assume that the optimal fidelity itself has a limit as $`N\to\infty`$ at fixed $`b`$.

## Definitions and the finite operational comparison

Use the [source and multiplicities](thermal-spectrum.md) with $`N=2n`$ and $`b=g/(Nk_{\mathrm B}T)`$. For even $`x`$, define

```math
a_x=e^{-b x(x-2)/4},
\qquad c_x=e^{-b x(x+2)/4},
\qquad h_x(b)=[a_x-(x+1)c_x]_+.
\qquad\text{(1)}
```

Let $`F_N^{\mathrm{glob}}(b)`$ be the optimal one-use average fidelity for an unknown Haar-uniform qubit. The sender owns one physical source spin and the late input. The receiver jointly controls all other $`N-1`$ source spins and can decode its output onto the designated physical output qubit. Local product ancillas, classical communication and the shared frame are allowed; every outcome is counted. No source preparation or laboratory-time advantage is asserted. The [model](model.md) fixes the same task throughout.

Define the nonnegative excess

```math
\Delta_N(b)=F_N^{\mathrm{glob}}(b)-\frac23.
\qquad\text{(2)}
```

It is nonnegative because a protocol can ignore the source and use optimal classical qubit transmission. The proved [finite operational sandwich](teleportation-bounds.md#finite-operational-sandwich) is

```math
\mathcal D_N(b)\le\Delta_N(b)\le\frac23\nu_N(b),
\qquad\text{(3)}
```

where the explicit decoder achieves

```math
\mathcal D_N(b)=\frac{2}{3Z_N(b)}
\sum_{\substack{2\le x\le N\\x\ \mathrm{even}}}
\frac{d_{N-1}((x-1)/2)}{x}\,h_x(b).
\qquad\text{(4)}
```

The upper bound remains valid when the source is divided among more laboratories. The matching decoder and the rate below use the receiver's joint control of the other $`N-1`$ spins. Joint control of helpers alone while both endpoints remain separate is a different model; no matching rare-excess rate for that model is claimed.

In each normalized spin block, the decoder's excess is $`2\nu_j/[3(x-1)]`$. Compared with the negativity upper bound, it loses only a factor polynomial in the spin dimension. That loss will not change the essential logarithmic rate.

## An explicit uniform finite bound

Write $`L=\ln(1/b)`$. For every even finite $`N`$ and $`0\lt b\le1/4`$,

```math
\boxed{
\nu_N(b)\le
\min\!\left\{
\frac12,
\frac{L+4}{2b}\exp\!\left[-\frac{L^2}{8b}\right]
\right\}.
}
\qquad\text{(5)}
```

Consequently, $`\Delta_N(b)`$ is bounded by two thirds of the same expression. The coefficient $`1/8`$ here is a conservative finite bound; the sharp limiting coefficient will be $`1/4`$.

**Proof.** Since $`Z_N(b)\ge D_N`$ and the rest multiplicity in [equation (16)](thermal-spectrum.md#multiplicity-ratios-used-in-the-limiting-arguments) is at most $`xD_N/2`$, the exact spectrum gives

```math
\nu_N(b)\le\frac12
\sum_{\substack{2\le x\le N\\x\ \mathrm{even}}}
(x-1)e^{-b x(x-2)/4}
\mathbf1\{bx>\ln(x+1)\}.
\qquad\text{(6)}
```

A contributing $`x`$ satisfies $`x>\ln3/b>1/b`$, and therefore

```math
bx>\ln(x+1)>\ln(1/b)=L.
\qquad\text{(7)}
```

Thus $`x>L/b`$. It also has $`x\ge4`$, so $`x(x-2)\ge x^2/2`$. Dropping the finite upper cutoff, including every integer instead of only even integers, and replacing $`x-1`$ by $`x`$ yield

```math
\nu_N(b)\le\frac12
\sum_{\substack{x\in\mathbb Z\\x\ge L/b}}
x e^{-b x^2/8}.
\qquad\text{(8)}
```

The function $`f(x)=x e^{-b x^2/8}`$ decreases for $`x\ge2/\sqrt b`$. For $`b\le1/4`$, $`L\ge2\sqrt b`$, so the sum begins in its decreasing region. The first-term-plus-integral estimate gives

```math
\sum_{\substack{x\in\mathbb Z\\x\ge L/b}}f(x)
\le f(L/b)+\int_{L/b}^{\infty}f(t)\,dt
=\frac{L+4}{b}e^{-L^2/(8b)}.
\qquad\text{(9)}
```

Combining (8)–(9) with the general $`\nu_N\le1/2`$ proves (5). The bound also applies when the finite source is exactly PPT, in which case its negativity and teleportation excess are zero.

## The ordered limit for source negativity

For each fixed $`b>0`$, define

```math
S(b)=\sum_{J=0}^{\infty}(2J+1)^2e^{-bJ(J+1)},
\qquad\text{(10)}
```

```math
A(b)=\frac12\sum_{\substack{x\ge2\\x\ \mathrm{even}}}
(x-1)e^{-b x(x-2)/4}
\left[1-(x+1)e^{-bx}\right]_+.
\qquad\text{(11)}
```

Both series converge. The exact multiplicity ratios and their uniform bounds give, by dominated convergence,

```math
\frac{Z_N(b)}{D_N}\longrightarrow S(b),
\qquad
\nu_N(b)\longrightarrow\nu_\infty(b):=\frac{A(b)}{S(b)}
\quad(N\to\infty\text{ through even }N).
\qquad\text{(12)}
```

For the denominator, the summable dominating sequence is $`(2J+1)^2e^{-bJ(J+1)}`$. For the negativity numerator divided by $`D_N`$, use $`(x-1)e^{-b x(x-2)/4}/2`$. Terms outside a finite source's spin range are extended by zero before taking the limit.

The limiting negativity is strictly positive for every fixed $`b>0`$: sufficiently large even $`x`$ obey $`bx>\ln(x+1)`$. This does not describe fixed physical temperature. Holding $`b`$ fixed as $`N`$ grows means taking $`T_N=g/(Nk_{\mathrm B}b)`$, already a temperature of order $`1/N`$.

The denominator has only polynomial growth as $`b\downarrow0`$:

```math
S(b)\sim\sqrt\pi\,b^{-3/2}.
\qquad\text{(13)}
```

Indeed, put $`u_J=\sqrt b(J+1/2)`$ and use $`J(J+1)=(J+1/2)^2-1/4`$. Then $`b^{3/2}S(b)`$ is a Gaussian Riemann sum converging to $`4\int_0^\infty u^2e^{-u^2}\,du=\sqrt\pi`$. In particular, $`\ln S(b)=O(\ln(1/b))`$.

## Sharp logarithmic rate

The exact source limit obeys

```math
\boxed{
\lim_{b\downarrow0}
\frac{b}{[\ln(1/b)]^2}\ln\nu_\infty(b)
=-\frac14.
}
\qquad\text{(14)}
```

The exponent comes from the first spin sectors that can be NPT. They occur at $`x`$ of order $`\ln(1/b)/b`$, far above the thermally typical order $`b^{-1/2}`$. Their Boltzmann cost is therefore of order $`\exp[-\ln^2(1/b)/(4b)]`$ on the logarithmic scale specified in (14).

**Upper bound.** Fix $`0\lt \varepsilon\lt 1`$ and let $`L=\ln(1/b)`$. Equation (7) restricts every positive term to $`x>L/b`$. For all sufficiently small $`b`$, uniformly on this tail,

```math
x(x-2)\ge(1-\varepsilon)x^2.
```

Drop the bracket in (11), replace even $`x`$ by all integers, and apply the same Gaussian sum estimate as above, now with exponent $`(1-\varepsilon)bx^2/4`$. It gives

```math
A(b)\le
\left(\frac{L}{2b}+\frac1{(1-\varepsilon)b}\right)
\exp\!\left[-\frac{(1-\varepsilon)L^2}{4b}\right]
\qquad\text{(15)}
```

for all sufficiently small $`b`$. The logarithm of the prefactor is $`O(L+\ln L)`$, negligible compared with $`L^2/b`$. Since $`S(b)\ge1`$,

```math
\limsup_{b\downarrow0}\frac b{L^2}\ln\nu_\infty(b)
\le-\frac{1-\varepsilon}{4}.
```

Let $`\varepsilon\downarrow0`$.

**Lower bound.** Fix any $`a>1`$ and choose the smallest even integer $`x_b\ge aL/b`$. Then

```math
x_b=\frac{aL}{b}+O(1),
\qquad
(x_b+1)e^{-bx_b}=O(Lb^{a-1})\longrightarrow0.
\qquad\text{(16)}
```

For all sufficiently small $`b`$, the bracket in that one term of (11) is at least $`1/2`$. Using (13),

```math
\ln\nu_\infty(b)
\ge-\frac{b x_b(x_b-2)}4-C_a(L+\ln L)
=-\frac{a^2L^2}{4b}+o(L^2/b).
\qquad\text{(17)}
```

Thus the lower limit is at least $`-a^2/4`$. Let $`a\downarrow1`$. This proves (14), without requiring a sharper expansion of the root of $`bx=\ln(x+1)`$.

## The same rate for optimal teleportation excess

For each fixed $`b>0`$, the decoder in (4) has the limit

```math
\mathcal D_N(b)\longrightarrow
d(b):=\frac1{3S(b)}
\sum_{\substack{x\ge2\\x\ \mathrm{even}}}
e^{-b x(x-2)/4}
\left[1-(x+1)e^{-bx}\right]_+>0.
\qquad\text{(18)}
```

Dominated convergence again applies, because $`d_{N-1}((x-1)/2)/(xD_N)\le1/2`$. Retaining the same one term $`x_b`$ used in (16) gives

```math
\liminf_{b\downarrow0}\frac b{L^2}\ln d(b)\ge-\frac14.
\qquad\text{(19)}
```

Its missing factor $`x_b-1`$ relative to (11) changes the logarithm only by $`O(L+\ln L)`$. The upper bound $`d(b)\le2\nu_\infty(b)/3`$ and (14) therefore show that its logarithmic rate is also exactly $`-1/4`$.

Define the two ordered envelopes

```math
\Delta_-(b)=\liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}\Delta_N(b),
\qquad
\Delta_+(b)=\limsup_{\substack{N\to\infty\\N\ \mathrm{even}}}\Delta_N(b).
\qquad\text{(20)}
```

The finite operational sandwich implies

```math
0\lt d(b)\le\Delta_-(b)\le\Delta_+(b)\le\frac23\nu_\infty(b).
\qquad\text{(21)}
```

Both endpoints in this sandwich have the same logarithmic rate. Hence

```math
\boxed{
\lim_{b\downarrow0}\frac b{[\ln(1/b)]^2}\ln\Delta_-(b)
=\lim_{b\downarrow0}\frac b{[\ln(1/b)]^2}\ln\Delta_+(b)
=-\frac14.
}
\qquad\text{(22)}
```

Equation (22) is the claimed ordered operational law. It does not assert $`\Delta_-(b)=\Delta_+(b)`$ at a fixed $`b`$, nor an exact optimal fidelity or prefactor.

## A controlled simultaneous finite-size regime

There is also a sufficient joint regime, stated without interchanging the limits. Let even $`N\to\infty`$ and let $`b_N\downarrow0`$ satisfy

```math
\frac{N b_N^2}{[\ln(1/b_N)]^2}\longrightarrow\infty.
\qquad\text{(23)}
```

Then both the finite source negativity and the finite optimal global excess have the sharp rate:

```math
\boxed{
\lim_{N\to\infty}
\frac{b_N}{[\ln(1/b_N)]^2}\ln\nu_N(b_N)
=\lim_{N\to\infty}
\frac{b_N}{[\ln(1/b_N)]^2}\ln\Delta_N(b_N)
=-\frac14.
}
\qquad\text{(24)}
```

**Proof.** The finite upper bound leading to (15) is uniform in $`N`$, since it used only $`Z_N\ge D_N`$ and the multiplicity upper bound. It gives the same upper logarithmic rate for $`\nu_N`$, and then for $`\Delta_N`$.

For the lower bound, choose the same even $`x_{b_N}\ge a\ln(1/b_N)/b_N`$. Condition (23) gives $`x_{b_N}^2/N\to0`$, so this spin is allowed for all large $`N`$. The exact product in (16) of [the spectrum page](thermal-spectrum.md#multiplicity-ratios-used-in-the-limiting-arguments), divided by $`x_{b_N}/2`$, tends to one. Also

```math
\frac{Z_N(b_N)}{D_N}\le S(b_N)=O(b_N^{-3/2}).
```

Thus this single term gives the lower rate in (17) for $`\nu_N`$, and its decoder counterpart (4) gives the same lower rate for $`\Delta_N`$. Let $`a\downarrow1`$ to finish the proof.

Condition (23) is sufficient, not necessary. No assertion is made here for an arbitrary joint sequence, for fixed physical temperature, or for the edge-sector region immediately below the finite NPT onset. In a different regime the finite source can be PPT, and then the logarithms of its zero excess do not have the value in (24).

## What changes operationally

The [exact NPT boundary](thermal-spectrum.md#exact-onset-of-a-negative-partial-transpose) occurs at a temperature of order $`g/\ln N`$. By contrast, a teleportation excess bounded away from zero requires, and the known Bell decoder can attain at, a temperature of order $`g/N`$ under the stated supplied-source model. In between, detecting a rare entangled sector is much less demanding than obtaining a useful one-use channel from the complete ensemble. Equations (14), (22) and (24) quantify that difference in the specified limits.

The inherited ingredients are the collective Gibbs family, spin multiplicities, invariant block spectrum, negativity monotonicity and Bell-subspace teleportation. The added conclusion is the operational cooling law and the sharp rare-sector suppression of the complete task, with the party model and limit order retained. The [teleportation proof](teleportation-bounds.md) and source comparisons identify those dependencies; no new preparation method, unrestricted hardware advantage or first entanglement-unlocking claim is implied.
