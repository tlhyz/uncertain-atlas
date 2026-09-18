# 反模式：把 FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量） 写成已经 已经在 H+1 换人 / 已经改了集合 / 已经必须回四列

**层次**：实现 / FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-finbar-notrotate-vs-bundled.md`](../tracks/implementation/worked-example-finbar-notrotate-vs-bundled.md)。

把 FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量） 写成已经 已经在 H+1 换人 / 已经改了集合 / 已经必须回四列，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 正式三事（431 余量），必须分开 not already h1-rotate、not already set-changed、not already four-col 三件事，不要和 431 / 35 / 1070 / 1071 糊成一句。

也不是：

- [finbar-notchktx-sold-as-bundled](finbar-notchktx-sold-as-bundled.md) 是 tx_results 仍未是 CheckTx 回包单句边界（1071 item 2），不是本页 validator_updates 仍未在 H+1 换人边界。
- 高度 H 的 validator_updates 已经在 H+1 计票是不变量 35，不是本页有 ValidatorUpdate 仍未改了集合边界。
