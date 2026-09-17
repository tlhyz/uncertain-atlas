# 例：看见 then _p_ decides block _v_ and finalizes consensus for height _h_ / 看见然后决定 _v_ is not already 处在高度 _h_ 就会调 Finalize interchangeable / 已经 +2/3 precommit 就会调 Finalize interchangeable；不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 已经 fintrigger bundled interchangeable

**层次**：实现 / FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs 正式三事（479 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs / not fintrigger bundled（479） interchangeable / not 610 notdecides interchangeable / not 362 finwhen interchangeable / not 478 finpersist interchangeable / not 605 notpersist interchangeable」，不是 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479），也不是 Finalize 何时调用 bundled（362），也不是 persist decision / synchronous call bundled（478）。不要另写怎样收块片、怎样数 2f+1、怎样落决定。

## 官方三件事

规范把 FinalizeBlock When preamble 里 then _p_ decides block _v_ and finalizes consensus for height _h_ 和「已经是 处在高度 _h_ 就会调 Finalize interchangeable / 已经是 persist outputs / 已经交差 interchangeable / 已经是 fintrigger bundled interchangeable」分开写成三件独立的实现事，不是「看见 decides block v 就已经到了这一高就会调 Finalize、已经 persist outputs、已经 fintrigger bundled interchangeable」一件事：

1. **看见 then _p_ decides block _v_ and finalizes consensus for height _h_ / 看见然后决定 _v_ is not already 处在高度 _h_ 就会调 Finalize interchangeable / 已经 +2/3 precommit 就会调 Finalize interchangeable / 已经 When trigger 2f+1 precommit 就已经会调 Finalize interchangeable / 362 +2/3 precommit interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 610 notdecides interchangeable / 479 fintrigger interchangeable / 611 finwhenparts interchangeable / 362 finwhen bundled interchangeable / 362 item 1 +2/3 precommit interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen bundled interchangeable / 362 item 2 persist decision interchangeable / 362 item 3 synchronous call interchangeable / 606 notoutputs interchangeable / 607 notsync interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 362 decides trigger interchangeable / 479 fintrigger interchangeable，也不是已经 FinalizeBlock When synchronous call not decides trigger bundled（607 余量） interchangeable / 607 notsync interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable / 605 notpersist interchangeable。**  
   官方写：then _p_ decides block _v_ and finalizes consensus for height _h_ in the following way。看见 decides block _v_，不是已经 +2/3 precommit 决定触发（362 bundled 第一句）就已经是同一句 interchangeable——479 bundled 第三件事常被写成「看见 decides block v 就已经到了这一高就会调 Finalize interchangeable」，本页从 479 item 3 侧钉 not at height h will Finalize 单句。看见 then，不是已经 When trigger 2f+1 precommit（609 / 479 item 2 余量） interchangeable——609 另钉 not +2/3 prevote ExtendVote / not without all block parts，本页钉 479 item 3 第一件事。看见 finalizes consensus for height _h_，不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362） interchangeable——362 钉 When 第 1–2 步 persist decision / calls FinalizeBlock，本页钉 not at height h will Finalize 单句。
2. **看见 decides block v / 看见 then decides block _v_ is not already persist outputs / AppHash / ResultsHash interchangeable / 已经 persist decision interchangeable / 已经 Finalize + Commit 交差 interchangeable / 478 finpersist interchangeable / 605 notpersist interchangeable / 587 finreturn interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 610 notdecides interchangeable / 479 fintrigger interchangeable / 478 finpersist item 1 interchangeable / 478 finpersist item 2 interchangeable / 606 notoutputs interchangeable / 33 four gates interchangeable，也不是已经 FinalizeBlock When persist decision not executes block v bundled（605 余量） interchangeable / 605 notpersist interchangeable / 466 executes block v interchangeable / 572 not execbv interchangeable / 335 finpersist interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 587 finreturn interchangeable / 467 finpersist interchangeable / 316 ExecTxResult interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量 / 467） interchangeable / 587 finreturn interchangeable / 403 finafter interchangeable / 590 fincommit interchangeable。**  
   官方把 decides block _v_ 和 persist decision / persist outputs / 已经交差 分开——479 item 3 常与 478 混成「看见 decides block v 就已经 persist outputs / 已经交差 interchangeable」，本页钉 not persist outputs 单句。看见 then decides block _v_，不是已经 persist decision（478 第 1 步 / 605） interchangeable——605 钉 not executes block v / not 交差，本页钉 479 item 3 第二件事。看见 finalizes consensus for height _h_，不是已经 four gates settled（33） interchangeable——33 钉四门已经结算，本页钉 not persist outputs 单句。
