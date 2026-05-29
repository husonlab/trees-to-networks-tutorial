# Setup Guide (Windows): Trees-to-Networks Tutorial

On Windows, the tutorial uses a **hybrid setup**:

- **Command-line tools** (IQ-TREE, ASTRAL, ete3, helper Python scripts) run inside **WSL Ubuntu** via a conda environment.
- **GUI applications** (BEAST, BEAUti, TreeAnnotator, Tracer, SplitsTree6, PhyloSketch2, PhyloCompare) come as **portable Windows `.zip` archives** - just extract and run the `.exe` inside. No installer is needed (with one small exception, BEAGLE).

This split avoids the headaches of running Java GUIs through WSL while keeping the Unix-style CLI workflow intact.

The guide is split into two parts:

1. **Part A - WSL Ubuntu + conda** (CLI tools)
2. **Part B - Native Windows installers** (GUI apps)

---

# Part A - WSL Ubuntu Setup (for CLI tools)

## Step A1 - Install WSL Ubuntu

1. Open the **Microsoft Store**.
2. Search for **Ubuntu**.
3. Install the regular version:
    -  Ubuntu
    - Do **not** choose *Ubuntu Pro* or *Ubuntu Preview*
4. Launch Ubuntu from the Start Menu.
5. When prompted, create a username and password.

WSL Ubuntu is free.

> If WSL isn't enabled on your machine yet, open PowerShell as Administrator and run `wsl --install`, then reboot.

---

## Step A2 - Update Ubuntu and install basic utilities

