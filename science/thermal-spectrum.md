# Thermal spectrum and the single-spin entanglement boundary

The supplied source is the Gibbs state of an isotropic collective antiferromagnet. Its energy normalization matters: the same temperature has a different meaning for a fixed pair coupling and for an interaction divided by the number of spins. This project uses the latter normalization throughout.

The spectrum and the rotationally invariant partial-transpose method below are established tools. Their explicit derivation fixes the normalization used by the [teleportation bounds](teleportation-bounds.md) and the [rare-sector analysis](rare-sectors.md). A negative partial transpose is a statement about the presence of entanglement; it does not establish a useful amount of quantum transmission.

## Model and conventions

Let $`N=2n\ge2`$ be even. Each physical site carries a spin one half, and

```math
\mathbf J=\frac12\sum_{i=1}^{N}\boldsymbol\sigma_i,
\qquad H_N=\frac gN\mathbf J^2,
\qquad g>0.
```

At temperature $`T>0`$, put

```math
b=\frac{g}{Nk_{\mathrm B}T},
\qquad
\rho_N(b)=\frac{e^{-b\mathbf J^2}}{Z_N(b)},
\qquad
Z_N(b)=\operatorname{Tr}e^{-b\mathbf J^2}.
```

Here $`b`$ is dimensionless. All logarithms on this page and in the asymptotic proofs are natural logarithms. The Gibbs state is supplied; preparing it, cooling it, and measuring or calibrating its Hamiltonian are separate physical costs. The [model](model.md) specifies the allowed laboratories and the one-use teleportation task.

For $`M`$ spins, let $`d_M(j)`$ be the multiplicity of the spin-$`j`$ representation:

```math
d_M(j)=\binom{M}{M/2-j}-\binom{M}{M/2-j-1}.
\tag{1}
```

Allowed spins differ by one and have the same integer or half-integer parity as $`M/2`$. A binomial coefficient with an inadmissible integer lower argument is zero. The projector $`P_j^{(M)}`$ includes all multiplicities and therefore has rank $`(2j+1)d_M(j)`$. Consequently,

```math
\rho_N(b)=\frac1{Z_N(b)}
\sum_{J=0}^{n}e^{-bJ(J+1)}P_J^{(N)},
\qquad
Z_N(b)=\sum_{J=0}^{n}(2J+1)d_N(J)e^{-bJ(J+1)}.
\tag{2}
```

Fix one physical spin $`A`$. Permutation invariance makes the choice of that site irrelevant. The negativity across $`A:A^c`$ is

```math
\nu_N(b)=\frac{\|\rho_N(b)^{T_A}\|_1-1}{2}.
\tag{3}
```

In the global benchmark, $`A`$ is the sender's one source spin and all $`N-1`$ other source spins are in the receiver's joint laboratory. Bounds across this cut also constrain more separated models, because grouping sites into one laboratory only enlarges the allowed operations. Matching teleportation constructions must retain the laboratory model in which they are proved.

## The invariant block and its partial transpose

The rest has half-integer spin $`j=\ell-\tfrac12`$, where $`\ell=1,\ldots,n`$. Define

```math
x=2j+1=2\ell,
\qquad
a_x=e^{-b x(x-2)/4},
\qquad
c_x=e^{-b x(x+2)/4}.
\tag{4}
```

The two possible total spins are $`j-\tfrac12=(x-2)/2`$ and $`j+\tfrac12=x/2`$. Thus the exponents in (4) are their actual energies $`J(J+1)`$. In particular, the first exponent is $`x(x-2)/4`$.

For every copy of the rest's spin-$`j`$ multiplicity space, the unnormalized Gibbs operator is

```math
X_j=a_xP_-+c_xP_+,
\qquad
t_x=\operatorname{Tr}X_j=(x-1)a_x+(x+1)c_x.
\tag{5}
```

Here $`P_-`$ and $`P_+`$ are the projectors onto total spins $`j-\tfrac12`$ and $`j+\tfrac12`$, of ranks $`x-1`$ and $`x+1`$. The corresponding normalized block is $`\tau_j=X_j/t_x`$, and its probability in the source is

