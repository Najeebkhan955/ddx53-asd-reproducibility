# Repository upload and verification status — 2026-11-02

## Core reproducibility dataset: complete and organized

The GitHub `main` branch was checked after the final 18 source files were uploaded and moved into the documented locations without modifying the underlying file blobs.

- [x] `scripts/`: 01–07 audit/reanalysis scripts and `run_all.py` (8 Python files).
- [x] `data/original/GSE129808_RAW.tar` — 7-library HTSeq source archive.
- [x] `data/structure/3IUY.pdb`, `AMP_A160_crystal_reference.pdb`, and `DDX53_3IUY_chainA_no_hetero.pdb`.
- [x] `data/docking_amp/` — six CB-Dock2 PDB exports from three runs.
- [x] `data/other_exports/` — S1, S2, S5, S9 and S11 CSVs.
- [x] `data/md_exports/` — S6 1,001-frame metrics, S7 contacts, S8 simulation settings, and previous MD reports.
- [x] `results/ASD_Table_S3_All_60617_Genes_Raw_HTSeq_Counts.csv`.
- [x] `results/ASD_Table_S4_All_60617_Genes_Descriptive_CPM.csv`.
- [x] `data/derived/Supplementary_S1S11.xlsx` (presence checked; all spreadsheet worksheets have not been independently audited in this GitHub check).
- [x] `data/docking_six/`: six archived ligand complexes; `figures/docking_six/`: 12 uploaded docking illustrations.

## Numeric and script validation

In a **local reconstructed copy** of the supplied source archive, using byte-identical scripts and primary inputs uploaded to this GitHub repository, `python scripts/run_all.py` exited successfully on 2026-11-02:

- 01 RNA-seq: 60,617 features, 7 libraries, 17,061 features after stated CPM filter; DDX53 11 total counts.
- 02 RNA-seq figures: 4 plots generated.
- 03 AMP docking pose audit: 27 poses; crystal-site first-pose RMSD 1.908177687 Å.
- 04 Six-ligand docking score audit: six ligands × nine modes, best archived carebastine score −7.0 kcal/mol.
- 05 MD export audit: 1,001 frames, mean aligned ligand RMSD 10.817 Å.
- 06 ADMET export audit: 22 author-supplied rows; **not** independent prediction.
- 07 Integrity verification: **9 / 9 PASS**, including original GEO TAR SHA-256, fully regenerated S3 and S4 SHA-256, both 60,617-row counts, AMP, MD and docking source counts.

The `scripts/` copies of 01–07 and `run_all.py`, both full S3/S4 CSV files, and the 18 newly uploaded source files have Git blob hashes matching the local prepared source package. The folder move was performed using those unchanged hashes.

### Optional uploads still missing

- [ ] `figures/Supp_Figure_S1_AMP_Pose_RMSD.png`
- [ ] `figures/Supp_Figure_S2_MD_RMSD.png`
- [ ] `figures/Supp_Figure_S3_DDX53_Counts.png`

These three images were included in the previously supplied `05_Supplementary_Figures.zip`, but are **not presently visible** on the GitHub `main` branch. They do not block `run_all.py`.

Other documentation and generated plots in the original comprehensive package were not all deposited. This checklist does not assert that every file from every previously shared archive is present.

## Scientific and reproducibility caveats

1. Source-derived reconstruction **does not** equal independent re-execution of the original 100 ns Desmond MD experiment, the six Vina docking jobs, or original ADMET prediction service.
2. AMP pose recovery used crystal ligand/template-associated input, so do not call it blind or template-free redocking validation.
3. Docking complex files historically named `6IUY-*` need receptor provenance and structure-level verification before presentation as PDB 3IUY-derived complexes. Filenames remain unchanged to preserve provenance.
4. DDX53 low counts and repeated donor libraries limit statistical inference.
5. Confirm that author-produced or third-party outputs may lawfully be public, document software/parameter provenance, and assign a license only once approved.
6. **GitHub repository is not a DOI**. No Zenodo DOI is assigned here. Following final source/figure checks, create a versioned GitHub Release and archive it in Zenodo.

See [README.md](README.md) for scope and command-line execution instructions.
