# 反模式：把 vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事（358 余量） 卖成 已经按原样签 / 已经是 CanonicalVote / 已经交差

**层次**：实现 / 两份扩展两份签。  
**分类**：建议（产品）。  
**对应例**：[worked-example-nonrp-notasis-vs-bundled.md](../../tracks/implementation/worked-example-nonrp-notasis-vs-bundled.md)。

官方把 vote_extension 会包进 CanonicalVoteExtension / non_rp_extension 按原样签 / 要签原样数据可以用 non_rp 三条核心句写成三件独立的实现事。把它们卖成已经按原样签 / 已经是 CanonicalVote / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 会包进 CanonicalVoteExtension 正式三事（358 余量），必须分开 not already signed as-is、not already CanonicalVote、not already settled 三件事，不要和 358 / 34 / 361 / 844 / 350 / 849 / 850 糊成一句。

## 和相邻反模式

- [extend-when-notsame-sold-as-bundled](extend-when-notsame-sold-as-bundled.md) 是回包字节不解释就已经包进 CanonicalVoteExtension（361/844），不是本页包装边界。
- CanonicalVoteExtension 就已经是 CanonicalVote 是不变量 34，不是本页包装边界。
