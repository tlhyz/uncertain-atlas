# 例：看见可选再验池里剩下的、再解锁、再开下一高 round 0 / 看见再验了 is not already 已经是 Recheck interchangeable / 已经解锁 interchangeable / 已经 finafter bundled interchangeable

**层次**：实现 / FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 9–11。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量）/ not 634 notrecheck interchangeable / not 591 finrecheck interchangeable / not 592 finunlock interchangeable / not 593 finh1 interchangeable / not 312 checktxtype interchangeable / not 632 notsettled interchangeable / not 633 notlock interchangeable」，不是 Finalize 之后 bundled（403），也不是 optional recheck bundled（591），也不是 unlocks mempool（592）。不要另写怎样再验、怎样解锁、怎样开下一高。

## 官方三件事

规范把 When 第 9–11 步 optionally re-checks all outstanding transactions in the mempool against the newly persisted Application state、unlocks the mempool — newly received transactions can now be checked、starts consensus for height _h+1_, round 0（发生在 When 第 8 步 `Commit` 之后）和「已经是已经是 Recheck interchangeable / 已经是已经解锁 interchangeable / 已经是 finafter bundled interchangeable」分开写成三件独立的实现事，不是「看见可选再验池里剩下的、再解锁、再开下一高 round 0 就已经 Recheck、就已经解锁、就已经 finafter bundled interchangeable」一件事：

1. **看见可选再验池里剩下的、再解锁、再开下一高 round 0 / 看见 optionally re-checks / outstanding transactions in the mempool / against newly persisted Application state / 看见 When 第 9 步 optional recheck is not already 已经是 Recheck interchangeable / CheckTx Type RECHECK interchangeable / 312 checktxtype interchangeable / 484 chktxtype interchangeable / 591 finrecheck interchangeable / 591 item 3 not Type=RECHECK interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 634 notrecheck interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable，也不是已经 FinalizeBlock When optional recheck bundled（591 余量） interchangeable / 591 finrecheck interchangeable / 591 item 1 not must recheck interchangeable / 591 item 2 not new transactions interchangeable / 591 item 3 not CheckTxState / ExecuteTxState interchangeable，也不是已经 CheckTx Type bundled（312 余量） interchangeable / 312 checktxtype interchangeable / 484 chktxtype interchangeable / 312 item 1 RECHECK not new txs interchangeable / 312 item 2 not optional recheck interchangeable / 484 chktxtype RECHECK interchangeable，也不是已经 RECHECK 就已经是新交易 bundled（312 item 1 余量） interchangeable / 312 checktxtype interchangeable / 588 no calls on new transactions interchangeable / 630 notoptional interchangeable / 373 checktxopt interchangeable。**  
   官方 When 第 9 步写：_p_'s CometBFT, **optionally**, re-checks all outstanding transactions in the mempool against the newly persisted Application state。发生在 When 第 8 步 calls `Commit` 之后、第 10 步 unlocks the mempool 之前。看见 optional recheck，不是已经 `CheckTxRequest` 的 `Type` 标明 `RECHECK`（312 / 484） interchangeable——403 bundled 第三件事常被写成「看见再验了 就已经 Recheck interchangeable」，本页从 403 item 3 侧钉 not Recheck 单句。看见 When 第 9 步，不是已经 optional recheck bundled（591） interchangeable——591 另钉 not must recheck / outstanding vs new / not Type=RECHECK，本页钉 403 item 3 第一件事。看见 against newly persisted，不是已经 CheckTx 只是弱过滤器（339） interchangeable——339 另钉 Process 对付无效块，本页钉 not Recheck 单句。
2. **看见可选再验池里剩下的、再解锁、再开下一高 round 0 / 看见 unlocks the mempool / newly received transactions can now be checked / 看见 When 第 10 步 unlock is not already 已经解锁 interchangeable / 已经能往下走 interchangeable / 592 finunlock interchangeable / 592 item 1 newly received can now be checked interchangeable / 592 item 2 not Commit lock interchangeable / 592 item 3 not optional recheck interchangeable / 631 notcommitlock item 2 not unlock interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 634 notrecheck interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable，也不是已经 FinalizeBlock When unlocks the mempool bundled（592 余量） interchangeable / 592 finunlock interchangeable / 592 item 1 newly received interchangeable / 592 item 2 not Commit lock interchangeable / 592 item 3 not optional recheck interchangeable，也不是已经 Commit 前上锁就已经解锁 bundled（310 余量） interchangeable / 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable / 481 commitpersist interchangeable，也不是已经 locks mempool after persist not unlock bundled（588 item 3 余量 / 631） interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable。**  
   官方把 When 第 10 步 unlocks the mempool 和 When 第 9 步 optional recheck、第 11 步 starts consensus for height _h+1_, round 0 分开——403 item 3 常与 592 / 631 混成「看见解锁了 就已经 unlock interchangeable / 就已经能往下走 interchangeable」，本页钉 not unlock 单句。看见 When 第 10 步，不是已经 unlocks the mempool（592） interchangeable——592 另钉 When 第 10 步 newly received can now be checked，本页钉 403 item 3 第二件事。看见 unlock after optional recheck，不是已经 Commit 前上锁（310） interchangeable——310 另钉默认锁 / Commit RPC 锁，本页钉 not unlock 单句。
