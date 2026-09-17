# 例：看见 The call is synchronous / 看见同步调用 is not already 异步 / 已经可以在返回后再改裁决 interchangeable / 已经 ProcessProposal 同步 interchangeable；不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 已经 finpersist bundled interchangeable

**层次**：实现 / FinalizeBlock When synchronous call not decides trigger / Process sync 正式三事（478 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When synchronous call not 异步 / not +2/3 precommit decides trigger / not finpersist bundled（478） interchangeable / not 607 notsync interchangeable / not 362 finwhen interchangeable / not 354 processwhen synchronous interchangeable」，不是 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478），也不是 Finalize 何时调用 bundled（362），也不是 ProcessProposal 同步 bundled（354）。不要另写怎样 persist decision、怎样写同步调用。

## 官方三件事

规范把 FinalizeBlock When 第 2 步 The call is synchronous 和「已经是 异步 / 已经可以在返回后再改裁决 interchangeable / 已经是 +2/3 precommit 决定 interchangeable / 已经是 finpersist bundled interchangeable」分开写成三件独立的实现事，不是「看见 synchronous call 就已经 异步 interchangeable、已经 +2/3 precommit 决定 interchangeable、已经 finpersist bundled interchangeable」一件事：

1. **看见 The call is synchronous / 看见同步调用 is not already 异步 / 已经可以在返回后再改裁决 interchangeable / 已经 ProcessProposal 调用是同步的、返回后不得再改裁决 interchangeable / 354 processwhen synchronous interchangeable / 354 Process 同步 interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 607 notsync interchangeable / 478 finpersist interchangeable / 354 processwhen synchronous interchangeable / 354 Process 同步 bundled interchangeable / 517 processwhen status interchangeable，也不是已经 ProcessProposal 调用是同步的 bundled（354 余量） interchangeable / 354 processwhen synchronous interchangeable / 351 Process also on proposer interchangeable / 360 Process guarantee interchangeable，也不是已经 PrepareProposal 调用是同步的 bundled（338 余量） interchangeable / 338 Prepare nondet interchangeable / 354 processwhen synchronous interchangeable / 505 preparewhen collect interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable。**  
   官方 When 第 2 步写：The call is synchronous。看见同步，不是已经 异步 / 已经可以在返回后再改裁决 interchangeable——478 bundled 第三件事常被写成「看见 synchronous 就已经 Process 同步 interchangeable」，本页从 478 item 3 侧钉 not Process sync 单句。看见 The call is synchronous，不是已经 ProcessProposal 调用是同步的、返回后不得再改裁决（354） interchangeable——354 钉 Process 同步，本页钉 Finalize 同步 call 第一件事。看见同步调用，不是已经 Prepare 没有确定性要求（338）那种已经 interchangeable——338 钉 Prepare nondet，本页钉 478 item 3 单句。
2. **看见 synchronous call / 看见 The call is synchronous is not already +2/3 precommit 同一 id(v) 才决定再调 Finalize interchangeable / 已经 decides block 触发条件 interchangeable / 362 +2/3 precommit interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 607 notsync interchangeable / 478 finpersist interchangeable / 362 finwhen bundled interchangeable / 362 item 3 synchronous call interchangeable / 605 notpersist interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen bundled interchangeable / 362 item 1 +2/3 precommit interchangeable / 362 item 2 persist decision interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 362 decides trigger interchangeable / 479 fintrigger interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit bundled（479 余量） interchangeable / 479 fintrigger interchangeable / 362 +2/3 precommit interchangeable / 466 executes block v interchangeable。**  
   官方把 The call is synchronous 和 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362）分开——478 item 3 常与 362 混成「看见 synchronous call 就已经 +2/3 precommit 决定 interchangeable」，本页钉 not decides trigger 单句。看见 synchronous call，不是已经 When trigger 2f+1 precommit（479） interchangeable——479 钉 Proposal / block parts / precommit 三事，本页钉 478 item 3 第二件事。看见 The call is synchronous，不是已经 calls FinalizeBlock with _v_'s data（606 / 478 item 2） interchangeable——606 另钉 not persist outputs / not decides trigger 从 calls 侧钉，本页从 sync call 侧钉 not decides trigger 单句。
