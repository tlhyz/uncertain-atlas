# 反模式：把往提案加了一笔新的不是已经进了内存池 not already in-pool / not already checktx / not already settled 正式三事（355 余量）说成已经进池 / 已经过了 CheckTx / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[往提案加了一笔新的 not already in-pool ≠ bundled（355）](../../tracks/implementation/worked-example-add-notmempool-vs-bundled.md)。

## 卖法

把往提案加了一笔新的 / 回包里有它 / 加进了 txs 写成已经进了内存池 interchangeable / 已经 in-pool interchangeable / 已经进池交差 interchangeable / 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable；把能提 / 回包里有它 写成已经过了 CheckTx interchangeable / 已经 checktx interchangeable / 已经 CheckTx 交差 interchangeable；把加进去了 / 加进了回包 / 写进 txs 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 355 preparedrop bundled / preparedrop-sold-as-evicted interchangeable / 819 add-notmempool interchangeable。

## 为什么错

官方把回包里有它、不是已经过了 CheckTx、不是已经交差写成三件独立的实现事。把它们卖成 already in-pool interchangeable / already checktx interchangeable / already settled interchangeable，会把 not already in-pool、not already checktx、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看往提案加了一笔新的不是已经进了内存池 not already in-pool / not already checktx / not already settled 正式三事（355 余量），必须分开 not already in-pool、not already checktx、not already settled 三件事，不要和 355 / 301 / 345 / 818 / 820 糊成一句。

## 和相邻反模式

- [preparedrop-sold-as-evicted](preparedrop-sold-as-evicted.md) 是 Prepare 改列表 bundled 全段，不是本页回包里有它 item 2 单句边界。
- [drop-notmempool-sold-as-bundled](drop-notmempool-sold-as-bundled.md) 是从提案拿掉 tx not already out-of-pool（355 item 1），不是本页 not already in-pool 边界。
- [preparereturn-sold-as-trimmed](preparereturn-sold-as-trimmed.md) 是整池可见就已经只能看见装得进一块的子集（345），不是本页 not already checktx 边界。
