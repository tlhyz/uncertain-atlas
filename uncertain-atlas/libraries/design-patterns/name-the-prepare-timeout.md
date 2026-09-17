# 模式：把 Prepare 及时性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**例**：[立刻整块执行 ≠ 已经离开关键路径](../../tracks/implementation/worked-example-prepare-timeout-vs-liveness.md)。

## 三个名字

1. **立刻整块执行不是已经离开关键路径：** 看见执行回了不是已经不挡 q 的提议钟。
2. **填了 TimeoutPropose 不是已经装得下：** 看见同步期不是 q 的提议钟已经不会响。
3. **又开一轮不是已经丢了活性：** 看见 TimeoutPropose 只是初值不是超时已经不再涨。

## 为什么要分开叫

官方把 Prepare 整块执行站在关键路径上、同步期里 *q* 的初值必须装得下、再开一轮不是丢掉活性写成三件事。把它们叫成一个「看见立刻执行了就已经来得及」，会把四门、本地超时和候选状态一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「立刻执行就已经来得及」，先数清问的是立刻整块执行不是已经离开关键路径、填了 TimeoutPropose 不是已经装得下，还是又开一轮不是已经丢了活性，再决定要不要同一次发布。
