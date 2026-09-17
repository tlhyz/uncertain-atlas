# 模式：把 ExecTxResult.info not already CheckTx info / not already Query info / not already settled 正式三事（414 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.info ≠ bundled（414）](../../tracks/implementation/worked-example-exectxlog-notchecktxinfo-vs-bundled.md)。

## 三个名字

1. **info 不是已经是 CheckTx 附加信息：** 看见回了信息，不是已经 391 / 754 interchangeable / 759 exectxlog-notchecktxinfo interchangeable。
2. **看见回了信息 不是已经是 Query 附加信息：** 看见有附加字段，不是已经 384 interchangeable。
3. **看见能回 不是已经交差：** 看见 ExecTxResult.info，不是已经交差 interchangeable。

官方把 ExecTxResult.log / ExecTxResult.info / log 与 info 非确定此外忽略 三条核心句拆成三个名字。把它们叫成一个「看见填了 ExecTxResult 日志栏就已经是 Query 日志」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.info 正式三事（414 余量），先数清问的是 info 是不是已经是 CheckTx 附加信息 / 391、是不是已经是 Query 附加信息 / 384、还是看见能回是不是已经交差，再决定要不要同一次发布。414 exectxlog vs querylog bundled unbundling 在本页 item 2 续。
