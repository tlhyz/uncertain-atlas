# 模式：把 ExtendVote When construct Precommit 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 6。  
**例**：[construct Precommit ≠ bundled](../../tracks/implementation/worked-example-extwhen-precommit-vs-bundled.md)。

## 三个名字

1. **constructs Precommit (Vote) 不是 construct CanonicalVote bundled：** 看见 constructs Precommit message，不是 511 constructs and signs CanonicalVote interchangeable。
2. **using CanonicalVoteExtension and CanonicalVote 不是只有包装或只有票：** 看见 using both，不是 510 fill CanonicalVoteExtension interchangeable / 511 CanonicalVote alone interchangeable。
3. **step 6 before broadcasts 不是 ExtendVote When 正式流程 bundled：** 看见 step 6 after step 5 before step 7，不是 438 广播 Precommit interchangeable / 写进 last_commit interchangeable。

## 为什么要分开叫

官方把 constructs Precommit、using both、step 6 顺序、construct CanonicalVote bundled（511）、ExtendVote When 正式流程 bundled（438）、写进 last_commit bundled 写成三个名字。把它们叫成一个「看见签了 CanonicalVote 就已经广播 Precommit interchangeable、已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」，会把 construct、using both、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When construct Precommit 正式三事，先数清问的是 constructs Precommit 是不是 construct CanonicalVote bundled interchangeable、using both 是不是只有 CanonicalVoteExtension interchangeable / 只有 CanonicalVote interchangeable、step 6 before broadcasts 是不是 ExtendVote When 正式流程 bundled interchangeable，再决定要不要同一次发布。
