# 模式：把 ExtendVote When construct CanonicalVote 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 5。  
**例**：[construct CanonicalVote ≠ bundled](../../tracks/implementation/worked-example-extwhen-canonicalvote-vs-bundled.md)。

## 三个名字

1. **constructs CanonicalVote 不是 fill CanonicalVoteExtension bundled：** 看见 constructs CanonicalVote structure，不是 510 signs populated CanonicalVoteExtension interchangeable。
2. **signs CanonicalVote 不是 signs populated CanonicalVoteExtension：** 看见 signs CanonicalVote structure，不是 438 已经验过扩展 interchangeable。
3. **step 5 before constructs Precommit 不是 ExtendVote When 正式流程 bundled：** 看见 step 5 after step 4 before step 6，不是 438 构造 Precommit 并广播 interchangeable。

## 为什么要分开叫

官方把 constructs CanonicalVote、signs CanonicalVote、step 5 顺序、fill CanonicalVoteExtension bundled（510）、ExtendVote When 正式流程 bundled（438）、验过扩展 bundled 写成三个名字。把它们叫成一个「看见签了 CanonicalVoteExtension 就已经验过扩展 interchangeable、已经构造 Precommit interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」，会把 construct、sign、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When construct CanonicalVote 正式三事，先数清问的是 constructs CanonicalVote 是不是 fill CanonicalVoteExtension bundled interchangeable、signs CanonicalVote 是不是 signs populated CanonicalVoteExtension interchangeable / 已经验过扩展 interchangeable、step 5 before constructs Precommit 是不是 ExtendVote When 正式流程 bundled interchangeable，再决定要不要同一次发布。
