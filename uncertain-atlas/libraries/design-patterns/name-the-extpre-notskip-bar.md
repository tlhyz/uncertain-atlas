# 模式：点名 extpre-notskip 杠

**层次**：实现 / Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-extpre-notskip-vs-bundled.md`](../tracks/implementation/worked-example-extpre-notskip-vs-bundled.md)。

- **丢掉无有效签扩展 不是已经跳过 Verify：** 看见丢掉了，不是已经跳过 Verify interchangeable / 1032 extpre-notskip interchangeable。
- **看见空扩展 不是已经没有签：** 看见空扩展，不是已经没有签 interchangeable。
- **看见没调 Verify 不是已经自己验过：** 看见没调 Verify，不是已经自己验过 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉无有效签扩展 正式三事（409 余量），先数清问的是是不是已经跳过 Verify、是不是已经没有签、还是看见没调 Verify 是不是已经自己验过，再决定要不要同一次发布。409 extreq vs precommit bundled unbundling 在本页 item 2 续。
