# 模式：点名 ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事（361 余量）

**层次**：实现 / ExtendVote 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-when-notlater-vs-bundled.md](../../tracks/implementation/worked-example-extend-when-notlater-vs-bundled.md)。

ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事（361 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **是同步的 不是已经能稍后改扩展：** 看见是同步的，不是已经能稍后改扩展 interchangeable / 843 extend-when-notlater interchangeable。
- **看见引擎在等 不是已经离开关键路径：** 看见是同步的，不是已经离开关键路径 interchangeable。
- **看见回了 不是已经交差：** 看见是同步的，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 调用是同步的 正式三事（361 余量），先数清问的是是不是已经能稍后改扩展、是不是已经离开关键路径、还是看见回了是不是已经交差，再决定要不要同一次发布。361 extend-when vs locked bundled unbundling 在本页 item 2 续。
