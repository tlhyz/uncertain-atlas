# 模式：点名 snapshot-switch-notver 杠

**层次**：实现 / AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应**：[`../tracks/implementation/worked-example-snapshot-switch-notver-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-switch-notver-vs-bundled.md)。

- **AppHash 对上 不是已经版本也对上：** 看见 AppHash 对上，不是已经是版本也对上 interchangeable / 954 snapshot-switch-notver interchangeable。
- **看见对了下一高度 不是已经对了当前头：** 看见对了下一高度，不是已经对了当前头 interchangeable。
- **看见 Info 绿了 不是已经交差：** 看见 Info 绿了，不是已经是本头交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AppHash 对上 正式三事（323 余量），先数清问的是是不是已经版本也对上、是不是已经对了当前头、还是看见 Info 绿了是不是已经交差，再决定要不要同一次发布。323 snapshot-switch vs history bundled unbundling 在本页 item 2 续。
