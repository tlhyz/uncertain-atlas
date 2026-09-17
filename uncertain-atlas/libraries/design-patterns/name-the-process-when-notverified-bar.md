# 模式：点名 非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事（354 余量）

**层次**：实现 / Process 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-when-notverified-vs-bundled.md](../../tracks/implementation/worked-example-process-when-notverified-vs-bundled.md)。

非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事（354 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **立刻 ACCEPT 不是已经验过这块：** 看见非验证者可以立刻回 ACCEPT，不是已经验过这块 interchangeable / 859 process-when-notverified interchangeable。
- **看见规范允许 不是已经是验证者也可以立刻交差：** 看见规范允许，不是已经是验证者也可以立刻交差 interchangeable。
- **看见立刻 ACCEPT 不是已经交差：** 看见立刻 ACCEPT，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看非验证者可以立刻回 ACCEPT 正式三事（354 余量），先数清问的是是不是已经验过这块、是不是已经是验证者也可以立刻交差、还是看见立刻 ACCEPT 是不是已经交差，再决定要不要同一次发布。354 process-when vs later bundled unbundling 在本页 item 3 完成。
