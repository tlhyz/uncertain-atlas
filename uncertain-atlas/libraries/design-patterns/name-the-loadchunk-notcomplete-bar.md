# 模式：点名 LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事（375 余量）

**层次**：实现 / LoadSnapshotChunk。  
**分类**：建议（产品）。  
**对应例**：[worked-example-loadchunk-notcomplete-vs-bundled.md](../../tracks/implementation/worked-example-loadchunk-notcomplete-vs-bundled.md)。

LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事（375 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **在拉 不是已经齐：** 看见在拉，不是已经 322 interchangeable / 800 loadchunk-notcomplete interchangeable。
- **看见问了邻居 不是已经有了全部快照：** 看见在拉，不是已经有了全部快照 interchangeable。
- **看见能拉 不是已经装完：** 看见 LoadSnapshotChunk，不是已经装完 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk 正式三事（375 余量），先数清问的是是不是已经齐 / 322、是不是已经有了全部快照、还是看见能拉是不是已经装完，再决定要不要同一次发布。375 loadchunk vs retrieved bundled unbundling 在本页 item 1 启动。
