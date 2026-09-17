# 模式：点名 exectx-notorder 杠

**层次**：实现 / 结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应**：[`../tracks/implementation/worked-example-exectx-notorder-vs-bundled.md`](../tracks/implementation/worked-example-exectx-notorder-vs-bundled.md)。

- **结果列表 不是已经同一顺序：** 看见回了列表，不是已经对上 interchangeable / 1013 exectx-notorder interchangeable。
- **看见条数一样 不是已经按送来的顺序：** 看见条数一样，不是已经按送来的顺序 interchangeable。
- **看见 Finalize 回了 不是引擎已经替你排好：** 看见 Finalize 回了，不是引擎已经替你排好 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看结果列表 正式三事（316 余量），先数清问的是是不是已经同一顺序、是不是已经按送来的顺序、还是看见 Finalize 回了是不是引擎已经替你排好，再决定要不要同一次发布。316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动。
