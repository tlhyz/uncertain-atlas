# 反模式：把 ExecTxResult.info not already CheckTx info / not already Query info / not already settled 正式三事（414 余量） 说成已经是 CheckTx 附加信息 / 已经是 Query 附加信息 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExecTxResult.info ≠ bundled（414）](../../tracks/implementation/worked-example-exectxlog-notchecktxinfo-vs-bundled.md)。

## 卖法

把 ExecTxResult 日志栏这句写成已经已经是 CheckTx 附加信息 / 已经是 Query 附加信息 / 已经交差 interchangeable，或已经和 414 exectxlog-vs-querylog bundled / exectxlog-notchecktxinfo-sold-as-bundled interchangeable。

## 为什么错

官方把 ExecTxResult.log / ExecTxResult.info / log 与 info 非确定此外忽略 三条核心句写成三件独立的实现事。把它们卖成已经是 CheckTx 附加信息 / 已经是 Query 附加信息 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.info 正式三事（414 余量），必须分开 not already CheckTx info、not already Query info、not already settled 三件事，不要和 414 / 391 / 754 / 384 / 758 / 760 糊成一句。

## 和相邻反模式

- [exectxlog-sold-as-querylog](exectxlog-sold-as-querylog.md) 是 ExecTxResult 日志栏 bundled（414），不是本页 item 2 单句边界。
- [checktxtx-notqueryinfo-sold-as-bundled](checktxtx-notqueryinfo-sold-as-bundled.md) 是 CheckTx 回包 info 就已经是 Query 附加信息（391/754），不是本页 ExecTxResult.info 边界。
