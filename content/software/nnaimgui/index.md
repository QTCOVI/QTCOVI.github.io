---
title: NNAIMGUI
summary: >
  A graphical user interface for the prediction and visualisation of QTAIM atomic properties
  using feed-forward neural network models. Includes the built-in NNAIMQ model for Bader charges.
tags:
  - Machine learning
  - QTAIM
  - Atomic charges
  - GUI
  - Neural networks
date: 2023-01-01
external_link: 'https://github.com/QTCOVI/NNAIMGUI'
---

## About

**NNAIMGUI** (M. Gallegos, University of Oviedo, 2023) is a code for the prediction and visualisation of atomic properties using feed-forward neural network (FFNN) models. It ships with the built-in NNAIMQ model for predicting QTAIM charges of gas-phase neutral singlet molecules containing C, H, O and N atoms, and supports user-supplied custom models for any atomic property of interest.

Key features:
- **Graphical user interface** for non-expert users, plus command-line mode.
- Built-in **charge equilibration** to enforce molecular electroneutrality (13 algorithms included).
- Supports user-defined FFNN models for any atomic property.
- Compatible with **Linux and Windows**.

## Installation

```bash
pip install git+https://github.com/m-gallegos/NNAIMGUI.git
```

## Citation

> M. Gallegos *et al.*, *J. Chem. Inf. Model.* (2023). https://doi.org/10.1021/acs.jcim.3c00597

## Links

- [GitHub repository](https://github.com/QTCOVI/NNAIMGUI)
- [Publication](https://doi.org/10.1021/acs.jcim.3c00597)
