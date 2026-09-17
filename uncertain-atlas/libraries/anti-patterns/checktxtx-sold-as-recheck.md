# 反模式：看见 CheckTx 请求 tx 是请求交易字节就当成已经是 Recheck / 看见 CheckTx 对照当前状态验、不应用这笔描述的状态改动就当成已经按 ExecuteTxState 验过 / 看见 CheckTx 回包 info 是附加信息就当成已经是 Query 附加信息

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**例**：[CheckTx 请求 tx 是请求交易字节 ≠ 已经是 Recheck](../../tracks/implementation/worked-example-checktxtx-vs-recheck.md)。

## 塌法

1. 看见 CheckTx 请求 `tx` 是请求交易字节 / 看见填了 tx，就当成已经是 Recheck，或当成已经是四门已经结算。
2. 看见 CheckTx 对照当前状态验、不应用这笔描述的状态改动 / 看见验了，就当成已经按 ExecuteTxState 验过，或当成已经参与处理块。
3. 看见 CheckTx 回包 `info` 是附加信息 / 看见回了信息，就当成已经是 Query 附加信息，或当成已经是 CheckTx 日志。

## 为什么会出事

官方写：`tx` 是请求交易字节。CheckTx 对照应用当前状态验这笔交易，例如验签和余额，但不应用这笔描述的任何状态改动。CheckTx 回包 `info` 是附加信息。

## 和相邻反模式

- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 RECHECK 就已经是一笔新交易，不是本页这种 CheckTx 请求 tx 是请求交易字节不是已经是 Recheck。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 CheckTx 技术上可选、不参与处理块就已经是四门已经结算，不是本页这种 CheckTx 对照当前状态验、不应用这笔描述的状态改动不是已经按 ExecuteTxState 验过。
- [querycode-sold-as-consensus](querycode-sold-as-consensus.md) 是 Query 回包 info 就已经是按键查，不是本页这种 CheckTx 回包 info 是附加信息不是已经是 Query 附加信息。
