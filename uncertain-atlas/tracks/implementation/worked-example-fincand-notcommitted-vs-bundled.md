# 例：看见 Application executes txs deterministically before returning control is not already committed / not fincand bundled（460） interchangeable / not findet bundled（470） interchangeable

**层次**：实现 / executes txs deterministically not already committed 正式三事（460 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「executes txs deterministically not already committed / not fincand bundled（460） interchangeable / not findet bundled（470） interchangeable」，不是 FinalizeBlock 套用候选 bundled（460），也不是 FinalizeBlock Usage determinism 正式三事（470）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 FinalizeBlock Usage 里 executes txs deterministically before returning control 和「已经交差 / 已经可以像 Prepare 那样 / fincand bundled interchangeable」分开写成三件独立的实现事，不是「看见确定执行 txs 就已经交差 interchangeable、已经像 Prepare 那样 interchangeable、已经 fincand bundled interchangeable」一件事：

1. **看见 Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT / 看见确定执行 txs is not already committed / Finalize + Commit 交差 interchangeable / 看见 before returning control is not already FinalizeBlock 套用候选 bundled（460） interchangeable / 已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable，也不是已经 FinalizeBlock Usage determinism 正式三事 bundled（470 第一件事） interchangeable / 已经 executes txs deterministically interchangeable / 已经 findet bundled interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 immediate execution 交差 interchangeable / 已经 Finalize + Commit interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（407 余量） interchangeable / 已经像 Prepare 那样 interchangeable / 已经 Prepare 没有确定性要求 interchangeable，也不是已经 FinalizeBlock 套用候选 not apply candidate bundled（460 第三件事 / 578 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 previously executed interchangeable。**  
   官方 Usage 写 executes txs deterministically before returning control to CometBFT。看见 before returning control，不是已经 Finalize + Commit 那种已经交差——460 bundled 第一件事常被写成「看见确定执行 txs 就已经交差」，本页钉 executes txs not already committed 单句。看见 deterministically，不是已经 Prepare 没有确定性要求（338） interchangeable——338 钉 Prepare 可以不确定，本页钉 460 item 1 边界。看见 executes txs，不是已经 FinalizeBlock Usage determinism（470 第一件事） interchangeable——470 另钉 findet 三事，本页钉 460 套用候选 item 1 单句。
2. **看见 executes txs deterministically is not already like Prepare / can depend on nondeterministic values interchangeable / 看见确定执行 is not already Prepare 没有确定性要求 bundled（338 余量） interchangeable / 已经 ExtendVote 没有确定性要求 interchangeable / 已经两边 raw 一样 interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（407 余量） interchangeable / 已经 state machine replication interchangeable / 已经 findet bundled interchangeable，也不是已经 FinalizeBlock 套用候选 not apply candidate state bundled（460 第二件事 / 577 余量） interchangeable / 已经 ExecuteTxState interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（408 余量） interchangeable / 已经 Process 含全部信息 interchangeable / 已经 Process MAY 整块执行 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 persist decision interchangeable / 已经 Process 跑过就不执行 interchangeable。**  
   官方把 Finalize 确定执行 txs 和 Prepare 可以依赖非确定值分开——460 bundled 常与 338 / 407 混成「看见 deterministically 就已经可以像 Prepare 那样 interchangeable」，本页钉 executes txs not like Prepare 单句。看见 according to application rules，不是已经 Finalize 实现必须确定（407 余量） interchangeable——407 钉 implementation must be deterministic，本页钉 executes txs 单句。看见 before returning control，不是已经 apply candidate state（577 余量） interchangeable——577 钉 candidate 单句，本页钉 460 item 1 边界。
3. **看见 executes txs deterministically before returning control is not already apply candidate / previously executed means no need to execute txs interchangeable / 看见确定执行 is not already FinalizeBlock 套用候选 bundled（460） interchangeable / 已经套用 candidate 就不需要再执行 interchangeable / 已经 previously executed interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 guarantee satisfied interchangeable / 已经 previously executed via Prepare or Process interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable，也不是已经 FinalizeBlock 套用候选 not apply candidate state bundled（460 第二件事 / 577 余量） interchangeable / 已经 ExecuteTxState interchangeable / 已经 Process ACCEPT switched interchangeable，也不是已经 FinalizeBlock 套用候选 not no re-execute bundled（460 第三件事 / 578 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable。**  
   官方把 executes txs deterministically 和 Alternatively apply candidate state / previously executed 两条路分开——460 bundled 三事常被写成「看见 Process 跑过就已经不用再 execute txs interchangeable」，本页钉 executes txs not apply candidate / previously executed 单句。看见 before returning control，不是已经 has run not apply candidate（572 余量） interchangeable——572 钉 472 guarantee 边界，本页钉 460 executes txs 单句。看见 deterministically execute txs，不是已经 Contains all information not executed（546 余量） interchangeable——546 钉 Process 含全部信息 ≠ 已经执行，本页钉 460 item 1 边界。

怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样测确定性是规范里的做法，本页不抄。FinalizeBlock 套用候选 apply candidate state（577 余量）、previously executed not no re-execute（578 余量）、FinalizeBlock Usage determinism 正式三事（470）是另外那套，本页不抄。

## 官方为什么这样拆

- **executes txs deterministically not already committed ≠ fincand bundled interchangeable：** 官方把 before returning control 和 Finalize + Commit 交差分开。
- **executes txs deterministically not like Prepare ≠ Prepare nondet interchangeable：** 官方把 Finalize 确定执行和 Prepare 可以不确定分开。
- **executes txs deterministically not apply candidate / previously executed ≠ fincand item 2/3 interchangeable：** 官方把 execute txs 路和 apply candidate / previously executed 路分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| executes txs deterministically | 不是 already committed | 不是 Finalize + Commit 交差 |
| executes txs deterministically | 不是 already like Prepare | 不是 Prepare 没有确定性要求（338） |
| executes txs deterministically | 不是 already apply candidate / previously executed | 不是 Finalize 套用候选 item 2/3（577/578） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 executes txs deterministically not already committed 正式三事（460 余量），必须分开 executes txs 是不是 already committed interchangeable / 460 bundled interchangeable / 470 findet interchangeable、executes txs 是不是 already like Prepare interchangeable / 338 Prepare nondet interchangeable / 407 finfields interchangeable、executes txs 是不是 already apply candidate / previously executed interchangeable / 572 has run not apply candidate interchangeable / 578 not no re-execute interchangeable。可以跳过「看见确定执行 txs 就已经交差 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样测确定性。
- apply candidate state not ExecuteTxState。那是不变量 577（460 item 2 余量）。
- previously executed not no re-execute in Finalize。那是不变量 578（460 item 3 余量）。
- FinalizeBlock 套用候选 bundled 三事。那是不变量 460。
- FinalizeBlock Usage determinism 正式三事。那是不变量 470。
