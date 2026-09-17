# 反模式：把 Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事（314 余量） 写成已经 已经是 ExecuteTxState / 已经能写 / 已经交差

**层次**：实现 / Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事（314 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应**：[`../tracks/implementation/worked-example-querystate-notexec-vs-bundled.md`](../tracks/implementation/worked-example-querystate-notexec-vs-bundled.md)。

把 Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事（314 余量） 写成已经 已经是 ExecuteTxState / 已经能写 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 连接 正式三事（314 余量），必须分开 not already ExecuteTxState、not already writable、not already settled 三件事，不要和 314 / 312 / 329 / 963 / 964 糊成一句。

也不是：

- [snapshot-restore-notresume-sold-as-bundled](snapshot-restore-notresume-sold-as-bundled.md) 是换一份仍不能接着装边界（321/961），不是本页能查仍不是 ExecuteTxState 边界。
- CheckTxState 已经是 ExecuteTxState 是不变量 312，不是本页连接在仍不能写边界。
