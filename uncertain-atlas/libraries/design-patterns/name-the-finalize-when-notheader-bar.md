# 模式：点名 回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事（362 余量）

**层次**：实现 / Finalize 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-when-notheader-vs-bundled.md](../../tracks/implementation/worked-example-finalize-when-notheader-vs-bundled.md)。

回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事（362 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回了 不是已经印进本头：** 看见回了，不是已经印进本头 interchangeable / 841 finalize-when-notheader interchangeable。
- **看见有 ResultHash 不是已经是本头 AppHash：** 看见回了，不是已经是本头 AppHash interchangeable / 147。
- **看见哈希了 不是已经交差：** 看见回了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回了 AppHash 和输出哈希进 ResultHash 正式三事（362 余量），先数清问的是是不是已经印进本头、是不是已经是本头 AppHash / 147、还是看见哈希了是不是已经交差，再决定要不要同一次发布。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。
