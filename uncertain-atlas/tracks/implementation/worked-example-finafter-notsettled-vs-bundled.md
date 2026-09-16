# 例：看见 Finalize 之后引擎才落盘各笔 output / AppHash / ResultsHash / 看见回了 Finalize is not already 已经交差 interchangeable / 已经落盘应用状态 interchangeable / 已经 finafter bundled interchangeable

**层次**：实现 / FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 6–7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量）/ not 632 notsettled interchangeable / not 616 notpersist interchangeable / not 335 finpersist interchangeable / not 481 commitpersist interchangeable / not 633 notlock interchangeable / not 634 notrecheck interchangeable」，不是 Finalize 之后 bundled（403），也不是 CometBFT persists 这三份 bundled（587 item 3 / 616），也不是 Finalize 落盘禁令（335）。不要另写怎样落盘这三份、怎样锁内存池、怎样再验。

## 官方三件事

规范把 Finalize 回了之后引擎才落盘各笔 output / `AppHash` / `ResultsHash`（When 第 6 步 CometBFT persists the transaction outputs, _AppHash_, and _ResultsHash_）和「已经是已经交差 interchangeable / 已经是已经落盘应用状态 interchangeable / 已经是 finafter bundled interchangeable」分开写成三件独立的实现事，不是「看见 Finalize 之后引擎才落盘这三份 就已经交差、就已经 Commit 落盘、就已经 finafter bundled interchangeable」一件事：

1. **看见 Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash / 看见 CometBFT persists the transaction outputs, AppHash, and ResultsHash / 看见 When 第 6 步 persists 这三份 is not already 已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 601 notsettled interchangeable / 587 finreturn interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 632 notsettled interchangeable / 403 finafter interchangeable / 633 notlock interchangeable / 634 notrecheck interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash not already settled bundled（587 item 3 余量 / 616） interchangeable / 616 notpersist interchangeable / 587 finreturn interchangeable / 614 notheader interchangeable / 615 notresulthash interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335 余量） interchangeable / 335 finpersist interchangeable / 335 item 1 Finalize 改了就已经落盘 interchangeable / 335 item 2 必须在 Commit 落盘 interchangeable / 616 notpersist interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 606 notoutputs interchangeable / 362 finwhen interchangeable。**  
   官方 When 第 6 步写：CometBFT persists the transaction outputs, _AppHash_, and _ResultsHash_。发生在 Application 回了 `FinalizeBlockResponse` 之后、When 第 7 步锁内存池之前。看见 Finalize 之后引擎才落盘这三份，不是已经 Finalize + Commit 交差（33） interchangeable——403 bundled 第一件事常被写成「看见回了 Finalize 就已经交差 interchangeable」，本页从 403 item 1 侧钉 not already settled 单句。看见 persists 这三份，不是已经 Finalize 改了就已经落盘（335） interchangeable——335 钉应用 MUST NOT 在 Finalize 持久化，本页钉 When 第 6 步引擎 persist 这三份 单句。看见 When 第 6 步，不是已经 CometBFT persists 这三份 not already settled（587 item 3 余量 / 616） interchangeable——616 另钉 587 When 第 6 步 not Commit 落盘，本页钉 403 item 1 第一件事。
2. **看见 Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash / 看见 persists 这三份 is not already 已经落盘应用状态 interchangeable / 已经应用在 Commit 里落盘 interchangeable / Commit 落盘应用状态 interchangeable / 481 commitpersist interchangeable / 467 finpersist interchangeable / 335 item 2 必须在 Commit 落盘 interchangeable / 481 item 1 persist signal interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 632 notsettled interchangeable / 403 finafter interchangeable / 633 notlock interchangeable / 634 notrecheck interchangeable，也不是已经 Commit Usage persist signal bundled（481 余量） interchangeable / 481 commitpersist interchangeable / 481 item 2 expected persist at end of call interchangeable / 481 item 3 historical blocks interchangeable / 399 retain height interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist bundled（590 余量） interchangeable / 590 fincommit interchangeable / 467 finpersist interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash not Commit persist application state bundled（587 item 3 余量 / 616） interchangeable / 616 notpersist interchangeable / 481 commitpersist interchangeable / 478 finpersist interchangeable / 606 notoutputs interchangeable。**  
   官方把 When 第 6 步引擎 persist 这三份 和应用在 `Commit` 里落盘应用状态分开——403 item 1 常与 481 / 335 混成「看见 Finalize 之后引擎才落盘 就已经落盘应用状态 interchangeable」，本页钉 not Commit persist application state 单句。看见 persists 这三份，不是已经 Signal the Application to persist application state（481） interchangeable——481 钉 Commit Usage persist signal，本页钉 403 item 1 第二件事。看见引擎落了 tx outputs / AppHash / ResultsHash，不是已经 When step 8 calls Commit to instruct（467 / 590） interchangeable——590 另钉 When 第 8 步，本页钉 not Commit persist 单句。
