# From Trees to Networks

*ISMB 2026 Tutorial IP3 — Daniel H. Huson, Anupam Gautam and Banu Cetinkaya. Version July 11, 2026.*

Converted from PowerPoint (111 slides). Each section below shows the rendered slide followed by its extracted text.

## Contents

1. [From Trees to Networks](#slide-1)
2. [Your presenters today](#slide-2)
3. [What we’ll do today (09:00 to 13:00)](#slide-3)
4. [Agenda](#slide-4)
5. [Agenda](#slide-5)
6. [Dataset: the Anopheles gambiae complex](#slide-6)
7. [Dataset: the Anopheles gambiae complex](#slide-7)
8. [Dataset: the Anopheles gambiae complex](#slide-8)
9. [What is introgression?](#slide-9)
10. [Six species, one complex](#slide-10)
11. [The same dataset, two different trees](#slide-11)
12. [Key findings (Fontaine et al, 2015)](#slide-12)
13. [Tutorial data: 15 loci sampled to show the story](#slide-13)
14. [Software for trees and networks](#slide-14)
15. [What we will do today](#slide-15)
16. [Agenda](#slide-16)
17. [Quick setup verification](#slide-17)
18. [Agenda](#slide-18)
19. [From sequences to gene trees to species trees](#slide-19)
20. [At a single locus](#slide-20)
21. [Inferring a tree by maximum likelihood](#slide-21)
22. [Inferring a distribution of trees by Bayesian inference](#slide-22)
23. [Genome-scale data: many loci, many gene trees](#slide-23)
24. [Why do gene trees disagree?](#slide-24)
25. [Cause #1 of discordance: incomplete lineage sorting (ILS)](#slide-25)
26. [Cause #2 of discordance: introgression](#slide-26)
27. [Telling ILS and introgression apart](#slide-27)
28. [Now: let’s try to see this in our data](#slide-28)
29. [PhyloGuide Q1](#slide-29)
30. [Agenda](#slide-30)
31. [Hands-on: per-locus ML inference with IQ-TREE 3](#slide-31)
32. [(untitled)](#slide-32)
33. [Run the IQ-TREE 3 command](#slide-33)
34. [Run the IQ-TREE 3 command](#slide-34)
35. [Nexus file for SplitsTree and PhyloParallelograms](#slide-35)
36. [Open the gene trees in SplitsTree and look around](#slide-36)
37. [Discussion items](#slide-37)
38. [PhyloGuide Q2](#slide-38)
39. [Agenda](#slide-39)
40. [Hands-on: Bayesian inference + visualizing the posterior](#slide-40)
41. [From “best tree” to “distribution of trees”](#slide-41)
42. [We’ll run BEAST X on a single locus: X_dist_04](#slide-42)
43. [BEAUti: import data and set substitution model](#slide-43)
44. [BEAUti: import data and set substitution model](#slide-44)
45. [BEAUti: clock model and tree prior](#slide-45)
46. [BEAUti: clock model and tree prior](#slide-46)
47. [BEAUti: clock model and tree prior](#slide-47)
48. [MCMC settings, generate XML, and start BEAST](#slide-48)
49. [MCMC settings, generate XML, and start BEAST](#slide-49)
50. [Inspect a precomputed run in Tracer (while yours runs)](#slide-50)
51. [Inspect a precomputed run in Tracer (while yours runs)](#slide-51)
52. [Inspect a precomputed run in Tracer (while yours runs)](#slide-52)
53. [Summarize the posterior with TreeAnnotator](#slide-53)
54. [Summarize the posterior with TreeAnnotator](#slide-54)
55. [Visualizing the full posterior: DensiTree in SplitsTree](#slide-55)
56. [Your first network: consensus outline from the posterior](#slide-56)
57. [Agenda](#slide-57)
58. [Hands-on: coalescent species tree with ASTRAL](#slide-58)
59. [What does ASTRAL tell us?](#slide-59)
60. [ASTRAL Is misled by autosomal introgression](#slide-60)
61. [Part I recap: from sequences to trees](#slide-61)
62. [PhyloGuide Q3](#slide-62)
63. [After the break: Making conflict explicit](#slide-63)
64. [🎉 COFFEE BREAK 🎉](#slide-64)
65. [Agenda](#slide-65)
66. [Part II: Networks and cross-locus reticulation](#slide-66)
67. [Split networks](#slide-67)
68. [Building a split network from distances](#slide-68)
69. [Two roles for networks: implicit and explicit](#slide-69)
70. [Rooted phylogenetic networks](#slide-70)
71. [Two roles for networks: implicit and explicit](#slide-71)
72. [Explicit reticulation: where two lineages meet](#slide-72)
73. [You have already computed a network](#slide-73)
74. [From gene trees to a reticulate network](#slide-74)
75. [Our three network views today](#slide-75)
76. [Agenda](#slide-76)
77. [Hands-on: Neighbor-Net on the 15 alignments](#slide-77)
78. [Neighbor-Net on our alignments](#slide-78)
79. [Let’s do one together: X_dist_02](#slide-79)
80. [Let’s do one together: X_dist_02](#slide-80)
81. [Open other alignments and explore](#slide-81)
82. [Open other alignments and explore](#slide-82)
83. [Compare with trees in Fontaine et al (2015)](#slide-83)
84. [Compare with trees in Fontaine et al (2015)](#slide-84)
85. [Compare with trees in Fontaine et al (2015)](#slide-85)
86. [What did you see?](#slide-86)
87. [Agenda](#slide-87)
88. [And what’s next?](#slide-88)
89. [Hands-on: sketch a hypothesis network in PhyloSketch](#slide-89)
90. [PhyloSketch in 90 seconds](#slide-90)
91. [Your target network: Fontaine et al. Fig 1C](#slide-91)
92. [(untitled)](#slide-92)
93. [(untitled)](#slide-93)
94. [Build your hypothesis network](#slide-94)
95. [Agenda](#slide-95)
96. [PhyloGuide Q4](#slide-96)
97. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-97)
98. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-98)
99. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-99)
100. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-100)
101. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-101)
102. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-102)
103. [(untitled)](#slide-103)
104. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-104)
105. [How does the parallelogram compare to what you sketched?](#slide-105)
106. [PhyloGuide Q5](#slide-106)
107. [Agenda](#slide-107)
108. [Back to the biology: what did this tell us about malaria](#slide-108)
109. [Take-aways from the tutorial](#slide-109)
110. [Thank you - and please give us feedback](#slide-110)
111. [(untitled)](#slide-111)

---

<a id="slide-1"></a>

## Slide 1 — From Trees to Networks

![Slide 1](images/slide-001.jpg)

ISMB 2026 Tutorial IP3  
Daniel H. Huson, Anupam Gautam and Banu Cetinkaya  
Version July 11, 2026  
Institute for Bioinformatics  
and Medical Informatics  

---

<a id="slide-2"></a>

## Slide 2 — Your presenters today

![Slide 2](images/slide-002.jpg)

Anupam Gautam  
Post-Doc  
University of Tübingen  
Max-Planck Institute for Biology Tübingen  
PhyloGuide, AI-assisted phylogenetic analysis  
Daniel Huson  
Professor of Algorithms in Bioinformatics  
University of Tübingen  
Phylogenetic networks, SplitsTree, PhyloSketch, PhyloParallelograms  
Banu Cetinkaya  
PhD student  
University of Tübingen  
Phylogenetic networks,  co-developer of PhyloParallelograms  

---

<a id="slide-3"></a>

## Slide 3 — What we’ll do today (09:00 to 13:00)

![Slide 3](images/slide-003.jpg)

09:00 - 10:50  Trees  
Per-locus inference with IQ-TREE and BEAST X  
Coalescent species tree with ASTRAL  
“We have many gene trees and they disagree”  
10:50 - 11:10 / Break ☕️  
11:10 - 13:00  Networks  
SplitsTree & Neighbor-Net on alignments  
PhyloSketch for interactive network construction  
PhyloParallelograms for networks from gene tree sets  

---

<a id="slide-4"></a>

## Slide 4 — Agenda

![Slide 4](images/slide-004.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-5"></a>

## Slide 5 — Agenda

![Slide 5](images/slide-005.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-6"></a>

## Slide 6 — Dataset: the Anopheles gambiae complex

![Slide 6](images/slide-006.jpg)

Image: Alan R Walker (Wikipedia)  

---

<a id="slide-7"></a>

## Slide 7 — Dataset: the Anopheles gambiae complex

![Slide 7](images/slide-007.jpg)

Why public health cares:  
Three of six species are the principal vectors of P. falciparum malaria  
How did they acquire vectorial capacity?  
Can phylogeny help understand the disease  

Malaria parasite connecting to a red blood cell  
NIAID, Wikipedia  

---

<a id="slide-8"></a>

## Slide 8 — Dataset: the Anopheles gambiae complex

![Slide 8](images/slide-008.jpg)

Major introgression events  
Fontaine et al (Fig 1C, 2015)  
Why phylogenetics cares:  
Six closely related species, recently diverged  (about 2 Mya)  
Pervasive autosomal introgression  
X chromosome tells a different story than autosomes  
Several different discordance signals  

---

<a id="slide-9"></a>

## Slide 9 — What is introgression?

![Slide 9](images/slide-009.jpg)

Two species can occasionally hybridize — mate and produce offspring.  
If hybrids repeatedly backcross into one parent, DNA from the other becomes permanently incorporated.  

---

<a id="slide-10"></a>

## Slide 10 — Six species, one complex

![Slide 10](images/slide-010.jpg)

Anopheles gambiae (vector)  
An. coluzzii (vector)  
An. arabiensis (vector)  
An. quadriannulatus (non-vector)  
An. melas (minor vector, brackish)  
An. merus (minor vector, brackish)  

An. christyi (outgroup)  
Fontaine et al (Fig 1A, 2015)  

---

<a id="slide-11"></a>

## Slide 11 — The same dataset, two different trees

![Slide 11](images/slide-011.jpg)

(X chromosome tree)  

Fontaine et al (Fig 1B, 2015)  

v  
v  
v  

Vectors do not form a clade  
Vectors form a clade  
Both trees 100% bootstrap support, which is “correct”?  

---

<a id="slide-12"></a>

## Slide 12 — Key findings (Fontaine et al, 2015)

![Slide 12](images/slide-012.jpg)

The X-chromosome tree is the species tree  
higher divergence between sister pairs confirms the branching order.  
Autosomes are pervasively introgressed between  
An. arabiensis and (An. gambiae + An. coluzzii).  
Vectorial capacity may have spread by introgression, not only de novo mutation.  

---

<a id="slide-13"></a>

## Slide 13 — Tutorial data: 15 loci sampled to show the story

![Slide 13](images/slide-013.jpg)

| Region | Loci | Expected topology |  
| --- | --- | --- |  
| X distal (Xag inversion) | 5 | (arabiensis, quadriannulatus) - species tree |  
| X pericentromeric | 1 | (arabiensis, (gambiae, coluzzii)) - introgressed |  
| Autosomal (2R, 3R) | 5 | (arabiensis, (gambiae, coluzzii)) - introgressed |  
| 2La inversion (2L) | 2 | 2La-specific topologies |  
| 3La inversion (3L) | 2 | (merus, quadriannulatus) - unexpected introgression |  

https://targetmalaria.org  
Names such as 2La or 3La refer to specific chromosomal inversions  

---

<a id="slide-14"></a>

## Slide 14 — Software for trees and networks

![Slide 14](images/slide-014.jpg)

Each tool does one job; together they form the workflow.  
Throughout  
PhyloGuide  
		AI assistant  
Part II (networks)  
SplitsTree  
	Consensus networks,  
	Neighbor-Net  
PhyloSketch  
	interactive sketching  
PhyloParallelograms  
     gene-trees-to-network  
Part I (trees)  
IQ-TREE 3  
	per-locus ML  
BEAST X  
	Bayesian inference  
BEAUti,  
Tracer,  
TreeAnnotator  
ASTRAL  
	MSC species tree  

---

<a id="slide-15"></a>

## Slide 15 — What we will do today

![Slide 15](images/slide-015.jpg)

When the genome is pervasively introgressed, tree methods can be confidently wrong. Networks make the conflict visible.  
Part I: infer gene trees and a species tree from a multi-locus alignment — and see them disagree across the genome.  
Part II: use phylogenetic networks to visualize and interpret that disagreement.  

---

<a id="slide-16"></a>

## Slide 16 — Agenda

![Slide 16](images/slide-016.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-17"></a>

## Slide 17 — Quick setup verification

![Slide 17](images/slide-017.jpg)

☐ Repository cloned:  
git clone https://github.com/husonlab/trees-to-networks-tutorial.git  
☐ iqtree3 --version works  
☐ astral –help or java -jar /path/to/astral.5.7.8.jar -h works  
☐ beauti and beast launch  
☐ SplitsTree launches  
☐ tracer launches  
☐ PhyloSketch launches  
☐ PhyloParallelograms launches  
☐ PhyloGuide URL bookmarked  

---

<a id="slide-18"></a>

## Slide 18 — Agenda

![Slide 18](images/slide-018.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-19"></a>

## Slide 19 — From sequences to gene trees to species trees

![Slide 19](images/slide-019.jpg)

Sequences  

Alignments  

Gene trees  

Species tree  

Discordance among trees  

Discordance among trees  

---

<a id="slide-20"></a>

## Slide 20 — At a single locus

![Slide 20](images/slide-020.jpg)

Input: a multiple sequence alignment (MSA) — 7 species, ~5000 nt, every column informative.  
From the MSA we infer a gene tree: the history of this one stretch of DNA.  

---

<a id="slide-21"></a>

## Slide 21 — Inferring a tree by maximum likelihood

![Slide 21](images/slide-021.jpg)

Probability of alignment A given tree T and model M:  
P(A | T, M )  
Find the tree and model that maximize it — with IQ-TREE 3.  
Substitution models (JC, K2P, HKY, GTR, +G, +I) describe how nucleotides change.  
Bootstrap (UFBoot) assesses confidence in the tree.  
Theory: Felsenstein (1981)  
Implementation: IQ-TREE 3 (2026)  
Enhancements: ModelFinder (2017), UFBoot2 (2018)  

---

<a id="slide-22"></a>

## Slide 22 — Inferring a distribution of trees by Bayesian inference

![Slide 22](images/slide-022.jpg)

Bayesian inference estimates the full posterior  
P(T, M | A),  
not just one best tree.  
Tool: BEAST X (MCMC) — thousands of trees, each weighted by posterior probability.  
Captures uncertainty.  
Theory: Yang & Rannala (1997)  
Implementation: Baele et al. (2025)  

---

<a id="slide-23"></a>

## Slide 23 — Genome-scale data: many loci, many gene trees

![Slide 23](images/slide-023.jpg)

Phylogenomics: hundreds to thousands of loci, each with its own history.  
Run ML or Bayesian inference per locus → a set of gene trees.  
Our tutorial: 15 loci, 15 gene trees.  

---

<a id="slide-24"></a>

## Slide 24 — Why do gene trees disagree?

![Slide 24](images/slide-024.jpg)

24  

---

<a id="slide-25"></a>

## Slide 25 — Cause #1 of discordance: incomplete lineage sorting (ILS)

![Slide 25](images/slide-025.jpg)

Ancestral polymorphism can persist across several species  
Different alleles sort into different lineages, so the gene tree can differ from the species tree  
A stochastic  process — no gene flow  
col  
ara  
gam  
species tree  
one gene tree  
other gene tree  

---

<a id="slide-26"></a>

## Slide 26 — Cause #2 of discordance: introgression

![Slide 26](images/slide-026.jpg)

Major introgression events  
Fontaine et al (Fig 1C, 2015)  
After speciation, gene flow (hybridization or HGT) can reintroduce alleles  
Introgressed alleles resemble the donor, not the closest relative  
Often non-uniform across the genome  
A biological process  

---

<a id="slide-27"></a>

## Slide 27 — Telling ILS and introgression apart

![Slide 27](images/slide-027.jpg)

Both ILS and introgression make gene trees disagree with the species tree.  
ILS: unsorted alleles are ancestral → coalesce deep in the species tree.  
Introgression: alleles came recently from a sister species → coalesce shallow.  
This is how Fontaine et al. (2015) showed Anopheles autosomes are introgressed, not just ILS.  

---

<a id="slide-28"></a>

## Slide 28 — Now: let’s try to see this in our data

![Slide 28](images/slide-028.jpg)

15 loci across the X chromosome, autosomes, and inversions.  
Run IQ-TREE on each → 15 gene trees.  
We expect discordance — the question is where?  

---

<a id="slide-29"></a>

## Slide 29 — PhyloGuide Q1

![Slide 29](images/slide-029.jpg)

Q: We have multi-locus alignments from a recently diverged species complex. How should we infer a species phylogeny?  

A: Infer gene trees for each locus, then estimate a species tree with ASTRAL instead of relying only on concatenation. This accounts for gene-tree discordance caused by ILS.  

---

<a id="slide-30"></a>

## Slide 30 — Agenda

![Slide 30](images/slide-030.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-31"></a>

## Slide 31 — Hands-on: per-locus ML inference with IQ-TREE 3

![Slide 31](images/slide-031.jpg)

Time budget: ~20 minutes  
Goal: 15 ML gene trees, one per locus — see how they vary across the genome.  
cd trees-to-networks-tutorial  
Run: iqtree3 -S data/alignments/ ...  (see next slide)  

3  

---

<a id="slide-32"></a>

## Slide 32

![Slide 32](images/slide-032.jpg)

The IQ-TREE 3 command  
iqtree3 -S data/alignments -B 1000 --prefix tutorial_loci -T AUTO -st DNA  
| Flag | What it does |  
| --- | --- |  
| -S data/alignments | Per-locus mode: one tree per FASTA in this directory |  
| -B 1000 | Ultrafast bootstrap with 1000 replicates |  
| --prefix tutorial\_loci | Output filename prefix |  
| -T AUTO | Auto-pick number of threads |  
| -st DNA | Force DNA mode (auto-detection fails on some loci) |  

---

<a id="slide-33"></a>

## Slide 33 — Run the IQ-TREE 3 command

![Slide 33](images/slide-033.jpg)

Run the command.  
Internally: ModelFinder picks a model per locus, then ML tree search, then UFBoot support.  
Runtime ~5 s. Output: tutorial_loci.treefile  

---

<a id="slide-34"></a>

## Slide 34 — Run the IQ-TREE 3 command

![Slide 34](images/slide-034.jpg)

You’ll see one block of output per locus, ending like this:  
Subset  Type   Seqs   Sites  Infor  Invar  Model  Name1   DNA    7  6208   144    5068      X_dist_01.fasta2   DNA    7  7530   234    5899      X_dist_02.fasta...  
15	DNA	7	5454	105	4455		inv_3La_02.fasta  
What’s normal:  
All 15 loci have 7 sequences; most pick HKY+F+G4  
An. christyi (the outgroup) failing composition chi2 tests in several loci is not a problem  

---

<a id="slide-35"></a>

## Slide 35 — Nexus file for SplitsTree and PhyloParallelograms

![Slide 35](images/slide-035.jpg)

IQ-TREE wrote 15 Newick trees to tutorial_loci.treefile, one per line in alphabetical order of FASTA filenames  
For SplitsTree and PhyloParallelograms, we want a NEXUS file with each tree labeled by its locus ID and correctly rooted by outgroup An_christyi  
Run our helper:  
python tools/make_nexus_treeset.py \  
    --alignments-dir data/alignments/ \  
    --treefile tutorial_loci.treefile \  
    --out tutorial_loci.nex \  
         --outgroup An_christyi  

---

<a id="slide-36"></a>

## Slide 36 — Open the gene trees in SplitsTree and look around

![Slide 36](images/slide-036.jpg)

Open tutorial_loci.nex in SplitsTree  
File -> Open -> select the .nex file  
What you should see: 15 named trees in the tree set  

---

<a id="slide-37"></a>

## Slide 37 — Discussion items

![Slide 37](images/slide-037.jpg)

Do all loci show the same topology? Why not?  
Can you tell apart X-distal from autosomal loci just by topology?  
Where in the genome would you expect to see "species-tree" signal vs "introgressed" signal, based on what we know about this dataset?  

---

<a id="slide-38"></a>

## Slide 38 — PhyloGuide Q2

![Slide 38](images/slide-038.jpg)

Q: We ran IQ-TREE on 15 alignments and the gene trees disagree across chromosomes - X chromosome shows one topology, autosomes another. What does this mean?  

A: Different genomic regions can have different evolutionary histories due to ILS, introgression, selection, or gene-tree error. It does not mean one topology is necessarily correct.  

---

<a id="slide-39"></a>

## Slide 39 — Agenda

![Slide 39](images/slide-039.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-40"></a>

## Slide 40 — Hands-on: Bayesian inference + visualizing the posterior

![Slide 40](images/slide-040.jpg)

Time budget: 30 minutes  
Goal: build a posterior tree distribution for one locus, then visualize within-locus uncertainty as a network.  
Tools: BEAST X, BEAUti, Tracer, TreeAnnotator, SplitsTree  
Locus: X_dist_04 (a clean X-distal alignment)  

---

<a id="slide-41"></a>

## Slide 41 — From “best tree” to “distribution of trees”

![Slide 41](images/slide-041.jpg)

What ML gave us (IQ-TREE):  
One tree per locus, with bootstrap support  
Discordance ACROSS loci  
What Bayesian gives us (BEAST X):  
A posterior distribution of trees per locus — uncertainty WITHIN a locus  
Summarize as one tree, or visualize the full distribution  

---

<a id="slide-42"></a>

## Slide 42 — We’ll run BEAST X on a single locus: X_dist_04

![Slide 42](images/slide-042.jpg)

Locus: chrX:9,845,592–9,849,716 (4,872 bp), X-distal Xag region  
Expected topology: (arabiensis, quadriannulatus) sister, christyi outgroup; model HKY+F+G4.  
Why this locus: clean signal, fast convergence, the true-species-tree topology — one locus keeps the demo short.  

---

<a id="slide-43"></a>

## Slide 43 — BEAUti: import data and set substitution model

![Slide 43](images/slide-043.jpg)

Launch BEAUti (from BEAST X installation)  
File -> Import Data ->  data/alignments/X_dist_04.fasta  

---

<a id="slide-44"></a>

## Slide 44 — BEAUti: import data and set substitution model

![Slide 44](images/slide-044.jpg)

Sites tab:  
Substitution Model: HKY  
Base frequencies: Empirical  
Site Heterogeneity Model: Gamma  
Number of Gamma Categories: 4  
Partition into codon positions: off  

---

<a id="slide-45"></a>

## Slide 45 — BEAUti: clock model and tree prior

![Slide 45](images/slide-045.jpg)

Clocks tab:  
Clock Type: Strict clock  

---

<a id="slide-46"></a>

## Slide 46 — BEAUti: clock model and tree prior

![Slide 46](images/slide-046.jpg)

Trees tab:  
Tree Prior: Coalescent: Constant Size  
This is appropriate for the within-genus timescale  

---

<a id="slide-47"></a>

## Slide 47 — BEAUti: clock model and tree prior

![Slide 47](images/slide-047.jpg)

States tab: nothing to change  
Priors tab: leave at defaults  
Operators tab: leave at defaults  

---

<a id="slide-48"></a>

## Slide 48 — MCMC settings, generate XML, and start BEAST

![Slide 48](images/slide-048.jpg)

MCMC tab:  
Length of chain: 5,000,000 (short for live demo; production runs would use 20M)  
Echo state to screen every: 10,000  
Log parameters every: 1000 (gives 5,000 samples)  
File name stem: X_dist_04  

---

<a id="slide-49"></a>

## Slide 49 — MCMC settings, generate XML, and start BEAST

![Slide 49](images/slide-049.jpg)

File -> Generate BEAST File -> save as X_dist_04.xml  
Run BEAST X immediately in a terminal:  
beast -beagle -overwrite X_dist_04.xml  
Expected runtime: about 2-3 minutes on Apple Silicon with BEAGLE  
Let it run in the background. We will come back to it later.  

---

<a id="slide-50"></a>

## Slide 50 — Inspect a precomputed run in Tracer (while yours runs)

![Slide 50](images/slide-050.jpg)

Your live run is writing X_dist_04.log and X_dist_04.trees, but is not done yet  
To see good convergence now, open the precomputed run:  
Tracer  
File -> Import Trace File  
-> precomputed/beast/X_dist_04.log  

---

<a id="slide-51"></a>

## Slide 51 — Inspect a precomputed run in Tracer (while yours runs)

![Slide 51](images/slide-051.jpg)

Effective sample size is good  
(nearly 4000)  

---

<a id="slide-52"></a>

## Slide 52 — Inspect a precomputed run in Tracer (while yours runs)

![Slide 52](images/slide-052.jpg)

Sampling looks good  
(“hairy caterpillar”)  

---

<a id="slide-53"></a>

## Slide 53 — Summarize the posterior with TreeAnnotator

![Slide 53](images/slide-053.jpg)

We have a distribution of trees but often want one summary tree  
TreeAnnotator computes the Maximum Clade Credibility (MCC) tree: the tree from the posterior whose clades collectively have the highest product of posterior support  
treeannotator -burnin 500 -heights median \  
    precomputed/beast/X_dist_04.trees X_dist_04.MCC.tre  
| -burnin 500 | Discard first 500 trees |  
| --- | --- |  
| -heights median | use median node heights for branch lengths |  
| precomputed/beast/X\_dist\_04.trees | Input trees |  
| X\_dist\_04.MCC.tre | one tree with posterior probabilities annotated on each internal node |  

---

<a id="slide-54"></a>

## Slide 54 — Summarize the posterior with TreeAnnotator

![Slide 54](images/slide-054.jpg)

Open in SplitsTree:  

MCC keeps (arabiensis, quadriannulatus) and (coluzzii, gambiae) — the species signal — but the deep backbone (melas, merus) is poorly resolved.  

Fontaine et al (Fig 1B, 2015)  

---

<a id="slide-55"></a>

## Slide 55 — Visualizing the full posterior: DensiTree in SplitsTree

![Slide 55](images/slide-055.jpg)

By the time you see this slide, your live BEAST run should be done.  
Open X_dist_04.trees in SplitsTree (the full posterior, 5000 trees)  
Tree -> Show DensiTree to overlay all trees  

---

<a id="slide-56"></a>

## Slide 56 — Your first network: consensus outline from the posterior

![Slide 56](images/slide-056.jpg)

In SplitsTree, with the same posterior tree set loaded:  
Network menu > Consensus Outline  
Network with splits weighted by posterior support (counts)  

Here:  
Boxes= posterior uncertainty, not hybridization.  

---

<a id="slide-57"></a>

## Slide 57 — Agenda

![Slide 57](images/slide-057.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-58"></a>

## Slide 58 — Hands-on: coalescent species tree with ASTRAL

![Slide 58](images/slide-058.jpg)

ASTRAL: for a set of gene trees, returns a single species tree that maximizes quartet agreement under the multispecies coalescent      (it models ILS but NOT introgression)  
Input: tutorial_loci.treefile (output of IQ-TREE)  
Command:  
 java -jar astral.5.7.8.jar \  
    -i tutorial_loci.treefile \  
    -o tutorial_loci.ASTRAL_species_tree.tre  

Species tree with quartet support values at each internal node  
Maddison (1997), ASTRAL-III (Zhang et al., 2018)  

---

<a id="slide-59"></a>

## Slide 59 — What does ASTRAL tell us?

![Slide 59](images/slide-059.jpg)

Open the ASTRAL output in  SplitsTree and reroot using An_christyi as outgroup:  

Fontaine et al (Fig 1B, 2015)  
This is the introgressed phylogeny: An. arabiensis sister of (An. gambiae and An. coluzzii)  

---

<a id="slide-60"></a>

## Slide 60 — ASTRAL Is misled by autosomal introgression

![Slide 60](images/slide-060.jpg)

The X-distal gene trees give the (arabiensis, quadriannulatus) topology — the true species branching order (Fontaine 2015).  
The autosomal trees and ASTRAL give the introgression-driven topology instead.  
ASTRAL gave a confident answer that is probably biologically wrong.  
It is not broken — MSC models ILS only, and cannot represent the introgression in our data.  

---

<a id="slide-61"></a>

## Slide 61 — Part I recap: from sequences to trees

![Slide 61](images/slide-061.jpg)

15 alignments  

ASTRAL  

species tree  

IQ-TREE3  

15 gene trees  

Tree distribution  

SplitsTree  

X_dist_04  

BEAST X  

Densi-Tree  

Consensus network  

TreeAnnotator  

MCC tree  

---

<a id="slide-62"></a>

## Slide 62 — PhyloGuide Q3

![Slide 62](images/slide-062.jpg)

Q: When is a tree inadequate? When do we need a network?  

A: A tree is inadequate when evolution is not strictly branching, such as with hybridization, introgression, HGT, or strong conflicting signal. Networks capture mixed ancestry and conflicting histories.  

---

<a id="slide-63"></a>

## Slide 63 — After the break: Making conflict explicit

![Slide 63](images/slide-063.jpg)

Part II preview:  
SplitsTree Neighbor-Net: networks of conflicting splits in the alignment data  
PhyloSketch: build a hypothesis network interactively  
PhyloParallelograms: networks inferred from the gene trees - and SEE the introgression  
Break: 20 minutes, then 11:10 reconvene  

---

<a id="slide-64"></a>

## Slide 64 — 🎉 COFFEE BREAK 🎉

![Slide 64](images/slide-064.jpg)

☕️  
☕️  
🍪  
🎉 20 minutes 🎉  

---

<a id="slide-65"></a>

## Slide 65 — Agenda

![Slide 65](images/slide-065.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-66"></a>

## Slide 66 — Part II: Networks and cross-locus reticulation

![Slide 66](images/slide-066.jpg)

Where we left off:  
15 gene trees disagree; ASTRAL's confident “species” tree is the introgression-driven one, not the true one.  
The data carry a non-tree-like signal.  
What we will do next:  
Three network views, each with a different tool — to see the introgression, not just infer it.  

---

<a id="slide-67"></a>

## Slide 67 — Split networks

![Slide 67](images/slide-067.jpg)

A split partitions the taxa into two sets; each tree edge is a split.  
A tree's splits are all compatible.  
A split network can show incompatible splits — any two produce a box.  

---

<a id="slide-68"></a>

## Slide 68 — Building a split network from distances

![Slide 68](images/slide-068.jpg)

Input: Pairwise distances  
Neighbor-Net extends Neighbor-Joining, retaining conflicting evidence as boxes  
Output: a split network approximating the distances  

Bryant & Moulton (2004)  

---

<a id="slide-69"></a>

## Slide 69 — Two roles for networks: implicit and explicit

![Slide 69](images/slide-069.jpg)

1. Implicit networks – data display networks  
Show conflicting signal without claiming specific events — “here is conflict”, not its cause.  
Example: split networks — for exploration and detecting non-tree-like signal.  

---

<a id="slide-70"></a>

## Slide 70 — Rooted phylogenetic networks

![Slide 70](images/slide-070.jpg)

A rooted tree: one root, leaves are taxa, internal nodes are inferred ancestors.  
A network generalizes this — internal nodes can have more than one parent (reticulation nodes).  
It captures both vertical inheritance and events where lineages combine or exchange DNA.  

---

<a id="slide-71"></a>

## Slide 71 — Two roles for networks: implicit and explicit

![Slide 71](images/slide-071.jpg)

2. Explicit networks – explicit evolutionary scenario  
Represent specific events — hybridization, introgression, HGT — as reticulation nodes.  
“These two parent lineages produced this hybrid.”  
Example: PhyloFusion output.  

---

<a id="slide-72"></a>

## Slide 72 — Explicit reticulation: where two lineages meet

![Slide 72](images/slide-072.jpg)

A reticulation node = genetic material from two parent lineages combining into one descendant.  
May correspond to:  
Hybridization, introgression, horizontal gene transfer, or recombination  
A network can have several reticulation nodes — one per event.  

---

<a id="slide-73"></a>

## Slide 73 — You have already computed a network

![Slide 73](images/slide-073.jpg)

In Part I, the consensus network from the BEAST X posterior was an implicit network:  
Splits weighted by posterior probability; boxes where it is uncertain (within-locus).  
Today we compute several more, viewing our 15 gene trees from different angles.  

---

<a id="slide-74"></a>

## Slide 74 — From gene trees to a reticulate network

![Slide 74](images/slide-074.jpg)

PhyloFusion takes rooted trees and computes an explicit network.  
It displays all input trees with as few reticulations as possible.  
Each reticulation is a hypothesized event explaining the disagreement.  
PhyloParallelograms: choose which trees to include and display.  

Zhang, Cetinkaya, Huson (2026)  

---

<a id="slide-75"></a>

## Slide 75 — Our three network views today

![Slide 75](images/slide-075.jpg)

1. SplitsTree Neighbor-Net on alignments (20 min) — implicit split network; see raw conflict in the data.  
2. PhyloSketch interactive sketching (20 min) — hand-draw a hypothesis network from your intuition.  
3. PhyloParallelograms on the gene trees (30 min) — explicit reticulation network (PhyloFusion); see the introgression.  

---

<a id="slide-76"></a>

## Slide 76 — Agenda

![Slide 76](images/slide-076.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-77"></a>

## Slide 77 — Hands-on: Neighbor-Net on the 15 alignments

![Slide 77](images/slide-077.jpg)

Time budget: 20 minutes  
Goal: see conflicting signal directly in alignment data, before any gene tree (SplitsTree).  
Plan: run Neighbor-Net on one alignment together, then each load 2–3 more from other categories and compare.  

---

<a id="slide-78"></a>

## Slide 78 — Neighbor-Net on our alignments

![Slide 78](images/slide-078.jpg)

We use Neighbor-Net (SplitsTree) to compute split networks for our 15 alignments  
Question: do they all look the same? Where are the boxes?  
| Region | Loci | Expected topology |  
| --- | --- | --- |  
| X distal (Xag inversion) | 5 | (arabiensis, quadriannulatus) - species tree |  
| X pericentromeric | 1 | (arabiensis, (gambiae, coluzzii)) - introgressed |  
| Autosomal (2R, 3R) | 5 | (arabiensis, (gambiae, coluzzii)) - introgressed |  
| 2La inversion (2L) | 2 | 2La-specific topologies |  
| 3La inversion (3L) | 2 | (merus, quadriannulatus) - unexpected introgression |  

---

<a id="slide-79"></a>

## Slide 79 — Let’s do one together: X_dist_02

![Slide 79](images/slide-079.jpg)

Open file data/alignments/X_dist_02.fasta in SplitsTree  
This will run p-distances and Neighbor-Net  

---

<a id="slide-80"></a>

## Slide 80 — Let’s do one together: X_dist_02

![Slide 80](images/slide-080.jpg)

Open file data/alignments/X_dist_02.fasta in SplitsTree  
Use the Taxa Filter item (side bar) to deactivate the outgroup:  

---

<a id="slide-81"></a>

## Slide 81 — Open other alignments and explore

![Slide 81](images/slide-081.jpg)

Repeat the same workflow on alignments from different categories:  

| Region | Loci | Expected topology |  
| --- | --- | --- |  
| X distal (Xag inversion) | 5 | (arabiensis, quadriannulatus) - species tree |  
| X pericentromeric | 1 | (arabiensis, (gambiae, coluzzii)) - introgressed |  
| Autosomal (2R, 3R) | 5 | (arabiensis, (gambiae, coluzzii)) - introgressed |  
| 2La inversion (2L) | 2 | 2La-specific topologies |  
| 3La inversion (3L) | 2 | (merus, quadriannulatus) - unexpected introgression |  

---

<a id="slide-82"></a>

## Slide 82 — Open other alignments and explore

![Slide 82](images/slide-082.jpg)

X_dist_02  
“species tree”  
auto_3R_02  
“introgressed”  
Inv_2La_02  
“2La-specific topologies”  

---

<a id="slide-83"></a>

## Slide 83 — Compare with trees in Fontaine et al (2015)

![Slide 83](images/slide-083.jpg)

(X chromosome tree)  

Fontaine et al (Fig 1B, 2015)  
X_dist_02  
“species tree”  
auto_3R_02  
“introgressed”  

---

<a id="slide-84"></a>

## Slide 84 — Compare with trees in Fontaine et al (2015)

![Slide 84](images/slide-084.jpg)

(X chromosome tree)  

Fontaine et al (Fig 1B, 2015)  

X_dist_02  
“species tree”  
auto_3R_02  
“introgressed”  

---

<a id="slide-85"></a>

## Slide 85 — Compare with trees in Fontaine et al (2015)

![Slide 85](images/slide-085.jpg)

(X chromosome tree)  

Fontaine et al (Fig 1B, 2015)  
Inv_2La_02  
“2La-specific topologies”  
Inv_3La_02  
“unexpected introgression”  

---

<a id="slide-86"></a>

## Slide 86 — What did you see?

![Slide 86](images/slide-086.jpg)

Across the categories you should have seen:  
X-distal: smaller boxes, closer to tree-like  
Autosomal: more boxes around An. arabiensis and (gambiae, coluzzii)  
2La / 3La inversions: distinctive boxes (3La groups An. merus with       An. quadriannulatus)  

---

<a id="slide-87"></a>

## Slide 87 — Agenda

![Slide 87](images/slide-087.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-88"></a>

## Slide 88 — And what’s next?

![Slide 88](images/slide-088.jpg)

Neighbor-Net gives an implicit network — it flags conflict.  
Next we build an explicit network by hand, drawing reticulation nodes for specific hypothesized events.  
This is the “phylogenetic sketching” workflow.  

---

<a id="slide-89"></a>

## Slide 89 — Hands-on: sketch a hypothesis network in PhyloSketch

![Slide 89](images/slide-089.jpg)

Time budget: 20 minutes  
Goal: hand-build a network capturing your best hypothesis for Anopheles evolution.  
Tool: PhyloSketch (Huson, 2025)  
Idea: turn the patterns you saw in gene trees and Neighbor-Nets into a biological hypothesis, drawn as an explicit network.  
Scaffold: use Fontaine et al. Fig 1C (next slide) as your target — aim to reproduce its main reticulations.  

---

<a id="slide-90"></a>

## Slide 90 — PhyloSketch in 90 seconds

![Slide 90](images/slide-090.jpg)

Launch PhyloSketch  
Draw: click to place taxa, drag to connect them  
Tree: connect leaves through internal nodes  
Reticulation: convert an internal node, then add a second parent edge  
Edit node label using context menu  
Save: File → Save As → .psketch  

---

<a id="slide-91"></a>

## Slide 91 — Your target network: Fontaine et al. Fig 1C

![Slide 91](images/slide-091.jpg)

Major introgression events  
Fontaine et al (Fig 1C, 2015)  

---

<a id="slide-92"></a>

## Slide 92

![Slide 92](images/slide-092.jpg)

Build your hypothesis network  
Events to consider:  
Step 1: Start from the species tree we believe is correct  
From X-distal loci, the species tree is:  
((((arabiensis,quadriannulatus), (gambiae, coluzzii)),melas),merus);  
with christyi as outgroup. Sketch this in PhyloSketch first.  
Step 2: Add reticulation nodes for hypothesized introgression  
| Event | Evidence in our data |  
| --- | --- |  
| Introgression from (gambiae, coluzzii) into An. arabiensis | Autosomal gene trees show An. arabiensis grouped with (gambiae, coluzzii) instead of An. quadriannulatus |  
| Introgression between An. merus and An. quadriannulatus | 3La inversion gene trees show (merus, quadriannulatus) sister |  

---

<a id="slide-93"></a>

## Slide 93

![Slide 93](images/slide-093.jpg)

Build your hypothesis network  
Step 3: Decide which events to include  
A minimal network has 1 reticulation  
A richer network might have 2 or 3  
Trade-off: every reticulation must be justified by evidence  

---

<a id="slide-94"></a>

## Slide 94 — Build your hypothesis network

![Slide 94](images/slide-094.jpg)

To create a transfer edge, declare an edge as “acceptor”:  

---

<a id="slide-95"></a>

## Slide 95 — Agenda

![Slide 95](images/slide-095.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-96"></a>

## Slide 96 — PhyloGuide Q4

![Slide 96](images/slide-096.jpg)

Q: We want to infer an explicit reticulation network from a set of gene trees, with the minimum number of reticulations needed to display all the trees. What method should we use?  

A: Use a minimum-hybridization network method, which finds the smallest number of reticulation events explaining all gene trees. Check ILS first because it can mimic reticulation.  

---

<a id="slide-97"></a>

## Slide 97 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 97](images/slide-097.jpg)

Time budget: 30 minutes  
Goal: show your 15 gene trees on an underlying network and see directly where they share history and where they conflict  
Interactively add and remove trees and watch the agreement and conflict change  
Big question: where does the conflict concentrate, and does it match the network you sketched in PhyloSketch?  

(paper submitted)  

---

<a id="slide-98"></a>

## Slide 98 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 98](images/slide-098.jpg)

PhyloParallelograms  
A phylogenetic parallelogram draws several rooted gene trees together based on an underlying network  
Where the trees agree, their branches run together as parallel bands; where they conflict, the branches split apart  
The underlying network displays all trees and minimizes reticulations – computed using the PhyloFusion algorithm            													     (Zhang, Cetinkaya, Huson 2026)  

---

<a id="slide-99"></a>

## Slide 99 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 99](images/slide-099.jpg)

Launch PhyloParallelograms  
File → Open → tutorial_loci.nex (the 15 gene trees with locus IDs)  
It lists all 15 trees; by default the first two are combined into a network.  
Explore different sets of trees to compare.  

---

<a id="slide-100"></a>

## Slide 100 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 100](images/slide-100.jpg)

Two X-distal loci (X_dist_01, X_dist_02). The two trees run together almost everywhere, and the underlying network needs just one reticulation (h=1) — these loci tell nearly the same story, close to the true species history. (h = reticulations in the network.)  

---

<a id="slide-101"></a>

## Slide 101 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 101](images/slide-101.jpg)

The point of the tool is interactive comparison. Try the following subsets and see how the network changes:  
The X-distal loci only (5 trees).  
The inversion loci only (4 trees).  
All 15 trees together.  
Different mixed subsets of trees.  

---

<a id="slide-102"></a>

## Slide 102 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 102](images/slide-102.jpg)

All five X-distal loci. Mostly parallel: the X chromosome carries the species branching order (with h=1)  

---

<a id="slide-103"></a>

## Slide 103

![Slide 103](images/slide-103.jpg)

Hands-on PhyloParallelograms: understanding gene trees through their network  
Four inversion loci (2La, 3La). The lines now diverge, especially around An. arabiensis, An. quadriannulatus and An. merus, and the network jumps to h=5. Fewer trees than the X set, but far more conflict — these are the introgression paths.  

---

<a id="slide-104"></a>

## Slide 104 — Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 104](images/slide-104.jpg)

All 15 gene trees at once. Maximum divergence across the genome, the underlying network at h=7 — the whole pattern, concordant X against introgressed autosomes and inversions, in a single network.  

---

<a id="slide-105"></a>

## Slide 105 — How does the parallelogram compare to what you sketched?

![Slide 105](images/slide-105.jpg)

Open your PhyloSketch sketch next to the PhyloParallelograms network on all 15 trees.  
Compare: Same number of reticulations? Same events (same lineage pairs)? Same direction of gene flow?  

---

<a id="slide-106"></a>

## Slide 106 — PhyloGuide Q5

![Slide 106](images/slide-106.jpg)

Q: We have a phylogenetic network for the Anopheles gambiae species complex with reticulations between An. arabiensis and the (An. gambiae, An. coluzzii) clade, and between An. merus and An. quadriannulatus. What does this tell us biologically?  

A: The reticulations suggest non-tree-like evolution, possibly due to historical gene flow/hybridization or ILS. Different loci may reflect different evolutionary histories across the genome.  

---

<a id="slide-107"></a>

## Slide 107 — Agenda

![Slide 107](images/slide-107.jpg)

Tutorial overview and dataset  
Setup verification  
Multi-locus phylogenomics lecture  
IQ-TREE 3 hands-on  
BEAST X + SplitsTree posterior visualization  
ASTRAL hands-on  
Networks lecture  
SplitsTree Neighbor-Net hands-on  
PhyloSketch hands-on  
PhyloParallelograms hands-on  
Biological interpretation + wrap-up  
☕️  

---

<a id="slide-108"></a>

## Slide 108 — Back to the biology: what did this tell us about malaria

![Slide 108](images/slide-108.jpg)

Species branching order: the X-chromosome topology is correct — An. arabiensis and An. quadriannulatus are sisters, not the three vectors.  
Pervasive autosomal introgression, especially between     An. arabiensis and the (An. gambiae, An. coluzzii) ancestor.  
Further introgression between An. merus and                     An. quadriannulatus in the 3La region.  
Implication: if introgression moves vector-capability traits, controlling one species may be undercut by introgression from another.  

---

<a id="slide-109"></a>

## Slide 109 — Take-aways from the tutorial

![Slide 109](images/slide-109.jpg)

Gene trees disagree systematically under pervasive introgression — this is data, not noise.  
Tree-summary methods can be confidently wrong: ASTRAL got the wrong species tree because it does not model introgression.  
Networks make the conflict visible: at the alignment level (Neighbor-Net), within-locus (consensus), and across loci (PhyloParallelograms).  
Sketching a hypothesis first makes the automated output interpretable.  
AI assistance (PhyloGuide) helps orient but does not replace expert judgment.  

---

<a id="slide-110"></a>

## Slide 110 — Thank you - and please give us feedback

![Slide 110](images/slide-110.jpg)

Thanks to:  
All of you for spending the morning with us  
The Anopheles genomics consortium and Fontaine et al. for the dataset used here  
The tool developers whose work underlies the tutorial (Minh lab, Suchard lab, Drummond lab, Rambaut lab, Mirarab lab, and our own group)  
ISCB for the tutorial program  
University of Tübingen for support  

---

<a id="slide-111"></a>

## Slide 111

![Slide 111](images/slide-111.jpg)

111  

---
