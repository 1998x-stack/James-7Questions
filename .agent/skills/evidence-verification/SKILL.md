---
name: evidence-verification
description: Audit sources, preserve measurement scope, and reject unsupported claims before publication.
---

# Deep Source Verification / Evidence Ledger

## When to use

deep search、多信源、数据验证、来源审计、核实财报、证据链

## Mission

确保所有研究结论均可追溯，严格区别一手、归因转述和方法假设。

## Workflow

1. 先列出待证命题而非先找支持证据。
2. 优先公司财报、监管记录、原始访谈，其次媒体整理。
3. 以每个事实最小可验证片段建立索引，标记数字口径与期间。
4. 检查多个媒体是否只是转载同一条稿件；不能视为独立佐证。
5. 寻找冲突材料与反向证据，未验证的数字不得进入KPI。
6. 逐项审查claim→source URL→口径→日期→置信度→适用范围。

## Required output

source id必须唯一，case.json引用的evidence id必须存在；source缺失时构建应失败。

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
