# 模式：点名 参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事（333 余量）

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：建议（产品）。  
**对应例**：[worked-example-params-delay-notve-vs-bundled.md](../../tracks/implementation/worked-example-params-delay-notve-vs-bundled.md)。

参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事（333 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **参数更新写了 H+1 不是已经是扩展启用高度那种切换：** 看见写了 H+1，不是已经切到 ABCI 2.0 interchangeable / 913 params-delay-notve interchangeable。
- **看见立刻生效 不是已经只改填的那一项：** 看见立刻生效，不是已经保持没填的字段 interchangeable。
- **看见写了 H+1 不是已经交差：** 看见写了 H+1，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参数更新写了 H+1 正式三事（333 余量），先数清问的是是不是已经是扩展启用高度那种切换、是不是已经只改填的那一项、还是看见写了 H+1 是不是已经交差，再决定要不要同一次发布。333 params-delay vs set bundled unbundling 在本页 item 3 完成。
