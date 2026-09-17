# 反模式：把 内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量） 写成已经 已经保证不重复 / 已经有强保证 / 已经交差

**层次**：实现 / 内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应**：[`../tracks/implementation/worked-example-replayprot-notguar-vs-bundled.md`](../tracks/implementation/worked-example-replayprot-notguar-vs-bundled.md)。

把 内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量） 写成已经 已经保证不重复 / 已经有强保证 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看内存池去重 正式三事（313 余量），必须分开 not already guaranteed、not already strong、not already settled 三件事，不要和 313 / 312 / 339 / 966 / 967 糊成一句。

也不是：

- [querystate-notsnap-sold-as-bundled](querystate-notsnap-sold-as-bundled.md) 是启动对齐仍不是快照重放边界（314/964），不是本页池子挡过仍无保证边界。
- CheckTxState 已经是 ExecuteTxState 是不变量 312，不是本页索引器在仍无强保证边界。
