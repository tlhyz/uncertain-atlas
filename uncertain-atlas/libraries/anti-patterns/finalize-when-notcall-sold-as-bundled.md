# 反模式：把 +2/3 precommit 才决定再调 Finalize not already will call / not already ExtendVote when / not already decided 正式三事（362 余量） 卖成 已经会调 Finalize / 已经是 ExtendVote when / 已经决定

**层次**：实现 / Finalize 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-when-notcall-vs-bundled.md](../../tracks/implementation/worked-example-finalize-when-notcall-vs-bundled.md)。

官方把 +2/3 precommit 才决定再调 Finalize / 先落决定再同步调 Finalize / 回了 AppHash 和输出哈希进 ResultHash 三条核心句写成三件独立的实现事。把它们卖成已经会调 Finalize / 已经是 ExtendVote when / 已经决定，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 precommit 才决定再调 Finalize 正式三事（362 余量），必须分开 not already will call、not already ExtendVote when、not already decided 三件事，不要和 362 / 361 / 472 finwhen / 363 / 836 / 840 / 841 糊成一句。

## 和相邻反模式

- [extwhen-call-vs-bundled](../../tracks/implementation/worked-example-extwhen-call-vs-bundled.md) 是 +2/3 prevote 才锁住再调 ExtendVote（361），不是本页 Finalize When 边界。
- finwhen-not* 别前缀是不变量 472，不是本页 +2/3 precommit 才决定再调边界。
