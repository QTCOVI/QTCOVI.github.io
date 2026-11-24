---
title: "Interacting Quantum Atoms: an energy decomposition born in Oviedo"
summary: >
  IQA splits the energy of a molecule into atomic self-energies and pairwise interactions, with no
  reference states and no orbital choices. Developed in our group, it is now used by research groups
  around the world. *Molecules* 2020 review.
tags:
  - IQA
  - Energy decomposition
  - Chemical bonding
date: 2020-09-03
image:
  caption: 'Biphenyl as non-overlapping topological atoms. Guevara-Vela et al., Molecules 25, 4028 (2020), CC BY 4.0.'
  focal_point: Center
---

> J. M. Guevara-Vela, E. Francisco, T. Rocha-Rinza, Á. Martín Pendás,
> *Interacting Quantum Atoms—A Review*,
> **Molecules** 25, 4028 (2020). [doi:10.3390/molecules25174028](https://doi.org/10.3390/molecules25174028) · open access
>
> Original method: M. A. Blanco, Á. Martín Pendás, E. Francisco, *J. Chem. Theory Comput.* 1, 1096 (2005).
> [doi:10.1021/ct0501093](https://doi.org/10.1021/ct0501093)

## The problem

Chemists explain molecules in terms of atoms and the interactions between them: steric repulsion, electrostatics,
covalency, hydrogen bonds. Quantum mechanics, however, gives a single total energy for the whole molecule.
Most energy decomposition schemes split it by comparing the molecule with chosen reference fragments, so the answer
depends on that choice and the terms can be hard to interpret.

## What we did

In 2005 our group introduced **Interacting Quantum Atoms (IQA)**. Building on the atoms defined by the topology of
the electron density (QTAIM), IQA writes the exact molecular energy as a sum of intra-atomic self-energies plus
pairwise interaction energies. Each interaction splits further into a classical electrostatic part and an
exchange–correlation part, the real-space signature of covalency.

{{< figure src="featured.jpg" caption="Biphenyl drawn as a chemist sees it (left) and as IQA sees it (right): non-overlapping topological atoms bounded by interatomic surfaces. Guevara-Vela et al., Molecules 2020, CC BY 4.0." >}}

The 2020 review, one of the group's most cited recent papers, gives a self-contained introduction to the method, covers its
extensions (correlated wavefunctions, DFT, QM/MM, machine learning) and surveys how groups worldwide have used it.

## Why it matters

- **Orbital-invariant and reference-free.** The same partition works for any wavefunction and any molecule.
- **Classic chemical concepts made quantitative**: steric effects, hydrogen-bond cooperativity, halogen bonds,
  metal–ligand bonding, reaction mechanisms.
- **A foundation for new work.** IQA underlies much of our later research, including [collective
  bonds](/highlights/collective-interactions/), [QM/MM energy
  decomposition](/highlights/qmmm-iqa/) and [machine-learned real-space
  descriptors](/highlights/explainable-chemical-ai/).
- **Widely adopted.** The original 2005 paper alone has more than 900 citations, and the review over 150.

**Related:** [IQA research line](/research/interacting-quantum-atoms/) ·
[Review publication page](/publication/2020-interacting-quantum-atoms-a-review/) ·
[Original 2005 paper](/publication/2005-interacting-quantum-atoms-a-correlated-energy-decomposition-scheme-based-on-the-/)
