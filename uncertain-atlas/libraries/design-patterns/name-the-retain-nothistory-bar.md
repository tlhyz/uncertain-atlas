# 模式：点名 低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事（366 余量）

**层次**：实现 / Commit 保留高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-retain-nothistory-vs-bundled.md](../../tracks/implementation/worked-example-retain-nothistory-vs-bundled.md)。

低于这个高度可删 not already no history / not already snapshot truncated / not already deleted 正式三事（366 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回了高度 不是已经没有历史：** 看见回了高度，不是已经 323 interchangeable / 828 retain-nothistory interchangeable。
- **看见能删 不是已经是快照截断：** 看见回了高度，不是已经是快照截断 interchangeable。
- **看见能剪 不是已经删完：** 看见回了高度，不是已经删完 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看低于这个高度可删 正式三事（366 余量），先数清问的是是不是已经没有历史 / 323、是不是已经是快照截断、还是看见能剪是不是已经删完，再决定要不要同一次发布。366 retain vs kept bundled unbundling 在本页 item 2 续。
