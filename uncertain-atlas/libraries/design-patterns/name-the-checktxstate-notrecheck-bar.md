# 模式：点名 checktxstate-notrecheck 杠

**层次**：实现 / RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应**：[`../tracks/implementation/worked-example-checktxstate-notrecheck-vs-bundled.md`](../tracks/implementation/worked-example-checktxstate-notrecheck-vs-bundled.md)。

- **RECHECK 不是已经是新交易：** 看见又跑了，不是已经是新交易 interchangeable / 970 checktxstate-notrecheck interchangeable。
- **看见 Type 在 不是已经当 NEW 处理：** 看见 Type 在，不是已经当 NEW 处理 interchangeable。
- **看见 Commit 回了 不是已经交差：** 看见 Commit 回了，不是锁已经放下 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 RECHECK 正式三事（312 余量），先数清问的是是不是已经是新交易、是不是已经当 NEW 处理、还是看见 Commit 回了是不是已经交差，再决定要不要同一次发布。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。
