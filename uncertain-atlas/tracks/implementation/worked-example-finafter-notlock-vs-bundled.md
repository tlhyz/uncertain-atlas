# 例：看见落完再锁内存池、新交易不进 CheckTx / 看见锁了 is not already 已经是 Commit 锁 interchangeable / 已经交差 interchangeable / 已经 finafter bundled interchangeable

**层次**：实现 / FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量）/ not 633 notlock interchangeable / not 310 commitlock interchangeable / not 632 notsettled interchangeable / not 634 notrecheck interchangeable / not 631 notcommitlock interchangeable」，不是 Finalize 之后 bundled（403），也不是 Commit 前上锁（310），也不是 locks mempool after persist bundled（588 item 3 / 631）。不要另写怎样锁内存池、怎样再验、怎样解锁。

## 官方三件事

规范把 When 第 7 步 _p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions（发生在 When 第 6 步 persist tx outputs / AppHash / ResultsHash 之后、第 8 步 `Commit` 之前）和「已经是已经是 Commit 锁 interchangeable / 已经是已经交差 interchangeable / 已经是 finafter bundled interchangeable」分开写成三件独立的实现事，不是「看见落完再锁内存池、新交易不进 CheckTx 就已经 Commit 锁、就已经交差、就已经 finafter bundled interchangeable」一件事：

1. **看见落完再锁内存池、新交易不进 CheckTx / 看见 locks the mempool / no calls to CheckTx on new transactions / 看见 When 第 7 步 落完再锁 is not already 已经是 Commit 锁 interchangeable / Commit 前上锁 interchangeable / Commit RPC 锁 interchangeable / 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 633 notlock interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 634 notrecheck interchangeable，也不是已经 Commit 前上锁 bundled（310 余量） interchangeable / 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable / 481 commitpersist interchangeable，也不是已经 FinalizeBlock When locks mempool after persist not Commit lock bundled（588 item 3 余量 / 631） interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist bundled（590 余量） interchangeable / 590 fincommit interchangeable / 467 finpersist interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable。**  
   官方 When 第 7 步写：_p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions。发生在 When 第 6 步 persist tx outputs / AppHash / ResultsHash 之后、第 8 步 `Commit` 之前。看见落完再锁，不是已经默认全局锁那种 Commit 前上锁、Commit 里等广播会停死（310） interchangeable——403 bundled 第二件事常被写成「看见锁了 就已经 Commit 锁 interchangeable」，本页从 403 item 2 侧钉 not Commit lock 单句。看见 When 第 7 步，不是已经 Commit 前上锁 bundled（310） interchangeable——310 另钉默认锁 / Commit RPC 锁 / Commit 里等 broadcast_tx，本页钉 403 item 2 第一件事。看见 locks the mempool，不是已经 locks mempool after persist not Commit lock（588 item 3 余量 / 631） interchangeable——631 从 finlock bundled 侧钉同一 When 第 7 步，本页从 finafter bundled 侧钉 not Commit lock 单句。
2. **看见落完再锁内存池、新交易不进 CheckTx / 看见锁了 is not already 已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 632 notsettled interchangeable / 601 notsettled interchangeable / 587 finreturn interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 633 notlock interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 634 notrecheck interchangeable，也不是已经 FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled bundled（403 item 1 余量 / 632） interchangeable / 632 notsettled interchangeable / 616 notpersist interchangeable / 335 finpersist interchangeable / 481 commitpersist interchangeable / 590 fincommit interchangeable，也不是已经 CometBFT locks the mempool not already settled bundled（588 item 1 余量 / 629） interchangeable / 629 notsettled interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 606 notoutputs interchangeable / 362 finwhen interchangeable。**  
   官方把 When 第 7 步落完再锁内存池和已经交差 / Finalize 改了就已经落盘分开——403 item 2 常与 632 / 335 / 629 混成「看见锁了 就已经交差 interchangeable」，本页钉 not already settled 单句。看见 When 第 7 步，不是已经 Finalize 之后引擎才落盘 not already settled（403 item 1 余量 / 632） interchangeable——632 另钉 When 第 6 步 persist 这三份，本页钉 403 item 2 第二件事。看见 locks the mempool，不是已经 CometBFT locks the mempool not already settled（588 item 1 余量 / 629） interchangeable——629 从 finlock bundled 侧钉 not settled，本页从 finafter bundled 侧钉 not already settled 单句。
