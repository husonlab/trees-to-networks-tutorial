# Tutorial Run-of-Show

Total duration: **240 minutes** (4 hours), structured as Part I (110 min) +
break (20 min) + Part II (110 min). Tutorial runs **09:00 to 13:00**.

**Presenter model.** Daniel Huson (DH) is the primary presenter throughout.
Anupam Gautam (AG) leads the five PhyloGuide check-ins; Banu Cetinkaya (BC)
leads the PhyloFusion centerpiece in Part II. Outside their dedicated
segments, AG and BC float through the room helping participants who get
stuck during hands-on work. This gives DH approximately 40 min of planned
breaks across the 4 hours and uses AG/BC's expertise on their signature
tools.

---

## Part I: Trees and within-locus uncertainty (110 min)

| Time  | Duration | Segment | Format | Lead | Notes |
|-------|----------|---------|--------|------|-------|
| 09:00 | 5 min  | Welcome and presenter introductions | Lecture | DH | Slides 1-3 |
| 09:05 | 10 min | Tutorial overview + dataset introduction | Lecture | DH | Anopheles gambiae complex, Fontaine 2015 story; map of Africa, the 6 species, what we'll see across the 4 hours |
| 09:15 | 5 min  | Setup verification | Hands-on | DH (AG/BC float) | Everyone confirms IQ-TREE, BEAST, SplitsTree launch; catches install issues early |
| 09:20 | 15 min | Lecture: from sequence alignments to multi-locus gene trees | Lecture | DH | MSC, ILS, introgression, why gene trees disagree |
| 09:35 | 5 min  | **PhyloGuide check-in #1**: "We have multi-locus alignments. How should we infer a species phylogeny?" | Demo + participant | **AG** | Compare PhyloGuide's recommendation with the expert approach |
| 09:40 | 22 min | Hands-on: per-locus ML inference with IQ-TREE 3 (-S mode on the 15 alignments) | Hands-on | DH (AG/BC float) | Run IQ-TREE, examine `tutorial_loci.treefile`, observe topology variation across loci |
| 10:02 | 5 min  | **PhyloGuide check-in #2**: "Our gene trees disagree across chromosomes. What does this mean?" | Demo + participant | **AG** | Set up the introgression-vs-ILS distinction |
| 10:07 | 30 min | Hands-on: Bayesian inference with BEAST X **plus posterior visualization in SplitsTree** | Hands-on | DH (AG/BC float) | BEAUti walkthrough, brief live run (approximately 3 min, 5M states) started during the walkthrough, Tracer convergence check, TreeAnnotator MCC tree, then **open `X_dist_04.trees` in SplitsTree, view as DensiTree alongside the consensus network from the posterior** |
| 10:37 | 5 min  | Hands-on: coalescent species tree with wASTRAL | Hands-on | DH (AG/BC float) | Run wASTRAL on `tutorial_loci.treefile`, see the species tree it returns and its support values |
| 10:42 | 8 min  | Part I synthesis + bridge to Part II + **feedback QR code slide** | Lecture | DH | The pedagogical hinge: "Even with Bayesian uncertainty within a locus and ASTRAL summarizing across loci, we still get *a* tree. But our gene trees disagree systematically. Trees and tree summaries force one answer. After the break: stop forcing, start visualizing." |
| 10:50 |        | (Part I ends) | | | |

---

## Break (20 min)

| Time  | Duration | Segment |
|-------|----------|---------|
| 10:50 | 20 min | Coffee / restroom / informal Q&A with presenters |
| 11:10 |        | (Reconvene) |

---

## Part II: Networks and cross-locus reticulation (110 min)

