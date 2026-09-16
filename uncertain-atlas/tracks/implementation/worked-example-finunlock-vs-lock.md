# 例：看见 unlocks the mempool 不是已经交差；看见 newly received transactions can now be checked 不是已经 optional recheck / 已经 CheckTx 技术上可选；看见 When 第 10 步 unlock after optional recheck 不是已经 locks mempool / 已经开下一高 round 0

**层次**：实现 / FinalizeBlock When unlocks mempool 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 10。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「unlocks the mempool 不是已经交差 / newly received transactions can now be checked 不是已经 optional recheck / 已经 CheckTx 技术上可选 / When 第 10 步 unlock after optional recheck 不是已经 locks mempool / 已经开下一高 round 0」，不是 Finalize 之后 bundled 三事，不是 locks mempool bundled，也不是 optional recheck bundled。不要另写怎样解锁、怎样再验、怎样开下一高。

## 官方三件事

规范把 When 第 10 步 unlocks the mempool — newly received transactions can now be checked 写成三件独立的实现事，不是「看见解锁了就已经交差、已经能收新交易、已经开下一高 interchangeable」一件事：

1. **看见 unlocks the mempool / 看见 When 第 10 步解锁内存池 不是已经交差，也不是已经四门已经结算。**  
   官方 When 第 10 步写：_p_'s CometBFT unlocks the mempool。发生在 When 第 9 步 optional recheck 之后、第 11 步 starts consensus for height _h+1_, round 0 之前。看见 unlocks，不是已经 Finalize + Commit 交差（33）。看见 When 第 10 步，不是已经 locks the mempool（588）就已经是同一句 interchangeable——588 钉 When 第 7 步锁，本页钉 When 第 10 步解锁。
2. **看见 newly received transactions can now be checked / 看见新收到的交易现在可以 CheckTx 不是已经 optional recheck outstanding txs，也不是已经 CheckTx 技术上可选 / 不参与处理块。**  
   官方 When 第 10 步写：newly received transactions **can now be checked**。看见 can now be checked，不是已经 optionally re-checks all **outstanding** transactions in the mempool（591）那种再验池里剩下的 interchangeable。看见 **newly received**，不是已经 no calls to CheckTx on new transactions（588）那种锁住期间不接新 CheckTx interchangeable——588 钉锁，本页钉解锁后能接。看见现在可以 CheckTx，不是已经 CheckTx technically optional — not involved in processing blocks（373） interchangeable。
3. **看见 When 第 10 步 unlock after optional recheck / 看见 unlock 之后才开下一高 不是已经是 Commit 锁解锁，也不是已经 starts consensus for h+1 round 0 interchangeable。**  
   官方把 When 第 9 步 optional recheck、第 10 步 unlocks the mempool、第 11 步 starts consensus for height _h+1_, round 0 分开写。看见 When 第 10 步，不是已经 Commit 前上锁、Commit 里等广播会停死（310）那种 Commit RPC 锁 interchangeable。看见 unlock，不是已经 Finalize 之后 bundled（403）第三件事 recheck+unlock+h+1 整包 interchangeable——403 另钉 Finalize 之后，本页只钉 When 第 10 步。看见解锁，不是已经开下一高 round 0（step 11）就已经是同一句 interchangeable。

怎样解锁、怎样再验、怎样开下一高是规范里的做法，本页不抄。locks mempool（588）是 When 第 7 步 no new CheckTx 那套另一切片，optional recheck（591）是 When 第 9 步 outstanding vs newly persisted 那套另一切片，calls Commit instruct persist（590）是 When 第 8 步那套另一切片，Finalize 之后 bundled（403）是 recheck+unlock+h+1 那套另一切片，Commit 前上锁（310）是默认锁 / Commit 里等广播那套另一切片，CheckTx 技术上可选（373）是 optional / not involved in blocks 那套另一切片，本页不抄。

## 官方为什么这样拆

- **unlocks the mempool ≠ 已经交差 / 已经四门已经结算：** 官方把 When 第 10 步解锁和 Finalize + Commit 交差分开。
- **newly received transactions can now be checked ≠ 已经 optional recheck / 已经 CheckTx 技术上可选：** 官方把新交易现在可以 CheckTx 和 optional recheck outstanding、CheckTx optional 分开。
- **When 第 10 步 unlock after optional recheck ≠ 已经是 Commit 锁解锁 / 已经开下一高 round 0：** 官方把 When 第 10 步 unlock 和 Commit RPC 锁、step 11 开下一高分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| unlocks the mempool | 不是已经交差 | 不是 locks mempool（588） |
| newly received transactions can now be checked | 不是已经 optional recheck | 不是 optional recheck（591） |
| When 第 10 步 unlock after optional recheck | 不是已经开下一高 round 0 | 不是 Finalize 之后 bundled（403） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见解锁了就已经交差、已经能收新交易、已经开下一高 interchangeable」，必须分开 unlocks the mempool 是不是已经交差、newly received transactions can now be checked 是不是已经 optional recheck / 已经 CheckTx 技术上可选、When 第 10 步 unlock after optional recheck 是不是已经是 Commit 锁解锁 / 已经开下一高 round 0。可以跳过「看见解锁了就已经交差」。不要另写怎样解锁。

## 本页不抄

- 怎样解锁、怎样再验、怎样开下一高。
- locks mempool。那是不变量 588。
- optional recheck。那是不变量 591。
- calls Commit instruct persist。那是不变量 590。
- Finalize 之后 bundled。那是不变量 403。
- Commit 前上锁。那是不变量 310。
- CheckTx 技术上可选。那是不变量 373。
