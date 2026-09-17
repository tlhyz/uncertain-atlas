# 反模式：把 只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量） 写成已经 已经有了全部历史 / 已经五个字段都相同 / 已经交差

**层次**：实现 / 只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应**：[`../tracks/implementation/worked-example-snapshot-take-notall-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-take-notall-vs-bundled.md)。

把 只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量） 写成已经 已经有了全部历史 / 已经五个字段都相同 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只留最近两份 正式三事（324 余量），必须分开 not already all-history、not already five-fields、not already settled 三件事，不要和 324 / 322 / 334 / 950 / 951 糊成一句。

也不是：

- [snapshot-take-notcons-sold-as-bundled](snapshot-take-notcons-sold-as-bundled.md) 是没停链仍未隔离单句边界（951 item 2），不是本页只留两份仍不是全部历史边界。
- ListSnapshots 已经齐是不变量 322，不是本页 Hash 对上仍不是五字段相同边界。
