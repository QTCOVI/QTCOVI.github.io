---
title: NNAIMQ
summary: >
  A Python-interfaced neural network model for the rapid prediction of QTAIM atomic charges
  of C, H, O and N atoms in gas-phase organic and biological molecules.
tags:
  - Machine learning
  - QTAIM
  - Atomic charges
  - Neural networks
date: 2024-01-01
external_link: 'https://github.com/QTCOVI/NNAIMQ'
---

## About

**NNAIMQ** predicts QTAIM (Bader) partial charges for C, H, O and N atoms in neutral, singlet-spin gas-phase organic and biological molecules. It comprises four Artificial Neural Networks (one per element) fitted to high-quality quantum chemical data.

Key features:
- High-accuracy QTAIM charges without running a full topological analysis.
- Supports standard `.xyz` geometry files as input.
- Compatible with x86-64 and ARM (Apple M1) processors.

## Requirements

- Python ≥ 3.7.3
- `keras`, `matplotlib`, `numpy`, `pandas`, `seaborn`, `tensorflow`

## Usage

```bash
cd code/
python nnaimq.py input
```

where `input` is a plain-text file listing the `.xyz` geometry files to process.

## Links

- [GitHub repository](https://github.com/QTCOVI/NNAIMQ)
