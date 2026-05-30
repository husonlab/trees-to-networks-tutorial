# Setup Guide (macOS): Trees-to-Networks Tutorial

This guide covers installation on **macOS**, tested on **Apple Silicon (M3)**. Notes for Intel Macs are included throughout — wherever the download file differs, look for the **"Intel Macs"** callout.

The macOS setup follows the same shape as the Linux one:

- **Command-line tools** (IQ-TREE, ASTRAL, BEAST, BEAUti, TreeAnnotator, Tracer, ete3) are installed into a single conda environment.
- **GUI applications** (SplitsTree6, PhyloSketch2, PhyloCompare) are installed from `.dmg` files downloaded from GitHub.

> **How to tell which Mac you have:** Apple menu → **About This Mac**. If the chip says "Apple M1 / M2 / M3 / M4", you're on Apple Silicon (arm64). If it says "Intel", you're on x86_64.

---

## Prerequisites

- macOS (tested on Apple Silicon)
- **Anaconda installed** (recommended). Miniconda also works, but full Anaconda has fewer "Solving environment" issues during `conda create`.
- `git` and `curl` available. `curl` is preinstalled on macOS — we'll use it instead of `wget` (which isn't installed by default).

If you don't have `git` yet, the easiest way is to install Apple's Command Line Tools:

```bash
xcode-select --install
```

A dialog will pop up — click **Install** and wait a few minutes.

### If you don't have Anaconda yet

Anaconda now **requires you to register (free) before downloading the installer**. Don't try to use a hardcoded URL — get a fresh download link from their website each time.

1. Go to <https://www.anaconda.com/download> in your browser.
2. Register / sign in with your email (free).
3. On the download page, pick the right installer:
   - **Apple Silicon (M-series):** `Anaconda3-XX.XX-MacOSX-arm64.sh` (the **command-line** installer, not the `.pkg`)
   - **Intel Macs:** `Anaconda3-XX.XX-MacOSX-x86_64.sh`
4. **Right-click** the download link → **Copy Link**.
5. In your Terminal, paste the link after `curl -O`:

```bash
curl -O <paste-the-link-you-copied-here>
```

This downloads an installer file named like `Anaconda3-<YEAR.MONTH>-MacOSX-arm64.sh` (the year and version change with each release). Check the exact filename:

```bash
ls Anaconda3-*.sh
```

Run the installer using that exact filename — for example:

```bash
bash Anaconda3-XX.XX-X-MacOSX-arm64.sh
```

> Replace `Anaconda3-XX.XX-X-MacOSX-arm64.sh` with whatever `ls` printed. Tab-completion (`bash Anaconda3-<Tab>`) also works.

During installation:

- Press `Enter` to scroll through the license.
- Type `yes` to accept.
- Accept the default install location.
- Type `yes` when asked to initialize Anaconda.

Restart your shell so `conda` is on your `PATH`:

```bash
source ~/.zshrc        # macOS default shell since Catalina
# or, if you're still on bash:
source ~/.bash_profile
```

Verify:

```bash
conda --version
```

---

## Step 1 — Clone the tutorial repository

```bash
cd ~
git clone https://github.com/husonlab/trees-to-networks-tutorial.git
cd trees-to-networks-tutorial
```

---

## Step 2 — Create the conda environment

This single command installs everything needed on the command line — IQ-TREE, ASTRAL, BEAST (with BEAUti, TreeAnnotator, TreeStat), Tracer, ete3, and Python 3.11. It also pulls in OpenJDK 11, which the Java-based tools need.

```bash
conda create -n tutorial \
    -c anaconda \
    -c conda-forge \
    -c defaults \
    -c bioconda \
    astral-tree=5.7.8 \
    iqtree=3.1.2 \
    ete3=3.1.2 \
    beast=10.5.0 \
    tracer=1.7.2 \
    python=3.11
```

Activate the environment:

```bash
conda activate tutorial
```

> All remaining commands assume the `tutorial` environment is active.

After activation, the following commands are on your `PATH`: `iqtree3`, `astral`, `beast`, `beauti`, `treeannotator`, `treestat`, `tracer`.

---

