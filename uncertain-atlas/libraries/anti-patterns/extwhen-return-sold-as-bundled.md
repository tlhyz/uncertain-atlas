# 反模式：把 ExtendVote When return extension 正式三事卖成 ExtendVote 何时调用 bundled / ExtendVote When 正式流程 / 按原样签

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[return extension ≠ bundled](../../tracks/implementation/worked-example-extwhen-return-vs-bundled.md)。

## 卖法

- 「看见 Application returns ExtendVoteResponse.extension 就已经 ExtendVote When 正式流程 interchangeable / 已经填进 CanonicalVoteExtension interchangeable / 已经广播 Precommit interchangeable。」
- 「看见 not interpreted by the consensus algorithm 就已经是同一份扩展 interchangeable / 已经 Verify 过 interchangeable。」
- 「看见 step 3 before CanonicalVoteExtension 就已经 ExtendVote 何时调用 bundled interchangeable / 已经按原样签 interchangeable。」

## 为什么错

官方把 returns extension、not interpreted by consensus、step 3 before CanonicalVoteExtension 写成三件独立的实现事。把它们卖成 ExtendVote 何时调用 bundled、ExtendVote When 正式流程、按原样签，会把 return、不解释、step 3 顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When return extension 正式三事，必须分开 returns ExtendVoteResponse.extension、not interpreted by consensus、step 3 before CanonicalVoteExtension 三个名字，不要把它们卖成 ExtendVote 何时调用 bundled / ExtendVote When 正式流程 / 按原样签。

## 和相邻反模式

- [extwhen-call-sold-as-bundled](extwhen-call-sold-as-bundled.md) 是 ExtendVote When call / synchronous 三事，不是本页 returns extension 单句专用边界。
- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 ExtendVote 何时调用三事，不是本页 not interpreted 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 step 3 before CanonicalVoteExtension 单句专用边界。
