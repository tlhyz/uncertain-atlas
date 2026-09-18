# 模式：点名 vreqh-notprop 杠

**层次**：实现 / VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-vreqh-notprop-vs-bundled.md`](../tracks/implementation/worked-example-vreqh-notprop-vs-bundled.md)。

- **height 不是已经是拟议块高度：** 看见填了 height，不是已经是拟议块高度 interchangeable / 1088 vreqh-notprop interchangeable。
- **看见能对一下 不是已经对上了：** 看见能对一下，不是已经对上了拟议块 interchangeable。
- **看见有高度 不是已经会调 Verify：** 看见有高度，不是已经会调 Verify interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 正式三事（415 余量），先数清问的是是不是已经是拟议块高度、是不是已经对上了、还是看见有高度是不是已经会调 Verify，再决定要不要同一次发布。415 verifyheight vs extheight bundled unbundling 在本页 item 1 启动。
