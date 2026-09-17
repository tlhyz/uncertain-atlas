# 模式：点名 Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事（349 余量）

**层次**：实现 / 四门无副作用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req9-notproc-vs-bundled.md](../../tracks/implementation/worked-example-req9-notproc-vs-bundled.md)。

Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事（349 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **Accept 不是已经改了已提交状态：** 看见回了 Accept，不是已经改了已提交状态 interchangeable / 867 req9-notproc interchangeable。
- **看见 Reject 了 不是已经是 ExecuteTxState：** 看见 Reject 了，不是已经是候选 ExecuteTxState interchangeable。
- **看见跑过了 不是已经交差：** 看见跑过了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 不得改已提交状态 正式三事（349 余量），先数清问的是是不是已经 Accept 就已经改了、是不是已经是候选 ExecuteTxState、还是看见跑过了是不是已经交差，再决定要不要同一次发布。349 req9 vs commit bundled unbundling 在本页 item 2 续。
