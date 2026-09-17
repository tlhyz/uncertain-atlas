# 反模式：把 CheckTx Request type 正式三事卖成 Recheck / 外部新交易 / tx 栏 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx_New ≠ CheckTx_Recheck](../../tracks/implementation/worked-example-chktxtype-vs-recheck.md)。

## 卖法

- 「看见 `CheckTx_New` / 看见 default full check 就已经是 `CheckTx_Recheck` / 已经从池里再验。」
- 「看见 `CheckTx_Recheck` / 看见 mempool initiating normal recheck 就已经是外部用户新交易 / 已经去重保证不重放。」
- 「看见 Request `type` 栏 / 看见 Type 标明 就已经是填了 `tx` 就知道种类 / 已经 Commit 后再验不需要读 type。」

## 为什么错

官方把 CheckTx_New default full check、CheckTx_Recheck mempool normal recheck、Request type 栏 写成三件独立的实现事。把它们卖成 Recheck、外部新交易、tx 栏 interchangeable，会把 New 完整验、Recheck 再验、type 栏 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type，必须分开 CheckTx_New、CheckTx_Recheck、Request type 栏 三个名字，不要把它们卖成 Recheck / 外部新交易 / tx 栏 interchangeable。

## 和相邻反模式

- [checktxtx-sold-as-recheck](../../libraries/anti-patterns/checktxtx-sold-as-recheck.md) 是 CheckTx 请求 tx 栏就已经 Recheck，不是本页 type 栏 New vs Recheck。
- [checktxstate-sold-as-execute](../../libraries/anti-patterns/checktxstate-sold-as-execute.md) 是 RECHECK 就已经是一笔新交易，不是本页 CheckTx_Recheck mempool recheck。
