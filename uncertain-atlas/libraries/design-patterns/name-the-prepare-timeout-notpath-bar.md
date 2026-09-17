# 模式：点名 立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事（327 余量）

**层次**：实现 / PrepareProposal 及时性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-timeout-notpath-vs-bundled.md](../../tracks/implementation/worked-example-prepare-timeout-notpath-vs-bundled.md)。

立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事（327 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **立刻整块执行 不是已经离开关键路径：** 看见立刻执行了，不是已经离开这条路径 interchangeable / 899 prepare-timeout-notpath interchangeable。
- **看见执行回了 不是已经不挡提议钟：** 看见执行回了，不是已经不挡提议钟 interchangeable。
- **看见候选写进内存 不是已经交差：** 看见候选写进内存，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻整块执行 正式三事（327 余量），先数清问的是是不是已经离开关键路径、是不是已经不挡提议钟、还是看见候选写进内存是不是已经交差，再决定要不要同一次发布。327 prepare-timeout vs liveness bundled unbundling 在本页 item 1 启动。
