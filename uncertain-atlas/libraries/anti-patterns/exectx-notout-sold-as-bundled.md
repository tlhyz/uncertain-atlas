# 反模式：把 Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量） 写成已经 已经没进块 / 已经没进共识 / 已经和池门同一把尺

**层次**：实现 / Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应**：[`../tracks/implementation/worked-example-exectx-notout-vs-bundled.md`](../tracks/implementation/worked-example-exectx-notout-vs-bundled.md)。

把 Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量） 写成已经 已经没进块 / 已经没进共识 / 已经和池门同一把尺，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code 非零 正式三事（316 余量），必须分开 not already out-of-block、not already unindexed、not already checktx-scale 三件事，不要和 316 / 315 / 301 / 1013 / 1015 糊成一句。

也不是：

- [exectx-notorder-sold-as-bundled](exectx-notorder-sold-as-bundled.md) 是结果列表仍未同一顺序单句边界（1013 item 1），不是本页 Code 非零仍在块里边界。
- MaxGas 已经在执行是不变量 315，不是本页没索引仍未没进共识边界。
