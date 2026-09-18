# 模式：点名 fhash-notheader 杠

**层次**：实现 / Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-fhash-notheader-vs-bundled.md`](../tracks/implementation/worked-example-fhash-notheader-vs-bundled.md)。

- **app_hash 空或硬编码 不是已经印进本头：** 看见回了空根，不是已经印进本头 interchangeable / 1100 fhash-notheader interchangeable。
- **看见硬编码 不是已经是本头 AppHash：** 看见硬编码，不是已经是本头 AppHash interchangeable。
- **看见必须确定 不是已经交差：** 看见必须确定，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash 正式三事（404 余量），先数清问的是是不是已经印进本头、是不是已经是本头 AppHash、还是看见必须确定是不是已经交差，再决定要不要同一次发布。404 finapphash vs header bundled unbundling 在本页 item 1 启动。
