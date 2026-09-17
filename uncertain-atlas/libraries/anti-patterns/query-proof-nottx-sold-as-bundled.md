# 反模式：把 头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量） 写成已经 已经是交易默克尔 / 已经同一种锚 / 已经交差

**层次**：实现 / 头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应**：[`../tracks/implementation/worked-example-query-proof-nottx-vs-bundled.md`](../tracks/implementation/worked-example-query-proof-nottx-vs-bundled.md)。

把 头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量） 写成已经 已经是交易默克尔 / 已经同一种锚 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上有 AppHash 正式三事（325 余量），必须分开 not already tx-merkle、not already same-anchor、not already settled 三件事，不要和 325 / 147 / 329 / 948 / 949 糊成一句。

也不是：

- [peerfilter-notstore-sold-as-bundled](peerfilter-notstore-sold-as-bundled.md) 是 /store 仍不是引擎在用边界（326/946），不是本页头上有 AppHash 仍不是交易默克尔边界。
- 本头 AppHash 已经是本高度交差是不变量 147，不是本页三份哈希仍不是同一种锚边界。
