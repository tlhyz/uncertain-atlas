# 模式：点名 checktxstate-notexec 杠

**层次**：实现 / CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应**：[`../tracks/implementation/worked-example-checktxstate-notexec-vs-bundled.md`](../tracks/implementation/worked-example-checktxstate-notexec-vs-bundled.md)。

- **CheckTx 过了 不是已经按 ExecuteTxState 验过：** 看见过了，不是已经按工作状态验 interchangeable / 968 checktxstate-notexec interchangeable。
- **看见进了池 不是已经按将要执行的那份验过：** 看见进了池，不是已经按将要执行的那份验 interchangeable。
- **看见重置了 不是已经交差：** 看见重置了，不是已经和 ExecuteTxState 同一份 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 过了 正式三事（312 余量），先数清问的是是不是已经按 ExecuteTxState 验过、是不是已经按将要执行的那份验过、还是看见重置了是不是已经交差，再决定要不要同一次发布。312 checktxstate vs execute bundled unbundling 在本页 item 1 启动。
