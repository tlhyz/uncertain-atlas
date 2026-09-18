# 模式：点名 ptime-notproc 杠

**层次**：实现 / proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应**：[`../tracks/implementation/worked-example-ptime-notproc-vs-bundled.md`](../tracks/implementation/worked-example-ptime-notproc-vs-bundled.md)。

- **先验块头 不是已经跑过 Process：** 看见验了头，不是已经跑过 Process interchangeable / 1095 ptime-notproc interchangeable。
- **看见提案带上头 不是已经知道本头哈希：** 看见提案带上头，不是已经知道本头哈希 interchangeable。
- **看见先验 不是已经交差：** 看见先验，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先验块头 正式三事（416 余量），先数清问的是是不是已经跑过 Process、是不是已经知道本头哈希、还是看见先验是不是已经交差，再决定要不要同一次发布。416 proposetimeout vs process bundled unbundling 在本页 item 2 续。
