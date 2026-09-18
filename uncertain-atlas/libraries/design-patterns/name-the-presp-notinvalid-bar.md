# 模式：点名 presp-notinvalid 杠

**层次**：实现 / ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-presp-notinvalid-vs-bundled.md`](../tracks/implementation/worked-example-presp-notinvalid-vs-bundled.md)。

- **status 不是已经当成块非法：** 看见回了 REJECT，不是已经当成块非法 interchangeable / 1067 presp-notinvalid interchangeable。
- **看见共识假设不合法 不是已经不能整块执行候选：** 看见共识假设不合法，不是已经不能整块执行候选 interchangeable。
- **看见会 prevote nil 不是已经当成块非法：** 看见会 prevote nil，不是已经当成块非法 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 status 正式三事（430 余量），先数清问的是是不是已经当成块非法、是不是已经不能整块执行候选、还是看见会 prevote nil 是不是已经当成块非法，再决定要不要同一次发布。430 procresp vs status bundled unbundling 在本页 item 1 启动。
