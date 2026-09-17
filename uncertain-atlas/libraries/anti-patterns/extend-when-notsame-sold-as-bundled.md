# 反模式：把 回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事（361 余量） 卖成 已经是同一份扩展 / 已经包进 CanonicalVoteExtension / 已经交差

**层次**：实现 / ExtendVote 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-when-notsame-vs-bundled.md](../../tracks/implementation/worked-example-extend-when-notsame-vs-bundled.md)。

官方把 +2/3 prevote 才锁住再调 ExtendVote / ExtendVote 调用是同步的 / 回包字节不被共识算法解释三条核心句写成三件独立的实现事。把它们卖成已经是同一份扩展 / 已经包进 CanonicalVoteExtension / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包字节不被共识算法解释 正式三事（361 余量），必须分开 not already same extension、not already packed CanonicalVoteExtension、not already settled 三件事，不要和 361 / 358 / 359 / 510 / 842 / 843 糊成一句。

## 和相邻反模式

- [extend-when-notlater-sold-as-bundled](extend-when-notlater-sold-as-bundled.md) 是同步调用单句边界（843 item 2），不是本页回包不解释边界。
- [extwhen-fill-vs-bundled](../../tracks/implementation/worked-example-extwhen-fill-vs-bundled.md) 是正式流程填 CanonicalVoteExtension（510），不是本页不解释边界。
