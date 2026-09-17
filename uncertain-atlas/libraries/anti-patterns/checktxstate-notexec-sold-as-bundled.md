# 反模式：把 CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量） 写成已经 已经按 ExecuteTxState 验过 / 已经按将要执行的那份验过 / 已经交差

**层次**：实现 / CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应**：[`../tracks/implementation/worked-example-checktxstate-notexec-vs-bundled.md`](../tracks/implementation/worked-example-checktxstate-notexec-vs-bundled.md)。

把 CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量） 写成已经 已经按 ExecuteTxState 验过 / 已经按将要执行的那份验过 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 过了 正式三事（312 余量），必须分开 not already ExecuteTxState、not already future-exec、not already settled 三件事，不要和 312 / 311 / 313 / 969 / 970 糊成一句。

也不是：

- [replayprot-notidem-sold-as-bundled](replayprot-notidem-sold-as-bundled.md) 是通常不受欢迎仍有幂等例外边界（313/967），不是本页过了仍未按 ExecuteTxState 验边界。
- 候选已经是 ExecuteTxState 是不变量 311，不是本页进了池仍未按将要执行的那份验边界。