3. **看见可选再验池里剩下的、再解锁、再开下一高 round 0 / 看见 starts consensus for height _h+1_, round 0 / 看见 When 第 9–11 步 recheck+unlock+h+1 is not already finafter bundled（403） interchangeable / 已经 Finalize 之后引擎才落盘 interchangeable / 已经落完再锁内存池 interchangeable / 403 finafter item 1 interchangeable / 403 finafter item 2 interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable / 588 finlock interchangeable / 631 notcommitlock interchangeable，也不是已经 Finalize 之后 bundled（403） interchangeable / 634 notrecheck interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable，也不是已经 Finalize 之后引擎才落盘 not already settled bundled（403 item 1 余量 / 632） interchangeable / 632 notsettled interchangeable / 616 notpersist interchangeable / 335 finpersist interchangeable / 481 commitpersist interchangeable / 590 fincommit interchangeable，也不是已经 Finalize 之后落完再锁内存池 not Commit lock bundled（403 item 2 余量 / 633） interchangeable / 633 notlock interchangeable / 588 finlock interchangeable / 631 notcommitlock interchangeable / 310 commitlock interchangeable，也不是已经 starts consensus for height h+1 round 0 bundled（593 余量） interchangeable / 593 finh1 interchangeable / 593 item 1 not settled interchangeable / 593 item 2 not next_block_delay interchangeable / 593 item 3 not unlock interchangeable / 479 fintrigger interchangeable / 478 finpersist interchangeable。**  
   官方把 403 finafter bundled 三事里的 optional recheck unlock h+1 和 Finalize 之后引擎才落盘 / 落完再锁内存池 分开——403 bundled 常与 item 1 / item 2 混成「看见再验了 就已经 finafter bundled interchangeable」，本页钉 403 item 3 第三件事。看见 When 第 11 步，不是已经 starts consensus for height h+1 round 0（593） interchangeable——593 另钉 not settled / not next_block_delay / not unlock，本页钉 not finafter bundled 单句。看见 recheck+unlock+h+1，不是已经 Finalize 之后引擎才落盘（632） interchangeable——632 另钉 item 1，本页钉 item 3 单句。403 finafter unbundling 在本页 item 3 完成。

怎样再验、怎样解锁、怎样开下一高是规范里的做法，本页不抄。Finalize 之后 bundled（403）、Finalize 之后引擎才落盘 not already settled（403 item 1 余量 / 632）、Finalize 之后落完再锁内存池 not Commit lock（403 item 2 余量 / 633）、optional recheck（591）、unlocks the mempool（592）、starts consensus for height h+1 round 0（593）、CheckTx Type（312 / 484）、locks mempool after persist not unlock（588 item 3 / 631）是另外那套，本页不抄。

## 官方为什么这样拆

- **optional recheck unlock h+1 not Recheck ≠ 591 finrecheck / 312 checktxtype interchangeable：** 官方把 403 item 3 和 When 第 9 步 optional recheck / Request type RECHECK 分开。
- **optional recheck unlock h+1 not unlock ≠ 592 finunlock / 631 notcommitlock interchangeable：** 官方把 403 item 3 和 When 第 10 步 unlock / finlock item 3 not unlock 分开。
- **optional recheck unlock h+1 not finafter bundled ≠ 632 notsettled / 633 notlock interchangeable：** 官方把 403 item 3 和 item 1 / item 2 分开；403 finafter unbundling 完成（634 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 可选再验池里剩下的、再解锁、再开下一高 round 0 | 不是 already Recheck | 不是 optional recheck（591） |
| 可选再验池里剩下的、再解锁、再开下一高 round 0 | 不是 already unlock | 不是 unlocks mempool（592） |
| 可选再验池里剩下的、再解锁、再开下一高 round 0 | 不是 already finafter bundled | 不是 Finalize 之后引擎才落盘 not settled（403 item 1 / 632） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量），必须分开 optional recheck unlock h+1 是不是 already Recheck interchangeable / 591 finrecheck interchangeable / 312 checktxtype RECHECK interchangeable / 484 chktxtype interchangeable、optional recheck unlock h+1 是不是 already unlock interchangeable / 592 finunlock interchangeable / 631 notcommitlock item 2 not unlock interchangeable / 310 commitlock interchangeable、optional recheck unlock h+1 是不是 already finafter bundled interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable / 593 finh1 interchangeable / 403 finafter item 1 落盘 interchangeable / 403 finafter item 2 落完再锁 interchangeable。可以跳过「看见再验了 就已经 Recheck interchangeable」。不要另写怎样再验。403 finafter unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样再验、怎样解锁、怎样开下一高。
- Finalize 之后 bundled。那是不变量 403。
- Finalize 之后引擎才落盘 not already settled。那是不变量 403 item 1 余量 / 632。
- Finalize 之后落完再锁内存池 not Commit lock。那是不变量 403 item 2 余量 / 633。
- optional recheck。那是不变量 591。
- unlocks the mempool。那是不变量 592。
- starts consensus for height h+1 round 0。那是不变量 593。
- CheckTx Type / RECHECK。那是不变量 312 / 484。
- locks mempool after persist not unlock。那是不变量 588 item 3 余量 / 631。
