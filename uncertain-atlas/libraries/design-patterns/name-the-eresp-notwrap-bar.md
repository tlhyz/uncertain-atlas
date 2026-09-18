# 模式：点名 eresp-notwrap 杠

**层次**：实现 / ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-eresp-notwrap-vs-bundled.md`](../tracks/implementation/worked-example-eresp-notwrap-vs-bundled.md)。

- **vote_extension 不是已经会包进 CanonicalVoteExtension：** 看见回了扩展，不是已经会包进 CanonicalVoteExtension interchangeable / 1082 eresp-notwrap interchangeable。
- **看见标成非确定 不是已经是同一份扩展：** 看见标成非确定，不是已经是同一份扩展 interchangeable。
- **看见可以 0 长 不是已经交差：** 看见可以 0 长，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 正式三事（418 余量），先数清问的是是不是已经会包进 CanonicalVoteExtension、是不是已经是同一份扩展、还是看见可以 0 长是不是已经交差，再决定要不要同一次发布。418 extresp vs wrap bundled unbundling 在本页 item 1 启动。
