# 模式：点名 填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事（327 余量）

**层次**：实现 / PrepareProposal 及时性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-timeout-notfit-vs-bundled.md](../../tracks/implementation/worked-example-prepare-timeout-notfit-vs-bundled.md)。

填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事（327 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **填了 TimeoutPropose 不是已经装得下：** 看见填了这个值，不是已经装得下 interchangeable / 900 prepare-timeout-notfit interchangeable。
- **看见同步期 不是钟已经不会响：** 看见同步期，不是钟已经不会响 interchangeable。
- **看见填了这个值 不是已经交差：** 看见填了这个值，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 TimeoutPropose 正式三事（327 余量），先数清问的是是不是已经装得下、是不是钟已经不会响、还是看见填了这个值是不是已经交差，再决定要不要同一次发布。327 prepare-timeout vs liveness bundled unbundling 在本页 item 2 续。
