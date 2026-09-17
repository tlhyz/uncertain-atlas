# 模式：点名 失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事（351 余量）

**层次**：实现 / Process 也会在提议者那边叫。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-also-notevery-vs-bundled.md](../../tracks/implementation/worked-example-process-also-notevery-vs-bundled.md)。

失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事（351 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **叫了 Process 不是已经是这一次 Prepare：** 看见失败时可能对上更早一次，不是已经是这一次 Prepare interchangeable / 862 process-also-notevery interchangeable。
- **看见进了这一轮 不是已经每轮都会叫：** 看见进了这一轮，不是已经每轮都会叫 interchangeable。
- **看见失败了 不是已经交差：** 看见失败了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看失败时可能对上更早一次或根本不调 正式三事（351 余量），先数清问的是是不是已经是这一次 Prepare、是不是已经每轮都会叫、还是看见失败了是不是已经交差，再决定要不要同一次发布。351 process-also vs prepare bundled unbundling 在本页 item 3 完成。
