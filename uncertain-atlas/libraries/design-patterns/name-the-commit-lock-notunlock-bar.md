# 模式：点名 commit-lock-notunlock 杠

**层次**：实现 / Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应**：[`../tracks/implementation/worked-example-commit-lock-notunlock-vs-bundled.md`](../tracks/implementation/worked-example-commit-lock-notunlock-vs-bundled.md)。

- **Commit 前上锁 不是已经解锁：** 看见锁上了，不是已经解锁 interchangeable / 975 commit-lock-notunlock interchangeable。
- **看见能一起更新 不是已经更新完：** 看见能一起更新，不是已经更新完 interchangeable。
- **看见 Commit 回了 不是已经交差：** 看见 Commit 回了，不是内存池锁已经按同一条路径放下 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 前上锁 正式三事（310 余量），先数清问的是是不是已经解锁、是不是已经更新完、还是看见 Commit 回了是不是已经交差，再决定要不要同一次发布。310 commit-lock vs rpc bundled unbundling 在本页 item 2 续。
