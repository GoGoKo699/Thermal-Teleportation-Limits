# What separated helpers can extract

The thermal communication bound has a second control boundary. Cooling the source into its singlet sector does not by itself make its entanglement freely accessible to individually separated spins. For the maximally mixed singlet, arbitrary singleton-party collaboration has an exact one-copy teleportation score that approaches the classical value. A layer of joint measurements on helper pairs reaches the known perfect endpoint.

The contrast is about the allowed quantum operations on the same supplied state. Full Bell-measurement teleportation from a spin-zero resource was established by [Barjaktarevic et al. (2005)](https://doi.org/10.1103/PhysRevLett.95.230501) and is explicitly described with nearest-neighbor helper measurements by [Gray et al. (2016)](https://doi.org/10.1103/PhysRevB.94.195136). That positive protocol is inherited. The quantitative singleton converse below specifies how much can be achieved without those joint helper operations.

## Singleton access to the maximally mixed singlet

Let $`\rho_N^{(0)}=P_0^{(N)}/D_N`$, with fixed physical targets $`A,B`$. Every party controls one source spin, the sender also receives the independent unknown input, local ancillary states are initially product, and arbitrary classical communication is allowed. Then

```math
\boxed{
F_N^{\mathrm{single}}(0)
=\frac23+\frac{1}{3(N-1)}.
}
```

The notation $`(0)`$ here means zero physical temperature, not $`b=0`$. All outcomes are retained in the score.

The associated optimal average target-pair concurrence under singleton LOCC is exactly $`1/(N-1)`$. The direct teleportation converse is slightly more informative: it also covers protocols that involve the unknown input before helper processing has ended.

### A hidden matching gives a protocol-wide converse

The standard valence-bond resolution writes the maximally mixed singlet as the uniform mixture over all perfect matchings $`M`$ of the $`N`$ labelled sites,

```math
\rho_N^{(0)}
=\frac{1}{(N-1)!!}
\sum_M |M\rangle\langle M|,
\qquad
|M\rangle=\bigotimes_{(i,j)\in M}|s\rangle_{ij}.
```

Each product lies in total spin zero. Permutation averaging gives the identity on the irreducible symmetric-group multiplicity space, which proves the resolution. This representation is known and also appears in the existing [Singlet-Access-Limits account](https://github.com/GoGoKo699/Singlet-Access-Limits/blob/main/research/ACCESS_LAW.md). No matching label is supplied to the parties.

For a fixed matching, suppose $`A`$ is not directly paired with $`B`$. Partition the singleton laboratories into a side containing the matching component of $`A`$ and another containing the component of $`B`$. The source is product across this cut. Place the late input on the $`A`$ side. Any allowed complete protocol remains LOCC across the cut, so its induced sender-to-$`B`$ channel is entanglement breaking and has Haar-average fidelity at most $`2/3`$. This includes arbitrary adaptivity and local processing at the two targets.

If $`A,B`$ are directly paired, the trivial upper bound is $`1`$. A uniformly random matching pairs them with probability $`1/(N-1)`$. The score of any fixed protocol is linear in its source state, so averaging these two bounds gives the displayed upper bound. The same argument bounds average concurrence by the probability of a direct target dimer. Convexity handles the unobserved mixture; no inference from an average entanglement measure to a particular measurement branch is needed.

### Common-axis helper measurements attain the bound

Measure all $`N-2`$ helpers in a common $`Z`$ basis. Let $`h=(N-2)/2`$. For a balanced helper outcome, the conditional target state is

```math
\omega_{AB}
=\left(\frac12+\frac1N\right)|s\rangle\langle s|
+\left(\frac12-\frac1N\right)|t_0\rangle\langle t_0|.
```

To obtain the weights, the helper spin-zero and spin-one multiplicities obey

```math
d_{N-2}(0)=\frac{1}{h+1}\binom{2h}{h},
\qquad
\frac{d_{N-2}(1)}{3}
=\frac{h}{h+2}d_{N-2}(0).
```

The diagonal weight of a fixed balanced product string in a helper spin-$`j`$ projector is $`d_{N-2}(j)/\binom{N-2}{h}`$. Coupling to the two target spins leaves the singlet and the zero-magnetization triplet with the preceding multiplicity ratio. The aggregate probability of balanced outcomes is

```math
p_{\mathrm{bal}}=\frac{N}{2(N-1)}.
```

The state $`\omega_{AB}`$ has concurrence $`2/N`$ and Bell fraction $`1/2+1/N`$. Standard teleportation in those branches has fidelity $`2/3+2/(3N)`$. In the other nonzero branches, the targets are polarized product states; use optimal classical transmission. Thus the unconditional excess is

```math
p_{\mathrm{bal}}\frac{2}{3N}
=\frac{1}{3(N-1)}.
```

For $`N=2`$ there are no helpers and the source is a singlet; the same final score is $`1`$. This endpoint may be handled directly rather than using helper multiplicities.

## A universal permutation-and-rotation ceiling

The converse extends beyond the zero-temperature source. Any density matrix invariant under both all site permutations and collective $`SU(2)`$ rotations is a mixture of normalized total-spin projectors. For each total spin $`J`$, its normalized projector is the permutation-and-rotation twirl of a product containing $`N/2-J`$ singlet dimers and $`2J`$ aligned spins. This follows from the multiplicity-free Schur–Weyl decomposition after imposing both commutants.

For a fixed term in that decomposition, singleton operations can convey a quantum advantage between $`A,B`$ only if they occupy the same dimer. Its probability after the permutation average is $`(N-2J)/[N(N-1)]`$. Hence

```math
F^{\mathrm{single}}(\rho)-\frac23
\le\frac{\mathbb E_\rho[N-2J]}{3N(N-1)}
\le\frac{1}{3(N-1)}.
```

Similarly, the average localizable concurrence is at most $`\mathbb E[N-2J]/[N(N-1)]`$. The maximally mixed singlet attains the largest ceiling, as shown above.

Both invariances matter. A GHZ state is permutation invariant and can yield a perfect target pair through singleton helper measurements, but is not collective-$`SU(2)`$ invariant. A specified singlet dimer is rotation invariant and gives its endpoints a perfect resource, but breaks permutation invariance. The result concerns the jointly invariant mixed state, not arbitrary singlet-supported pure states or every state with one of the two symmetries.

In particular, the thermal source in this project belongs to the invariant class at every temperature. Singleton access therefore never gives a nonvanishing one-copy quantum teleportation advantage as $`N`$ grows, even at zero temperature.

## The known paired-helper endpoint

Every spin-zero state is a simultaneous eigenstate of the global Pauli parities,

```math
X^{\otimes N}=Z^{\otimes N}=(-1)^{N/2}I
\quad\text{on the singlet subspace}.
```

A full Bell measurement on a helper pair reads the commuting products $`X_iX_j`$ and $`Z_iZ_j`$. Take any fixed perfect matching of the $`N-2`$ helpers and measure its pairs. Multiplying their outcome signs determines the two target parities $`X_AX_B`$ and $`Z_AZ_B`$. The corresponding target joint eigenspace is one Bell state. A target Pauli correction makes that state fixed and known in every nonzero branch.

This argument works for an arbitrary density matrix supported on total spin zero. It is the Bell-subspace mechanism of the 2005 teleportation protocol, not a new unlocking discovery. The measurements form one parallel layer when the fixed helper pairs can be operated on simultaneously. They can be geometrically local when the helper sites admit the required local perfect matching; no such matching or hardware schedule is assumed for every geometry.

Only two aggregate parity signs are needed for the final correction. The experiment may still acquire two bits from every helper Bell measurement. No detector-bandwidth, classical-message, or laboratory-latency improvement is claimed.

## A fixed disjoint-pair budget converse

There is also a useful partial-access upper bound for the maximally mixed singlet. Fix, before any source-dependent observation, a helper partition with $`k`$ disjoint pairs and $`N-2-2k`$ singleton helpers. Allow arbitrary quantum operations inside each helper pair and unrestricted classical communication between all resulting laboratories. The targets remain singleton laboratories. Then

```math
F_{N,k}-\frac23\le\frac{1}{3(N-2k-1)},
\qquad
0\le k\le\frac{N-2}{2}.
```

To prove it, draw a hidden singlet matching $`M`$ from the source's uniform decomposition and add the $`k`$ fixed helper-pair edges as a second edge color. Each helper site belonging to a pair has degree two in this two-colored multigraph; the other sites, including $`A,B`$, have degree one. Coincident edges form an alternating two-edge cycle. The full multigraph consists of alternating cycles and paths. Contract every path through paired helpers. Its endpoints are the $`N-2k`$ unpaired sites, and permutation invariance makes the induced endpoint matching uniform. The probability that $`A,B`$ belong to the same connected component is therefore $`1/(N-2k-1)`$.

When their components differ, the initial resource is product across a cut that is a union of complete helper laboratories. The full allowed protocol is LOCC across that cut, so its teleportation score is at most $`2/3`$. In the connected event use the upper bound $`1`$ and average, exactly as in the singleton proof.

The converse is attained at the two endpoints $`k=0`$ and $`k=(N-2)/2`$ by the preceding protocols. No optimality claim is made for intermediate $`k`$. The statement does not cover adaptive changes of helper partners, overlapping joint-operation graphs, or a budget of arbitrary two-qubit gates. Those are different access models.

For this fixed partition model, a prescribed excess $`\delta>0`$ requires $`N-2k-1\le1/(3\delta)`$. Thus all but a bounded number of helper sites must belong to quantum-capable pairs to retain a fixed advantage. This is a constraint on the allowed helper partition of one supplied state, not a preparation-depth or transport-time lower bound.
