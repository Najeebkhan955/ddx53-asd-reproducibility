# DDX53 in Autism Spectrum Disorder — Reproducibility Repository

This repository organizes the available materials for an exploratory, donor-aware transcriptomic reassessment and source-derived docking, molecular-dynamics (MD), and ADMET analyses of DDX53 in ASD.

**Current state:** The complete S3/S4 matrices, S1–S11 workbook, all eight Python script files, archived docking-complex files, MD report exports and associated output tables are hosted here. Some original inputs required to **rerun all scripts from source** have not yet been deposited. See [REPOSITORY_STATUS.md](REPOSITORY_STATUS.md) for the exact checklist. No DOI has been assigned.

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
| `data/md_exports/` | Uploaded carebastine–DDX53 MD/report files; original 1,001-frame S6 and S7 tables still need depositing |
| `data/structure/` | Uploaded receptor-preparation log; original PDB 3IUY and extracted AMP reference still need depositing |
| `figures/docking_six/` | Original uploaded ligand-interaction and LigPlot figures |

Source folders to populate: `data/original/` (GEO TAR), `data/docking_amp/` (three CB-Dock2 AMP pose outputs), `data/other_exports/` (S5/S9 etc.). These paths are required by the scripts; see the status checklist before running them.

**Note:** Some historical files are named `6IUY-...`, although the reported target is PDB **3IUY**. Original filenames were intentionally retained and their molecular identity/coordinates must be checked before citing them; a filename is not proof of receptor identity.

## Key results and boundaries

- GSE129808: seven libraries, **60,617** Ensembl features; 17,061 pass CPM ≥1 in at least two libraries.
- DDX53 (ENSG00000184735.6) original read counts: **3, 1, 1, 1, 5, 0, 0** (11 total). Repeated libraries do **not** constitute independent ASD donor replication; no donor-independent DEG or classification claim is supported.
- Archived six-ligand focused Vina outputs: 54 modes; carebastine recorded first-mode score −7.0 kcal/mol. Docking scores do **not** prove binding, inhibition or treatment effectiveness.
- AMP crystal-site CB-Dock2 first-pose heavy-atom RMSD 1.908 Å against crystal AMP A160 (second pose 0.394 Å). The crystal ligand was supplied and 3IUY appeared as a template; this is **not independent template-free redocking validation**.
- Archived 100-ns Desmond derived metrics: mean protein-aligned carebastine RMSD approximately 10.82 Å; do not claim continuous occupancy of its initial pose.
- ADMET entries are prior computational predictions, not experimentally measured pharmacokinetic endpoints.

## Reproduction

After depositing the original inputs listed in [REPOSITORY_STATUS.md](REPOSITORY_STATUS.md):

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py
```

The scripts regenerate or audit numerical outputs from source archives and exports. They do **not** rerun the original Desmond MD simulation, all six Vina docking jobs or the originating ADMET prediction service. Relevant project/trajectory, docking configuration and original service records are required to reproduce those software computations.

S3 and S4 were checked against the corresponding prepared source-derived exports by their exact Git blob hashes, with no changes during repository reorganization. Supplementary data and scripts are provided for research traceability; all findings require appropriately qualified interpretation.

## License, authorship and permanent archive

The underlying GEO/PDB entries retain their source attribution and reuse terms; permission for author-generated simulation/docking outputs should be confirmed. A public GitHub URL is not a DOI. After data-provenance and file-integrity review, a versioned GitHub release can be archived through Zenodo to obtain a DOI.

**Repository maintenance:** This folder reorganization preserved file contents and retained the six legacy `6IUY` prefixes pending structure-level verification.
