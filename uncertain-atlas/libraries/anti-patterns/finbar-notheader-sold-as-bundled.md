# 反模式：把 FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量） 写成已经 已经印进本头 / 已经交给引擎 / 已经必须确定

**层次**：实现 / FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-finbar-notheader-vs-bundled.md`](../tracks/implementation/worked-example-finbar-notheader-vs-bundled.md)。

把 FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量） 写成已经 已经印进本头 / 已经交给引擎 / 已经必须确定，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 events 正式三事（431 余量），必须分开 not already header-printed、not already engine-handed、not already must-det 三件事，不要和 431 / 357 / 316 / 1071 / 1072 糊成一句。

也不是：

- [presp-nothonest-sold-as-bundled](presp-nothonest-sold-as-bundled.md) 是 Process SHOULD Accept 仍未 honest must Accept 边界（430/1069），不是本页 Finalize events 仍未印进本头边界。
- Prepare 里产出了事件就已经交给引擎是不变量 357，不是本页能指索引仍未交给引擎边界。
