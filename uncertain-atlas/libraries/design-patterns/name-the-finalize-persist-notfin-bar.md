# 模式：点名 必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事（335 余量）

**层次**：实现 / FinalizeBlock 落盘禁令。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-persist-notfin-vs-bundled.md](../../tracks/implementation/worked-example-finalize-persist-notfin-vs-bundled.md)。

必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事（335 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **必须在 Commit 落盘 不是已经在 Finalize 落了：** 看见必须在 Commit 落盘，不是已经在 Finalize 落了 interchangeable / 903 finalize-persist-notfin interchangeable。
- **看见返回前写完 不是已经解锁：** 看见返回前写完，不是已经解锁 interchangeable。
- **看见 Commit 绿了 不是已经交差：** 看见 Commit 绿了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须在 Commit 落盘 正式三事（335 余量），先数清问的是是不是已经在 Finalize 落了、是不是已经解锁、还是看见 Commit 绿了是不是已经交差，再决定要不要同一次发布。335 finalize-persist vs commit bundled unbundling 在本页 item 2 续。
