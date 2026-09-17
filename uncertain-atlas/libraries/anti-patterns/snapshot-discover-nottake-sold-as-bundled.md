# 反模式：把 挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量） 写成已经 已经收下 / 已经装完 / 已经交差

**层次**：实现 / 挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应**：[`../tracks/implementation/worked-example-snapshot-discover-nottake-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-discover-nottake-vs-bundled.md)。

把 挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量） 写成已经 已经收下 / 已经装完 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看挑了最高 正式三事（322 余量），必须分开 not already offered、not already restored、not already settled 三件事，不要和 322 / 38 / 324 / 956 / 958 糊成一句。

也不是：

- [snapshot-discover-notfull-sold-as-bundled](snapshot-discover-notfull-sold-as-bundled.md) 是问了仍未齐单句边界（956 item 1），不是本页挑了仍未收下边界。
- 只有 AppHash 可信任是不变量 38，不是本页最高仍未装完边界。
