# 例：看见 Application executes txs deterministically before returning control is not already like Prepare / not findet bundled（470） interchangeable / not fincand committed interchangeable

**层次**：实现 / executes txs deterministically not like Prepare 正式三事（470 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「executes txs deterministically not like Prepare / not findet bundled（470） interchangeable / not fincand committed interchangeable」，不是 FinalizeBlock Usage determinism 正式三事（470），也不是 FinalizeBlock 套用候选 bundled（460）。不要另写怎样测确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 executes txs deterministically before returning control 和「已经可以像 Prepare 那样 / fincand bundled interchangeable / 460 committed interchangeable」分开写成三件独立的实现事，不是「看见 Usage 写了 deterministically 就已经可以像 Prepare 那样 interchangeable、已经套用 candidate 就不需要再执行 interchangeable、已经 findet bundled interchangeable」一件事：

1. **看见 Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT / 看见 executes txs deterministically is not already like Prepare / can depend on nondeterministic values interchangeable / 看见确定执行 is not already Prepare 没有确定性要求 bundled（338 余量） interchangeable / 已经 ExtendVote 没有确定性要求 interchangeable / 已经两边 raw 一样 interchangeable，也不是已经 FinalizeBlock Usage determinism 正式三事 bundled（470） interchangeable / 已经 findet bundled interchangeable / 已经 app_hash MUST be deterministic interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（407 余量） interchangeable / 已经 state machine replication interchangeable / 已经 implementation MUST be deterministic interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（408 余量） interchangeable / 已经 Process 含全部信息 interchangeable / 已经 Process MAY 整块执行 interchangeable，也不是已经 PrepareProposal 没有确定性要求 bundled（338 余量） interchangeable / 已经 raw proposal interchangeable / 已经 can modify this set interchangeable。**  
   官方 Usage 写 executes txs deterministically before returning control to CometBFT。看见 deterministically，不是已经 Prepare 没有确定性要求（338） interchangeable——338 钉 Prepare 可以不确定，本页钉 470 item 1 not like Prepare 单句。看见 according to application rules，不是已经 Finalize 实现必须确定 not like Prepare（407 余量） interchangeable——574 钉 implementation 单句，本页钉 executes txs 单句。看见 before returning control，不是已经 FinalizeBlock 确定执行 txs（408 余量） interchangeable——408 钉 finexec bundled，本页钉 470 executes txs 边界。
2. **看见 executes txs deterministically before returning control is not already apply candidate / previously executed means no need to execute txs interchangeable / 看见确定执行 is not already FinalizeBlock 套用候选 bundled（460） interchangeable / 已经套用 candidate 就不需要再执行 interchangeable / 已经 previously executed interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（460 第二件事 / 577 余量） interchangeable / 已经 ExecuteTxState interchangeable / 已经 Process ACCEPT switched interchangeable，也不是已经 previously executed not no re-execute bundled（460 第三件事 / 578 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 guarantee satisfied interchangeable / 已经 previously executed via Prepare or Process interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable。**  
   官方把 executes txs deterministically 和 Alternatively apply candidate state / previously executed 两条路分开——470 bundled item 1 常与 460 混成「看见 deterministically 就已经套用 candidate 就不需要再执行 interchangeable」，本页钉 executes txs not apply candidate / previously executed 单句。看见 deterministically execute txs，不是已经 apply candidate not ExecuteTxState（577 余量） interchangeable——577 钉 apply candidate 单句，本页钉 executes txs 边界。看见 before returning control，不是已经 previously executed not no re-execute（578 余量） interchangeable——578 钉 item 3 边界，本页钉 470 item 1 单句。
3. **看见 executes txs deterministically before returning control is not already committed / Finalize + Commit 交差 interchangeable / 看见确定执行 is not already executes txs deterministically not already committed bundled（460 第一件事 / 576 余量） interchangeable / 已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable，也不是已经 FinalizeBlock Usage determinism 正式三事 bundled（470） interchangeable / 已经 findet bundled interchangeable / 已经 app_hash MUST be deterministic interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 persist decision interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 ProcessProposal MAY fully execute not already committed bundled（543 余量） interchangeable / 已经 MAY execute not committed interchangeable / 已经是 ExecuteTxState interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460） interchangeable / 已经 before returning control interchangeable / 已经 findet item 2/3 interchangeable。**  
   官方把 executes txs deterministically 和 before returning control 已经交差分开——470 bundled item 1 常与 576 混成「看见 deterministically 就已经 committed interchangeable」，本页钉 executes txs not committed 单句（从 findet 角度）。看见 deterministically，不是已经 executes txs not committed（576 余量） interchangeable——576 钉 460 item 1 边界，本页钉 470 findet 单句。看见 before returning control，不是已经 Finalize + Commit 那种已经交差 interchangeable——460 / 576 各钉 committed 边界，本页钉 findet item 1 第三件事。

怎样写 FinalizeBlock、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。app_hash MUST be deterministic not 印进本头（580 余量）、implementation MUST be deterministic not Req 11–12（581 余量）、FinalizeBlock Usage determinism 正式三事（470）是另外那套，本页不抄。

## 官方为什么这样拆

- **executes txs deterministically not like Prepare ≠ findet bundled interchangeable：** 官方把 Finalize 执行确定性和 Prepare 可以不确定分开。
- **executes txs deterministically not apply candidate / previously executed ≠ fincand item 2/3 interchangeable：** 官方把 execute txs 路和 apply candidate / previously executed 路分开。
- **executes txs deterministically not committed ≠ 576 / 460 committed interchangeable：** 官方把 findet executes txs 和 committed 交差分开（从 findet 角度钉边界）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| executes txs deterministically | 不是 already like Prepare | 不是 Prepare 没有确定性要求（338） |
| executes txs deterministically | 不是 already apply candidate / previously executed | 不是 Finalize 套用候选 item 2/3（577/578） |
| executes txs deterministically | 不是 already committed | 不是 executes txs not committed（576） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 executes txs deterministically not like Prepare 正式三事（470 余量），必须分开 executes txs 是不是 already like Prepare interchangeable / 470 findet interchangeable / 338 Prepare nondet interchangeable、executes txs 是不是 already apply candidate / previously executed interchangeable / 577 apply candidate interchangeable / 578 not no re-execute interchangeable、executes txs 是不是 already committed interchangeable / 576 not committed interchangeable / 460 fincand interchangeable。可以跳过「看见 Usage 写了 deterministically 就已经可以像 Prepare 那样 interchangeable」。不要另写怎样测确定性。

## 本页不抄

- 怎样写 FinalizeBlock、怎样测确定性、怎样写测试向量。
- app_hash MUST be deterministic not 印进本头。那是不变量 580（470 item 2 余量）。
- implementation MUST be deterministic not Req 11–12。那是不变量 581（470 item 3 余量）。
- FinalizeBlock Usage determinism 正式三事。那是不变量 470。
