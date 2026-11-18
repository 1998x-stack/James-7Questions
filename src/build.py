#!/usr/bin/env python3
"""Build static case atlas from versioned, auditable case JSON. No network IO."""
from __future__ import annotations
import argparse
import html
import json
import pathlib
import re
import sys
from xml.sax.saxutils import escape
ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
METHODS = {'porter':'波特五力','socratic':'苏格拉底式追问','james':'James 七连问（研究重建）','dmaic':'DMAIC（事后映射）'}

def load_cases():
    return [json.loads(p.read_text('utf-8')) for p in sorted((ROOT/'cases').glob('*/case.json'))]

def validate(case):
    from jsonschema import Draft202012Validator
    schema=json.loads((ROOT/'schemas'/'case.schema.json').read_text('utf-8'))
    Draft202012Validator(schema).validate(case)
    required={'id','company','title','frameworks','sources','kpis','timeline','abstract','period'}
    miss=required-set(case)
    if miss: raise ValueError(f"{case.get('id','?')}: missing {sorted(miss)}")
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',case['id']): raise ValueError('slug must be kebab-case')
    ids=[s['id'] for s in case['sources']]
    if len(set(ids))!=len(ids): raise ValueError('duplicate evidence id')
    if set(case['frameworks'])!=set(METHODS):raise ValueError('case must contain all four frameworks')
    for key,n in [('porter',5),('socratic',6),('james',7),('dmaic',5)]:
        arr=case['frameworks'][key]['steps']
        if len(arr)!=n:raise ValueError(f'{key}: expected {n}, got {len(arr)}')
        for i,step in enumerate(arr):
            if not {'name','question','finding','evidence','caution','action'} <= set(step): raise ValueError(f'{key}[{i}]: incomplete step')
            if not step['caution'].strip(): raise ValueError(f'{key}[{i}]: caveat must not be blank')
            if set(step['evidence'])-set(ids): raise ValueError(f'{key}[{i}]: dangling source')
    return True

def write(path,content):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(content,encoding='utf-8')

def html_document(case, method, case_index, css, js, library=False):
    tag='首页 - 决策研究工作台' if library else f'{METHODS[method]} - {case["company"]}'
    data=json.dumps(case,ensure_ascii=False).replace('</','<\\/')
    index=json.dumps(case_index,ensure_ascii=False).replace('</','<\\/')
    base='./' if library else './'
    css_extra=''
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{html.escape(case['abstract'],quote=True)}"><meta name="color-scheme" content="light"><title>{html.escape(tag)}</title><style>{css}\n{css_extra}</style></head><body><div id="app"></div><script>window.CASE_DATA={data};window.CASE_INDEX={index};window.METHOD={json.dumps(method)};window.PAGE_MODE={json.dumps('library' if library else 'framework')};window.BASE_PATH={json.dumps(base)};</script><script>{js}</script></body></html>'''

