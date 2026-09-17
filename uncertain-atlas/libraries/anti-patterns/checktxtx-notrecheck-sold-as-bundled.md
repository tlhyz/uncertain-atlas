# 反模式：把 CheckTx 请求 tx not already Recheck / not already four gates / not already settled 正式三事（391 余量） 说成已经是 Recheck / 已经四门齐了 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx ≠ bundled（391）](../../tracks/implementation/worked-example-checktxtx-notrecheck-vs-bundled.md)。

## 卖法

把 CheckTx 请求余栏这句写成已经已经是 Recheck / 已经四门齐了 / 已经交差 interchangeable，或已经和 391 checktxtx-vs-recheck bundled / checktxtx-notrecheck-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx 请求 tx / 对照当前状态验 / 回包 info 三条核心句写成三件独立的实现事。把它们卖成已经是 Recheck / 已经四门齐了 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 请求 tx 正式三事（391 余量），必须分开 not already Recheck、not already four gates、not already settled 三件事，不要和 391 / 373 / 484 / 707 / 753 / 754 糊成一句。

## 和相邻反模式

- [checktxtx-sold-as-recheck](checktxtx-sold-as-recheck.md) 是 CheckTx 请求余栏 bundled（391），不是本页 item 1 单句边界。
- [chktxtype-sold-as-recheck](chktxtype-sold-as-recheck.md) 是 CheckTx Request type New vs Recheck（484），不是本页请求字节边界。