Inside the Ubuntu terminal:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install wget curl bzip2 git -y
```

---

## Step A3 - Install Anaconda inside WSL

Anaconda now **requires you to register (free) before downloading the installer**. Don't use a hardcoded download link - get a fresh one from their website each time.

1. Go to <https://www.anaconda.com/download> in your browser.
2. Register / sign in with your email (free).
3. On the download page, find the **Linux 64-Bit (x86) Installer (.sh)**.
4. **Right-click** the download link ‚Üí **Copy link address**.
5. Back in your WSL Ubuntu terminal, paste the link after `wget`:

```bash
wget <paste-the-link-you-copied-here>
```

This downloads an installer file named something like `Anaconda3-<YEAR.MONTH>-Linux-x86_64.sh` in the current folder (the year and version change with each Anaconda release). Check the exact filename you got:

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
- Type `yes` to accept the license.
- Accept the default installation location.
- Type `yes` when asked to initialize Anaconda.

Restart your shell (or close and reopen Ubuntu):

```bash
source ~/.bashrc
```

Verify:

```bash
conda --version
```

---

## Step A4 - Clone the tutorial repository

```bash
cd ~
git clone https://github.com/husonlab/trees-to-networks-tutorial.git
cd trees-to-networks-tutorial
```

> **Important:** the tutorial folder is now inside your **WSL home directory**, *not* on a Windows drive. From Windows it lives at:
> ```
> \\wsl$\Ubuntu\home\<your-wsl-username>\trees-to-networks-tutorial
> ```
> You'll need this path later when opening files from the native Windows GUI apps (BEAUti, Tracer, SplitsTree, etc.). See the [Accessing WSL files from Windows](#accessing-wsl-files-from-windows-and-vice-versa) section at the end of this guide for details.

---

## Step A5 - Create the conda environment

Python 3.11 is used because `ete3` is not yet compatible with newer Python versions.

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

> All remaining WSL commands assume the `tutorial` environment is active.

This gives you `iqtree3`, `astral`, and Python with `ete3` on the WSL command line.

> **Note:** Unlike the Linux setup, we do *not* install `beast` and `tracer` via conda on Windows. Use the native Windows installers in Part B instead - they integrate with Windows file dialogs and BEAGLE, and avoid X-server complications.

---

# Part B - Native Windows GUI Apps

These apps come as **`.zip` archives - no installer is run**. You just download, right-click ‚Üí **Extract All**, then double-click the `.exe` inside.

By default, downloads land in your **`Downloads`** folder. You can extract the archives there too, or move them somewhere more permanent like `C:\Tools\` if you prefer.

> **Important - Java is required.** BEAST needs a Java Runtime (JRE) installed on Windows. The other apps (SplitsTree6, PhyloSketch2, PhyloCompare, Tracer) bundle their own. Install the 64-bit Java JRE from <https://www.oracle.com/java/technologies/downloads/> before launching BEAST. (Do **not** install the browser Java from java.com - it won't run BEAST.)

## Step B1 - Install BEAST (BEAUti + BEAST + TreeAnnotator + TreeStat + LogCombiner)

1. Download the BEAST X Windows ZIP from the official release page:
   [https://github.com/beast-dev/beast-mcmc/releases/latest](https://github.com/beast-dev/beast-mcmc/releases/latest)
   (Look under **Assets** for a file named like `BEAST.X.v10.5.0.zip`. Direct link for v10.5.0: <https://github.com/beast-dev/beast-mcmc/releases/download/v10.5.0/BEAST.X.v10.5.0.zip>)
2. The file lands in your `Downloads` folder.
3. Right-click the `.zip` ‚Üí **Extract All** ‚Üí confirm.
4. Open the extracted folder. The executables are **directly inside** (no `bin\` subfolder):
    - `BEAUti.exe`
    - `BEAST.exe`
    - `TreeAnnotator.exe`
    - `TreeStat.exe`
    - `LogCombiner.exe`
5. Double-click any of them to launch.

> *(Optional)* Right-click `BEAUti.exe` and `TreeAnnotator.exe` ‚Üí **Pin to Start** or send a shortcut to the desktop so you don't have to dig into the folder each time.

### BEAGLE library (recommended for BEAST performance)

BEAGLE significantly speeds up BEAST. Unlike the other apps, BEAGLE *does* use an installer (`.msi`) because it registers a system library.

1. Download the Windows BEAGLE `.msi` directly:
   <https://github.com/beagle-dev/beagle-lib/releases/download/v4.0.0/BEAGLE-4.0.0-win64.msi>
   (Or check <https://github.com/beagle-dev/beagle-lib/releases> for a newer version.)
2. Double-click the `.msi` in your `Downloads` folder and accept the default settings.
3. BEAST will detect and use BEAGLE automatically the next time you start a run.

---

## Step B2 - Install Tracer

1. Open <https://github.com/beast-dev/tracer/releases/tag/v1.7.2>.
2. Under **Assets**, download the Windows `.zip` (file name like `Tracer.v1.7.2.zip`).
3. The file lands in your `Downloads` folder.
4. Right-click the `.zip` ‚Üí **Extract All** ‚Üí confirm.
5. Inside the extracted folder, double-click `Tracer.exe` (directly in the folder - no `bin\`).

Tracer is used to inspect BEAST MCMC log files.

---

## Step B3 - Install SplitsTree6

1. Open the [SplitsTree6 v6.7.9 release page](https://github.com/husonlab/splitstree6/releases/tag/v6.7.9).
2. Under **Assets**, download the Windows `.zip`.
3. Right-click the downloaded `.zip` in your `Downloads` folder ‚Üí **Extract All**.
4. Inside the extracted folder, double-click `SplitsTree.exe` to launch.

---

## Step B4 - Install PhyloSketch2

1. Open the [PhyloSketch2 v2.2.12 release page](https://github.com/husonlab/phylosketch2/releases/tag/v2.2.12).
2. Under **Assets**, download the Windows `.zip`.
3. Right-click the downloaded `.zip` in your `Downloads` folder ‚Üí **Extract All**.
4. Inside the extracted folder, double-click `PhyloSketch2.exe` to launch.

---

## Step B5 - Install PhyloCompare

1. Open <https://github.com/husonlab/phylocompare/releases/tag/v1.0.1>.
2. Under **Assets**, download the Windows `.zip` (file name like `PhyloCompare-1.0.1-windows-x86_64.zip`).
3. Right-click the downloaded `.zip` in your `Downloads` folder ‚Üí **Extract All**.
4. Inside the extracted folder, open `bin\` and double-click `PhyloCompare.exe` to launch.

---

> **Tip:** for any of these apps, after the first launch you can right-click the `.exe` ‚Üí **Pin to Start** or **Create shortcut** ‚Üí drag the shortcut to your desktop. This way you don't have to navigate into the extracted folder every time.

---

# Verifying the installation

## In WSL Ubuntu (with `tutorial` env active):

```bash
iqtree3 --version
astral --help
python -c "import ete3; print('ete3', ete3.__version__)"
```

All three should run cleanly.

## On native Windows:

Open each `.exe` from inside its extracted folder (or via a shortcut you made) and confirm the window appears:

- `BEAUti.exe` (in extracted BEAST folder, root)
- `BEAST.exe` (in extracted BEAST folder, root)
- `TreeAnnotator.exe` (in extracted BEAST folder, root)
- `Tracer.exe` (in extracted Tracer folder, root)
- `SplitsTree.exe` (in extracted SplitsTree folder)
- `PhyloSketch2.exe` (in extracted PhyloSketch2 folder)
- `PhyloCompare.exe` (in extracted PhyloCompare folder, in `bin\`)

Close each one after confirming.

---

# Quick reference - what runs where

| Tool | Where | How to launch |
|---|---|---|
| IQ-TREE 3 | WSL Ubuntu | `iqtree3 ...` in Ubuntu terminal |
| ASTRAL | WSL Ubuntu | `astral ...` in Ubuntu terminal |
| ete3 (Python) | WSL Ubuntu | `import ete3` in Python |
| Helper scripts (`tools/...`) | WSL Ubuntu | `python tools/...` |
| BEAUti | Native Windows | `BEAUti.exe` in extracted BEAST folder |
| BEAST | Native Windows | `BEAST.exe` in extracted BEAST folder |
| TreeAnnotator | Native Windows | `TreeAnnotator.exe` in extracted BEAST folder |
| Tracer | Native Windows | `Tracer.exe` in extracted Tracer folder |
| SplitsTree6 | Native Windows | `SplitsTree.exe` in extracted SplitsTree folder |
| PhyloSketch2 | Native Windows | `PhyloSketch2.exe` in extracted PhyloSketch2 folder |
| PhyloCompare | Native Windows | `bin\PhyloCompare.exe` in extracted PhyloCompare folder |

---

# Accessing WSL files from Windows (and vice versa)

Because you cloned the tutorial inside WSL (`~/trees-to-networks-tutorial`), the files live on a Linux filesystem - **not** on `C:\` or your Windows Desktop. To open them in a Windows GUI app (BEAUti, Tracer, SplitsTree, etc.) you have to point Windows at the WSL filesystem.

## From Windows Explorer (the easy way)

1. Open **File Explorer**.
2. In the address bar, type:
   ```
   \\wsl$\Ubuntu\home\<your-wsl-username>\trees-to-networks-tutorial
   ```
   Replace `<your-wsl-username>` with the WSL username you set when you first launched Ubuntu.
3. Press Enter. You'll see the tutorial files just like a normal folder.
4. *(Optional, recommended)* Right-click the folder ‚Üí **Pin to Quick access**, so it shows up in the File Explorer sidebar. From now on you can get there in one click.

## From a Windows GUI app's "Open File" dialog

When BEAUti / Tracer / SplitsTree opens its file picker:

1. Click in the **path bar at the top** of the dialog.
2. Paste:
   ```
   \\wsl$\Ubuntu\home\<your-wsl-username>\trees-to-networks-tutorial
   ```
3. Press Enter. You can now browse and select the tutorial files (e.g. `.fasta`, `.nex`, `.treefile`, `.xml`).

> **Tip:** to find `<your-wsl-username>` quickly, run `whoami` inside WSL Ubuntu.

## From WSL into Windows folders

The reverse direction is just as easy. Your Windows drives are mounted under `/mnt/` in WSL:

- `C:\` ‚Üí `/mnt/c/`
- `D:\` ‚Üí `/mnt/d/`
- Your Windows `Downloads` folder ‚Üí `/mnt/c/Users/<your-windows-username>/Downloads/`

So if you ever need to copy a file from `Downloads` into the tutorial folder:

```bash
cp /mnt/c/Users/<your-windows-username>/Downloads/somefile.xml ~/trees-to-networks-tutorial/
```

## Recommended workflow

- Keep the tutorial folder where it is (in WSL: `~/trees-to-networks-tutorial`).
- Run all CLI tools (IQ-TREE, ASTRAL, Python scripts) from inside WSL - they're fast on the WSL filesystem.
- When you need to open a file in a Windows GUI app, use the `\\wsl$\Ubuntu\...` path.
- Avoid moving the tutorial folder onto `/mnt/c/`; CLI tools run noticeably slower against the Windows filesystem.
