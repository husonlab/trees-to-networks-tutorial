# Precomputed Outputs

Every output a participant might generate during the tutorial has a
precomputed version here. If your live run fails or is slow, copy the
corresponding precomputed file and rejoin the group at the next step.

## Subdirectories

- `iqtree/` - IQ-TREE 3 per-locus ML gene trees and combined NEXUS
- `beast/` - BEAST X Bayesian analysis of X_dist_04 (XML, log, trees,
  MCC tree)
- `astral/` - wASTRAL coalescent species tree from the gene tree set
- `networks/` - SplitsTree NeighborNet, consensus network, and
  PhyloCompare outputs

## Use during the tutorial

The exercise files in `../exercises/` reference these precomputed
outputs when a fallback path is needed. The slides also reference
these (e.g., the BEAST Tracer screenshot uses
`beast/X_dist_04.log`).
