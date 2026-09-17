# 反模式：把 往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事（355 余量） 卖成 已经进了内存池 / 已经过了 CheckTx / 已经交差

**层次**：实现 / Prepare 改列表。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-drop-notinpool-vs-bundled.md](../../tracks/implementation/worked-example-prepare-drop-notinpool-vs-bundled.md)。

官方把从提案拿掉 tx / 往提案加了一笔新的 / 把 t1 改成 t2 三条核心句写成三件独立的实现事。把它们卖成已经进了内存池 / 已经过了 CheckTx / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看往提案加了一笔新的 正式三事（355 余量），必须分开 not already in mempool、not already passed CheckTx、not already settled 三件事，不要和 355 / 345 / 317 / 854 / 856 糊成一句。

## 和相邻反模式

- [prepare-drop-notdeleted-sold-as-bundled](prepare-drop-notdeleted-sold-as-bundled.md) 是拿掉出池单句边界（854 item 1），不是本页加新的边界。
- 整池可见就已经只能看见装得进一块的子集是不变量 345，不是本页加新的边界。
