# 例：看见应用确定地执行 FinalizeBlockRequest.txs 再交还控制权不是已经交差；看见也可以套用同一块先前经 Prepare / Process 跑出的 candidate state 不是已经是 ExecuteTxState；看见同一块先前经 Prepare 或 Process 执行过不是已经不用再在 Finalize 执行

**层次**：实现 / FinalizeBlock 套用候选正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「确定执行 txs 不是已经交差 / 也可以套用 candidate state 不是已经是 ExecuteTxState / 同一块先前 Prepare 或 Process 执行过不是已经不用再在 Finalize 执行」，不是 Finalize 时的 Process 保证 bundled 三事，也不是 Finalize 执行余量 bundled 三事，也不是 ProcessProposal 候选执行那套。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把确定执行 txs、也可以套用 candidate state、同一块先前经 Prepare 或 Process 执行过写成三件独立的实现事，不是「看见 Process 跑过就已经在 Finalize 套用、已经是 ExecuteTxState、已经交差」一件事：

1. **看见应用按自己定的规则，确定地执行 `FinalizeBlockRequest.txs` 里的交易，再把控制权交还给 CometBFT / 看见先跑了 不是已经交差，也不是已经可以像 Prepare 那样依赖非确定值。**  
   官方写：The Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT。看见确定执行 txs，不是已经 Finalize + Commit 那种已经交差。看见 before returning control，不是已经 Prepare 没有确定性要求（338）那种可以像 Prepare 那样。看见按应用规则执行，不是已经 Process MAY 整块执行（452）就已经是同一句 interchangeable。
2. **看见也可以套用同一块先前经 `PrepareProposal` 或 `ProcessProposal` 跑出的 candidate state / 看见套用了 不是已经是 ExecuteTxState，也不是已经不用再回 app_hash / tx_results。**  
   官方写：Alternatively, it can apply the candidate state corresponding to the same block previously executed via `PrepareProposal` or `ProcessProposal`。看见可以套用 candidate，不是已经进 `ExecuteTxState`。看见 apply candidate state，不是已经 Process 回了 Accept 就已经换工作状态（452）。看见 Alternatively，不是已经只能重新执行 txs、不能复用候选那种已经跑过 Process 就意味着已经交差。
3. **看见同一块先前经 Prepare 或 Process 执行过 / 看见有 candidate 不是已经不用再在 Finalize 执行，也不是已经 candidate 就不需要 Commit。**  
   官方把 previously executed via PrepareProposal or ProcessProposal 和 Finalize 确定执行 txs / 套用 candidate 配成两条路。看见同一块先跑过，不是已经不用再给 `FinalizeBlockRequest.txs` 那种已经跑过 Process 就不需要 Finalize。看见有 candidate，不是已经 Finalize 改了就已经落盘（335）就已经是同一句 interchangeable。看见先前执行过，不是已经 Process 候选就已经是 ExecuteTxState（311）就已经是同一句 interchangeable。

怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存是规范里的做法，本页不抄。Finalize 时的 Process 保证（360）是至少一名非拜占庭跑过 Process / 字段再填一遍 / 可以套用候选那套另一切片，Finalize 执行余量（408）是确定执行 txs / Process 含全部信息 / Process MAY 整块执行那套另一切片，ProcessProposal 候选执行（452）是 MAY 整块执行 / candidate state / read-only 那套另一切片，本页不抄。

## 官方为什么这样拆

- **确定执行 txs ≠ 已经交差：** 官方把 before returning control 和 Finalize + Commit 分开。
- **也可以套用 candidate state ≠ 已经是 ExecuteTxState：** 官方把 apply candidate 和进 ExecuteTxState 分开。
- **同一块先前 Prepare 或 Process 执行过 ≠ 已经不用再在 Finalize 执行：** 官方把 previously executed 和已经跑过 Process 就不需要 Finalize 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 确定执行 txs | 不是已经交差 | 不是 Finalize 执行余量 bundled（408） |
| 套用 candidate state | 不是已经是 ExecuteTxState | 不是候选已经是 ExecuteTxState（311） |
| 同一块先前 Prepare / Process 执行过 | 不是已经不用再在 Finalize 执行 | 不是 Process 候选执行（452） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 跑过就已经在 Finalize 套用、已经是 ExecuteTxState、已经交差」，必须分开确定执行 txs 是不是已经交差、套用 candidate state 是不是已经是 ExecuteTxState、同一块先前 Prepare 或 Process 执行过是不是已经不用再在 Finalize 执行。可以跳过「看见有 candidate 就已经交差」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存。
- Finalize 时的 Process 保证。那是不变量 360。
- Finalize 执行余量 bundled。那是不变量 408。
- ProcessProposal 候选执行。那是不变量 452。
- 候选已经是 ExecuteTxState。那是不变量 311。
- Finalize 改了就已经落盘。那是不变量 335。
