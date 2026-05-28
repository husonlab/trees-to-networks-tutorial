# Trees-to-Networks Tutorial Setup

## Windows Setup

For Windows, some parts of the tutorial are easier to run inside **WSL (Windows Subsystem for Linux)**, preferably using Ubuntu.

---

# Install WSL Ubuntu

1. Open the **Microsoft Store**
2. Search for **Ubuntu**
3. Install the regular version:
- ✅ Ubuntu
- ❌ Do not choose *Pro* or *Preview*

WSL Ubuntu is free.

After installation:

1. Launch Ubuntu
2. Create a username and password when prompted

---

# Install Anaconda Inside WSL Ubuntu

Update Ubuntu first:

```bash
sudo apt update && sudo apt upgrade -y
```

Install required utilities:

```bash
sudo apt install wget curl bzip2 -y
```

Download Anaconda:

```bash
wget https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh
```

Run the installer:

```bash
bash Anaconda3-latest-Linux-x86_64.sh
```

During installation:

- Press `Enter` to continue
- Type `yes` to accept the license
- Choose the default installation location
- Type `yes` when asked to initialize Anaconda

Restart the shell:

```bash
source ~/.bashrc
```

Verify installation:

```bash
conda --version
```

---

# Create Conda Environment

Use Python 3.11 because `ete3` is not compatible with Python 3.14.

```bash
conda create -n tutorial \
 -c anaconda \
 -c conda-forge \
 -c defaults \
 -c bioconda \
 astral-tree=5.7.8 \
 iqtree=3.1.2 \
 ete3=3.1.2 \
 python=3.11
```

Activate the environment:

```bash
conda activate tutorial
```

---

# Run IQ-TREE

```bash
iqtree3 -S data/alignments/ \
 -B 1000 \
 --prefix tutorial_loci \
 -T AUTO \
 -st DNA
```

---

# Generate Nexus Treeset

```bash
python tools/make_nexus_treeset.py \
 --alignments-dir data/alignments/ \
 --treefile tutorial_loci.treefile \
 --out tutorial_loci.nex \
 --outgroup An_christyi
```

---

# BEAST and TreeAnnotator

- **BEAST** can be run using the GUI application.
- **TreeAnnotator** can also be run from the GUI.

For BEAST, it is recommended to install the **BEAGLE library** for improved performance.

Most remaining software can be installed normally as `.exe` applications on Windows.