def markdown_report(case, method):
    f=case['frameworks'][method];source={s['id']:s for s in case['sources']}
    lines=[f'# {f["title"]}：{case["title"]}', '',f'> 研究时段：{case["period"]}｜公司：{case["company"]}｜行业：{case["industry"]}', '',
    '> 方法学声明：本案例采用事后研究复盘；James 七问非携程官方固定题目，DMAIC 非经过证实的内部项目档案。','',
    '## 执行摘要','',case['abstract'],'',f'**核心判断：** {f["decision"]}','',
    '## 第一部分：理解现实与明确边界','',
    f'**战略命题：** {case["thesis"]}','',
    '### 核验过的关键经营指标','',
    '|指标|观察值|口径与限制|来源|','|---|---:|---|---|']
    for k in case['kpis']:lines.append('|'+ '|'.join([k['label'],k['value'],k['note'],f'[{k["source"]}](#{k["source"].lower()})'])+'|')
    lines+=['','### 经历的主要节点','']
    for t in case['timeline']:lines.append(f'- **{t["date"]}｜{t["title"]}：** {t["text"]} [{t["source"]}]')
    lines+=['',f'## 第二部分：{f["title"]}分析','',f'**方法目的：** {f["subtitle"]}','']
    for i,s in enumerate(f['steps'],1):
        lines+= [f'### {i}. {s["name"]}','',f'**核心追问：** {s["question"]}','',f'**证据支持的观察：** {s["finding"]}','',f'**反证与不确定性：** {s["caution"]}','',f'**建议的下一行动：** {s["action"]}','',f'证据索引：{", ".join("["+sid+"](#"+sid.lower()+")" for sid in s["evidence"])}','']
    lines+=['## 第三部分：管理含义与决策边界','','**战略建议（研究重建，而非历史决议原文）：**', '', f['decision'],'',
    '### 必须保留的区别','',
    '- **渠道迁移 ≠ 净增订单：** 仅凭移动交易占比不能识别真实增量与渠道替代。',
    '- **营收增长 ≠ 单位经济改善：** 2014年研发和营销增幅高于净营业收入增幅，短期盈利承压。',
    '- **同期变化 ≠ 管理措施的因果贡献：** 智能手机普及是重要混杂因素，未建立反事实对照。',
    '- **管理者事后复盘 ≠ 正式DMAIC项目：** 不应虚构控制图、样本、置信区间或实验效果。',
    '- **战术有效 ≠ 合法可持续：** 研究应包含法律、竞争影响和交易伙伴价值边界。', '',
    '### 下一轮研究问题','',
    '1. 按产品线补全2012—2015年季度移动交易占比、订单量与净收入可比序列。',
    '2. 区分App下载、月活用户、订单与复购，避免将累计下载当作活跃用户。',
    '3. 根据同行公开财报建立对照序列，审查行业趋势与企业特定措施的差别。',
    '4. 获取支付改进的期初期末基线、灰度分组与故障数据，才可能估计独立贡献。','',
    '## 第四部分：资料与证据审计','','所引用网页属原始文件或注明来源的媒体整理稿。原始财务数据和管理复盘的证据强度不同。','']
    for s in case['sources']: lines+= [f'<a id="{s["id"].lower()}"></a>', f'**[{s["id"]}] {s["title"]}**（{s["type"]}，{s["year"]}）', '',f'- 资料链接：{s["url"]}',f'- 支持内容：{s["note"]}','']
    lines+=['---','',f'**总体局限：** {case["caveat"]}','', '构建于版本化案例仓库，可重新生成并审查。']
    return '\n'.join(lines)+'\n'

