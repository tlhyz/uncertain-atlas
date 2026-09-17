# 反模式：把 ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量） 写成已经 已经有了全部快照 / 已经没有上限 / 已经交差

**层次**：实现 / ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应**：[`../tracks/implementation/worked-example-snapshot-discover-notfull-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-discover-notfull-vs-bundled.md)。

把 ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量） 写成已经 已经有了全部快照 / 已经没有上限 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 回了 正式三事（322 余量），必须分开 not already all-snapshots、not already unbounded、not already settled 三件事，不要和 322 / 321 / 323 / 957 / 958 糊成一句。

也不是：

- [snapshot-switch-nothist-sold-as-bundled](snapshot-switch-nothist-sold-as-bundled.md) 是切进仍没有完整历史边界（323/955），不是本页问了仍未齐边界。
- Offer 收下已经装完是不变量 321，不是本页回了仍有 10 份上限边界。
