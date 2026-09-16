# 例：看见 locks mempool after persist / 看见 persist 之后才锁 is not already 已经是 Commit 锁 interchangeable / 已经解锁 interchangeable / 已经是 Recheck interchangeable / 已经 finlock bundled interchangeable

**层次**：实现 / FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量）/ not 631 notcommitlock interchangeable / not 310 commitlock interchangeable / not 592 finunlock interchangeable / not 591 finrecheck interchangeable / not 629 notsettled interchangeable / not 630 notoptional interchangeable」，不是 FinalizeBlock When locks mempool 正式三事 bundled（588），也不是 Commit 前上锁（310），也不是 Finalize 之后 bundled（403）。不要另写怎样锁内存池、怎样再验、怎样解锁。

## 官方三件事

规范把 FinalizeBlock When 第 7 步 _p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions（发生在 When 第 6 步 persist tx outputs / AppHash / ResultsHash 之后、第 8 步 `Commit` 之前）和「已经是已经是 Commit 锁 interchangeable / 已经是已经解锁 interchangeable / 已经是 Recheck interchangeable / 已经是 finlock bundled interchangeable」分开写成三件独立的实现事，不是「看见 persist 之后才锁 就已经 Commit 锁、就已经解锁、就已经 Recheck interchangeable」一件事：

1. **看见 locks mempool after persist / 看见 persist 之后才锁 / 看见 When 第 7 步 locks mempool after persist is not already 已经是 Commit 锁 interchangeable / Commit 前上锁 interchangeable / Commit RPC 锁 interchangeable / 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable，也不是已经 Commit 前上锁 bundled（310 余量） interchangeable / 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable / 481 commitpersist interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist bundled（590 余量） interchangeable / 590 fincommit interchangeable / 481 commitpersist interchangeable / 335 finpersist interchangeable / 467 finreturn interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 2 落完再锁内存池 interchangeable / 403 item 3 optional recheck interchangeable / 587 finreturn interchangeable。**  
   官方 When 第 7 步写：_p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions。发生在 When 第 6 步 persist tx outputs / AppHash / ResultsHash 之后、第 8 步 `Commit` 之前。看见 persist 之后才锁，不是已经默认全局锁那种 Commit 前上锁、Commit 里等广播会停死（310） interchangeable——588 bundled 第三件事常被写成「看见 locks mempool after persist 就已经 Commit 锁 interchangeable」，本页从 588 item 3 侧钉 not Commit lock 单句。看见 When 第 7 步，不是已经 Commit 前上锁 bundled（310） interchangeable——310 另钉默认锁 / Commit RPC 锁 / Commit 里等 broadcast_tx，本页钉 588 item 3 第一件事。看见 locks mempool after persist，不是已经 calls Commit instruct persist（590） interchangeable——590 钉 When 第 8 步，本页钉 persist 之后才锁 not Commit lock 单句。
2. **看见 locks mempool after persist / 看见 persist 之后才锁 is not already 已经解锁 interchangeable / 已经是 Recheck interchangeable / unlocks the mempool interchangeable / 592 finunlock interchangeable / 591 finrecheck interchangeable / 312 checktxtype RECHECK interchangeable / 403 finafter item 3 optional recheck interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable，也不是已经 FinalizeBlock When unlocks the mempool bundled（592 余量） interchangeable / 592 finunlock interchangeable / 592 item 1 newly received can now be checked interchangeable / 592 item 2 not Commit lock interchangeable / 592 item 3 not optional recheck interchangeable，也不是已经 FinalizeBlock When optional recheck bundled（591 余量） interchangeable / 591 finrecheck interchangeable / 591 item 1 outstanding vs newly persisted interchangeable / 591 item 2 not unlock interchangeable / 591 item 3 not Commit lock interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 3 optional recheck unlocks mempool interchangeable / 312 checktxtype interchangeable / 484 chktxtype interchangeable。**  
   官方把 When 第 7 步锁内存池和 When 第 9–10 步 optional recheck / unlocks the mempool 分开——588 item 3 常与 592 / 591 混成「看见 locks mempool after persist 就已经解锁 interchangeable / 就已经 Recheck interchangeable」，本页钉 not unlock / not Recheck 单句。看见 When 第 7 步，不是已经 unlocks the mempool（592） interchangeable——592 另钉 When 第 10 步 newly received can now be checked，本页钉 588 item 3 第二件事。看见 persist 之后才锁，不是已经 optional recheck（591） interchangeable——591 另钉 When 第 9 步 outstanding vs newly persisted，本页钉 not Recheck 单句。
