# 模式：点名 Query 高度 not already QueryState / not already replicated / not already settled 正式三事（371 余量）

**层次**：实现 / Query 高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-queryheight-notstate-vs-bundled.md](../../tracks/implementation/worked-example-queryheight-notstate-vs-bundled.md)。

Query 高度 not already QueryState / not already replicated / not already settled 正式三事（371 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **能查 不是已经是 QueryState：** 看见能查，不是已经 329 interchangeable / 812 queryheight-notstate interchangeable。
- **看见填了高度 不是已经复制：** 看见能查，不是已经复制 interchangeable。
- **看见能回 不是已经交差：** 看见能查，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 高度 正式三事（371 余量），先数清问的是是不是已经是 QueryState / 329、是不是已经复制、还是看见能回是不是已经交差，再决定要不要同一次发布。371 queryheight vs committed bundled unbundling 在本页 item 1 启动。
