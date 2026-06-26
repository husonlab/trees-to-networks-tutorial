# Tree processing scripts

Scripts run by tutorial attendees to post-process IQ-TREE output for
downstream visualization in SplitsTree and PhyloParallelograms.

## Tools

1. **`make_nexus_treeset.py`** - convert IQ-TREE `-S` mode output (one
   Newick tree per line, ordered alphabetically by input FASTA filename)
   into a NEXUS file with each tree labelled by its locus ID and rooted
   on a chosen outgroup.

   Usage:

       python scripts/make_nexus_treeset.py \
           --alignments-dir alignments/ \
           --treefile tutorial_loci.treefile \
           --out tutorial_loci.nex \
           --outgroup An_christyi

   Locus IDs are taken from the alignment filenames in
   `--alignments-dir`, matched against the trees in `--treefile` by
   position (the same alphabetical order IQ-TREE used). The `--outgroup`
   taxon must be present in every tree; the script re-roots each tree
   on that taxon before writing the NEXUS block.

## Dependencies

This script requires the `ete3` package for tree parsing, rooting, and
NEXUS output. Install with either:

    pip install ete3

or, if you use conda:

    conda install -c etetoolkit ete3