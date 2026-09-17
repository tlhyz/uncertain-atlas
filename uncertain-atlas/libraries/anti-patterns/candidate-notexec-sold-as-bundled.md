# 反模式：把 立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量） 写成已经 已经是 ExecuteTxState / 已经能点名本高度最终 / 已经交差

**层次**：实现 / 立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应**：[`../tracks/implementation/worked-example-candidate-notexec-vs-bundled.md`](../tracks/implementation/worked-example-candidate-notexec-vs-bundled.md)。

把 立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量） 写成已经 已经是 ExecuteTxState / 已经能点名本高度最终 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻执行出候选 正式三事（311 余量），必须分开 not already ExecuteTxState、not already this-final、not already settled 三件事，不要和 311 / 310 / 342 / 971 / 973 糊成一句。

也不是：

- [candidate-nothash-sold-as-bundled](candidate-nothash-sold-as-bundled.md) 是 Prepare 仍不知道本头单句边界（971 item 1），不是本页立刻执行仍不是 ExecuteTxState 边界。
- 默认锁已经 RPC 安全是不变量 310，不是本页内存里有仍不能点名本高度最终边界。
