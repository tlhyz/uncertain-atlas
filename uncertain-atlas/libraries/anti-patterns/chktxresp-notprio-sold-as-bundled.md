# 反模式：把 Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量） 写成已经 已经是共识顺序 / 已经进了块 / 已经从池里删掉

**层次**：实现 / Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应**：[`../tracks/implementation/worked-example-chktxresp-notprio-vs-bundled.md`](../tracks/implementation/worked-example-chktxresp-notprio-vs-bundled.md)。

把 Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量） 写成已经 已经是共识顺序 / 已经进了块 / 已经从池里删掉，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Priority 正式三事（317 余量），必须分开 not already consensus-order、not already in-block、not already deleted 三件事，不要和 317 / 301 / 69 / 1016 / 1017 糊成一句。

也不是：

- [chktxresp-notfork-sold-as-bundled](chktxresp-notfork-sold-as-bundled.md) 是各节点不一样仍未分叉单句边界（1017 item 2），不是本页 Priority 仍未共识顺序边界。
- 提案收了已经从池里删掉是不变量 301/992，不是本页排在前面仍未进块边界。
