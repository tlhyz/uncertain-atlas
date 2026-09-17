# 模式：点名 Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事（335 余量）

**层次**：实现 / FinalizeBlock 落盘禁令。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-persist-notdisk-vs-bundled.md](../../tracks/implementation/worked-example-finalize-persist-notdisk-vs-bundled.md)。

Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事（335 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **Finalize 改了状态 不是已经落盘：** 看见改了状态，不是已经写盘 interchangeable / 902 finalize-persist-notdisk interchangeable。
- **看见决定块来了 不是已经 Commit：** 看见决定块来了，不是已经 Commit interchangeable。
- **看见能转移 不是已经交差：** 看见能转移，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 改了状态 正式三事（335 余量），先数清问的是是不是已经落盘、是不是已经 Commit、还是看见能转移是不是已经交差，再决定要不要同一次发布。335 finalize-persist vs commit bundled unbundling 在本页 item 1 启动。
