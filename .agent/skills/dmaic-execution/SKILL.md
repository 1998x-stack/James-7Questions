---
name: dmaic-execution
description: Translate an existing business process issue into measurable, controlled improvement work.
---

# DMAIC Execution / Continuous Improvement

## When to use

DMAIC、六西格玛、技术交付、质量、缺陷、工程管理、持续改进

## Mission

将战略拆解为CTQ、基线、根因、干预、控制计划，而非把DMAIC当作所有战略的答案。

## Workflow

1. Define：业务目标、问题边界、利益相关者、CTQ和项目章程。
2. Measure：测量定义、采样计划、基线、数据质量、系统能力。
3. Analyze：过程图、因果图、统计检验、替代根因、约束。
4. Improve：试点方案、实验设计、技术与组织协同改进。
5. Control：监控图表、控制界限、责任人、报警规则、复盘与回滚。

## Required output

没有样本与统计控制图时不能声称“六西格玛认证项目”；历史案例注明“事后DMAIC映射”。

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
