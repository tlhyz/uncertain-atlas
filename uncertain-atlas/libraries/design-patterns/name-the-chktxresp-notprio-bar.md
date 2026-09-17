# 模式：点名 chktxresp-notprio 杠

**层次**：实现 / Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应**：[`../tracks/implementation/worked-example-chktxresp-notprio-vs-bundled.md`](../tracks/implementation/worked-example-chktxresp-notprio-vs-bundled.md)。

- **Priority 不是已经是共识顺序：** 看见有 Priority，不是已经是共识顺序 interchangeable / 1018 chktxresp-notprio interchangeable。
- **看见排在前面 不是已经进了块：** 看见排在前面，不是已经进了块 interchangeable。
- **看见能优先 不是已经从池里删掉：** 看见能优先，不是已经从池里删掉 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Priority 正式三事（317 余量），先数清问的是是不是已经是共识顺序、是不是已经进了块、还是看见能优先是不是已经从池里删掉，再决定要不要同一次发布。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。
