# 反模式：把 切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量） 写成已经 已经有完整历史 / 已经能给任意旧高度 / 已经交差

**层次**：实现 / 切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应**：[`../tracks/implementation/worked-example-snapshot-switch-nothist-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-switch-nothist-vs-bundled.md)。

把 切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量） 写成已经 已经有完整历史 / 已经能给任意旧高度 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看切进共识 正式三事（323 余量），必须分开 not already full-history、not already any-old、not already settled 三件事，不要和 323 / 322 / 321 / 953 / 954 糊成一句。

也不是：

- [snapshot-switch-notver-sold-as-bundled](snapshot-switch-notver-sold-as-bundled.md) 是 AppHash 对上仍不是版本也对上单句边界（954 item 2），不是本页切进仍没有完整历史边界。
- ListSnapshots 已经齐是不变量 322，不是本页能出块仍不能给任意旧高度边界。
