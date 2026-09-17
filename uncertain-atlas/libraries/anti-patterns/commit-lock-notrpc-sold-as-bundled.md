# 反模式：把 默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量） 写成已经 已经 RPC 安全 / 已经没有并发假设 / 已经交差

**层次**：实现 / 默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应**：[`../tracks/implementation/worked-example-commit-lock-notrpc-vs-bundled.md`](../tracks/implementation/worked-example-commit-lock-notrpc-vs-bundled.md)。

把 默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量） 写成已经 已经 RPC 安全 / 已经没有并发假设 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看默认锁 正式三事（310 余量），必须分开 not already RPC-safe、not already no-concurrency、not already settled 三件事，不要和 310 / 307 / 311 / 975 / 976 糊成一句。

也不是：

- [candidate-notdrop-sold-as-bundled](candidate-notdrop-sold-as-bundled.md) 是丢掉仍可能再执行边界（311/973），不是本页有锁仍不能直接给 RPC 读边界。
- 一条连接已经是四门是不变量 307，不是本页默认顺序收仍有并发假设边界。
