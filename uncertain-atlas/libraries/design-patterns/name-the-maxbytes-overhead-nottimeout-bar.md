# 模式：点名 timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事（344 余量）

**层次**：实现 / BlockParams.MaxBytes 开销与投递。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-overhead-nottimeout-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-overhead-nottimeout-vs-bundled.md)。

timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事（344 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **满块投递延迟 不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行：** 看见填了 TimeoutPropose，不是已经按满块投递算过 interchangeable / 883 maxbytes-overhead-nottimeout interchangeable。
- **看见超时在 不是已经离开关键路径：** 看见超时在，不是已经离开关键路径 interchangeable。
- **看见投递延迟 不是已经交差：** 看见投递延迟，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 timeout 必须按满块投递延迟算 正式三事（344 余量），先数清问的是是不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行、是不是已经离开关键路径、还是看见投递延迟是不是已经交差，再决定要不要同一次发布。344 maxbytes vs full bundled unbundling 在本页 item 3 完成。
