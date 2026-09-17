# 反模式：把 Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量） 写成已经 已经印进本头 / 已经进了那份哈希 / 已经是共识

**层次**：实现 / Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应**：[`../tracks/implementation/worked-example-exectx-notheader-vs-bundled.md`](../tracks/implementation/worked-example-exectx-notheader-vs-bundled.md)。

把 Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量） 写成已经 已经印进本头 / 已经进了那份哈希 / 已经是共识，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code / Data 正式三事（316 余量），必须分开 not already this-header、not already in-hash、not already consensus 三件事，不要和 316 / 147 / 317 / 1013 / 1014 糊成一句。

也不是：

- [exectx-notout-sold-as-bundled](exectx-notout-sold-as-bundled.md) 是 Code 非零仍在块里单句边界（1014 item 2），不是本页 Code/Data 仍未印进本头边界。
- 本头 AppHash 已经是本高度交差是不变量 147，不是本页 Events 仍未进那份哈希边界。
