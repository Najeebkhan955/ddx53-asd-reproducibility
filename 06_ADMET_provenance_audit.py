#!/usr/bin/env python3
"""Audit the previously supplied carebastine ADMET records, without re-predicting ADMET."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'data/other_exports/S9_ADMET_author_supplied.csv';OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
def main():
    with SRC.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    if not rows:raise ValueError('No source ADMET rows')
    flags=[r for r in rows if any(x in (r['Property']+' '+r['Category']).lower() for x in ('bbb','p-gp','cyp','ames','carcin','toxicity'))]
    with (OUT/'ADMET_source_values_no_reprediction.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    report={'compound':'carebastine','source':'author-supplied S9 predictions','source_rows':len(rows),
            'clinical_relevance_flags':[{'property':r['Property'],'reported_value':r['Reported_Value']} for r in flags],
            'independently_recomputed':False,'caveats':['Original ADMET service outputs, version, prediction timestamps and input SMILES were not supplied.','Model scores are not measured pharmacokinetic endpoints.']}
    (OUT/'ADMET_provenance_audit.json').write_text(json.dumps(report,indent=2))
    print('PASS ADMET provenance: tracked',len(rows),'archived rows; predictions NOT reproduced')
if __name__=='__main__':main()
