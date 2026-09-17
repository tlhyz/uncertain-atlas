# 模式：点名 Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事（354 余量）

**层次**：实现 / Process 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-when-notlater-vs-bundled.md](../../tracks/implementation/worked-example-process-when-notlater-vs-bundled.md)。

Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事（354 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **同步 不是已经能稍后改裁决：** 看见 Process 调用是同步的，不是已经能稍后改裁决 interchangeable / 857 process-when-notlater interchangeable。
- **看见引擎在等 不是已经离开关键路径：** 看见引擎在等回包，不是已经离开关键路径 interchangeable。
- **看见立刻执行 不是已经交差：** 看见立刻执行，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 调用是同步的 正式三事（354 余量），先数清问的是是不是已经能稍后改裁决、是不是已经离开关键路径、还是看见立刻执行是不是已经交差，再决定要不要同一次发布。354 process-when vs later bundled unbundling 在本页 item 1 启动。
