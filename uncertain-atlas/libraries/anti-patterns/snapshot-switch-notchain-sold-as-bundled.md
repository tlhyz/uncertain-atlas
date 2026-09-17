# 反模式：把 装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量） 写成已经 已经有了 ChainID / 已经能出块 / 已经交差

**层次**：实现 / 装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应**：[`../tracks/implementation/worked-example-snapshot-switch-notchain-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-switch-notchain-vs-bundled.md)。

把 装完 not already chainid / not already block-ready / not already settled 正式三事（323 余量） 写成已经 已经有了 ChainID / 已经能出块 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完 正式三事（323 余量），必须分开 not already chainid、not already block-ready、not already settled 三件事，不要和 323 / 38 / 321 / 954 / 955 糊成一句。

也不是：

- [snapshot-take-notall-sold-as-bundled](snapshot-take-notall-sold-as-bundled.md) 是只留两份仍不是全部历史边界（324/952），不是本页装完仍没有 ChainID 边界。
- 只有 AppHash 可信任是不变量 38，不是本页状态机在仍不能出块边界。
