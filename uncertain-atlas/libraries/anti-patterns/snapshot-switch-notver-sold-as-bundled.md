# 反模式：把 AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量） 写成已经 已经版本也对上 / 已经对了当前头 / 已经交差

**层次**：实现 / AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应**：[`../tracks/implementation/worked-example-snapshot-switch-notver-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-switch-notver-vs-bundled.md)。

把 AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量） 写成已经 已经版本也对上 / 已经对了当前头 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AppHash 对上 正式三事（323 余量），必须分开 not already version-matched、not already this-header、not already settled 三件事，不要和 323 / 147 / 324 / 953 / 955 糊成一句。

也不是：

- [snapshot-switch-notchain-sold-as-bundled](snapshot-switch-notchain-sold-as-bundled.md) 是装完仍没有 ChainID 单句边界（953 item 1），不是本页 AppHash 对上仍不是版本也对上边界。
- 本头 AppHash 已经是本高度交差是不变量 147，不是本页对了下一高度仍不是当前头边界。
