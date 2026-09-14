# 反模式：把 ExtendVote When construct Precommit 正式三事卖成 construct CanonicalVote bundled / ExtendVote When 正式流程 / 写进 last_commit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[construct Precommit ≠ bundled](../../tracks/implementation/worked-example-extwhen-precommit-vs-bundled.md)。

## 卖法

- 「看见 constructs Precommit 就已经 construct CanonicalVote interchangeable / 已经 fill CanonicalVoteExtension interchangeable。」
- 「看见 using CanonicalVoteExtension and CanonicalVote 就已经只有 CanonicalVote interchangeable / 已经包装就是票 interchangeable。」
- 「看见 step 6 就已经 ExtendVote When 正式流程 interchangeable / 已经广播 Precommit interchangeable / 已经写进 last_commit interchangeable。」

## 为什么错

官方把 constructs Precommit、using both、step 6 顺序写成三件独立的实现事。把它们卖成 construct CanonicalVote bundled、ExtendVote When 正式流程、写进 last_commit，会把 construct、using both、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When construct Precommit 正式三事，必须分开 constructs Precommit、using CanonicalVoteExtension and CanonicalVote、step 6 before broadcasts 三个名字，不要把它们卖成 construct CanonicalVote bundled / ExtendVote When 正式流程 / 写进 last_commit。

## 和相邻反模式

- [extwhen-canonicalvote-sold-as-bundled](extwhen-canonicalvote-sold-as-bundled.md) 是 ExtendVote When construct CanonicalVote 三事，不是本页 constructs Precommit 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 step 6 before broadcasts 单句专用边界。
- [extwhen-fill-sold-as-bundled](extwhen-fill-sold-as-bundled.md) 是 ExtendVote When fill CanonicalVoteExtension 三事，不是本页 using both 单句专用边界。
