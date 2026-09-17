# 模式：点名 还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事（328 余量）

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-oscillate-notstable-vs-bundled.md](../../tracks/implementation/worked-example-checktx-oscillate-notstable-vs-bundled.md)。

还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事（328 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **还在振荡 不是已经过了 h_stable：** 看见还在振荡，不是已经过了 h_stable interchangeable / 942 checktx-oscillate-notstable interchangeable。
- **看见还在池里 不是已经离池：** 看见还在池里，不是已经离池 interchangeable。
- **看见最终不再振荡 不是已经交差：** 看见最终不再振荡，不是已经进了块 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还在振荡 正式三事（328 余量），先数清问的是是不是已经过了 h_stable、是不是已经离池、还是看见最终不再振荡是不是已经交差，再决定要不要同一次发布。328 checktx-oscillate vs stable bundled unbundling 在本页 item 2 续。
