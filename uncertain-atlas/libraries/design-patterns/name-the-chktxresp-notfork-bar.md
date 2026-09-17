# 模式：点名 chktxresp-notfork 杠

**层次**：实现 / 各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应**：[`../tracks/implementation/worked-example-chktxresp-notfork-vs-bundled.md`](../tracks/implementation/worked-example-chktxresp-notfork-vs-bundled.md)。

- **各节点 Data 不一样 不是已经分叉：** 看见各节点 Data 不一样，不是已经分叉 interchangeable / 1017 chktxresp-notfork interchangeable。
- **看见不确定 不是已经违规：** 看见不确定，不是已经违规 interchangeable。
- **看见 CheckTxState 不同 不是已经和 ExecuteTxState 同一份：** 看见 CheckTxState 不同，不是已经和 ExecuteTxState 同一份 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看各节点 Data 不一样 正式三事（317 余量），先数清问的是是不是已经分叉、是不是已经违规、还是看见 CheckTxState 不同是不是已经和 ExecuteTxState 同一份，再决定要不要同一次发布。317 checktxresponse vs exec bundled unbundling 在本页 item 2 续。
