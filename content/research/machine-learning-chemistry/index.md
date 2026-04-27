---
title: Machine Learning & Neural Network Potentials
summary: >
  We integrate quantum chemical topology with machine learning to build physically
  motivated neural network interatomic potentials and to accelerate the discovery
  of new chemical bonding descriptors.
tags:
  - Machine learning
  - Neural network potentials
  - AI in chemistry
date: 2024-01-01
---

## Overview

Machine learning is transforming computational chemistry, and we are harnessing it in two complementary ways:

### IQA-Informed Neural Network Potentials
Classical machine-learned interatomic potentials (NNPs) are trained on total energies and forces, but lack chemical interpretability. We develop NNPs informed by IQA energy components (self-energies and interaction energies), resulting in potentials that:
- Decompose into physically meaningful atomic and pairwise contributions.
- Transfer more reliably to out-of-distribution chemical environments.
- Naturally encode the correct physics of bonding interactions.

### Topological Descriptors as ML Features
QTAIM atomic properties and IQA energy components serve as physically motivated features for machine learning models targeting molecular properties, reaction barriers, and drug–target binding affinities.

### Deep Learning for Electron Density
We explore the use of deep learning models to predict electron densities directly, enabling rapid computation of topological properties for large molecular datasets.

## Codes & Tools
Our ML work builds on open-source frameworks (PyTorch, JAX) and is integrated with our in-house topological analysis codes.
