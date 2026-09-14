# 例：看见 application may apply a candidate state from previous Prepare or Process is not already ExecuteTxState / not Finalize 时的 Process 保证 bundled（360） interchangeable / not same block already ran means no need to execute interchangeable

**层次**：实现 / apply candidate state not ExecuteTxState 正式三事（360 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「apply candidate state not ExecuteTxState / not Finalize 时的 Process 保证 bundled（360） interchangeable / not same block already ran means no need to execute interchangeable」，不是 Finalize 时的 Process 保证 bundled（360），也不是候选已经是 ExecuteTxState（311 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 application may apply a candidate state from previous Prepare or Process / execute according to `FinalizeBlockRequest.txs` / can reuse memory from same block 和「已经套用先前候选 interchangeable / 已经是 ExecuteTxState interchangeable / 已经交差 interchangeable」分开写成三件独立的实现事，不是「看见可以套用先前 Prepare / Process 的候选就已经是 ExecuteTxState interchangeable、已经同一块先跑过 interchangeable、已经交差 interchangeable」一件事：

1. **看见 application may apply a candidate state from previous Prepare or Process / 看见可以套用先前候选 is not already ExecuteTxState / already previously executed interchangeable / 看见可以套用 is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经已经是 ExecuteTxState interchangeable / 已经 previously executed interchangeable，也不是已经 candidate state is ExecuteTxState bundled（311 余量） interchangeable / 已经立刻执行出候选 interchangeable / 已经内存里有状态 interchangeable，也不是已经 Process can execute whole block like Finalize bundled（408 余量） interchangeable / 已经整块跑了 interchangeable / 已经像 Finalize 那样执行 interchangeable，也不是已经 at least one non-byzantine ran Process not every validator bundled（582 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 persist decision interchangeable。**  
   官方 Usage 写：The application may apply a candidate state from previous Prepare or Process calls on the same block。看见 may apply candidate，不是已经 ExecuteTxState interchangeable——360 bundled 第三件事常被写成「看见可以套用先前候选就已经是 ExecuteTxState interchangeable」，本页钉 apply candidate not ExecuteTxState 单句。看见 can apply candidate state，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 at least one / refill bundled，本页钉 item 3 边界。看见 from previous Prepare or Process，不是已经 candidate state is ExecuteTxState（311 余量） interchangeable——311 钉立刻执行出候选边界，本页钉 360 item 3 单句。
2. **看见 execute according to `FinalizeBlockRequest.txs` / application determines execution from txs is not already same block already ran means no need to execute / 看见按 txs 执行 is not already Process already ran means don't execute bundled（466 余量） interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 previously executed interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经套用先前候选 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 executes block v interchangeable / 已经 persist decision interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable。**  
   官方把 may apply candidate 和 execute according to txs 分开——360 bundled 第三件事常与 466 混成「看见同一块先跑过就已经 Process 跑过就不执行 interchangeable」，本页钉 apply candidate not same block already ran means no need to execute 单句。看见 determines execution from txs，不是已经 Application executes block _v_（466 余量） interchangeable——466 When 流程另钉 executes block _v_ 三事，本页钉 360 item 3 单句。看见 may apply candidate，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉 proposer path，本页钉 apply candidate 边界。
3. **看见 can apply candidate / reuse memory state from same block is not already committed / settled interchangeable / 看见套用候选 is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473 余量） interchangeable / 已经不用再 Finalize interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 newly decided block fields interchangeable，也不是已经 FinalizeBlock persist decision not committed bundled（335 余量） interchangeable / 已经必须在 Commit 落盘 interchangeable / 已经改了状态 interchangeable。**  
   官方把 can apply candidate 和 already committed 分开——360 bundled 第三件事第三句「看见同一块先跑过，不是已经交差」常被写成 335 / 576 bundled interchangeable，本页钉 apply candidate not already committed 单句。看见 reuse memory state，不是已经 Finalize + Commit 那种已经交差 interchangeable——335 / 576 各钉 committed 边界，本页钉 360 item 3 第三件事。看见 may apply candidate，不是已经 Finalize 请求把字段再填一遍（583 余量） interchangeable——583 钉 refill 边界，本页钉 apply candidate 单句。

怎样写 Finalize、怎样缓存 candidate、怎样从 Prepare/Process 复用内存是规范里的做法，本页不抄。at least one non-byzantine ran Process not every validator（582 余量）、Finalize 请求把字段再填一遍 not no need to provide again（583 余量）、Finalize 时的 Process 保证 bundled（360）是另外那套，本页不抄。

## 官方为什么这样拆

- **apply candidate not ExecuteTxState ≠ Finalize 时的 Process 保证 bundled interchangeable：** 官方把 may apply candidate 和已经是 ExecuteTxState 分开。
- **apply candidate not same block already ran means no need to execute ≠ executes block v / Process already ran interchangeable：** 官方把 can apply candidate 和 Process 跑过就不执行分开。
- **apply candidate not already committed ≠ finpersist / finfields bundled interchangeable：** 官方把套用候选和已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| apply candidate from Prepare/Process | 不是 already ExecuteTxState | 不是 Finalize 时的 Process 保证 bundled（360） |
| same block already ran | 不是 already no need to execute at Finalize | 不是 FinalizeBlock When Application executes block v（466） |
| can apply candidate | 不是 already committed / settled | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 apply candidate state not ExecuteTxState 正式三事（360 余量），必须分开 apply candidate 是不是 already ExecuteTxState interchangeable / 360 bundled interchangeable / 311 candidate is ExecuteTxState interchangeable、apply candidate 是不是 already same block already ran means no need to execute interchangeable / 466 executes block v interchangeable / 351 Process also on proposer interchangeable、apply candidate 是不是 already committed interchangeable / 335 finpersist interchangeable / 583 refill interchangeable。可以跳过「看见可以套用先前候选就已经是 ExecuteTxState interchangeable」。不要另写怎样缓存 candidate。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样从 Prepare/Process 复用内存。
- at least one non-byzantine ran Process not every validator。那是不变量 582（360 item 1 余量）。
- Finalize 请求把字段再填一遍不是已经不用再给。那是不变量 583（360 item 2 余量）。
- Finalize 时的 Process 保证 bundled 三事。那是不变量 360。
- 候选已经是 ExecuteTxState。那是不变量 311。
