# 反模式：把从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量）说成已经出池 / 已经永远不提 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[从提案拿掉 tx not already out-of-pool ≠ bundled（355）](../../tracks/implementation/worked-example-drop-notmempool-vs-bundled.md)。

## 卖法

把从提案拿掉 tx / 本块不提 / 回包没有它 写成已经从内存池删掉 interchangeable / 已经 out-of-pool interchangeable / 已经出池交差 interchangeable / 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable；把拿掉了 / 本块不提这笔 写成已经永远不提 interchangeable / 已经 never-propose interchangeable / 已经永远不提交差 interchangeable；把回包没有它 / 回包里没这笔 / 没写进 txs 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 355 preparedrop bundled / preparedrop-sold-as-evicted interchangeable / 818 drop-notmempool interchangeable。

## 为什么错

官方把本块不提、不是已经永远不提、不是已经交差写成三件独立的实现事。把它们卖成 already out-of-pool interchangeable / already never-propose interchangeable / already settled interchangeable，会把 not already out-of-pool、not already never-propose、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量），必须分开 not already out-of-pool、not already never-propose、not already settled 三件事，不要和 355 / 301 / 345 / 819 / 820 糊成一句。

## 和相邻反模式

- [preparedrop-sold-as-evicted](preparedrop-sold-as-evicted.md) 是 Prepare 改列表 bundled 全段，不是本页本块不提 item 1 单句边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了就已经从池里删掉（301），不是本页 not already out-of-pool 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
