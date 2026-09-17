# 模式：点名 crashrec-notskip 杠

**层次**：实现 / 启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应**：[`../tracks/implementation/worked-example-crashrec-notskip-vs-bundled.md`](../tracks/implementation/worked-example-crashrec-notskip-vs-bundled.md)。

- **启动 Info 对上 不是已经是任意高度：** 看见 Info 绿了，不是已经能从半截高度接着走 interchangeable / 1021 crashrec-notskip interchangeable。
- **看见对上了 不是已经跳过重放：** 看见对上了，不是已经跳过重放 interchangeable。
- **看见 InitChain 叫过 不是已经不用再叫：** 看见 InitChain 叫过，不是已经不用再叫 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动 Info 对上 正式三事（320 余量），先数清问的是是不是已经是任意高度、是不是已经跳过重放、还是看见 InitChain 叫过是不是已经不用再叫，再决定要不要同一次发布。320 crash-steps vs commit bundled unbundling 在本页 item 3 完成。
