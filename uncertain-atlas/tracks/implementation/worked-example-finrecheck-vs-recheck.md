# 例：看见 optionally re-checks outstanding mempool transactions 不是已经必须再验 / 已经交差；看见 all outstanding transactions in the mempool 不是已经新交易 / 已经 CheckTx 过了；看见 against the newly persisted Application state 不是已经 CheckTxState / ExecuteTxState / 已经 Type=RECHECK bundled

**层次**：实现 / FinalizeBlock When optional recheck 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 9。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「optionally re-checks 不是已经必须再验 / 已经交差 / outstanding mempool txs 不是已经新交易 / 已经 CheckTx 过了 / against newly persisted Application state 不是已经 CheckTxState / ExecuteTxState / 已经 Type=RECHECK bundled」，不是 Finalize 之后 bundled 三事，不是 CheckTx Type bundled，也不是 locks mempool bundled。不要另写怎样再验、怎样填 Type、怎样解锁。

## 官方三件事

规范把 When 第 9 步 optionally re-checks all outstanding transactions in the mempool against the newly persisted Application state 写成三件独立的实现事，不是「看见 When 第 9 步再验了就已经交差、已经是 Recheck、已经对新交易也验了」一件事：

1. **看见 optionally re-checks / 看见 When 第 9 步可选再验 不是已经必须再验，也不是已经交差 / 已经四门已经结算。**  
   官方 When 第 9 步写：_p_'s CometBFT, **optionally**, re-checks …。发生在 When 第 8 步 calls `Commit` 之后、第 10 步 unlocks the mempool 之前。看见 optionally，不是已经必须再验才能开下一高 interchangeable。看见 When 第 9 步，不是已经 Finalize + Commit 交差（33）。看见可选再验，不是已经 Finalize 之后 bundled（403）第三件事整包 interchangeable——403 另钉 Finalize 之后 recheck+unlock+h+1，本页只钉 When 第 9 步 optional。
2. **看见 all outstanding transactions in the mempool / 看见池里剩下的 outstanding txs 不是已经 new transactions / 已经 CheckTx 过了就永远有效。**  
   官方 When 第 9 步写：re-checks **all outstanding transactions in the mempool**。看见 outstanding in mempool，不是已经 no calls to `CheckTx` on **new** transactions（588）那种新交易不进 CheckTx interchangeable——588 钉 When 第 7 步锁新交易，本页钉 When 第 9 步再验池里剩下的。看见再验 outstanding，不是已经 CheckTx 过了就永远有效（301） interchangeable。看见池里剩下的，不是已经提案收了已经从池里删掉（301）那种交接 interchangeable。
3. **看见 against the newly persisted Application state / 看见对照刚落盘的应用状态 不是已经 CheckTxState / ExecuteTxState，也不是已经 `CheckTx` 的 `Type` 标明 `RECHECK` interchangeable。**  
   官方 When 第 9 步写：re-checks … **against the newly persisted Application state**。看见 newly persisted，不是已经 Finalize 改了就已经落盘（335） interchangeable。看见对照刚落盘状态，不是已经 CheckTx 只是弱过滤器、不能保证验的就是以后执行那份状态（312 Usage 前半） interchangeable。看见 When 第 9 步再验，不是已经 `CheckTxRequest` 的 `Type` 标明 `CHECK_TX_TYPE_RECHECK`（312 / 484）就已经是同一句 interchangeable——312 / 484 钉 Request type / Commit 后再验机制，本页钉 When 第 9 步 optional recheck 对象。

怎样再验、怎样填 Type、怎样解锁是规范里的做法，本页不抄。Finalize 之后 bundled（403）是落完锁 / Commit / optional recheck / unlock / h+1 那套另一切片，locks mempool（588）是 When 第 7 步 no new CheckTx 那套另一切片，calls Commit instruct persist（590）是 When 第 8 步那套另一切片，CheckTx Type（312 / 484）是 RECHECK vs NEW 那套另一切片，CheckTx 过了就永远有效（301）是池交接那套另一切片，CheckTx 弱过滤器（339）是 Process 对付无效块那套另一切片，本页不抄。

## 官方为什么这样拆

- **optionally re-checks ≠ 已经必须再验 / 已经交差：** 官方把 When 第 9 步 optional 再验和必须再验、Finalize + Commit 交差分开。
- **all outstanding transactions in the mempool ≠ 已经 new transactions / 已经 CheckTx 过了：** 官方把再验池里 outstanding 和新交易不进 CheckTx、过了就永远有效分开。
- **against newly persisted Application state ≠ 已经 CheckTxState / ExecuteTxState / 已经 Type=RECHECK：** 官方把 When 第 9 步对照刚落盘状态和 CheckTxState、ExecuteTxState、Request type 栏分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| optionally re-checks | 不是已经必须再验 | 不是 Finalize 之后 bundled（403） |
| all outstanding transactions in the mempool | 不是已经 new transactions | 不是 locks mempool（588） |
| against newly persisted Application state | 不是已经 Type=RECHECK | 不是 CheckTx Type（312 / 484） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 When 第 9 步再验了就已经交差、已经是 Recheck、已经对新交易也验了」，必须分开 optionally re-checks 是不是已经必须再验 / 已经交差、all outstanding transactions in the mempool 是不是已经 new transactions / 已经 CheckTx 过了、against newly persisted Application state 是不是已经 CheckTxState / ExecuteTxState / 已经 Type=RECHECK bundled。可以跳过「看见再验了就已经交差」。不要另写怎样再验。

## 本页不抄

- 怎样再验、怎样填 Type、怎样解锁。
- Finalize 之后 bundled。那是不变量 403。
- locks mempool。那是不变量 588。
- calls Commit instruct persist。那是不变量 590。
- CheckTx Type / RECHECK。那是不变量 312 / 484。
- CheckTx 过了就永远有效。那是不变量 301。
