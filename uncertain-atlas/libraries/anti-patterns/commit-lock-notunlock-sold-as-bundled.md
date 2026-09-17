# 反模式：把 Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量） 写成已经 已经解锁 / 已经更新完 / 已经交差

**层次**：实现 / Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应**：[`../tracks/implementation/worked-example-commit-lock-notunlock-vs-bundled.md`](../tracks/implementation/worked-example-commit-lock-notunlock-vs-bundled.md)。

把 Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量） 写成已经 已经解锁 / 已经更新完 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 前上锁 正式三事（310 余量），必须分开 not already unlocked、not already updated、not already settled 三件事，不要和 310 / 5 / 312 / 974 / 976 糊成一句。

也不是：

- [commit-lock-notrpc-sold-as-bundled](commit-lock-notrpc-sold-as-bundled.md) 是有锁仍不能直接给 RPC 读单句边界（974 item 1），不是本页锁上了仍未解锁边界。
- 半写已经原子是不变量 5，不是本页能一起更新仍未更新完边界。
