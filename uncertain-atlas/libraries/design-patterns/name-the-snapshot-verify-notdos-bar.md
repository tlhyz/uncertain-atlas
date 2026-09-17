# 模式：点名 封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事（332 余量）

**层次**：实现 / Snapshot Verification。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-verify-notdos-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-verify-notdos-vs-bundled.md)。

封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事（332 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **封禁邻居 不是已经没有快照 DoS：** 看见封禁了，不是已经没有这种 DoS interchangeable / 937 snapshot-verify-notdos interchangeable。
- **看见配了受信名单 不是已经收下这个人：** 看见配了受信名单，不是已经是过滤已经收下 interchangeable。
- **看见能挡一家 不是已经交差：** 看见能挡一家，不是已经能挡所有有害快照 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看封禁邻居 正式三事（332 余量），先数清问的是是不是已经没有快照 DoS、是不是已经收下这个人、还是看见能挡一家是不是已经交差，再决定要不要同一次发布。332 snapshot-verify vs early bundled unbundling 在本页 item 3 完成。
