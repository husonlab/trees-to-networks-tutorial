# Trees to Networks - Cheat Sheet

ISMB 2026 Tutorial IP3. Designed to print on A4, double-sided.

## Repository

    git clone https://github.com/husonlab/trees-to-networks-tutorial.git
    cd trees-to-networks-tutorial

## Species (7)

| Code               | Species              | Role         |
|--------------------|----------------------|--------------|
| An_gambiae         | A. gambiae           | Vector       |
| An_coluzzii        | A. coluzzii          | Vector       |
| An_arabiensis      | A. arabiensis        | Vector       |
| An_quadriannulatus | A. quadriannulatus   | Non-vector   |
| An_melas           | A. melas             | Minor vector |
| An_merus           | A. merus             | Minor vector |
| An_christyi        | A. christyi          | Outgroup     |

## Loci (15)

| Region             | n | Expected topology                                  |
|--------------------|---|----------------------------------------------------|
| X distal (Xag)     | 5 | (arabiensis, quadriannulatus) -- species tree      |
| X pericentromeric  | 1 | (arabiensis, (gambiae, coluzzii)) -- introgressed  |
| Autosomal (2R, 3R) | 5 | (arabiensis, (gambiae, coluzzii)) -- introgressed  |
| 2La inversion (2L) | 2 | 2La-specific                                       |
| 3La inversion (3L) | 2 | (merus, quadriannulatus) -- unexpected             |

---

## Part I: Trees

### 1. IQ-TREE 3

    iqtree3 -S data/alignments -B 1000 --prefix tutorial_loci -T AUTO -st DNA

Output: `tutorial_loci.treefile`

### Label and root as NEXUS (requires `ete3`)

    python tools/make_nexus_treeset.py \
        --alignments-dir data/alignments/ \
        --treefile tutorial_loci.treefile \
        --out tutorial_loci.nex \
        --outgroup An_christyi

Install ete3 first if needed: `pip install ete3` or `conda install -c etetoolkit ete3`
Output: `tutorial_loci.nex`

### 2. BEAST X (locus X_dist_04)

**BEAUti** -- File > Import Data > `data/alignments/X_dist_04.fasta`

| Tab       | Setting                                              |
|-----------|------------------------------------------------------|
| Sites     | HKY, Empirical, Gamma, 4 cats, codon partition off   |
| Clocks    | Strict clock                                         |
| Trees     | Coalescent: Constant Size                            |
| States    | defaults                                             |
| Priors    | defaults                                             |
| Operators | defaults                                             |
| MCMC      | chain 5,000,000, echo 10,000, log 1,000, stem X_dist_04 |

File > Generate BEAST File > `X_dist_04.xml`

**Run:**

    beast -beagle -overwrite X_dist_04.xml

**Tracer** -- File > Import Trace File > `precomputed/beast/X_dist_04.log`
Check: ESS ~4000, "hairy caterpillar" trace.

**TreeAnnotator:**

    treeannotator -burnin 500 -heights median \
        precomputed/beast/X_dist_04.trees X_dist_04.MCC.tre

**SplitsTree DensiTree** -- File > Open > `X_dist_04.trees`,
then Tree > Show DensiTree

**SplitsTree Consensus Outline** -- with the same file loaded,
Network > Consensus Outline

### 3. ASTRAL

    java -jar astral.5.7.8.jar \
        -i tutorial_loci.treefile \
        -o tutorial_loci.ASTRAL_species_tree.tre

Re-root output on `An_christyi`.

---

## Part II: Networks

### 4. SplitsTree Neighbor-Net

File > Open > `data/alignments/X_dist_02.fasta` (computes p-distances + Neighbor-Net automatically).
Side bar > Taxa Filter > deactivate `An_christyi`.

Compare across categories:

- `X_dist_02` (species tree)
- `auto_3R_02` (introgressed)
- `Inv_2La_02` (2La-specific)
- `Inv_3La_02` (unexpected)

### 5. PhyloSketch

- Click: place taxon. Drag: connect to another.
- Convert internal node to reticulation, then connect second parent.
- Double-click to rename. File > Save As > `.psketch`.

Start from the species tree:

    ((((arabiensis, quadriannulatus), (gambiae, coluzzii)), melas), merus);

Add reticulations for:

- `(gambiae, coluzzii)` -> `arabiensis`  [autosomal evidence]
- `merus` <-> `quadriannulatus`  [3La evidence]
- bidirectional flow involving 2La  [2La evidence]

### 6. PhyloParallelograms

1. File > Open > `tutorial_loci.nex`
2. Try subsets:
    - all 15 trees
    - X-distal only (5)
    - autosomal only (5)
    - 2La only (2)
    - 3La only (2)
    - mixed (X-distal + 3La, etc.)
3. Compare reticulation count and topology with your PhyloSketch sketch.

---

## Files at a glance

| File                                      | Made by         | Used by                       |
|-------------------------------------------|-----------------|-------------------------------|
| `data/alignments/*.fasta`                 | repo            | IQ-TREE, BEAST X, Neighbor-Net|
| `tutorial_loci.treefile`                  | IQ-TREE         | ASTRAL, helper script         |
| `tutorial_loci.nex`                       | helper script   | SplitsTree, PhyloParallelograms      |
| `X_dist_04.xml`                           | BEAUti          | BEAST X                       |
| `X_dist_04.log`, `X_dist_04.trees`        | BEAST X         | Tracer, TreeAnnotator         |
| `X_dist_04.MCC.tre`                       | TreeAnnotator   | tree viewer                   |
| `tutorial_loci.ASTRAL_species_tree.tre`   | ASTRAL          | tree viewer                   |
| `precomputed/beast/X_dist_04.{log,trees}` | repo (fallback) | Tracer, TreeAnnotator         |

## Pipeline

    data/alignments/*.fasta
        |
        +--> [IQ-TREE]    --> tutorial_loci.treefile --> [helper] --> tutorial_loci.nex
        |                                                                |
        |                                       +------------------------+
        |                                       |
        |                                       +--> [SplitsTree: view]
        |                                       +--> [PhyloParallelograms]
        |
        +--> [SplitsTree: Neighbor-Net per alignment]
        |
        +--> [BEAUti] --> X_dist_04.xml --> [BEAST X] --> X_dist_04.{log,trees}
                                                              |
                                                              +--> [Tracer: convergence]
                                                              +--> [TreeAnnotator] --> X_dist_04.MCC.tre
                                                              +--> [SplitsTree: DensiTree, Consensus Outline]

    tutorial_loci.treefile --> [ASTRAL] --> tutorial_loci.ASTRAL_species_tree.tre