3. **看见 synchronous call / 看见 The call is synchronous is not already finpersist bundled（478） interchangeable / 已经 persist decision interchangeable / 已经 calls FinalizeBlock interchangeable / 478 finpersist item 1 interchangeable / 478 finpersist item 2 interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 607 notsync interchangeable / 605 notpersist interchangeable / 606 notoutputs interchangeable / 466 executes block v interchangeable，也不是已经 FinalizeBlock When persist decision not executes block v bundled（605 余量） interchangeable / 605 notpersist interchangeable / 572 not execbv interchangeable / 33 four gates interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen interchangeable / 362 item 1 +2/3 precommit interchangeable / 362 item 2 persist decision interchangeable。**  
   官方把 478 finpersist bundled 三事里的 synchronous call 和 persist decision / calls FinalizeBlock / decides trigger 分开——478 bundled 常与 item 1 / item 2 混成「看见 synchronous call 就已经 finpersist bundled interchangeable」，本页钉 478 item 3 第三件事。看见 The call is synchronous，不是已经 persist decision（605 / 478 item 1 余量） interchangeable——605 另钉 not executes block v / not 交差，本页钉 item 3 单句。看见 synchronous call，不是已经 calls FinalizeBlock（606 / 478 item 2 余量） interchangeable——606 另钉 not persist outputs / not decides trigger 从 calls 侧钉，本页钉 not finpersist bundled 单句。

怎样 persist decision、怎样写同步调用、怎样在 When 里决定再调 Finalize 是规范里的做法，本页不抄。FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478）、persist decision not executes block v（605 / 478 item 1）、calls FinalizeBlock not persist outputs（606 / 478 item 2）、Finalize 何时调用 bundled（362）、ProcessProposal 同步 bundled（354）是另外那套，本页不抄。

## 官方为什么这样拆

- **synchronous call not Process sync ≠ 354 processwhen synchronous interchangeable：** 官方把 Finalize 同步 call 和 ProcessProposal 同步分开。
- **synchronous call not decides trigger ≠ 362 finwhen / 479 fintrigger interchangeable：** 官方把 478 item 3 和 +2/3 precommit 决定 / When trigger 分开。
- **synchronous call not finpersist bundled ≠ persist decision / calls FinalizeBlock interchangeable：** 官方把 478 item 3 和 item 1 / item 2 / 605 / 606 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| synchronous call | 不是 already Process sync / 异步 | 不是 Process 同步 bundled（354） |
| synchronous call | 不是 already decides trigger | 不是 finwhen bundled（362） |
| synchronous call | 不是 already finpersist bundled | 不是 persist decision（605 / 478 item 1） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When synchronous call not decides trigger / Process sync 正式三事（478 余量），必须分开 synchronous call 是不是 already 异步 / ProcessProposal 同步 interchangeable / 354 processwhen synchronous interchangeable / 338 Prepare nondet interchangeable、synchronous call 是不是 already +2/3 precommit 决定 interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable / 606 notoutputs interchangeable、synchronous call 是不是 already finpersist bundled interchangeable / 605 notpersist interchangeable / 606 notoutputs interchangeable / 466 executes block v interchangeable。可以跳过「看见 synchronous call 就已经 +2/3 precommit 决定 interchangeable」。不要另写怎样 persist decision。

## 本页不抄

- 怎样 persist decision、怎样写同步调用、怎样在 When 里决定再调 Finalize。
- FinalizeBlock When persist decision / synchronous call 正式三事 bundled。那是不变量 478。
- persist decision not executes block v。那是不变量 605（478 item 1 余量）。
- calls FinalizeBlock not persist outputs。那是不变量 606（478 item 2 余量）。
- Finalize 何时调用 bundled。那是不变量 362。
- ProcessProposal 同步 bundled。那是不变量 354。
