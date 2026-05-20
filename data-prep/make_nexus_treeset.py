#!/usr/bin/env python3.11
"""
make_nexus_treeset.py - Convert IQ-TREE -S multi-locus output into a NEXUS file
with named trees, suitable as input to SplitsTree, PhyloFusion, Dendroscope, etc.

In -S mode, IQ-TREE writes one tree per line to <prefix>.treefile, in the
alphabetical order of the input FASTA filenames. This script pairs each tree
with its corresponding locus ID (the FASTA stem) and emits a NEXUS file with
named trees.

Usage:
    python make_nexus_treeset.py \\
        --alignments-dir alignments/ \\
        --treefile tutorial_loci.treefile \\
        --out tutorial_loci.nex

Requires: ete3 (for robust Newick parsing)
"""

import argparse
import sys
from pathlib import Path

try:
    from ete3 import Tree
except ImportError:
    sys.exit("ERROR: ete3 is not installed. Run: pip install ete3")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--alignments-dir", required=True,
                    help="Directory containing the input FASTA alignments")
    ap.add_argument("--treefile", required=True,
                    help="IQ-TREE output treefile (one Newick tree per line)")
    ap.add_argument("--out", required=True,
                    help="Output NEXUS file path (e.g. tutorial_loci.nex)")
    args = ap.parse_args()

    # Match IQ-TREE -S file ordering: alphabetical sort of *.fasta in the dir.
    fasta_files = sorted(Path(args.alignments_dir).glob("*.fasta"))
    locus_ids = [f.stem for f in fasta_files]
    if not locus_ids:
        sys.exit(f"ERROR: no *.fasta files found in {args.alignments_dir}")

    # Read the trees (one per line, blank lines ignored).
    with open(args.treefile) as fh:
        trees_newick = [line.strip() for line in fh if line.strip()]

    if len(trees_newick) != len(locus_ids):
        sys.exit(f"ERROR: {len(trees_newick)} trees in {args.treefile} but "
                 f"{len(locus_ids)} FASTA files in {args.alignments_dir}.\n"
                 f"FASTAs: {locus_ids}")

    # Collect the union of taxa across all trees (some loci may miss species).
    all_taxa = set()
    for newick in trees_newick:
        t = Tree(newick, format=0)
        all_taxa.update(leaf.name for leaf in t.get_leaves())
    taxa_sorted = sorted(all_taxa)

    # Write NEXUS file with named TREES block.
    with open(args.out, "w") as fh:
        fh.write("#NEXUS\n\n")
        fh.write("BEGIN TAXA;\n")
        fh.write(f"    DIMENSIONS NTAX={len(taxa_sorted)};\n")
        fh.write("    TAXLABELS\n")
        for taxon in taxa_sorted:
            fh.write(f"        {taxon}\n")
        fh.write("    ;\n")
        fh.write("END;\n\n")

        fh.write("BEGIN TREES;\n")
        for locus_id, newick in zip(locus_ids, trees_newick):
            # Ensure the newick ends with ';'
            n = newick if newick.endswith(";") else newick + ";"
            fh.write(f"    TREE {locus_id} = {n}\n")
        fh.write("END;\n")

    print(f"Wrote {len(locus_ids)} named trees to {args.out}")
    print(f"  ({len(taxa_sorted)} taxa)")
    print(f"\nTaxa in trees: {', '.join(taxa_sorted)}")


if __name__ == "__main__":
    main()

