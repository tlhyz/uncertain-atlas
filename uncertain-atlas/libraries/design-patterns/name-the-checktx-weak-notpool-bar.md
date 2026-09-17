# 模式：点名 拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事（339 余量）

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-weak-notpool-vs-bundled.md](../../tracks/implementation/worked-example-checktx-weak-notpool-vs-bundled.md)。

拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事（339 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **拜占庭能提案一满块无效交易 不是已经被池子挡住：** 看见池子会挡，不是拜占庭已经被挡住 interchangeable / 930 checktx-weak-notpool interchangeable。
- **看见能提案无效交易 不是已经进不了共识：** 看见能提案无效交易，不是已经进不了块 interchangeable。
- **看见诚实节点过了 CheckTx 不是已经交差：** 看见诚实节点过了 CheckTx，不是对手已经守同一把尺 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拜占庭能提案一满块无效交易 正式三事（339 余量），先数清问的是是不是已经被池子挡住、是不是已经进不了共识、还是看见诚实节点过了 CheckTx 是不是已经交差，再决定要不要同一次发布。339 checktx-weak vs process bundled unbundling 在本页 item 2 续。
