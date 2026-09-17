# 例：看见 CometBFT calls Commit / 看见 When 第 8 步叫 Commit is not already 已经交差 interchangeable / 已经四门已经结算 interchangeable / 已经 fincommit bundled interchangeable

**层次**：实现 / FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 8。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量）/ not 644 fincommit-notsettled interchangeable / not 335 finpersist interchangeable / not 587 finreturn interchangeable / not 403 finafter interchangeable / not 588 finlock interchangeable / not 481 commitpersist interchangeable」，不是 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590），也不是 Finalize 落盘禁令 bundled（335），也不是 CometBFT persists 这三份 bundled（587）。不要另写怎样落盘、怎样写 Commit、怎样 optional recheck。

## 官方三件事

规范把 When 第 8 步 _p_'s CometBFT calls `Commit` to instruct the Application to persist its state 和「已经是已经交差 interchangeable / 已经是四门已经结算 interchangeable / 已经是 fincommit bundled interchangeable」分开写成三件独立的实现事，不是「看见 When 第 8 步叫了 Commit 就已经交差、就已经四门已经结算、就已经 fincommit bundled interchangeable」一件事：

1. **看见 CometBFT calls Commit / 看见 When 第 8 步叫 Commit / 看见 calls `Commit` is not already 已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 632 notsettled interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable / 644 fincommit-notsettled interchangeable / 590 fincommit interchangeable / 645 fincommit-notpersist interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 1 引擎才落盘这三份 interchangeable / 403 item 2 落完再锁内存池 interchangeable / 403 item 3 optional recheck interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量） interchangeable / 587 finreturn interchangeable / 616 notpersist interchangeable / 481 commitpersist interchangeable / 467 finpersist interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 601 notsettled interchangeable / 594 not settled interchangeable。**  
   官方 When 第 8 步写：_p_'s CometBFT calls `Commit`。发生在 When 第 7 步 locks the mempool 之后、第 9 步 optional recheck 之前。看见 calls Commit，不是已经 Finalize + Commit 那种已经交差（33） interchangeable——590 bundled 第一件事常被写成「看见 When 第 8 步叫了 Commit 就已经交差 interchangeable」，本页从 590 item 1 侧钉 not already settled 单句。看见 When 第 8 步，不是已经 CometBFT persists 这三份（587）那种引擎落这三份 interchangeable——587 另钉 When 第 6 步，本页钉 calls Commit not settled 单句。看见叫 Commit，不是已经 Finalize 之后 bundled（403）那种落完锁内存池 / Commit / Recheck 整包 interchangeable——403 另钉 Finalize 之后全流程，本页钉 not already settled 单句。
2. **看见 CometBFT calls Commit / 看见 When 第 8 步叫 Commit is not already 已经四门已经结算 interchangeable / 已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable / 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 478 finpersist interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable / 644 fincommit-notsettled interchangeable / 590 fincommit interchangeable / 645 fincommit-notpersist interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 FinalizeBlock equiv ABCI 1.0 not four gates settled bundled（586 item 1 余量 / 602） interchangeable / 602 notgates interchangeable / 586 finequiv interchangeable / 601 notsettled interchangeable / 363 finresp interchangeable，也不是已经 Finalize 回包义务 not four gates settled bundled（600 / 363 item 1 余量） interchangeable / 600 notgates interchangeable / 363 finresp interchangeable / 465 equiv bundled interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 335 finpersist interchangeable。**  
   官方把 When 第 8 步 calls Commit 和四门已经结算分开——590 item 1 常与 33 / 602 混成「看见 When 第 8 步叫了 Commit 就已经四门已经结算 interchangeable」，本页钉 not four gates settled 单句。看见 calls Commit，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了（33） interchangeable——33 钉四门已经结算，本页钉 590 item 1 第二件事。看见 When 第 8 步，不是已经 persist decision（478 第 1 步） interchangeable——478 钉 When 第 1 步，本页钉 calls Commit not four gates 单句。
