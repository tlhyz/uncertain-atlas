# 反模式：把 ExtendVote When construct CanonicalVote 正式三事卖成 fill CanonicalVoteExtension bundled / ExtendVote When 正式流程 / 验过扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[construct CanonicalVote ≠ bundled](../../tracks/implementation/worked-example-extwhen-canonicalvote-vs-bundled.md)。

## 卖法

- 「看见 constructs and signs CanonicalVote 就已经 fill CanonicalVoteExtension interchangeable / 已经 signs populated CanonicalVoteExtension interchangeable。」
- 「看见签了 CanonicalVote 就已经验过扩展 interchangeable / 已经 Accept interchangeable。」
- 「看见 step 5 就已经 ExtendVote When 正式流程 interchangeable / 已经广播 Precommit interchangeable / 已经写进 last_commit interchangeable。」

## 为什么错

官方把 constructs CanonicalVote、signs CanonicalVote、step 5 顺序写成三件独立的实现事。把它们卖成 fill CanonicalVoteExtension bundled、ExtendVote When 正式流程、验过扩展，会把 construct、sign、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When construct CanonicalVote 正式三事，必须分开 constructs CanonicalVote、signs CanonicalVote、step 5 before constructs Precommit 三个名字，不要把它们卖成 fill CanonicalVoteExtension bundled / ExtendVote When 正式流程 / 验过扩展。

## 和相邻反模式

- [extwhen-fill-sold-as-bundled](extwhen-fill-sold-as-bundled.md) 是 ExtendVote When fill CanonicalVoteExtension 三事，不是本页 constructs CanonicalVote 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 step 5 before constructs Precommit 单句专用边界。
- [extwhen-return-sold-as-bundled](extwhen-return-sold-as-bundled.md) 是 ExtendVote When return extension 三事，不是本页 signs CanonicalVote 单句专用边界。
