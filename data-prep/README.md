# Data Preparation

Scripts used to build the alignments in `../data/alignments/` from the
raw multiple genome alignment file (MAF) deposited by Fontaine et al.
(2015).

You do NOT need to rerun these scripts to do the tutorial - the output
alignments are already in `../data/alignments/`. The scripts are
included for reproducibility and for participants who want to apply the
same workflow to their own MAF files.

## Workflow overview

1. **`inspect_maf.py`** - scan a MAF file and report which species are
   present in each block (used to verify species codes)
2. **`find_good_blocks.py`** - find MAF blocks where all required
   species are simultaneously present and the block is long enough to
   serve as a locus
3. **`extract_loci.py`** - extract per-locus FASTA alignments from a
   MAF file given a list of coordinates (`loci.tsv`)

## Source data

To rerun from scratch, download the MAF from Dryad:
https://datadryad.org/dataset/doi:10.5061/dryad.f4114

The relevant directory is `MAF_HD_V4_TBA.C9.DRYAD/` containing one
.maf file per chromosome.

## Configuration files

- `../data/loci.tsv` - the 15 loci we picked, with coordinates and
  expected topology categories
- `../data/species_map.tsv` - mapping from MAF species codes to clean
  phylogenetic names