## Step 3 — Install SplitsTree6

Download the macOS DMG (universal — works on both Apple Silicon and Intel):

```bash
curl -LO https://github.com/husonlab/splitstree6/releases/download/v6.7.9/SplitsTree_macos_6_7_9.dmg
```

Or download manually from the [SplitsTree6 v6.7.9 release page](https://github.com/husonlab/splitstree6/releases/tag/v6.7.9).

Install:

1. Double-click `SplitsTree_macos_6_7_9.dmg` in Finder to mount it.
2. Inside the mounted disk image, double-click the **installer** to launch the interactive setup.
3. Follow the on-screen prompts (accept the license, choose the install location — the default is fine).
4. When finished, eject the DMG.
5. Launch SplitsTree from **Applications** or via Spotlight (Cmd+Space → "SplitsTree").

---

## Step 4 — Install PhyloSketch2

### Apple Silicon (M-series):

```bash
curl -LO https://github.com/husonlab/phylosketch2/releases/download/v2.2.12/PhyloSketch2_macos-arm64_2_2_12.dmg
```

### Intel Macs:

Download the x86_64 build from the [PhyloSketch2 v2.2.12 release page](https://github.com/husonlab/phylosketch2/releases/tag/v2.2.12) — look under **Assets** for a file ending in `macos-x86_64`.

### Install:

1. Double-click the `.dmg` in Finder to mount it.
2. Inside the mounted disk image, double-click the **installer** to launch the interactive setup.
3. Follow the on-screen prompts (accept the license, choose the install location — the default is fine).
4. When finished, eject the DMG.
5. Launch PhyloSketch2 from **Applications** or via Spotlight.

---

## Step 5 — Install PhyloCompare

### Apple Silicon (M-series):

```bash
curl -LO https://github.com/husonlab/phylocompare/releases/download/v1.0.1/PhyloCompare-1.0.1-macos-aarch64.dmg
```

### Intel Macs:

Download the x86_64 build from the [PhyloCompare v1.0.1 release page](https://github.com/husonlab/phylocompare/releases/tag/v1.0.1) — look under **Assets** for a file ending in `macos-x86_64`.

### Install:

1. Double-click the `.dmg` in Finder to mount it.
2. **Drag** the **PhyloCompare** app into the **Applications** folder. *(Unlike the other two, this DMG does not run an interactive installer — it's drag-to-install.)*
3. Eject the DMG.
4. Launch from **Applications** or via Spotlight.

---

## Note on Gatekeeper / "unidentified developer"

When you first launch one of the DMG apps, macOS may block it with a message like:

> *"SplitsTree" cannot be opened because the developer cannot be verified.*

This is normal for academic software that isn't signed with an Apple Developer ID. To bypass it:

- **Easy way:** Right-click (or Control-click) the app in **Applications** → **Open** → in the dialog that appears, click **Open** again.
- **Or:** Apple menu → **System Settings** → **Privacy & Security** → scroll down → click **Open Anyway** next to the blocked app.

You only need to do this once per app.

---

## Verifying the installation

With the `tutorial` environment active, the following commands should all run and print version/usage info:

```bash
iqtree3 --version
astral --help
beast -help
beauti                # opens GUI
treeannotator         # opens GUI
tracer                # opens GUI
```

And the three downloaded apps — launch from **Applications**:

- **SplitsTree**
- **PhyloSketch2**
- **PhyloCompare**

Close each one after confirming it opens.

---

## Quick reference — what each tool does

| Tool | Type | Source |
|---|---|---|
| IQ-TREE 3 | CLI | conda (bioconda) |
| ASTRAL | CLI | conda (bioconda) |
| BEAST 10.5.0 (BEAUti, TreeAnnotator, TreeStat) | CLI + GUI | conda (bioconda) |
| Tracer 1.7.2 | GUI | conda (bioconda) |
| ete3 | Python lib | conda (conda-forge) |
| SplitsTree6 | GUI | GitHub DMG |
| PhyloSketch2 | GUI | GitHub DMG (separate Intel / arm64 builds) |
| PhyloCompare | GUI | GitHub DMG (separate Intel / arm64 builds) |
