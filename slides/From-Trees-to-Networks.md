# From Trees to Networks

*ISMB 2026 Tutorial IP3: Daniel H. Huson, Anupam Gautam and Banu Cetinkaya. Version July 11, 2026.*

Converted from PowerPoint (111 slides). Each section shows the rendered slide followed by the speaker notes.

## Contents

1. [From Trees to Networks](#slide-1)
2. [Your presenters today](#slide-2)
3. [What we'll do today (09:00 to 13:00)](#slide-3)
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
28. [Now: let's try to see this in our data](#slide-28)
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
41. [From "best tree" to "distribution of trees"](#slide-41)
42. [We'll run BEAST X on a single locus: X_dist_04](#slide-42)
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
64. [COFFEE BREAK](#slide-64)
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
79. [Let's do one together: X_dist_02](#slide-79)
80. [Let's do one together: X_dist_02](#slide-80)
81. [Open other alignments and explore](#slide-81)
82. [Open other alignments and explore](#slide-82)
83. [Compare with trees in Fontaine et al (2015)](#slide-83)
84. [Compare with trees in Fontaine et al (2015)](#slide-84)
85. [Compare with trees in Fontaine et al (2015)](#slide-85)
86. [What did you see?](#slide-86)
87. [Agenda](#slide-87)
88. [And what's next?](#slide-88)
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
103. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-103)
104. [Hands-on PhyloParallelograms: understanding gene trees through their network](#slide-104)
105. [How does the parallelogram compare to what you sketched?](#slide-105)
106. [PhyloGuide Q5](#slide-106)
107. [Agenda](#slide-107)
108. [Back to the biology: what did this tell us about malaria](#slide-108)
109. [Take-aways from the tutorial](#slide-109)
110. [Thank you - and please give us feedback](#slide-110)
111. [Share your feedback](#slide-111)

---

<a id="slide-1"></a>

## Slide 1: From Trees to Networks

![Slide 1](images/slide-001.jpg)

**Notes:** Good morning, and welcome. Over the next four hours we travel from trees: clean and familiar: to networks, which we need once the genome stops behaving like a tree.

---

<a id="slide-2"></a>

## Slide 2: Your presenters today

![Slide 2](images/slide-002.jpg)

**Notes:** I'm Daniel. Anupam and Banu will circulate to help during the hands-on parts and each lead a section later: flag them if you get stuck.

---

<a id="slide-3"></a>

## Slide 3: What we'll do today (09:00 to 13:00)

![Slide 3](images/slide-003.jpg)

**Notes:** Here's the morning: Part I we infer trees, Part II we visualize their disagreement as networks, with a coffee break between. It's hands-on, so keep a laptop open.

---

<a id="slide-4"></a>

## Slide 4: Agenda

![Slide 4](images/slide-004.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-5"></a>

## Slide 5: Agenda

![Slide 5](images/slide-005.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-6"></a>

## Slide 6: Dataset: the Anopheles gambiae complex

![Slide 6](images/slide-006.jpg)

**Notes:** Our one running example is the Anopheles gambiae complex: six mosquito species, one of the best-studied malaria vector systems.

---

<a id="slide-7"></a>

## Slide 7: Dataset: the Anopheles gambiae complex

![Slide 7](images/slide-007.jpg)

**Notes:** Why public health cares: three of these six species are the main vectors of falciparum malaria, and we still don't fully know how they gained that capacity.

---

<a id="slide-8"></a>

## Slide 8: Dataset: the Anopheles gambiae complex

![Slide 8](images/slide-008.jpg)

**Notes:** Why we care phylogenetically: they diverged only about two million years ago, they've hybridized, and the X chromosome tells a different story from the autosomes.

---

<a id="slide-9"></a>

## Slide 9: What is introgression?

![Slide 9](images/slide-009.jpg)

**Notes:** Introgression, our key word: two species hybridize, and if the hybrids keep backcrossing into one parent, some of the other species' DNA becomes permanently built in.

---

<a id="slide-10"></a>

## Slide 10: Six species, one complex

![Slide 10](images/slide-010.jpg)

**Notes:** Here are the six species, plus christyi as outgroup. Notice the vectors don't form a clade: the first sign that something interesting is going on.

---

<a id="slide-11"></a>

## Slide 11: The same dataset, two different trees

![Slide 11](images/slide-011.jpg)

**Notes:** Fontaine and colleagues found the X chromosome and the rest of the genome give different trees: both with 100% bootstrap. Bootstrap isn't the problem; the conflict is biological.

---

<a id="slide-12"></a>

## Slide 12: Key findings (Fontaine et al, 2015)

![Slide 12](images/slide-012.jpg)

**Notes:** Their conclusion: the X tree is the species tree, the autosomes are pervasively introgressed between arabiensis and gambiae+coluzzii, and vectorial capacity may even have spread that way.

---

<a id="slide-13"></a>

## Slide 13: Tutorial data: 15 loci sampled to show the story

![Slide 13](images/slide-013.jpg)

**Notes:** We didn't hand you the whole genome: just fifteen loci, chosen so you'll meet every one of these topology categories in your own gene trees today.

---

<a id="slide-14"></a>

## Slide 14: Software for trees and networks

![Slide 14](images/slide-014.jpg)

**Notes:** A quick map of the software. Don't memorize it: the point is that each tool does one job, and together they make the whole workflow.

---

<a id="slide-15"></a>

## Slide 15: What we will do today

![Slide 15](images/slide-015.jpg)

**Notes:** The thesis for the day: when the genome is pervasively introgressed, trees can be confidently wrong, and networks make that conflict visible.

---

<a id="slide-16"></a>

## Slide 16: Agenda

![Slide 16](images/slide-016.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-17"></a>

## Slide 17: Quick setup verification

![Slide 17](images/slide-017.jpg)

**Notes:** Let's check everyone's setup against this list. If a tool won't launch, don't worry: we have precomputed outputs for every step, so you can always keep up.

---

<a id="slide-18"></a>

## Slide 18: Agenda

![Slide 18](images/slide-018.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-19"></a>

## Slide 19: From sequences to gene trees to species trees

![Slide 19](images/slide-019.jpg)

**Notes:** The modern workflow: sequences, aligned, each giving a gene tree, then summarized into a species tree. The catch is the gene trees disagree: and that's information, not noise.

---

<a id="slide-20"></a>

## Slide 20: At a single locus

![Slide 20](images/slide-020.jpg)

**Notes:** Start simple: one locus. One alignment, about 5,000 nucleotides, seven species: and we just want the history of this one stretch of DNA.

---

<a id="slide-21"></a>

## Slide 21: Inferring a tree by maximum likelihood

![Slide 21](images/slide-021.jpg)

**Notes:** IQ-TREE does this by maximum likelihood: find the tree and model that make the observed alignment most probable, with bootstrap for confidence. It's remarkably fast now.

---

<a id="slide-22"></a>

## Slide 22: Inferring a distribution of trees by Bayesian inference

![Slide 22](images/slide-022.jpg)

**Notes:** Sometimes one best tree isn't enough: we want the uncertainty. Bayesian inference with BEAST estimates the whole posterior: thousands of trees, each weighted by probability.

---

<a id="slide-23"></a>

## Slide 23: Genome-scale data: many loci, many gene trees

![Slide 23](images/slide-023.jpg)

**Notes:** Now scale up to many loci: hundreds or thousands, fifteen for us. Run inference per locus and you get a set of gene trees, each with its own history.

---

<a id="slide-24"></a>

## Slide 24: Why do gene trees disagree?

![Slide 24](images/slide-024.jpg)

**Notes:** And here's the fact we have to explain: on the same seven species, different parts of the genome give different trees. Why?

---

<a id="slide-25"></a>

## Slide 25: Cause #1 of discordance: incomplete lineage sorting (ILS)

![Slide 25](images/slide-025.jpg)

**Notes:** First cause, incomplete lineage sorting: ancestral variation sorts randomly into descendants, so gene trees can differ from the species tree with no gene flow at all. This is our null.

---

<a id="slide-26"></a>

## Slide 26: Cause #2 of discordance: introgression

![Slide 26](images/slide-026.jpg)

**Notes:** Second cause, introgression: after species split, gene flow moves alleles across the boundary, so those genes carry a donor-like history. Real biology, and often patchy.

---

<a id="slide-27"></a>

## Slide 27: Telling ILS and introgression apart

![Slide 27](images/slide-027.jpg)

**Notes:** How to tell them apart? Timing. ILS alleles are ancestral and coalesce deep; introgressed alleles arrived recently and coalesce shallow: that's how Fontaine showed introgression here.

---

<a id="slide-28"></a>

## Slide 28: Now: let's try to see this in our data

![Slide 28](images/slide-028.jpg)

**Notes:** That's the theory: now let's open our terminals and look for it in the data.

---

<a id="slide-29"></a>

## Slide 29: PhyloGuide Q1

![Slide 29](images/slide-029.jpg)

**Notes:** A PhyloGuide checkpoint: how should we infer a species tree from many loci? Infer gene trees, then use ASTRAL, which accounts for ILS, rather than concatenation alone.

---

<a id="slide-30"></a>

## Slide 30: Agenda

![Slide 30](images/slide-030.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-31"></a>

## Slide 31: Hands-on: per-locus ML inference with IQ-TREE 3

![Slide 31](images/slide-031.jpg)

**Notes:** Our first hands-on: fifteen ML gene trees, one per locus. Make sure your terminal is inside the cloned repo. Remember, each program here has just one job.

---

<a id="slide-32"></a>

## Slide 32

![Slide 32](images/slide-032.jpg)

**Notes:** The command is short. The key flag is -S: analyze every alignment separately: fifteen independent trees, not one concatenated one. The rest sets bootstraps, threads, and DNA mode.

---

<a id="slide-33"></a>

## Slide 33: Run the IQ-TREE 3 command

![Slide 33](images/slide-033.jpg)

**Notes:** Run it. Internally: ModelFinder picks a model per locus, then the ML search, then bootstrap: all in about five seconds. Still amazes me.

---

<a id="slide-34"></a>

## Slide 34: Run the IQ-TREE 3 command

![Slide 34](images/slide-034.jpg)

**Notes:** Don't close the terminal: look. Each locus picks its own model, usually HKY+F+G4, and they needn't match. christyi failing a composition test on a few loci is fine.

---

<a id="slide-35"></a>

## Slide 35: Nexus file for SplitsTree and PhyloParallelograms

![Slide 35](images/slide-035.jpg)

**Notes:** One helper script before SplitsTree: it repackages the trees as a NEXUS set, labelled by locus and rooted on the outgroup. Nothing biological changes: just names and a root.

---

<a id="slide-36"></a>

## Slide 36: Open the gene trees in SplitsTree and look around

![Slide 36](images/slide-036.jpg)

**Notes:** Now open the trees in SplitsTree, just as a viewer, and scroll through. Some group arabiensis with quadriannulatus, others with gambiae and coluzzii: already, one tree isn't enough.

---

<a id="slide-37"></a>

## Slide 37: Discussion items

![Slide 37](images/slide-037.jpg)

**Notes:** A good moment to ask: can you tell which trees came from the X chromosome? Usually you'll spot one group of five that resemble each other.

---

<a id="slide-38"></a>

## Slide 38: PhyloGuide Q2

![Slide 38](images/slide-038.jpg)

**Notes:** A PhyloGuide checkpoint: the gene trees disagree across chromosomes: what does that mean? Different regions can have different histories; it doesn't mean one topology is simply correct.

---

<a id="slide-39"></a>

## Slide 39: Agenda

![Slide 39](images/slide-039.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-40"></a>

## Slide 40: Hands-on: Bayesian inference + visualizing the posterior

![Slide 40](images/slide-040.jpg)

**Notes:** Next thirty minutes: Bayesian inference on one locus, then we visualize the posterior as a network: your first network of the day, within a single locus.

---

<a id="slide-41"></a>

## Slide 41: From "best tree" to "distribution of trees"

![Slide 41](images/slide-041.jpg)

**Notes:** The bridge: ML gave us one tree per locus and disagreement across loci. Bayesian inference adds the uncertainty within a locus: a whole distribution of trees.

---

<a id="slide-42"></a>

## Slide 42: We'll run BEAST X on a single locus: X_dist_04

![Slide 42](images/slide-042.jpg)

**Notes:** We'll use one clean X-distal locus, X_dist_04. It isn't 'the' species tree: just a fast, clear example of what Bayesian inference produces.

---

<a id="slide-43"></a>

## Slide 43: BEAUti: import data and set substitution model

![Slide 43](images/slide-043.jpg)

**Notes:** Everything starts in BEAUti: think of it as an XML generator that builds the file BEAST will run. First, import the alignment.

---

<a id="slide-44"></a>

## Slide 44: BEAUti: import data and set substitution model

![Slide 44](images/slide-044.jpg)

**Notes:** In the Sites tab, set the model: HKY, empirical frequencies, gamma rates with four categories: the same choices IQ-TREE made automatically, now by hand.

---

<a id="slide-45"></a>

## Slide 45: BEAUti: clock model and tree prior

![Slide 45](images/slide-045.jpg)

**Notes:** Clocks tab: a strict clock, so every lineage evolves at the same rate. Fine for a demo at this timescale.

---

<a id="slide-46"></a>

## Slide 46: BEAUti: clock model and tree prior

![Slide 46](images/slide-046.jpg)

**Notes:** Trees tab: a constant-size coalescent prior. The prior says which trees are plausible before the data, and this one suits closely related species.

---

<a id="slide-47"></a>

## Slide 47: BEAUti: clock model and tree prior

![Slide 47](images/slide-047.jpg)

**Notes:** States, Priors, and Operators we leave at defaults: the choices that mattered were the clock and the tree prior.

---

<a id="slide-48"></a>

## Slide 48: MCMC settings, generate XML, and start BEAST

![Slide 48](images/slide-048.jpg)

**Notes:** MCMC tab: chain length five million. Nothing magic about the number: it just gives enough samples for a tutorial; real runs go far longer. Convergence is what matters.

---

<a id="slide-49"></a>

## Slide 49: MCMC settings, generate XML, and start BEAST

![Slide 49](images/slide-049.jpg)

**Notes:** Generate the XML, start BEAST now, and let it run in the background while we look at other results: real analysis often means several programs at once.

---

<a id="slide-50"></a>

## Slide 50: Inspect a precomputed run in Tracer (while yours runs)

![Slide 50](images/slide-050.jpg)

**Notes:** While yours runs, we open a precomputed long run in Tracer. Tracer teaches you to distrust a pretty tree until you've checked the chain converged.

---

<a id="slide-51"></a>

## Slide 51: Inspect a precomputed run in Tracer (while yours runs)

![Slide 51](images/slide-051.jpg)

**Notes:** First, effective sample size: how many independent samples we really have. We want comfortably above two hundred; here it's in the thousands.

---

<a id="slide-52"></a>

## Slide 52: Inspect a precomputed run in Tracer (while yours runs)

![Slide 52](images/slide-052.jpg)

**Notes:** Then the trace: good mixing looks boring: a steady 'hairy caterpillar', no trends or jumps. Once you've seen it, you'll always recognize it.

---

<a id="slide-53"></a>

## Slide 53: Summarize the posterior with TreeAnnotator

![Slide 53](images/slide-053.jpg)

**Notes:** To get one summary tree, TreeAnnotator builds the maximum clade credibility tree: the tree whose clades are collectively best supported, with posteriors on each branch.

---

<a id="slide-54"></a>

## Slide 54: Summarize the posterior with TreeAnnotator

![Slide 54](images/slide-054.jpg)

**Notes:** Notice this MCC keeps the two well-supported pairs: arabiensis+quadriannulatus and coluzzii+gambiae, the species signal: but the deep backbone with melas and merus stays unresolved from one short locus. So don't over-trust a single summary tree.

---

<a id="slide-55"></a>

## Slide 55: Visualizing the full posterior: DensiTree in SplitsTree

![Slide 55](images/slide-055.jpg)

**Notes:** The nicest view is all the trees at once. DensiTree overlays the whole posterior: edges agreeing with the consensus form dark bundles, conflicting ones show in red. Uncertainty made visible.

---

<a id="slide-56"></a>

## Slide 56: Your first network: consensus outline from the posterior

![Slide 56](images/slide-056.jpg)

**Notes:** Now a consensus network from the same posterior. Notice it's already a network: but here the boxes mean posterior uncertainty, not hybridization. Hold that distinction for Part II.

---

<a id="slide-57"></a>

## Slide 57: Agenda

![Slide 57](images/slide-057.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-58"></a>

## Slide 58: Hands-on: coalescent species tree with ASTRAL

![Slide 58](images/slide-058.jpg)

**Notes:** Back to all fifteen trees. ASTRAL takes gene trees and finds the species tree that best fits their quartets under the coalescent: it models ILS, and it's fast.

---

<a id="slide-59"></a>

## Slide 59: What does ASTRAL tell us?

![Slide 59](images/slide-059.jpg)

**Notes:** And the surprise: ASTRAL confidently returns the introgressed topology, with arabiensis sister to gambiae+coluzzii. It didn't fail: the biology just broke its assumptions.

---

<a id="slide-60"></a>

## Slide 60: ASTRAL Is misled by autosomal introgression

![Slide 60](images/slide-060.jpg)

**Notes:** This is the central slide. The X-distal trees give the true order; the autosomes and ASTRAL give the introgressed one. ASTRAL isn't broken: the coalescent models ILS, not introgression. Every method was confident; nature just asked a harder question.

---

<a id="slide-61"></a>

## Slide 61: Part I recap: from sequences to trees

![Slide 61](images/slide-061.jpg)

**Notes:** A quick recap of Part I: what each tool took in and produced: before the key slide.

---

<a id="slide-62"></a>

## Slide 62: PhyloGuide Q3

![Slide 62](images/slide-062.jpg)

**Notes:** A PhyloGuide checkpoint: when do we need a network? Whenever evolution isn't strictly branching: hybridization, introgression, HGT, or strong conflict: a network captures the mixed history.

---

<a id="slide-63"></a>

## Slide 63: After the break: Making conflict explicit

![Slide 63](images/slide-063.jpg)

**Notes:** After the break, three network views that make the conflict explicit. Please scan the feedback QR during the break: back at 11:10.

---

<a id="slide-64"></a>

## Slide 64: üéâ COFFEE BREAK üéâ

![Slide 64](images/slide-064.jpg)

**Notes:** Coffee break: back in twenty minutes.

---

<a id="slide-65"></a>

## Slide 65: Agenda

![Slide 65](images/slide-065.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-66"></a>

## Slide 66: Part II: Networks and cross-locus reticulation

![Slide 66](images/slide-066.jpg)

**Notes:** Welcome back. We left off with fifteen disagreeing trees and an ASTRAL tree that chose the introgression signal. Now, in Part II, we look at that conflict directly.

---

<a id="slide-67"></a>

## Slide 67: Split networks

![Slide 67](images/slide-067.jpg)

**Notes:** A little theory: each tree edge is a split of the taxa. A tree's splits are all compatible; a network can show incompatible ones: and every incompatible pair becomes a box.

---

<a id="slide-68"></a>

## Slide 68: Building a split network from distances

![Slide 68](images/slide-068.jpg)

**Notes:** Where do splits come from? A distance matrix from the alignment. Neighbor-Net extends Neighbor-Joining but keeps conflicting evidence as boxes instead of forcing a tree. The tool is SplitsTree.

---

<a id="slide-69"></a>

## Slide 69: Two roles for networks: implicit and explicit

![Slide 69](images/slide-069.jpg)

**Notes:** Two kinds of network. First, implicit: data-display networks that show conflict without claiming a cause. Split networks are the example, great for exploration.

---

<a id="slide-70"></a>

## Slide 70: Rooted phylogenetic networks

![Slide 70](images/slide-070.jpg)

**Notes:** A definition: a rooted tree has one root, taxa as leaves, ancestors inside. A network lets internal nodes have more than one parent: reticulation nodes: capturing lineages that combine.

---

<a id="slide-71"></a>

## Slide 71: Two roles for networks: implicit and explicit

![Slide 71](images/slide-071.jpg)

**Notes:** The second kind: explicit networks, where reticulation nodes stand for real events: hybridization, introgression, HGT. The network now proposes a specific scenario.

---

<a id="slide-72"></a>

## Slide 72: Explicit reticulation: where two lineages meet

![Slide 72](images/slide-072.jpg)

**Notes:** So a reticulation node means two parent lineages combined into one descendant: hybridization, introgression, HGT, or recombination: and a network can hold several, one per event.

---

<a id="slide-73"></a>

## Slide 73: You have already computed a network

![Slide 73](images/slide-073.jpg)

**Notes:** You've actually already built a network: the consensus outline from your BEAST posterior, an implicit one. The rest of Part II just changes the input and the network type.

---

<a id="slide-74"></a>

## Slide 74: From gene trees to a reticulate network

![Slide 74](images/slide-074.jpg)

**Notes:** Where we're headed: PhyloFusion takes rooted gene trees and computes an explicit network that displays all of them with as few reticulations as possible: each one a hypothesized event.

---

<a id="slide-75"></a>

## Slide 75: Our three network views today

![Slide 75](images/slide-075.jpg)

**Notes:** The plan: three views: Neighbor-Net from alignments, PhyloSketch from your intuition, and PhyloParallelograms from the gene trees. Each answers a slightly different question.

---

<a id="slide-76"></a>

## Slide 76: Agenda

![Slide 76](images/slide-076.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-77"></a>

## Slide 77: Hands-on: Neighbor-Net on the 15 alignments

![Slide 77](images/slide-077.jpg)

**Notes:** First view: Neighbor-Net, straight from the alignments: no gene trees needed. We'll do one together, then you each load a few more and compare.

---

<a id="slide-78"></a>

## Slide 78: Neighbor-Net on our alignments

![Slide 78](images/slide-078.jpg)

**Notes:** Here's the locus key to guide you. As you build networks, keep asking: do they all look alike? Where are the boxes?

---

<a id="slide-79"></a>

## Slide 79: Let's do one together: X_dist_02

![Slide 79](images/slide-079.jpg)

**Notes:** Let's do one together: open X_dist_02, and SplitsTree computes p-distances and a Neighbor-Net automatically.

---

<a id="slide-80"></a>

## Slide 80: Let's do one together: X_dist_02

![Slide 80](images/slide-080.jpg)

**Notes:** Use the Taxa Filter to switch off the christyi outgroup, so the network spreads out over the ingroup where the real conflict is.

---

<a id="slide-81"></a>

## Slide 81: Open other alignments and explore

![Slide 81](images/slide-081.jpg)

**Notes:** Now try loci from the other categories: species-tree, introgressed, inversion: and compare. Don't stop after one; the comparison is the whole point.

---

<a id="slide-82"></a>

## Slide 82: Open other alignments and explore

![Slide 82](images/slide-082.jpg)

**Notes:** A few examples across categories: X-distal, autosomal, and a 2La inversion: so you know what to expect: some almost tree-like, others with large boxes.

---

<a id="slide-83"></a>

## Slide 83: Compare with trees in Fontaine et al (2015)

![Slide 83](images/slide-083.jpg)

**Notes:** Line your networks up against the Fontaine trees: the X-distal one should look close to the species tree.

---

<a id="slide-84"></a>

## Slide 84: Compare with trees in Fontaine et al (2015)

![Slide 84](images/slide-084.jpg)

**Notes:** Same comparison: it's the X-distal versus autosomal contrast that's worth dwelling on.

---

<a id="slide-85"></a>

## Slide 85: Compare with trees in Fontaine et al (2015)

![Slide 85](images/slide-085.jpg)

**Notes:** The inversion loci tell their own stories: 3La tends to pull merus together with quadriannulatus.

---

<a id="slide-86"></a>

## Slide 86: What did you see?

![Slide 86](images/slide-086.jpg)

**Notes:** Pooling what we saw: X-distal small-boxed and tree-like, autosomal boxier around arabiensis and gambiae+coluzzii, inversions distinctive. The gene-tree conflict is visible right in the alignments.

---

<a id="slide-87"></a>

## Slide 87: Agenda

![Slide 87](images/slide-087.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-88"></a>

## Slide 88: And what's next?

![Slide 88](images/slide-088.jpg)

**Notes:** Neighbor-Net only flags conflict. Next we build an explicit network by hand, drawing the reticulation events ourselves. That's phylogenetic sketching.

---

<a id="slide-89"></a>

## Slide 89: Hands-on: sketch a hypothesis network in PhyloSketch

![Slide 89](images/slide-089.jpg)

**Notes:** PhyloSketch isn't an inference engine: it's for drawing explicit hypotheses. Turn the patterns you've seen into a network. And you won't be blind: Fontaine's Fig 1C is your target.

---

<a id="slide-90"></a>

## Slide 90: PhyloSketch in 90 seconds

![Slide 90](images/slide-090.jpg)

**Notes:** Ninety seconds on the tool: click to place taxa, drag to connect, turn a node into a reticulation by adding a second parent, and save as a .psketch file.

---

<a id="slide-91"></a>

## Slide 91: Your target network: Fontaine et al. Fig 1C

![Slide 91](images/slide-091.jpg)

**Notes:** Here's your target: Fontaine's Fig 1C, the published map of the major introgression events. Your job is to reproduce it as a network, not to guess it blind.

---

<a id="slide-92"></a>

## Slide 92

![Slide 92](images/slide-092.jpg)

**Notes:** Start from the species tree we trust: the X-distal topology: and sketch that first. Then add reticulation nodes for the events in the table. A starting .psketch is provided if you'd rather not draw from scratch.

---

<a id="slide-93"></a>

## Slide 93

![Slide 93](images/slide-093.jpg)

**Notes:** Now decide how many events to include: one reticulation is minimal, two or three richer: but every one has to be justified by evidence you've seen. There's no single right answer.

---

<a id="slide-94"></a>

## Slide 94: Build your hypothesis network

![Slide 94](images/slide-094.jpg)

**Notes:** One mechanics note: to draw a transfer edge in PhyloSketch, declare an edge as the 'acceptor', then connect the donor.

---

<a id="slide-95"></a>

## Slide 95: Agenda

![Slide 95](images/slide-095.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-96"></a>

## Slide 96: PhyloGuide Q4

![Slide 96](images/slide-096.jpg)

**Notes:** A PhyloGuide checkpoint: how do we infer a network with the fewest reticulations that display all the gene trees? A minimum-hybridization method: but check ILS first, since it can mimic reticulation.

---

<a id="slide-97"></a>

## Slide 97: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 97](images/slide-097.jpg)

**Notes:** Our last tool, and the one that motivated much of this: PhyloParallelograms shows all fifteen gene trees on one shared network, so you see where they agree and conflict at a glance.

---

<a id="slide-98"></a>

## Slide 98: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 98](images/slide-098.jpg)

**Notes:** A parallelogram draws several rooted gene trees together on an underlying network: where they agree, branches run as parallel bands; where they conflict, the bands split. PhyloFusion computes the network.

---

<a id="slide-99"></a>

## Slide 99: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 99](images/slide-099.jpg)

**Notes:** Open tutorial_loci.nex: the fifteen labelled gene trees. By default the first two form a network; from there, explore.

---

<a id="slide-100"></a>

## Slide 100: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 100](images/slide-100.jpg)

**Notes:** Two X-distal loci: the trees run together almost everywhere, and the network needs just one reticulation: nearly the same story, close to the true history.

---

<a id="slide-101"></a>

## Slide 101: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 101](images/slide-101.jpg)

**Notes:** The point is interactive comparison. Try the X-distal loci alone, the inversion loci alone, all fifteen, and mixed subsets: and watch the network change.

---

<a id="slide-102"></a>

## Slide 102: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 102](images/slide-102.jpg)

**Notes:** All five X-distal loci: still mostly parallel, still one reticulation: the X carries the species branching order.

---

<a id="slide-103"></a>

## Slide 103: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 103](images/slide-103.jpg)

**Notes:** Now the four inversion loci: the bands diverge, especially around arabiensis, quadriannulatus and merus, and the network jumps to five reticulations. Fewer trees, far more conflict: the introgression paths.

---

<a id="slide-104"></a>

## Slide 104: Hands-on PhyloParallelograms: understanding gene trees through their network

![Slide 104](images/slide-104.jpg)

**Notes:** And all fifteen at once: seven reticulations, the whole pattern in one picture: the concordant X against the introgressed autosomes and inversions. Colour by chromosome and you simply see it.

---

<a id="slide-105"></a>

## Slide 105: How does the parallelogram compare to what you sketched?

![Slide 105](images/slide-105.jpg)

**Notes:** Now compare your sketch to the computed network: same number of reticulations? Same events and lineage pairs? Same direction of flow? Hand-drawn intuition meets automated inference.

---

<a id="slide-106"></a>

## Slide 106: PhyloGuide Q5

![Slide 106](images/slide-106.jpg)

**Notes:** A PhyloGuide checkpoint: what do reticulations between arabiensis and gambiae+coluzzii, and between merus and quadriannulatus, mean? Non-tree-like evolution: gene flow or hybridization: with different loci carrying different histories.

---

<a id="slide-107"></a>

## Slide 107: Agenda

![Slide 107](images/slide-107.jpg)

**Notes:** A quick look at where we are in the plan before the next section.

---

<a id="slide-108"></a>

## Slide 108: Back to the biology: what did this tell us about malaria

![Slide 108](images/slide-108.jpg)

**Notes:** The biology, finally: the X gives the true order: arabiensis and quadriannulatus are sisters, not the vectors. The autosomes are pervasively introgressed, with a further merus-quadriannulatus event. If introgression carries vector traits, controlling one species can be undercut by another.

---

<a id="slide-109"></a>

## Slide 109: Take-aways from the tutorial

![Slide 109](images/slide-109.jpg)

**Notes:** The take-aways: gene trees disagree systematically under introgression: that's data. Tree methods can be confidently wrong. Networks make the conflict visible three ways. Sketch first, then infer. And AI can orient you, but doesn't replace judgment.

---

<a id="slide-110"></a>

## Slide 110: Thank you - and please give us feedback

![Slide 110](images/slide-110.jpg)

**Notes:** Thank you: to all of you, to the Anopheles consortium and Fontaine et al. for the data, to the tool developers, and to ISCB. Please leave feedback via the QR, and we'll stay for questions.

---

<a id="slide-111"></a>

## Slide 111: Share your feedback

![Slide 111](images/slide-111.jpg)

---
