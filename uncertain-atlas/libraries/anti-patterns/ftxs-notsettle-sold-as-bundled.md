# 反模式：把 Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量） 写成已经 已经交差 / 已经可以像 Prepare 那样 / 已经只依赖上一份状态和决定块

**层次**：实现 / Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-ftxs-notsettle-vs-bundled.md`](../tracks/implementation/worked-example-ftxs-notsettle-vs-bundled.md)。

把 Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量） 写成已经 已经交差 / 已经可以像 Prepare 那样 / 已经只依赖上一份状态和决定块，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 执行再交还 正式三事（408 余量），必须分开 not already settled、not already like-Prepare、not already last-state-only 三件事，不要和 408 / 1110 / 342 / 1113 / 1114 糊成一句。

也不是：

- [ffields-notinfo-sold-as-bundled](ffields-notinfo-sold-as-bundled.md) 是 Info 回应用状态仍未是握手对齐边界（407/1111），不是本页执行再交还仍未交差边界。
- Finalize 实现必须确定因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样是不变量 1110，不是本页必须确定仍未可以像 Prepare 那样边界。
