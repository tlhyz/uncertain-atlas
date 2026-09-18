# Uncertain Atlas 架构

本目录是一条链的长期知识系统。  
它不是 Gate 网格/马丁回测工具的一部分。

交易相关代码：`/workspace/qtb`、`strategies`、`configs`、`backtest.py`。  
协议知识：只在 `/workspace/uncertain-atlas`。

---

## 五条轨，不要串目录

```text
uncertain-atlas/
  README.md              入口
  GOAL.md                最高准则
  ARCHITECTURE.md        本文件
  AUDIT_LOG.md           自审

  index/                 地图：怎么走、先学什么
  courses/               课程：按 Level 把原理讲清楚
  protocols/             协议档案：一条链或一个品类一份 19 节
  tracks/                横向专题：对照表必须随各波更新
  libraries/             可复用结论：模式 / 反模式 / 决策矩阵
  exams/                 统一题库（后置，现在不要做）
```

读法：

```text
index 看路
  → courses 把机器和工具学懂
  → protocols 用同一模板看真实链
  → tracks 横过来按问题重排
  → libraries 提炼以后「不确定」能直接用的句子
```

禁止：

- 在 `qtb/` 里写协议教材
- 在某一条链的档案里塞完整密码学课（课在 `courses/`）
- 在课程里塞 19 节项目报告（报告在 `protocols/`）
- 在正文里穿插考试
- 只写 README 目录、不写课文（违反细致）
- 对照表不随新档案更新（违反全面）

---

## 每条轨写什么

| 轨 | 单元 | 完成标准 |
|---|---|---|
| index | 路线图、知识树、研究顺序、资产目录 | 能回答「下一步写哪份」 |
| courses | Level 0–10 课文 | A–J + 精密检查，不掺题 |
| protocols | 每条核心链/品类一份 19 节 | 有架构图、生命周期、假设、代价、源码入口、「不确定」适用性 |
| tracks | 专题长文与对照表 | 能横比至少 3 个项目 |
| libraries | 一条模式/反模式一页 | 问题、方案、适用、代价、真实项目、常见 bug |
| exams | 按 Level 收题 | 现在只收不考 |

---

## 协议档案固定 19 节

见 [`protocols/README.md`](protocols/README.md)。禁止各自发明目录。

---

## 当前进度（知识，不是考试）

| 轨 | 状态 | 约数 |
|---|---|---|
| index | 已立；含 [`05-optimization-roadmap.md`](index/05-optimization-roadmap.md) | 6 文件 |
| courses | L0–L10 均有正文；L8.4 数学后置 | 77 模块 |
| protocols | 20+ 链/品类；主线 19 节 + 若干过滤器页 | 见 [`protocols/README.md`](protocols/README.md) |
| tracks | 16 专题；failure-museum 92+ 案；implementation 精读 ABCI++ | ~470 文件 |
| libraries | design-patterns ~540；anti-patterns ~650；invariants ~1054；corpus C1032+ | 见 [`index/03-knowledge-assets.md`](index/03-knowledge-assets.md) |
| decision-matrix | 对照列完整；**不确定候选列**填建议档（非最终选型） | 2 表 |
| threat-model | **v1 入口已立**：[`libraries/threat-model/INDEX.md`](libraries/threat-model/INDEX.md)；README 仍是 sold-as 活页 | v1 |
| review loop | [`REVIEW_LOOP.md`](REVIEW_LOOP.md) + `tools/review_audit.py` + 小时定时器 | 已启用 |
| tools | adversarial_runner + atlas_index + invariant_corpus_links | [`tools/`](tools/README.md) |
| exams | L0 题已迁入，暂不考 | 后置 |

**canonical 分支（建议）：** `cursor/uncertain-atlas-optimization-5ee2`（本仓库 KB 最全 + 优化迭代）。  
`main` 仅含 `qtb/` 交易框架；协议知识不在 `main`。

优化路线图：[`ROADMAP.md`](ROADMAP.md)。

---

## 已知架构缺口（2026-09-17）

| 缺口 | 计划 |
|---|---|
| 285+ cometbft 快照分支难导航 | Phase 3 合并为 long-lived KB 分支 |
| ABCI++ 不变量未拆完（~1054/793） | Phase 1 继续流水线 |
| adversarial runner pytest 钩子已有（10 条 Cxx） | Phase 1 P1-4 占位已接 |
| PQ CPU 实测空（方法已写） | Phase 1 P1-5 测数字 |
| 无全文检索 | Phase 3 atlas_index v0 已有脚本 |
| 过滤器页链缺 19 节 | Phase 2 补档或永久声明 |
