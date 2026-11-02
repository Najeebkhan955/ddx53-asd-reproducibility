#!/usr/bin/env python3
"""Recreate full S3 raw counts and S4 CPM/log2(CPM+0.5) from deposited GEO files.

No differential-expression test is conducted: the seven libraries derive from only
three donor sources (one affected donor), so library-level group comparisons do
not provide valid independent ASD replication.
"""
import csv, gzip, hashlib, io, json, tarfile
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data/original/GSE129808_RAW.tar'
OUT = ROOT / 'results'; OUT.mkdir(exist_ok=True)
EXPECTED = ['GSM3722366','GSM3722367','GSM3722368','GSM3722369',
            'GSM3722370','GSM3722371','GSM3722372']

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load_original():
    gene_ids, vectors, sample_ids = None, [], []
    with tarfile.open(SRC, 'r:*') as t:
        members = sorted([m for m in t.getmembers() if m.isfile()], key=lambda m:m.name)
        if len(members) != 7: raise ValueError('Expected 7 source files in GEO TAR')
        for member in members:
            sample = member.name.rsplit('/',1)[-1].split('_')[0]
            data = t.extractfile(member).read()
            with gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb') as gz:
                lines = gz.read().decode('utf-8').splitlines()
            if lines[0] != 'Gene\tCounts':
                raise ValueError('Unexpected HTSeq header in '+member.name)
            parsed = [line.split('\t') for line in lines[1:]]
            ids = [g for g,_ in parsed]
            if gene_ids is None: gene_ids = ids
            elif gene_ids != ids: raise ValueError('Gene IDs/order differ between files')
            values = np.asarray([int(n) for _,n in parsed],dtype=np.int64)
            if np.any(values<0): raise ValueError('Negative count in '+member.name)
            vectors.append(values); sample_ids.append(sample)
    if sample_ids != EXPECTED: raise ValueError(f'Unexpected GSM sample order: {sample_ids}')
    counts = np.column_stack(vectors)
    if counts.shape!=(60617,7): raise ValueError(f'Unexpected count shape: {counts.shape}')
    return gene_ids,sample_ids,counts

def main():
    genes, samples, counts = load_original()
    totals = counts.sum(axis=0)
    cpm = 1e6 * counts / totals
    log2_cpm = np.log2(cpm + 0.5)
    detected = np.sum(counts > 0,axis=0)
    pass_per_gene = (cpm >= 1).sum(axis=1)
    n_pass = int((pass_per_gene >= 2).sum())
    assert n_pass == 17061
    d = counts[genes.index('ENSG00000184735.6')]
    assert d.tolist() == [3,1,1,1,5,0,0]
    s3 = OUT/'ASD_Table_S3_All_60617_Genes_Raw_HTSeq_Counts.csv'
    s4 = OUT/'ASD_Table_S4_All_60617_Genes_Descriptive_CPM.csv'
    with s3.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['Ensembl_gene_id']+samples)
        for g,row in zip(genes,counts): w.writerow([g]+row.tolist())
    with s4.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['Ensembl_gene_id']+[f'CPM_{s}' for s in samples] +
            [f'log2_CPM_plus_0.5_{s}' for s in samples] +
            ['n_libraries_CPM_ge_1','pass_CPM_ge_1_in_2_libraries'])
        for i,g in enumerate(genes):
            w.writerow([g] + [f'{x:.9f}' for x in cpm[i]] +
                [f'{x:.9f}' for x in log2_cpm[i]] +
                [int(pass_per_gene[i]),int(pass_per_gene[i]>=2)])
    with (OUT/'GSE129808_sample_QC.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['GSM','gene_assigned_counts','genes_with_count_gt_0','DDX53_reads','DDX53_CPM'])
        for i,s in enumerate(samples):w.writerow([s,int(totals[i]),int(detected[i]),int(d[i]),f'{cpm[genes.index("ENSG00000184735.6"),i]:.9f}'])
    meta={ 'source':'NCBI GEO GSE129808_RAW.tar','source_archive_SHA256':sha256(SRC),
           'features':len(genes),'libraries':samples,'library_totals':totals.tolist(),
           'detected_genes':detected.tolist(),'features_CPM_ge_1_in_2_libraries':n_pass,
           'DDX53_gene':'ENSG00000184735.6','DDX53_raw_counts':d.tolist(),
           'DDX53_CPM':cpm[genes.index('ENSG00000184735.6')].tolist(),
           'derived_S3_SHA256':sha256(s3),'derived_S4_SHA256':sha256(s4),
           'design_note':'7 libraries from 3 donors, one ASD donor; descriptive analysis only'}
    (OUT/'GSE129808_reanalysis_audit.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print('PASS RNA-seq:',len(genes),'features, 7 libraries, 17061 filtered, DDX53 11 reads')
    print('S3 SHA256',meta['derived_S3_SHA256']);print('S4 SHA256',meta['derived_S4_SHA256'])

if __name__=='__main__': main()
