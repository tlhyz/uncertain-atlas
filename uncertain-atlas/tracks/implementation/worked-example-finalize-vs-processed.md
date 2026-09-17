# 例：看见引擎保证至少一名非拜占庭验证者对这块跑过 Process 不是已经每个验证者都跑过 Process；看见 Finalize 请求把字段再填一遍不是已经不用再给；看见可以套用先前 Prepare / Process 的候选不是已经是 ExecuteTxState

**层次**：实现 / Finalize 时的 Process 保证。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「引擎保证至少一名非拜占庭验证者对这块跑过 Process 不是已经每个验证者都跑过 Process / Finalize 请求把字段再填一遍不是已经不用再给 / 可以套用先前 Prepare / Process 的候选不是已经是 ExecuteTxState」，不是 Process 也会在提议者那边叫，也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。不要另写怎样写 Finalize。

## 官方三件事

规范把决定一块时至少一名非拜占庭验证者跑过 Process、Finalize 请求仍把字段再填一遍、可以套用先前候选写成三件独立的实现事，不是「看见要 Finalize 了就已经每个验证者都跑过 Process、已经不用再给、已经是 ExecuteTxState」一件事：

1. **看见引擎保证至少一名非拜占庭验证者对这块跑过 Process / 看见要 Finalize 了 不是已经每个验证者都跑过 Process，也不是已经是提议者那边也会叫 Process。**  
   官方写：调用 `FinalizeBlock` 时，共识算法保证至少一名非拜占庭验证者对这块跑过 `ProcessProposal`。看见要 Finalize 了，不是已经每个验证者都跑过。看见有保证，不是已经是提议者那边也会叫。看见至少一名，不是已经交差。
2. **看见 Finalize 请求把字段再填一遍 / 看见 Prepare / Process 已经给过 不是已经不用再给，也不是已经跑过 Process。**  
   官方写：目前 CometBFT 会把 `FinalizeBlockRequest` 的字段填满，哪怕这些字段已经经 `PrepareProposalRequest` 或 `ProcessProposalRequest` 给过应用。看见再填一遍，不是已经不用再给。看见字段名对得上，不是已经跑过 Process。看见请求齐了，不是已经交差。
3. **看见可以套用先前 Prepare / Process 的候选 / 看见同一块先跑过 不是已经是 ExecuteTxState，也不是已经交差。**  
   官方写：应用按 `FinalizeBlockRequest.txs` 确定执行；也可以套用先前经 Prepare 或 Process 对同一块跑出的候选。看见可以套用，不是已经是 ExecuteTxState。看见同一块先跑过，不是已经交差。看见有候选，不是已经落盘。

怎样写 Finalize、怎样缓存候选、怎样再填字段是规范里的做法，本页不抄。Process 也会在提议者那边叫是不变量 351，本页不抄。

## 官方为什么这样拆

- **至少一名非拜占庭验证者跑过 Process ≠ 已经每个验证者都跑过 Process：** 官方把至少一名和每个都跑过分开。
- **Finalize 请求把字段再填一遍 ≠ 已经不用再给：** 官方把再填一遍和已经给过分开。
- **可以套用先前候选 ≠ 已经是 ExecuteTxState：** 官方把可以套用和已经是工作状态分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 至少一名非拜占庭验证者跑过 Process | 不是已经每个验证者都跑过 Process | 不是 Process 也会在提议者那边叫就已经不用再 Process（351） |
| Finalize 请求把字段再填一遍 | 不是已经不用再给 | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 可以套用先前候选 | 不是已经是 ExecuteTxState | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见要 Finalize 了就已经每个验证者都跑过 Process、已经不用再给、已经是 ExecuteTxState」，必须分开至少一名非拜占庭验证者跑过 Process 是不是已经每个验证者都跑过 Process、Finalize 请求把字段再填一遍是不是已经不用再给、可以套用先前候选是不是已经是 ExecuteTxState。可以跳过「看见要 Finalize 了就已经每个验证者都跑过 Process」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存候选、怎样再填字段。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- 候选已经是 ExecuteTxState。那是不变量 311。
