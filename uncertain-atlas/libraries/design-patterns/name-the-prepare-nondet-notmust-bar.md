# 模式：点名 Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事（338 余量）

**层次**：实现 / PrepareProposal 与 ExtendVote 的确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-nondet-notmust-vs-bundled.md](../../tracks/implementation/worked-example-prepare-nondet-notmust-vs-bundled.md)。

Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事（338 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **没有确定性要求 不是已经必须确定：** 看见没有这道要求，不是已经必须确定 interchangeable / 896 prepare-nondet-notmust interchangeable。
- **看见可以依赖其它值 不是已经和 Process 同一把尺：** 看见可以依赖其它值，不是已经和 Process 同一把尺 interchangeable。
- **看见 Prepare 回了 不是已经交差：** 看见 Prepare 回了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有确定性要求 正式三事（338 余量），先数清问的是是不是已经必须确定、是不是已经和 Process 同一把尺、还是看见 Prepare 回了是不是已经交差，再决定要不要同一次发布。338 prepare-nondet vs process bundled unbundling 在本页 item 1 启动。
