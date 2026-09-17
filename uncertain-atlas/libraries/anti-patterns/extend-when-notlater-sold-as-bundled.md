# 反模式：把 ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事（361 余量） 卖成 已经能稍后改扩展 / 已经离开关键路径 / 已经交差

**层次**：实现 / ExtendVote 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-when-notlater-vs-bundled.md](../../tracks/implementation/worked-example-extend-when-notlater-vs-bundled.md)。

官方把 +2/3 prevote 才锁住再调 ExtendVote / ExtendVote 调用是同步的 / 回包字节不被共识算法解释三条核心句写成三件独立的实现事。把它们卖成已经能稍后改扩展 / 已经离开关键路径 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 调用是同步的 正式三事（361 余量），必须分开 not already can change later、not already left critical path、not already settled 三件事，不要和 361 / 354 / 362 / 840 / 842 / 844 糊成一句。

## 和相邻反模式

- [extend-when-notcall-sold-as-bundled](extend-when-notcall-sold-as-bundled.md) 是 +2/3 prevote 才锁住再调单句边界（842 item 1），不是本页同步调用边界。
- [finalize-when-notpersist-sold-as-bundled](finalize-when-notpersist-sold-as-bundled.md) 是先落决定再同步调 Finalize（362/840），不是本页 ExtendVote 同步边界。
