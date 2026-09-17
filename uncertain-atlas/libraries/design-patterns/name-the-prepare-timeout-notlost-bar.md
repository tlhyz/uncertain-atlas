# 模式：点名 又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事（327 余量）

**层次**：实现 / PrepareProposal 及时性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-timeout-notlost-vs-bundled.md](../../tracks/implementation/worked-example-prepare-timeout-notlost-vs-bundled.md)。

又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事（327 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **又开一轮 不是已经丢了活性：** 看见又开一轮，不是已经停 interchangeable / 901 prepare-timeout-notlost interchangeable。
- **看见初值 不是超时已经不再涨：** 看见初值，不是已经是最后那一档 interchangeable。
- **看见又开一轮 不是已经交差：** 看见又开一轮，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看又开一轮 正式三事（327 余量），先数清问的是是不是已经丢了活性、是不是超时已经不再涨、还是看见又开一轮是不是已经交差，再决定要不要同一次发布。327 prepare-timeout vs liveness bundled unbundling 在本页 item 3 完成。
