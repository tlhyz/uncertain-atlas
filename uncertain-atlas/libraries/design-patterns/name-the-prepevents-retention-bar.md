# 模式：把 Prepare 事件保留路径正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[Prepare MAY 产出块/tx 事件 ≠ 已经在 PrepareProposalResponse 里交回](../../tracks/implementation/worked-example-prepevents-vs-finalize.md)。

## 三个名字

1. **Prepare MAY 产出块/tx 事件不是已经在 PrepareProposalResponse 里交回：** 看见先产出不是已经 Prepare 返回时就交给引擎。
2. **MUST 留到块决定之后不是已经 Process 时就交出去：** 看见必须留着不是已经 Process 时就索引。
3. **经 FinalizeBlockResponse 交回不是已经是 CheckTx / ExecTxResult events：** 看见 Finalize 给了 events 不是已经池门或逐笔回包 interchangeable。

## 为什么要分开叫

官方把 Prepare 事件保留路径写成三个名字。把它们叫成一个「看见 Prepare 里产出了事件就已经交给引擎」，会把 MAY 产出、MUST 保留到决定、Finalize 交回和 CheckTx / ExecTxResult events 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里产出了事件就已经交给引擎」，先数清问的是 Prepare MAY 产出块/tx 事件是不是已经在 PrepareProposalResponse 里交回、MUST 留到块决定之后是不是已经 Process 时就交出去，还是经 FinalizeBlockResponse 交回是不是已经是 CheckTxResponse.events / ExecTxResult.events，再决定要不要同一次发布。
