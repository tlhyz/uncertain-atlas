# 模式：点名 roundset-notset 杠

**层次**：共识 / 同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应**：[`../tracks/consensus/worked-example-roundset-notset-vs-bundled.md`](../tracks/consensus/worked-example-roundset-notset-vs-bundled.md)。

- **同一高度换轮 不是已经换成应用刚回的那套：** 看见换轮了，不是这高度已经换了名单 interchangeable / 995 roundset-notset interchangeable。
- **看见应用回了更新 不是本高度各轮已经用上：** 看见应用回了更新，不是本高度各轮已经用上 interchangeable。
- **看见下一轮换了人 不是集合已经变了：** 看见下一轮换了人，不是集合已经变了 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度换轮 正式三事（302 余量），先数清问的是是不是已经换成应用刚回的那套、是不是本高度各轮已经用上、还是看见下一轮换了人是不是集合已经变了，再决定要不要同一次发布。302 round vs set bundled unbundling 在本页 item 1 启动。
