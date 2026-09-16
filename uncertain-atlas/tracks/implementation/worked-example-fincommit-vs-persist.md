# 例：看见 CometBFT calls Commit to instruct the Application to persist its state 不是已经交差；看见 instruct Application to persist its state 不是已经引擎 persist tx outputs / AppHash / ResultsHash；看见 When 第 8 步 calls Commit after lock mempool 不是已经是 Commit 锁 / 已经 Commit Usage signal bundled

**层次**：实现 / FinalizeBlock When calls Commit instruct persist 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 8。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「CometBFT calls Commit to instruct persist 不是已经交差 / instruct Application to persist its state 不是已经引擎 persist 这三份 / When 第 8 步 calls Commit after lock mempool 不是已经是 Commit 锁 / 已经 Commit Usage signal bundled」，不是 Finalize 落盘禁令 bundled，不是 Commit Usage persist signal bundled，也不是 Finalize 之后 bundled。不要另写怎样落盘、怎样写 Commit。

## 官方三件事

规范把 When 第 8 步 _p_'s CometBFT calls `Commit` to instruct the Application to persist its state 写成三件独立的实现事，不是「看见 When 第 8 步叫了 Commit 就已经交差、已经在 Finalize 落了、已经在引擎 persist 这三份 interchangeable」一件事：

1. **看见 CometBFT calls `Commit` / 看见 When 第 8 步叫 Commit 不是已经交差，也不是已经四门已经结算。**  
   官方 When 第 8 步写：_p_'s CometBFT calls `Commit`。发生在 When 第 7 步 locks the mempool 之后、第 9 步 optional recheck 之前。看见 calls Commit，不是已经 Finalize + Commit 那种已经交差（33）。看见 When 第 8 步，不是已经 Finalize 改了就已经落盘（335） interchangeable。看见引擎叫 Commit，不是已经 CometBFT persists tx outputs / AppHash / ResultsHash（587）那种引擎落这三份 interchangeable。
2. **看见 to instruct the Application to persist its state / 看见 instruct Application to persist its state 不是已经引擎 persist tx outputs / AppHash / ResultsHash，也不是已经 Commit Usage Signal persist bundled interchangeable。**  
   官方 When 第 8 步写：calls `Commit` **to instruct the Application to persist its state**。看见 instruct persist，不是已经 CometBFT persists the transaction outputs, _AppHash_, and _ResultsHash_（587）。看见 Application to persist its state，不是已经 Signal the Application to persist application state（481） Usage 那句就已经是同一句 interchangeable——481 钉 Commit Usage persist signal，本页钉 When 第 8 步 instruct persist。看见 persist its state，不是已经 Finalize MUST NOT persist / MUST persist in Commit（335） Usage 禁令 interchangeable——335 钉 app requirements 禁令，本页钉 When 调用时机。
3. **看见 When 第 8 步 calls Commit after lock mempool / 看见 lock 之后才 Commit 不是已经是 Commit 锁，也不是已经 optional recheck / unlock / 已经是 Recheck interchangeable。**  
   官方把 When 第 7 步 locks the mempool、第 8 步 calls Commit、第 9–10 步 optional recheck / unlock 分开写。看见 When 第 8 步，不是已经 locks mempool（588）就已经是同一句 interchangeable。看见 calls Commit after lock，不是已经 Commit 前上锁、Commit 里等广播会停死（310）。看见 instruct persist，不是已经 Finalize 之后 bundled（403）那种落完锁内存池 / Commit / Recheck 整包 interchangeable——403 另钉 Finalize 之后，本页只钉 When 第 8 步。

怎样落盘、怎样写 Commit、怎样 optional recheck 是规范里的做法，本页不抄。Finalize 落盘禁令（335）是 Finalize MUST NOT persist / MUST persist in Commit / remember last Commit height 那套另一切片，Commit Usage persist signal（481）是 Signal persist / expected at end of this call / Historical blocks 那套另一切片，CometBFT persists 这三份（587）是 When 第 6 步那套另一切片，locks mempool（588）是 When 第 7 步那套另一切片，Finalize 之后 bundled（403）是落完锁 / Commit / Recheck 那套另一切片，Commit 空请求（399）是 Commit 不带参数那套另一切片，本页不抄。

## 官方为什么这样拆

- **CometBFT calls Commit ≠ 已经交差 / 已经在 Finalize 落了 / 已经引擎 persist 这三份：** 官方把 When 第 8 步 calls Commit 和交差、Finalize 禁令、引擎 persist 分开。
- **instruct Application to persist its state ≠ 已经引擎 persist 这三份 / 已经 Commit Usage signal bundled：** 官方把 When instruct persist 和引擎 persist 这三份、Commit Usage signal 分开。
- **When 第 8 步 calls Commit after lock mempool ≠ 已经是 Commit 锁 / 已经 recheck / unlock：** 官方把 When 第 8 步 Commit 和 Commit 锁、optional recheck、unlock 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CometBFT calls Commit | 不是已经交差 | 不是四门已经结算（33） |
| instruct Application to persist its state | 不是已经引擎 persist 这三份 | 不是 CometBFT persists（587） |
| When 第 8 步 calls Commit after lock mempool | 不是已经是 Commit 锁 | 不是 locks mempool（588） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 When 第 8 步叫了 Commit 就已经交差、已经在 Finalize 落了、已经在引擎 persist 这三份 interchangeable」，必须分开 CometBFT calls Commit 是不是已经交差、instruct Application to persist its state 是不是已经引擎 persist 这三份 / 已经 Commit Usage signal bundled、When 第 8 步 calls Commit after lock mempool 是不是已经是 Commit 锁 / 已经 recheck / unlock。可以跳过「看见叫了 Commit 就已经交差」。不要另写怎样落盘。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样 optional recheck。
- Finalize 落盘禁令。那是不变量 335。
- Commit Usage persist signal bundled。那是不变量 481。
- CometBFT persists 这三份。那是不变量 587。
- locks mempool。那是不变量 588。
- Finalize 之后 bundled。那是不变量 403。
- Commit 空请求。那是不变量 399。