3. **看见落完再锁内存池、新交易不进 CheckTx / 看见锁了 is not already finafter bundled（403） interchangeable / 已经 Finalize 之后引擎才落盘 interchangeable / 已经 optional recheck unlock h+1 interchangeable / 403 finafter item 1 interchangeable / 403 finafter item 3 interchangeable / 632 notsettled interchangeable / 634 notrecheck interchangeable / 588 finlock interchangeable / 631 notcommitlock interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 633 notlock interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 634 notrecheck interchangeable，也不是已经 Finalize 之后 optional recheck unlock h+1 not Recheck bundled（403 item 3 余量 / 634） interchangeable / 634 notrecheck interchangeable / 591 finrecheck interchangeable / 592 finunlock interchangeable / 593 finh1 interchangeable / 312 checktxtype RECHECK interchangeable，也不是已经 FinalizeBlock When locks mempool after persist not Commit lock bundled（588 item 3 余量 / 631） interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable / 310 commitlock interchangeable，也不是已经 FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional bundled（588 item 2 余量 / 630） interchangeable / 630 notoptional interchangeable / 373 checktxopt interchangeable / 312 checktxtype interchangeable / 489 chktxcodereject interchangeable。**  
   官方把 403 finafter bundled 三事里的落完再锁内存池、新交易不进 CheckTx 和 Finalize 之后引擎才落盘 / optional recheck unlock h+1 分开——403 bundled 常与 item 1 / item 3 混成「看见锁了 就已经 finafter bundled interchangeable」，本页钉 403 item 2 第三件事。看见 When 第 7 步，不是已经 Finalize 之后引擎才落盘 not already settled（403 item 1 余量 / 632） interchangeable——632 另钉 item 1，本页钉 item 2 单句。看见 locks the mempool，不是已经 optional recheck unlock h+1 not Recheck（403 item 3 余量 / 634） interchangeable——634 另钉 not Recheck / not unlock / not h+1 round 0，本页钉 not finafter bundled 单句。403 finafter unbundling 在本页 item 2 续。

怎样锁内存池、怎样再验池里剩下的、怎样解锁是规范里的做法，本页不抄。Finalize 之后 bundled（403）、Finalize 之后引擎才落盘 not already settled（403 item 1 余量 / 632）、Finalize 之后 optional recheck unlock h+1 not Recheck（403 item 3 余量 / 634）、locks mempool after persist not Commit lock（588 item 3 余量 / 631）、Commit 前上锁（310）、CometBFT locks the mempool not already settled（588 item 1 余量 / 629）、no calls to CheckTx on new transactions not CheckTx optional（588 item 2 余量 / 630）是另外那套，本页不抄。

## 官方为什么这样拆

- **落完再锁内存池 not Commit lock ≠ 310 commitlock / 631 notcommitlock interchangeable：** 官方把 When 第 7 步落完再锁 和 Commit RPC 锁 / Commit 前上锁 / finlock item 3 分开。
- **落完再锁内存池 not already settled ≠ 632 notsettled / 629 notsettled interchangeable：** 官方把 403 item 2 和 item 1 / finlock item 1 分开。
- **落完再锁内存池 not finafter bundled ≠ 634 notrecheck / 632 notsettled interchangeable：** 官方把 403 item 2 和 item 3 / item 1 分开；403 finafter unbundling 续（633 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 落完再锁内存池、新交易不进 CheckTx | 不是 already Commit 锁 | 不是 Commit 前上锁（310） |
| 落完再锁内存池、新交易不进 CheckTx | 不是 already 已经交差 | 不是 Finalize 之后引擎才落盘 not settled（403 item 1 / 632） |
| 落完再锁内存池、新交易不进 CheckTx | 不是 already finafter bundled | 不是 optional recheck unlock h+1 not Recheck（403 item 3 / 634） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量），必须分开落完再锁内存池 是不是 already Commit lock interchangeable / 310 commitlock interchangeable / 631 notcommitlock interchangeable / 590 fincommit interchangeable、落完再锁内存池 是不是 already 已经交差 interchangeable / 632 notsettled interchangeable / 335 finpersist interchangeable / 629 notsettled interchangeable / 33 four gates interchangeable、落完再锁内存池 是不是 already finafter bundled interchangeable / 634 notrecheck interchangeable / 403 finafter item 1 落盘 interchangeable / 403 finafter item 3 optional recheck interchangeable / 588 finlock interchangeable。可以跳过「看见锁了 就已经 Commit 锁 interchangeable」。不要另写怎样锁内存池。403 finafter unbundling 在本页 item 2 续。

## 本页不抄

- 怎样锁内存池、怎样再验池里剩下的、怎样解锁。
- Finalize 之后 bundled。那是不变量 403。
- Finalize 之后引擎才落盘 not already settled。那是不变量 403 item 1 余量 / 632。
- Finalize 之后 optional recheck unlock h+1 not Recheck。那是不变量 403 item 3 余量 / 634。
- locks mempool after persist not Commit lock。那是不变量 588 item 3 余量 / 631。
- Commit 前上锁就已经解锁。那是不变量 310。
- CometBFT locks the mempool not already settled。那是不变量 588 item 1 余量 / 629。
- no calls to CheckTx on new transactions not CheckTx optional。那是不变量 588 item 2 余量 / 630。
