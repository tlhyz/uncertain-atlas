# 模式：点名 fend-notapphash 杠

**层次**：实现 / FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-fend-notapphash-vs-bundled.md`](../tracks/implementation/worked-example-fend-notapphash-vs-bundled.md)。

- **app_hash 不是已经写进下一块头：** 看见回了 app_hash，不是已经写进下一块头 interchangeable / 1074 fend-notapphash interchangeable。
- **看见有默克尔根 不是已经是本头 AppHash：** 看见有默克尔根，不是已经是本头 AppHash interchangeable。
- **看见必须确定 不是已经只是索引：** 看见必须确定，不是已经只是索引 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash 正式三事（432 余量），先数清问的是是不是已经写进下一块头、是不是已经是本头 AppHash、还是看见必须确定是不是已经只是索引，再决定要不要同一次发布。432 finrespend vs params bundled unbundling 在本页 item 2 续。
