# 例：看见 optionally re-checks / 看见 When 第 9 步 optional recheck is not already 已经必须再验 interchangeable / 已经交差 interchangeable / 已经 finrecheck bundled interchangeable

**层次**：实现 / FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 9。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量）/ not 635 finrecheck-notmust interchangeable / not 634 notrecheck interchangeable / not 403 finafter interchangeable / not 312 checktxtype interchangeable / not 636 notoutstanding interchangeable / not 637 nottype interchangeable」，不是 FinalizeBlock When optional recheck 正式三事 bundled（591），也不是 Finalize 之后 bundled（403），也不是 CheckTx Type（312 / 484）。不要另写怎样再验、怎样填 Type、怎样解锁。

## 官方三件事

规范把 When 第 9 步 _p_'s CometBFT, **optionally**, re-checks all outstanding transactions in the mempool against the newly persisted Application state 和「已经是已经必须再验 interchangeable / 已经是已经交差 interchangeable / 已经是 finrecheck bundled interchangeable」分开写成三件独立的实现事，不是「看见 When 第 9 步 optional recheck 就已经必须再验、就已经交差、就已经 finrecheck bundled interchangeable」一件事：

1. **看见 optionally re-checks / 看见 When 第 9 步 optional recheck / 看见 optionally, re-checks is not already 已经必须再验 interchangeable / 已经必须再验才能开下一高 interchangeable / 312 checktxtype RECHECK interchangeable / 484 chktxtype RECHECK interchangeable / 634 notrecheck interchangeable / 403 finafter item 3 interchangeable，也不是已经 FinalizeBlock When optional recheck 正式三事 bundled（591） interchangeable / 635 finrecheck-notmust interchangeable / 591 finrecheck interchangeable / 636 notoutstanding interchangeable / 637 nottype interchangeable，也不是已经 Finalize 之后 optional recheck unlock h+1 not Recheck bundled（403 item 3 余量 / 634） interchangeable / 634 notrecheck interchangeable / 592 finunlock interchangeable / 593 finh1 interchangeable / 632 notsettled interchangeable，也不是已经 CheckTx Type bundled（312 余量） interchangeable / 312 checktxtype interchangeable / 484 chktxtype interchangeable / 312 item 1 RECHECK not new txs interchangeable / 312 item 2 not optional recheck interchangeable，也不是已经 CheckTx 过了就永远有效 bundled（301 余量） interchangeable / 301 mempool interchangeable / 339 checktxweak interchangeable / 588 no calls on new transactions interchangeable。**  
   官方 When 第 9 步写：_p_'s CometBFT, **optionally**, re-checks …。发生在 When 第 8 步 calls `Commit` 之后、第 10 步 unlocks the mempool 之前。看见 optionally，不是已经必须再验才能开下一高 interchangeable——591 bundled 第一件事常被写成「看见 When 第 9 步再验了 就已经必须再验 interchangeable / 就已经 Recheck interchangeable」，本页从 591 item 1 侧钉 not must recheck 单句。看见 When 第 9 步，不是已经 `CheckTxRequest` 的 `Type` 标明 `RECHECK`（312 / 484） interchangeable——312 / 484 另钉 Request type，本页钉 optional 不是 must 单句。看见 optional recheck，不是已经 Finalize 之后 optional recheck unlock h+1 not Recheck（403 item 3 余量 / 634） interchangeable——634 另钉 403 item 3 not Recheck，本页钉 591 item 1 第一件事。
2. **看见 optionally re-checks / 看见 When 第 9 步 optional recheck is not already 已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 601 notsettled interchangeable，也不是已经 FinalizeBlock When optional recheck 正式三事 bundled（591） interchangeable / 635 finrecheck-notmust interchangeable / 591 finrecheck interchangeable / 636 notoutstanding interchangeable / 637 nottype interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 1 引擎才落盘这三份 interchangeable / 403 item 2 落完再锁内存池 interchangeable / 403 item 3 optional recheck interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 594 not settled interchangeable / 632 notsettled interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量） interchangeable / 587 finreturn interchangeable / 616 notpersist interchangeable / 481 commitpersist interchangeable / 467 finpersist interchangeable。**  
   官方把 When 第 9 步 optional recheck 和 Finalize + Commit 交差 / 四门已经结算分开——591 item 1 常与 33 / 335 混成「看见 When 第 9 步再验了 就已经交差 interchangeable」，本页钉 not already settled 单句。看见 optionally re-checks，不是已经 Finalize + Commit 那种已经交差（33） interchangeable——33 钉四门已经结算，本页钉 591 item 1 第二件事。看见 When 第 9 步，不是已经 Finalize 之后 bundled（403）那种落完就锁 / 已经交差 interchangeable——403 另钉 Finalize 之后全流程，本页钉 not already settled 单句。
