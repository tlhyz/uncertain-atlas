# 模式：点名 votets-notcheck 杠

**层次**：共识 / 带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应**：[`../tracks/consensus/worked-example-votets-notcheck-vs-bundled.md`](../tracks/consensus/worked-example-votets-notcheck-vs-bundled.md)。

- **带了 Timestamp 不是已经验过：** 看见字段在，不是已经验过 interchangeable / 998 votets-notcheck interchangeable。
- **看见单调 不是已经执行：** 看见单调，不是已经执行 interchangeable。
- **看见会用来算下一块 不是票上的时间已经有要求：** 看见会用来算下一块，不是收到时已经验过 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看带了 Timestamp 正式三事（304 余量），先数清问的是是不是已经验过、是不是已经执行、还是看见会用来算下一块是不是票上的时间已经有要求，再决定要不要同一次发布。304 vote-ts vs checked bundled unbundling 在本页 item 1 启动。
