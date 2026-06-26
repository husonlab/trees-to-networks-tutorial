# From Trees to Networks -- Hands-On Guide

**ISMB 2026 Tutorial IP3**
Daniel H. Huson, Anupam Gautam, Banu Cetinkaya
University of Tubingen

This guide contains the hands-on steps for the tutorial. The accompanying slide deck covers the biological background, conceptual material, and discussion. Use the two together: follow the slides for the "why", follow this guide for the "what to type".

A note on commands: all shell commands assume you are inside the tutorial repository:

    git clone https://github.com/husonlab/trees-to-networks-tutorial.git
    cd trees-to-networks-tutorial

All file paths below are relative to that directory.

---

## Schedule

| Time          | Section                                              |
|---------------|------------------------------------------------------|
| 09:00 - 09:15 | Setup verification                                   |
| 09:15 - 09:35 | 1. IQ-TREE 3 hands-on                                |
| 09:35 - 10:15 | 2. BEAST X + SplitsTree posterior visualization      |
| 10:15 - 10:35 | 3. ASTRAL hands-on                                   |
| 10:35 - 10:50 | Discussion                                           |
| 10:50 - 11:10 | Coffee break                                         |
| 11:10 - 11:30 | 4. SplitsTree Neighbor-Net hands-on                  |
| 11:30 - 12:00 | 5. PhyloSketch hands-on                              |
| 12:00 - 12:35 | 6. PhyloParallelograms hands-on                             |
| 12:35 - 13:00 | Biological interpretation and wrap-up                |

---

## Setup verification

Before the tutorial starts, run through this checklist. If any item fails, please flag one of the presenters or a TA -- we will get you running before the hands-on starts.

- [ ] Repository cloned: `git clone https://github.com/husonlab/trees-to-networks-tutorial.git`
- [ ] `iqtree3 --version` works
- [ ] `java -jar /path/to/astral.5.7.8.jar -h` works
- [ ] `beauti` launches
- [ ] SplitsTree launches
- [ ] `tracer` launches
- [ ] PhyloSketch launches
- [ ] PhyloParallelograms launches
- [ ] PhyloGuide URL bookmarked

The dataset is already in the repository under `data/alignments/`. You do NOT need to rebuild it from the raw MAF file -- the scripts in `data-prep/` are for reproducibility only.

---

## Part I: Trees

The goal of Part I is to produce gene trees from each of our 15 loci and a species tree from the set, and to observe that the gene trees disagree systematically across the genome.

### 1. IQ-TREE 3 hands-on

**Time budget: 20 minutes**
**Goal: produce 15 maximum-likelihood gene trees, one per locus.**

#### 1.1 Run IQ-TREE in per-locus mode

From the repository root:

    iqtree3 -S data/alignments -B 1000 --prefix tutorial_loci -T AUTO -st DNA

Flags:

| Flag                     | What it does                                                       |
|--------------------------|--------------------------------------------------------------------|
| `-S data/alignments`     | Per-locus mode: one tree per FASTA file in the directory           |
| `-B 1000`                | Ultrafast bootstrap, 1000 replicates                               |
| `--prefix tutorial_loci` | Output filename prefix                                             |
| `-T AUTO`                | Auto-pick number of threads                                        |
| `-st DNA`                | Force DNA mode (auto-detection fails on some loci)                 |

Internally this runs ModelFinder per locus, then maximum-likelihood tree search, then UFBoot for branch support. Expected runtime: about 5 seconds.

#### 1.2 Check the output

You should see one block of output per locus, ending like this:

    Subset Type   Seqs   Sites   Infor   Invar   Model   Name
    1      DNA    7      6208    144     5068            X_dist_01.fasta
    2      DNA    7      7530    234     5899            X_dist_02.fasta
    ...
    15     DNA    7      5454    105     4455            inv_3La_02.fasta

What is normal:

- All 15 loci have 7 sequences.
- Most loci pick `HKY+F+G4` as the best-fit model.
- An. christyi (the outgroup) failing composition chi2 tests in several loci is not a problem.

The main output file is `tutorial_loci.treefile` -- a Newick file with one gene tree per line, in alphabetical order of the input FASTA filenames.

#### 1.3 Convert to a labelled, rooted NEXUS tree set

