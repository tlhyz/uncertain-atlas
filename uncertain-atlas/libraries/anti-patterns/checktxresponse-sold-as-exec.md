# 反模式：看见 CheckTx 的 Data 就当成已经被引擎用了 / 看见各节点 Data 不一样就当成已经分叉 / 看见 Priority 就当成已经是共识顺序

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**例**：[CheckTx 的 Data ≠ 已经被引擎用了](../../tracks/implementation/worked-example-checktxresponse-vs-exec.md)。

## 塌法

1. 看见 CheckTxResponse.Data / 看见回了结果字节，就当成已经被 CometBFT 用了，或当成已经是 ExecTxResult.Data。
2. 看见 Data 不确定 / 看见各节点 Data 不一样，就当成已经分叉，或当成已经和 Finalize 的 Data 同一把确定性尺子。
3. 看见 Priority / 看见排进提案优先，就当成已经是共识顺序，或当成已经进了块。

## 为什么会出事

官方写：CometBFT 忽略 CheckTxResponse 里的 Data；这份 Data 不必确定，因为各节点 CheckTxState 可以不一样。Priority 只是内存池里显式优先，好进一块提案。

## 和相邻反模式

- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Finalize 的 Data ≠ 已经印进本头，不是本页这种被忽略的 CheckTx Data。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState，不是本页。
