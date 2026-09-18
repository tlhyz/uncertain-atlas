# 反模式：把 tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量） 写成已经 已经没进块 / 已经印进本头 / 已经交差

**层次**：实现 / tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-fhash-notout-vs-bundled.md`](../tracks/implementation/worked-example-fhash-notout-vs-bundled.md)。

把 tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量） 写成已经 已经没进块 / 已经印进本头 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code==0 正式三事（404 余量），必须分开 not already not-in-block、not already header-printed、not already settled 三件事，不要和 404 / 316 / 431 / 1100 / 1101 糊成一句。

也不是：

- [fhash-notalign-sold-as-bundled](fhash-notalign-sold-as-bundled.md) 是 Query 锚仍未对上 AppHash 单句边界（1101 item 2），不是本页 Code==0 仍未没进块边界。
- Code 非零就已经没进块是不变量 316，不是本页这笔合法仍未印进本头边界。