`tutorial_loci.treefile` has unnamed, unrooted trees. For downstream use in SplitsTree and PhyloParallelograms we want each tree labelled by its locus ID and rooted on the outgroup (An_christyi).

Run our helper script (requires `ete3`; install with `pip install ete3` or `conda install -c etetoolkit ete3`):

    python tools/make_nexus_treeset.py \
        --alignments-dir data/alignments/ \
        --treefile tutorial_loci.treefile \
        --out tutorial_loci.nex \
        --outgroup An_christyi

This produces `tutorial_loci.nex` -- the NEXUS file we will use repeatedly in Parts I and II.

#### 1.4 Inspect the gene trees in SplitsTree

1. Launch SplitsTree.
2. File > Open > select `tutorial_loci.nex`.
3. You should see 15 named trees in the tree-set panel.

Discussion (we will come back to these):

- Do all loci show the same topology? Why not?
- Can you tell X-distal loci apart from autosomal ones just by topology?
- Where in the genome would you expect to see "species-tree" signal vs "introgressed" signal?

---

### 2. BEAST X + SplitsTree posterior visualization

**Time budget: 30 minutes**
**Goal: produce a posterior tree distribution for one locus, then visualize the within-locus uncertainty as a network.**

We will run BEAST X on a single locus, `X_dist_04`, chosen because it is clean and Bayesian convergence is fast (4,872 bp, X-distal Xag region, expected to show the true species topology).

#### 2.1 Set up the analysis in BEAUti

1. Launch **BEAUti** (from your BEAST X installation).
2. **File > Import Data** > `data/alignments/X_dist_04.fasta`
3. **Sites** tab:
    - Substitution Model: **HKY**
    - Base frequencies: **Empirical**
    - Site Heterogeneity Model: **Gamma**
    - Number of Gamma Categories: **4**
    - Partition into codon positions: **off**
4. **Clocks** tab:
    - Clock Type: **Strict clock**
5. **Trees** tab:
    - Tree Prior: **Coalescent: Constant Size**
    - (Appropriate for the within-genus timescale.)
6. **States** tab: nothing to change.
7. **Priors** tab: leave at defaults.
8. **Operators** tab: leave at defaults.
9. **MCMC** tab:
    - Length of chain: **5,000,000** (short for live demo; production runs would use 20M)
    - Echo state to screen every: **10,000**
    - Log parameters every: **1,000** (gives 5,000 samples)
    - File name stem: **X_dist_04**
10. **File > Generate BEAST File**, save as `X_dist_04.xml`.

#### 2.2 Run BEAST X

In a terminal:

    beast -beagle -overwrite X_dist_04.xml

Expected runtime: about 2-3 minutes on Apple Silicon with BEAGLE. Leave it running in the background and continue with step 2.3 while it works.

#### 2.3 Inspect a precomputed run in Tracer (while yours runs)

Your live run is producing `X_dist_04.log` (parameter trace) and `X_dist_04.trees` (sampled trees), but it is not done yet. To see what good convergence looks like now, open the precomputed long run from the repository:

1. Launch **Tracer**.
2. **File > Import Trace File** > `precomputed/beast/X_dist_04.log`.
3. Check: effective sample size (ESS) should be nearly 4000 -- "good".
4. Check: trace plot should look like a "hairy caterpillar" -- well-mixed.

#### 2.4 Summarize the posterior with TreeAnnotator

We have a distribution of trees but often want one summary tree. TreeAnnotator computes the Maximum Clade Credibility (MCC) tree -- the tree from the posterior whose clades collectively have the highest product of posterior support.

    treeannotator -burnin 500 -heights median \
        precomputed/beast/X_dist_04.trees X_dist_04.MCC.tre

Flags:

| Flag                    | What it does                                              |
|-------------------------|-----------------------------------------------------------|
| `-burnin 500`           | Discard the first 500 trees                               |
| `-heights median`       | Use median node heights for branch lengths                |

The output `X_dist_04.MCC.tre` is a single tree with posterior probabilities annotated on each internal node.

By the time you reach this step, your live BEAST run from step 2.2 should be done. If you would like, replace `precomputed/beast/X_dist_04.trees` with your own `X_dist_04.trees`.

#### 2.5 Visualize the full posterior in SplitsTree

DensiTree overlay of all 5,000 posterior trees:

