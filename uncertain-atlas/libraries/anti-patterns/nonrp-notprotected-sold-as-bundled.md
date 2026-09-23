# 反模式：把 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量）说成已经有重放保护 / 已经必须填 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[non_rp_extension 按原样签 not already replay-protected ≠ bundled（358）](../../tracks/implementation/worked-example-nonrp-notprotected-vs-bundled.md)。

## 卖法

把按原样签了 / `non_rp_extension` 按应用给的字节原样签 / 没有再套一层重放保护 写成已经有重放保护 interchangeable / 已经 replay-protected interchangeable / 已经有 Height Round ChainID 交差 interchangeable / 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable；把字段在 / non_rp_extension 字段存在 写成已经必须填 interchangeable / 已经 must-fill interchangeable / 已经必须填交差 interchangeable；把没有包装 / 不套一层重放保护 / 和 vote_extension 不同 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 358 nonrp bundled / nonrp-sold-as-protected interchangeable / 828 nonrp-notprotected interchangeable。

## 为什么错

官方把按原样签了、不是已经必须填、不是已经交差写成三件独立的实现事。把它们卖成 already replay-protected interchangeable / already must-fill interchangeable / already settled interchangeable，会把 not already replay-protected、not already must-fill、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量），必须分开 not already replay-protected、not already must-fill、not already settled 三件事，不要和 358 / 350 / 34 / 827 / 829 糊成一句。

## 和相邻反模式

- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是两份扩展两份签 bundled 全段，不是本页按原样签了 item 2 单句边界。
- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮只能交出一份扩展就已经是每一高度一份（350），不是本页 not already replay-protected 边界。
- [nonrp-notraw-sold-as-bundled](nonrp-notraw-sold-as-bundled.md) 是 vote_extension 包进 CanonicalVoteExtension not already raw-signed（358 item 1），不是本页 not already settled 边界。
