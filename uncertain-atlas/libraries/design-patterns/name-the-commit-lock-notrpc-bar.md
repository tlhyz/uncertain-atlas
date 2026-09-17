# 模式：点名 commit-lock-notrpc 杠

**层次**：实现 / 默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应**：[`../tracks/implementation/worked-example-commit-lock-notrpc-vs-bundled.md`](../tracks/implementation/worked-example-commit-lock-notrpc-vs-bundled.md)。

- **默认锁 不是已经能把状态直接给 RPC：** 看见有锁，不是已经能直接给 RPC 读 interchangeable / 974 commit-lock-notrpc interchangeable。
- **看见默认顺序收 不是已经没有并发假设：** 看见默认顺序收，不是已经没有并发假设 interchangeable。
- **看见编进同一个二进制 不是已经交差：** 看见编进同一个二进制，不是已经换了这把锁 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看默认锁 正式三事（310 余量），先数清问的是是不是已经 RPC 安全、是不是已经没有并发假设、还是看见编进同一个二进制是不是已经交差，再决定要不要同一次发布。310 commit-lock vs rpc bundled unbundling 在本页 item 1 启动。
