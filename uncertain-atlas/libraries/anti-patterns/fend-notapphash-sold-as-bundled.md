# 反模式：把 FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量） 写成已经 已经写进下一块头 / 已经是本头 AppHash / 已经只是索引

**层次**：实现 / FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-fend-notapphash-vs-bundled.md`](../tracks/implementation/worked-example-fend-notapphash-vs-bundled.md)。

把 FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量） 写成已经 已经写进下一块头 / 已经是本头 AppHash / 已经只是索引，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash 正式三事（432 余量），必须分开 not already next-header、not already this-header、not already index-only 三件事，不要和 432 / 404 / 431 / 1073 / 1075 糊成一句。

也不是：

- [fend-notheffect-sold-as-bundled](fend-notheffect-sold-as-bundled.md) 是 cparam 仍未在块 H 生效单句边界（1073 item 1），不是本页 app_hash 仍未写进下一块头边界。
- Finalize 回包 app_hash 可以空或硬编码就已经印进本头是不变量 404，不是本页有默克尔根仍未是本头 AppHash 边界。
