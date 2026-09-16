# 例：看见 as a result of executing the block / 看见是执行这块的结果 不是已经 Process / Prepare candidate 就不需要再在 Finalize 执行；不是已经 apply candidate state 就不需要执行 txs；不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 已经 finasresult bundled interchangeable / 已经 466 executes block v interchangeable

**层次**：实现 / FinalizeBlock must provide values as a result of executing the block not candidate / Process already ran 正式三事（477 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「as a result of executing the block not candidate / Process already ran / not finasresult bundled（477） interchangeable / not fincand bundled（460） interchangeable / not finexecbv notcand（574） interchangeable」，不是 FinalizeBlock must provide values as a result of executing the block bundled（477），也不是 must provide values not already changed set / settled 正式三事（594 余量）。不要另写怎样编回包四列。

## 官方三件事

规范把 FinalizeBlock Usage 里 The Application must provide values for `FinalizeBlockResponse.app_hash`, `FinalizeBlockResponse.tx_results`, `FinalizeBlockResponse.validator_updates`, and `FinalizeBlockResponse.consensus_param_updates` **as a result of executing the block** 和「已经 Process / Prepare candidate 就不需要再在 Finalize 执行 interchangeable / 已经是 finasresult bundled interchangeable / 已经是 fincand bundled interchangeable」分开写成三件独立的实现事，不是「看见 as a result of executing 就已经 Process 跑过就不用再执行、已经 apply candidate interchangeable、已经 477 finasresult bundled interchangeable」一件事：

1. **看见 as a result of executing the block / 看见是执行这块的结果 / 看见 must provide values as a result of executing is not already Process / Prepare candidate 就不需要再在 Finalize 执行 interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 previously executed means no need to execute interchangeable / 已经 Process 回了 Accept（347） interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 595 notcand interchangeable / 477 finasresult interchangeable / 594 not settled interchangeable，也不是已经 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量） interchangeable / 574 notcand interchangeable / 466 executes block v interchangeable / 573 not persist interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 351 Process also on proposer interchangeable / 568 not passed means ran Process interchangeable。**  
   官方 Usage 写：must provide values … as a result of executing the block。另句写 may apply a candidate state from previous Prepare or Process calls on the same block——must provide 来自执行这块，不是已经 Process / Prepare candidate 就不需要再在 Finalize 执行 interchangeable。看见 as a result of executing，不是已经 FinalizeBlock must provide values bundled（477） interchangeable——477 另钉 must provide 四列 / 提供了值 三事，本页钉 item 2 单句。看见 executing the block，不是已经 FinalizeBlock When Application executes block v not apply candidate（574 余量） interchangeable——574 从 When executes block v 角度钉 Process already ran，本页钉 Usage as a result of executing 单句。
2. **看见 as a result of executing the block / 看见 must provide values as a result of executing is not already apply candidate state 就不需要执行 txs interchangeable / 已经套用先前候选 interchangeable / 已经 ExecuteTxState interchangeable / 已经 may apply candidate means no need to execute txs interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 595 notcand interchangeable / 477 finasresult interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460） interchangeable / 460 fincand interchangeable / 578 not no re-execute interchangeable / 577 notcandstate interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable / 408 Process whole block interchangeable。**  
   官方把 as a result of executing the block 和 Alternatively apply candidate state 配成：must provide 的值来自执行这块，或来自套用同一块先前 Prepare / Process 跑出的 candidate——但 apply candidate 不是已经不用再 provide tx_results / app_hash interchangeable。477 item 2 常与 460 / 584 混成「看见 as a result of executing 就已经 apply candidate interchangeable」，本页钉 not apply candidate not fincand bundled 单句。看见 executing the block，不是已经 Finalize 套用候选 bundled（460） interchangeable——460 另钉 execute txs / previously executed 三事，本页钉 477 item 2 边界。
3. **看见 as a result of executing the block / 看见 must provide values as a result of executing is not already Application executes block _v_ When 第 3 步 interchangeable / 466 executes block v interchangeable / 已经 persist decision interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 595 notcand interchangeable / 594 not settled interchangeable / 458 finempty interchangeable / 477 item 3 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 351 Process also on proposer interchangeable / 347 Process Accept interchangeable / 360 bundled interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 471 fincparam interchangeable / 363 finresp interchangeable。**  
   官方把 Usage as a result of executing 和 When Application executes block _v_ 分开——477 item 2 常与 466 / 351 混成「看见 executing 就已经 Application executes block v interchangeable / 已经提议者 Process 过 interchangeable」，本页钉 not 466 executes block v not 351 Process also on proposer 单句。看见 as a result of executing，不是已经 must provide not changed set / settled（594 余量） interchangeable——594 钉 item 1 边界，本页钉 item 2 单句。看见 executing the block，不是已经 empty keep current means no must provide obligation（477 item 3 余量） interchangeable——477 item 3 另钉 provided values / CheckTx，本页钉 item 2 单句。

怎样编回包四列、怎样在 Finalize 套用 candidate、怎样从 Prepare/Process 复用内存是规范里的做法，本页不抄。FinalizeBlock must provide values bundled（477）、FinalizeBlock must provide values not already changed set / settled（594 余量）、Finalize 套用候选 bundled（460）、FinalizeBlock When Application executes block v not apply candidate（574 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **as a result of executing not Process already ran ≠ finasresult bundled interchangeable：** 官方把 must provide 来自 executing the block 和 Process / Prepare candidate 就不需要再在 Finalize 执行分开。
- **as a result of executing not apply candidate ≠ fincand bundled interchangeable：** 官方把 executing the block 和 apply candidate state 就不需要执行 txs 分开。
- **as a result of executing not candidate ≠ 466 executes block v / 351 Process also on proposer：** 官方把 477 item 2 和 When executes block v / Process 也会在提议者那边叫 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| as a result of executing | 不是 already Process already ran / no need to execute | 不是 finasresult bundled（477） |
| as a result of executing | 不是 already apply candidate / no need to execute txs | 不是 Finalize 套用候选（460） |
| as a result of executing | 不是 already 466 executes block v / 351 proposer Process | 不是 must provide not settled（594） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values as a result of executing the block not candidate / Process already ran 正式三事（477 余量），必须分开 as a result of executing 是不是 already Process / Prepare candidate 就不需要再在 Finalize 执行 interchangeable / 574 notcand interchangeable / 351 Process also on proposer interchangeable、是不是 already apply candidate state 就不需要执行 txs interchangeable / 460 fincand interchangeable / 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable、是不是 already 466 executes block v / 594 not settled / 477 item 3 empty keep current interchangeable。可以跳过「看见 as a result of executing 就已经 Process 跑过就不用再执行 interchangeable」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样在 Finalize 套用 candidate、怎样从 Prepare/Process 复用内存。
- FinalizeBlock must provide values bundled。那是不变量 477。
- must provide values not already changed set / settled。那是不变量 594（477 item 1 余量）。
- Finalize 套用候选 bundled。那是不变量 460。
- FinalizeBlock When Application executes block v not apply candidate。那是不变量 574（466 item 2 余量）。
- empty keep current means no must provide obligation。那是不变量 477 item 3 余量。
