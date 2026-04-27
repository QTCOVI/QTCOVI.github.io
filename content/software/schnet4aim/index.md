---
title: SchNet4AIM
summary: >
  A deep learning code based on the SchNet architecture for training models on atomic (1-body)
  and pairwise (2-body) QTAIM properties. Supports CPU and GPU execution.
tags:
  - Machine learning
  - QTAIM
  - Neural networks
  - Deep learning
date: 2024-01-01
external_link: 'https://github.com/QTCOVI/SchNet4AIM'
---

## About

**SchNet4AIM** is a code designed to train [SchNet](https://doi.org/10.1063/1.5019779) deep-learning models on atomic (1-body) and pairwise (2-body) properties formulated within the Quantum Theory of Atoms in Molecules (QTAIM). It is built as a targeted modification of [SchNetPack](https://github.com/atomistic-machine-learning/schnetpack), retaining only the components relevant for 1p/2p property training.

Key features:
- Train on **atomic** (charges, energies, volumes) or **pairwise** (delocalization indices, IQA interaction energies) QTAIM properties.
- Supports **JSON** and **ASE-SQLite** database formats.
- Runs on **CPU and GPU** (GPU recommended for speed).

## Installation

```bash
git clone https://github.com/QTCOVI/SchNet4AIM.git
cd SchNet4AIM
pip install -r requirements.txt
```

## Links

- [GitHub repository](https://github.com/QTCOVI/SchNet4AIM)
