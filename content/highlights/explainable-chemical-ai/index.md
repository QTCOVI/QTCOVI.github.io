---
title: "Explainable chemical AI: machine learning that speaks the language of chemists"
summary: >
  SchNet4AIM learns rigorous real-space descriptors (atomic charges, delocalization indices,
  interaction energies) and predicts them in milliseconds, so machine-learned chemistry can be
  accurate and interpretable at the same time. *Nature Communications* 2024.
tags:
  - Machine learning
  - Explainable AI
  - QTAIM
  - IQA
date: 2024-05-21
image:
  caption: 'Architecture of SchNet4AIM. Gallegos et al., Nat. Commun. 15, 4345 (2024), CC BY 4.0.'
  focal_point: Center
---

> M. Gallegos, V. Vassilev-Galindo, I. Poltavsky, Á. Martín Pendás, A. Tkatchenko,
> *Explainable chemical artificial intelligence from accurate machine learning of real-space chemical descriptors*,
> **Nature Communications** 15, 4345 (2024). [doi:10.1038/s41467-024-48567-9](https://doi.org/10.1038/s41467-024-48567-9) · open access

## The problem

Machine learning has made computational chemistry very fast. Neural networks now predict energies and forces
with near-quantum accuracy at a tiny fraction of the cost. The price is that the predictions come out of a black box:
the network tells you *what* the energy is, but not *why*. Generic explainable-AI tools help only partly,
because what they explain depends on the network architecture and the training data.

Real-space descriptors from the Quantum Theory of Atoms in Molecules (QTAIM) and Interacting Quantum Atoms (IQA)
have the opposite profile. Atomic charges, delocalization indices and pairwise interaction energies are physically
rigorous and chemically meaningful, but they need expensive six-dimensional integrations. Until now that cost kept
them out of molecular dynamics and large systems.

## What we did

Together with Alexandre Tkatchenko's group (University of Luxembourg) we built **SchNet4AIM**, a SchNet-based
deep neural network that predicts both one-body (atomic) and two-body (interatomic) real-space quantities.
Interatomic predictions are handled natively by building pair environment tensors from the atomic ones.

{{< figure src="cycloaddition.jpg" caption="SchNet4AIM tracks charge transfer and the onset of new bonds (delocalization indices δ) along a 1,3-dipolar cycloaddition, a geometry far from its training data. Gallegos et al., Nat. Commun. 2024, CC BY 4.0." >}}

The model reproduces QTAIM charges, delocalization indices and IQA interaction energies with chemical accuracy, and it
keeps working in extrapolation regimes such as reaction paths it was never trained on.

{{< figure src="co2-cage.jpg" caption="Real-space descriptors along molecular dynamics: CO₂ trapped in and released from a molecular cage. Group delocalization indices tell when and where binding happens. Gallegos et al., Nat. Commun. 2024, CC BY 4.0." >}}

## Why it matters

- **Speed meets rigour.** Descriptors that used to take hours per geometry are now available at every step of a
  molecular dynamics trajectory.
- **Explanations with physical meaning.** Group delocalization indices computed from the atomistic predictions work as
  reliable reporters of supramolecular binding events, giving an explanation grounded in physics instead of in the
  internals of a network.
- **A route to Explainable Chemical AI (XCAI).** The work points to models whose outputs chemists can read directly
  in terms of atoms, bonds and electron sharing.

The code is freely available: see [SchNet4AIM](/software/schnet4aim/).
The paper has collected about 100 citations in its first two years.

**Related:** [Machine learning research line](/research/machine-learning-chemistry/) ·
[Publication page](/publication/2024-explainable-chemical-artificial-intelligence-from-accurate-machine-learning-of-r/)
