# DDX53 in Autism Spectrum Disorder — Reproducibility Repository

Source-traceable analyses supporting the revised exploratory DDX53–ASD study: reanalysis of NCBI GEO GSE129808 HTSeq gene counts, DDX53 expression QC, AMP crystal-pose comparisons, and audits of archived molecular docking, molecular dynamics and ADMET exports.

## Research sources

- [NCBI GEO GSE129808](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129808) — seven libraries from three source donors; original processed counts in `data/original/`.
- [RCSB PDB 3IUY](https://www.rcsb.org/structure/3IUY) — experimentally determined DDX53 DEAD-box domain.
- Citation: Ross et al. (2020), *Biological Psychiatry*, DOI [10.1016/j.biopsych.2019.07.014](https://doi.org/10.1016/j.biopsych.2019.07.014).

## Key data and scientific scope

The complete gene-count matrix includes **60,617 features across seven libraries**. DDX53 (ENSG00000184735.6) has **11 total assigned reads** (3, 1, 1, 1, 5, 0, 0). These data do not support donor-independent ASD differential-expression significance or diagnostic classification.

Archived AMP docking outputs were compared with the crystallographic AMP A160 pose. The crystal-site CB-Dock2 run yielded first-pose heavy-atom RMSD **1.908 Å**; however, the input was crystal AMP and the server indicated 3IUY as a template. **This is not fully independent template-free docking validation.** Archived six-compound scores are predictions, not experimentally measured affinity or DDX53 inhibition. The carebastine MD results describe ligand displacement, not proven stable occupancy.

## Repository organization

- `scripts/` — Python regeneration and integrity-check scripts (seven analyses plus `run_all.py`).
- `data/original/` — GSE129808 processed HTSeq source archive.
- `data/structure/` and `data/docking_amp/` — DDX53 and AMP structure/pose inputs.
- `data/md_exports/`, `data/other_exports/`, `data/derived/` — source-derived tables and archived author exports.
- `results/` — complete S3 (raw counts) and S4 (normalized CPM/log2) CSVs, analysis outputs and plots.
- `figures/` — supplementary figures.

## Reproduce

Python 3.10+:

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py
```

The scripts reanalyze existing GEO counts and archived docking/MD/ADMET data. They do **not** independently rerun the original Desmond trajectory, all six original Vina docking jobs, or ADMET model services; those workflows require additional original files/settings. See the included documentation for data provenance, numerical definitions, run scope and limitations.

## Attribution and permissions

Public GEO/PDB resources retain their original attribution and license conditions. Author-supplied exports require coauthor permission before publication. Code and third-party data are not necessarily governed by the same license.

A GitHub repository URL is not a DOI. For permanent DOI archiving, publish an appropriate release and archive it in Zenodo, then cite the resulting DOI in the manuscript and reviewer response.
