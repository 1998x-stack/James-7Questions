#!/usr/bin/env python3
"""Install six detailed reusable, multi-agent research skills and lightweight agent adapters."""
from pathlib import Path
from textwrap import dedent
ROOT=Path(__file__).resolve().parents[1]
SKILLS={
'market-structure':{
 'title':'Market Structure / Porter Five Forces',
 'description':'Analyze business boundaries and five competitive forces using citable, comparable evidence.',
 'triggers':'市场规模、产业竞争、行业进入壁垒、供应商与购买方议价权、替代品、Porter Five Forces',
 'goal':'识别决定长期利润分配的结构性力量，避免仅以竞品份额替代行业结构研究。',
 'method':('先定义产品/服务、地域、时间、客户、替代关系，禁止混用GMV与净收入。','分别调查既有竞争者、新进入者、替代品、供给侧与需求侧议价能力。','对每一力量形成可反驳假设，记录强度、因果机制、反例与资料时间。','将五力结果映射至商业模式、单位经济和决策风险。'),
 'must':'每个竞争力量提供question、finding、evidence、caution、action；无法找到同口径份额时标记未知。',
 'reference':'波特五力定义： https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-forces.aspx\n经营财报：优先发行人公告与原始监管文件。\n防错：平台双边市场应分别审查供给方与需求方，不把手机渠道迁移等同净新增量。',
 'asset':'# 五力研究模板\n\n- 市场定义：\n- 行业内竞争：\n- 潜在进入者：\n- 供应商议价权：\n- 购买者议价权：\n- 替代品：\n- 证据冲突与反证：\n- 战略取舍：\n'},
'socratic-audit':{
 'title':'Socratic Inquiry / Argument Audit',
 'description':'Challenge a strategic thesis through definitions, evidence, rival explanations, and falsifiability.',
 'triggers':'苏格拉底式追问、验证商业假设、证据审计、反证、相关性与因果性',
 'goal':'让研究陈述可证伪；研究者必须主动寻找与结论相反的材料。',
 'method':('明确命题、决策问题和允许推翻命题的条件。','澄清模糊概念：增长、份额、活跃用户、收入、净利润的口径。','提出证据和证据源分级：原始文档、转述、假设。','系统列举替代解释、混杂变量、选择偏差和反向因果。','审查长短期后果、风险、外部性与法定义务。','记录可以证伪的预测及决策停止阈值。'),
 'must':'六步逐层追问，任何强因果结论必须具备因果识别设计或明确标注研究假设。',
 'reference':'斯坦福哲学百科 Socrates/elenchus: https://plato.stanford.edu/entries/socrates/\n研究设计：区分观察数据、反事实假设与因果识别。\n禁止：把提问的数量当成论证强度。',
 'asset':'# 反证登记模板\n\n| 命题 | 支持证据 | 反向证据 | 替代解释 | 证伪条件 | 状态 |\n|---|---|---|---|---|---|\n| | | | | | 待验证 |\n'},
'james-seven-questions':{
 'title':'James Seven Questions / Strategic Decision',
 'description':'A transparent, reconstructed seven-stage business analysis framework inspired by public reporting.',
 'triggers':'梁建章、James七连问、商业战略决策、业务管理者七问',
 'goal':'由市场事实逐层追问至战略杠杆、反证、资源配置与验证计划。',
 'method':('市场定义：明确用户、产品、地域和替代关系。','市场规模与演变：规模、利润池、增长和渠道迁移。','竞争结构：平台及产业链、市场份额与关键角色。','因果机制：为什么增长、转化、盈利或失速。','战略杠杆：相互竞争的行动、边际收益与投入。','反证和约束：失败条件、因果混杂、合法性和外部性。','行动与验证：负责人、指标、实验、风险和复盘。'),
 'must':'必须写明“研究重建，非梁建章官方固定七题”；七阶段各自至少一个反证风险。',
 'reference':'七连问报道线索《携程的“战争”》： https://www.donews.com/article/detail/7489/97454.html\n梁建章第一人称回顾： https://www.yicai.com/news/100103627.html\n不宣称准确复刻视频号“胖总聊旅游”2025-01-22节目内容。',
 'asset':'# James七连问决策备忘\n\n1. 市场定义：\n2. 规模变化：\n3. 竞争格局：\n4. 核心机制：\n5. 战略杠杆：\n6. 反证与约束：\n7. 行动验证：\n\n**最终决策：**\n**证据缺口：**\n**停止条件：**\n'},
'dmaic-execution':{
 'title':'DMAIC Execution / Continuous Improvement',
 'description':'Translate an existing business process issue into measurable, controlled improvement work.',
 'triggers':'DMAIC、六西格玛、技术交付、质量、缺陷、工程管理、持续改进',
 'goal':'将战略拆解为CTQ、基线、根因、干预、控制计划，而非把DMAIC当作所有战略的答案。',
 'method':('Define：业务目标、问题边界、利益相关者、CTQ和项目章程。','Measure：测量定义、采样计划、基线、数据质量、系统能力。','Analyze：过程图、因果图、统计检验、替代根因、约束。','Improve：试点方案、实验设计、技术与组织协同改进。','Control：监控图表、控制界限、责任人、报警规则、复盘与回滚。'),
 'must':'没有样本与统计控制图时不能声称“六西格玛认证项目”；历史案例注明“事后DMAIC映射”。',
 'reference':'ASQ官方定义 https://asq.org/quality-resources/dmaic\n适用性：主要面向已有流程；新业务设计可能更适合探索性实验或DMADV。\n携程技术演讲整理：https://www.tmtpost.com/175717.html',
 'asset':'# DMAIC 项目章程\n\n- Define：项目范围、CTQ、目标与Owner\n- Measure：指标字典、基线、样本、缺失数据\n- Analyze：根因图、反事实和效应识别\n- Improve：干预组合、A/B或准实验、风险\n- Control：控制图、责任人、复盘周期、回滚阈值\n'},
'evidence-verification':{
 'title':'Deep Source Verification / Evidence Ledger',
 'description':'Audit sources, preserve measurement scope, and reject unsupported claims before publication.',
 'triggers':'deep search、多信源、数据验证、来源审计、核实财报、证据链',
 'goal':'确保所有研究结论均可追溯，严格区别一手、归因转述和方法假设。',
 'method':('先列出待证命题而非先找支持证据。','优先公司财报、监管记录、原始访谈，其次媒体整理。','以每个事实最小可验证片段建立索引，标记数字口径与期间。','检查多个媒体是否只是转载同一条稿件；不能视为独立佐证。','寻找冲突材料与反向证据，未验证的数字不得进入KPI。','逐项审查claim→source URL→口径→日期→置信度→适用范围。'),
 'must':'source id必须唯一，case.json引用的evidence id必须存在；source缺失时构建应失败。',
 'reference':'SEC官方公司材料作为财务主来源；媒体整理作为可能有转述误差的二级来源。\n指标防错：季度、峰值日、住宿、机票、公司整体与渠道占比不得混用。\n2026年的后续监管事件不能自动作为2013年管理者当时决策证据。',
 'asset':'# 证据台账\n\n| ID | 待证命题 | 原始URL | 发布日期 | 统计期间 | 原始口径 | 证据类别 | 反证 |\n|---|---|---|---|---|---|---|---|\n'},
'case-publishing':{
 'title':'Case Publishing / Fourfold Artifact Factory',
 'description':'Create, validate, and publish four HTML + four Markdown + four PDF files per case.',
 'triggers':'新增案例、HTML PDF Markdown、GitHub Pages、企业管理者研究WebUI',
 'goal':'保证公司研究内容与展示模板解耦，持续添加案例时不会复制粘贴前端代码。',
 'method':('复制cases/ctrip-mobile-2012-2015/case.json并替换元数据与证据。','执行python src/build.py --no-pdf快速预览，验证4种framework及必填字段。','完成全量研究后执行python src/build.py生成四种PDF。','运行python -m unittest discover -s tests，并检查PDF页数、中文文字与按钮交互。','提交源数据、Skills及docs输出，CI自动重新构建并部署到Pages。'),
 'must':'每新增一例必须交付4 HTML、4 MD、4 PDF；输出不得隐藏反证和引用；索引自动增加。',
 'reference':'GitHub Pages Actions部署：https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages\n前端参考：https://vercel.com/geist/introduction（只借鉴层级和可读性，不复制其产品标识）\n技术约束：离线静态站点，HTML自包含；新增案例无须修改UI.js。',
 'asset':'# 案例发布检查清单\n\n- [ ] 数字口径与原始数据核验\n- [ ] 5/6/7/5分析阶段完整\n- [ ] 4 HTML打开并可点击\n- [ ] 4 Markdown内容与来源齐全\n- [ ] 4 PDF可检索中文、无截断\n- [ ] 首页自动展示新增案例\n- [ ] GitHub Actions成功 + Pages可访问\n'},
}

