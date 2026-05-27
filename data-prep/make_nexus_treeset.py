#!/usr/bin/env python3.11
"""
make_nexus_treeset.py - Convert IQ-TREE -S multi-locus output into a NEXUS
file with named, optionally rerooted trees, suitable as input to PhyloCompare,
SplitsTree, Dendroscope, etc.

In -S mode, IQ-TREE writes one tree per line to <prefix>.treefile, in the
alphabetical order of the input FASTA filenames. This script:

  1. Pairs each tree with its corresponding locus ID (the FASTA stem)
  2. Optionally re-roots each tree on a specified outgroup taxon
  3. Writes a NEXUS file with named TREES block

Usage:
    python make_nexus_treeset.py \\
        --alignments-dir alignments/ \\
        --treefile tutorial_loci.treefile \\
        --out tutorial_loci.nex \\
        --outgroup An_christyi

If --outgroup is omitted, trees are written as-is (no rerooting).

If a tree does not contain the outgroup taxon (e.g. that species was missing
from the alignment), the tree is written without rerooting and a warning is
printed.

Requires: ete3 (for robust Newick parsing and rerooting)
"""

import argparse
import sys
from pathlib import Path

try:
    from ete3 import Tree
except ImportError:
    sys.exit("ERROR: ete3 is not installed. Run: pip install ete3")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--alignments-dir", required=True,
                    help="Directory containing the input FASTA alignments")
    ap.add_argument("--treefile", required=True,
                    help="IQ-TREE output treefile (one Newick tree per line)")
    ap.add_argument("--out", required=True,
                    help="Output NEXUS file path (e.g. tutorial_loci.nex)")
    ap.add_argument("--outgroup", default=None,
                    help="Taxon to root each tree on (e.g. An_christyi). "
                         "If omitted, no rerooting is performed.")
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

    # Process trees: optionally reroot, collect taxa.
    processed_newick = []
    all_taxa = set()
    rerooted_count = 0
    skipped_count = 0

    for locus_id, newick in zip(locus_ids, trees_newick):
        t = Tree(newick, format=0)
        leaf_names = set(t.get_leaf_names())
        all_taxa.update(leaf_names)

        if args.outgroup:
            if args.outgroup in leaf_names:
                try:
                    t.set_outgroup(args.outgroup)
                    rerooted_count += 1
                except Exception as e:
                    print(f"  WARN  {locus_id}: rerooting failed "
                          f"({e}); writing original tree",
                          file=sys.stderr)
                    skipped_count += 1
            else:
                print(f"  WARN  {locus_id}: outgroup '{args.outgroup}' "
                      f"not in tree; writing original tree",
                      file=sys.stderr)
                skipped_count += 1

        # Write Newick with support values and branch lengths preserved.
        # format=0 preserves both internal node names (bootstrap values) and
        # branch lengths in the standard way.
        processed_newick.append(t.write(format=0))

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
        for locus_id, newick in zip(locus_ids, processed_newick):
            n = newick if newick.endswith(";") else newick + ";"
            fh.write(f"    TREE {locus_id} = {n}\n")
        fh.write("END;\n")

    # Summary output.
    print(f"Wrote {len(locus_ids)} named trees to {args.out}")
    print(f"  ({len(taxa_sorted)} taxa)")
    if args.outgroup:
        print(f"  Rerooted on outgroup: {args.outgroup}")
        print(f"    rerooted: {rerooted_count}")
        if skipped_count:
            print(f"    skipped (outgroup absent): {skipped_count}")
    print(f"\nTaxa in trees: {', '.join(taxa_sorted)}")


if __name__ == "__main__":
    main()
