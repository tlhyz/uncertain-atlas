# 例：看见 CometBFT locks the mempool 不是已经交差；看见 no calls to CheckTx on new transactions 不是已经 CheckTx 技术上可选 / 已经进池；看见 locks mempool after persist 不是已经是 Commit 锁 / 已经解锁 / 已经是 Recheck

**层次**：实现 / FinalizeBlock When locks mempool 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「CometBFT locks the mempool 不是已经交差 / no calls to CheckTx on new transactions 不是已经 CheckTx 技术上可选 / 已经进池 / locks mempool after persist 不是已经是 Commit 锁 / 已经解锁 / 已经是 Recheck」，不是 Finalize 之后 bundled 三事，也不是 Commit 前上锁 bundled，也不是 CheckTx Type bundled。不要另写怎样锁内存池、怎样再验、怎样解锁。

## 官方三件事

规范把 When 第 7 步 CometBFT locks the mempool — no calls to `CheckTx` on new transactions 写成三件独立的实现事，不是「看见锁了内存池就已经交差、已经不能再收新交易、已经是 Commit 锁 / 已经 Recheck」一件事：

1. **看见 CometBFT locks the mempool / 看见引擎锁内存池 不是已经交差，也不是已经四门已经结算。**  
   官方 When 第 7 步写：_p_'s CometBFT locks the mempool。发生在 When 第 6 步 persist tx outputs / AppHash / ResultsHash 之后、第 8 步 `Commit` 之前。看见锁了，不是已经 Finalize + Commit 那种已经交差（33）。看见 When 第 7 步，不是已经 CometBFT persists 这三份（587）那种已经 Commit 落盘应用状态 interchangeable。看见锁内存池，不是已经 Finalize 之后 bundled（403）那种落完就锁 / 已经交差 interchangeable——本页只钉 When 第 7 步，不抄 403 整包。
2. **看见 no calls to `CheckTx` on new transactions / 看见新交易不再进 CheckTx 不是已经 CheckTx 技术上可选 / 不参与处理块，也不是已经进了池 / 已经开始流言。**  
   官方 When 第 7 步写：no calls to `CheckTx` on new transactions。看见新交易不进 CheckTx，不是已经 CheckTx technically optional — not involved in processing blocks（373）那种可选 interchangeable。看见锁住期间不接新 CheckTx，不是已经 Check 通过就是已进提案（33）。看见 no calls on **new** transactions，不是已经池里旧交易也不能再验——第 9 步 optional recheck 是另一步（403 item 3），不是本步。
3. **看见 locks mempool after persist / 看见 persist 之后才锁 不是已经是 Commit 锁，也不是已经解锁 / 已经是 Recheck。**  
   官方把 When 第 7 步锁内存池和 When 第 8 步 `Commit`、第 9–10 步 optional recheck / unlock 分开写。看见锁了，不是已经默认全局锁那种 Commit 前上锁、Commit 里等广播会停死（310）。看见 When 第 7 步，不是已经 unlocks the mempool（403 item 3）就已经是同一句 interchangeable。看见锁内存池，不是已经 `CheckTx` 的 `Type` 标明 `RECHECK`（312）就已经是同一句 interchangeable。

怎样锁内存池、怎样再验池里剩下的、怎样解锁是规范里的做法，本页不抄。Finalize 之后 bundled（403）是落完锁内存池 / Commit / Recheck 那套另一切片，Commit 前上锁（310）是默认锁 / Commit 前上锁 / Commit 里等广播那套另一切片，CheckTx Type（312）是 RECHECK vs NEW 那套另一切片，CheckTx 技术上可选（373）是 optional / not involved in blocks 那套另一切片，CometBFT persists 这三份（587）是 When 第 6 步那套另一切片，本页不抄。

## 官方为什么这样拆

- **CometBFT locks the mempool ≠ 已经交差 / 已经四门已经结算：** 官方把 When 第 7 步锁内存池和 Finalize + Commit 交差分开。
- **no calls to CheckTx on new transactions ≠ 已经 CheckTx 技术上可选 / 已经进池：** 官方把锁住期间不接新 CheckTx 和 CheckTx optional / 池门分开。
- **locks mempool after persist ≠ 已经是 Commit 锁 / 已经解锁 / 已经是 Recheck：** 官方把 When 第 7 步锁和 Commit RPC 锁、unlock、Recheck 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CometBFT locks the mempool | 不是已经交差 | 不是四门已经结算（33） |
| no calls to CheckTx on new transactions | 不是已经 CheckTx 技术上可选 | 不是 CheckTx optional（373） |
| locks mempool after persist | 不是已经是 Commit 锁 | 不是 Commit 前上锁（310） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见锁了内存池就已经交差、已经不能再收新交易、已经是 Commit 锁 / 已经 Recheck」，必须分开 CometBFT locks the mempool 是不是已经交差、no calls to CheckTx on new transactions 是不是已经 CheckTx 技术上可选 / 已经进池、locks mempool after persist 是不是已经是 Commit 锁 / 已经解锁 / 已经是 Recheck。可以跳过「看见锁了就已经交差」。不要另写怎样锁内存池。

## 本页不抄

- 怎样锁内存池、怎样再验池里剩下的、怎样解锁。
- Finalize 之后 bundled 三事。那是不变量 403。
- Commit 前上锁就已经解锁。那是不变量 310。
- RECHECK 就已经是新交易。那是不变量 312。
- CheckTx 技术上可选。那是不变量 373。
- CometBFT persists 这三份。那是不变量 587。
