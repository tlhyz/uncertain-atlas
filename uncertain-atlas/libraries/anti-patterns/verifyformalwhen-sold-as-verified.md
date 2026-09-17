# 反模式：看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 就当成已经跳过 Verify / 看见带有效签就会调 VerifyVoteExtension 就当成已经验过扩展 / 看见 ACCEPT 留给 h+1 Prepare 就当成已经写进 last_commit

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**例**：[Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify ≠ 已经跳过 Verify](../../tracks/implementation/worked-example-verify-formal-when-vs-flow.md)。

## 塌法

1. 看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify / 看见丢掉了，就当成已经跳过 Verify，或当成已经验过扩展。
2. 看见带有效签就会调 `VerifyVoteExtension` / 看见 CometBFT 会叫，就当成已经验过扩展，或当成已经 Accept。
3. 看见 `ACCEPT` 会把票和扩展留给 *h+1* 自己提议时的 Prepare 填 `ExtendedCommitInfo` / 看见 `REJECT` 会把 Precommit 当非法丢掉，就当成已经写进 last_commit，或当成已经 Verify 过迟到扩展。

## 为什么会出事

官方写：Precommit 没有带有效签的扩展会先当非法丢掉，不调 Verify。带有效签才会调 `VerifyVoteExtension`。`ACCEPT` 会把票和扩展留在内部结构，给 *h+1* 自己提议时的 Prepare 填 `ExtendedCommitInfo`。`REJECT` 会把 Precommit 当非法丢掉。看见收到 Precommit，不是已经跳过 Verify，也不是已经验过扩展，也不是已经写进 last_commit。

## 和相邻反模式

- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是空扩展仍会调 Verify 就已经跳过 Verify，不是本页这种 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify。
- [extreq-sold-as-precommit](extreq-sold-as-precommit.md) 是 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块就已经会调 ExtendVote，不是本页这种带有效签就会调 VerifyVoteExtension 不是已经验过扩展。
- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过，不是本页这种 ACCEPT 留给 h+1 Prepare 不是已经写进 last_commit。
- [verifystatus-sold-as-vote](verifystatus-sold-as-vote.md) 是 VerifyStatus 的 ACCEPT 就已经验过扩展，不是本页这种带有效签就会调 VerifyVoteExtension 不是已经 Accept。
