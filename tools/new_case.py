#!/usr/bin/env python3
"""Scaffold a draft without copying another company's facts. Not published by build.py."""
from pathlib import Path
import argparse, json, re
STAGES={
 'porter':['行业内竞争','潜在进入者','购买者议价','供应商议价','替代品'],
 'socratic':['提出主张','定义概念','检查证据','替代解释','检查后果','可证伪命题'],
 'james':['市场定义','规模与变化','竞争结构','因果机制','战略杠杆','反证与约束','行动验证'],
 'dmaic':['Define','Measure','Analyze','Improve','Control']}

def create_draft(slug,company,title,industry,period,folder=None):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug): raise ValueError('slug must be kebab-case')
    folder=Path(folder) if folder else Path(__file__).resolve().parents[1]/'cases'
    target=folder/slug/'draft.case.json'
    if target.exists() or target.with_name('case.json').exists():raise FileExistsError(slug)
    frameworks={k:{'title':k,'subtitle':'待研究','decision':'待核验','steps':[{'name':name,'question':'待研究','finding':'待核验','evidence':[],'caution':'此为草稿，不得公开发布','action':'补充证据与可执行动作'} for name in names]} for k,names in STAGES.items()}
    case={'schema_version':'1.0.0','id':slug,'company':company,'title':title,'subtitle':'待研究','period':period,'industry':industry,'tags':[],'status':'草稿，禁止发布','abstract':'尚未完成来源核验与管理分析，不得作为正式案例发布。','thesis':'待研究','decision':'待研究','caveat':'尚无证据，请补全后再发布。','kpis':[],'timeline':[],'sources':[],'frameworks':frameworks}
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(case,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return target
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('slug','company','title','industry','period'): p.add_argument('--'+k,required=True)
    a=p.parse_args();print('Created unpublished draft:',create_draft(**vars(a)))
