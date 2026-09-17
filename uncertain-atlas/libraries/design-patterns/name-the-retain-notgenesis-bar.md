# 模式：点名 全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事（366 余量）

**层次**：实现 / Commit 保留高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-retain-notgenesis-vs-bundled.md](../../tracks/implementation/worked-example-retain-notgenesis-vs-bundled.md)。

全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事（366 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **能剪 不是已经能从创世再装：** 看见能剪，不是已经 38 interchangeable / 829 retain-notgenesis interchangeable。
- **看见开了 state sync 不是已经能给轻客户端验：** 看见能剪，不是已经能给轻客户端验 interchangeable。
- **看见能丢 不是已经交差：** 看见能剪，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看全网都删会永久丢 正式三事（366 余量），先数清问的是是不是已经能从创世再装 / 38、是不是已经能给轻客户端验、还是看见能丢是不是已经交差，再决定要不要同一次发布。366 retain vs kept bundled unbundling 在本页 item 3 完成。
