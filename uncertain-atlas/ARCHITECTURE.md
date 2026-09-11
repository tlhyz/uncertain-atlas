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
  protocols/             协议档案：一条链一份 19 节报告
  tracks/                横向专题：共识、状态、PQ、失败博物馆
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

---

## 每条轨写什么

| 轨 | 单元 | 完成标准 |
|---|---|---|
| index | 路线图、知识树、研究顺序、资产目录 | 能回答「下一步写哪份」 |
| courses | Level 0–10 课文 | A–J 齐全，不掺题 |
| protocols | 每条核心链一份 19 节 | 有架构图、生命周期、假设、代价、源码入口、「不确定」适用性 |
| tracks | 专题长文 | 能横比至少 3 个项目 |
| libraries | 一条模式/反模式一页 | 问题、方案、适用、代价、真实项目、常见 bug |
| exams | 按 Level 收题 | 现在只收不考 |

---

## 协议档案固定 19 节

见 [`protocols/README.md`](protocols/README.md)。所有链同一骨架，禁止各自发明目录。

---

## 当前进度（知识，不是考试）

| 轨 | 状态 |
|---|---|
| index | 已立，路径已改到五条轨 |
| courses L0–L3 | L0–L2 全课；L3 三课 + Bitcoin 档案 |
| protocols/bitcoin | 19 节第一版 |
| protocols/cometbft | 19 节第一版 |
| protocols/ethereum | 19 节第一版 |
| protocols/avalanche | 19 节第一版（对照） |
| protocols/solana | 19 节第一版 |
| tracks/state-models | 指向 L2.4 |
| tracks/consensus | 对照表 |
| tracks/post-quantum | 工程账本第一版 |
| tracks/failure-museum | CVE-2018-17144 |
| libraries | 模式 8 + 反模式 10 + 决策/威胁/不变量草稿 |
| exams | L0 题已迁入，暂不考 |
