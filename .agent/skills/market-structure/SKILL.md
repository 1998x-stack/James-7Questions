---
name: market-structure
description: Analyze business boundaries and five competitive forces using citable, comparable evidence.
---

# Market Structure / Porter Five Forces

## When to use

市场规模、产业竞争、行业进入壁垒、供应商与购买方议价权、替代品、Porter Five Forces

## Mission

识别决定长期利润分配的结构性力量，避免仅以竞品份额替代行业结构研究。

## Workflow

1. 先定义产品/服务、地域、时间、客户、替代关系，禁止混用GMV与净收入。
2. 分别调查既有竞争者、新进入者、替代品、供给侧与需求侧议价能力。
3. 对每一力量形成可反驳假设，记录强度、因果机制、反例与资料时间。
4. 将五力结果映射至商业模式、单位经济和决策风险。

## Required output

每个竞争力量提供question、finding、evidence、caution、action；无法找到同口径份额时标记未知。

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
