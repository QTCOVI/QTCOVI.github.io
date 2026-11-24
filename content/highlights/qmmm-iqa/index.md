---
title: "Bringing quantum atoms into proteins: IQA meets QM/MM"
summary: >
  Combining IQA with QM/MM and continuum solvation gives residue-by-residue energy terms for every
  covalent and noncovalent interaction in a biomolecule, illustrated on metal hydration and inhibitor
  binding to the MMP-12 enzyme. *J. Chem. Inf. Model.* 2022.
tags:
  - IQA
  - QM/MM
  - Biomolecules
  - Drug design
date: 2022-02-25
image:
  caption: 'MMP-12 with a hydroxamate inhibitor in its S1′ pocket. López et al., J. Chem. Inf. Model. 62, 1510 (2022), CC BY 4.0.'
  focal_point: Center
---

> R. López, N. Díaz, E. Francisco, Á. Martín Pendás, D. Suárez,
> *QM/MM Energy Decomposition Using the Interacting Quantum Atoms Approach*,
> **Journal of Chemical Information and Modeling** 62, 1510–1524 (2022).
> [doi:10.1021/acs.jcim.1c01372](https://doi.org/10.1021/acs.jcim.1c01372) · open access

## The problem

Hybrid quantum mechanics/molecular mechanics (QM/MM) is the workhorse for modelling enzymes and drug binding: a small
active region is treated quantum mechanically and the rest of the protein with a classical force field. QM/MM gives
accurate energies, but not a breakdown of *which* residues and interactions are responsible for them. Energy
decompositions that do exist rarely treat the quantum and classical regions on an equal footing.

## What we did

We extended the Interacting Quantum Atoms partition to QM/MM, together with molecular mechanics and
Poisson–Boltzmann surface-area (PBSA) solvation. The result is a consistent set of intra- and inter-residue energy
terms for all kinds of covalent and noncovalent interactions across the QM/MM boundary.

{{< figure src="water-shells.jpg" caption="Moving the second hydration shell of Mg(II) and Zn(II) from the MM to the QM region, and the effect on the metal–water electrostatic interaction. López et al., J. Chem. Inf. Model. 2022, CC BY 4.0." >}}

We tested the approach on Zn(II) and Mg(II) water clusters with QM regions of growing size, to characterize metal–water
interactions and boundary artifacts. We then applied it to a homologous series of inhibitors bound to matrix
metalloproteinase-12 (MMP-12), a drug target, starting from their crystal structures.

## Why it matters

- **Residue-level insight with quantum accuracy.** IQA QM/MM shows which contacts drive inhibitor binding, which
  helps rational drug design.
- **Boundary artifacts made visible.** The descriptors show how the size of the QM region affects the description,
  a long-standing practical problem in QM/MM.
- **A bridge between our methods and our biomolecular work**, joining the group's expertise in real-space chemical
  bonding and in biomolecular simulation.

**Related:** [IQA research line](/research/interacting-quantum-atoms/) ·
[Publication page](/publication/2022-qm-mm-energy-decomposition-using-the-interacting-quantum-atoms-approach/)
