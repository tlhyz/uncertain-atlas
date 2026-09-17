# 模式：把 CheckTxResponse 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**例**：[CheckTx 的 Data ≠ 已经被引擎用了](../../tracks/implementation/worked-example-checktxresponse-vs-exec.md)。

## 三个名字

1. **CheckTx 的 Data 不是已经被引擎用了：** 看见回了字节不是已经进了 LastResultsHash。
2. **各节点 Data 不一样不是已经分叉：** 看见不必确定不是已经和 Finalize 同一把尺子。
3. **Priority 不是已经是共识顺序：** 看见池里优先不是已经进了块。

## 为什么要分开叫

官方把忽略这份 Data、CheckTxState 可以不同、池里显式优先写成三件事。把它们叫成一个「看见 CheckTx 回了就已经交差」，会把 Finalize 回执、CheckTxState 和池交接一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「CheckTx 已经回了 Data」，先数清问的是这份 Data 不是已经被引擎用了、各节点不一样不是已经分叉，还是 Priority 不是已经是共识顺序，再决定要不要同一次发布。
