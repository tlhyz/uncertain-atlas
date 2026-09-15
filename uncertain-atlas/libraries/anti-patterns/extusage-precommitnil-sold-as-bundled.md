# 反模式：把 ExtendVote Usage precommit nil will not call ExtendVote 正式三事卖成 ExtendVote Usage bundled / 已经会调 ExtendVote / 已经不会叫

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[precommit nil will not call ExtendVote ≠ bundled](../../tracks/implementation/worked-example-extusage-precommitnil-vs-bundled.md)。

## 卖法

- 「看见 precommit nil / 看见要广播 nil 票 就已经会调 ExtendVote interchangeable / 已经签了 nil 票仍带扩展 interchangeable。」
- 「看见 vote_extension 只会挂在非 nil Precommit 上 就已经 ExtendVote Usage bundled interchangeable / 已经不会叫 interchangeable。」
- 「看见 nil 票不带 CanonicalVoteExtension 就已经应用可以选 0 长扩展 interchangeable / 已经跳过 Verify interchangeable。」

## 为什么错

官方把 only on non-nil Precommit、precommit nil will not call ExtendVote、nil vote no CanonicalVoteExtension 写成三件独立的实现事。把它们卖成 ExtendVote Usage bundled、已经会调 ExtendVote、已经不会叫，会把 attachment 条件、nil 路径不调、nil 票无 extension 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage precommit nil will not call ExtendVote 正式三事，必须分开 only on non-nil Precommit、precommit nil will not call、nil vote no CanonicalVoteExtension 三个名字，不要把它们卖成 ExtendVote Usage bundled / 已经会调 ExtendVote / 已经不会叫。

## 和相邻反模式

- [extusage-sold-as-deterministic](extusage-sold-as-deterministic.md) 是 437 bundled 专用；本页是 precommit nil will not call 单句边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When broadcast，不是本页 nil 路径不调边界。
- [verifyusage-emptyext-sold-as-bundled](verifyusage-emptyext-sold-as-bundled.md) 是 Verify Usage 0 长仍会 call，不是本页 ExtendVote nil 路径边界。
