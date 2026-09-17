# 反模式：把 定期 Flush not already four gates / not already received / not already settled 正式三事（374 余量） 卖成 已经是四门 / 已经收到 / 已经交差

**层次**：实现 / Flush。  
**分类**：建议（产品）。  
**对应例**：[worked-example-flush-notgates-vs-bundled.md](../../tracks/implementation/worked-example-flush-notgates-vs-bundled.md)。

官方把 Flush 冲队列 / 定期 Flush / 立刻 Flush 三条核心句写成三件独立的实现事。把它们卖成已经是四门 / 已经收到 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看定期 Flush 正式三事（374 余量），必须分开 not already four gates、not already received、not already settled 三件事，不要和 374 / 307 / 493 / 672 / 492 / 674 / 803 / 805 糊成一句。

## 和相邻反模式

- [flush-notdelivered-sold-as-bundled](flush-notdelivered-sold-as-bundled.md) 是冲队列单句边界（803 item 1），不是本页定期 Flush 边界。
- [flushusage-notperiodicasync-sold-as-bundled](flushusage-notperiodicasync-sold-as-bundled.md) 是 Usage periodically async 就已经发出去（493/672），不是本页定期 Flush 边界。