```math
p_j=\frac{d_{N-1}(j)t_x}{Z_N(b)}.
\tag{6}
```

These probabilities sum to one by the Clebsch–Gordan decomposition. The multiplicity factors are not additional entangled systems across the cut.

To compute the partial transpose explicitly, write $`K=\mathbf J_{A^c}\cdot\boldsymbol\sigma_A`$. Its two eigenvalues are $`j`$ and $`-(j+1)`$, so

```math
P_- =\frac{jI-K}{x},
\qquad
P_+ =\frac{(j+1)I+K}{x}.
\tag{7}
```

Transposition of the qubit, followed by conjugation by its spin-flip unitary, sends every Pauli matrix to its negative. This is a unitary conjugate of the partial transpose and preserves its spectrum. It sends $`K`$ to $`-K`$. Substitution in (5) therefore gives the two eigenvalues of the unnormalized partial transpose:

```math
\lambda_+(x)=\frac{(x-1)a_x+c_x}{x}
\quad\text{with multiplicity }x+1,
```

```math
\lambda_-(x)=\frac{-a_x+(x+1)c_x}{x}
\quad\text{with multiplicity }x-1.
\tag{8}
```

Only the second eigenvalue can be negative. It follows that

```math
\nu_j:=\nu(\tau_j)
=\frac{x-1}{x\,t_x}\,[a_x-(x+1)c_x]_+,
\qquad [u]_+=\max\{u,0\},
\tag{9}
```

and the exact finite source negativity is

```math
\boxed{
\nu_N(b)=\frac1{Z_N(b)}
\sum_{\substack{2\le x\le N\\x\ \mathrm{even}}}
d_{N-1}\!\left(\frac{x-1}{2}\right)
\frac{x-1}{x}
\left[
e^{-b x(x-2)/4}-(x+1)e^{-b x(x+2)/4}
\right]_+.
}
\tag{10}
```

The orthogonal rest-spin blocks explain why their negativities add with the probabilities (6). This is an equality for the supplied finite state, with no thermodynamic limit or low-temperature approximation.

## Exact onset of a negative partial transpose

Since $`a_x/c_x=e^{bx}`$, (8) is negative exactly when

```math
bx>\ln(x+1).
\tag{11}
```

The function $`\ln(x+1)/x`$ decreases for $`x>0`$: its derivative has the sign of $`x/(x+1)-\ln(x+1)<0`$. The largest allowed value $`x=N`$ has nonzero rest multiplicity. Therefore

```math
\boxed{
\nu_N(b)>0
\quad\Longleftrightarrow\quad
b>\frac{\ln(N+1)}{N}
\quad\Longleftrightarrow\quad
T<\frac{g}{k_{\mathrm B}\ln(N+1)}.
}
\tag{12}
```

At equality every block is positive under partial transpose, with a zero eigenvalue in the extremal block. The same PPT conclusion holds above the stated temperature.

For these invariant qubit–spin blocks, PPT also implies separability across the one-spin cut, as established by Schliemann. One can see the needed construction directly. A normalized invariant block is determined by its lower-spin probability $`q=(x-1)a_x/t_x`$. The PPT interval is $`0\le q\le(x-1)/x`$. Collective-rotation twirls of the product states $`|\uparrow\rangle|j,j\rangle`$ and $`|\downarrow\rangle|j,j\rangle`$ have lower-spin probabilities zero and $`(x-1)/x`$, respectively. Their convex mixtures cover that interval and are separable. The rest multiplicity flags are local to the receiver, so the complete PPT source is separable across $`A:A^c`$. This is a classification of the one-spin cut, not a full-separability classification of all $`N`$ individual spins.

