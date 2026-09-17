# 模式：点名 extpre-notcall 杠

**层次**：实现 / ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-extpre-notcall-vs-bundled.md`](../tracks/implementation/worked-example-extpre-notcall-vs-bundled.md)。

- **对应即将发 Precommit 不是已经会调 ExtendVote：** 看见填了请求，不是已经会调 interchangeable / 1031 extpre-notcall interchangeable。
- **看见对上了拟议块 不是已经只在即将广播非 nil Precommit 时才叫：** 看见对上了拟议块，不是已经只在即将广播非 nil Precommit 时才叫 interchangeable。
- **看见有内容 不是已经交差：** 看见有内容，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看对应即将发 Precommit 正式三事（409 余量），先数清问的是是不是已经会调、是不是已经只在即将广播非 nil Precommit 时才叫、还是看见有内容是不是已经交差，再决定要不要同一次发布。409 extreq vs precommit bundled unbundling 在本页 item 1 启动。
