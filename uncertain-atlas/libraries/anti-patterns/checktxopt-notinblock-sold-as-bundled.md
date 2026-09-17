# 反模式：把 Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事（373 余量） 卖成 已经没进块 / 已经被挡住拜占庭 / 已经交差

**层次**：实现 / CheckTx 可选。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktxopt-notinblock-vs-bundled.md](../../tracks/implementation/worked-example-checktxopt-notinblock-vs-bundled.md)。

官方把 CheckTx 技术上可选 / Code ≠ 0 拒收 / 回包码不再另有含义三条核心句写成三件独立的实现事。把它们卖成已经没进块 / 已经被挡住拜占庭 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code≠0 拒收 正式三事（373 余量），必须分开 not already not-in-block、not already byzantine blocked、not already settled 三件事，不要和 373 / 316 / 489 / 686 / 381 / 785 / 806 / 808 糊成一句。

## 和相邻反模式

- [checktxopt-notsettled-sold-as-bundled](checktxopt-notsettled-sold-as-bundled.md) 是可选单句边界（806 item 1），不是本页 Code≠0 拒收边界。
- [chktxcodereject-notgossip-sold-as-bundled](chktxcodereject-notgossip-sold-as-bundled.md) 是 Usage Code≠0 就已经拒广播（489/686），不是本页拒收边界。
