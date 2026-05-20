# Data

Tutorial input data: 15 per-locus alignments from the Anopheles gambiae
species complex, plus metadata describing each locus and the species
mapping.

## Contents

- `loci.tsv` - locus metadata (chromosome, coordinates, expected
  topology, pedagogical role)
- `species_map.tsv` - mapping from MAF species codes to clean species
  names
- `alignments/` - 15 FASTA alignments, one per locus

## Provenance

These alignments were extracted from the multiple genome alignment
deposited at Dryad doi:10.5061/dryad.f4114 by Fontaine et al. (2015).
See `../data-prep/README.md` for the extraction procedure.

The original MAF file (~2 GB) is not included in this repo; only the
15 per-locus extracts (~5 KB each) are shipped. To rerun the extraction,
download the MAF from Dryad and follow the instructions in
`../data-prep/`.

## Citation

> Fontaine, M.C., Pease, J.B., Steele, A., et al. (2015). Extensive
> introgression in a malaria vector species complex revealed by
> phylogenomics. Science 347(6217): 1258524.
