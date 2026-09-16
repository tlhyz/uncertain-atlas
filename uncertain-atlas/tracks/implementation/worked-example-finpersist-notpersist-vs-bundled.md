# 例：看见 _p_ persists _v_ as the decision for height _h_ / 看见把 _v_ 落成这一高的决定 is not already Application executes block _v_ interchangeable / 已经 executes block v interchangeable；不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 已经 finpersist bundled interchangeable

**层次**：实现 / FinalizeBlock When persist decision not executes block v / 已经交差 正式三事（478 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 1。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When persist decision not executes block v / not 已经交差 / not finpersist bundled（478） interchangeable / not 605 notpersist interchangeable / not 466 executes block v interchangeable / not 572 not execbv interchangeable」，不是 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478），也不是 Application executes block v bundled（466），也不是 Finalize 何时调用 bundled（362）。不要另写怎样 persist decision、怎样写同步调用。

## 官方三件事

规范把 FinalizeBlock When 第 1 步 _p_ persists _v_ as the decision for height _h_ 和「已经是 Application executes block _v_ interchangeable / 已经是 Finalize + Commit 交差 interchangeable / 已经是 finpersist bundled interchangeable」分开写成三件独立的实现事，不是「看见 persists _v_ as the decision 就已经 executes block v、已经交差、已经 finpersist bundled interchangeable」一件事：

1. **看见 _p_ persists _v_ as the decision for height _h_ / 看见把 _v_ 落成这一高的决定 is not already Application executes block _v_ interchangeable / 已经 When 第 3 步 executes block _v_ interchangeable / 已经 execute according to FinalizeBlockRequest.txs interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 572 not execbv interchangeable / 582 not executes block v interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 finexecbv interchangeable / 573 not persist interchangeable / 584 apply candidate interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 472 When calling interchangeable / 360 Process guarantee interchangeable / 351 Process also on proposer interchangeable。**  
   官方 When 第 1 步写：_p_ persists _v_ as the decision for height _h_。看见 persist decision，不是已经 Application executes block _v_ 那种已经执行完（466 第 3 步）——466 钉 When 第 3 步 executes block v，本页从 478 item 1 侧钉 not executes block v 单句。看见把 _v_ 落成决定，不是已经 When calling / consensus guarantees means Application executes block v（472 / 572） interchangeable——572 钉 When calling not executes block v，本页钉 persist decision 第一件事。看见 persists _v_ as decision，不是已经 apply candidate state / previously executed means no need to execute txs（460 / 578） interchangeable——460 钉 fincand bundled，本页钉 478 item 1 单句。
2. **看见 persist decision / 看见把 _v_ 落成这一高的决定 is not already Finalize + Commit 那种已经交差 interchangeable / 已经四门已经结算 interchangeable / 已经 persist outputs / AppHash / ResultsHash interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable，也不是已经 FinalizeBlock equiv not four gates settled bundled（602 余量） interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 601 notsettled interchangeable / 594 not settled interchangeable，也不是已经 FinalizeBlock must provide values not already settled bundled（594 余量） interchangeable / 477 finasresult interchangeable / 363 finresp interchangeable / 478 finpersist item 2 calls FinalizeBlock interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量 / 467） interchangeable / 587 finreturn interchangeable / 335 Finalize 落盘禁令 interchangeable / 403 finafter interchangeable。**  
   官方把 persist _v_ as decision 和 Finalize + Commit 已经交差 / 四门已经结算 / persist outputs 分开——478 bundled 第一件事常被写成「看见 persist decision 就已经交差 interchangeable」，本页钉 not 已经交差 单句。看见 persist decision，不是已经 four gates settled（33） interchangeable——33 钉四门已经结算，本页钉 478 item 1 第二件事。看见把 _v_ 落成决定，不是已经 persist tx outputs / AppHash / ResultsHash（587 / 467） interchangeable——587 钉 When 第 4–6 步 returns / ResultHash / persist 这三份，本页钉 persist decision 单句。
