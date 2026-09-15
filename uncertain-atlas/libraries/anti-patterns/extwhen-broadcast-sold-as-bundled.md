# 反模式：把 ExtendVote When broadcast Precommit 正式三事卖成 construct Precommit bundled / ExtendVote When 正式流程 / 写进 last_commit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[broadcast Precommit ≠ bundled](../../tracks/implementation/worked-example-extwhen-broadcast-vs-bundled.md)。

## 卖法

- 「看见 broadcasts the Precommit message 就已经 constructs Precommit using both interchangeable / 已经 construct CanonicalVote interchangeable。」
- 「看见 step 7 就已经 fill CanonicalVoteExtension interchangeable / 已经 signs populated CanonicalVoteExtension interchangeable。」
- 「看见广播了 就已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable / 已经交差 interchangeable。」

## 为什么错

官方把 broadcasts Precommit、step 7 顺序、broadcast 与 last_commit/Verify 边界写成三件独立的实现事。把它们卖成 construct Precommit bundled、ExtendVote When 正式流程、写进 last_commit，会把 broadcast、顺序、后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事，必须分开 broadcasts Precommit、step 7 after step 6、broadcasts 不是 last_commit/Verify 三个名字，不要把它们卖成 construct Precommit bundled / ExtendVote When 正式流程 / 写进 last_commit。

## 和相邻反模式

- [extwhen-precommit-sold-as-bundled](extwhen-precommit-sold-as-bundled.md) 是 ExtendVote When construct Precommit 三事，不是本页 broadcasts Precommit 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 broadcasts 不是 last_commit 单句专用边界。
- [extwhen-return-sold-as-bundled](extwhen-return-sold-as-bundled.md) 是 ExtendVote When return extension 三事，不是本页 step 7 顺序单句专用边界。
