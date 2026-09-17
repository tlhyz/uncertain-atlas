# 模式：点名 last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事（370 余量）

**层次**：实现 / Info 握手。  
**分类**：建议（产品）。  
**对应例**：[worked-example-info-notpersist-vs-bundled.md](../../tracks/implementation/worked-example-info-notpersist-vs-bundled.md)。

last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事（370 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回了这两列 不是已经交差：** 看见回了这两列，不是已经交差 interchangeable / 817 info-notpersist interchangeable。
- **看见要在 Commit 里落 不是已经是崩溃三步：** 看见回了这两列，不是已经 320 interchangeable。
- **看见有高度 不是已经在剪：** 看见回了这两列，不是已经在剪 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 last_block 落盘 正式三事（370 余量），先数清问的是是不是已经交差、是不是已经是崩溃三步已经 Commit / 320、还是看见有高度是不是已经在剪，再决定要不要同一次发布。370 info vs handshake bundled unbundling 在本页 item 3 完成。
