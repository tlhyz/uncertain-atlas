# 反模式：把 CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量） 写成已经 已经保证不重放 / 已经过了 CheckTx 就有应用级保护 / 已经交差

**层次**：实现 / CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-cguard-notreplay-vs-bundled.md`](../tracks/implementation/worked-example-cguard-notreplay-vs-bundled.md)。

把 CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量） 写成已经 已经保证不重放 / 已经过了 CheckTx 就有应用级保护 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看来源 正式三事（405 余量），必须分开 not already no-replay、not already app-protected、not already settled 三件事，不要和 405 / 313 / 328 / 1103 / 1105 糊成一句。

也不是：

- [cguard-notopt-sold-as-bundled](cguard-notopt-sold-as-bundled.md) 是守卫仍未是技术上可选单句边界（1103 item 1），不是本页来源仍未保证不重放边界。
- 内存池去重就已经保证不重放是不变量 313，不是本页能来自邻居仍未有应用级保护边界。
