#!/usr/bin/env python3
"""Descriptive GEO library plots, with donor limitations made explicit (no DEG tests)."""
import csv, json
from pathlib import Path
import numpy as np
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; IN=ROOT/'results';FIG=ROOT/'results/figures';FIG.mkdir(exist_ok=True)
SAMPLES=['50B','68E','68H-i','68H-ii','70C','70J-i','70J-ii']
GROUP=['Control']*4+['ASD-associated']*3

def main():
    with (IN/'ASD_Table_S4_All_60617_Genes_Descriptive_CPM.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.reader(f))
    genes=[r[0] for r in rows[1:]]
    cpm=np.asarray([[float(v) for v in row[1:8]] for row in rows[1:]])
    log2=np.asarray([[float(v) for v in row[8:15]] for row in rows[1:]])
    filtered=np.asarray([int(row[16])==1 for row in rows[1:]])
    assert len(genes)==60617 and filtered.sum()==17061
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','savefig.facecolor':'white'})
    # Figure A: donor-aware QC
    with (IN/'GSE129808_sample_QC.csv').open() as f:qc=list(csv.DictReader(f))
    totals=[int(r['gene_assigned_counts'])/1e6 for r in qc]
    fig,ax=plt.subplots(figsize=(8.6,4)); ax.bar(SAMPLES,totals)
    ax.set(ylabel='Gene-assigned reads (millions)',title='GSE129808 | Library-level QC');ax.grid(axis='y',alpha=.15)
    fig.tight_layout();fig.savefig(FIG/'RNAseq_QC_library_totals.png',dpi=250);plt.close(fig)
    # Figure B: top-30 highest variance gene features by log2(CPM+0.5)
    var=log2[filtered].var(axis=1)
    ids=np.flatnonzero(filtered)
    selected=ids[np.argsort(-var,kind='stable')[:30]]
    X=log2[selected,:]
    sd=X.std(axis=1,keepdims=True); sd[sd==0]=1
    Z=(X-X.mean(axis=1,keepdims=True))/sd
    gene_order=leaves_list(linkage(pdist(Z),method='average'))
    sample_order=leaves_list(linkage(pdist(log2[filtered].T,metric='correlation'),method='average'))
    fig,ax=plt.subplots(figsize=(8.5,8.3))
    im=ax.imshow(Z[gene_order][:,sample_order],aspect='auto',cmap='coolwarm',vmin=-2,vmax=2)
    ax.set_xticks(range(7),[SAMPLES[i] for i in sample_order],rotation=45,ha='right')
    ax.set_yticks(range(30),[genes[selected[i]] for i in gene_order],fontsize=6.5)
    ax.set_title('Descriptive gene-wise z-score heatmap (not DEGs)')
    fig.colorbar(im,ax=ax,label='Within-gene z-score',shrink=.55)
    fig.tight_layout();fig.savefig(FIG/'RNAseq_top30_variance_heatmap.png',dpi=250);plt.close(fig)
    # Figure C: DDX53 counts, explicit donor dependence
    with (IN/'GSE129808_sample_QC.csv').open() as f:qc=list(csv.DictReader(f))
    y=[int(r['DDX53_reads']) for r in qc]
    fig,ax=plt.subplots(figsize=(8.8,4.3));ax.bar(SAMPLES,y)
    for i,v in enumerate(y):ax.text(i,v+.1,str(v),ha='center',va='bottom',fontsize=9)
    ax.set(ylim=(0,6.0),ylabel='DDX53 raw gene-assigned reads',title='DDX53: 11 reads in 7 libraries (3 donors)')
    ax.grid(axis='y',alpha=.15)
    fig.tight_layout();fig.savefig(FIG/'DDX53_raw_counts.png',dpi=250);plt.close(fig)
    # Figure D: correlations on filtered features; descriptive only
    corr=np.corrcoef(log2[filtered].T)
    fig,ax=plt.subplots(figsize=(6.8,5.4));im=ax.imshow(corr,vmin=.85,vmax=1,cmap='viridis')
    ax.set_xticks(range(7),SAMPLES,rotation=45,ha='right');ax.set_yticks(range(7),SAMPLES)
    for i in range(7):
        for j in range(7):ax.text(j,i,f'{corr[i,j]:.3f}',ha='center',va='center',fontsize=7,color='white' if corr[i,j]<.94 else 'black')
    ax.set_title('Library correlations, not ASD classification');fig.colorbar(im,ax=ax,label='Pearson r')
    fig.tight_layout();fig.savefig(FIG/'RNAseq_library_correlations.png',dpi=250);plt.close(fig)
    report={'filter': 'CPM >= 1 in at least 2 libraries','passing_features':int(filtered.sum()),'top30_Ensembl': [genes[x] for x in selected],
    'pearson_offdiag_min':float(corr[np.triu_indices(7,1)].min()),'pearson_offdiag_max':float(corr[np.triu_indices(7,1)].max()),
    'interpretation':'Exploratory library-level patterns; donor-aware ASD differential expression is not estimable.'}
    (IN/'RNAseq_descriptive_figure_audit.json').write_text(json.dumps(report,indent=2))
    print('PASS RNA-seq figures:',len(list(FIG.glob('RNAseq*.png')))+int((FIG/'DDX53_raw_counts.png').exists()),'plots')

if __name__=='__main__':main()
