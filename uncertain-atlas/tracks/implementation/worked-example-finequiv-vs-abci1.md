# 例：看见 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 不是已经是四门已经结算；看见收成一门不是已经没有 Prepare/Process；看见等价于旧三步不是已经是 Contains the fields of the newly decided block / 已经 Process 跑过就不用在 Finalize 再执行

**层次**：实现 / FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 不是已经是四门已经结算 / 收成一门不是已经没有 Prepare/Process / 等价于旧三步不是已经是含刚决定那块的字段」，不是 Finalize 回包义务 bundled 三事，也不是四门已经结算 bundled，也不是 Finalize 含刚决定那块字段 bundled。不要另写怎样写 Finalize 回包、怎样映射旧三步。

## 官方三件事

规范把 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock`、ABCI++ 仍保留 Prepare/Process 等门、Finalize 仍要在块决定后执行写成三件独立的实现事，不是「看见收成一门就已经是四门已经结算、已经没有 Prepare/Process、已经 Process 跑过就不用在 Finalize 再执行」一件事：

1. **看见 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 不是已经是四门已经结算，也不是已经交差。**  
   官方写：This method is equivalent to the call sequence `BeginBlock`, `DeliverTx`, and `EndBlock` in ABCI 1.0。看见等价于旧三步，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了（33）。看见收成一门，不是已经交差。看见 Finalize 被调用，不是已经 Process 回了 Accept 就已经是同一句 interchangeable。
2. **看见等价于旧三步 / 看见收成一门 不是已经没有 Prepare/Process，也不是已经 ABCI++ 只剩 Finalize 一门 interchangeable。**  
   官方把 Finalize 收成 ABCI 1.0 那三步，和 ABCI++ 另设 Prepare / Process 门分开写。看见 BeginBlock/DeliverTx/EndBlock 在 Finalize 里，不是已经没有 PrepareProposal / ProcessProposal。看见收成一门，不是已经 CheckTx 过了就可以跳过 Prepare / Process。看见旧三步语义在 Finalize，不是已经可以把 Prepare / Process 当成可有可无 interchangeable。
3. **看见等价于旧三步 / 看见收成一门 不是已经是 Contains the fields of the newly decided block interchangeable，也不是已经 Process 跑过 / 已经有 candidate 就不用在 Finalize 再执行。**  
   官方另写：Contains the fields of the newly decided block；executes the transactions in FinalizeBlockRequest.txs deterministically before returning control；Alternatively, it can apply the candidate state corresponding to the same block previously executed via PrepareProposal or ProcessProposal。看见等价，不是已经含刚决定那块的字段就等于已经跑过 Process（461）。看见收成一门，不是已经 Process 整块执行过就不需要再在 Finalize 执行（460）。看见旧三步在 Finalize，不是已经 Prepare / Process 传过字段就够 interchangeable。

怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock、怎样在 Finalize 套用 candidate 是规范里的做法，本页不抄。Finalize 回包义务 bundled（363）是 decided_last_commit 定奖惩 / 必须回四列那套另一切片，四门已经结算（33）是 Finalize + Commit 才进提交状态那套另一切片，Finalize 含刚决定那块字段 bundled（461）是 newly decided block 字段那套另一切片，Finalize 套用候选（460）是 execute txs / apply candidate 那套另一切片，本页不抄。

## 官方为什么这样拆

- **等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算 / 已经交差：** 官方把收成一门和 ABCI++ 四门齐了分开。
- **等价于旧三步 ≠ 已经没有 Prepare/Process：** 官方把 Finalize 里的旧语义和 ABCI++ 另设的门分开。
- **等价于旧三步 ≠ 已经是含刚决定那块的字段 / 已经 Process 就不需要 Finalize：** 官方把历史映射和 Finalize 仍要执行的义务分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock | 不是已经是四门已经结算 | 不是四门已经结算（33） |
| 收成一门 | 不是已经没有 Prepare/Process | 不是 Finalize 回包义务 bundled（363） |
| 等价于旧三步 | 不是已经是含刚决定那块的字段 | 不是 Finalize 含刚决定那块字段（461） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收成一门就已经是四门已经结算、已经没有 Prepare/Process、已经 Process 跑过就不用在 Finalize 再执行」，必须分开 equiv 是不是已经四门已经结算、是不是已经没有 Prepare/Process、是不是已经是含刚决定那块的字段 / 已经 Process 就不需要 Finalize。可以跳过「看见收成一门就已经是四门已经结算」。不要另写怎样写 Finalize 回包。

## 本页不抄

- 怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock、怎样在 Finalize 套用 candidate。
- Finalize 回包义务 bundled 三事。那是不变量 363。
- 四门已经结算。那是不变量 33。
- Finalize 含刚决定那块字段 bundled 三事。那是不变量 461。
- Finalize 套用候选。那是不变量 460。
- CheckTx 技术上可选。那是不变量 373。
