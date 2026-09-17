# 模式：点名 snapshot-switch-nothist 杠

**层次**：实现 / 切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应**：[`../tracks/implementation/worked-example-snapshot-switch-nothist-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-switch-nothist-vs-bundled.md)。

- **切进共识 不是已经有完整历史：** 看见能出块，不是已经有从创世的完整历史 interchangeable / 955 snapshot-switch-nothist interchangeable。
- **看见能出块 不是已经能给任意旧高度：** 看见能出块，不是已经能给任意旧高度 interchangeable。
- **看见和其他节点一样跑 不是已经交差：** 看见和其他节点一样跑，不是已经不用管扩展高度 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看切进共识 正式三事（323 余量），先数清问的是是不是已经有完整历史、是不是已经能给任意旧高度、还是看见和其他节点一样跑是不是已经交差，再决定要不要同一次发布。323 snapshot-switch vs history bundled unbundling 在本页 item 3 完成。
