# 模式：把 ExecTxResult 日志栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.log 是应用日志的输出 ≠ 已经是 Query 日志](../../tracks/implementation/worked-example-exectxlog-vs-querylog.md)。

## 三个名字

1. **ExecTxResult.log 是应用日志的输出不是已经是 Query 日志：** 看见回了日志不是已经新鲜。
2. **ExecTxResult.info 是附加信息不是已经是 CheckTx 附加信息：** 看见回了信息不是已经是 Query 附加信息。
3. **ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略不是已经印进本头：** 看见记了日志不是已经是共识。

## 为什么要分开叫

官方把 ExecTxResult `log` 是应用日志的输出、`info` 是附加信息、这两栏标成非确定且引擎会记日志此外忽略写成三件事。把它们叫成一个「看见填了 ExecTxResult 日志栏就已经是 Query 日志」，会把已经是 Query 日志、已经是 CheckTx 附加信息和已经印进本头一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExecTxResult 日志栏就已经是 Query 日志」，先数清问的是 ExecTxResult.log 是应用日志的输出不是已经是 Query 日志、ExecTxResult.info 是附加信息不是已经是 CheckTx 附加信息，还是 ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略不是已经印进本头，再决定要不要同一次发布。
