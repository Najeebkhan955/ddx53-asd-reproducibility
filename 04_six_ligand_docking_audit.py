#!/usr/bin/env python3
"""Reanalyze provided 54 archived Vina pose scores (NOT rerun actual docking)."""
import csv,json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'data/other_exports/S5_focused_docking_54.csv';O=ROOT/'results';O.mkdir(exist_ok=True)
def main():
    by=defaultdict(list)
    with P.open(encoding='utf-8',newline='') as f:
        for r in csv.DictReader(f):by[r['compound']].append(r)
    if len(by)!=6 or sum(map(len,by.values()))!=54:raise ValueError('Require 6 compounds x 9 archived Vina poses')
    rows=[]
    for ligand,poses in by.items():
        if sorted(int(x['mode']) for x in poses)!=list(range(1,10)):raise ValueError('Unexpected mode labels for '+ligand)
        energies=[float(x['vina_score_kcal_mol']) for x in poses]
        rows.append([ligand,poses[0]['PubChem_CID'],len(poses),min(energies),max(energies),poses[0]['source_pdbqt']])
    rows.sort(key=lambda r:r[3])
    with (O/'Six_ligand_focused_docking_summary.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['ligand','CID','num_poses','best_Vina_score_kcal_mol','worst_pose_score','archived_original_PDBQT_filename']);w.writerows(rows)
    (O/'Six_ligand_docking_audit.json').write_text(json.dumps({'ligands':len(rows),'archived_poses':54,'ranked':rows,
      'caveat':'Archived scores, no protein-ligand affinity measurement, original PDBQT files not included for independent redocking.'},indent=2))
    assert rows[0][0].lower()=='carebastine' and abs(rows[0][3]-(-7))<.001
    print('PASS focused docking: 6 ligands, 54 poses; best archived carebastine -7.0 kcal/mol')
if __name__=='__main__':main()
