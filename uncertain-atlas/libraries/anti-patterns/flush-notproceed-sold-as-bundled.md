# 反模式：把 立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事（374 余量） 卖成 已经能往下走 / 已经 Commit / 已经解锁

**层次**：实现 / Flush。  
**分类**：建议（产品）。  
**对应例**：[worked-example-flush-notproceed-vs-bundled.md](../../tracks/implementation/worked-example-flush-notproceed-vs-bundled.md)。

官方把 Flush 冲队列 / 定期 Flush / 立刻 Flush 三条核心句写成三件独立的实现事。把它们卖成已经能往下走 / 已经 Commit / 已经解锁，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻 Flush 正式三事（374 余量），必须分开 not already can proceed、not already Commit、not already unlocked 三件事，不要和 374 / 310 / 493 / 673 / 399 / 733 / 803 / 804 糊成一句。

## 和相邻反模式

- [flush-notgates-sold-as-bundled](flush-notgates-sold-as-bundled.md) 是定期 Flush 单句边界（804 item 2），不是本页立刻 Flush 边界。
- [flushusage-notimmediatesync-sold-as-bundled](flushusage-notimmediatesync-sold-as-bundled.md) 是 Usage immediately sync 就已经回包（493/673），不是本页立刻 Flush 边界。
