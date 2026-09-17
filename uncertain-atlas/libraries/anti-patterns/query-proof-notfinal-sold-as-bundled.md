# 反模式：把 一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量） 写成已经 已经对上最终 AppHash / 已经交给下一层 / 已经交差

**层次**：实现 / 一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应**：[`../tracks/implementation/worked-example-query-proof-notfinal-vs-bundled.md`](../tracks/implementation/worked-example-query-proof-notfinal-vs-bundled.md)。

把 一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量） 写成已经 已经对上最终 AppHash / 已经交给下一层 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一层 ProofOp 的根 正式三事（325 余量），必须分开 not already final-apphash、not already next-value、not already settled 三件事，不要和 325 / 38 / 147 / 947 / 948 糊成一句。

也不是：

- [query-proof-notmatch-sold-as-bundled](query-proof-notmatch-sold-as-bundled.md) 是回了 Proof 仍未对上单句边界（948 item 2），不是本页一层根仍不是最终 AppHash 边界。
- 只有 AppHash 可信任是不变量 38，不是本页能证缺席仍未对着块哈希边界。
