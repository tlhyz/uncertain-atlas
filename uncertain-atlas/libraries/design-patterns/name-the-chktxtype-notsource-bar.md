# 模式：把 CheckTx Request type CheckTx_Recheck mempool normal recheck not external new transaction / not CheckTx_New default / not pool dedup means no replay 正式三事（484 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`。  
**例**：[type ≠ bundled（484）](../../tracks/implementation/worked-example-chktxtype-notsource-vs-bundled.md)。

## 三个名字

1. **CheckTx_Recheck 不是外部新交易：** 看见 mempool initiating，不是已经 405 interchangeable / 708 chktxtype-notsource interchangeable。
2. **看见 Recheck 不是 New default full check：** 看见 Recheck，不是已经 707 interchangeable。
3. **看见 Usage 这句 不是去重保证不重放：** 看见 Recheck 单句，不是已经 313 interchangeable。

官方把 CheckTx Request type 三条核心句拆成三个名字。把它们叫成一个「看见填了 CheckTx 请求就已经是 Recheck」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type CheckTx_Recheck 正式三事（484 余量），先数清问的是 Recheck 是不是外部新交易 / 405、是不是 New default、还是看见 Usage 是不是去重保证不重放 / 313，再决定要不要同一次发布。484 chktxtype vs recheck bundled unbundling 在本页 item 2 续。
