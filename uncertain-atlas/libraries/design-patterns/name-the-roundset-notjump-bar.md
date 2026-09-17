# 模式：点名 roundset-notjump 杠

**层次**：共识 / 新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应**：[`../tracks/consensus/worked-example-roundset-notjump-vs-bundled.md`](../tracks/consensus/worked-example-roundset-notjump-vs-bundled.md)。

- **新加入 不是已经能跳到队头：** 看见加进来了，不是已经排到队头 interchangeable / 996 roundset-notjump interchangeable。
- **看见退出再加入 不是已经洗掉队尾：** 看见退出再加入，不是已经洗掉队尾 interchangeable。
- **看见初始优先级有数 不是已经公平当过一轮：** 看见初始优先级有数，不是已经公平当过一轮 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看新加入 正式三事（302 余量），先数清问的是是不是已经能跳到队头、是不是已经洗掉队尾、还是看见初始优先级有数是不是已经公平当过一轮，再决定要不要同一次发布。302 round vs set bundled unbundling 在本页 item 2 续。
