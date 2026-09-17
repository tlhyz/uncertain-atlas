# 反模式：把 Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量） 写成已经 已经装完 / 已经有了全部块 / 已经交差

**层次**：实现 / Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应**：[`../tracks/implementation/worked-example-snapshot-restore-notdone-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-restore-notdone-vs-bundled.md)。

把 Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量） 写成已经 已经装完 / 已经有了全部块 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下 正式三事（321 余量），必须分开 not already restored、not already has-chunks、not already settled 三件事，不要和 321 / 38 / 322 / 960 / 961 糊成一句。

也不是：

- [snapshot-discover-nothalt-sold-as-bundled](snapshot-discover-nothalt-sold-as-bundled.md) 是 Offer 被拒仍未停边界（322/958），不是本页 Offer 收下仍未装完边界。
- 只有 AppHash 可信任是不变量 38，不是本页选了这份仍没有块边界。
