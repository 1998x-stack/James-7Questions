# James 7Questions · Decision Atlas

> 面向企业经营管理者的可扩展、可追溯战略分析平台。**一份案例数据 → 波特五力、苏格拉底式追问、James 七连问、DMAIC 四套框架 → 4 HTML + 4 Markdown + 4 PDF。**

![Production](https://img.shields.io/badge/architecture-static%20first-244b74) ![Output](https://img.shields.io/badge/artifacts-4%20HTML%20%2B%204%20MD%20%2B%204%20PDF-2a6c5f)

**Repository:** https://github.com/1998x-stack/James-7Questions  
**GitHub Pages（需 Actions 工作流完成并在仓库设置中启用）：** https://1998x-stack.github.io/James-7Questions/

## 一、定位

本仓库不做“向管理者展示四张漂亮的图”的演示项目，而是构建一个可扩展的**证据驱动决策工作台**。

- **波特五力**：分析市场结构和利润分配；五个可交互节点。
- **苏格拉底式追问**：检查假设、口径、证据、替代解释和可证伪性；六个可交互节点。
- **James 七连问（研究重建）**：定义市场、规模变化、竞争结构、因果机制、杠杆、反证与决策；七个可交互节点。**不是已核实的梁建章官方固定七题**。
- **DMAIC（事后映射）**：定义、测量、分析、改进、控制；五个可交互节点。公开资料尚未证明携程案例具有完整的正式项目档案。

产品面向高管、行业研究员、业务负责人和策略咨询人员。默认优先展示决策问题、主要证据、局限与下一步行动，具体资料可逐层展开。

## 二、已交付首个真实案例

### 携程移动互联网转型（2012—2015）

- **核心判断：** 移动预订入口变化迫使携程从旧的呼叫中心/PC优势转向移动产品与组织能力的共同重构。
- **经过核验的财务事实：** 2014年净营收约73亿元，同比增长36%；归母净利润2.43亿元，同比下降76%；研发费用+86%，营销费用+74%。详见 [SEC披露](https://www.sec.gov/Archives/edgar/data/1269238/000110465915021180/a15-7370_1ex99d1.htm)。
- **经过核验的移动交易事实：** 2013Q2酒店移动预订占比超20%；2014Q1住宿移动交易占比超40%。两个不同期间与产品口径不能混用。
- **工程实践：** 叶亚明演讲整理披露集中式无线开发向16个业务团队分担移动职责的调整，移动支付成功率一年提升约10个百分点。请注意演讲转述属性及缺少原始实验数据的局限。
- **归因约束：** 数据支持渠道转型发生，不足以精确分解智能手机普及、市场推广和组织重构的独立贡献。

打开 `docs/index.html` 或 `docs/cases/ctrip-mobile-2012-2015/james.html` 即可浏览独立 HTML，**无需服务器或网络依赖**（点击来源链接才需要网络）。

## 三、仓库结构

```text
James-7Questions/
├── README.md                    # 产品定位 / 扩展指南
├── AGENTS.md                    # Agent跨平台治理与交付协议
├── cases/
│   └── ctrip-mobile-2012-2015/
│       └── case.json            # 单一事实源：指标、证据、4种框架
├── schemas/
│   └── case.schema.json         # 机器可验证结构
├── .agent/skills/              # 六个完整Skills的权威实现
│   ├── market-structure/        # 每个包含SKILL.md, references/, assets/, scripts/
│   ├── socratic-audit/
│   ├── james-seven-questions/
│   ├── dmaic-execution/
│   ├── evidence-verification/
│   └── case-publishing/
├── .pi/skills/                  # Pi agent兼容入口和到权威实现的引用
├── .claude/skills/              # Claude agent兼容入口和到权威实现的引用
├── src/
│   ├── build.py                 # HTML/Markdown/PDF一致性生成器
│   ├── ui.css                   # 设计系统与响应式布局
│   └── ui.js                    # 无框架交互可视化
├── tests/                       # 结构、输出及引用验证
├── .github/workflows/pages.yml  # GitHub Pages + CI
├── docs/                        # 静态Pages产物
│   ├── index.html               # 自动化案例库
│   └── cases/<slug>/
│       ├── porter.html, socratic.html, james.html, dmaic.html
│       └── downloads/
│           ├── porter.md/.pdf
│           ├── socratic.md/.pdf
│           ├── james.md/.pdf
│           └── dmaic.md/.pdf
└── tools/create_skills.py       # Skills/适配器内容生成器
```

## 四、立即运行

```bash
python -m pip install -r requirements.txt
python src/build.py
python -m unittest discover -s tests -v
python -m http.server 8000 --directory docs
# 浏览器打开 http://localhost:8000
```

若只预览网页，`python src/build.py --no-pdf` 可仅使用Python标准库完成HTML和Markdown构建，适合轻量开发。完整PDF生成需要`reportlab`。

## 五、新增公司/业务（最重要）

1. 复制 `cases/ctrip-mobile-2012-2015/case.json` 至 `cases/<your-slug>/case.json`。
2. 替换公司与业务信息；先补充资料源，建立稳定的 `S1`/`S2` 等 `source_id`。
3. 按固定阶段完善 `porter:5, socratic:6, james:7, dmaic:5`；每个阶段包含 `name / question / finding / evidence / caution / action`。
4. 运行 `python src/build.py`，构建器将自动扫描所有案例并更新首页与四份报告。**不需要修改JS、CSS或复制页面模板。**
5. 运行自动化测试；PR审核证据质量；合并后GitHub Actions构建并发布Pages。

完整人工审核见 `.agent/skills/case-publishing/assets/template.md`。新增业务可指向同一公司不同时间段，例如 `ctrip-ai-trip-planning-2026`，避免把不同战略周期压在一个研究对象上。

## 六、如何使用六套 Skills

```text
证据研究          .agent/skills/evidence-verification/SKILL.md
市场结构          .agent/skills/market-structure/SKILL.md
论证审查          .agent/skills/socratic-audit/SKILL.md
战略七问          .agent/skills/james-seven-questions/SKILL.md
执行改进          .agent/skills/dmaic-execution/SKILL.md
发布与质量验收    .agent/skills/case-publishing/SKILL.md
```

`.pi/skills/` 和 `.claude/skills/` 提供各自的SKILL入口，并引用唯一的`.agent/skills/`权威实现，以避免三份研究指令随时间不一致。所有Agent从根目录 `AGENTS.md` 开始读取。

## 七、设计思路

不再使用高对比霓虹、复杂背景或堆砌图案的“技术演示型”仪表盘，改为偏咨询公司研究台的**浅色、严肃、结构化**设计：

- 左侧常驻框架导航；上方明确当前案例；中部四张关键财务/渠道指标卡；主区左右分栏展示分析图和“证据与决策工作卡”。
- 五力采用辐射图、苏格拉底为论证阶梯、七连问为阶段流、DMAIC为环形循环；交互节点均支持键盘和鼠标。
- 每步展示问题、观察、局限、行动、证据链接；按管理者“判断—证据—行动”阅读顺序布局。
- 在 <=750px 宽屏幕下变为纵向页面；支持打印、四套Markdown/PDF下载。
- 参考 [Vercel Geist](https://vercel.com/geist/introduction) 的排版层级与高对比度原则，以及 [NN/g的任务导向信息架构](https://www.nngroup.com/articles/information-scent/)，但未照搬其品牌组件。

## 八、数据规范与限制

- 每个数字记录时间、单位、定义及来源；禁止把峰值日指标作为全年平均数。
- 多个平台转载同一篇报道，不等于多个独立信源。
- 未找到正式七道题的完整原始清单，永远显式标注为**研究重建**。
- 未找到2014年当时正式使用DMAIC的完整项目文档，永远标注为**事后映射**。
- 不从真实业务发生的时间关系中推导未经证实的因果效果。
- GitHub Pages仅承载公开资料；包含个人隐私、商业秘密和机密资料的案例不能直接公开。

## 九、Pages 部署

`.github/workflows/pages.yml` 在推送main或手动触发时安装依赖、验证、重建全部报告，再通过官方 `actions/upload-pages-artifact` 和 `actions/deploy-pages` 发布。

**一次性仓库设置：** Settings → Pages → Build and deployment → Source: GitHub Actions。GitHub App可能缺少修改Pages配置的管理权限，无法仅靠提交代码证明站点已启用。检查 Actions 成功，以及Pages URL实际HTTP访问成功后，才能将状态宣告为“已上线”。

## 许可证与内容说明

源代码 MIT；第三方报告由各版权人持有，本仓库只保留少量必要事实性摘要与原文链接，不重新发布第三方全文。研究内容不构成投资、法律或经营保证。