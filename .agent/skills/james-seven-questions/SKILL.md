---
name: james-seven-questions
description: A transparent, reconstructed seven-stage business analysis framework inspired by public reporting.
---

# James Seven Questions / Strategic Decision

## When to use

梁建章、James七连问、商业战略决策、业务管理者七问

## Mission

由市场事实逐层追问至战略杠杆、反证、资源配置与验证计划。

## Workflow

1. 市场定义：明确用户、产品、地域和替代关系。
2. 市场规模与演变：规模、利润池、增长和渠道迁移。
3. 竞争结构：平台及产业链、市场份额与关键角色。
4. 因果机制：为什么增长、转化、盈利或失速。
5. 战略杠杆：相互竞争的行动、边际收益与投入。
6. 反证和约束：失败条件、因果混杂、合法性和外部性。
7. 行动与验证：负责人、指标、实验、风险和复盘。

## Required output

必须写明“研究重建，非梁建章官方固定七题”；七阶段各自至少一个反证风险。

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
