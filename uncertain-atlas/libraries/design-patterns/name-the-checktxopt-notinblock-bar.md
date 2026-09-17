# 模式：点名 Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事（373 余量）

**层次**：实现 / CheckTx 可选。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktxopt-notinblock-vs-bundled.md](../../tracks/implementation/worked-example-checktxopt-notinblock-vs-bundled.md)。

Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事（373 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **Code≠0 拒收 不是已经没进块：** 看见拒了，不是已经 316 interchangeable / 807 checktxopt-notinblock interchangeable。
- **看见没广播 不是已经被挡住拜占庭：** 看见拒了，不是已经被挡住 interchangeable。
- **看见没进提案 不是已经交差：** 看见拒收，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code≠0 拒收 正式三事（373 余量），先数清问的是是不是已经没进块 / 316、是不是已经被挡住拜占庭、还是看见没进提案是不是已经交差，再决定要不要同一次发布。373 checktxopt vs block bundled unbundling 在本页 item 2 续。
