# 模式：点名 同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事（328 余量）

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-oscillate-notcode-vs-bundled.md](../../tracks/implementation/worked-example-checktx-oscillate-notcode-vs-bundled.md)。

同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事（328 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **同一高度回了不同码 不是已经有了 CheckTxCode：** 看见回了两次，不是已经有这个码 interchangeable / 941 checktx-oscillate-notcode interchangeable。
- **看见集合在 不是已经能说 OK：** 看见集合在，不是已经能说成功 interchangeable。
- **看见集合在 不是已经交差：** 看见集合在，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度回了不同码 正式三事（328 余量），先数清问的是是不是已经有了 CheckTxCode、是不是已经能说 OK、还是看见集合在是不是已经交差，再决定要不要同一次发布。328 checktx-oscillate vs stable bundled unbundling 在本页 item 1 启动。
