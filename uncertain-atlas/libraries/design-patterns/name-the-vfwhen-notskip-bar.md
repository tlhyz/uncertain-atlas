# 模式：点名 vfwhen-notskip 杠

**层次**：实现 / Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-vfwhen-notskip-vs-bundled.md`](../tracks/implementation/worked-example-vfwhen-notskip-vs-bundled.md)。

- **unsigned discard 不是已经跳过 Verify：** 看见丢掉了，不是已经跳过 Verify interchangeable / 1085 vfwhen-notskip interchangeable。
- **看见没调 Verify 不是已经验过扩展：** 看见没调 Verify，不是已经验过扩展 interchangeable。
- **看见没签 不是已经 Accept：** 看见没签，不是已经 Accept interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 unsigned discard 正式三事（435 余量），先数清问的是是不是已经跳过 Verify、是不是已经验过扩展、还是看见没签是不是已经 Accept，再决定要不要同一次发布。435 verify-formal-when vs flow bundled unbundling 在本页 item 1 启动。
