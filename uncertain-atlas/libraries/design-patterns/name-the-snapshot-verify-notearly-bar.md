# 模式：点名 装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事（332 余量）

**层次**：实现 / Snapshot Verification。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-verify-notearly-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-verify-notearly-vs-bundled.md)。

装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事（332 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **装完又对上 LastBlockAppHash 不是已经在装回当中验过：** 看见对上了，不是已经在装的时候验过 interchangeable / 935 snapshot-verify-notearly interchangeable。
- **看见高度对上 不是已经进了网：** 看见高度对上，不是已经切进共识 interchangeable。
- **看见 Info 绿了 不是已经交差：** 看见 Info 绿了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完又对上 LastBlockAppHash 正式三事（332 余量），先数清问的是是不是已经在装回当中验过、是不是已经进了网、还是看见 Info 绿了是不是已经交差，再决定要不要同一次发布。332 snapshot-verify vs early bundled unbundling 在本页 item 1 启动。
