# 模式：点名 Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事（370 余量）

**层次**：实现 / Info 握手。  
**分类**：建议（产品）。  
**对应例**：[worked-example-info-notreplay-vs-bundled.md](../../tracks/implementation/worked-example-info-notreplay-vs-bundled.md)。

Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事（370 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **握手对齐 不是已经是快照重放：** 看见能回，不是已经 314 interchangeable / 815 info-notreplay interchangeable。
- **看见握手了 不是已经是 QueryState：** 看见能回，不是已经是 QueryState interchangeable。
- **看见对齐了 不是已经交差：** 看见能回，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 握手 正式三事（370 余量），先数清问的是是不是已经是快照重放 / 314、是不是已经是 QueryState、还是看见对齐了是不是已经交差，再决定要不要同一次发布。370 info vs handshake bundled unbundling 在本页 item 1 启动。
