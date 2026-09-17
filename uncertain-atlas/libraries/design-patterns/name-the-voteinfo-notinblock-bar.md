# 模式：点名 按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 余量）

**层次**：实现 / VoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-voteinfo-notinblock-vs-bundled.md](../../tracks/implementation/worked-example-voteinfo-notinblock-vs-bundled.md)。

按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **排好了 不是已经进了块：** 看见顺序在，不是已经 300 interchangeable / 832 voteinfo-notinblock interchangeable。
- **看见从 store 再装 不是已经交差：** 看见顺序在，不是已经交差 interchangeable。
- **看见排好了 不是已经罚没：** 看见顺序在，不是已经罚没 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按投票权降序排 正式三事（365 余量），先数清问的是是不是已经进了块 / 300、是不是已经交差、还是看见排好了是不是已经罚没，再决定要不要同一次发布。365 voteinfo vs reward bundled unbundling 在本页 item 3 完成。
