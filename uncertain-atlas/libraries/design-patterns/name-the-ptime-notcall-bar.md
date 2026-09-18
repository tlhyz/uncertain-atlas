# 模式：点名 ptime-notcall 杠

**层次**：实现 / prevote-or-nil look not already will-call / not already still-reject / not already settled 正式三事（416 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应**：[`../tracks/implementation/worked-example-ptime-notcall-vs-bundled.md`](../tracks/implementation/worked-example-ptime-notcall-vs-bundled.md)。

- **看 prevote 不是已经会调 Process：** 看见在看，不是已经会调 Process interchangeable / 1096 ptime-notcall interchangeable。
- **看见还没调 不是已经还能再 Reject：** 看见还没调，不是已经还能再 Reject interchangeable。
- **看见有算法 不是已经交差：** 看见有算法，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 prevote-or-nil 正式三事（416 余量），先数清问的是是不是已经会调 Process、是不是已经还能再 Reject、还是看见有算法是不是已经交差，再决定要不要同一次发布。416 proposetimeout vs process bundled unbundling 在本页 item 3 完成。
