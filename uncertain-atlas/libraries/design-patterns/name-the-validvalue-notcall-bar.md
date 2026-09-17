# 模式：点名 validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事（356 余量）

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validvalue-notcall-vs-bundled.md](../../tracks/implementation/worked-example-validvalue-notcall-vs-bundled.md)。

validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事（356 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **直接用了 不是已经还会调 Prepare：** 看见直接用了，不是已经还会调 Prepare interchangeable / 851 validvalue-notcall interchangeable。
- **看见有 validValue 不是已经能再改列表：** 看见直接用了，不是已经能再改列表 interchangeable。
- **看见锁住了 不是已经交差：** 看见直接用了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validValue 非 nil 正式三事（356 余量），先数清问的是是不是已经还会调 Prepare、是不是已经能再改列表、还是看见锁住了是不是已经交差，再决定要不要同一次发布。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。
