# 模式：点名 fhash-notout 杠

**层次**：实现 / tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-fhash-notout-vs-bundled.md`](../tracks/implementation/worked-example-fhash-notout-vs-bundled.md)。

- **Code==0 不是已经没进块：** 看见回了 0，不是已经没进块 interchangeable / 1102 fhash-notout interchangeable。
- **看见这笔合法 不是已经印进本头：** 看见这笔合法，不是已经印进本头 interchangeable。
- **看见能回 不是已经交差：** 看见能回，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code==0 正式三事（404 余量），先数清问的是是不是已经没进块、是不是已经印进本头、还是看见能回是不是已经交差，再决定要不要同一次发布。404 finapphash vs header bundled unbundling 在本页 item 3 完成。
