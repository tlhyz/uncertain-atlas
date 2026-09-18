# 反模式：把 FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量） 写成已经 已经在块 H 生效 / 已经在 H+1 换人 / 已经只改这一项

**层次**：实现 / FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-fend-notheffect-vs-bundled.md`](../tracks/implementation/worked-example-fend-notheffect-vs-bundled.md)。

把 FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量） 写成已经 已经在块 H 生效 / 已经在 H+1 换人 / 已经只改这一项，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 consensus_param_updates 正式三事（432 余量），必须分开 not already h-effective、not already h1-rotate、not already one-field 三件事，不要和 432 / 319 / 35 / 1074 / 1075 糊成一句。

也不是：

- [finbar-notrotate-sold-as-bundled](finbar-notrotate-sold-as-bundled.md) 是 Finalize validator_updates 仍未在 H+1 换人边界（431/1072），不是本页 Finalize cparam 仍未在块 H 生效边界。
- 只改一个字段就只改这一项是不变量 319，不是本页能指 H+1 仍未在 H+1 换人边界。
