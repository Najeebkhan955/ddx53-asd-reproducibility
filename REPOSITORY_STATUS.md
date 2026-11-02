# GitHub repository verification and completion status

Updated 2 November 2026 following the final upload and folder arrangement.

## Deposited and organized

- [x] 8 Python files under `scripts/`: seven stages plus `run_all.py`.
- [x] Original source archive: `data/original/GSE129808_RAW.tar`.
- [x] Original structural inputs: `data/structure/3IUY.pdb`, AMP A160 reference and prepared DDX53 receptor.
- [x] Three AMP docking runs: six PDB pose and complex files under `data/docking_amp/`.
- [x] Six historic docking-complex PDB files under `data/docking_six/`.
- [x] Raw MD numeric exports (S6, S7, S8), source report files and 14 author-original MD figures under `figures/md_original/`.
- [x] S1, S2, S5, S9, S11 source tables under `data/other_exports/`.
- [x] S3 full 60,617-gene raw-count CSV and S4 full 60,617-gene descriptive CPM CSV under `results/`.
- [x] S1–S11 Excel workbook under `data/derived/`.
- [x] 12 original six-ligand docking interaction figures under `figures/docking_six/`.
- [x] `README.md`, `DATA_AVAILABILITY.md`, `requirements.txt` and source-derived numerical audit reports.

## Optional figure files not yet deposited

- [ ] `figures/Supp_Figure_S1_AMP_Pose_RMSD.png`
- [ ] `figures/Supp_Figure_S2_MD_RMSD.png`
- [ ] `figures/Supp_Figure_S3_DDX53_Counts.png`

These three supplementary illustrations were in a previously supplied image ZIP; their absence does **not** invalidate the source-derived numerical workflow, and the plotting scripts can regenerate core plots.

## Evidence and limitations

- **Local source-derived run:** seven analysis stages completed; `results/REPRODUCIBILITY_REPORT.json` reports **9/9 PASS** (GEO archive hash, S3/S4 regeneration and hashes, count dimensions, AMP pose count, MD frame count, six ligand docking summaries).
- **Remote tree verification:** all documented core input, derived data, script and originally uploaded MD plot paths confirmed; folder moves preserve Git blob SHA.
- **Not verified independently:** all workbook sheet values, original complete Vina configurations/reruns, Desmond trajectory simulation rerun, ADMET prediction service or any claim of experimental drug affinity.
- **AMP validation caution:** template/crystal-informed pose placement; no independent blind redocking.
- **File-name caution:** six complex files are historically prefixed `6IUY` but study references 3IUY. Do not silently rename or overstate run provenance.
- **Licensing:** public availability does not itself grant reuse rights; verify authorship and redistribution terms.
- **Archival DOI:** no Zenodo DOI or public GitHub Release assigned at the time of this update. A stable release and actual DOI should precede any DOI citation in the manuscript.

See [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md) for exact manuscript wording.
