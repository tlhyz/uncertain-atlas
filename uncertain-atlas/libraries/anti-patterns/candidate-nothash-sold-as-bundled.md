# 反模式：把 Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量） 写成已经 已经知道本头 / Prepare 当时已经有 / 已经交差

**层次**：实现 / Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应**：[`../tracks/implementation/worked-example-candidate-nothash-vs-bundled.md`](../tracks/implementation/worked-example-candidate-nothash-vs-bundled.md)。

把 Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量） 写成已经 已经知道本头 / Prepare 当时已经有 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有头哈希 正式三事（311 余量），必须分开 not already this-header、not already process-had-it、not already settled 三件事，不要和 311 / 33 / 312 / 972 / 973 糊成一句。

也不是：

- [checktxstate-notrecheck-sold-as-bundled](checktxstate-notrecheck-sold-as-bundled.md) 是 RECHECK 仍不是新交易边界（312/970），不是本页 Prepare 仍不知道本头边界。
- 四门已经结算是不变量 33，不是本页 Process 有哈希仍不是 Prepare 当时已有边界。
