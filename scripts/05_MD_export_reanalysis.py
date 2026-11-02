#!/usr/bin/env python3
"""Reanalyse archived numerical Desmond exports in S6/S7/S8.

These exports are NOT the original Desmond trajectory (.dtr/.cms). This script
reproduces descriptive metrics from exported arrays, NOT molecular dynamics.
"""
import csv,json,statistics
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'data/md_exports';OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
def rows(path):
    with path.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def main():
    frames=rows(D/'S6_1001_MD_frames.csv');contacts=rows(D/'S7_MD_contact_occupancies.csv')
    if len(frames)!=1001:raise ValueError('Expected 1,001 frames (0 through 1000)')
    if [int(r['frame']) for r in frames]!=list(range(1001)):raise ValueError('Unexpected frame indices')
    time=np.asarray([float(r['time_ns']) for r in frames]);
    if abs(time[-1]-100)>0.001:raise ValueError('Expected 100 ns duration')
    metrics={
     'protein_CA_RMSD': 'Protein_CA_RMSD_A',
     'protein_backbone_RMSD':'Protein_Backbone_RMSD_A',
     'ligand_protein_aligned_RMSD':'Ligand_ProteinAligned_RMSD_A',
     'ligand_self_aligned_RMSD':'Ligand_LigandAligned_RMSD_A',
    }
    report={'source':'single pre-existing archived Desmond export S6/S7/S8',
            'number_of_frames':len(frames),'production_time_ns':float(time[-1]),
            'RMSD_summary_excludes_initial_frame':True,
            'note':'This analysis does not simulate a system or establish equilibrium binding affinity.'}
    for name,col in metrics.items():
        values=np.asarray([float(r[col]) for r in frames])
        report[name]={'mean_A':float(values[1:].mean()),'SD_population_A':float(values[1:].std()),
                        'range_min_A':float(values[1:].min()),'range_max_A':float(values[1:].max())}
    arr=np.asarray([float(r['Ligand_ProteinAligned_RMSD_A']) for r in frames[1:]])
    report['ligand_protein_aligned_RMSD_fraction_postinitial_over_5A']=float((arr>5).mean())
    categories={
      'HBond':'contacts_HBond','Hydrophobic':'contacts_Hydrophobic',
      'WaterBridge':'contacts_WaterBridge','Ionic':'contacts_Ionic',
      'Pi-Cation':'contacts_Pi-Cation','Pi-Pi':'contacts_Pi-Pi','Metal':'contacts_Metal'
    }
    for label,col in categories.items():
        count=int(sum(float(r[col])>0 for r in frames))
        report['fraction_frames_with_'+label]=count/len(frames)
    report['frames_with_any_contact']=int(sum(any(float(r[v])>0 for v in categories.values()) for r in frames))
    report['contact_residue_rows']=len(contacts)
    errors=[]
    for r in contacts:
        num=int(float(r['Frames_with_contact']));pct=float(r['Percent_of_frames'])
        if abs(pct-100*num/1001) > 0.11:errors.append((r['Interaction_type'],r['Residue']))
    report['S7_occupancy_rounding_disagreements']=errors
    (OUT/'MD_export_descriptive_audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(9.1,4.1))
    ax.plot(time,np.asarray([float(r['Protein_CA_RMSD_A']) for r in frames]),label='Protein Cα RMSD',lw=1.1)
    ax.plot(time,np.asarray([float(r['Ligand_ProteinAligned_RMSD_A']) for r in frames]),label='Protein-aligned ligand RMSD',lw=1.1)
    ax.set(xlabel='Time (ns)',ylabel='RMSD (Å)',title='Carebastine–DDX53 | archived single 100-ns Desmond export')
    ax.legend();ax.grid(alpha=.17);fig.tight_layout();fig.savefig(OUT/'figures/MD_archived_RMSD_time_series.png',dpi=250);plt.close(fig)
    assert report['frames_with_any_contact']==794,report['frames_with_any_contact']
    print('PASS MD export audit: 1001 frames, ligand RMSD mean',round(report['ligand_protein_aligned_RMSD']['mean_A'],3),'Å')
    if errors: print('CAUTION: S7 occupancy disagreements:',errors[:5])
if __name__=='__main__':main()
