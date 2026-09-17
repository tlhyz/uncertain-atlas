# 反模式：把 块进 store not already settled / not already committed / not already atomic 正式三事（320 余量） 写成已经 已经交差 / 应用已经提交 / 已经原子

**层次**：实现 / 块进 store not already settled / not already committed / not already atomic 正式三事（320 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应**：[`../tracks/implementation/worked-example-crashrec-notcommit-vs-bundled.md`](../tracks/implementation/worked-example-crashrec-notcommit-vs-bundled.md)。

把 块进 store not already settled / not already committed / not already atomic 正式三事（320 余量） 写成已经 已经交差 / 应用已经提交 / 已经原子，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看块进 store 正式三事（320 余量），必须分开 not already settled、not already committed、not already atomic 三件事，不要和 320 / 298 / 335 / 1019 / 1021 糊成一句。

也不是：

- [crashrec-notahead-sold-as-bundled](crashrec-notahead-sold-as-bundled.md) 是应用比引擎高仍未允许单句边界（1019 item 1），不是本页块进 store 仍未 Commit 边界。
- WAL 已经 fsync 是不变量 298，不是本页结果存了仍未应用提交边界。
