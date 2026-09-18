# 反模式：把 Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量） 写成已经 已经可以像 Prepare 那样 / 已经印进本头 / 已经交差

**层次**：实现 / Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应**：[`../tracks/implementation/worked-example-ffields-notprep-vs-bundled.md`](../tracks/implementation/worked-example-ffields-notprep-vs-bundled.md)。

把 Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量） 写成已经 已经可以像 Prepare 那样 / 已经印进本头 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 必须确定 正式三事（407 余量），必须分开 not already like-Prepare、not already header-printed、not already settled 三件事，不要和 407 / 342 / 338 / 1109 / 1111 糊成一句。

也不是：

- [ffields-notfour-sold-as-bundled](ffields-notfour-sold-as-bundled.md) 是刚决定字段仍未是四门已经结算单句边界（1109 item 1），不是本页必须确定仍未可以像 Prepare 那样边界。
- Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样是不变量 342，不是本页在复制里推进仍未印进本头边界。
