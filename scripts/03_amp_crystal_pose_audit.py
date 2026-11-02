#!/usr/bin/env python3
"""Compare 27 CB-Dock2 AMP poses to original PDB 3IUY AMP A160.

Important: NO ligand superposition is used for POSE RMSD. The separate
Kabsch-fitted ligand-only RMSD is a conformational, NOT pocket-pose, metric.
The template-guided run references 3IUY: no claim of independent validation.
"""
import csv,json,hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/'data/docking_amp'; OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
REF=ROOT/'data/structure/AMP_A160_crystal_reference.pdb'
RUNS={
 'DDX53_3IUY_chainA_no_hetero_AMP_A160_crystal_reference_out_6.-6.9.pdb':('Crystal-site custom / template caveat',-6.9),
 'DDX53_3IUY_chainA_no_hetero_AMP_A160_crystal_reference_out_1.-6.1.pdb':('Alternative pocket A',-6.1),
 'DDX53_3IUY_chainA_no_hetero_AMP_A160_crystal_reference_out_4.-6.1.pdb':('Alternative pocket B',-6.1),
}
def models(fp):
    all_models=[]; now=[]; had_model=False
    for line in fp.read_text().splitlines():
        if line.startswith('MODEL '):had_model=True;now=[]
        elif line.startswith('ENDMDL'):all_models.append(now);now=[]
        elif line.startswith(('ATOM  ','HETATM')):
            atom=line[12:16].strip();element=(line[76:78].strip() or ''.join(c for c in atom if c.isalpha())[:1]).upper()
            if element in ('H','D'):continue
            if atom in {v[0] for v in now}:raise ValueError('Duplicate atom name: '+atom)
            now.append((atom,element,np.array([float(line[s:s+8]) for s in (30,38,46)])))
    if not had_model:all_models=[now]
    return all_models

def compare(ref,pose):
    a={n:(e,xyz) for n,e,xyz in ref};b={n:(e,xyz) for n,e,xyz in pose}
    if set(a)!=set(b) or len(a)!=23:raise ValueError('AMP atom identity mismatch or not 23 heavy atoms')
    names=sorted(a)
    if any(a[n][0]!=b[n][0] for n in names):raise ValueError('Element mismatch')
    A=np.stack([a[n][1] for n in names]);B=np.stack([b[n][1] for n in names])
    distance=np.linalg.norm(A-B,axis=1); ac=A.mean(0);bc=B.mean(0)
    U,_,Vt=np.linalg.svd((B-bc).T@(A-ac)); D=np.eye(3);D[-1,-1]=np.linalg.det(U@Vt)
    fitted=(B-bc)@U@D@Vt
    return len(names),float(np.sqrt(np.mean(distance**2))),float(np.linalg.norm(ac-bc)),float(np.sqrt(np.mean(np.linalg.norm(fitted-(A-ac),axis=1)**2))),float(distance.max())

def main():
    ref=models(REF)[0]; rows=[]; summary=[]
    for filename,(label,score) in RUNS.items():
        poses=models(P/filename)
        if len(poses)!=9:raise ValueError(f'{filename}: expected 9 poses')
        for number,pose in enumerate(poses,1):
            n,rmsd,centroid,internal,maxdist=compare(ref,pose)
            rows.append([filename,label,score,number,n,f'{rmsd:.9f}',f'{centroid:.9f}',f'{internal:.9f}',f'{maxdist:.9f}',int(rmsd<=2)])
        summary.append({'run':label,'reported_run_best_Vina_score_kcal_mol':score,
                        'first_pose_RMSD_A':float(rows[-9][5]),'lowest_RMSD_among_9_A':min(float(x[5]) for x in rows[-9:])})
    path=OUT/'AMP_all_27_poses_crystal_comparison.csv'
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['source_pose_file','run_category','reported_best_score_FOR_RUN_only_kcal_mol',
        'pose_index','matched_heavy_atoms','pose_RMSD_A_NO_ligand_alignment','centroid_displacement_A',
        'ligand_only_superposed_RMSD_A_NOT_pose','maximum_atom_displacement_A','within_2A']);w.writerows(rows)
    first=[r for r in rows if r[1].startswith('Crystal-site') and r[3]==1][0]
    second=[r for r in rows if r[1].startswith('Crystal-site') and r[3]==2][0]
    assert abs(float(first[5])-1.908)<0.01 and abs(float(second[5])-0.394)<0.01
    report={'reference':'AMP A160 from experimental PDB 3IUY Chain A','matched_heavy_atoms':23,
       'comparison':'Coordinate-frame RMSD without ligand superposition','run_summaries':summary,
       'warning':'Crystal-site run listed 3IUY as a CB-Dock2 template; the original crystal AMP was input. Not independent template-excluded redocking.',
       'warning2':'Scores are the reported BEST PER RUN, not measured affinities and not per-pose scores for modes 2-9.'}
    (OUT/'AMP_pose_audit.json').write_text(json.dumps(report,indent=2))
    plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(9,4.5))
    for label in dict((x[1],None) for x in rows):
        sub=[r for r in rows if r[1]==label];ax.plot([r[3] for r in sub],[float(r[5]) for r in sub],marker='o',label=label)
    ax.axhline(2,color='black',ls='--',lw=1,label='Conventional 2 Å benchmark')
    ax.set(xlabel='Pose index within docking output',ylabel='AMP crystal-pose RMSD (Å)',title='AMP A160 pose comparison: 27 exported poses')
    ax.set_xticks(range(1,10));ax.legend(fontsize=8,loc='best');ax.grid(alpha=.15)
    fig.tight_layout();fig.savefig(OUT/'figures/AMP_27_pose_RMSD.png',dpi=250);plt.close(fig)
    print('PASS AMP pose audit:',len(rows),'poses; crystal-site first pose',first[5],'Å')

if __name__=='__main__':main()
