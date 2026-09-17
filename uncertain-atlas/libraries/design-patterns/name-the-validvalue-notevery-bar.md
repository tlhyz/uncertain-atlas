# 模式：点名 自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事（356 余量）

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validvalue-notevery-vs-bundled.md](../../tracks/implementation/worked-example-validvalue-notevery-vs-bundled.md)。

自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事（356 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **是提议者 不是已经每轮都会调 Prepare：** 看见是提议者，不是已经每轮都会调 Prepare interchangeable / 852 validvalue-notevery interchangeable。
- **看见进了这一轮 不是已经是 validValue 为 nil：** 看见是提议者，不是已经是 validValue 为 nil interchangeable。
- **看见规范写了 When 不是已经交差：** 看见是提议者，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自己是提议者 正式三事（356 余量），先数清问的是是不是已经每轮都会调 Prepare、是不是已经是 validValue 为 nil、还是看见规范写了 When 是不是已经交差，再决定要不要同一次发布。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。
