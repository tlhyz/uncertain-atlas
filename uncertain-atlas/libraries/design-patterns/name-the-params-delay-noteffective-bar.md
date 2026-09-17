# 模式：点名 本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事（333 余量）

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：建议（产品）。  
**对应例**：[worked-example-params-delay-noteffective-vs-bundled.md](../../tracks/implementation/worked-example-params-delay-noteffective-vs-bundled.md)。

本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事（333 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **本高回了 ConsensusParams 不是已经在本高生效：** 看见本高回了参数，不是已经在本高用上 interchangeable / 911 params-delay-noteffective interchangeable。
- **看见本高 Finalize 绿了 不是已经本高提议按新上限：** 看见本高 Finalize 绿了，不是本高提议已经按新上限 interchangeable。
- **看见能更新 不是已经交差：** 看见能更新，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本高回了 ConsensusParams 正式三事（333 余量），先数清问的是是不是已经在本高生效、是不是已经本高提议按新上限、还是看见能更新是不是已经交差，再决定要不要同一次发布。333 params-delay vs set bundled unbundling 在本页 item 1 启动。
