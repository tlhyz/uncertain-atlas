# 例：看见 Application executes block _v_ 不是已经 persist decision / When calling guarantee；看见 executes block _v_ 不是已经 Process 跑过就不执行 / apply candidate；看见 executes block _v_ 不是已经 +2/3 precommit 决定 / ResultHash

**层次**：实现 / FinalizeBlock When Application executes block v。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When Application executes block v / not already persist decision / When calling guarantee / not Process already ran means don't execute / apply candidate / not +2/3 precommit decided / ResultHash」，不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472），也不是 apply candidate state not ExecuteTxState 正式三事（584 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock When 第 3 步 Application executes block _v_ / Usage 里 execute according to `FinalizeBlockRequest.txs` / may apply candidate state from previous Prepare or Process 和「已经 persist decision interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 +2/3 precommit decided interchangeable」分开写成三件独立的实现事，不是「看见 Application executes block _v_ 就已经 persist decision interchangeable、已经 apply candidate interchangeable、已经 ResultHash interchangeable」一件事：

1. **看见 Application executes block _v_ / 看见 When 第 3 步 executes block _v_ is not already persist decision / When calling / consensus guarantees means Application executes block v / 看见执行了 is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经 persist decision interchangeable / 已经把块落成这一高的决定 interchangeable / 已经 When calling guarantee interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经字段再填一遍 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 When calling guarantee not executes block v / persist decision bundled（572 余量） interchangeable / 572 not execbv interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 362 +2/3 precommit interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable。**  
   官方 When 写：Application executes block _v_。Usage 把 When 第 3 步和 When calling guarantee 分开——466 bundled 第一件事常被写成「看见 Application executes block _v_ 就已经 persist decision interchangeable」，本页钉 executes block v not persist decision / When calling guarantee 单句。看见 executes block _v_，不是已经 FinalizeBlock When calling ProcessProposal guarantee（472） interchangeable——472 另钉 not every validator / not proposer 三事，本页钉 finexecbv item 1 边界。看见 When 第 3 步，不是已经 When calling guarantee not executes block v（572 余量） interchangeable——572 从 472 item 3 角度钉 not executes block v 单句，本页钉 466 bundled 三事。
2. **看见 Application executes block _v_ / execute according to `FinalizeBlockRequest.txs` is not already same block already ran means no need to execute / Process already ran means don't execute / 看见按 txs 执行 is not already apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 previously executed interchangeable / 已经套用先前候选 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经已经是 ExecuteTxState interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 FinalizeBlock When Application executes block v not apply candidate bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 583 not refill interchangeable / 311 candidate is ExecuteTxState interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 351 Process also on proposer interchangeable / 408 Process whole block interchangeable。**  
   官方 Usage 写：The application determines execution from `FinalizeBlockRequest.txs`；The application may apply a candidate state from previous Prepare or Process calls on the same block。看见 executes block _v_，不是已经 Process 跑过就不执行 interchangeable——466 bundled 第二件事常与 584 混成「看见同一块先跑过就已经不用再执行 interchangeable」，本页钉 executes block v not apply candidate / Process already ran 单句。看见 execute according to txs，不是已经 apply candidate state not ExecuteTxState（584 余量） interchangeable——584 从 360 item 3 角度钉 apply candidate 三事，本页钉 finexecbv item 2 单句。看见 may apply candidate，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉 proposer path，本页钉 finexecbv 边界。
3. **看见 Application executes block _v_ / 应用回了 AppHash 和各笔输出 is not already +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 看见执行了 is not already +2/3 precommit decided interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable / 已经 ResultHash interchangeable / 已经印进本头 interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 572 not execbv interchangeable / 570 not every validator interchangeable / 466 executes block v interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经 persist decision interchangeable / 584 apply candidate interchangeable，也不是已经 FinalizeBlock persist decision not committed bundled（335 余量） interchangeable / 335 finpersist interchangeable / 576 fincand committed interchangeable / 147 apphash vs this block interchangeable。**  
   官方 When 把 +2/3 precommit 决定再调 Finalize、Application executes block _v_、引擎哈希进 ResultHash 分开——466 bundled 第三件事「看见 Application executes block _v_ 就已经 ResultHash interchangeable」常与 362 混成一件事，本页钉 executes block v not +2/3 precommit decided / ResultHash 单句。看见 executes block _v_，不是已经 +2/3 precommit same id(v)（362 余量） interchangeable——362 另钉 When 流程 precommit 路径，本页钉 finexecbv item 3 边界。看见回了 AppHash，不是已经本头 AppHash 就已经是本高度交差（147 余量） interchangeable——147 钉 AppHash 边界，本页钉 finexecbv 单句。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径是规范里的做法，本页不抄。FinalizeBlock When calling ProcessProposal guarantee bundled（472）、apply candidate state not ExecuteTxState 正式三事（584 余量）、+2/3 precommit 同一 id(v) 才决定再调 Finalize（362）是另外那套，本页不抄。

## 官方为什么这样拆

- **Application executes block v not persist decision / When calling guarantee ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 When 第 3 步 executes block _v_ 和 Usage When calling guarantee 分开。
- **Application executes block v not apply candidate / Process already ran ≠ apply candidate state not ExecuteTxState bundled interchangeable：** 官方把 executes block _v_ 和 may apply candidate / Process 跑过就不执行分开。
- **Application executes block v not +2/3 precommit decided / ResultHash ≠ +2/3 precommit same id(v) already will Finalize bundled interchangeable：** 官方把 Application executes block _v_ 和 When 流程 precommit 决定 / ResultHash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application executes block v | 不是 already persist decision / When calling guarantee | 不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472） |
| Application executes block v | 不是 already Process already ran / apply candidate | 不是 apply candidate state not ExecuteTxState（584） |
| Application executes block v | 不是 already +2/3 precommit decided / ResultHash | 不是 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v，必须分开 executes block v 是不是 already persist decision / When calling guarantee interchangeable / 472 finwhen interchangeable / 572 not execbv interchangeable、executes block v 是不是 already Process already ran / apply candidate interchangeable / 584 apply candidate interchangeable / 351 Process also on proposer interchangeable、executes block v 是不是 already +2/3 precommit decided / ResultHash interchangeable / 362 +2/3 precommit interchangeable / 335 finpersist interchangeable / 147 apphash vs this block interchangeable。可以跳过「看见 Application executes block _v_ 就已经 persist decision interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- When calling guarantee not executes block v / persist decision。那是不变量 572（472 item 3 余量）。
- apply candidate state not ExecuteTxState 单句边界。那是不变量 584（360 item 3 余量）。
- +2/3 precommit 同一 id(v) 才决定再调 Finalize 三事。那是不变量 362。