3. **看见 optionally re-checks / 看见 When 第 9 步 optional recheck is not already finrecheck bundled（591） interchangeable / 已经 all outstanding transactions in the mempool interchangeable / 已经 against newly persisted Application state interchangeable / 591 finrecheck item 2 interchangeable / 591 finrecheck item 3 interchangeable / 636 notoutstanding interchangeable / 637 nottype interchangeable / 634 notrecheck interchangeable，也不是已经 FinalizeBlock When optional recheck 正式三事 bundled（591） interchangeable / 635 finrecheck-notmust interchangeable / 591 finrecheck interchangeable / 301 mempool interchangeable / 588 no calls on new transactions interchangeable / 312 checktxtype RECHECK interchangeable，也不是已经 all outstanding transactions in the mempool not new transactions bundled（591 item 2 余量 / 636） interchangeable / 636 notoutstanding interchangeable / 588 finlock interchangeable / 301 mempool interchangeable / 339 checktxweak interchangeable，也不是已经 against newly persisted Application state not Type=RECHECK bundled（591 item 3 余量 / 637） interchangeable / 637 nottype interchangeable / 312 checktxtype interchangeable / 484 chktxtype interchangeable / 339 checktxweak interchangeable / 312 item 2 not optional recheck interchangeable，也不是已经 Finalize 之后 optional recheck unlock h+1 not Recheck bundled（403 item 3 余量 / 634） interchangeable / 634 notrecheck interchangeable / 592 finunlock interchangeable / 593 finh1 interchangeable / 632 notsettled interchangeable。**  
   官方把 591 finrecheck bundled 三事里的 optionally re-checks 和 all outstanding transactions in the mempool / against newly persisted Application state 分开——591 bundled 常与 item 2 / item 3 混成「看见 When 第 9 步再验了 就已经 finrecheck bundled interchangeable」，本页钉 591 item 1 第三件事。看见 optionally re-checks，不是已经 all outstanding transactions in the mempool not new transactions（591 item 2 余量 / 636） interchangeable——636 另钉 outstanding vs new，本页钉 item 1 单句。看见 When 第 9 步，不是已经 against newly persisted Application state not Type=RECHECK（591 item 3 余量 / 637） interchangeable——637 另钉 not Type=RECHECK / not CheckTxState，本页钉 not finrecheck bundled 单句。591 finrecheck unbundling 在本页 item 1 启动。

怎样再验、怎样填 Type、怎样解锁是规范里的做法，本页不抄。FinalizeBlock When optional recheck 正式三事 bundled（591）、all outstanding transactions in the mempool not new transactions（591 item 2 余量 / 636）、against newly persisted Application state not Type=RECHECK（591 item 3 余量 / 637）、Finalize 之后 optional recheck unlock h+1 not Recheck（403 item 3 余量 / 634）、Finalize 之后 bundled（403）、CheckTx Type（312 / 484）、locks mempool（588）、CheckTx 过了就永远有效（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **optionally re-checks not must recheck ≠ 312 checktxtype / 634 notrecheck interchangeable：** 官方把 When 第 9 步 optional 和必须再验 / Request type RECHECK 分开。
- **optionally re-checks not already settled ≠ 33 four gates / 403 finafter interchangeable：** 官方把 591 item 1 和已经交差 / Finalize 之后 bundled 分开。
- **optionally re-checks not finrecheck bundled ≠ 636 notoutstanding / 637 nottype interchangeable：** 官方把 591 item 1 和 item 2 / item 3 分开；591 finrecheck unbundling 启动（635 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| optionally re-checks | 不是 already must recheck | 不是 optional recheck（591） |
| optionally re-checks | 不是 already settled / 交差 | 不是 finafter bundled（403） |
| optionally re-checks | 不是 already finrecheck bundled | 不是 outstanding vs new（591 item 2 / 636） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量），必须分开 optionally re-checks 是不是 already must recheck interchangeable / 312 checktxtype RECHECK interchangeable / 484 chktxtype interchangeable / 634 notrecheck interchangeable、optionally re-checks 是不是 already settled / 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable、optionally re-checks 是不是 already finrecheck bundled interchangeable / 636 notoutstanding interchangeable / 637 nottype interchangeable / 301 mempool interchangeable / 588 no calls on new transactions interchangeable。可以跳过「看见 When 第 9 步再验了 就已经必须再验 interchangeable」。不要另写怎样再验。591 finrecheck unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样再验、怎样填 Type、怎样解锁。
- FinalizeBlock When optional recheck 正式三事 bundled。那是不变量 591。
- all outstanding transactions in the mempool not new transactions。那是不变量 591 item 2 余量 / 636。
- against newly persisted Application state not Type=RECHECK。那是不变量 591 item 3 余量 / 637。
- Finalize 之后 optional recheck unlock h+1 not Recheck。那是不变量 403 item 3 余量 / 634。
- Finalize 之后 bundled。那是不变量 403。
- CheckTx Type / RECHECK。那是不变量 312 / 484。
- locks mempool / no new CheckTx。那是不变量 588。
- CheckTx 过了就永远有效。那是不变量 301。
