# 反模式：把 要签原样数据可以用 non_rp not already same as vote_extension / not already empty still verify / not already settled 正式三事（358 余量） 卖成 已经和 vote_extension 同一份 / 已经是空扩展仍验签 / 已经交差

**层次**：实现 / 两份扩展两份签。  
**分类**：建议（产品）。  
**对应例**：[worked-example-nonrp-notsame-vs-bundled.md](../../tracks/implementation/worked-example-nonrp-notsame-vs-bundled.md)。

官方把 vote_extension 会包进 CanonicalVoteExtension / non_rp_extension 按原样签 / 要签原样数据可以用 non_rp 三条核心句写成三件独立的实现事。把它们卖成已经和 vote_extension 同一份 / 已经是空扩展仍验签 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看要签原样数据可以用 non_rp 正式三事（358 余量），必须分开 not already same as vote_extension、not already empty still verify、not already settled 三件事，不要和 358 / 353 / 361 / 844 / 350 / 848 / 849 糊成一句。

## 和相邻反模式

- [nonrp-notrp-sold-as-bundled](nonrp-notrp-sold-as-bundled.md) 是原样签单句边界（849 item 2），不是本页第二份字段边界。
- [extend-when-notsame-sold-as-bundled](extend-when-notsame-sold-as-bundled.md) 是回包字节不解释就已经是同一份（361/844），不是本页第二份字段边界。
