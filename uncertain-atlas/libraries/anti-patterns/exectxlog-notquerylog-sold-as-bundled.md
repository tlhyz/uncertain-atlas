# 反模式：把 ExecTxResult.log not already Query log / not already fresh / not already settled 正式三事（414 余量） 说成已经是 Query 日志 / 已经新鲜 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExecTxResult.log ≠ bundled（414）](../../tracks/implementation/worked-example-exectxlog-notquerylog-vs-bundled.md)。

## 卖法

把 ExecTxResult 日志栏这句写成已经已经是 Query 日志 / 已经新鲜 / 已经交差 interchangeable，或已经和 414 exectxlog-vs-querylog bundled / exectxlog-notquerylog-sold-as-bundled interchangeable。

## 为什么错

官方把 ExecTxResult.log / ExecTxResult.info / log 与 info 非确定此外忽略 三条核心句写成三件独立的实现事。把它们卖成已经是 Query 日志 / 已经新鲜 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.log 正式三事（414 余量），必须分开 not already Query log、not already fresh、not already settled 三件事，不要和 414 / 384 / 390 / 745 / 759 / 760 糊成一句。

## 和相邻反模式

- [exectxlog-sold-as-querylog](exectxlog-sold-as-querylog.md) 是 ExecTxResult 日志栏 bundled（414），不是本页 item 1 单句边界。
- [proofop-notquerylog-sold-as-bundled](proofop-notquerylog-sold-as-bundled.md) 是 CheckTx 回包 log 就已经是 Query 日志（390/745），不是本页 ExecTxResult.log 边界。
