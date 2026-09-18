# 反模式：看见 Prepare 产出了事件就当成已经在 PrepareProposalResponse 里交回 / 看见留着事件就当成已经 Process 时就交出去 / 看见 Finalize 回了 events 就当成已经是 CheckTx / ExecTxResult events

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[Prepare MAY 产出块/tx 事件 ≠ 已经在 PrepareProposalResponse 里交回](../../tracks/implementation/worked-example-prepevents-vs-finalize.md)。

## 塌法

1. 看见 Prepare 执行准备提案时 MAY 产出块事件或交易事件 / 看见先跑了，就当成已经在 PrepareProposalResponse 里交回，或当成已经 Prepare 返回时引擎就已经收到。
2. 看见应用 MUST 把这些事件留到块决定之后 / 看见留着，就当成已经 Process 时就交出去，或当成已经 prevote nil / REJECT 时就可以丢掉不算。
3. 看见然后经 FinalizeBlockResponse 交给 CometBFT / 看见 Finalize 回了 events，就当成已经是 CheckTxResponse.events，或当成已经是 ExecTxResult.events，或当成已经像 Code/Data 那样印进 LastResultsHash。

## 为什么会出事

官方写：As a result of executing the prepared proposal, the Application may produce block events or transaction events。The Application must keep those events until a block is decided and then pass them on to CometBFT via FinalizeBlockResponse。`PrepareProposalResponse` 只有 `txs`。这不是已经 Prepare 返回时就交给引擎，不是已经 Process 时就索引，也不是已经 CheckTx / ExecTxResult events interchangeable。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验三事 bundled，不是本页这种事件保留路径单独切片。
- [finrespbar-sold-as-header](finrespbar-sold-as-header.md) 是 FinalizeBlockResponse.events 就已经印进本头，不是本页这种 Prepare→Finalize 保留路径不是已经池门或逐笔 events。
- [exectxevents-sold-as-header](exectxevents-sold-as-header.md) 是 ExecTxResult.events 就已经印进本头，不是本页这种 Prepare 事件不是已经 ExecTxResult.events。
