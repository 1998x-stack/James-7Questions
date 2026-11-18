---
name: socratic-audit
description: Challenge a strategic thesis through definitions, evidence, rival explanations, and falsifiability.
---

# Socratic Inquiry / Argument Audit

## When to use

苏格拉底式追问、验证商业假设、证据审计、反证、相关性与因果性

## Mission

让研究陈述可证伪；研究者必须主动寻找与结论相反的材料。

## Workflow

1. 明确命题、决策问题和允许推翻命题的条件。
2. 澄清模糊概念：增长、份额、活跃用户、收入、净利润的口径。
3. 提出证据和证据源分级：原始文档、转述、假设。
4. 系统列举替代解释、混杂变量、选择偏差和反向因果。
5. 审查长短期后果、风险、外部性与法定义务。
6. 记录可以证伪的预测及决策停止阈值。

## Required output

六步逐层追问，任何强因果结论必须具备因果识别设计或明确标注研究假设。

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
