# 模式：点名 往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事（355 余量）

**层次**：实现 / Prepare 改列表。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-drop-notinpool-vs-bundled.md](../../tracks/implementation/worked-example-prepare-drop-notinpool-vs-bundled.md)。

往提案加了一笔新的 not already in mempool / not already passed CheckTx / not already settled 正式三事（355 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回包里有它 不是已经进了内存池：** 看见回包里有它，不是已经进了内存池 interchangeable / 855 prepare-drop-notinpool interchangeable。
- **看见能提 不是已经过了 CheckTx：** 看见回包里有它，不是已经过了 CheckTx interchangeable。
- **看见加进去了 不是已经交差：** 看见回包里有它，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看往提案加了一笔新的 正式三事（355 余量），先数清问的是是不是已经进了内存池、是不是已经过了 CheckTx、还是看见加进去了是不是已经交差，再决定要不要同一次发布。355 prepare-drop vs mempool bundled unbundling 在本页 item 2 续。
