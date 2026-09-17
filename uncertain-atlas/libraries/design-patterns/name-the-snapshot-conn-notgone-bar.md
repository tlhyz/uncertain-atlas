# 模式：点名 应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事（334 余量）

**层次**：实现 / Snapshot Connection。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-conn-notgone-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-conn-notgone-vs-bundled.md)。

应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事（334 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **应用选择不实现 不是已经没有 state sync 这条对象：** 看见可选，不是已经删掉这条对象 interchangeable / 934 snapshot-conn-notgone interchangeable。
- **看见快照管理可选 不是已经从创世是唯一合法路径：** 看见可选，不是已经等于从创世 interchangeable。
- **看见可选 不是已经交差：** 看见可选，不是已经清单齐了 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用选择不实现 正式三事（334 余量），先数清问的是是不是已经没有 state sync 这条对象、是不是已经从创世是唯一合法路径、还是看见可选是不是已经交差，再决定要不要同一次发布。334 snapshot-conn vs required bundled unbundling 在本页 item 3 完成。