3. **看见 decides block v / 看见 then decides block _v_ is not already fintrigger bundled（479） interchangeable / 已经 Proposal + all block parts interchangeable / 已经 2f+1 precommit same id(v) interchangeable / 608 notparts interchangeable / 609 notprecommit interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 610 notdecides interchangeable / 479 fintrigger item 1 interchangeable / 479 fintrigger item 2 interchangeable / 611 finwhenparts interchangeable，也不是已经 FinalizeBlock When trigger Proposal + all block parts not only hash bundled（608 余量） interchangeable / 608 notparts interchangeable / 428 finhash interchangeable / 472 Process guarantee interchangeable，也不是已经 FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote bundled（609 余量） interchangeable / 609 notprecommit interchangeable / 361 extendwhen interchangeable / 361 prevote ExtendVote interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen bundled interchangeable / 362 item 1 +2/3 precommit interchangeable / 362 item 2 persist decision interchangeable。**  
   官方把 479 fintrigger bundled 三事里的 decides block v 和 Proposal + parts / 2f+1 precommit 分开——479 bundled 常与 item 1 / item 2 混成「看见 decides block v 就已经 fintrigger bundled interchangeable」，本页钉 479 item 3 第三件事。看见 then decides block _v_，不是已经 Proposal + all block parts（608 / 479 item 1 余量） interchangeable——608 另钉 not only hash / not Process ran，本页钉 item 3 单句。看见 decides block v，不是已经 2f+1 precommit same id(v)（609 / 479 item 2 余量） interchangeable——609 另钉 not +2/3 prevote ExtendVote / not without all block parts，本页钉 not fintrigger bundled 单句。

怎样收块片、怎样数 2f+1、怎样落决定是规范里的做法，本页不抄。FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479）、Proposal + all block parts not only hash（608 / 479 item 1）、2f+1 precommit not +2/3 prevote ExtendVote（609 / 479 item 2）、Finalize 何时调用 bundled（362）、persist decision / synchronous call bundled（478）、AppHash tx outputs ResultHash persist（587 / 467）是另外那套，本页不抄。

## 官方为什么这样拆

- **decides block v not at height h will Finalize ≠ 362 finwhen / +2/3 precommit interchangeable：** 官方把决定 _v_ 和到了这一高就会调 Finalize / 362 finwhen 分开。
- **decides block v not persist outputs ≠ 478 finpersist / 605 notpersist / 587 finreturn interchangeable：** 官方把 479 item 3 和 persist decision / persist outputs / 已经交差 分开。
- **decides block v not fintrigger bundled ≠ 608 notparts / 609 notprecommit interchangeable：** 官方把 479 item 3 和 item 1 / item 2 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| decides block v | 不是 already at height h will Finalize | 不是 finwhen bundled（362） |
| decides block v | 不是 already persist outputs / 交差 | 不是 persist decision（605 / 478） |
| decides block v | 不是 already fintrigger bundled | 不是 Proposal + parts（608 / 479 item 1） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs 正式三事（479 余量），必须分开 decides block v 是不是 already 处在高度 _h_ 就会调 Finalize interchangeable / 362 finwhen interchangeable / 362 +2/3 precommit interchangeable / 606 notoutputs interchangeable、decides block v 是不是 already persist outputs / 已经交差 interchangeable / 478 finpersist interchangeable / 605 notpersist interchangeable / 587 finreturn interchangeable / 33 four gates interchangeable、decides block v 是不是 already fintrigger bundled interchangeable / 608 notparts interchangeable / 609 notprecommit interchangeable / 611 finwhenparts interchangeable。可以跳过「看见 decides block v 就已经到了这一高就会调 Finalize interchangeable」。不要另写怎样收块片。

## 本页不抄

- 怎样收块片、怎样数 2f+1、怎样落决定。
- FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled。那是不变量 479。
- Proposal + all block parts not only hash / Process ran。那是不变量 608（479 item 1 余量）。
- 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts。那是不变量 609（479 item 2 余量）。
- Finalize 何时调用 bundled。那是不变量 362。
- persist decision / synchronous call bundled。那是不变量 478。
- AppHash tx outputs ResultHash persist bundled。那是不变量 587 / 467。
