# 反模式：把 non_rp_extension 按原样签 not already has replay protection / not already must-fill / not already settled 正式三事（358 余量） 卖成 已经有重放保护 / 已经必须填 / 已经交差

**层次**：实现 / 两份扩展两份签。  
**分类**：建议（产品）。  
**对应例**：[worked-example-nonrp-notrp-vs-bundled.md](../../tracks/implementation/worked-example-nonrp-notrp-vs-bundled.md)。

官方把 vote_extension 会包进 CanonicalVoteExtension / non_rp_extension 按原样签 / 要签原样数据可以用 non_rp 三条核心句写成三件独立的实现事。把它们卖成已经有重放保护 / 已经必须填 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 按原样签 正式三事（358 余量），必须分开 not already has replay protection、not already must-fill、not already settled 三件事，不要和 358 / 350 / 353 / 848 / 850 糊成一句。

## 和相邻反模式

- [nonrp-notasis-sold-as-bundled](nonrp-notasis-sold-as-bundled.md) 是包装单句边界（848 item 1），不是本页原样签边界。
- 一轮只能交出一份扩展是不变量 350，不是本页原样签边界。
