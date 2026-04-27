---
title: edf-omp
summary: >
  High-performance Fortran code for computing Electron Number Distribution Functions (EDFs)
  in real-space atomic basins, accelerated with OpenMP parallelism and LAPACK.
tags:
  - Electron distribution
  - Topological analysis
  - Fortran
  - HPC
date: 2024-01-01
external_link: 'https://github.com/QTCOVI/edf-omp'
---

## About

**edf-omp** computes **Electron Number Distribution Functions** (EDFs) — the probability distribution of finding *n* electrons in a QTAIM atomic basin. EDFs encode the full statistics of electron population fluctuations, giving direct access to:

- Atomic mean electron populations (charges).
- Electron localisation and delocalization indices.
- Higher-order cumulants revealing multi-centre bonding and electron correlation.

The code is written in Fortran and parallelised with **OpenMP**, using **LAPACK** for the required linear algebra. It is designed for high-throughput calculations on large systems.

The compiled binary is also available at the companion [GitHub Pages site](https://qtcovi.github.io/edf-omp/).

## Links

- [GitHub repository](https://github.com/QTCOVI/edf-omp)
- [Web page & downloads](https://qtcovi.github.io/edf-omp/)
