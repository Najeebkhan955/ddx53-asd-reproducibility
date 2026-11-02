# DDX53 in Autism Spectrum Disorder — Reproducibility Repository

**Public research repository** for the exploratory DDX53–ASD study, covering a descriptive reanalysis of GEO GSE129808 RNA-seq data, structure-informed AMP pose comparisons, archived six-ligand molecular docking results, Desmond molecular-dynamics (MD) export reanalysis, and author-supplied ADMET predictions.

> **Scope:** This repository provides source inputs, derived numerical data, figures and scripted reanalyses. It does **not** independently reproduce the original Vina docking jobs, a complete 100-ns Desmond simulation, or third-party ADMET model inference. AMP pose recovery used crystal-/template-associated inputs; it is **not** a blind, template-free redocking validation.

## Where to find the files

| Folder | Deposited contents |
|---|---|
| `data/original/` | Original GSE129808 HTSeq archive (`GSE129808_RAW.tar`) |
| `data/structure/` | PDB 3IUY, extracted crystallographic AMP A160, prepared DDX53 receptor, preparation log |
| `data/docking_amp/` | Three CB-Dock2 AMP runs (six pose/complex PDB exports) |
| `data/docking_six/` | Six author-provided docked protein–ligand complexes (legacy filenames preserved) |
| `data/md_exports/` | S6 (1,001-frame MD descriptors), S7 contacts, S8 settings, archived MD reports |
| `data/other_exports/` | S1, S2, S5 (six ligands, 54 poses), S9 ADMET and S11 AMP comparison CSVs |
| `data/derived/` | Supplementary S1–S11 Excel workbook |
| `results/` | **Full 60,617-gene S3 raw-counts and S4 descriptive CPM matrices**, analysis JSON and CSV reports |
| `scripts/` | `01`–`07` Python reanalysis/audit scripts and `run_all.py` |
| `figures/docking_six/` | Twelve original ligand-interaction and LigPlot graphics |
| `figures/md_original/` | Fourteen original MD plot PNGs from the author |
| `figures/` | Three optional derived supplementary PNG exports are not yet deposited; some plots regenerate from scripts |

For a detailed inventory and limitations, see [REPOSITORY_STATUS.md](REPOSITORY_STATUS.md). For manuscript-ready wording, see [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md).

## Run the deposited source-derived reanalyses

Use Python 3.10+ and the committed source files:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py
```

The scripts regenerate or audit source-derived tabular values and plots. A previously recorded **local** execution of the same script and source-file versions completed the seven analysis stages and reported **9/9 integrity checks passed**.

## Sources and scientific interpretation

- **RNA-seq:** [NCBI GEO GSE129808](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129808); seven libraries from three donors, 60,617 Ensembl features. DDX53 (ENSG00000184735.6) has 11 assigned reads total across the seven libraries.
- **Structure:** [RCSB PDB 3IUY](https://www.rcsb.org/structure/3IUY) is the DDX53 DEAD-box domain. The crystallographic AMP A160 was used in pose comparisons.
- **AMP audit:** The first pose in the crystal-site-associated run gave 1.908 Å heavy-atom pose RMSD versus crystal AMP.
- **Focused docking audit:** Six archived ligand series (54 pose scores) are computational predictions.
- **MD:** Derived carebastine results show substantial ligand displacement; archived figures and numerical summaries should not be interpreted as continuous binding-site occupancy.
- **ADMET:** Author-supplied predictions were checked for provenance; they were not experimentally measured or independently recomputed.

### Original complex filenames

The original protein–ligand complexes use filenames beginning with `6IUY-`, while the manuscript's target structure is **3IUY**. These names were retained unchanged to preserve source provenance. Preliminary residue-sequence and internal geometry comparisons are consistent with the 3IUY protein fragment (213 shared chain-A Cα residue identities, no mismatches in that comparison).

## How to cite

**Manuscript data-availability link:** https://github.com/Najeebkhan955/ddx53-asd-reproducibility

This is a public GitHub link, **not** a DOI. A versioned GitHub release and subsequent Zenodo archival are recommended for a permanently citable research-data DOI. Do not use a fabricated DOI.

