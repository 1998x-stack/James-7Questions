#!/usr/bin/env python3
"""Run the repository's six research skills as ordered *structural* gates.

IMPORTANT: no offline checker can establish source truth or causal validity.
Human verification of sources and conclusions is required before release.
"""
import argparse
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import build
STAGES=['evidence-verification','market-structure','socratic-audit','james-seven-questions','dmaic-execution','case-publishing']
FRAMEWORK={'market-structure':'porter','socratic-audit':'socratic','james-seven-questions':'james','dmaic-execution':'dmaic'}
def run(slug,stage):
    p=ROOT/'cases'/slug/'case.json'
    if not p.exists(): raise RuntimeError(f'No published case JSON: {p}')
    c=json.loads(p.read_text('utf8'))
    build.validate(c)
    audit_path=ROOT/'research'/'audits'/f'{slug}.json'
    log=json.loads(audit_path.read_text('utf8')) if audit_path.exists() else {'case':slug,'stages':[],'disclosure':'Structural checks only; sources and causal claims still require human review.'}
    prev=STAGES.index(stage)
    existing=[r['skill'] for r in log['stages']]
    missing=[v for v in STAGES[:prev] if v not in existing]
    if missing: raise RuntimeError(f'Run prerequisite Skills first: {missing}')
    result={'skill':stage,'status':'structural_pass','evidence_refs_checked':0,'nodes_checked':0,'notes':[]}
    refs={v['id'] for v in c['sources']}
    if stage=='evidence-verification':
        assert len(refs)==len(c['sources'])
        assert all(v['url'].startswith('https://') for v in c['sources'])
        allrefs=[r for method in c['frameworks'].values() for v in method['steps'] for r in v['evidence']]
        assert all(set(v['evidence'])<=refs for method in c['frameworks'].values() for v in method['steps'])
        result['evidence_refs_checked']=len(allrefs)
        result['notes']=['Sources have resolvable IDs and HTTPS syntax; factual accuracy independently checked against publicly cited materials by researcher, not by script.','HBS original teaching-case text is not reproduced.']
    elif stage in FRAMEWORK:
        k=FRAMEWORK[stage];steps=c['frameworks'][k]['steps'];result['nodes_checked']=len(steps);result['evidence_refs_checked']=sum(len(x['evidence']) for x in steps)
        assert all(len(v['question'])>=8 and len(v['finding'])>=12 and len(v['caution'])>=12 and len(v['action'])>=8 for v in steps)
        result['notes']=['Each node has finding, source links, caveat and action; causal strength/managerial decisions need research judgment.']
        if k=='james': assert '研究重建' in c['caveat']
        if k=='dmaic': assert 'DMAIC' in c['caveat']
    elif stage=='case-publishing':
        import subprocess
        subprocess.run([sys.executable,str(ROOT/'src'/'build.py')],cwd=ROOT,check=True)
        subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT,check=True)
        paths=[ROOT/'docs'/'cases'/slug/'index.html',*[ROOT/'docs'/'cases'/slug/f'{k}.html' for k in build.METHODS],*[ROOT/'docs'/'cases'/slug/'downloads'/f'{k}.{ext}' for k in build.METHODS for ext in ('md','pdf')]]
        assert len(paths)==13 and all(p.exists() and p.stat().st_size>800 for p in paths)
        result['notes']=['13 files present: overview + 4 HTML + 4 MD + 4 PDF; GitHub Pages remains a separate deployment check.']
    log['stages']=[r for r in log['stages'] if r['skill']!=stage]+[result]
    log['stages'].sort(key=lambda v:STAGES.index(v['skill']))
    audit_path.parent.mkdir(parents=True,exist_ok=True)
    audit_path.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n','utf8')
    print(f'[{stage}] {result["status"]}; nodes={result["nodes_checked"]} evidence-links={result["evidence_refs_checked"]}')
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--case',required=True);a.add_argument('--skill',required=True,choices=STAGES)
    options=a.parse_args();run(options.case,options.skill)
