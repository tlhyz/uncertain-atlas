# 反模式：把 从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事（355 余量） 卖成 已经从内存池删掉 / 已经永远不提 / 已经交差

**层次**：实现 / Prepare 改列表。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-drop-notdeleted-vs-bundled.md](../../tracks/implementation/worked-example-prepare-drop-notdeleted-vs-bundled.md)。

官方把从提案拿掉 tx / 往提案加了一笔新的 / 把 t1 改成 t2 三条核心句写成三件独立的实现事。把它们卖成已经从内存池删掉 / 已经永远不提 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从提案拿掉 tx 正式三事（355 余量），必须分开 not already deleted from mempool、not already never propose、not already settled 三件事，不要和 355 / 301 / 356 / 853 / 855 / 856 糊成一句。

## 和相邻反模式

- [validvalue-notraw-sold-as-bundled](validvalue-notraw-sold-as-bundled.md) 是没调 Prepare 就已经从提案拿掉 tx（356/853），不是本页拿掉出池边界。
- 提案收了就已经从池里删掉是不变量 301，不是本页本块不提边界。
