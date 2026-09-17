# 反模式：把 上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量） 写成已经 已经跟上正在跑的块 / 已经是 CheckTxState / 已经交差

**层次**：实现 / 上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应**：[`../tracks/implementation/worked-example-querystate-notlive-vs-bundled.md`](../tracks/implementation/worked-example-querystate-notlive-vs-bundled.md)。

把 上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量） 写成已经 已经跟上正在跑的块 / 已经是 CheckTxState / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看上次 Commit 正式三事（314 余量），必须分开 not already live、not already CheckTxState、not already settled 三件事，不要和 314 / 310 / 321 / 962 / 964 糊成一句。

也不是：

- [querystate-notexec-sold-as-bundled](querystate-notexec-sold-as-bundled.md) 是能查仍不是 ExecuteTxState 单句边界（962 item 1），不是本页上次 Commit 仍未跟上正在跑的块边界。
- 默认锁已经 RPC 安全是不变量 310，不是本页能读仍不是 CheckTxState 边界。
