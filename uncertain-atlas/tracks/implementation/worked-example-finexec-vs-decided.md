# 例：看见 Application executes block v 不是已经把 v 落成这一高的决定；看见应用执行块 v 不是已经每个验证者都跑过 Process / 已经是 ExecuteTxState；看见执行块 v 不是已经套用 candidate 就不需要再在 Finalize 执行

**层次**：实现 / FinalizeBlock When Application executes block v 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「Application executes block v 不是已经把 v 落成这一高的决定 / 不是已经每个验证者都跑过 Process / 已经是 ExecuteTxState / 不是已经套用 candidate 就不需要再在 Finalize 执行」，不是 Finalize 何时调用 bundled 三事，也不是 Finalize 套用候选 bundled 三事，也不是 Finalize 时的 Process 保证 bundled 三事。不要另写怎样写 Finalize When 流程、怎样实现 candidate 缓存。

## 官方三件事

规范把 When 第 3 步 Application executes block _v_、和前面 persist decision / 同步调 Finalize、以及后面 calculate AppHash / 套用 candidate 分开写成三件独立的实现事，不是「看见调了 Finalize 就已经执行完、已经每个验证者都跑过 Process、已经 Process 跑过就不用在 Finalize 再执行」一件事：

1. **看见 `_p_`'s Application executes block _v_ / 看见应用执行块 _v_ 不是已经把 _v_ 落成这一高的决定，也不是已经交差。**  
   官方 When 写：1. _p_ persists _v_ as the decision for height _h_。2. _p_'s CometBFT calls `FinalizeBlock` with _v_'s data. The call is synchronous。3. _p_'s Application executes block _v_。看见 executes block _v_，不是已经 persist decision 那种已经决定。看见执行块，不是已经同步调 Finalize 那种已经交差。看见 When 第 3 步，不是已经 +2/3 precommit 同一 id(v) 那种已经会调 Finalize interchangeable（362）。
2. **看见 Application executes block _v_ / 看见应用执行块 _v_ 不是已经每个验证者都跑过 Process，也不是已经是 ExecuteTxState。**  
   官方 Usage 另写：When calling `FinalizeBlock` with a block, the consensus algorithm guarantees that at least one non-byzantine validator has run `ProcessProposal` on that block。看见 executes block _v_，不是已经每个验证者都跑过 Process（360）。看见 When 里应用执行，不是已经 Process MAY 整块执行（452）就已经是同一句 interchangeable。看见执行块，不是已经进 `ExecuteTxState`（311）。
3. **看见 Application executes block _v_ / 看见应用执行块 _v_ 不是已经套用 candidate 就不需要再在 Finalize 执行，也不是已经 Process 跑过就不用在 Finalize 再执行。**  
   官方 Usage 写：The Application executes the transactions in `FinalizeBlockRequest.txs` deterministically；Alternatively, it can apply the candidate state corresponding to the same block previously executed via `PrepareProposal` or `ProcessProposal`。看见 When 第 3 步 executes block _v_，不是已经 previously executed 就不需要 Finalize 那种已经跑过 Process（460）。看见执行块，不是已经 apply candidate 就已经交差 interchangeable。看见 executes block _v_，不是已经 determine txs / apply candidate 就可以混成「已经 Process 跑过就不执行」 interchangeable。

怎样写 Finalize When 流程、怎样实现 candidate 缓存、怎样在 Finalize 套用 candidate 是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）是 +2/3 precommit / persist decision / AppHash ResultHash 那套另一切片，Finalize 套用候选（460）是 execute txs / apply candidate / previously executed 那套另一切片，Finalize 时的 Process 保证（360）是至少一名非拜占庭跑过 Process / 字段再填一遍那套另一切片，本页不抄。

## 官方为什么这样拆

- **Application executes block v ≠ 已经把 v 落成这一高的决定 / 已经交差：** 官方把 persist decision / 同步调 Finalize 和 executes block _v_ 分开。
- **Application executes block v ≠ 已经每个验证者都跑过 Process / 已经是 ExecuteTxState：** 官方把 When 第 3 步和 Process 保证 / candidate 执行分开。
- **Application executes block v ≠ 已经套用 candidate 就不需要再在 Finalize 执行：** 官方把 executes block _v_ 和 previously executed / apply candidate 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application executes block v | 不是已经把 v 落成这一高的决定 | 不是 Finalize 何时调用 bundled（362） |
| Application executes block v | 不是已经每个验证者都跑过 Process | 不是 Finalize 时的 Process 保证（360） |
| Application executes block v | 不是已经套用 candidate 就不需要再在 Finalize 执行 | 不是 Finalize 套用候选（460） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见调了 Finalize 就已经执行完、已经每个验证者都跑过 Process、已经 Process 跑过就不用在 Finalize 再执行」，必须分开 executes block v 是不是已经把 v 落成这一高的决定、是不是已经每个验证者都跑过 Process / 已经是 ExecuteTxState，是不是已经套用 candidate 就不需要再在 Finalize 执行。可以跳过「看见 persist decision 就已经执行完」。不要另写怎样写 Finalize When 流程。

## 本页不抄

- 怎样写 Finalize When 流程、怎样 persist decision、怎样实现 candidate 缓存。
- Finalize 何时调用 bundled 三事。那是不变量 362。
- Finalize 套用候选。那是不变量 460。
- Finalize 时的 Process 保证。那是不变量 360。
- ProcessProposal 候选执行。那是不变量 452。
- Finalize 改了就已经落盘。那是不变量 335。
