# 模式：点名 两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事（342 余量）

**层次**：实现 / FinalizeBlock 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-det-notprocess-vs-bundled.md](../../tracks/implementation/worked-example-finalize-det-notprocess-vs-bundled.md)。

两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事（342 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **状态机复制 不是已经是 Process 对任意块同一裁决：** 看见状态机复制，不是已经是 Process 对任意块同一裁决 interchangeable / 889 finalize-det-notprocess interchangeable。
- **看见两边状态一起走 不是已经是 Prepare 可以不确定：** 看见两边状态一起走，不是已经是 Prepare 可以不确定 interchangeable。
- **看见 Agreement 不是已经交差：** 看见 Agreement，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边状态机复制 正式三事（342 余量），先数清问的是是不是已经是 Process 对任意块同一裁决、是不是已经是 Prepare 可以不确定、还是看见 Agreement 是不是已经交差，再决定要不要同一次发布。342 finalize-det vs prepare bundled unbundling 在本页 item 3 完成。
