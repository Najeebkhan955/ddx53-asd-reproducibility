# Manuscript-ready Data Availability statement

## Recommended statement (before DOI assignment)

The reanalysis scripts, data-processing documentation, complete GSE129808-derived raw-count (Table S3; 60,617 gene features) and normalized expression (Table S4) matrices, supplementary tables (S1–S11), crystallographic DDX53/AMP reference inputs, deposited molecular-docking exports, and source-derived MD and ADMET audit outputs are publicly available in the GitHub repository **DDX53 in Autism Spectrum Disorder — Reproducibility Repository** (https://github.com/Najeebkhan955/ddx53-asd-reproducibility; accessed 2 November 2026). The original RNA-seq series is independently accessible from NCBI GEO under accession GSE129808, and the DDX53 crystal structure under PDB ID 3IUY. The deposited scripts reproduce or audit the available derived analyses; the original complete Desmond simulation, all Vina docking computations, and the underlying ADMET model predictions cannot be independently rerun from the archived exports alone.

## Recommended source attribution

- GitHub repository: https://github.com/Najeebkhan955/ddx53-asd-reproducibility
- RNA-seq record: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129808
- Crystal structure: https://www.rcsb.org/structure/3IUY

**Important:** The GitHub URL is valid now, but it is not a registered DOI, and `main` can continue changing. If a journal requires permanent archived research data, make a tagged GitHub Release and link it to Zenodo. Replace the GitHub-only statement with the **actual** Zenodo DOI only after Zenodo assigns one. Author identity, publication title, journal and DOI should not be invented.

## Reproducibility qualification

The reported 9/9 integrity verification is from a local reconstruction using the deposited scripts and source-file versions. It checks source archive and regenerated table hashes, feature counts, and selected source-derived numerical outputs, **not** blind AMP redocking, independent molecular dynamics, causal ASD mechanisms or experimental DDX53–ligand affinity.