| Time  | Duration | Segment | Format | Lead | Notes |
|-------|----------|---------|--------|------|-------|
| 11:10 | 5 min  | Welcome back + Part II overview | Lecture | DH | Recap Part I conclusion, preview the network views |
| 11:15 | 15 min | Lecture: what is a phylogenetic network? Splits, hybridization, types of networks | Lecture | DH | Conceptual foundation; references back to Huson & Bryant 2006 |
| 11:30 | 5 min  | **PhyloGuide check-in #3**: "When is a tree not enough? When do we need a network?" | Demo + participant | **AG** | Concept-driven check-in |
| 11:35 | 20 min | Hands-on: SplitsTree NeighborNet on the 15 alignments | Hands-on | DH (AG/BC float) | Network view of conflicting splits in raw alignment data; visual contrast between X-distal and autosomal loci |
| 11:55 | 20 min | Hands-on: PhyloSketch, interactive network construction | Hands-on | DH (AG/BC float) | Build a hypothesized network from biological intuition; introduces reticulation nodes |
| 12:15 | 5 min  | **PhyloGuide check-in #4**: "We want to visualize reticulation across loci. What method fits?" | Demo + participant | **AG** | Sets up PhyloFusion |
| 12:20 | 25 min | Hands-on: PhyloFusion, networks from the gene tree set, with interactive subset selection | Hands-on | **BC** (DH/AG float) | The pedagogical centerpiece: load the gene tree set, select X-only / autosomal-only / all 15, see how the network changes; map gene trees onto the network |
| 12:45 | 5 min  | **PhyloGuide check-in #5**: "What does this network tell us biologically?" | Demo + participant | **AG** | Set up the biological interpretation that follows |
| 12:50 | 10 min | Biological interpretation + wrap-up + **feedback QR code slide (final)** | Lecture / discussion | DH | Connect back to Fontaine's biological conclusions; pointers to repo, docs, future workshops |
| 13:00 |        | (Tutorial ends) | | | |

---

## Time Buffers and Compression Plan

The schedule sums to exactly 220 min of content + 20 min break. In practice,
hands-on segments tend to run 2 to 5 min long. If running behind:

- **PhyloGuide check-ins** compress easily from 5 min to 2 min by skipping
  the participant-try step and just demoing the GPT response. With 5
  check-ins, this is up to 15 min of recoverable slack.
- **Lecture segments at 09:20 and 11:15** can each absorb a 5-minute
  compression by cutting detailed examples and pointing to slides for
  self-study.
- **The synthesis at 10:42 is the most protected segment**; it is the
  pedagogical hinge of the tutorial. Don't compress it.
- **PhyloFusion at 12:20 is the second-most-protected**; it's the
  hands-on payoff for the networks half.

If running *ahead* of schedule, expand the discussion in the 10:42 synthesis
and the 12:50 biological interpretation; those are the natural slack points.

---

## Presenter Notes

- **Floating coverage.** During DH's hands-on segments, AG and BC walk
  the room helping participants who fall behind, point them at the
  `precomputed/` files when needed, and answer one-on-one questions that
  would otherwise interrupt the group flow.
- **The BEAST live run** at 10:07 should be *started immediately* (during
  the BEAUti walkthrough discussion) so that by the time DH finishes
  the walkthrough, the run has data to look at in Tracer.
- **The SplitsTree posterior visualization** at the end of the BEAST
  segment is the pedagogical bonus of the new Part I structure: DensiTree
  (all posterior trees superimposed) and consensus network (splits weighted
  by posterior support) shown side-by-side in SplitsTree, both computed
  from the same `X_dist_04.trees` file. This is where participants first
  see a network, but as a *within-locus uncertainty* network. In Part II
  they'll see networks for *cross-locus reticulation*, providing a clean
  conceptual escalation.
- **Handoffs.** Each AG or BC segment is introduced by DH explicitly
  ("...and for the next 5 minutes Anupam is going to ask PhyloGuide...").
  At the end of the guest segment, AG/BC hands back to DH explicitly.
- **Feedback QR code slides.** Same QR code appears at 10:42 (before
  break) and 12:50 (during wrap-up), per ISCB requirements.

---

## Required Slide Deck Structure

To match this schedule, the deck should have these sections:

1. **Title + presenters** (slides 1-3)
2. **Tutorial overview + dataset** (4-10)
3. **Setup verification placeholder** (11)
4. **Lecture: multi-locus phylogenomics** (12-22)
5. **IQ-TREE hands-on** (23-27, with click-through commands)
6. **BEAST X + SplitsTree posterior visualization** (28-37, with BEAUti screenshots and SplitsTree DensiTree/consensus-network screenshots)
7. **wASTRAL hands-on** (38-39)
8. **Part I synthesis + feedback QR code** (40-42)
9. **Part II opener + networks lecture** (43-53)
10. **SplitsTree NeighborNet hands-on** (54-57)
11. **PhyloSketch hands-on** (58-62)
12. **PhyloFusion hands-on** (63-68)
13. **Biological interpretation + wrap-up + feedback QR code** (69-72)

Plus approximately 10 slides for the 5 PhyloGuide check-ins (one question
slide + one canonical-response screenshot per check-in). Total: 80 to 85
slides for 220 min of content = approximately 2.7 min per slide on average.
Comfortable hands-on tutorial pace.

AG owns the content for the PhyloGuide check-in slides but they should
match the deck's visual style.
