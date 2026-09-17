# 反模式：把 本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量） 写成已经 已经不用再验剩下的 / 池已经空了 / 剩下的已经永远有效

**层次**：共识 / 本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应**：[`../tracks/mempool/worked-example-proposed-notrecheck-vs-bundled.md`](../tracks/mempool/worked-example-proposed-notrecheck-vs-bundled.md)。

把 本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量） 写成已经 已经不用再验剩下的 / 池已经空了 / 剩下的已经永远有效，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本块已 commit 正式三事（301 余量），必须分开 not already skip-recheck、not already empty、not already forever 三件事，不要和 301 / 69 / 312 / 992 / 994 糊成一句。

也不是：

- [proposed-notdel-sold-as-bundled](proposed-notdel-sold-as-bundled.md) 是提案收了仍未从池里删掉单句边界（992 item 1），不是本页 commit 后仍须再验边界。
- 单笔 CheckTx 绿已经整包可提案是不变量 69，不是本页本块交易没了仍未池空边界。
