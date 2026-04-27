---
title:
date: 2024-01-01
type: landing

sections:
  - block: hero
    content:
      title: |
        QTCOVI
        Research Group
      image:
        filename: group_photo.jpg
      text: |
        <br>

        We are the **Theoretical and Computational Chemistry** group at the [University of Oviedo](https://www.uniovi.es), Spain.
        We develop orbital-invariant methodologies to understand chemical bonding through **Quantum Chemical Topology** (QCT),
        with applications ranging from catalysis and excited states to biomolecules and AI-assisted chemistry.
    design:
      background:
        color: '#1565c0'
        text_color_light: true

  - block: features
    content:
      title: Research Pillars
      items:
        - name: Quantum Chemical Topology
          icon: atom
          icon_pack: fas
          description: >
            We use QCT—including QTAIM and IQA—to rigorously partition molecular energies and electron densities,
            providing physically meaningful descriptors of chemical bonding.
        - name: Real-Space Descriptors
          icon: chart-bar
          icon_pack: fas
          description: >
            Statistics of the electron distribution in real space underpin our bond indices, delocalization measures,
            and non-covalent interaction descriptors.
        - name: Method Development & AI
          icon: brain
          icon_pack: fas
          description: >
            We develop new topological tools and increasingly combine them with machine learning and neural network
            potentials to tackle complex chemical systems.

  - block: collection
    content:
      title: Recent Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: ''
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'

  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text:
      email: ampendas@uniovi.es
      address:
        street: Departamento de Química Física y Analítica, Facultad de Química
        city: Oviedo
        region: Asturias
        postcode: '33006'
        country: Spain
        country_code: ES
      autolink: true
    design:
      columns: '2'
---
