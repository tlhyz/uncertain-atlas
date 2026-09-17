# 模式：点名 只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事（354 余量）

**层次**：实现 / Process 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-when-notreject-vs-bundled.md](../../tracks/implementation/worked-example-process-when-notreject-vs-bundled.md)。

只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事（354 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **已经回了 ACCEPT 不是已经还能再 Reject：** 看见已经回了 ACCEPT，不是已经还能再 Reject interchangeable / 858 process-when-notreject interchangeable。
- **看见还在跑 不是已经还能强迫 nil：** 看见还在跑，不是已经还能强迫 prevote/precommit nil interchangeable。
- **看见异步了 不是已经交差：** 看见异步了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只做基本检查再异步 Process 正式三事（354 余量），先数清问的是是不是已经还能再 Reject、是不是已经还能强迫 nil、还是看见异步了是不是已经交差，再决定要不要同一次发布。354 process-when vs later bundled unbundling 在本页 item 2 续。
