# 模式：点名 不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事（339 余量）

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-weak-notsort-vs-bundled.md](../../tracks/implementation/worked-example-checktx-weak-notsort-vs-bundled.md)。

不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事（339 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **不该验排序相关有效性 不是已经该在 CheckTx 里验：** 看见不该验所有，不是已经该把排序相关写进 CheckTx interchangeable / 929 checktx-weak-notsort interchangeable。
- **看见排序会改有效性 不是已经按将要执行的那份验过：** 看见排序会改有效性，不是已经按 ExecuteTxState 验过 interchangeable。
- **看见过了 CheckTx 不是已经交差：** 看见过了 CheckTx，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不该验排序相关有效性 正式三事（339 余量），先数清问的是是不是已经该在 CheckTx 里验、是不是已经按将要执行的那份验过、还是看见过了 CheckTx 是不是已经交差，再决定要不要同一次发布。339 checktx-weak vs process bundled unbundling 在本页 item 1 启动。
