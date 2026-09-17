# 模式：把 ExecTxResult.log / info 非确定 not already printed in header / not already consensus / not already settled 正式三事（414 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.log ≠ bundled（414）](../../tracks/implementation/worked-example-exectxlog-notheader-vs-bundled.md)。

## 三个名字

1. **nondet 不是已经印进本头：** 看见记了日志，不是已经 316 interchangeable / 760 exectxlog-notheader interchangeable。
2. **看见记了日志 不是已经是共识：** 看见标成非确定，不是已经 316 interchangeable。
3. **看见被忽略 不是已经交差：** 看见 log / info 被忽略，不是已经交差 interchangeable。

官方把 ExecTxResult.log / ExecTxResult.info / log 与 info 非确定此外忽略 三条核心句拆成三个名字。把它们叫成一个「看见填了 ExecTxResult 日志栏就已经是 Query 日志」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.log / info 非确定 正式三事（414 余量），先数清问的是是不是已经印进本头 / 316、是不是已经是共识 / 316、还是看见被忽略是不是已经交差，再决定要不要同一次发布。414 exectxlog vs querylog bundled unbundling 在本页 item 3 完成。