3. **看见 CometBFT calls Commit / 看见 When 第 8 步叫 Commit is not already fincommit bundled（590） interchangeable / 已经 instruct Application to persist its state interchangeable / 已经引擎 persist 这三份 interchangeable / 已经 Commit Usage signal bundled interchangeable / 590 fincommit item 2 interchangeable / 590 fincommit item 3 interchangeable / 645 fincommit-notpersist interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable / 644 fincommit-notsettled interchangeable / 590 fincommit interchangeable / 481 commitpersist interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable，也不是已经 instruct Application to persist its state not engine persist bundled（590 item 2 余量 / 645） interchangeable / 645 fincommit-notpersist interchangeable / 481 commitpersist interchangeable / 467 finpersist interchangeable / 616 notpersist interchangeable，也不是已经 When 第 8 步 calls Commit after lock mempool not Commit lock bundled（590 item 3 余量 / 646） interchangeable / 646 fincommit-notcommitlock interchangeable / 310 commitlock interchangeable / 588 finlock interchangeable / 631 notcommitlock interchangeable / 403 finafter item 3 optional recheck interchangeable。**  
   官方把 590 fincommit bundled 三事里的 CometBFT calls Commit 和 instruct persist / after lock mempool 分开——590 bundled 常与 item 2 / item 3 混成「看见 When 第 8 步叫了 Commit 就已经 fincommit bundled interchangeable」，本页钉 590 item 1 第三件事。看见 calls Commit，不是已经 instruct Application to persist its state not engine persist（590 item 2 余量 / 645） interchangeable——645 另钉 not engine persist / not Commit Usage signal，本页钉 item 1 单句。看见 When 第 8 步，不是已经 calls Commit after lock mempool not Commit lock（590 item 3 余量 / 646） interchangeable——646 另钉 not Commit lock / not recheck / unlock，本页钉 not fincommit bundled 单句。590 fincommit unbundling 在本页 item 1 启动。

怎样落盘、怎样写 Commit、怎样 optional recheck 是规范里的做法，本页不抄。FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590）、instruct Application to persist its state not engine persist（590 item 2 余量 / 645）、When 第 8 步 calls Commit after lock mempool not Commit lock（590 item 3 余量 / 646）、Finalize 之后 bundled（403）、Finalize 落盘禁令（335）、Commit Usage persist signal（481）、CometBFT persists 这三份（587）、locks mempool（588）是另外那套，本页不抄。

## 官方为什么这样拆

- **calls Commit not already settled ≠ 403 finafter / 587 finreturn interchangeable：** 官方把 When 第 8 步 calls Commit 和 Finalize + Commit 交差 / persists 这三份 分开。
- **calls Commit not four gates settled ≠ 33 four gates / 602 notgates interchangeable：** 官方把 590 item 1 和四门已经结算 / finequiv not four gates 分开。
- **calls Commit not fincommit bundled ≠ 645 fincommit-notpersist / 646 fincommit-notcommitlock interchangeable：** 官方把 590 item 1 和 item 2 / item 3 分开；590 fincommit unbundling 启动（644 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CometBFT calls Commit | 不是 already settled / 交差 | 不是 finafter bundled（403） |
| CometBFT calls Commit | 不是 already four gates settled | 不是 four gates（33） |
| CometBFT calls Commit | 不是 already fincommit bundled | 不是 instruct persist（590 item 2 / 645） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量），必须分开 CometBFT calls Commit 是不是 already settled / 交差 interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable / 632 notsettled interchangeable、calls Commit 是不是 already four gates settled interchangeable / 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable、calls Commit 是不是 already fincommit bundled interchangeable / 645 fincommit-notpersist interchangeable / 646 fincommit-notcommitlock interchangeable / 481 commitpersist interchangeable。可以跳过「看见 When 第 8 步叫了 Commit 就已经交差 interchangeable」。不要另写怎样落盘。590 fincommit unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样 optional recheck。
- FinalizeBlock When calls Commit instruct persist 正式三事 bundled。那是不变量 590。
- instruct Application to persist its state not engine persist。那是不变量 590 item 2 余量 / 645。
- When 第 8 步 calls Commit after lock mempool not Commit lock。那是不变量 590 item 3 余量 / 646。
- Finalize 之后 bundled。那是不变量 403。
- Finalize 落盘禁令。那是不变量 335。
- Commit Usage persist signal bundled。那是不变量 481。
- CometBFT persists 这三份。那是不变量 587。
- locks mempool。那是不变量 588。
