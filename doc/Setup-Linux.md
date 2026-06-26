# Setup Guide (Linux): Trees-to-Networks Tutorial

This guide covers installing all required software on **Linux** (tested on Ubuntu 24.04).

> **Using Windows?** See the separate guide `INSTALL_WINDOWS.md`.

The tutorial software stack:

| Tool | Type | Source |
|---|---|---|
| IQ-TREE 3 | CLI | conda (bioconda) |
| ASTRAL | CLI | conda (bioconda) |
| BEAST 10.5.0 (BEAUti, TreeAnnotator, TreeStat) | CLI + GUI | conda (bioconda) |
| Tracer 1.7.2 | GUI | conda (bioconda) |
| ete3 | Python lib | conda (conda-forge) |
| SplitsTree6 | GUI | GitHub release |
| PhyloSketch2 | GUI | GitHub release |
| PhyloParallelograms | GUI | GitHub release |

---

## Prerequisites

- Linux (tested on Ubuntu 24.04)
- **Anaconda installed** (recommended). Miniconda also works, but full Anaconda has fewer "Solving environment" issues during `conda create`.
- `git` and `wget` available

If `git` is missing:

```bash
sudo apt update
sudo apt install git
```

### If you don't have Anaconda yet

Anaconda now **requires you to register (free) before downloading the installer**. Don't try to `wget` a hardcoded URL - get a fresh download link from their website each time.

1. Go to <https://www.anaconda.com/download> in your browser.
2. Register / sign in with your email (free).
3. On the download page, find the **Linux 64-Bit (x86) Installer (.sh)**.
4. **Right-click** the download link  **Copy link address**.
5. In your terminal, paste the link after `wget`:

```bash
wget <paste-the-link-you-copied-here>
```

This downloads an installer file named something like `Anaconda3-<YEAR.MONTH>-Linux-x86_64.sh` (the year and version change with each Anaconda release). Check the exact filename you got:

```bash
ls Anaconda3-*.sh
```

Run the installer using that exact filename - for example:

```bash
bash Anaconda3-XX.XX-X-Linux-x86_64.sh
```

> Replace `Anaconda3-XX.XX-X-Linux-x86_64.sh` with whatever `ls` printed. Tab-completion (`bash Anaconda3-<Tab>`) also works.

During installation:

- Press `Enter` to scroll through the license.
- Type `yes` to accept.
- Accept the default install location.
- Type `yes` when asked to initialize Anaconda.

Restart your shell so `conda` is on your `PATH`:

```bash
source ~/.bashrc
```

Verify:

```bash
conda --version
```

## Step 1 - Clone the tutorial repository

```bash
git clone https://github.com/husonlab/trees-to-networks-tutorial.git
cd trees-to-networks-tutorial
```

## Step 2 - Create the conda environment

This single command installs everything needed on the command line - IQ-TREE, ASTRAL, BEAST (with BEAUti, TreeAnnotator, TreeStat), Tracer, ete3, and Python 3.11. It also pulls in OpenJDK 11, which the Java-based tools need.

> **Why Python 3.11?** `ete3` is not compatible with Python 3.14.

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

> **Note on Tracer:** On some Linux desktops `tracer` may print a `java.awt.Desktop` warning at startup. The GUI still launches and works normally - the warning can be ignored.

## Step 3 - Install SplitsTree6

Download and run the installer from the [SplitsTree6 v6.7.9 GitHub release](https://github.com/husonlab/splitstree6/releases/tag/v6.7.9):

```bash
wget https://github.com/husonlab/splitstree6/releases/download/v6.7.9/SplitsTree_unix_6_7_9.sh
chmod +x SplitsTree_unix_6_7_9.sh
./SplitsTree_unix_6_7_9.sh
```

The installer is interactive - follow the on-screen prompts. **By default it installs to `~/splitstree6` (your home directory)**, not the folder you ran the installer from. You can change this when prompted.

Launch directly with the full path:

```bash
~/splitstree6/SplitsTree
```

### Adding SplitsTree to your PATH (optional but recommended)

For **bash** (Ubuntu default):

```bash
echo 'export PATH="$HOME/splitstree6:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For **zsh**:

```bash
echo 'export PATH="$HOME/splitstree6:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Then launch with just `SplitsTree`.

> A `Gtk-CRITICAL ... gtk_window_resize: assertion 'height > 0' failed` warning may appear in the terminal. It is harmless - the application opens normally.

## Step 4 - Install PhyloSketch2

Download and run the installer from the [PhyloSketch2 v2.2.13 GitHub release](https://github.com/husonlab/phylosketch2/releases/tag/v2.2.13):

```bash
wget https://github.com/husonlab/phylosketch2/releases/download/v2.2.13/PhyloSketch2_unix_2_2_13.sh
chmod +x PhyloSketch2_unix_2_2_13.sh
./PhyloSketch2_unix_2_2_13.sh
```

Follow the interactive installer prompts. **By default it installs to `~/phylosketch2`.**

Launch directly:

```bash
~/phylosketch2/PhyloSketch2
```

### Adding PhyloSketch2 to your PATH (optional)

```bash
echo 'export PATH="$HOME/phylosketch2:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Use `~/.zshrc` for zsh. Then launch with just `PhyloSketch2`.

## Step 5 - Install PhyloParallelograms

PhyloParallelograms is distributed as a tarball - no installer required.

```bash
cd ~
wget https://github.com/husonlab/phyloparallelograms/releases/download/v1.0.7/PhyloParallelograms-1.0.7-linux-x86_64.tar.gz
tar -xvzf PhyloParallelograms-1.0.7-linux-x86_64.tar.gz
```

Launch:

```bash
~/PhyloParallelograms/bin/PhyloParallelograms
```

### Adding PhyloParallelograms to your PATH (optional)

```bash
echo 'export PATH="$HOME/PhyloParallelograms/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Use `~/.zshrc` for zsh. Then launch with just `PhyloParallelograms`.

---

---

# Verifying the installation

## CLI tools (with `tutorial` env active)

With the `tutorial` environment active, the following commands should all run and print version/usage info:

```bash
iqtree3 --version
astral --help
beast -help
beauti                # opens GUI
treeannotator         # opens GUI
tracer                # opens GUI
```

## GUI apps (default install locations)

```bash
~/splitstree6/SplitsTree
~/phylosketch2/PhyloSketch2
~/PhyloParallelograms/bin/PhyloParallelograms
```

Or, if you added them to your PATH:

```bash
SplitsTree
PhyloSketch2
PhyloParallelograms
```
