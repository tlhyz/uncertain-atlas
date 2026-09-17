# 反模式：看见 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块就当成已经会调 ExtendVote / 看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 就当成已经跳过 Verify / 看见 Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 就当成已经 Verify 过迟到扩展

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**例**：[ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块 ≠ 已经会调 ExtendVote](../../tracks/implementation/worked-example-extreq-vs-precommit.md)。

## 塌法

1. 看见 `ExtendVoteRequest` 的内容对应共识即将发 Precommit 的那份拟议块 / 看见填了请求，就当成已经会调 ExtendVote，或当成已经签了 nil 票。
2. 看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify / 看见空扩展，就当成已经跳过 Verify，或当成已经自己验过。
3. 看见 Verify `ACCEPT` 会把这张票和扩展留在内部结构、给 *h+1* 自己提议时的 Prepare 填 `ExtendedCommitInfo` / 看见收下了，就当成已经 Verify 过迟到扩展，或当成已经交差。

## 为什么会出事

官方写：`ExtendVoteRequest` 的内容对应共识算法即将发 Precommit 的那份拟议块。若 Precommit 没有带有效签的扩展，*p* 把这张 Precommit 当非法丢掉。0 长度扩展只要伴随签名也合法，就算有效。应用回 `ACCEPT` 后，*p* 把收到的票和对应扩展留在内部结构，用来在高度 *h+1*、自己当提议者的那些轮里，给 `PrepareProposal` 填 `ExtendedCommitInfo`。

## 和相邻反模式

- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮只能交出一份扩展就已经是每一高度一份，不是本页这种 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块不是已经会调 ExtendVote。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是空扩展仍会调 Verify 就已经跳过 Verify，不是本页这种 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify。
- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过，不是本页这种 Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify 过迟到扩展。
