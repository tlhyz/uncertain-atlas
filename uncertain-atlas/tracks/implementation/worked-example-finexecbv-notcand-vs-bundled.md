# 例：看见 Application executes block _v_ / execute according to FinalizeBlockRequest.txs is not already same block already ran means no need to execute / Process already ran means don't execute / not FinalizeBlock When Application executes block v bundled（466） interchangeable / not apply candidate state not ExecuteTxState bundled（584） interchangeable

**层次**：实现 / FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When Application executes block v not apply candidate / Process already ran / not FinalizeBlock When Application executes block v bundled（466） interchangeable / not apply candidate state not ExecuteTxState bundled（584） interchangeable」，不是 FinalizeBlock When Application executes block v bundled（466），也不是 FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（573 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock When 第 3 步 Application executes block _v_ / Usage 里 execute according to `FinalizeBlockRequest.txs` / may apply a candidate state from previous Prepare or Process 和「已经 Process 跑过就不执行 interchangeable / 已经套用先前候选 interchangeable / 已经是 FinalizeBlock When Application executes block v bundled interchangeable」分开写成三件独立的实现事，不是「看见 Application executes block _v_ 就已经 Process 跑过就不执行 interchangeable、已经 apply candidate interchangeable、已经 466 finexecbv bundled interchangeable」一件事：

1. **看见 Application executes block _v_ / execute according to `FinalizeBlockRequest.txs` is not already same block already ran means no need to execute / Process already ran means don't execute / 看见按 txs 执行 is not already FinalizeBlock When Application executes block v bundled（466） interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 previously executed interchangeable / 已经套用先前候选 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经已经是 ExecuteTxState interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable，也不是已经 FinalizeBlock When Application executes block v not persist decision bundled（573 余量） interchangeable / 573 not persist interchangeable / 572 not execbv interchangeable / 362 +2/3 precommit interchangeable。**  
   官方 Usage 写：The application determines execution from `FinalizeBlockRequest.txs`。When 写：Application executes block _v_。看见 execute according to txs，不是已经 Process 跑过就不执行 interchangeable——466 item 2 常被写成「看见同一块先跑过就已经不用再执行 interchangeable」，本页钉 executes block v not Process already ran 单句。看见 executes block _v_，不是已经 FinalizeBlock When Application executes block v（466） interchangeable——466 另钉 not persist decision / not +2/3 precommit 三事，本页钉 item 2 边界。看见按 txs 执行，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 at least one / refill bundled，本页钉 finexecbv notcand 单句。
2. **看见 Application executes block _v_ is not already apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 看见 may apply candidate from previous Prepare or Process is not already ExecuteTxState / already previously executed interchangeable / 已经套用先前候选 interchangeable / 已经内存里有状态 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466） interchangeable / 574 not cand interchangeable / 466 executes block v interchangeable / 573 not persist interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经已经是 ExecuteTxState interchangeable / 582 not every validator interchangeable，也不是已经 candidate state is ExecuteTxState bundled（311 余量） interchangeable / 311 candidate is ExecuteTxState interchangeable / 408 Process whole block interchangeable / 583 not refill interchangeable。**  
   官方 Usage 写：The application may apply a candidate state from previous Prepare or Process calls on the same block。看见 may apply candidate，不是已经 ExecuteTxState interchangeable——466 item 2 常与 584 混成「看见 Application executes block _v_ 就已经是 apply candidate interchangeable」，本页钉 not apply candidate not 584 bundled 单句。看见 executes block _v_，不是已经 apply candidate state not ExecuteTxState（584 余量） interchangeable——584 从 360 item 3 角度钉 apply candidate 三事，本页钉 466 item 2 单句。看见 can apply candidate state，不是已经 candidate state is ExecuteTxState（311 余量） interchangeable——311 钉立刻执行出候选边界，本页钉 finexecbv notcand 单句。
3. **看见 Application executes block _v_ is not already Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 看见 execute according to txs is not already Process 也会在提议者那边叫 interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable / 已经提议者 Process 过就代表已经跑过 Process interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466） interchangeable / 574 not cand interchangeable / 466 executes block v interchangeable / 573 not persist interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable，也不是已经 Process can execute whole block like Finalize bundled（408 余量） interchangeable / 408 Process whole block interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。**  
   官方把 execute according to txs 和 Process 也会在提议者那边叫 分开——466 item 2 常与 351 混成「看见 Process 跑过就不执行 interchangeable / 已经提议者 Process 过 interchangeable」，本页钉 not Process already ran not 351 Process also on proposer 单句。看见 executes block _v_，不是已经 Process can execute whole block like Finalize（408 余量） interchangeable——408 钉整块跑边界，本页钉 466 item 2 第三件事。看见 may apply candidate，不是已经 even if already passed（568 余量） interchangeable——568 钉 473 item 2 边界，本页钉 finexecbv notcand 单句。

怎样写 Finalize、怎样缓存 candidate、怎样从 Prepare/Process 复用内存是规范里的做法，本页不抄。FinalizeBlock When Application executes block v bundled（466）、apply candidate state not ExecuteTxState 正式三事（584 余量）、FinalizeBlock When Application executes block v not persist decision 正式三事（573 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **executes block v not Process already ran / apply candidate ≠ FinalizeBlock When Application executes block v bundled interchangeable：** 官方把 execute according to txs / Application executes block _v_ 和 Process 跑过就不执行分开。
- **executes block v not apply candidate / Process already ran ≠ apply candidate state not ExecuteTxState bundled interchangeable：** 官方把 Application executes block _v_ 和 may apply candidate / ExecuteTxState 分开。
- **executes block v not Process already ran / apply candidate ≠ 351 Process also on proposer interchangeable：** 官方把 466 item 2 和 Process 也会在提议者那边叫 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application executes block v | 不是 already Process already ran / no need to execute | 不是 FinalizeBlock When Application executes block v bundled（466） |
| Application executes block v | 不是 already apply candidate / ExecuteTxState | 不是 apply candidate state not ExecuteTxState（584） |
| Application executes block v | 不是 already Process also on proposer means ran Process | 不是 Process 也会在提议者那边叫（351） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量），必须分开 executes block v 是不是 already Process already ran / no need to execute interchangeable / 466 finexecbv interchangeable / 573 not persist interchangeable / 362 +2/3 precommit interchangeable、executes block v 是不是 already apply candidate / ExecuteTxState interchangeable / 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable / 408 Process whole block interchangeable、executes block v 是不是 already Process also on proposer means ran Process interchangeable / 351 Process also on proposer interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。可以跳过「看见 Application executes block _v_ 就已经 Process 跑过就不执行 interchangeable」。不要另写怎样缓存 candidate。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样从 Prepare/Process 复用内存。
- Application executes block v not persist decision / When calling guarantee。那是不变量 573（466 item 1 余量）。
- Application executes block v not +2/3 precommit decided / ResultHash。那是不变量 362 / 466 item 3 余量。
- FinalizeBlock When Application executes block v bundled 三事。那是不变量 466。
- apply candidate state not ExecuteTxState 正式三事（360 余量）。那是不变量 584。
