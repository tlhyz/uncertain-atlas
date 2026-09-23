# Uncertain Atlas 架构

本目录是「不确定图谱」的长期知识系统：课程、协议档案、横向专题、模式库。

协议知识只写在这里。

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

- 把回测或策略代码写进本知识库
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

| 轨 | 状态 |
|---|---|
| index | 已立；写作顺序已改「写全知识」 |
| courses | L0–L10 均有正文；L8.4 数学后置；决策列空 |
| protocols | 主线 11 链 + 乐观 rollup 品类 + Algorand 抽签对照 |
| tracks | 上列精读 + 分区/形式化缝；最终性表已随第 8 波回填 |
| libraries | 模式 333 + 反模式 440 + 决策/威胁/不变量（439 条）+ 对抗语料 C01–C447 |
| exams | L0 题已迁入，暂不考 |
