# DDX53 in Autism Spectrum Disorder — Reproducibility Repository

This repository organizes the available materials for an exploratory, donor-aware transcriptomic reassessment and source-derived docking, molecular-dynamics (MD), and ADMET analyses of DDX53 in ASD.

**Current state (2026-11-02):** The original GEO archive, crystal structure, AMP docking inputs, MD numeric exports, focused-docking and ADMET tables, complete S3/S4 matrices, S1–S11 workbook, and eight Python scripts are deposited. In a **local reconstructed copy using byte-identical deposited scripts and core source files**, all seven analysis stages ran successfully and **9/9 integrity checks passed**. These tests do not independently rerun the underlying MD/Vina/ADMET computations. See [REPOSITORY_STATUS.md](REPOSITORY_STATUS.md) for remaining figure and methodological caveats. No DOI has yet been assigned.

## Source studies

- [NCBI GEO GSE129808](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129808) — original processed RNA-seq counts, seven libraries derived from three donors.
- [RCSB 3IUY](https://www.rcsb.org/structure/3IUY) — experimental human DDX53 DEAD-box-domain structure.
- Ross PJ et al. (2020). *Biological Psychiatry*. [doi:10.1016/j.biopsych.2019.07.014](https://doi.org/10.1016/j.biopsych.2019.07.014).

## Organization

| Folder | Contents |
|---|---|
| `scripts/` | 01–07 numerical analyses and `run_all.py` |
| `results/` | Full 60,617-feature S3 raw counts and S4 descriptive CPM/log₂ values; archived quantitative summary outputs |
| `data/derived/` | Supplementary workbook S1–S11 |
| `data/docking_six/` | Uploaded six protein–ligand complex PDB files |
| `data/md_exports/` | Archived MD report files, S6 1,001-frame values, S7 contact occupancies, and S8 settings |
| `data/structure/` | Original PDB 3IUY, extracted AMP A160, prepared receptor and preparation log |
| `figures/docking_six/` | Original uploaded ligand-interaction and LigPlot figures |

Additional source folders: `data/original/` (GEO TAR), `data/docking_amp/` (three  AMP pose outputs), `data/other_exports/` (S1/S2/S5/S9/S11). These inputs have now been deposited at the paths expected by the scripts. Three optional supplementary figures (S1–S3) remain to be uploaded; the scripts can regenerate research plots.


