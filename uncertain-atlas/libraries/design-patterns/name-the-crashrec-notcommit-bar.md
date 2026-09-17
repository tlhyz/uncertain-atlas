# 模式：点名 crashrec-notcommit 杠

**层次**：实现 / 块进 store not already settled / not already committed / not already atomic 正式三事（320 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应**：[`../tracks/implementation/worked-example-crashrec-notcommit-vs-bundled.md`](../tracks/implementation/worked-example-crashrec-notcommit-vs-bundled.md)。

- **块进 store 不是已经交差：** 看见块存了，不是已经交差 interchangeable / 1020 crashrec-notcommit interchangeable。
- **看见结果存了 不是应用已经提交：** 看见结果存了，不是应用已经提交 interchangeable。
- **看见三步 不是已经原子：** 看见三步，不是已经原子 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看块进 store 正式三事（320 余量），先数清问的是是不是已经交差、是不是应用已经提交、还是看见三步是不是已经原子，再决定要不要同一次发布。320 crash-steps vs commit bundled unbundling 在本页 item 2 续。
