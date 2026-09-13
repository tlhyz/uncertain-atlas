# 模式：把 CheckTx Request type 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`。  
**例**：[CheckTx_New ≠ CheckTx_Recheck](../../tracks/implementation/worked-example-chktxtype-vs-recheck.md)。

## 三个名字

1. **CheckTx_New default full check 不是 CheckTx_Recheck / tx 栏就等于 Recheck：** 看见 New 是默认完整验，不是内存池正常再验 interchangeable。
2. **CheckTx_Recheck mempool normal recheck 不是外部新交易 / 去重保证不重放：** 看见 Recheck 是内存池发起再验，不是外部 admission interchangeable。
3. **Request type 栏 不是 tx 栏 / Commit 后再验不需要读 Type：** 看见 type 标明 New vs Recheck，不是已经填 tx 就知道种类 interchangeable。

## 为什么要分开叫

官方把 CheckTx Request `type` 栏里 New / Recheck 枚举、app requirements 里 Commit 后再验 Type 标明，和 tx 栏、When recheck 流程写成三个名字。把它们叫成一个「看见填了 CheckTx 请求就已经是 Recheck」，会把 New 完整验、Recheck 再验、type 栏 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type，先数清问的是 CheckTx_New 是不是 Recheck、CheckTx_Recheck 是不是外部新交易、Request type 栏是不是 tx 栏 interchangeable，再决定要不要同一次发布。
