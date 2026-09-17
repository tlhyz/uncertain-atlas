# 模式：把 Verify When 正式流程三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**例**：[Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify ≠ 已经跳过 Verify](../../tracks/implementation/worked-example-verify-formal-when-vs-flow.md)。

## 三个名字

1. **Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify：** 看见丢掉了不是已经验过扩展。
2. **带有效签就会调 VerifyVoteExtension 不是已经验过扩展：** 看见 CometBFT 会叫不是已经 Accept。
3. **ACCEPT 会把票和扩展留给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo、REJECT 会把 Precommit 当非法丢掉 不是已经写进 last_commit：** 看见 REJECT 不是已经 Verify 过迟到扩展。

## 为什么要分开叫

官方把 Precommit 没有有效签先丢掉、带有效签才调 Verify、ACCEPT 留给下一高 Prepare / REJECT 丢掉整张 Precommit 写成三件事。把它们叫成一个「看见收到 Precommit 就已经验过扩展」，会把已经跳过 Verify、已经验过扩展和已经写进 last_commit 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收到 Precommit 就已经验过扩展」，先数清问的是 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 是不是已经跳过 Verify、带有效签就会调 VerifyVoteExtension 是不是已经验过扩展，还是 ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit 是不是已经写进 last_commit，再决定要不要同一次发布。
