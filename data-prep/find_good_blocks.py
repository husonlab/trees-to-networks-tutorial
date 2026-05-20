#!/usr/bin/env python3.11
"""
find_good_blocks.py — Find MAF blocks where ALL specified species are present.

The goal is to pick 3+ kb alignment windows that fall entirely within a single
high-coverage block, avoiding the gappy stitched-alignment artifacts you get
when a window spans multiple blocks of varying species coverage.

Usage:
    python find_good_blocks.py /path/to/chr2R.tba_HD_AgamC9.maf \\
        --required AgamP3,AgamM1,AgamS1,AaraD1,AquaS1,AmelC1,AmerM1,AchrA1 \\
        --min-length 3000 \\
        --out chr2R.good_blocks.tsv

Output is a TSV with columns:
    chrom   start   end   length_bp   n_species   species_codes

Each row is one block in the MAF that contains all the required species and
is at least min-length bp long in reference coordinates. Pick locus windows
that fall comfortably inside one of these blocks.
"""

import argparse
import sys
from pathlib import Path


def parse_s_line(line):
    """Parse a MAF 's' line. Returns (species_code, contig, start, size, strand)
    or None if the line is malformed."""
    parts = line.split()
    if len(parts) < 7 or parts[0] != "s":
        return None
    src = parts[1]
    if "." in src:
        sp_code, contig = src.split(".", 1)
    else:
        sp_code, contig = src, ""
    try:
        start = int(parts[2])
        size = int(parts[3])
        strand = parts[4]
    except (ValueError, IndexError):
        return None
    return sp_code, contig, start, size, strand


def iterate_blocks(path):
    """Yield lists of 's' line records, one list per alignment block."""
    current_block = []
    with open(path) as fh:
        for line in fh:
            if line.startswith("a"):
                if current_block:
                    yield current_block
                current_block = []
            elif line.startswith("s "):
                rec = parse_s_line(line)
                if rec is not None:
                    current_block.append(rec)
    if current_block:
        yield current_block


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("maf_path", help="Path to a .maf file")
    ap.add_argument("--required", required=True,
                    help="Comma-separated species codes that must all be present in each block")
    ap.add_argument("--reference", default="AgamP3",
                    help="Reference species code, used for output coordinates (default: AgamP3)")
    ap.add_argument("--min-length", type=int, default=3000,
                    help="Minimum block size in reference bp (default: 3000)")
    ap.add_argument("--out", default="-",
                    help="Output TSV path; '-' for stdout (default: stdout)")
    args = ap.parse_args()

    required = set(args.required.split(","))
    if args.reference not in required:
        required.add(args.reference)

    out_fh = open(args.out, "w") if args.out != "-" else sys.stdout
    out_fh.write("chrom\tstart\tend\tlength_bp\tn_species\tspecies_codes\n")

    n_total = 0
    n_with_all = 0
    n_good = 0

    for block in iterate_blocks(args.maf_path):
        n_total += 1
        species_in_block = {rec[0]: rec for rec in block}

        if not required.issubset(species_in_block.keys()):
            continue
        n_with_all += 1

        ref_rec = species_in_block[args.reference]
        ref_contig, ref_start, ref_size, ref_strand = ref_rec[1], ref_rec[2], ref_rec[3], ref_rec[4]

        if ref_size < args.min_length:
            continue
        n_good += 1

        ref_end = ref_start + ref_size
        sp_list = ",".join(sorted(species_in_block.keys()))
        out_fh.write(f"{ref_contig}\t{ref_start}\t{ref_end}\t{ref_size}\t"
                     f"{len(species_in_block)}\t{sp_list}\n")

    print(f"Scanned {n_total} blocks.", file=sys.stderr)
    print(f"  {n_with_all} contain all required species "
          f"({100*n_with_all/n_total:.1f}%)", file=sys.stderr)
    print(f"  {n_good} are also >= {args.min_length} bp on the reference", file=sys.stderr)

    if args.out != "-":
        out_fh.close()


if __name__ == "__main__":
    main()