The [block decoder](teleportation-bounds.md#finite-operational-sandwich) gives a strictly positive, possibly extremely small, teleportation excess whenever a block satisfies (11). Thus in the global benchmark the onset of any excess above the classical fidelity coincides with (12). The temperature needed for an excess bounded away from zero is much lower.

## A uniform bound on the amount

Equation (9) implies

```math
0\le\nu_j\le\frac1x.
\tag{13}
```

Indeed, after dropping the negative term in its numerator and using $`t_x\ge(x-1)a_x`$, the right side follows immediately. Equality is the zero-upper-sector limit $`c_x/a_x\to0`$ at fixed $`j`$.

Every contributing block obeys $`bx>\ln(x+1)\ge\ln3`$. Its negativity is therefore at most $`b/\ln3`$. Averaging over (6), and also using $`x\ge2`$, yields

```math
\boxed{
\nu_N(b)\le\min\!\left\{\frac12,\frac b{\ln3}\right\}.
}
\tag{14}
```

This bound holds for every finite even $`N`$ and every $`b>0`$. It does not assume a typical-spin approximation. Together with negativity monotonicity, it forces the [operational cooling scale](teleportation-bounds.md) for a fixed teleportation advantage. The [rare-sector bound](rare-sectors.md#an-explicit-uniform-finite-bound) gives a much smaller estimate when $`b`$ tends to zero.

## Multiplicity ratios used in the limiting arguments

Let $`D_N=d_N(0)=\binom{2n}{n}/(n+1)`$. Direct evaluation of (1) gives

```math
\frac{d_N(J)}{D_N}
=(2J+1)\frac{n+1}{n+J+1}
\prod_{r=0}^{J-1}\frac{n-r}{n+r+1}
\le2J+1,
\qquad 0\le J\le n,
\tag{15}
```

and

```math
\frac{d_{N-1}(\ell-\tfrac12)}{D_N}
=\ell\frac{n+1}{n+\ell}
\prod_{r=1}^{\ell-1}\frac{n-r}{n+r}
\le\ell,
\qquad1\le\ell\le n.
\tag{16}
```

Empty products equal one. In particular, $`d_{N-1}(\tfrac12)=D_N`$. Every factor after $`2J+1`$ or $`\ell`$ is at most one. For any fixed $`J`$ or $`\ell`$, these factors tend to one as $`N\to\infty`$. Hence

```math
\frac{d_N(J)}{D_N}\longrightarrow2J+1,
\qquad
\frac{d_{N-1}(\ell-\tfrac12)}{D_N}\longrightarrow\ell.
\tag{17}
```

The convergence of (16), divided by $`\ell`$, remains uniform along a sequence with $`\ell^2/N\to0`$. To see this directly, take logarithms of its product. For $`\ell/n\le1/2`$, the elementary bound $`|\ln(1-u)-\ln(1+u)|\le C u`$ for $`0\le u\le1/2`$ gives a total logarithmic error $`O(\ell^2/n)`$, including the prefactor. It tends to zero. This explicit condition is used in the simultaneous limit, rather than assuming fixed-spin asymptotics at an arbitrarily growing spin.

## Attribution and verification

The spin multiplicities and collective singlet structure are standard Schur–Weyl ingredients; see Livine and Terno, [*Entanglement of zero-angular-momentum mixtures and black-hole entropy*](https://arxiv.org/abs/quant-ph/0502043v2), Phys. Rev. A **72**, 022307 (2005). The rotationally invariant qubit–spin partial-transpose spectrum is established in Schliemann, [*Entanglement in SU(2)-invariant quantum spin systems*](https://arxiv.org/abs/quant-ph/0212114v3), Phys. Rev. A **68**, 012309 (2003), Section III, Eqs. (3)–(9). Equations (7)–(10) reproduce the needed calculation to make its normalization and degeneracies inspectable. The Gibbs family and its entanglement-presence questions are not new source models or new PPT criteria. The exact thermal threshold (12) is a direct specialization of this inherited spectrum to the supplied Gibbs weights.

The contribution uses these ingredients to separate exact entanglement onset from the amount available for a complete teleportation task, and to establish the [rare-sector operational law](rare-sectors.md). The source comparison in the repository's references identifies the relevant thermal and teleportation antecedents and its reading scope.

[The spectrum check](../verification/check_spectrum.py) compares (10) against direct dense partial transposes of the finite Gibbs matrix, checks the exact multiplicity products, and tests boundary and uniform-bound cases. Those calculations support the tested instances. The arbitrary-size statements are proved above.
