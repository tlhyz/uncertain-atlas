# 模式：点名 ffields-notfour 杠

**层次**：实现 / Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应**：[`../tracks/implementation/worked-example-ffields-notfour-vs-bundled.md`](../tracks/implementation/worked-example-ffields-notfour-vs-bundled.md)。

- **Finalize 刚决定字段 不是已经是四门已经结算：** 看见填了字段，不是已经是四门已经结算 interchangeable / 1109 ffields-notfour interchangeable。
- **看见有刚决定那块 不是已经跑过 Process：** 看见有刚决定那块，不是已经跑过 Process interchangeable。
- **看见能填 不是已经交差：** 看见能填，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 刚决定字段 正式三事（407 余量），先数清问的是是不是已经是四门已经结算、是不是已经跑过 Process、还是看见能填是不是已经交差，再决定要不要同一次发布。407 finfields vs equiv bundled unbundling 在本页 item 1 启动。
