# Repository completion and source-input checklist

Verified against the GitHub `main` tree on 2026-11-02. The existing files have been organized into folders without changing the content of the moved files.

## Already present
- [x] Seven analysis scripts plus `run_all.py`, all under `scripts/`
- [x] **Complete** S3 original HTSeq count matrix: `results/ASD_Table_S3_All_60617_Genes_Raw_HTSeq_Counts.csv`
- [x] **Complete** S4 normalized CPM/log₂ matrix: `results/ASD_Table_S4_All_60617_Genes_Descriptive_CPM.csv`
- [x] Supplementary S1–S11 workbook: `data/derived/Supplementary_S1S11.xlsx`
- [x] Six historic docking-complex PDB files: `data/docking_six/`
- [x] Interaction drawings: `figures/docking_six/`
- [x] Archived carebastine MD report outputs: `data/md_exports/`
- [x] Numerical result-audit JSON/CSV files: `results/`

## Source files still needed for **end-to-end script execution**
- [ ] `data/original/GSE129808_RAW.tar` — seven sample HTSeq archive. [Original GEO download](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE129nnn/GSE129808/suppl/GSE129808_RAW.tar)
- [ ] `data/structure/3IUY.pdb` — unmodified original crystallographic structure. [RCSB 3IUY](https://www.rcsb.org/structure/3IUY)
- [ ] `data/structure/AMP_A160_crystal_reference.pdb` — extracted AMP A160 reference coordinates.
- [ ] `data/docking_amp/` — three nine-pose CB-Dock2 AMP docking PDB exports: `...out_6.-6.9.pdb`, `...out_1.-6.1.pdb`, and `...out_4.-6.1.pdb` (names defined in `scripts/03_amp_crystal_pose_audit.py`).
- [ ] `data/md_exports/S6_1001_MD_frames.csv` and `S7_MD_contact_occupancies.csv` (plus settings file `S8_MD_settings_and_audit.csv`).
- [ ] `data/other_exports/S5_focused_docking_54.csv` and `S9_ADMET_author_supplied.csv` (S1, S2 and S11 are also useful for full supplementary traceability).

These are **input files**; the published S3/S4 and audit results do not replace the original source files needed to rerun the script workflow. Until these are uploaded, `python scripts/run_all.py` is not expected to finish successfully. The missing MD numerical exports are distinct from the deposited `.eaf/.log/.pdf` files.

## Before citing a DOI
1. Validate that all listed source files are present and correctly attributed.
2. Run `python scripts/run_all.py` and verify the integrity report.
3. Confirm whether `6IUY-*` filenames refer to structures actually derived from PDB 3IUY; do **not** silently rename ambiguous files.
4. Confirm permissions for public sharing of author-created and third-party exports.
5. Create a versioned GitHub release, archive via Zenodo if a DOI is needed, and insert the **actual assigned DOI** in the manuscript and reviewer response.

### Scientific validation boundary
The FitDock/CB-Dock2 AMP calculations were template-associated or crystal-pose informed; these should not be represented as independent de novo redocking. Desmond summary reanalysis does not replace a simulation rerun. ADMET export checking is not prospective model validation.
