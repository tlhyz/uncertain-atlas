# 模式：点名 h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事（330 余量）

**层次**：实现 / VoteExtensionsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-ve-height-notlegal-vs-bundled.md](../../tracks/implementation/worked-example-ve-height-notlegal-vs-bundled.md)。

h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事（330 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **h < H 带了扩展 不是已经合法：** 看见 h < H 的票带了扩展，不是已经合法 interchangeable / 928 ve-height-notlegal interchangeable。
- **看见字段在 不是已经启用：** 看见字段在，不是已经切到 ABCI 2.0 interchangeable。
- **看见字段在 不是已经交差：** 看见字段在，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h < H 带了扩展 正式三事（330 余量），先数清问的是是不是已经合法、是不是已经启用、还是看见字段在是不是已经交差，再决定要不要同一次发布。330 ve-height vs prepare bundled unbundling 在本页 item 3 完成。
