# 例：看见 starts consensus for height h+1 不是已经交差 / 已经四门已经结算；看见 round 0 不是已经继续同一 round / 已经 next_block_delay 槽位 / 已经 timeout_commit；看见 When 第 11 步 after unlock 不是已经 unlocks mempool / 已经 Finalize 之后 bundled / 已经 When trigger 2f+1 precommit

**层次**：实现 / FinalizeBlock When starts consensus for h+1 round 0 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 11。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「starts consensus for height h+1 不是已经交差 / 已经 persist decision / round 0 不是已经继续同一 round / 已经 next_block_delay / timeout_commit / When 第 11 步 after unlock 不是已经 unlock mempool / 已经 Finalize 之后 bundled / 已经 When trigger 2f+1 precommit」，不是 Finalize 之后 bundled 三事，不是 next_block_delay 非确定 bundled，也不是 When trigger Proposal parts bundled。不要另写怎样开下一高、怎样等 delay、怎样进 round 0。

## 官方三件事

规范把 When 第 11 步 _p_ starts consensus for height _h+1_, round 0 写成三件独立的实现事，不是「看见开下一高了就已经交差、已经是 round 0、已经 unlock 之后 interchangeable」一件事：

1. **看见 starts consensus for height _h+1_ / 看见 When 第 11 步开下一高 不是已经交差 / 已经四门已经结算，也不是已经 persist decision interchangeable。**  
   官方 When 第 11 步写：_p_ starts consensus for height _h+1_, round 0。发生在 When 第 10 步 unlocks the mempool 之后。看见 starts consensus for height h+1，不是已经 Finalize + Commit 交差（33）。看见 When 第 11 步，不是已经 _p_ persists _v_ as the decision for height _h_（478 第 1 步）就已经是同一句 interchangeable——478 钉 When 第 1 步 persist decision，本页钉 When 第 11 步开下一高。
2. **看见 round 0 / 看见 round 0 不是已经继续同一 round _r_ / 已经换轮，也不是已经 `FinalizeBlockResponse.next_block_delay` 槽位 / 已经 `timeout_commit` interchangeable。**  
   官方 When 第 11 步写：starts consensus for height _h+1_, **round 0**。看见 round 0，不是已经同一高度换轮（302）那种还在高度 _h_ interchangeable——302 钉同高换轮，本页钉下一高 round 0。看见开下一高，不是已经 `next_block_delay` Deterministic = No / 各节点 MAY 不同（589） interchangeable。看见 round 0，不是已经 processing time / more precommits / `timeout_commit`（480） interchangeable。
3. **看见 When 第 11 步 after unlock / 看见 unlock 之后才开下一高 不是已经 unlocks the mempool（592），也不是已经 Finalize 之后 bundled（403）第三件事 recheck+unlock+h+1 整包 interchangeable。**  
   官方把 When 第 10 步 unlocks the mempool、第 11 步 starts consensus for height _h+1_, round 0 分开写。看见 When 第 11 步，不是已经 unlocks the mempool（592）就已经是同一句 interchangeable——592 钉 When 第 10 步解锁，本页钉 When 第 11 步开下一高。看见 starts consensus，不是已经 Finalize 之后 bundled（403）第三件事整包 interchangeable——403 另钉 Finalize 之后 recheck+unlock+h+1，本页只钉 When 第 11 步。看见开下一高 round 0，不是已经 When trigger Proposal block parts 2f+1 precommit decides _v_（479） interchangeable——479 钉 When 前导触发，本页钉 When 第 11 步收尾。

怎样开下一高、怎样等 delay、怎样进 round 0 是规范里的做法，本页不抄。Finalize 之后 bundled（403）是落完锁 / Commit / optional recheck / unlock / h+1 那套另一切片，unlocks mempool（592）是 When 第 10 步 newly received can now be checked 那套另一切片，next_block_delay 非确定（589）是 Response 表 Deterministic = No 那套另一切片，processing time / timeout_commit（480）是 Usage next_block_delay 那套另一切片，When trigger 2f+1 precommit（479）是 When 前导 Proposal parts 那套另一切片，persist decision（478）是 When 第 1 步那套另一切片，本页不抄。

## 官方为什么这样拆

- **starts consensus for height h+1 ≠ 已经交差 / 已经 persist decision：** 官方把 When 第 11 步开下一高和 Finalize + Commit 交差、persist decision 分开。
- **round 0 ≠ 已经继续同一 round / 已经 next_block_delay / timeout_commit：** 官方把 round 0、同高换轮、next_block_delay、timeout_commit 分开。
- **When 第 11 步 after unlock ≠ 已经 unlock mempool / 已经 Finalize 之后 bundled / 已经 When trigger：** 官方把 When 第 11 步开下一高和 unlock、Finalize 之后 bundled、When 前导 trigger 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| starts consensus for height h+1 | 不是已经交差 | 不是 persist decision（478） |
| round 0 | 不是已经继续同一 round | 不是 next_block_delay（589） |
| When 第 11 步 after unlock | 不是已经 unlock mempool | 不是 Finalize 之后 bundled（403） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见开下一高了就已经交差、已经是 round 0、已经 unlock 之后 interchangeable」，必须分开 starts consensus for height h+1 是不是已经交差 / 已经 persist decision、round 0 是不是已经继续同一 round / 已经 next_block_delay / timeout_commit、When 第 11 步 after unlock 是不是已经 unlocks the mempool / 已经 Finalize 之后 bundled / 已经 When trigger 2f+1 precommit。可以跳过「看见开下一高就已经交差」。不要另写怎样开下一高。

## 本页不抄

- 怎样开下一高、怎样等 delay、怎样进 round 0。
- Finalize 之后 bundled。那是不变量 403。
- unlocks mempool。那是不变量 592。
- next_block_delay 非确定。那是不变量 589。
- processing time / timeout_commit。那是不变量 480。
- When trigger 2f+1 precommit。那是不变量 479。
- persist decision。那是不变量 478。
