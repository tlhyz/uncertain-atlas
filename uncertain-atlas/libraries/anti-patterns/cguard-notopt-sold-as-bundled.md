# 反模式：把 CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量） 写成已经 已经是技术上可选 / 已经是四门已经结算 / 已经交差

**层次**：实现 / CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-cguard-notopt-vs-bundled.md`](../tracks/implementation/worked-example-cguard-notopt-vs-bundled.md)。

把 CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量） 写成已经 已经是技术上可选 / 已经是四门已经结算 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 守卫 正式三事（405 余量），必须分开 not already technically-optional、not already four-gates、not already settled 三件事，不要和 405 / 373 / 339 / 1104 / 1105 糊成一句。

也不是：

- [fhash-notout-sold-as-bundled](fhash-notout-sold-as-bundled.md) 是 Code==0 仍未没进块边界（404/1102），不是本页守卫仍未是技术上可选边界。
- CheckTx 技术上可选、不参与处理块就已经是四门已经结算是不变量 373，不是本页守着本地池仍未是四门已经结算边界。
