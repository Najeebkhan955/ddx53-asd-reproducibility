#!/usr/bin/env python3
"""Check source hashes, full S3/S4 integrity and all expected analysis outputs."""
import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
IN=ROOT/'data';OUT=ROOT/'results'
EXPECTED_SOURCE_SHA='80e0e539b87720065f81c378a7bb8a54557ee6abf8e850d185a171a8543918cd'
EXPECTED_S3_SHA='ba304790f68b7888da2f2f58e06ed02419994dfbbae0441690d4ee6f017ee963'
EXPECTED_S4_SHA='97e49ab512d009a510f3a0984e8cd29314cf56441ffcf2bef332395a897aae2a'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for part in iter(lambda:f.read(1024*1024),b''):h.update(part)
    return h.hexdigest()
def data_rows(p):
    with p.open(encoding='utf-8',newline='') as f:return sum(1 for _ in csv.reader(f))-1

def main():
    checks={
      'original_GEO_TAR_SHA256_matches':sha(IN/'original/GSE129808_RAW.tar')==EXPECTED_SOURCE_SHA,
      'generated_S3_SHA256_matches_original_verified_export':sha(OUT/'ASD_Table_S3_All_60617_Genes_Raw_HTSeq_Counts.csv')==EXPECTED_S3_SHA,
      'generated_S4_SHA256_matches_original_verified_export':sha(OUT/'ASD_Table_S4_All_60617_Genes_Descriptive_CPM.csv')==EXPECTED_S4_SHA,
      'S3_features_60617':data_rows(OUT/'ASD_Table_S3_All_60617_Genes_Raw_HTSeq_Counts.csv')==60617,
      'S4_features_60617':data_rows(OUT/'ASD_Table_S4_All_60617_Genes_Descriptive_CPM.csv')==60617,
      'AMP_27_poses':data_rows(OUT/'AMP_all_27_poses_crystal_comparison.csv')==27,
      'MD_1001_frames':data_rows(IN/'md_exports/S6_1001_MD_frames.csv')==1001,
      'S5_six_ligands_54_poses':data_rows(IN/'other_exports/S5_focused_docking_54.csv')==54,
      'six_ligand_summary':data_rows(OUT/'Six_ligand_focused_docking_summary.csv')==6,
    }
    missing_methods={'full_Desmond_MD_reproduction':'Requires original .cms/.dtr, system topology and logs, not provided.',
     'ADMET_model_prediction_reproduction':'Requires original service inputs/output logs/model versions, not provided.',
     'six_ligand_AutoDock_Vina_rerun':'Requires all original prepared receptor/ligand PDBQT, config, seeds and execution logs.',
     'CB-Dock2_independent_redocking':'Template-matched AMP input used; original crystal AMP site is not prospectively blinded.'}
    report={'checks':checks,'passed':all(checks.values()),'not_reproducible_from_current_inputs':missing_methods}
    (OUT/'REPRODUCIBILITY_REPORT.json').write_text(json.dumps(report,indent=2))
    print('INTEGRITY:',sum(checks.values()),'/',len(checks),'checks passed')
    if not all(checks.values()):
        for k,v in checks.items():
            if not v:print('FAILED:',k)
        raise SystemExit(1)
if __name__=='__main__':main()
