---
name: case-publishing
description: Create, validate, and publish four HTML + four Markdown + four PDF files per case.
---

# Case Publishing / Fourfold Artifact Factory

## When to use

新增案例、HTML PDF Markdown、GitHub Pages、企业管理者研究WebUI

## Mission

保证公司研究内容与展示模板解耦，持续添加案例时不会复制粘贴前端代码。

## Workflow

1. 复制cases/ctrip-mobile-2012-2015/case.json并替换元数据与证据。
2. 执行python src/build.py --no-pdf快速预览，验证4种framework及必填字段。
3. 完成全量研究后执行python src/build.py生成四种PDF。
4. 运行python -m unittest discover -s tests，并检查PDF页数、中文文字与按钮交互。
5. 提交源数据、Skills及docs输出，CI自动重新构建并部署到Pages。

## Required output

每新增一例必须交付4 HTML、4 MD、4 PDF；输出不得隐藏反证和引用；索引自动增加。

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
