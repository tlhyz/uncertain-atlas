# 反模式：把 Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量） 写成已经 已经对上 AppHash / 已经是同一棵树 / 已经交差

**层次**：实现 / Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应**：[`../tracks/implementation/worked-example-query-proof-notmatch-vs-bundled.md`](../tracks/implementation/worked-example-query-proof-notmatch-vs-bundled.md)。

把 Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量） 写成已经 已经对上 AppHash / 已经是同一棵树 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 Proof 正式三事（325 余量），必须分开 not already matched、not already one-tree、not already settled 三件事，不要和 325 / 314 / 38 / 947 / 949 糊成一句。

也不是：

- [query-proof-nottx-sold-as-bundled](query-proof-nottx-sold-as-bundled.md) 是头上有 AppHash 仍不是交易默克尔单句边界（947 item 1），不是本页回了 Proof 仍未对上边界。
- QueryState 已经是 ExecuteTxState 是不变量 314，不是本页有 type 仍不是同一棵树边界。
