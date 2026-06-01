> [!WARNING]
> **This repository is under active development for ISMB 2026.**
>
> Tutorial: **From Trees to Networks**, scheduled for July-12, 9am-1pm at ISMB 2026.
>
> Materials will be finalized by **June 16, 2026**. Until then, files may
> change without notice and some sections may be incomplete. If you're a
> registered attendee, please follow [`SETUP.md`](SETUP.md) starting one
> week before the tutorial.

# From Trees to Networks

Tutorial materials for *From Trees to Networks*, originally developed for the
[ISMB 2026](https://www.iscb.org/ismb2026/) tutorial program [(tutorial IP3)](https://www.iscb.org/ismb2026/whats-happening/tutorials#ip3). The tutorial
covers phylogenetic and phylogenomic analysis using gene trees, species trees,
and phylogenetic networks, with hands-on exercises using the *Anopheles
gambiae* species complex from [Fontaine et al. (2015)](https://www.science.org/doi/10.1126/science.1258524) — a textbook dataset
for studying pervasive autosomal introgression.

## Tutorial Overview

Participants will work through a phylogenomic inference pipeline from sequence
alignments to phylogenetic networks:

- **Part I — Trees** (110 min): per-locus gene tree inference with
  maximum likelihood (IQ-TREE 3) and Bayesian inference (BEAST X), then
  coalescent species-tree estimation with wASTRAL (ASTER)
- **Part II — Networks** (110 min): visualizing conflicting phylogenetic
  signal with SplitsTree, building networks interactively with PhyloSketch,
  and inferring networks from gene tree sets with PhyloCompare.

The pedagogical core: when the genome has been pervasively introgressed,
trees and tree-summary methods can return confident but biologically
incorrect answers. Networks make the conflict visible rather than
averaging it away.

## Audience

The tutorial is aimed at researchers with some prior exposure to
phylogenetics. Familiarity with command-line tools and basic
sequence-alignment concepts is assumed. No prior experience with
phylogenetic networks is required.

## Getting Started

1. Read [`doc/Setup.md`](doc/Setup.md) for installation instructions and prerequisites
   — **complete this before tutorial day**.
2. Clone this repository to your laptop:
   ```bash
   git clone https://github.com/husonlab/trees-to-networks-tutorial.git
   ```
3. On tutorial day, follow the hands-on guide [`doc/Hands-On-Guide.md`](doc/Hands-On-Guide.md).

## Repository Structure

```
trees-to-networks-tutorial/
├── README.md
├── doc/                    # documents: Setup, Hands-On Guide, Cheat Sheet, References
├── slides/                 # tutorial slide deck (PDF)
├── data/                   # 15 per-locus alignments + metadata
├── data-prep/              # scripts used to build data/ from raw MAF
├── precomputed/            # expected outputs for every hands-on step
│   ├── iqtree/             # IQ-TREE gene trees & NEXUS tree set
│   ├── astral/             # wASTRAL species tree
│   ├── beast/              # BEAST X posterior on locus X_dist_04
│   └── networks/           # SplitsTree & PhyloFusion network outputs
└── tools/                  # Additional tools
```

A guiding principle: **every output participants might generate during the
tutorial has a precomputed version in `precomputed/`**. If a step fails on
your laptop, copy the precomputed file and rejoin at the next step.

## Citation

If you use these materials, please cite:

> Huson, D.H., Gautam, A., Cetinkaya, B. (2026). *From Trees to Networks.*
> ISMB 2026 Tutorial. https://github.com/husonlab/trees-to-networks-tutorial

For the source data:

> Fontaine, M.C., Pease, J.B., Steele, A., et al. (2015). Extensive
> introgression in a malaria vector species complex revealed by
> phylogenomics. *Science* 347(6217): 1258524.
> https://doi.org/10.1126/science.1258524

## License

Tutorial materials (slides, exercises, scripts) are released under
[CC-BY-4.0](LICENSE). Source data are derived from the Fontaine et al. (2015)
Dryad deposit (doi:10.5061/dryad.f4114) and are subject to the terms of that
deposit.

## Acknowledgments

This tutorial would not be possible without the open-source tools developed
by the phylogenetics community:

- [IQ-TREE](http://www.iqtree.org/) — Minh, Wong, Ly-Trong et al.
- [BEAST X](https://beast.community) — Baele, Drummond, Suchard, Rambaut, Lemey et al.
- [ASTRAL](https://github.com/smirarab/ASTRAL) —  Rabiee, Sayyari, and Mirarab
- [Tracer](https://github.com/beast-dev/tracer) — Rambaut et al.
- [SplitsTree](https://github.com/husonlab/splitstree6) — Huson lab
- [PhyloSketch](https://github.com/husonlab/phylosketch2) — Huson lab
- [PhyloCompare](https://github.com/husonlab/phylocompare) — Huson lab
