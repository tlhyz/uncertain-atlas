# 模式：点名 ffields-notprep 杠

**层次**：实现 / Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应**：[`../tracks/implementation/worked-example-ffields-notprep-vs-bundled.md`](../tracks/implementation/worked-example-ffields-notprep-vs-bundled.md)。

- **Finalize 必须确定 不是已经可以像 Prepare 那样：** 看见必须确定，不是已经可以像 Prepare 那样 interchangeable / 1110 ffields-notprep interchangeable。
- **看见在复制里推进 不是已经印进本头：** 看见在复制里推进，不是已经印进本头 interchangeable。
- **看见能推进 不是已经交差：** 看见能推进，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 必须确定 正式三事（407 余量），先数清问的是是不是已经可以像 Prepare 那样、是不是已经印进本头、还是看见能推进是不是已经交差，再决定要不要同一次发布。407 finfields vs equiv bundled unbundling 在本页 item 2 续。
