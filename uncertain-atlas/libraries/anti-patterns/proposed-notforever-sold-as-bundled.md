# 反模式：把 CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量） 写成已经 已经进块 / 已经结算 / 已经永远有效

**层次**：共识 / CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应**：[`../tracks/mempool/worked-example-proposed-notforever-vs-bundled.md`](../tracks/mempool/worked-example-proposed-notforever-vs-bundled.md)。

把 CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量） 写成已经 已经进块 / 已经结算 / 已经永远有效，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 过了 正式三事（301 余量），必须分开 not already in-block、not already settled、not already forever-valid 三件事，不要和 301 / 328 / 339 / 144 / 992 / 993 糊成一句。

也不是：

- [proposed-notrecheck-sold-as-bundled](proposed-notrecheck-sold-as-bundled.md) 是 commit 后仍须再验单句边界（993 item 2），不是本页曾经绿过仍未永远有效边界。
- CheckTx 振荡就已经是永远绿是不变量 328，不是本页进了池仍未结算边界。
