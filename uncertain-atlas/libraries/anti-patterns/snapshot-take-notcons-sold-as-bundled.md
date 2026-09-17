# 反模式：把 没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量） 写成已经 已经隔离 / 已经各节点相同 / 已经交差

**层次**：实现 / 没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应**：[`../tracks/implementation/worked-example-snapshot-take-notcons-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-take-notcons-vs-bundled.md)。

把 没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量） 写成已经 已经隔离 / 已经各节点相同 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没停链 正式三事（324 余量），必须分开 not already consistent、not already same-bytes、not already settled 三件事，不要和 324 / 323 / 322 / 950 / 952 糊成一句。

也不是：

- [snapshot-take-notafter-sold-as-bundled](snapshot-take-notafter-sold-as-bundled.md) 是拍了仍未交差之后拍单句边界（950 item 1），不是本页没停链仍未隔离边界。
- 切进共识已经有完整历史是不变量 323，不是本页后台拍仍未各节点相同边界。
