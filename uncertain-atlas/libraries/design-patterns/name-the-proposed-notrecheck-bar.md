# 模式：点名 proposed-notrecheck 杠

**层次**：共识 / 本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应**：[`../tracks/mempool/worked-example-proposed-notrecheck-vs-bundled.md`](../tracks/mempool/worked-example-proposed-notrecheck-vs-bundled.md)。

- **本块已 commit 不是已经不用再验剩下的：** 看见 commit 了，不是剩下的已经不用再验 interchangeable / 993 proposed-notrecheck interchangeable。
- **看见本块交易没了 不是池已经空了：** 看见本块交易从池里去掉，不是池已经空了 interchangeable。
- **看见再验开始了 不是剩下的已经永远有效：** 看见再验开始了，不是剩下的已经永远有效 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本块已 commit 正式三事（301 余量），先数清问的是是不是已经不用再验剩下的、是不是池已经空了、还是看见再验开始了是不是剩下的已经永远有效，再决定要不要同一次发布。301 proposed vs removed bundled unbundling 在本页 item 2 续。
