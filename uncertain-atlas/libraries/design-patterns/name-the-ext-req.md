# 模式：把 ExtendVote 请求对应三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**例**：[ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块 ≠ 已经会调 ExtendVote](../../tracks/implementation/worked-example-extreq-vs-precommit.md)。

## 三个名字

1. **ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块不是已经会调 ExtendVote：** 看见填了请求不是已经签了 nil 票。
2. **Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify：** 看见空扩展不是已经自己验过。
3. **Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify 过迟到扩展：** 看见收下了不是已经交差。

## 为什么要分开叫

官方把 `ExtendVoteRequest` 的内容对应即将发 Precommit 的那份拟议块、没有有效签的扩展先丢掉整张 Precommit、ACCEPT 才把票和扩展留给下一高 Prepare 写成三件事。把它们叫成一个「看见填了 ExtendVote 请求对应就已经会调 ExtendVote」，会把已经会调、已经跳过 Verify 和已经 Verify 过迟到扩展一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求对应就已经会调 ExtendVote」，先数清问的是 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块不是已经会调 ExtendVote、Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify，还是 Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify 过迟到扩展，再决定要不要同一次发布。
