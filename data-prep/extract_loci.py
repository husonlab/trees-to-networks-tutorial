#!/opt/homebrew/bin/python3.11
"""
extract_loci.py — Extract per-locus FASTA alignments from Fontaine et al. 2015
Anopheles gambiae complex MAF files for the ISMB 2026 tutorial.

Workflow:
  1. Reads a TSV of loci (locus_id, chrom, start, end, ...) — see loci.tsv
  2. Reads a TSV mapping MAF species codes to clean species names — see species_map.tsv
  3. For each locus, uses Biopython's MafIndex to extract the alignment slice
     anchored on the reference species (default: AgamP3).
  4. Writes one FASTA per locus with cleaned species names.
  5. Reports QC info per locus: species present, alignment length, gap fraction.

Usage:
    pip install biopython
    python extract_loci.py \\
        --maf-dir /path/to/MAF_HD_V4_TBA.C9.DRYAD \\
        --loci loci.tsv \\
        --species-map species_map.tsv \\
        --out-dir alignments/

The first run for a given chromosome builds a SQLite index alongside the .maf
file (named *.mafindex). This indexing takes a few minutes per chromosome but
is one-time; subsequent extractions are fast.
"""

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

try:
    from Bio.AlignIO.MafIO import MafIndex
except ImportError:
    sys.exit("ERROR: biopython is not installed. Run: pip install biopython")


# ---- IO helpers ------------------------------------------------------------

def load_loci(path):
    """Load loci from a TSV file with columns: locus_id, chrom, start, end (+ any extras)."""
    loci = []
    with open(path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            row["start"] = int(row["start"])
            row["end"] = int(row["end"])
            loci.append(row)
    return loci


def load_species_map(path):
    """Load MAF code -> clean species name map. Lines starting with # are comments."""
    mapping = {}
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            code, name = parts[0].strip(), parts[1].strip()
            if code and name:
                mapping[code] = name
    return mapping


# ---- Core extraction --------------------------------------------------------

def index_for_chrom(maf_dir, chrom, reference):
    """Build (or load existing) MafIndex for one chromosome MAF."""
    maf_path = Path(maf_dir) / f"{chrom}.tba_HD_AgamC9.maf"
    if not maf_path.exists():
        raise FileNotFoundError(f"MAF not found: {maf_path}")
    idx_path = str(maf_path) + ".mafindex"
    target = f"{reference}.{chrom}"
    print(f"  [{chrom}] using reference {target}", file=sys.stderr)
    print(f"  [{chrom}] indexing {maf_path.name} (one-time; subsequent runs fast)...",
          file=sys.stderr)
    return MafIndex(idx_path, str(maf_path), target)


def extract_locus(idx, start, end, species_map):
    """Return dict {clean_name: aligned_sequence} for one locus."""
    try:
        msa = idx.get_spliced([start], [end], strand=1)
    except Exception as e:
        print(f"    ERROR extracting {start}-{end}: {e}", file=sys.stderr)
        return None

    seen = {}
    for record in msa:
        # record.id looks like "AgamP3.chr2R" or "AmerM1.chrsupercont1.201"
        code = record.id.split(".", 1)[0]
        clean = species_map.get(code)
        if clean is None:
            # Skip species not in our map (e.g. extra strains we don't want)
            continue
        if clean in seen:
            # Duplicate species in alignment (rare; can happen with merged blocks).
            # Keep the longer non-gap version.
            old = seen[clean]
            new = str(record.seq)
            if (len(new) - new.count("-")) > (len(old) - old.count("-")):
                seen[clean] = new
        else:
            seen[clean] = str(record.seq)
    return seen


def write_fasta(seqs, path):
    """Write {name: seq} dict as FASTA."""
    with open(path, "w") as fh:
        for name, seq in seqs.items():
            fh.write(f">{name}\n{seq}\n")


# ---- QC reporting -----------------------------------------------------------

def report(locus_id, seqs, expected):
    """Print one-line QC for a locus. Returns True if all expected species present."""
    if seqs is None:
        print(f"  FAIL {locus_id}: extraction failed")
        return False
    n = len(seqs)
    aln_len = len(next(iter(seqs.values()))) if seqs else 0
    missing = expected - set(seqs.keys())
    extra = set(seqs.keys()) - expected
    gap_total = sum(s.count("-") + s.upper().count("N") for s in seqs.values())
    total = sum(len(s) for s in seqs.values())
    gap_pct = (100.0 * gap_total / total) if total else 0.0
    flag = "OK  " if not missing else "WARN"
    extras = []
    if missing:
        extras.append(f"missing={','.join(sorted(missing))}")
    if extra:
        extras.append(f"extra={','.join(sorted(extra))}")
    tail = ("  " + "; ".join(extras)) if extras else ""
    print(f"  {flag} {locus_id:<15} {n} species, {aln_len:>5} bp, {gap_pct:5.1f}% gap/N{tail}")
    return not missing


# ---- Main -------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--maf-dir", required=True,
                    help="Directory containing the *.tba_HD_AgamC9.maf files")
    ap.add_argument("--loci", required=True,
                    help="TSV file with locus list (columns: locus_id, chrom, start, end, ...)")
    ap.add_argument("--species-map", required=True,
                    help="TSV mapping MAF species codes to clean names")
    ap.add_argument("--out-dir", required=True,
                    help="Output directory for FASTA files")
    ap.add_argument("--reference", default="AgamP3",
                    help="Reference species code used to anchor coordinates (default: AgamP3)")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    loci = load_loci(args.loci)
    species_map = load_species_map(args.species_map)
    # The "expected" set is everything in the map EXCEPT the reference, unless
    # the reference is also listed as a phylogenetic taxon.
    expected = set(species_map.values())

    print(f"Loaded {len(loci)} loci.", file=sys.stderr)
    print(f"Loaded species map with {len(species_map)} codes -> "
          f"{len(expected)} clean names.", file=sys.stderr)

    # Group loci by chromosome to reuse indices
    by_chrom = defaultdict(list)
    for l in loci:
        by_chrom[l["chrom"]].append(l)

    n_ok = 0
    n_total = len(loci)
    for chrom in sorted(by_chrom.keys()):
        print(f"\n=== {chrom} ({len(by_chrom[chrom])} loci) ===", file=sys.stderr)
        try:
            idx = index_for_chrom(args.maf_dir, chrom, reference=args.reference)
        except FileNotFoundError as e:
            print(f"  SKIP: {e}", file=sys.stderr)
            continue
        for l in by_chrom[chrom]:
            seqs = extract_locus(idx, l["start"], l["end"], species_map)
            ok = report(l["locus_id"], seqs, expected)
            if seqs:
                write_fasta(seqs, out_dir / f"{l['locus_id']}.fasta")
                if ok:
                    n_ok += 1

    print(f"\nDone. {n_ok}/{n_total} loci have all expected species present.",
          file=sys.stderr)
    if n_ok < n_total:
        print("Loci with missing species were still written (check the WARN lines).",
              file=sys.stderr)


if __name__ == "__main__":
    main()
