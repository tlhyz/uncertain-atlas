# 反模式：把 ExecTxResult.log / info 非确定 not already printed in header / not already consensus / not already settled 正式三事（414 余量） 说成已经印进本头 / 已经是共识 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExecTxResult.log ≠ bundled（414）](../../tracks/implementation/worked-example-exectxlog-notheader-vs-bundled.md)。

## 卖法

把 ExecTxResult 日志栏这句写成已经已经印进本头 / 已经是共识 / 已经交差 interchangeable，或已经和 414 exectxlog-vs-querylog bundled / exectxlog-notheader-sold-as-bundled interchangeable。

## 为什么错

官方把 ExecTxResult.log / ExecTxResult.info / log 与 info 非确定此外忽略 三条核心句写成三件独立的实现事。把它们卖成已经印进本头 / 已经是共识 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.log / info 非确定 正式三事（414 余量），必须分开 not already printed in header、not already consensus、not already settled 三件事，不要和 414 / 316 / 758 / 759 糊成一句。

## 和相邻反模式

- [exectxlog-sold-as-querylog](exectxlog-sold-as-querylog.md) 是 ExecTxResult 日志栏 bundled（414），不是本页 item 3 单句边界。
- [exectxlog-notquerylog-sold-as-bundled](exectxlog-notquerylog-sold-as-bundled.md) 是 ExecTxResult.log 单句边界（758 item 1），不是本页非确定此外忽略边界。
