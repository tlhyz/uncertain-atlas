# 模式：把 CheckTx 弱过滤器三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**例**：[不该验排序相关有效性 ≠ 已经该在 CheckTx 里验](../../tracks/implementation/worked-example-checktx-weak-vs-process.md)。

## 三个名字

1. **不该验排序相关有效性不是已经该在 CheckTx 里验：** 看见有效性依赖排序不是已经按将要执行的那份验过。
2. **拜占庭能提案一满块无效交易不是已经被池子挡住：** 看见拜占庭可以不在乎 CheckTx 不是已经进不了共识。
3. **ProcessProposal 对付这种行为不是已经是 CheckTx：** 看见规范点名 ProcessProposal 不是已经是 Finalize。

## 为什么要分开叫

官方把「不该验所有、尤其是排序相关」、拜占庭可以提案无效块、ProcessProposal 才是对策写成三件事。把它们叫成一个「看见过了 CheckTx 就已经验完」，会把两份状态、四门和重放保护一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见过了 CheckTx 就已经验完」，先数清问的是不该验排序相关有效性不是已经该在 CheckTx 里验、拜占庭能提案一满块无效交易不是已经被池子挡住，还是 ProcessProposal 对付这种行为不是已经是 CheckTx，再决定要不要同一次发布。
