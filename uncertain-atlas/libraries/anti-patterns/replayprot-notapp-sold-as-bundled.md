# 反模式：把 过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量） 写成已经 已经有应用级保护 / 已经是应用谓词 / 已经交差

**层次**：实现 / 过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应**：[`../tracks/implementation/worked-example-replayprot-notapp-vs-bundled.md`](../tracks/implementation/worked-example-replayprot-notapp-vs-bundled.md)。

把 过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量） 写成已经 已经有应用级保护 / 已经是应用谓词 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看过了 CheckTx 正式三事（313 余量），必须分开 not already app-guard、not already app-predicate、not already settled 三件事，不要和 313 / 301 / 328 / 965 / 967 糊成一句。

也不是：

- [replayprot-notguar-sold-as-bundled](replayprot-notguar-sold-as-bundled.md) 是池子挡过仍无保证单句边界（965 item 1），不是本页过了 CheckTx 仍无应用级保护边界。
- 提案收了已经从池里删掉是不变量 301，不是本页索引器滤过仍不是应用谓词边界。
