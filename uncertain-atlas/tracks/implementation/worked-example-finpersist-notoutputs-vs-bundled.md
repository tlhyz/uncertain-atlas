# 例：看见 _p_'s CometBFT calls `FinalizeBlock` with _v_'s data / 看见同步调 Finalize is not already persist the transaction outputs, AppHash, and ResultsHash interchangeable / 已经 persist outputs / 已经落盘 interchangeable；不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 已经 finpersist bundled interchangeable

**层次**：实现 / FinalizeBlock When calls FinalizeBlock not persist outputs / 已经落盘 正式三事（478 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When calls FinalizeBlock not persist outputs / not 362 decides trigger / not finpersist bundled（478） interchangeable / not 606 notoutputs interchangeable / not 587 finreturn interchangeable / not 362 +2/3 precommit interchangeable」，不是 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478），也不是 AppHash tx outputs ResultHash persist bundled（587 / 467），也不是 Finalize 何时调用 bundled（362）。不要另写怎样 persist decision、怎样写同步调用。

## 官方三件事

规范把 FinalizeBlock When 第 2 步 _p_'s CometBFT calls `FinalizeBlock` with _v_'s data 和「已经是 persist tx outputs / AppHash / ResultsHash interchangeable / 已经是 +2/3 precommit 决定 interchangeable / 已经是 finpersist bundled interchangeable」分开写成三件独立的实现事，不是「看见 calls FinalizeBlock 就已经 persist outputs、已经 +2/3 precommit 决定 interchangeable、已经 finpersist bundled interchangeable」一件事：

1. **看见 _p_'s CometBFT calls `FinalizeBlock` with _v_'s data / 看见同步调 Finalize / 看见 with _v_'s data is not already persist the transaction outputs, AppHash, and ResultsHash interchangeable / 已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable / 已经 Application returns AppHash + tx outputs interchangeable / 已经 ResultHash / LastResultsHash interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 606 notoutputs interchangeable / 478 finpersist interchangeable / 587 finreturn interchangeable / 467 finpersist interchangeable / 335 finpersist interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量 / 467） interchangeable / 587 finreturn interchangeable / 466 executes block v interchangeable / 335 Finalize 落盘禁令 interchangeable，也不是已经 Application calculates and returns AppHash + tx outputs bundled（587 item 1 余量） interchangeable / 587 finreturn item 1 interchangeable / 147 apphash vs this block interchangeable / 316 ExecTxResult 回执 interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 590 fincommit interchangeable / 588 finlock interchangeable。**  
   官方 When 第 2 步写：_p_'s CometBFT calls `FinalizeBlock` with _v_'s data. The call is synchronous。看见 calls FinalizeBlock，不是已经 persist tx outputs / AppHash / ResultsHash（587 When 第 4–6 步 / 467） interchangeable——587 钉 When 第 4–6 步 returns / ResultHash / persist 这三份，本页从 478 item 2 侧钉 not persist outputs 单句。看见 with _v_'s data，不是已经 Application calculates and returns AppHash + tx outputs（587 item 1） interchangeable——587 item 1 另钉 not 印进本头 / not 本头 AppHash，本页钉 calls FinalizeBlock 第一件事。看见同步调 Finalize，不是已经 Finalize 改了就已经落盘（335） interchangeable——335 钉 Finalize 落盘禁令，本页钉 478 item 2 单句。
2. **看见 calls FinalizeBlock / 看见 with _v_'s data is not already +2/3 precommit 同一 id(v) 才决定再调 Finalize interchangeable / 已经 decides block 触发条件 interchangeable / 已经 When trigger 2f+1 precommit interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 606 notoutputs interchangeable / 478 finpersist interchangeable / 362 +2/3 precommit interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen bundled interchangeable / 605 notpersist interchangeable / 466 executes block v interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit bundled（479 余量） interchangeable / 479 fintrigger interchangeable / 362 item 1 +2/3 precommit interchangeable / 362 item 2 persist decision interchangeable，也不是已经 FinalizeBlock When Application executes block v not +2/3 precommit decided bundled（466 余量 / 573） interchangeable / 573 not persist interchangeable / 362 +2/3 precommit interchangeable / 466 executes block v interchangeable。**  
   官方把 calls FinalizeBlock with _v_'s data 和 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362）分开——478 bundled 第二件事常与 362 混成「看见 calls FinalizeBlock 就已经 +2/3 precommit 决定 interchangeable」，本页钉 not decides trigger 单句。看见 with _v_'s data，不是已经 When trigger 2f+1 precommit（479） interchangeable——479 钉 Proposal / block parts / precommit 三事，本页钉 478 item 2 第二件事。看见 calls FinalizeBlock，不是已经 persist decision（605 / 478 item 1） interchangeable——605 钉 not executes block v / not 交差，本页钉 calls FinalizeBlock 单句。
