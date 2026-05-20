#!/opt/homebrew/bin/python3.11

"""
inspect_maf.py — Scan a MAF file and report all unique species codes and contigs.

Run this once per chromosome MAF to discover the species codes present in the
Fontaine et al. 2015 Dryad data (doi:10.5061/dryad.f4114), then use the codes
to populate species_map.tsv for extract_loci.py.

Usage:
    python inspect_maf.py /path/to/chr2R.tba_HD_AgamC9.maf [--max-blocks N]
"""

import argparse
import sys
from collections import Counter, defaultdict


def scan_maf(path, max_blocks=None):
    """Return (species_counts, contig_examples, block_count)."""
    species_counts = Counter()
    contig_examples = defaultdict(set)  # species -> set of contig names seen
    block_count = 0

    with open(path) as fh:
        for line in fh:
            if line.startswith("a"):
                block_count += 1
                if max_blocks is not None and block_count > max_blocks:
                    break
            elif line.startswith("s"):
                # s species.contig start size strand srcSize seq
                parts = line.split()
                if len(parts) < 2:
                    continue
                src = parts[1]
                if "." in src:
                    species, contig = src.split(".", 1)
                else:
                    species, contig = src, ""
                species_counts[species] += 1
                if len(contig_examples[species]) < 3:
                    contig_examples[species].add(contig)

    return species_counts, contig_examples, block_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("maf_path", help="Path to a .maf file")
    ap.add_argument("--max-blocks", type=int, default=5000,
                    help="Scan only the first N blocks for speed (default: 5000; "
                         "use 0 for full scan)")
    args = ap.parse_args()

    max_blocks = None if args.max_blocks == 0 else args.max_blocks
    print(f"Scanning {args.maf_path}"
          + (f" (first {max_blocks} blocks)" if max_blocks else " (full file)")
          + " ...", file=sys.stderr)

    counts, examples, n_blocks = scan_maf(args.maf_path, max_blocks=max_blocks)

    print(f"\nScanned {n_blocks} alignment blocks.\n")
    print(f"{'Species code':<15} {'#blocks':>8}  Example contigs")
    print("-" * 60)
    for sp, n in counts.most_common():
        ex = ", ".join(sorted(examples[sp])[:3])
        print(f"{sp:<15} {n:>8}  {ex}")


if __name__ == "__main__":
    main()
