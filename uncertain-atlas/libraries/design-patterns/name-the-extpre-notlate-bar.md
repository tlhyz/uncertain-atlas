# 模式：点名 extpre-notlate 杠

**层次**：实现 / Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-extpre-notlate-vs-bundled.md`](../tracks/implementation/worked-example-extpre-notlate-vs-bundled.md)。

- **ACCEPT 留给 h+1 不是已经 Verify 过迟到扩展：** 看见收下了，不是已经 Verify 过迟到扩展 interchangeable / 1033 extpre-notlate interchangeable。
- **看见留给下一高 不是已经交差：** 看见留给下一高，不是已经交差 interchangeable。
- **看见能填 不是已经必须再 Verify：** 看见能填，不是已经必须再 Verify interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT 留给 h+1 正式三事（409 余量），先数清问的是是不是已经 Verify 过迟到扩展、是不是已经交差、还是看见能填是不是已经必须再 Verify，再决定要不要同一次发布。409 extreq vs precommit bundled unbundling 在本页 item 3 完成。