3. **看见 calls FinalizeBlock / 看见同步调 Finalize is not already finpersist bundled（478） interchangeable / 已经 persist decision interchangeable / 已经 synchronous call interchangeable / 已经 The call is synchronous interchangeable，也不是已经 FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478） interchangeable / 606 notoutputs interchangeable / 478 finpersist item 1 interchangeable / 478 finpersist item 3 interchangeable / 605 notpersist interchangeable / 354 processwhen synchronous interchangeable，也不是已经 FinalizeBlock When persist decision not executes block v bundled（605 余量） interchangeable / 605 notpersist interchangeable / 466 executes block v interchangeable / 572 not execbv interchangeable，也不是已经 synchronous call not decides trigger bundled（478 item 3 余量） interchangeable / 362 +2/3 precommit interchangeable / 354 Process 同步 interchangeable / 466 executes block v interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen interchangeable / 362 item 3 synchronous call interchangeable / 479 fintrigger interchangeable。**  
   官方把 478 finpersist bundled 三事里的 calls FinalizeBlock 和 persist decision / synchronous call / decides trigger 分开——478 bundled 常与 item 1 / item 3 混成「看见 calls FinalizeBlock 就已经 finpersist bundled interchangeable」，本页钉 478 item 2 第三件事。看见 calls FinalizeBlock，不是已经 persist decision（605 / 478 item 1 余量） interchangeable——605 另钉 not executes block v / not 交差，本页钉 item 2 单句。看见 with _v_'s data，不是已经 The call is synchronous / +2/3 precommit 决定 interchangeable（478 item 3 余量 / 362）——478 item 3 另钉 not 异步 / not decides trigger，本页钉 calls FinalizeBlock 单句。

怎样 persist decision、怎样写同步调用、怎样在 When 第 4–6 步 persist outputs 是规范里的做法，本页不抄。FinalizeBlock When persist decision / synchronous call 正式三事 bundled（478）、persist decision not executes block v（605 / 478 item 1）、synchronous call not decides trigger（478 item 3 余量 / 362）、AppHash tx outputs ResultHash persist（587 / 467）、Finalize 何时调用 bundled（362）是另外那套，本页不抄。

## 官方为什么这样拆

- **calls FinalizeBlock not persist outputs ≠ finreturn / 467 persist bundled interchangeable：** 官方把 calls FinalizeBlock with _v_'s data 和 persist tx outputs / AppHash / ResultsHash 分开。
- **calls FinalizeBlock not decides trigger ≠ 362 finwhen / 479 fintrigger interchangeable：** 官方把 478 item 2 和 +2/3 precommit 决定 / When trigger 分开。
- **calls FinalizeBlock not finpersist bundled ≠ persist decision / synchronous call interchangeable：** 官方把 478 item 2 和 item 1 / item 3 / 605 / 362 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| calls FinalizeBlock | 不是 already persist outputs | 不是 finreturn / 467 persist（587） |
| calls FinalizeBlock | 不是 already decides trigger | 不是 finwhen bundled（362） |
| calls FinalizeBlock | 不是 already finpersist bundled | 不是 persist decision（605 / 478 item 1） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calls FinalizeBlock not persist outputs / 362 decides trigger 正式三事（478 余量），必须分开 calls FinalizeBlock 是不是 already persist tx outputs / AppHash / ResultsHash interchangeable / 587 finreturn interchangeable / 467 finpersist interchangeable / 335 finpersist interchangeable、calls FinalizeBlock 是不是 already +2/3 precommit 决定 interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable / 605 notpersist interchangeable、calls FinalizeBlock 是不是 already finpersist bundled interchangeable / 605 notpersist interchangeable / 478 item 3 synchronous call interchangeable / 354 processwhen synchronous interchangeable。可以跳过「看见 calls FinalizeBlock 就已经 persist outputs interchangeable」。不要另写怎样 persist decision。

## 本页不抄

- 怎样 persist decision、怎样写同步调用、怎样在 When 第 4–6 步 persist outputs。
- FinalizeBlock When persist decision / synchronous call 正式三事 bundled。那是不变量 478。
- persist decision not executes block v。那是不变量 605（478 item 1 余量）。
- synchronous call not decides trigger。那是不变量 478 item 3 余量 / 362。
- AppHash tx outputs ResultHash persist bundled。那是不变量 587 / 467。
- Finalize 何时调用 bundled。那是不变量 362。
