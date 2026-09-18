# 反模式：把 Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量） 写成已经 已经是四门已经结算 / 已经跑过 Process / 已经交差

**层次**：实现 / Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应**：[`../tracks/implementation/worked-example-ffields-notfour-vs-bundled.md`](../tracks/implementation/worked-example-ffields-notfour-vs-bundled.md)。

把 Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量） 写成已经 已经是四门已经结算 / 已经跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 刚决定字段 正式三事（407 余量），必须分开 not already four-gates、not already processed、not already settled 三件事，不要和 407 / 363 / 1099 / 1110 / 1111 糊成一句。

也不是：

- [sheight-notprove-sold-as-bundled](sheight-notprove-sold-as-bundled.md) 是 Query 可选证明仍未对上 AppHash 边界（406/1108），不是本页刚决定字段仍未是四门已经结算边界。
- Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算是不变量 363，不是本页有刚决定那块仍未跑过 Process 边界。
