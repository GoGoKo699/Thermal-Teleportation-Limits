# Related work and attribution

The contribution concerns the use of a supplied thermal state of the collective antiferromagnet. The [model](../science/model.md) fixes a one-qubit sender, a late unknown input, a deterministic average-fidelity score and the receiver's allowed quantum control. The central conclusions are the useful-cooling law and the rare-spin suppression of optimized teleportation; [helper access](../science/helper-access.md) separately quantifies restrictions on helper cooperation.

The Hamiltonian, spin decomposition, qubit–spin partial transpose, teleportation benchmarks and singlet Bell decoder have established antecedents. The [source-evidence record](source-evidence.md) identifies the inspected versions and the scope of those comparisons.

## Spin sectors and thermal entanglement

**[S03] John Schliemann, “Entanglement in SU(2)-invariant quantum spin systems,” Physical Review A 68, 012309 (2003).** [DOI](https://doi.org/10.1103/PhysRevA.68.012309) · [arXiv:quant-ph/0212114](https://arxiv.org/abs/quant-ph/0212114)

Section III gives the partial-transpose spectrum and the equivalence of PPT and separability for a rotationally invariant spin-$`j`$ system coupled to a qubit. Substituting the thermal weights and the largest receiver spin yields the finite-$`N`$ onset $`b=\ln(N+1)/N`$. The [thermal-spectrum page](../science/thermal-spectrum.md) reconstructs this inherited calculation. The spectrum and that direct threshold specialization are not assigned independent novelty here.

**[T05] Géza Tóth, “Entanglement witnesses in spin models,” Physical Review A 71, 010301(R) (2005).** [DOI](https://doi.org/10.1103/PhysRevA.71.010301) · [arXiv:quant-ph/0406061](https://arxiv.org/abs/quant-ph/0406061)

Section II.C treats the complete-graph collective-spin Hamiltonian and thermal entanglement detection. The existence of entanglement in this model is established background.

**[VAE14] Giuseppe Vitagliano, Iagoba Apellaniz, Iñigo L. Egusquiza and Géza Tóth, “Spin squeezing and entanglement for an arbitrary spin,” Physical Review A 89, 032307 (2014).** [DOI](https://doi.org/10.1103/PhysRevA.89.032307) · [arXiv:1310.2269](https://arxiv.org/abs/1310.2269)

Section III.B, Eqs. (35)–(36), identifies the permutation-average product of singlet dimers as the uniform qubit singlet and as the zero-temperature ensemble of $`\mathbf J^2`$. The dimer decomposition and two-producibility are inherited ingredients of the [singleton converse](../science/helper-access.md).

**[RC05] Raúl Rossignoli and Norma Canosa, “Global thermal entanglement in n-qubit systems,” Physical Review A 72, 012335 (2005).** [DOI](https://doi.org/10.1103/PhysRevA.72.012335) · [arXiv:1312.7370](https://arxiv.org/abs/1312.7370)

This work treats global and reduced negativities for thermal full-range and nearest-neighbor spin models. Its general full-range XYZ formalism contains the isotropic collective antiferromagnet as a parameter choice, and it already relates negativity to teleportation bounds. The detailed finite-size XY examples do not establish the present optimized physical-qubit teleportation rate or its useful-cooling law.

**[MRC08] Juan Mauricio Matera, Raúl Rossignoli and Norma Canosa, “Thermal entanglement in fully connected spin systems and its random-phase-approximation description,” Physical Review A 78, 012316 (2008).** [DOI](https://doi.org/10.1103/PhysRevA.78.012316) · [arXiv:1104.5694](https://arxiv.org/abs/1104.5694)

This paper studies thermal pairwise concurrence for attractive fully connected XYZ couplings and a maximal-spin ground-state family. Its Kac normalization and sector bookkeeping are relevant background. A pairwise reduced-state concurrence is a different output from teleportation assisted by a jointly controlled receiver laboratory.

## Teleportation and localizable entanglement

**[H99] Michał Horodecki, Paweł Horodecki and Ryszard Horodecki, “General teleportation channel, singlet fraction, and quasidistillation,” Physical Review A 60, 1888 (1999).** [DOI](https://doi.org/10.1103/PhysRevA.60.1888) · [arXiv:quant-ph/9807091](https://arxiv.org/abs/quant-ph/9807091)

The channel–state relation, singlet-fraction benchmark and general trace-preserving teleportation framework are inherited. The present [teleportation bounds](../science/teleportation-bounds.md) apply these tools to the specified thermal source and control partition.

**[VW02] Guifré Vidal and Reinhard F. Werner, “Computable measure of entanglement,” Physical Review A 65, 032314 (2002).** [DOI](https://doi.org/10.1103/PhysRevA.65.032314) · [arXiv:quant-ph/0102117](https://arxiv.org/abs/quant-ph/0102117)

Negativity monotonicity and its use as a teleportation upper bound are established tools. The new thermal conclusions depend on the weight of the contributing spin sectors and a matching task construction, rather than on a new entanglement monotone.

**[P05] Markus Popp, Frank Verstraete, Miguel A. Martín-Delgado and J. I. Cirac, “Localizable entanglement,” Physical Review A 71, 042306 (2005).** [DOI](https://doi.org/10.1103/PhysRevA.71.042306) · [arXiv:quant-ph/0411123](https://arxiv.org/abs/quant-ph/0411123)

Localizable entanglement, including mixed-state extensions, supplies the established language for helper measurements. The complete teleportation converse here also permits adaptation after the unknown input arrives.

**[G06] Gilad Gour, “Entanglement of collaboration,” Physical Review A 74, 052307 (2006).** [DOI](https://doi.org/10.1103/PhysRevA.74.052307) · [arXiv:quant-ph/0610132](https://arxiv.org/abs/quant-ph/0610132)

The relation between concurrence-based localization and full LOCC collaboration, including convexity, is relevant to the helper-access score. The direct latent-dimer teleportation proof makes the allowed input-dependent operations explicit.

**[VV03] Frank Verstraete and Henri Verschelde, “Optimal Teleportation with a Mixed State of Two Qubits,” Physical Review Letters 90, 097901 (2003).** [DOI](https://doi.org/10.1103/PhysRevLett.90.097901) · [arXiv:quant-ph/0303007](https://arxiv.org/abs/quant-ph/0303007)

Local filtering with a retained separable failure branch supplies a deterministic teleportation protocol. This successful-filter-plus-classical-fallback construction is an inherited ingredient of the receiver's rare-sector protocol. The new task conclusion depends on the thermal sector weights and their limiting rate.

**[L21] J.-Y. Li, X.-X. Fang, T. Zhang, G. N. M. Tabia, H. Lu and Y.-C. Liang, “Activating hidden teleportation power: Theory and experiment,” Physical Review Research 3, 023045 (2021).** [DOI](https://doi.org/10.1103/PhysRevResearch.3.023045) · [arXiv:2008.01689](https://arxiv.org/abs/2008.01689)

Hidden teleportation power and the tradeoff between filter success and conditional fidelity are established context. The state families inspected there are two-qudit Werner and rank-deficient resources, rather than the collective Gibbs spin distribution.

**[CV07] L. Campos Venuti, C. Degli Esposti Boschi and M. Roncaglia, “Qubit Teleportation and Transfer across Antiferromagnetic Spin Chains,” Physical Review Letters 99, 060401 (2007).** [DOI](https://doi.org/10.1103/PhysRevLett.99.060401) · [arXiv:quant-ph/0703202](https://arxiv.org/abs/quant-ph/0703202)

Thermal spin-chain teleportation and its cooling/size tradeoff are prior results. This construction uses a reduced endpoint resource in finite open chains; the present global-receiver task processes the complete collective thermal state.

## Bell parities and helper cooperation

**[S01] John A. Smolin, “Four-party unlockable bound entangled state,” Physical Review A 63, 032306 (2001).** [DOI](https://doi.org/10.1103/PhysRevA.63.032306) · [arXiv:quant-ph/0001001](https://arxiv.org/abs/quant-ph/0001001)

**[WY07] Guoming Wang and Mingsheng Ying, “Multipartite unlockable bound entanglement in the stabilizer formalism,” Physical Review A 75, 052332 (2007).** [DOI](https://doi.org/10.1103/PhysRevA.75.052332) · [arXiv:quant-ph/0703033](https://arxiv.org/abs/quant-ph/0703033)

These works establish that helper quantum cooperation can unlock entanglement unavailable to fully separated parties. The activation phenomenon and parity mechanism are prior results.

**[B05] J. P. Barjaktarevic, R. H. McKenzie, J. Links and G. J. Milburn, “Measurement-Based Teleportation along Quantum Spin Chains,” Physical Review Letters 95, 230501 (2005).** [DOI](https://doi.org/10.1103/PhysRevLett.95.230501) · [arXiv:quant-ph/0501180](https://arxiv.org/abs/quant-ph/0501180)

This is the direct antecedent for the positive singlet endpoint. It proves unit-fidelity teleportation for states in a Bell subspace and places all total-spin-zero states in one such subspace. Mixtures follow by linearity.

**[G16] Johnnie Gray, Abolfazl Bayat, Reuben K. Puddy, Charles G. Smith and Sougato Bose, “Unravelling quantum dot array simulators via singlet-triplet measurements,” Physical Review B 94, 195136 (2016).** [DOI](https://doi.org/10.1103/PhysRevB.94.195136)

Section V explicitly states that complete Bell measurements on helper pairs always give perfect endpoint entanglement for a spin singlet, with corrections determined by Bell outcomes. The [pair decoder](../science/cooling-and-decoding.md#3-disjoint-helper-bell-measurements), its singlet-support guarantee and its lack of a multiplicity-readout requirement are inherited.

## Equilibrium states and symmetry constraints

**[LT05] Etera R. Livine and Daniel R. Terno, “Entanglement of zero-angular-momentum mixtures and black-hole entropy,” Physical Review A 72, 022307 (2005).** [DOI](https://doi.org/10.1103/PhysRevA.72.022307) · [arXiv:quant-ph/0502043](https://arxiv.org/abs/quant-ph/0502043)

This work computes entanglement of formation and distillation for zero-angular-momentum mixtures across jointly controlled bipartitions. Its representation-theoretic decomposition is part of the source background. It does not impose individually separated helper laboratories.

**[F08] Alessandro Ferraro, Daniel Cavalcanti, Artur García-Saez and Antonio Acín, “Thermal Bound Entanglement in Macroscopic Systems and Area Law,” Physical Review Letters 100, 080502 (2008).** [DOI](https://doi.org/10.1103/PhysRevLett.100.080502)

**[C08] Daniel Cavalcanti, Alessandro Ferraro, Artur García-Saez and Antonio Acín, “Distillable entanglement and area laws in spin and harmonic-oscillator systems,” Physical Review A 78, 012335 (2008).** [DOI](https://doi.org/10.1103/PhysRevA.78.012335) · [arXiv:0705.3762](https://arxiv.org/abs/0705.3762)

Natural thermal states can contain entanglement inaccessible to fully local distillation; that qualitative distinction is established. These works use bipartition negativities and area-law arguments for oscillator systems and finite spin chains. The present account resolves a quantitative physical-qubit teleportation task in a different collective model, with its temperature normalization explicit.

**[M24] Amin Moharramipour, Leonardo A. Lessa, Chong Wang, Timothy H. Hsieh and Subhayan Sahu, “Symmetry-Enforced Entanglement in Maximally Mixed States,” PRX Quantum 5, 040336 (2024).** [DOI](https://doi.org/10.1103/PRXQuantum.5.040336) · [arXiv:2406.08542](https://arxiv.org/abs/2406.08542)

This work gives exact collective-bipartition entanglement measures for maximally mixed invariant sectors and the logarithmic entanglement of non-Abelian singlet ensembles. The underlying mixed singlet source and collective-irrep distillation are prior material.

**[N26] Amir-Reza Negari, Leonardo A. Lessa and Subhayan Sahu, “Symmetry enforces entanglement at high temperatures,” Physical Review A 114, 022458 (2026).** [DOI](https://doi.org/10.1103/rckt-3lfm) · [arXiv:2508.20166v3](https://arxiv.org/abs/2508.20166v3)

The paper treats strong Abelian canonical constraints and superselection-restricted Gibbs entanglement. The state here is the ordinary, unprojected Gibbs state of $`\mathbf J^2`$, and the operational score uses ordinary qubit teleportation.

**[MAG26] Siqi Mo, Ehud Altman and Samuel J. Garratt, “Thermal entanglement transitions from strong SU(2) symmetry,” arXiv:2610.00826v1 (2026).** [Primary preprint](https://arxiv.org/abs/2610.00826v1)

Its singlet-projected Gibbs states of local ferromagnets are strongly SU(2) symmetric, with entanglement across macroscopic cuts. Sections II–III make those state and cut assumptions explicit. Here thermal population of nonzero total-spin sectors is essential, and the sender cut contains one physical qubit.

## Relation to unconditional particle access

[**Singlet Access Limits**](https://github.com/GoGoKo699/Singlet-Access-Limits) studies unconditional particle discard from the uniform singlet ensemble. Its [access-law derivation](https://github.com/GoGoKo699/Singlet-Access-Limits/blob/9be80f53618e860169a7c801fd087c08f8a6138b/research/ACCESS_LAW.md) gives an exact retained-particle distillability boundary and explicitly includes the dimer decomposition. Its [near-full-access result](https://github.com/GoGoKo699/Singlet-Access-Limits/blob/9be80f53618e860169a7c801fd087c08f8a6138b/research/NEAR_FULL_ACCESS.md) bounds the amount of collective entanglement after loss.

Those results retain no discarded records and grant joint quantum control within each retained side. The present helper-access task keeps measurement records, fixes a physical target pair and varies which helper parties can cooperate. The thermal task additionally populates nonzero-spin sectors. These operational differences are stated before applying any inherited identity.

## What this account adds

| Established ingredient | Its role here | Consequential conclusion developed here |
|---|---|---|
| Collective-spin thermal spectrum and qubit–spin partial transpose | Identify which receiver sectors can contribute negativity | Finite uniform suppression and the sharp ordered rare-spin rate |
| Negativity and teleportation benchmarks | Bound every allowed deterministic protocol | A useful-fidelity cooling necessity, matched in order by an explicit decoder |
| Bell-subspace singlet teleportation | Supply the positive decoding endpoint | Exact thermal output, finite performance guarantees and controlled temperature scaling |
| Dimer mixtures and LOCC convexity | Bound fully separated helper strategies | Physical-target helper-access and fixed-coalition participation laws |

The source comparison is bounded by the versions and sections recorded in [source evidence](source-evidence.md). The claims do not require treating the prior positive protocol, the entanglement witness, the spectrum or the abstract phenomenon of unlocking as new.

---

[Scientific model](../science/model.md) · [Cooling and decoding](../science/cooling-and-decoding.md) · [Source evidence](source-evidence.md)

