# The project's 30-milestone understanding map

A supplied collective antiferromagnet can contain entanglement without providing a fixed teleportation advantage. Understanding that distinction requires both a communication task and the spin-sector structure of its source. The map below connects those ingredients to the cooling law, the rare-sector rate, and the limits imposed by separated helpers.

The selected educational anchor is John Watrous, [*The Theory of Quantum Information* (Cambridge University Press, 2018)][W]. Section numbers below were checked against the author's [official contents][WTOC]. The linked chapter files are the author-hosted January 2018 prepublication manuscript. They supply quantum-information foundations; the project supplies the collective-spin, thermal, and operational bridge. Primary research references identify inherited results and proof ingredients rather than additional educational anchors.

| Phase | Milestones | Allocation and direction |
|---|---|---|
| Background/preliminaries | M01–M12 | Twelve milestones connect individual states, outcomes, and channels to laboratory partitions and the collective thermal source. Both the quantum-information language and the spin bridge are needed before the project's claims can be interpreted. M12 integrates them into the complete task. |
| Narrative/innovation | M13–M30 | Eighteen milestones follow local invariant blocks into finite-source bounds, the fixed-score cooling law, the rare-sector operational rate, and the helper-access comparison. These are distinct arguments with different control and limit assumptions. M30 connects their conclusions and boundaries. |

The milestones are understanding targets, not thirty expanded tutorial chapters or an exhaustive list of lemmas. Dependencies refer to earlier milestones. Canonical statements and proofs remain in [science](../science/README.md); the final targets require connecting them rather than treating their formulas as independent facts.

## Background/preliminaries

### M01: Background/preliminaries · The input and the resource

