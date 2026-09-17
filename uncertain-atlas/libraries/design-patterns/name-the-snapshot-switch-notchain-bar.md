# 模式：点名 snapshot-switch-notchain 杠

**层次**：实现 / 装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应**：[`../tracks/implementation/worked-example-snapshot-switch-notchain-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-switch-notchain-vs-bundled.md)。

- **装完 不是已经有了 ChainID：** 看见装完，不是已经有了这些 interchangeable / 953 snapshot-switch-notchain interchangeable。
- **看见状态机在 不是已经能出块：** 看见状态机在，不是已经能出块 interchangeable。
- **看见有创世文件 不是已经交差：** 看见有创世文件，不是已经和轻客户端对过 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完 正式三事（323 余量），先数清问的是是不是已经有了 ChainID、是不是已经能出块、还是看见有创世文件是不是已经交差，再决定要不要同一次发布。323 snapshot-switch vs history bundled unbundling 在本页 item 1 启动。
