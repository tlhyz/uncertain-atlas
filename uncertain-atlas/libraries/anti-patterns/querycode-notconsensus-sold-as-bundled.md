# 反模式：把 Query 回包 code not already past consensus / not already CheckTx reject-broadcast / not already settled 正式三事（384 余量） 说成已经过了共识 / 已经是 CheckTx 那种拒广播 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（384）](../../tracks/implementation/worked-example-querycode-notconsensus-vs-bundled.md)。

## 卖法

把 Query 回包码这句写成已经已经过了共识 / 已经是 CheckTx 那种拒广播 / 已经交差 interchangeable，或已经和 384 querycode-vs-consensus bundled / querycode-notconsensus-sold-as-bundled interchangeable。

## 为什么错

官方把 Query 回包 code / log / info 三条核心句写成三件独立的实现事。把它们卖成已经过了共识 / 已经是 CheckTx 那种拒广播 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 code 正式三事（384 余量），必须分开 not already past consensus、not already CheckTx reject-broadcast、not already settled 三件事，不要和 384 / 373 / 777 / 778 糊成一句。

## 和相邻反模式

- [querycode-sold-as-consensus](querycode-sold-as-consensus.md) 是 Query 回包码 bundled（384），不是本页 item 1 单句边界。
- [exectxlog-notquerylog-sold-as-bundled](exectxlog-notquerylog-sold-as-bundled.md) 是 ExecTxResult.log 就已经是 Query 日志（414/758），不是本页 Query code 边界。
