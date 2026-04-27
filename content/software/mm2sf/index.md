---
title: MM2SF
summary: >
  A tool for the automated generation of optimised Atom-Centred Symmetry Functions (ACSFs)
  for neural network interatomic potentials, using Gaussian Mixture Models to characterise
  the chemical space of a system.
tags:
  - Machine learning
  - Neural network potentials
  - Symmetry functions
  - Descriptor generation
date: 2024-01-01
external_link: 'https://github.com/QTCOVI/MM2SF'
---

## About

**MM2SF** automatically generates optimised Atom-Centred Symmetry Functions (ACSFs) for use as descriptors in neural network interatomic potentials. Given a molecular dynamics trajectory or normal-mode sampling, it applies a Gaussian Mixture Model (GMM) to decompose the chemical space into well-defined clusters, then selects symmetry function parameters that accurately describe each region.

Supported symmetry function types:
- **Two-body (radial)** — *G*<sup>rad</sup>
- **Three-body (angular)** — *G*<sup>ang</sup> (modified functional form)

## Installation

```bash
pip install git+https://github.com/m-gallegos/MM2SF.git
```

Or from a downloaded zip:

```bash
pip install MM2SF-main.zip
```

## Links

- [GitHub repository](https://github.com/QTCOVI/MM2SF)
