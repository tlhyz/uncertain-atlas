# 模式：点名 两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事（338 余量）

**层次**：实现 / PrepareProposal 与 ExtendVote 的确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-nondet-notraw-vs-bundled.md](../../tracks/implementation/worked-example-prepare-nondet-notraw-vs-bundled.md)。

两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事（338 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **raw 一样 不是已经是同一份提案：** 看见 raw 一样，不是已经是同一份提案 interchangeable / 897 prepare-nondet-notraw interchangeable。
- **看见同一高度、同一轮 不是已经必须同一份：** 看见同一高度、同一轮，不是已经必须同一份 interchangeable。
- **看见诚实准备 不是已经交差：** 看见诚实准备，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边 raw 一样 正式三事（338 余量），先数清问的是是不是已经是同一份提案、是不是已经必须同一份、还是看见诚实准备是不是已经交差，再决定要不要同一次发布。338 prepare-nondet vs process bundled unbundling 在本页 item 2 续。