3. **看见 persist decision / 看见把 _v_ 落成这一高的决定 is not already finpersist bundled（478） interchangeable / 已经 calls FinalizeBlock interchangeable / 已经 synchronous call interchangeable / 已经 +2/3 precommit 决定 interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 605 notpersist interchangeable / 478 finpersist item 2 interchangeable / 478 finpersist item 3 interchangeable / 362 +2/3 precommit interchangeable / 354 processwhen synchronous interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable / 466 executes block v interchangeable，也不是已经 FinalizeBlock equiv not four gates settled bundled（602 余量） interchangeable / 602 notgates interchangeable / 586 finequiv interchangeable / 600 notgates interchangeable，也不是已经 Finalize 回包义务 must provide not settled bundled（601 余量） interchangeable / 601 notsettled interchangeable / 594 not settled interchangeable / 363 finresp interchangeable。**  
   官方把 478 finpersist bundled 三事里的 persist decision 和 calls FinalizeBlock / synchronous call / decides trigger 分开——478 bundled 常与 item 2 / item 3 混成「看见 persist decision 就已经 finpersist bundled interchangeable」，本页钉 478 item 1 第三件事。看见 persist decision，不是已经 calls FinalizeBlock with _v_'s data（478 item 2 余量） interchangeable——478 item 2 另钉 not persist outputs / not decides trigger，本页钉 item 1 单句。看见把 _v_ 落成决定，不是已经 The call is synchronous / +2/3 precommit 决定 interchangeable（478 item 3 余量 / 362）——362 钉何时决定，本页钉 persist decision 单句。

怎样 persist decision、怎样写同步调用、怎样在 When 第 2 步调 Finalize 是规范里的做法，本页不抄。FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478）、calls FinalizeBlock not persist outputs（478 item 2 余量）、synchronous call not decides trigger（478 item 3 余量）、Application executes block v（466）、Finalize 何时调用 bundled（362）、AppHash tx outputs ResultHash persist（587 / 467）是另外那套，本页不抄。

## 官方为什么这样拆

- **persist decision not executes block v ≠ executes block v bundled / When calling guarantee interchangeable：** 官方把 persist _v_ as decision 和 Application executes block _v_ / When calling guarantee 分开。
- **persist decision not 交差 ≠ four gates settled / persist outputs interchangeable：** 官方把 478 item 1 和 Finalize + Commit 交差 / persist tx outputs / AppHash / ResultsHash 分开。
- **persist decision not finpersist bundled ≠ calls FinalizeBlock / synchronous call / decides trigger interchangeable：** 官方把 478 item 1 和 item 2 / item 3 / 362 finwhen 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| persist decision | 不是 already executes block v | 不是 executes block v bundled（466） |
| persist decision | 不是 already 交差 / persist outputs | 不是 four gates（33） / finreturn（587） |
| persist decision | 不是 already finpersist bundled | 不是 calls FinalizeBlock（478 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When persist decision not executes block v / 已经交差 正式三事（478 余量），必须分开 persist decision 是不是 already Application executes block _v_ interchangeable / 466 executes block v interchangeable / 572 not execbv interchangeable / 584 apply candidate interchangeable、persist decision 是不是 already Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable、persist decision 是不是 already finpersist bundled interchangeable / 478 item 2 calls FinalizeBlock interchangeable / 478 item 3 synchronous call interchangeable / 362 +2/3 precommit interchangeable。可以跳过「看见 persist decision 就已经 executes block v interchangeable」。不要另写怎样 persist decision。

## 本页不抄

- 怎样 persist decision、怎样写同步调用、怎样在 When 第 2 步调 Finalize。
- FinalizeBlock When persist decision / synchronous call 正式三事 bundled。那是不变量 478。
- calls FinalizeBlock not persist outputs。那是不变量 478 item 2 余量。
- synchronous call not decides trigger。那是不变量 478 item 3 余量 / 362。
- Application executes block v bundled。那是不变量 466。
- Finalize 何时调用 bundled。那是不变量 362。
- 四门已经结算。那是不变量 33。
