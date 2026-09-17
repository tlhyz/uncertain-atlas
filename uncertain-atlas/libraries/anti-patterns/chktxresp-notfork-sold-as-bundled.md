# 反模式：把 各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量） 写成已经 已经分叉 / 已经违规 / 已经和 ExecuteTxState 同一份

**层次**：实现 / 各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应**：[`../tracks/implementation/worked-example-chktxresp-notfork-vs-bundled.md`](../tracks/implementation/worked-example-chktxresp-notfork-vs-bundled.md)。

把 各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量） 写成已经 已经分叉 / 已经违规 / 已经和 ExecuteTxState 同一份，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看各节点 Data 不一样 正式三事（317 余量），必须分开 not already forked、not already illegal、not already same-state 三件事，不要和 317 / 312 / 328 / 1016 / 1018 糊成一句。

也不是：

- [chktxresp-notused-sold-as-bundled](chktxresp-notused-sold-as-bundled.md) 是 CheckTx Data 仍未被引擎用单句边界（1016 item 1），不是本页各节点不一样仍未分叉边界。
- CheckTxState 已经是 ExecuteTxState 是不变量 312，不是本页不确定仍未违规边界。
