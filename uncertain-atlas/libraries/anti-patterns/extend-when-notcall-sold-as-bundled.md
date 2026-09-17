# 反模式：把 +2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事（361 余量） 卖成 已经会调 ExtendVote / 已经是一轮一份扩展 / 已经锁住

**层次**：实现 / ExtendVote 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-when-notcall-vs-bundled.md](../../tracks/implementation/worked-example-extend-when-notcall-vs-bundled.md)。

官方把 +2/3 prevote 才锁住再调 ExtendVote / ExtendVote 调用是同步的 / 回包字节不被共识算法解释三条核心句写成三件独立的实现事。把它们卖成已经会调 ExtendVote / 已经是一轮一份扩展 / 已经锁住，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 prevote 才锁住再调 ExtendVote 正式三事（361 余量），必须分开 not already will call、not already one-per-round、not already locked 三件事，不要和 361 / 350 / 507–512 extwhen / 362 / 839 / 843 / 844 糊成一句。

## 和相邻反模式

- [extwhen-call-vs-bundled](../../tracks/implementation/worked-example-extwhen-call-vs-bundled.md) 是 ExtendVote When 正式流程别前缀（508），不是本页 +2/3 prevote 才锁住再调边界。
- [finalize-when-notcall-sold-as-bundled](finalize-when-notcall-sold-as-bundled.md) 是 +2/3 precommit 才决定再调 Finalize（362/839），不是本页 ExtendVote When 边界。