1. Open **SplitsTree**.
2. **File > Open** > `X_dist_04.trees` (the full posterior).
3. **Tree > Show DensiTree** to overlay all trees.

#### 2.6 Your first network: consensus outline from the posterior

With the same posterior tree set still loaded in SplitsTree:

- **Network** menu > **Consensus Outline**.

This produces a network with splits weighted by posterior support (counts). Parallelograms in this network indicate where the posterior is uncertain -- an *implicit network of within-locus uncertainty*.

---

### 3. ASTRAL hands-on

**Time budget: 20 minutes**
**Goal: compute a coalescent species tree from the 15 gene trees and confront ASTRAL's confident answer with what we know about the biology.**

#### 3.1 Run ASTRAL

ASTRAL takes a set of gene trees and returns a single species tree that maximizes quartet agreement under the multispecies coalescent. It models ILS but NOT introgression.

    java -jar astral.5.7.8.jar \
        -i tutorial_loci.treefile \
        -o tutorial_loci.ASTRAL_species_tree.tre

(Adjust the path to your `astral.5.7.8.jar` as needed.) Output: a species tree with quartet support values at each internal node.

#### 3.2 Inspect and re-root

ASTRAL's output is unrooted. Re-root on `An_christyi` for biological interpretation. You can do this in SplitsTree or your viewer of choice.

#### 3.3 The key observation

- The X-distal gene trees give the `(arabiensis, quadriannulatus)` topology -- the true species branching order.
- The autosomal gene trees and ASTRAL's output show the *introgression-driven* topology.
- ASTRAL gave us a confident answer that is biologically wrong.
- ASTRAL is not broken: its model (MSC, ILS only) cannot represent introgression.

This sets up Part II.

---

## Part II: Networks

In Part II we look at the same data through three network lenses, each addressing a different layer of conflict.

### 4. SplitsTree Neighbor-Net hands-on

**Time budget: 20 minutes**
**Goal: visualize conflicting signal directly in the alignment data, before any gene tree is computed.**

We will walk through one alignment together, then you load 2-3 more from different categories and compare.

#### 4.1 Walk through together: X_dist_02

1. In SplitsTree, **File > Open** > `data/alignments/X_dist_02.fasta`.
   SplitsTree will compute p-distances and run Neighbor-Net.
2. Use the **Taxa Filter** item (side bar) to deactivate the outgroup `An_christyi` so the in-group structure is easier to read.

#### 4.2 Open other alignments and explore

Repeat the same workflow on alignments from different categories. Our 15 loci span:

| Region                       | Loci | Expected topology                                       |
|------------------------------|------|---------------------------------------------------------|
| X distal (Xag inversion)     | 5    | `(arabiensis, quadriannulatus)` -- species tree         |
| X pericentromeric            | 1    | `(arabiensis, (gambiae, coluzzii))` -- introgressed     |
| Autosomal (2R, 3R)           | 5    | `(arabiensis, (gambiae, coluzzii))` -- introgressed     |
| 2La inversion (2L)           | 2    | 2La-specific topologies                                 |
| 3La inversion (3L)           | 2    | `(merus, quadriannulatus)` -- unexpected introgression  |

Suggested triples to compare:

- `X_dist_02` -- species tree
- `auto_3R_02` -- introgressed
- `Inv_2La_02` -- 2La-specific topology
- `Inv_3La_02` -- unexpected introgression

#### 4.3 What you should see

- **X-distal alignments**: smaller parallelograms; closer to tree-like.
- **Autosomal alignments**: more parallelograms involving arabiensis and the (gambiae, coluzzii) clade.
- **2La inversion alignments**: distinctive boxes reflecting trans-specific polymorphism.
- **3La inversion alignments**: parallelograms grouping merus with quadriannulatus.

The big picture: the conflict pattern we saw in IQ-TREE gene trees is also visible directly in alignment data.

---

### 5. PhyloSketch hands-on

**Time budget: 20 minutes**
**Goal: build, by hand, a phylogenetic network that captures your best hypothesis about Anopheles evolution given everything we have seen.**

The pedagogical idea is to translate observed patterns into a biological hypothesis before letting any algorithm infer one.

#### 5.1 PhyloSketch in 90 seconds

