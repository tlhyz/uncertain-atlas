# 反模式：把 Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量） 写成已经 已经能往下走 / 已经允许 / 已经交差

**层次**：实现 / Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应**：[`../tracks/implementation/worked-example-commit-lock-notbcast-vs-bundled.md`](../tracks/implementation/worked-example-commit-lock-notbcast-vs-bundled.md)。

把 Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量） 写成已经 已经能往下走 / 已经允许 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 里等广播 正式三事（310 余量），必须分开 not already proceeding、not already allowed、not already settled 三件事，不要和 310 / 301 / 33 / 974 / 975 糊成一句。

也不是：

- [commit-lock-notunlock-sold-as-bundled](commit-lock-notunlock-sold-as-bundled.md) 是锁上了仍未解锁单句边界（975 item 2），不是本页等广播仍不能往下走边界。
- 提案收了已经从池里删掉是不变量 301，不是本页同步内存池调用仍未交差边界。
