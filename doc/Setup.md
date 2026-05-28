# Attendee Setup Instructions

**ISMB 2026 Tutorial IP3**
Daniel H. Huson, Anupam Gautam, Banu Cetinkaya
University of Tubingen

**Action required before tutorial day.** Please complete the software
installation and data download below. Allow **about 60 minutes** the first
time you work through it; some installers are large.

If you hit setup problems, please reach out **before** the tutorial —
diagnosing installs in person on the day takes time away from the actual
tutorial. Contact details at the bottom of this page.

---

These instructions are hosted here:

```html
https://github.com/husonlab/trees-to-networks-tutorial/blob/main/doc/Setup.md
```

Additional setup steps for **Windows** are here: 

```html
https://github.com/husonlab/trees-to-networks-tutorial/blob/main/doc/Setup-Windows.md
```
---

## Hardware Requirements

- A laptop running **macOS** (Apple Silicon or Intel), **Linux** (Ubuntu 20.04+
  or equivalent), or **Windows 10/11**
- At least **8 GB RAM**
- At least **3 GB free disk space**
- Working **internet connection on tutorial day** (we'll reference PhyloGuide
  in the browser)

---

## Tutorial Materials

Clone this repository to your laptop:

```bash
git clone https://github.com/husonlab/trees-to-networks-tutorial.git
cd trees-to-networks-tutorial
```

The repository is ~100 MB and contains everything you need — alignments,
precomputed outputs, exercise instructions, and slides. **No additional
downloads are required.** (The source MAF file from Fontaine et al. 2015 is
~2 GB and not included; it's only needed if you want to rerun the data
preparation step yourself, which is optional.)

---

## Software to Install

Eight tools, all free, all native installers. Java is a prerequisite for
several of them, so install it first.

### 1. Java

Required by BEAST X, Tracer, and the Java versions of ASTRAL.
Install **Java 17 or later** (OpenJDK is recommended).

- **macOS**: `brew install openjdk@17` (or download from https://adoptium.net/)
- **Linux**: `sudo apt install default-jdk` (Ubuntu/Debian) or equivalent
- **Windows**: download from https://adoptium.net/

Verify:
```bash
java -version
```
You should see version 17.0 or higher.

### 2. IQ-TREE 3

Maximum-likelihood phylogenetic inference. Download from
http://www.iqtree.org/#download — get **IQ-TREE version 3.x**. Extract the
archive and put the `iqtree3` binary somewhere on your `PATH`
(e.g. `/usr/local/bin/` or `~/bin/`).

Verify:
```bash
iqtree3 --version
```

### 3. ASTRAL

Coalescent species-tree inference. Available at
https://github.com/smirarab/ASTRAL.

```bash
wget https://github.com/smirarab/ASTRAL/raw/master/Astral.5.7.8.zip
unzip Astral.5.7.8.zip
java -jar Astral/astral.5.7.8.jar -h
```

Note the full path to `astral.5.7.8.jar` — you'll need it for the tutorial commands.

### 4. BEAST X (with BEAUti and TreeAnnotator bundled)

Bayesian phylogenetic inference. Download from https://beast.community — get
**BEAST X v10.5 or newer**. The installer bundles BEAUti (GUI for setting up
runs) and TreeAnnotator (for summarizing posterior tree sets).

- **macOS**: `.pkg` installer (includes BEAGLE for hardware acceleration)
- **Windows**: `.zip` archive
- **Linux**: `.tgz` archive (you may need to install BEAGLE separately from
  https://github.com/beagle-dev/beagle-lib)

Verify:
```bash
beast -help
beauti -help
treeannotator -help
```

### 5. Tracer

For inspecting BEAST output. Download **v1.7+** from
https://github.com/beast-dev/tracer/releases. Standalone Java application,
no installation required — just unzip and run.

### 6. SplitsTree

For phylogenetic network visualization. Download from

> https://github.com/husonlab/splitstree6

Native installers for macOS, Windows, and Linux are available.


### 7. PhyloSketch

For interactive phylogenetic network sketching.
Download from

> https://github.com/husonlab/phylosketch2

Native installers for macOS, Windows, and Linux are available.

### 8. PhyloCompare

For inferring networks from gene tree sets and drawing gene trees inside
networks.

Download from
> https://github.com/husonlab/phylocompare

Native installers for macOS, Windows, and Linux are available.
---

## Online Tool to Bookmark

**PhyloGuide** — an experimental phylogenetics-focused custom GPT we'll reference at
several points during the tutorial. No account or login required, just
bookmark the URL:

> https://chatgpt.com/g/g-6a0c387e1fc081919668ca163cb76424-phyloguide

You'll need an internet connection on tutorial day to access it.

---

## Pre-Reading (Optional)

The tutorial doesn't require prior reading, but if you want to prepare:

- **Source paper for our dataset**:
  Fontaine, M.C., Pease, J.B., Steele, A., et al. (2015). Extensive
  introgression in a malaria vector species complex revealed by phylogenomics.
  *Science* 347(6217): 1258524.
  [doi:10.1126/science.1258524](https://doi.org/10.1126/science.1258524)

- **Daniel H. Huson, David Bryant, Application of Phylogenetic Networks in Evolutionary Studies, Molecular Biology and Evolution, Volume 23, Issue 2, February 2006, Pages 254–267. [doi.org/10.1093/molbev/msj030](https://doi.org/10.1093/molbev/msj030)

---

## Testing Your Setup

After installing everything, verify the toolchain by running these from
inside the cloned repository:

```bash
iqtree3 -s data/alignments/X_dist_04.fasta -st DNA -T 1 \
    --prefix /tmp/setup_test_iqtree --quiet

java -jar /path/to/Astral/astral.5.7.8.jar precomputed/iqtree/tutorial_loci.treefile \
    -o /tmp/setup_test_astral.tre

beauti
````

(4) Launch SplitsTree (close it after it opens)
Open from your Applications folder / Start menu / launcher

(5) Launch Tracer (close it after it opens)
Open the .jar or the platform-specific launcher in the Tracer folder


If all five work, you're ready for tutorial day. Clean up the test outputs:

```bash
rm /tmp/setup_test_*
```

---

## Day-of Checklist

- [ ] Laptop with all eight tools installed and tested
- [ ] Power adapter — the tutorial is ~4 hours with one 20-minute break
- [ ] Cloned repository in a known location on your filesystem
- [ ] Internet connection working
- [ ] PhyloGuide URL bookmarked

---

### Windows

Additional setup steps for **Windows** are here:

```html
https://github.com/husonlab/trees-to-networks-tutorial/blob/main/doc/Setup-Windows.md
```
---

## Help and Contact

If you run into problems during setup, please reach out before the tutorial:

> **daniel.huson@uni-tuebingen.de**

We strongly recommend completing setup at least a few days before tutorial
day. Debugging install issues in real time during the tutorial eats into
the content time for everyone in the room.