3. **看见 Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash / 看见 persists 这三份 is not already finafter bundled（403） interchangeable / 已经落完再锁内存池 interchangeable / 已经 optional recheck unlock h+1 interchangeable / 403 finafter item 2 interchangeable / 403 finafter item 3 interchangeable / 633 notlock interchangeable / 634 notrecheck interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 632 notsettled interchangeable / 403 finafter interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable / 631 notcommitlock interchangeable，也不是已经 Finalize 之后落完再锁内存池 not Commit lock bundled（403 item 2 余量 / 633） interchangeable / 633 notlock interchangeable / 588 finlock interchangeable / 631 notcommitlock interchangeable / 310 commitlock interchangeable，也不是已经 Finalize 之后 optional recheck unlock h+1 not Recheck bundled（403 item 3 余量 / 634） interchangeable / 634 notrecheck interchangeable / 591 finrecheck interchangeable / 592 finunlock interchangeable / 593 finh1 interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 item 3 余量 / 616） interchangeable / 616 notpersist interchangeable / 614 notheader interchangeable / 615 notresulthash interchangeable / 587 finreturn interchangeable。**  
   官方把 403 finafter bundled 三事里的 Finalize 之后引擎才落盘这三份 和落完再锁内存池 / optional recheck unlock h+1 分开——403 bundled 常与 item 2 / item 3 混成「看见 Finalize 之后引擎才落盘 就已经 finafter bundled interchangeable」，本页钉 403 item 1 第三件事。看见 persists 这三份，不是已经落完再锁内存池 not Commit lock（403 item 2 余量 / 633） interchangeable——633 另钉 not Commit lock / not 588 finlock bundled，本页钉 item 1 单句。看见 When 第 6 步，不是已经 optional recheck unlock h+1 not Recheck（403 item 3 余量 / 634） interchangeable——634 另钉 not Recheck / not unlock / not h+1 round 0，本页钉 not finafter bundled 单句。403 finafter unbundling 在本页 item 1 启动。

怎样落盘这三份、怎样锁内存池、怎样再验、怎样开下一高是规范里的做法，本页不抄。Finalize 之后 bundled（403）、Finalize 之后落完再锁内存池 not Commit lock（403 item 2 余量 / 633）、Finalize 之后 optional recheck unlock h+1 not Recheck（403 item 3 余量 / 634）、CometBFT persists 这三份 not already settled（587 item 3 余量 / 616）、Finalize 落盘禁令（335）、Commit Usage persist signal（481）、locks mempool not settled（588 item 1 / 629）是另外那套，本页不抄。

## 官方为什么这样拆

- **Finalize 之后引擎才落盘 not already settled ≠ 335 finpersist / 616 notpersist interchangeable：** 官方把 When 第 6 步引擎 persist 这三份 和已经交差 / Finalize 改了就已经落盘分开。
- **Finalize 之后引擎才落盘 not Commit persist application state ≠ 481 commitpersist / 590 fincommit interchangeable：** 官方把 403 item 1 和 Commit 落盘应用状态分开。
- **Finalize 之后引擎才落盘 not finafter bundled ≠ 633 notlock / 634 notrecheck interchangeable：** 官方把 403 item 1 和 item 2 / item 3 分开；403 finafter unbundling 启动（632 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 之后引擎才落盘这三份 | 不是 already 已经交差 | 不是 persists not settled（587 item 3 / 616） |
| Finalize 之后引擎才落盘这三份 | 不是 already 落盘应用状态 | 不是 commitpersist（481） |
| Finalize 之后引擎才落盘这三份 | 不是 already finafter bundled | 不是落完再锁 not Commit lock（403 item 2 / 633） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量），必须分开 Finalize 之后引擎才落盘 是不是 already 已经交差 interchangeable / 335 finpersist interchangeable / 616 notpersist interchangeable / 33 four gates interchangeable、Finalize 之后引擎才落盘 是不是 already 落盘应用状态 interchangeable / 481 commitpersist interchangeable / 590 fincommit interchangeable / 467 finpersist interchangeable、Finalize 之后引擎才落盘 是不是 already finafter bundled interchangeable / 633 notlock interchangeable / 634 notrecheck interchangeable / 588 finlock interchangeable。可以跳过「看见回了 Finalize 就已经交差 interchangeable」。不要另写怎样落盘这三份。403 finafter unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样落盘这三份、怎样锁内存池、怎样再验、怎样开下一高。
- Finalize 之后 bundled。那是不变量 403。
- Finalize 之后落完再锁内存池 not Commit lock。那是不变量 403 item 2 余量 / 633。
- Finalize 之后 optional recheck unlock h+1 not Recheck。那是不变量 403 item 3 余量 / 634。
- CometBFT persists 这三份 not already settled。那是不变量 587 item 3 余量 / 616。
- Finalize 落盘禁令。那是不变量 335。
- Commit Usage persist signal。那是不变量 481。
- locks mempool not settled。那是不变量 588 item 1 余量 / 629。