def pdf_report(case, method, path):
    try:
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.lib.colors import HexColor
        from reportlab.lib.enums import TA_LEFT
        from reportlab.lib.pagesizes import A4
    except ImportError as exc: raise RuntimeError('PDF build requires reportlab: pip install reportlab') from exc
    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    f=case['frameworks'][method]
    navy=HexColor('#15243c'); blue=HexColor('#2a5dbb'); muted=HexColor('#68788b'); line=HexColor('#dde5ef');
    styles={
      'cover':ParagraphStyle('cover',fontName='STSong-Light',fontSize=23,leading=34,textColor=navy,spaceAfter=18),
      'h1':ParagraphStyle('h1',fontName='STSong-Light',fontSize=15,leading=22,textColor=navy,spaceBefore=18,spaceAfter=8),
      'h2':ParagraphStyle('h2',fontName='STSong-Light',fontSize=12,leading=20,textColor=blue,spaceBefore=14,spaceAfter=6),
      'body':ParagraphStyle('body',fontName='STSong-Light',fontSize=10.4,leading=18,textColor=navy,spaceAfter=8,wordWrap='CJK'),
      'small':ParagraphStyle('small',fontName='STSong-Light',fontSize=8.8,leading=15,textColor=muted,spaceAfter=5,wordWrap='CJK'),
      'quote':ParagraphStyle('quote',fontName='STSong-Light',fontSize=11.5,leading=21,textColor=blue,spaceAfter=12,wordWrap='CJK'),
    }
    text=lambda s:escape(str(s))
    P=lambda s,style='body':Paragraph(text(s),styles[style]); flow=[]
    flow+=[P('DECISION ATLAS / EXECUTIVE RESEARCH','small'),Spacer(1,14),P(f['title'],'cover'),P(case['title'],'h1'),P(f"研究期间：{case['period']}   ｜   案例公司：{case['company']}",'small'),Spacer(1,12),P('核心决策判断','h2'),P(f['decision'],'quote'),P('研究责任边界','h2'),P(case['caveat'],'small'),Spacer(1,13),P('执行摘要','h1'),P(case['abstract']),P('战略命题','h2'),P(case['thesis']),P('关键指标（注意不同期间与业务口径）','h1')]
    for k in case['kpis']:flow.append(P(f"{k['label']}：{k['value']} ｜ {k['note']} [{k['source']}]"))
    flow.append(P('关键事件时间线','h1'))
    for t in case['timeline']:flow.append(P(f"{t['date']}  {t['title']}：{t['text']} [{t['source']}]",'small'))
    flow.append(PageBreak());flow.append(P('逐阶段追问、分析与行动','h1'))
    for i,s in enumerate(f['steps'],1):
        bloc=[P(f'{i:02d}  {s["name"]}','h2'),P('问题：'+s['question']),P('证据观察：'+s['finding']),P('不确定性：'+s['caution'],'small'),P('管理行动：'+s['action']),P('证据：'+', '.join(s['evidence']),'small')]
        flow+=bloc
    flow.extend([P('研究限制与应当避免的归因','h1')])
    for s in ['渠道占比上升不等于全部订单属于净新增量。','同期数据增长不能直接归因于特定战略或组织措施。','2014年营业增长与归母净利下降同时存在，投入质量需要单独分析。','所谓James固定七问与正式DMAIC档案尚无充分一手来源。']:
        flow.append(P('• '+s))
    flow.append(P('来源目录','h1'))
    for s in case['sources']:
        flow.append(P(f"[{s['id']}] {s['title']} — {s['type']} / {s['year']}",'small'))
        flow.append(Paragraph(f'<link href="{html.escape(s["url"],quote=True)}" color="#2b5da8">{html.escape(s["url"],quote=True)}</link>',styles['small']))
    path.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=47,leftMargin=47,topMargin=58,bottomMargin=50,author='Decision Atlas Research',title=f"{f['title']} - {case['company']}")
    def paginate(c,d):
        c.saveState();c.setFillColor(muted);c.setFont('STSong-Light',8);c.drawString(48,32,'DECISION ATLAS  /  CASE RESEARCH');c.drawRightString(A4[0]-48,32,str(d.page));c.setStrokeColor(line);c.line(47,44,A4[0]-47,44);c.restoreState()
    doc.build(flow,onFirstPage=paginate,onLaterPages=paginate)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--no-pdf',action='store_true');args=parser.parse_args();cases=load_cases()
    if not cases:raise SystemExit('No cases in cases/*/case.json')
    for c in cases:validate(c)
    css=(ROOT/'src/ui.css').read_text('utf-8');js=(ROOT/'src/ui.js').read_text('utf-8')
    index=[{k:c[k] for k in ['id','title','company','industry','period','tags','abstract']} for c in cases]
    write(DOCS/'index.html',html_document(cases[0],'porter',index,css,js,True))
    for case in cases:
        slug=case['id'];folder=DOCS/'cases'/slug
        for method in METHODS:
            write(folder/f'{method}.html',html_document(case,method,index,css,js))
            write(folder/'downloads'/f'{method}.md',markdown_report(case,method))
            if not args.no_pdf:pdf_report(case,method,folder/'downloads'/f'{method}.pdf')
        write(folder/'metadata.json',json.dumps({k:case[k] for k in ['id','title','period','industry','status','caveat']},ensure_ascii=False,indent=2)+'\n')
    write(DOCS/'.nojekyll','')
    print(f'Generated {len(cases)} case(s), {len(cases)*4} framework HTML, {len(cases)*4} Markdown, '+('0' if args.no_pdf else str(len(cases)*4))+' PDF')
if __name__=='__main__':main()
