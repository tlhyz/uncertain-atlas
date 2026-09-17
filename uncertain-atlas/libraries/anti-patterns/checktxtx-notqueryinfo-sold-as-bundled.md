# 反模式：把 CheckTx 回包 info not already Query info / not already CheckTx log / not already settled 正式三事（391 余量） 说成已经是 Query 附加信息 / 已经是 CheckTx 日志 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx ≠ bundled（391）](../../tracks/implementation/worked-example-checktxtx-notqueryinfo-vs-bundled.md)。

## 卖法

把 CheckTx 请求余栏这句写成已经已经是 Query 附加信息 / 已经是 CheckTx 日志 / 已经交差 interchangeable，或已经和 391 checktxtx-vs-recheck bundled / checktxtx-notqueryinfo-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx 请求 tx / 对照当前状态验 / 回包 info 三条核心句写成三件独立的实现事。把它们卖成已经是 Query 附加信息 / 已经是 CheckTx 日志 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 info 正式三事（391 余量），必须分开 not already Query info、not already CheckTx log、not already settled 三件事，不要和 391 / 384 / 390 / 745 / 752 / 753 糊成一句。

## 和相邻反模式

- [checktxtx-sold-as-recheck](checktxtx-sold-as-recheck.md) 是 CheckTx 请求余栏 bundled（391），不是本页 item 3 单句边界。
- [proofop-notquerylog-sold-as-bundled](proofop-notquerylog-sold-as-bundled.md) 是 CheckTx 回包 log 就已经是 Query 日志（390/745），不是本页 info 边界。