- Launch PhyloSketch.
- Drawing leaves and branches: click to place taxa, drag to connect them.
- Building a tree: connect leaves through internal nodes.
- Adding a reticulation: convert an internal node to a reticulation node, then connect a second parent edge to it.
- Editing labels: double-click to rename.
- Saving: **File > Save As** > `.psketch` file.

#### 5.2 Step 1: start from the species tree

From X-distal loci, the species tree is:

    ((((arabiensis, quadriannulatus), (gambiae, coluzzii)), melas), merus);

with `An_christyi` as outgroup. Sketch this in PhyloSketch first.

#### 5.3 Step 2: add reticulation nodes for hypothesized introgression

Events to consider:

| Event                                                          | Evidence in our data                                                                            |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Introgression from `(gambiae, coluzzii)` into `arabiensis`     | Autosomal gene trees show arabiensis grouped with (gambiae, coluzzii) instead of quadriannulatus|
| Introgression between `merus` and `quadriannulatus`            | 3La inversion gene trees show `(merus, quadriannulatus)` sister                                 |
| Bidirectional gene flow involving the 2La inversion            | 2La inversion gene trees show distinctive non-species-tree topologies                           |

#### 5.4 Step 3: decide which events to include

- A minimal network has 1 reticulation.
- A richer network might have 2 or 3.
- Trade-off: every reticulation must be justified by evidence.

**Save your sketch** -- you will compare it to PhyloParallelograms's automated inference in the next section.

---

### 6. PhyloParallelograms hands-on

**Time budget: 25 minutes**
**Goal: compute an explicit reticulation network from your 15 gene trees and explore how different subsets of trees yield different networks.**

PhyloParallelograms uses the PhyloFusion algorithm (Zhang, Cetinkaya, Huson 2026) to compute a network that displays all input trees with as few reticulations as possible. Each reticulation in the output is a hypothesized event -- matching a hybridization, introgression, or other gene-flow event.

#### 6.1 Open the tree set

1. Launch **PhyloParallelograms**.
2. **File > Open** > `tutorial_loci.nex` (the NEXUS tree set we created after IQ-TREE; it contains all 15 gene trees with their locus IDs).
3. PhyloParallelograms lists all 15 trees in the tree-set panel. By default the first trees are combined into a network.

#### 6.2 Explore different subsets of trees

The point of the tool is interactive comparison. Try the following subsets and see how the network changes:

- All 15 trees together.
- X-distal loci only (5 trees).
- Autosomal loci only (5 trees).
- 2La inversion loci only (2 trees).
- 3La inversion loci only (2 trees).
- Mixed subsets, e.g. X-distal + autosomal, X-distal + 3La.

For each, note: how many reticulations? Which lineages are involved? Does the underlying tree topology change?

#### 6.3 Compare with your PhyloSketch network

Open your saved sketch from PhyloSketch alongside the PhyloParallelograms network and compare:

- Same number of reticulations?
- Same reticulation events (same pairs of lineages involved)?
- Same direction of gene flow (if your sketch indicated direction)?

---

## Wrap-up

### Take-aways

1. Gene trees disagree systematically across the genome when introgression is pervasive. This is data, not noise.
2. Tree-summary methods can be confidently wrong when the underlying biology is reticulate. ASTRAL got the "wrong" species tree from our data -- not because it is broken, but because its model does not represent introgression.
3. Networks make the conflict visible, in three complementary ways: alignment-level (Neighbor-Net), within-locus uncertainty (consensus from posterior), and across-locus reticulation (PhyloParallelograms).
4. Hypothesis sketching before automated inference clarifies what you are looking for and makes the algorithm's output interpretable.
5. AI assistance (PhyloGuide) is useful for orientation and recommendations but should not replace expert judgment.

### Where to go next

- Tutorial repository (everything we did today, re-runnable on your own data): <https://github.com/husonlab/trees-to-networks-tutorial>
- SplitsTree: <https://github.com/husonlab/splitstree6>
- PhyloSketch: <https://github.com/husonlab/phylosketch2>
- PhyloParallelograms: <https://github.com/husonlab/phyloparallelograms>
- IQ-TREE: <http://www.iqtree.org>
- BEAST X: <https://beast.community>
- ASTRAL: <https://github.com/smirarab/ASTRAL>
- Further reading: see `References.md` in the repository.