- **Central question:** Which qubits carry the message, and which are supplied to help transmit it?
- **Understanding target:** Distinguish the independent unknown input from the source spins, and identify the fixed physical sender and receiver.
- **Dependencies and story role:** Entry point. It gives the task's individual systems before introducing their joint state or the collective Hamiltonian.
- **Conceptual connection:** A register's physical role matters separately from its two-dimensional Hilbert space; the input arrives after the resource has been supplied.
- **Source pointers:** Watrous §2.1, [registers and states][W2]; [communication task](../science/model.md#communication-task).

### M02: Background/preliminaries · A mixed state and its missing record

- **Central question:** What changes when a state has a useful ensemble decomposition but its preparation label is unavailable?
- **Understanding target:** Separate a density operator from an ensemble record or purification, and recognize that different decompositions describe the same supplied resource.
- **Dependencies and story role:** M01. This establishes the distinction later needed for hidden singlet matchings and unobserved thermal sectors.
- **Conceptual connection:** A proof may average over pure resources without granting the protocol knowledge of which resource occurred.
- **Source pointers:** Watrous §§2.1.2–2.1.3, [states, reductions, and purifications][W2]; [source specification](../science/model.md#source-and-normalization).

### M03: Background/preliminaries · Outcomes belong in the score

- **Central question:** How does a probabilistic measurement become part of a complete communication protocol?
- **Understanding target:** Distinguish a conditional output state from its probability-weighted contribution, including failed filters and classical fallback.
- **Dependencies and story role:** M01–M02. It makes outcome accounting explicit before any teleportation or filtering construction.
- **Conceptual connection:** A successful branch can be excellent while the trace-preserving channel has only a small average advantage.
- **Source pointers:** Watrous §§2.2–2.3, [channels and measurements][W2]; [all-outcome fidelity](../science/model.md#communication-task); [middle-level projection](../science/teleportation-bounds.md#middle-level-projection).

### M04: Background/preliminaries · Bell transmission and the classical baseline

- **Central question:** What makes a teleportation score a quantum advantage?
- **Understanding target:** Relate a Bell resource and its classical correction record to qubit transmission, and distinguish perfect transmission from an excess above the Haar-average classical value $`2/3`$.
- **Dependencies and story role:** M01–M03. It introduces the operational comparison used throughout the research account.
- **Conceptual connection:** The relevant target is an unconditional channel score, not the mere production of an entangled pair in one branch.
- **Source pointers:** Watrous §6.3.1, [teleportation][W6], and §7.2.1, [Haar measure][W7]; [task and fixed advantage](../science/model.md#communication-task).

### M05: Background/preliminaries · The channel seen through a reference

- **Central question:** How can the whole protocol be represented by one bipartite output state?
- **Understanding target:** Connect a trace-preserving channel to its normalized Choi state, entanglement fidelity, and Haar-average qubit fidelity, keeping their normalizations distinct.
- **Dependencies and story role:** M03–M04. This is the language needed for a converse that includes input-dependent adaptation.
- **Conceptual connection:** A reference qubit converts the transmission problem into an entanglement constraint across the physical sender cut.
- **Source pointers:** Watrous §2.2.2, [channel representations][W2], and §3.2, [state fidelity][W3]; the project's [complete-protocol upper-bound proof](../science/teleportation-bounds.md#a-universal-upper-bound-from-the-source-cut).

### M06: Background/preliminaries · Laboratories define LOCC

- **Central question:** Which joint operations are allowed when the same spins are divided among different laboratories?
- **Understanding target:** Distinguish singleton access, fixed paired helpers, and the global receiver benchmark; explain why grouping laboratories preserves upper bounds but can invalidate a proposed lower construction.
- **Dependencies and story role:** M01–M05. It moves from individual registers to the operational partition of the whole source.
- **Conceptual connection:** Entanglement and allowed processing are defined relative to a cut. In the global benchmark the receiver owns every source spin except the sender's spin, including the physical output.
- **Source pointers:** Watrous §6.1.2, [LOCC][W6]; [access models](../science/model.md#access-models).

### M07: Background/preliminaries · Presence and amount of entanglement

- **Central question:** What does a negative partial transpose establish, and what additional information does negativity retain?
- **Understanding target:** Distinguish the PPT/NPT sign test from the trace-norm quantity $`\nu=(\lVert\rho^{T_A}\rVert_1-1)/2`$, and understand why an entanglement monotone can constrain a complete channel.
- **Dependencies and story role:** M02, M05–M06. It introduces the quantitative bridge between a supplied state and the communication score.
- **Conceptual connection:** An arbitrarily small negative contribution can certify entanglement without guaranteeing an advantage bounded away from zero.
- **Source pointers:** Watrous §6.2.3, [partial transposition][W6], and §1.1.3, [operator norms][W1]; [project negativity and score bound](../science/teleportation-bounds.md#a-universal-upper-bound-from-the-source-cut).

### M08: Background/preliminaries · One qubit coupled to a collective spin

- **Central question:** Why does separating one physical spin leave only two coupled-spin sectors inside each rest-spin block?
- **Understanding target:** Identify the sender's spin one half, the rest spin $`j`$, the dimension $`x=2j+1`$, and the total spins $`j\pm1/2`$ with their different ranks.
- **Dependencies and story role:** M01–M02, M07. This is the first project-specific spin bridge and the local object used in the thermal proofs.
- **Conceptual connection:** Collective symmetry reduces a many-qubit cut to a family of invariant qubit–spin operators without replacing the physical sender by a macroscopic subsystem.
- **Source pointers:** [Invariant block and its partial transpose](../science/thermal-spectrum.md#the-invariant-block-and-its-partial-transpose), including its Schliemann attribution; [flagged blocks](../science/teleportation-bounds.md#locally-flagged-qubitspin-blocks).

### M09: Background/preliminaries · Symmetry, sectors, and multiplicity

- **Central question:** What information survives when a state is invariant under both site permutations and collective rotations?
- **Understanding target:** Distinguish an irrep's spin dimension from its multiplicity, and relate the two invariances to mixtures of normalized total-spin projectors.
- **Dependencies and story role:** M02, M08. It assembles local coupled-spin blocks into the symmetry structure of the complete source.
- **Conceptual connection:** The project's spin multiplicities specialize the operator-algebra perspective of permutation invariance; neither invariance alone gives the later singleton ceiling.
- **Source pointers:** Watrous §7.1.2, [permutation-invariant operators][W7]; [source multiplicities](../science/thermal-spectrum.md#model-and-conventions); [two-symmetry ceiling](../science/helper-access.md#a-universal-permutation-and-rotation-ceiling).

### M10: Background/preliminaries · Temperature with the physical normalization attached

- **Central question:** Which parameter determines the thermal weights when the interaction strength per spin is kept of order $`g`$?
- **Understanding target:** Connect $`H_N=g\mathbf J^2/N`$, the gap $`2g/N`$, the Gibbs weights, and $`b=g/(Nk_{\mathrm B}T)`$; distinguish fixed $`b`$ from fixed physical temperature.
- **Dependencies and story role:** M08–M09. This connects the collective spectrum to the experimentally meaningful temperature scale.
- **Conceptual connection:** A dimensionless thermal statement acquires its size dependence only after the Hamiltonian normalization is restored.
- **Source pointers:** [Source and normalization](../science/model.md#source-and-normalization); [thermal multiplicities and partition function](../science/thermal-spectrum.md#model-and-conventions).

### M11: Background/preliminaries · Flags, weights, and complete ensembles

- **Central question:** When can blockwise quantities be combined into a statement about the supplied state?
- **Understanding target:** Distinguish receiver-local orthogonal spin flags, unobserved pure-state decompositions, and ordinary measurement outcomes; account for the weights of every contributing block.
- **Dependencies and story role:** M02–M03, M06–M10. It joins symmetry bookkeeping to the all-outcome operational framework.
- **Conceptual connection:** Negativity adds over orthogonal local flags, while a hidden matching supplies a convex converse. These are different reasons for averaging and grant different protocol information.
- **Source pointers:** Watrous §§1.2.1–1.2.2, [convexity and probability][W1]; [block probabilities](../science/thermal-spectrum.md#the-invariant-block-and-its-partial-transpose); [hidden-matching converse](../science/helper-access.md#a-hidden-matching-gives-a-protocol-wide-converse).

### M12: Background/preliminaries · The complete comparison

- **Central question:** What must be specified before asking whether this thermal source is useful?
- **Understanding target:** Integrate the supplied state, late unknown input, fixed targets, laboratory partition, common frame, unconditional fidelity, and limit parameters into one task; distinguish entanglement presence, fixed score, and accessible score.
- **Dependencies and story role:** M01–M11. This closes the background phase by connecting its individual objects to the full problem.
- **Conceptual connection:** The same state can answer these three questions differently because a spectral sign, a probability-weighted channel, and a control restriction encode different information.
- **Source pointers:** [Model](../science/model.md); [scientific route](../science/README.md); [operational interpretation](../science/interpretation.md).

## Narrative/innovation

### M13: Narrative/innovation · The entangled invariant block

- **Central question:** Which part of a thermal qubit–spin block can acquire a negative partial transpose?
- **Understanding target:** Relate $`a_xP_-+c_xP_+`$ to its partial-transpose eigenvalues and their degeneracies, obtaining the condition $`bx>\ln(x+1)`$ and the normalized block negativity.
- **Dependencies and story role:** M07–M12. The narrative begins with one local block, whose exact criterion drives both temperature arguments.
- **Conceptual connection:** An inherited invariant-spin spectrum becomes a thermal criterion only after the actual lower- and upper-spin Gibbs weights are inserted.
- **Source pointers:** [Invariant block derivation](../science/thermal-spectrum.md#the-invariant-block-and-its-partial-transpose); [primary-source evidence](../references/source-evidence.md#load-bearing-primary-sources).

### M14: Narrative/innovation · First entanglement in the finite source

- **Central question:** Which allowed block determines the first appearance of entanglement across one physical spin?
- **Understanding target:** Explain why the extremal allowed value $`x=N`$ gives the exact boundary $`b=\ln(N+1)/N`$, including PPT at equality and the family-specific implication from PPT to separability.
- **Dependencies and story role:** M09–M10, M13. It assembles the local criterion into a statement about the whole finite source.
- **Conceptual connection:** The first contributing sector need not be typical or probable. This boundary concerns one-spin-cut entanglement, not full separability of all physical spins.
- **Source pointers:** [Exact NPT onset and separable twirls](../science/thermal-spectrum.md#exact-onset-of-a-negative-partial-transpose).

### M15: Narrative/innovation · A bound for every complete protocol

- **Central question:** Why can an ingenious receiver decoder not turn a vanishing block-negativity bound into a fixed score?
- **Understanding target:** Combine $`\nu_j\le1/x`$ with the NPT condition to obtain $`\nu_N\le b/\ln3`$, then connect source negativity to $`F_N^{\mathrm{glob}}-2/3\le2\nu_N/3`$ through the channel Choi state.
- **Dependencies and story role:** M05–M07, M11, M13. It turns local spectral information into a protocol-wide converse.
- **Conceptual connection:** The input-reference construction includes adaptation after input arrival; the bound also covers every more separated laboratory model.
- **Source pointers:** [Uniform negativity bound](../science/thermal-spectrum.md#a-uniform-bound-on-the-amount); [complete-protocol proof](../science/teleportation-bounds.md#a-universal-upper-bound-from-the-source-cut).

### M16: Narrative/innovation · A useful qubit inside each NPT block

- **Central question:** Can the entanglement detected in a large rest-spin block produce an explicit all-outcome teleportation advantage?
- **Understanding target:** Follow the receiver projection onto $`m=\pm1/2`$, its success probability $`2/x`$, and its Bell-diagonal output; relate the unconditional block excess to $`2\nu_j/[3(x-1)]`$.
- **Dependencies and story role:** M03–M08, M13. It supplies a constructive local counterpart to the preceding converse.
- **Conceptual connection:** Two retained magnetic levels lose a polynomial factor rather than requiring the whole block to be an effective Bell pair. Failure uses classical transmission.
- **Source pointers:** [Middle-level projection](../science/teleportation-bounds.md#middle-level-projection); [global receiver permissions](../science/model.md#access-models).

### M17: Narrative/innovation · The finite operational sandwich

- **Central question:** How much can be concluded about optimal teleportation without finding its exact decoder?
- **Understanding target:** Combine the probability-weighted explicit decoder sum with the negativity converse, distinguishing an achievable score, an optimal score, and an upper bound.
- **Dependencies and story role:** M11, M15–M16. It assembles local constructions into a rigorous finite-source operational comparison.
- **Conceptual connection:** The sandwich proves positive global-receiver excess at every NPT point while retaining the block-dependent loss needed for the sharper asymptotic result.
- **Source pointers:** [Finite operational sandwich](../science/teleportation-bounds.md#finite-operational-sandwich); [finite quantities for the rate proof](../science/rare-sectors.md#definitions-and-the-finite-operational-comparison).

### M18: Narrative/innovation · The established Bell-parity decoder

- **Central question:** How do disjoint helper-pair measurements exploit the singlet constraint, and what remains at finite temperature?
- **Understanding target:** Connect global Pauli parities to complete helper Bell measurements, target correction, and the thermal Werner visibility $`R_N(b)`$ expressed through spin characters.
- **Dependencies and story role:** M04, M06, M09–M12. It introduces the weaker-access construction used to match the cooling order.
- **Conceptual connection:** The perfect singlet endpoint is inherited from Barjaktarevic et al. (2005), with the helper formulation explicit in Gray et al. (2016). Full Bell resolution and a common frame are supplied control resources.
- **Source pointers:** [Disjoint helper Bell measurements](../science/cooling-and-decoding.md#3-disjoint-helper-bell-measurements); [decoder antecedents](../references/source-evidence.md#positive-decoder-and-helper-access-antecedents).

### M19: Narrative/innovation · Uniform performance, rather than a large-size guess

- **Central question:** Why does a fixed value of $`b`$ suffice for a fixed score at every even size?
- **Understanding target:** Use the multiplicity-ratio bound to control all excited sectors uniformly, distinguish the certified $`F>0.8939`$ guarantee at $`b\ge2`$ from a rotor-series decimal, and connect sufficiently large constant $`b_\delta`$ to any fixed $`0\lt \delta\lt 1/3`$.
- **Dependencies and story role:** M10–M11, M18. It upgrades a known zero-temperature endpoint into a finite-temperature sufficiency statement.
- **Conceptual connection:** Uniform bounds on the full ensemble justify an arbitrary-size operating point; an asymptotic numerical value alone would not.
- **Source pointers:** [Finite uniform guarantee](../science/cooling-and-decoding.md#4-a-finite-uniform-performance-guarantee); [every fixed excess](../science/cooling-and-decoding.md#5-every-fixed-fidelity-excess-has-the-same-cooling-order).

### M20: Narrative/innovation · Presence and a fixed score require different cooling

- **Central question:** How do the converse and construction locate the physically useful temperature order?
- **Understanding target:** Connect the necessary global-receiver bound and sufficient paired-helper protocol to $`T=\Theta_\delta(g/[Nk_{\mathrm B}])`$, and compare this with the exact entanglement-presence temperature $`g/[k_{\mathrm B}\ln(N+1)]`$.
- **Dependencies and story role:** M14–M15, M18–M19. This integrates the finite-temperature argument before asking how a tiny remaining advantage behaves.
- **Conceptual connection:** The conclusion concerns a prescribed size-independent excess and optimal order in $`N`$, not an exact finite-size fidelity threshold or optimized constants.
- **Source pointers:** [Fixed-score cooling order](../science/cooling-and-decoding.md#5-every-fixed-fidelity-excess-has-the-same-cooling-order); [finite physical comparison](../science/interpretation.md#a-finite-comparison).

### M21: Narrative/innovation · From multiplicities to limiting thermal series

- **Central question:** What survives the large-even-size limit when $`b>0`$ is held fixed?
- **Understanding target:** Relate the exact multiplicity products to their fixed-spin limits, the summable dominating bounds, and the limiting partition series $`S(b)`$; explain why $`S(b)\sim\sqrt\pi b^{-3/2}`$ has only polynomial small-$`b`$ growth.
- **Dependencies and story role:** M09–M11, M17. It supplies the controlled whole-source limit used in the rare-sector analysis.
- **Conceptual connection:** Taking a limit term by term requires a uniform summable bound. Fixed $`b`$ already means physical temperature proportional to $`1/N`$.
- **Source pointers:** [Multiplicity ratios](../science/thermal-spectrum.md#multiplicity-ratios-used-in-the-limiting-arguments); [ordered source limit](../science/rare-sectors.md#the-ordered-limit-for-source-negativity).

### M22: Narrative/innovation · Why the contributing sector is rare

- **Central question:** How far above the typical spin must a small-$`b`$ sector lie before it can be NPT?
- **Understanding target:** Contrast typical spin of order $`b^{-1/2}`$ with the first contributing dimension of order $`\ln(1/b)/b`$, and connect this tail restriction to the explicit finite bound with exponent coefficient $`1/8`$.
- **Dependencies and story role:** M13, M17, M21. It identifies the suppression mechanism before sharpening its coefficient.
- **Conceptual connection:** The thermal Gaussian tail and the block-entanglement condition select different spin scales. The finite conservative bound is not the sharp limiting law.
- **Source pointers:** [Uniform finite tail bound](../science/rare-sectors.md#an-explicit-uniform-finite-bound); [mechanism in physical terms](../science/interpretation.md#what-causes-the-rare-sector-law).

### M23: Narrative/innovation · The sharp source logarithmic rate

- **Central question:** Which part of the rare tail fixes the coefficient $`-1/4`$?
- **Understanding target:** Connect a Gaussian-tail upper bound to a single allowed even spin just beyond $`\ln(1/b)/b`$, and identify why polynomial factors disappear when the logarithm is scaled by $`b/\ln^2(1/b)`$.
- **Dependencies and story role:** M21–M22. It upgrades the mechanism to matching upper and lower estimates for limiting source negativity.
- **Conceptual connection:** The result specifies a leading logarithmic rate after large size, not an exact asymptotic prefactor or a uniform formula at the finite NPT edge.
- **Source pointers:** [Sharp logarithmic rate and proof](../science/rare-sectors.md#sharp-logarithmic-rate).

### M24: Narrative/innovation · The same rate for an optimal channel

- **Central question:** Why does source entanglement suppression also describe the best global-receiver teleportation excess?
- **Understanding target:** Use the explicit block decoder's polynomial loss and the finite sandwich to connect the decoder limit to both the lower and upper large-size envelopes of the optimal excess.
- **Dependencies and story role:** M16–M17, M21–M23. It turns the source-rate statement into an operational conclusion.
- **Conceptual connection:** Matching envelope rates establish $`-1/4`$ without asserting a fixed-$`b`$ limit of the optimal fidelity. The constructive lower bound requires the global receiver laboratory.
- **Source pointers:** [Optimal-excess rate](../science/rare-sectors.md#the-same-rate-for-optimal-teleportation-excess); [ordered operational sandwich](../science/teleportation-bounds.md#ordered-rare-sector-rate).

### M25: Narrative/innovation · Limits with their physical regime retained

- **Central question:** When can system size and $`b\downarrow0`$ vary together without losing the rare-sector conclusion?
- **Understanding target:** Connect the sufficient condition $`Nb_N^2/\ln^2(1/b_N)\to\infty`$ to uniform multiplicity control at the selected rare spin; distinguish this joint theorem from the ordered theorem and from fixed positive physical temperature.
- **Dependencies and story role:** M10, M21–M24. It completes the rare-sector argument by locating its valid finite-size regime.
- **Conceptual connection:** A fixed-spin multiplicity limit cannot be applied automatically to a spin that grows with temperature. The theorem requires that growing spin to remain within its controlled range.
- **Source pointers:** [Controlled simultaneous regime](../science/rare-sectors.md#a-controlled-simultaneous-finite-size-regime); [parameter limits](../science/model.md#parameter-limits).

### M26: Narrative/innovation · The singlet mixture as a hidden matching

- **Central question:** What can a valence-bond resolution reveal about access without revealing a matching to the parties?
- **Understanding target:** Relate the maximally mixed singlet to the uniform ensemble of perfect singlet matchings, and distinguish a useful proof decomposition from an available classical record.
- **Dependencies and story role:** M02, M06, M09, M11–M12. It introduces the local combinatorial object behind the separated-helper converse.
- **Conceptual connection:** Entanglement across the physical sender cut does not specify which individual laboratories can act jointly along the hidden matching.
- **Source pointers:** [Hidden-matching resolution and converse](../science/helper-access.md#a-hidden-matching-gives-a-protocol-wide-converse); [helper-access antecedents](../references/source-evidence.md#positive-decoder-and-helper-access-antecedents).

### M27: Narrative/innovation · A singleton converse for the whole task

- **Central question:** Why can arbitrary singleton adaptation not outperform the direct-target matching probability?
- **Understanding target:** For each matching without an $`AB`$ dimer, identify a product cut that is a union of allowed laboratories; then connect its entanglement-breaking channel bound and source linearity to $`F_N^{\mathrm{single}}(0)\le2/3+1/[3(N-1)]`$.
- **Dependencies and story role:** M03–M06, M26. It extends a matching observation into a complete-protocol upper bound.
- **Conceptual connection:** The argument includes the late unknown input and is stronger in scope than bounding a chosen helper measurement or a prior Bell-pair-localization stage.
- **Source pointers:** [Protocol-wide singleton converse](../science/helper-access.md#a-hidden-matching-gives-a-protocol-wide-converse).

### M28: Narrative/innovation · Sharpness and the two-symmetry ceiling

- **Central question:** Is the singleton bound attainable, and how much of it survives beyond the zero-temperature source?
- **Understanding target:** Combine balanced common-axis helper outcomes and classical fallback to attain the exact singleton score; connect sector twirling to the universal ceiling for states invariant under both permutations and collective rotations.
- **Dependencies and story role:** M03, M09, M26–M27. It places the exact singlet answer inside a larger physical symmetry class.
- **Conceptual connection:** Both symmetries are necessary to the stated universal class. Cooling alone never yields a size-independent singleton advantage for this thermal family.
- **Source pointers:** [Common-axis attainment](../science/helper-access.md#common-axis-helper-measurements-attain-the-bound); [universal two-symmetry ceiling and counterexamples](../science/helper-access.md#a-universal-permutation-and-rotation-ceiling).

### M29: Narrative/innovation · A fixed pair partition and its boundary

- **Central question:** How much quantum-capable helper pairing is necessary for a fixed singlet-source advantage?
- **Understanding target:** Connect alternating paths in a hidden matching plus $`k`$ fixed disjoint helper pairs to the upper bound $`F_{N,k}-2/3\le1/[3(N-2k-1)]`$ and the requirement that all but a bounded number of helpers be paired.
- **Dependencies and story role:** M06, M18, M26–M28. It joins the singleton limit to the established perfect paired-helper endpoint through a quantitative converse.
- **Conceptual connection:** The bound concerns a partition fixed before observations. Tight endpoints do not imply intermediate optimality, an adaptive-partner theorem, or a general two-qubit-gate budget law.
- **Source pointers:** [Fixed disjoint-pair budget converse](../science/helper-access.md#a-fixed-disjoint-pair-budget-converse); [known paired-helper endpoint](../science/helper-access.md#the-known-paired-helper-endpoint).

### M30: Narrative/innovation · Temperature, rarity, and cooperation in one account

- **Central question:** What does the combined result establish about extracting communication from a supplied thermal many-body state?
- **Understanding target:** Connect exact entanglement onset, fixed-score cooling, the global-receiver rare-sector rate, and the singleton/pair access comparison while retaining their different quantifiers, laboratory permissions, and limits.
- **Dependencies and story role:** M12–M29, particularly M20, M24–M25, and M28–M29. This closes the narrative by integrating its three arguments into the project's scientific contribution.
- **Conceptual connection:** The inherited Gibbs family, invariant-spin spectrum, and positive Bell decoder support new operational comparisons. Finite verification checks instances of the derivations; supplied equilibrium states and ideal controls do not establish preparation time, refrigeration work, or hardware advantage.
- **Source pointers:** [Interpretation](../science/interpretation.md); [attribution and comparison scope](../references/related-work.md); [verification boundaries](../verification/README.md); [model and supplied controls](../science/model.md#supplied-controls-and-charged-boundaries).

[W]: https://cs.uwaterloo.ca/~watrous/TQI/
[WTOC]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf
[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W6]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf
[W7]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf
