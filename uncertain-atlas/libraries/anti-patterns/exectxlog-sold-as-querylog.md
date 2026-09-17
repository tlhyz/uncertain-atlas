# 反模式：看见 ExecTxResult.log 是应用日志的输出就当成已经是 Query 日志 / 看见 ExecTxResult.info 是附加信息就当成已经是 CheckTx 附加信息 / 看见 ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略就当成已经印进本头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.log 是应用日志的输出 ≠ 已经是 Query 日志](../../tracks/implementation/worked-example-exectxlog-vs-querylog.md)。

## 塌法

1. 看见 ExecTxResult `log` 是应用日志的输出 / 看见回了日志，就当成已经是 Query 日志，或当成已经新鲜。
2. 看见 ExecTxResult `info` 是附加信息 / 看见回了信息，就当成已经是 CheckTx 附加信息，或当成已经是 Query 附加信息。
3. 看见 ExecTxResult `log` / `info` 标成非确定、引擎会记日志此外忽略 / 看见记了日志，就当成已经印进本头，或当成已经是共识。

## 为什么会出事

官方写：`log` 是应用日志的输出。`info` 是附加信息。这两栏 Deterministic = No。应用需求页写：Info 和 Log 是非确定的调试字段，CometBFT 会记日志，此外忽略。看见填了栏，不是已经是 Query 日志，也不是已经是 CheckTx 附加信息，也不是已经印进本头。

## 和相邻反模式

- [querycode-sold-as-consensus](querycode-sold-as-consensus.md) 是 Query 回包 log 就已经新鲜，不是本页这种 ExecTxResult.log 是应用日志的输出不是已经是 Query 日志。
- [checktxtx-sold-as-recheck](checktxtx-sold-as-recheck.md) 是 CheckTx 回包 info 就已经是 Query 附加信息，不是本页这种 ExecTxResult.info 是附加信息不是已经是 CheckTx 附加信息。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code / Data 就已经印进本头，不是本页这种 ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略不是已经印进本头。