def write(p,t): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t,encoding='utf-8')
for key,skill in SKILLS.items():
    folder=ROOT/'.agent'/'skills'/key
    steps='\n'.join(f'{i}. {s}' for i,s in enumerate(skill['method'],1))
    sk=f'''---
name: {key}
description: {skill['description']}
---

# {skill['title']}

## When to use

{skill['triggers']}

## Mission

{skill['goal']}

## Workflow

{steps}

## Required output

{skill['must']}

每个结论输出 claim / evidence / scope / inference / counterevidence / uncertainty / decision_impact，并与案例的四种框架字段同步。先检查 `cases/<slug>/case.json`，后运行 `python src/build.py`。不允许捏造市场规模、竞争份额、模型实证或会议记录。

## Source discipline

- 来源按原始财报/监管公告 > 本人署名/同期演讲 > 明确归因的媒体整理 > 其他评论排序。
- 不复制长篇版权材料；保留可验证URL和简短分析性转述。
- 指标必须写明时间区间、单位、产品边界与分子分母。
- 推断必须说明能否由资料直接证明。

## Files

- `references/method.md`：研究与审计原则。
- `scripts/run.py`：本Skill的构建/验证入口。
- `assets/template.md`：本Skill结果占位模板。

## Completion gate

1. 所有引用存在，所有阶段有局限与下一动作。
2. 不将方法论的研究重建冒充历史原始制度。
3. `python -m unittest discover -s tests` 通过。
4. `python src/build.py` 生成四套互相一致的HTML、Markdown和PDF。
'''
    write(folder/'SKILL.md',sk)
    write(folder/'references/method.md',f'# {skill["title"]} — 研究参考\n\n{skill["reference"]}\n\n## 审计重点\n\n{skill["must"]}\n')
    write(folder/'assets/template.md',skill['asset'])
    write(folder/'scripts/run.py',f'''#!/usr/bin/env python3
"""{skill['title']} skill entrypoint. Use shared case schema and generator."""
from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[4]
runpy.run_path(str(root/'src'/'build.py'),run_name='__main__')
''')
    for agent in ['.pi','.claude']:
        stub=ROOT/agent/'skills'/key
        write(stub/'SKILL.md',f'''---
name: {key}
description: {skill['description']}
---

# {skill['title']}

Canonical implementation: `.agent/skills/{key}/SKILL.md`.

**必读：** 在执行任务前读取仓库根目录的 `AGENTS.md`、`.agent/skills/{key}/SKILL.md`、其 `references/method.md`、`assets/template.md`。执行工具入口 `.agent/skills/{key}/scripts/run.py`。不要直接编辑生成的HTML/PDF来替代源案例数据。

所有研究均须执行证据审计并交付 4 HTML + 4 Markdown + 4 PDF。
''')
        write(stub/'references/README.md',f'真实研究资料在 `.agent/skills/{key}/references/method.md`。\n')
        write(stub/'scripts/README.md',f'执行 `python .agent/skills/{key}/scripts/run.py`。\n')
        write(stub/'assets/README.md',f'模板在 `.agent/skills/{key}/assets/template.md`。\n')
print(f'Installed {len(SKILLS)} canonical skills and {len(SKILLS)*2} platform wrappers')
