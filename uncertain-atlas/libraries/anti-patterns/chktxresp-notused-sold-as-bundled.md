# 反模式：把 CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量） 写成已经 已经被引擎用了 / 已经和 Finalize 那份同一把尺 / 已经进了下一头的 LastResultsHash

**层次**：实现 / CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应**：[`../tracks/implementation/worked-example-chktxresp-notused-vs-bundled.md`](../tracks/implementation/worked-example-chktxresp-notused-vs-bundled.md)。

把 CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量） 写成已经 已经被引擎用了 / 已经和 Finalize 那份同一把尺 / 已经进了下一头的 LastResultsHash，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Data 正式三事（317 余量），必须分开 not already engine-used、not already same-scale、not already last-results 三件事，不要和 317 / 316 / 312 / 1017 / 1018 糊成一句。

也不是：

- [exectx-notheader-sold-as-bundled](exectx-notheader-sold-as-bundled.md) 是 Finalize Code/Data 仍未印进本头边界（316/1015），不是本页 CheckTx Data 仍未被引擎用边界。
- CheckTxState 已经是 ExecuteTxState 是不变量 312，不是本页字段名也叫 Data 仍未同一把尺边界。
