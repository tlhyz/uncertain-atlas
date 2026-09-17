# 反模式：把 启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量） 写成已经 已经是任意高度 / 已经跳过重放 / 已经不用再叫

**层次**：实现 / 启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应**：[`../tracks/implementation/worked-example-crashrec-notskip-vs-bundled.md`](../tracks/implementation/worked-example-crashrec-notskip-vs-bundled.md)。

把 启动 Info 对上 not already any-height / not already skip-replay / not already no-reinit 正式三事（320 余量） 写成已经 已经是任意高度 / 已经跳过重放 / 已经不用再叫，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动 Info 对上 正式三事（320 余量），必须分开 not already any-height、not already skip-replay、not already no-reinit 三件事，不要和 320 / 314 / 310 / 1019 / 1020 糊成一句。

也不是：

- [crashrec-notcommit-sold-as-bundled](crashrec-notcommit-sold-as-bundled.md) 是块进 store 仍未 Commit 单句边界（1020 item 2），不是本页启动 Info 对上仍未能跳步边界。
- 启动对齐已经是快照重放是不变量 314，不是本页对上了仍未跳过重放边界。
