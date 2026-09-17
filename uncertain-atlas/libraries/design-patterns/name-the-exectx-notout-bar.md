# 模式：点名 exectx-notout 杠

**层次**：实现 / Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应**：[`../tracks/implementation/worked-example-exectx-notout-vs-bundled.md`](../tracks/implementation/worked-example-exectx-notout-vs-bundled.md)。

- **Code 非零 不是已经没进块：** 看见标成无效，不是已经没进块 interchangeable / 1014 exectx-notout interchangeable。
- **看见没索引 不是已经没进共识：** 看见没索引，不是已经没进共识 interchangeable。
- **看见类比 CheckTx 不是已经和池门同一把尺：** 看见类比 CheckTx，不是已经和池门同一把尺 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code 非零 正式三事（316 余量），先数清问的是是不是已经没进块、是不是已经没进共识、还是看见类比 CheckTx 是不是已经和池门同一把尺，再决定要不要同一次发布。316 exectxresult vs consensus bundled unbundling 在本页 item 2 续。