3. **看见 locks mempool after persist / 看见 persist 之后才锁 is not already finlock bundled（588） interchangeable / 已经 CometBFT locks the mempool interchangeable / 已经 no calls to CheckTx on new transactions interchangeable / 588 finlock item 1 interchangeable / 588 finlock item 2 interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable / 373 checktxopt interchangeable / 310 commitlock interchangeable / 312 checktxtype interchangeable，也不是已经 CometBFT locks the mempool not already settled bundled（588 item 1 余量 / 629） interchangeable / 629 notsettled interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable，也不是已经 no calls to CheckTx on new transactions not CheckTx optional bundled（588 item 2 余量 / 630） interchangeable / 630 notoptional interchangeable / 373 checktxopt interchangeable / 312 checktxtype interchangeable / 489 chktxcodereject interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量） interchangeable / 587 finreturn interchangeable / 616 notpersist interchangeable / 478 finpersist interchangeable / 605 notpersist interchangeable。**  
   官方把 588 finlock bundled 三事里的 locks mempool after persist 和 locks the mempool / no calls to CheckTx on new transactions 分开——588 bundled 常与 item 1 / item 2 混成「看见 persist 之后才锁 就已经 finlock bundled interchangeable」，本页钉 588 item 3 第三件事。看见 locks mempool after persist，不是已经 CometBFT locks the mempool not already settled（588 item 1 余量 / 629） interchangeable——629 另钉 not settled / not four gates，本页钉 item 3 单句。看见 When 第 7 步，不是已经 no calls to CheckTx on new transactions not CheckTx optional（588 item 2 余量 / 630） interchangeable——630 另钉 not CheckTx optional / not 进池，本页钉 not finlock bundled 单句。588 finlock unbundling 在本页 item 3 完成。

怎样锁内存池、怎样再验池里剩下的、怎样解锁是规范里的做法，本页不抄。FinalizeBlock When locks mempool 正式三事 bundled（588）、CometBFT locks the mempool not already settled（588 item 1 余量 / 629）、no calls to CheckTx on new transactions not CheckTx optional（588 item 2 余量 / 630）、Finalize 之后 bundled（403）、Commit 前上锁（310）、optional recheck（591）、unlocks the mempool（592）、CheckTx Type（312）、CometBFT persists 这三份（587）是另外那套，本页不抄。

## 官方为什么这样拆

- **locks mempool after persist not Commit lock ≠ 310 commitlock / 590 fincommit interchangeable：** 官方把 When 第 7 步 persist 之后才锁 和 Commit RPC 锁 / Commit 前上锁 分开。
- **locks mempool after persist not unlock / not Recheck ≠ 592 finunlock / 591 finrecheck interchangeable：** 官方把 588 item 3 和 When 第 9–10 步 optional recheck / unlock 分开。
- **locks mempool after persist not finlock bundled ≠ 629 notsettled / 630 notoptional interchangeable：** 官方把 588 item 3 和 item 1 / item 2 分开；588 finlock unbundling 完成（631 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| locks mempool after persist | 不是 already Commit 锁 | 不是 Commit 前上锁（310） |
| locks mempool after persist | 不是 already unlock / Recheck | 不是 unlocks mempool（592） |
| locks mempool after persist | 不是 already finlock bundled | 不是 no CheckTx optional（588 item 2 / 630） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量），必须分开 locks mempool after persist 是不是 already Commit lock interchangeable / 310 commitlock interchangeable / 590 fincommit interchangeable、locks mempool after persist 是不是 already unlock interchangeable / 592 finunlock interchangeable / 591 finrecheck interchangeable / 312 checktxtype RECHECK interchangeable、locks mempool after persist 是不是 already finlock bundled interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable / 588 finlock item 1 locks the mempool interchangeable。可以跳过「看见 persist 之后才锁 就已经 Commit 锁 interchangeable」。不要另写怎样锁内存池。588 finlock unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样锁内存池、怎样再验池里剩下的、怎样解锁。
- FinalizeBlock When locks mempool 正式三事 bundled。那是不变量 588。
- CometBFT locks the mempool not already settled。那是不变量 588 item 1 余量 / 629。
- no calls to CheckTx on new transactions not CheckTx optional。那是不变量 588 item 2 余量 / 630。
- Commit 前上锁就已经解锁。那是不变量 310。
- optional recheck。那是不变量 591。
- unlocks the mempool。那是不变量 592。
- RECHECK 就已经是新交易。那是不变量 312。
- Finalize 之后 bundled。那是不变量 403。
- CometBFT persists 这三份。那是不变量 587。
