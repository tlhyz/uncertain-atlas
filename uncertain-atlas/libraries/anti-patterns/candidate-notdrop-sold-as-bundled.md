# 反模式：把 丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量） 写成已经 已经永远不用再执行 / 已经能一直攒 / 已经交差

**层次**：实现 / 丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应**：[`../tracks/implementation/worked-example-candidate-notdrop-vs-bundled.md`](../tracks/implementation/worked-example-candidate-notdrop-vs-bundled.md)。

把 丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量） 写成已经 已经永远不用再执行 / 已经能一直攒 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉候选 正式三事（311 余量），必须分开 not already never-rerun、not already unbounded-ok、not already settled 三件事，不要和 311 / 5 / 338 / 971 / 972 糊成一句。

也不是：

- [candidate-notexec-sold-as-bundled](candidate-notexec-sold-as-bundled.md) 是立刻执行仍不是 ExecuteTxState 单句边界（972 item 2），不是本页丢掉仍可能再执行边界。
- 半写已经原子是不变量 5，不是本页有上界仍不是规范写死条数边界。
