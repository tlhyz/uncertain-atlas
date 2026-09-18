# 反模式：把 Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量） 写成已经 已经印进本头 / 已经是本头 AppHash / 已经交差

**层次**：实现 / Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-fhash-notheader-vs-bundled.md`](../tracks/implementation/worked-example-fhash-notheader-vs-bundled.md)。

把 Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量） 写成已经 已经印进本头 / 已经是本头 AppHash / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash 正式三事（404 余量），必须分开 not already header-printed、not already this-header、not already settled 三件事，不要和 404 / 147 / 432 / 1101 / 1102 糊成一句。

也不是：

- [htmt-notdec-sold-as-bundled](htmt-notdec-sold-as-bundled.md) 是 Finalize h/t 对上仍未是刚决定那块的字段边界（417/1099），不是本页空或硬编码仍未印进本头边界。
- 本头 AppHash 就已经是本高度交差是不变量 147，不是本页硬编码仍未是本头 AppHash 边界。
