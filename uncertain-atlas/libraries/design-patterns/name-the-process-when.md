# 模式：把 Process 何时调用三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[Process 调用是同步的 ≠ 已经能在返回之后再改裁决](../../tracks/implementation/worked-example-process-when-vs-later.md)。

## 三个名字

1. **Process 调用是同步的不是已经能在返回之后再改裁决：** 看见引擎在等回包不是已经离开关键路径。
2. **只做基本检查再异步 Process 不是已经还能再 Reject：** 看见已经回了 ACCEPT 不是已经还能强迫 prevote/precommit nil。
3. **非验证者可以立刻回 ACCEPT 不是已经验过这块：** 看见不是验证者不是已经是验证者也可以立刻交差。

## 为什么要分开叫

官方把 Process 调用是同步的、异步之后不能再改票、非验证者可以立刻 ACCEPT 写成三件事。把它们叫成一个「看见已经回了就已经能稍后改裁决」，会把立刻整块执行离开关键路径、四门和提议者 Process 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见已经回了就已经能稍后改裁决」，先数清问的是 Process 调用是同步的不是已经能在返回之后再改裁决、只做基本检查再异步 Process 不是已经还能再 Reject，还是非验证者可以立刻回 ACCEPT 不是已经验过这块，再决定要不要同一次发布。
