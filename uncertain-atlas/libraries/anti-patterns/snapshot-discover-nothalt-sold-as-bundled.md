# 反模式：把 Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量） 写成已经 已经没有快照 / 已经停 / 已经交差

**层次**：实现 / Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应**：[`../tracks/implementation/worked-example-snapshot-discover-nothalt-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-discover-nothalt-vs-bundled.md)。

把 Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量） 写成已经 已经没有快照 / 已经停 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 被拒 正式三事（322 余量），必须分开 not already empty、not already halted、not already settled 三件事，不要和 322 / 314 / 321 / 956 / 957 糊成一句。

也不是：

- [snapshot-discover-nottake-sold-as-bundled](snapshot-discover-nottake-sold-as-bundled.md) 是挑了仍未收下单句边界（957 item 2），不是本页被拒仍未停边界。
- 启动对齐已经是快照重放是不变量 314，不是本页能中止仍未发现完边界。
