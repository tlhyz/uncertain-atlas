# 模式：点名 本地不再振荡 not already global same height / not already same b / not already settled 正式三事（328 余量）

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-oscillate-notsameb-vs-bundled.md](../../tracks/implementation/worked-example-checktx-oscillate-notsameb-vs-bundled.md)。

本地不再振荡 not already global same height / not already same b / not already settled 正式三事（328 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **本地不再振荡 不是已经各节点同一份 b：** 看见本地不再振荡，不是已经同一份 b interchangeable / 943 checktx-oscillate-notsameb interchangeable。
- **看见本节点稳住了 不是已经是全局同一高度：** 看见本节点稳住了，不是已经全网同一高度 interchangeable。
- **看见本地 h_p,stable 不是已经交差：** 看见本地 h_p,stable，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地不再振荡 正式三事（328 余量），先数清问的是是不是已经是全局同一高度、是不是已经各节点同一份 b、还是看见本地稳住是不是已经交差，再决定要不要同一次发布。328 checktx-oscillate vs stable bundled unbundling 在本页 item 3 完成。
