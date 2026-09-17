# 模式：点名 从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事（355 余量）

**层次**：实现 / Prepare 改列表。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-drop-notdeleted-vs-bundled.md](../../tracks/implementation/worked-example-prepare-drop-notdeleted-vs-bundled.md)。

从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事（355 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **本块不提 不是已经从内存池删掉：** 看见本块不提，不是已经从内存池删掉 interchangeable / 854 prepare-drop-notdeleted interchangeable。
- **看见拿掉了 不是已经永远不提：** 看见本块不提，不是已经永远不提 interchangeable。
- **看见回包没有它 不是已经交差：** 看见本块不提，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从提案拿掉 tx 正式三事（355 余量），先数清问的是是不是已经从内存池删掉、是不是已经永远不提、还是看见回包没有它是不是已经交差，再决定要不要同一次发布。355 prepare-drop vs mempool bundled unbundling 在本页 item 1 启动。
