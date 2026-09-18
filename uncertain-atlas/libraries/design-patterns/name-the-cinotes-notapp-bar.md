# 模式：点名 cinotes-notapp 杠

**层次**：实现 / CiNotes engine guarantees and persists order not already app-sorted / not already recv-order / not already Process-decided 正式三事（444 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes 句。  
**对应**：[`../tracks/implementation/worked-example-cinotes-notapp-vs-bundled.md`](../tracks/implementation/worked-example-cinotes-notapp-vs-bundled.md)。

- **引擎保证并落盘顺序不是已经由应用排过 不是已经由应用排过：看见引擎保证并落盘顺序不是已经由应用排过，不是已经由应用排过 interchangeable / 1354 cinotes-notapp interchangeable。**
- **engine guarantees and persists order is not already sorted by the app 不是已经是收到票时的顺序：看见engine guarantees and persists order is not already sorted by the app，不是已经是收到票时的顺序 interchangeable / 1354 cinotes-notapp interchangeable。**
- **引擎保证并落盘顺序不是已经由应用排过 不是已经由 Process 回包决定：看见引擎保证并落盘顺序不是已经由应用排过，不是已经由 Process 回包决定 interchangeable / 1354 cinotes-notapp interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（444 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
