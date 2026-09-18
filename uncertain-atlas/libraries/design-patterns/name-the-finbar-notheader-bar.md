# 模式：点名 finbar-notheader 杠

**层次**：实现 / FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-finbar-notheader-vs-bundled.md`](../tracks/implementation/worked-example-finbar-notheader-vs-bundled.md)。

- **events 不是已经印进本头：** 看见回了 events，不是已经印进本头 interchangeable / 1070 finbar-notheader interchangeable。
- **看见能指索引 不是已经交给引擎：** 看见能指索引，不是已经交给引擎 interchangeable。
- **看见标成非确定 不是已经必须确定：** 看见标成非确定，不是已经必须确定 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 events 正式三事（431 余量），先数清问的是是不是已经印进本头、是不是已经交给引擎、还是看见标成非确定是不是已经必须确定，再决定要不要同一次发布。431 finrespbar vs header bundled unbundling 在本页 item 1 启动。
