#!/usr/bin/env python3
"""Run the deposited reproducibility audit with a single command."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
jobs=['01_rebuild_S3_S4.py','02_rnaseq_figures.py','03_amp_crystal_pose_audit.py',
      '04_six_ligand_docking_audit.py','05_MD_export_reanalysis.py',
      '06_ADMET_provenance_audit.py','07_verify_repo_integrity.py']
for file in jobs:
    print('\n### Running',file,flush=True)
    subprocess.run([sys.executable,str(root/file)],check=True)
print('\nALL AVAILABLE SOURCE-DERIVED REANALYSES COMPLETED. Read README for scientific limits.')
