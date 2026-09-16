# 例：看见 CometBFT locks the mempool / 看见引擎锁内存池 is not already 已经交差 interchangeable / 已经四门已经结算 interchangeable / 已经 finlock bundled interchangeable

**层次**：实现 / FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量）/ not 629 notsettled interchangeable / not 33 four gates interchangeable / not 403 finafter interchangeable / not 587 finreturn interchangeable / not 630 notoptional interchangeable / not 631 notcommitlock interchangeable」，不是 FinalizeBlock When locks mempool 正式三事 bundled（588），也不是 Finalize 之后 bundled（403），也不是 CometBFT persists 这三份 bundled（587）。不要另写怎样锁内存池、怎样再验、怎样解锁。

## 官方三件事

规范把 FinalizeBlock When 第 7 步 _p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions 和「已经是已经交差 interchangeable / 已经是四门已经结算 interchangeable / 已经是 finlock bundled interchangeable」分开写成三件独立的实现事，不是「看见锁了内存池 就已经交差、就已经四门已经结算、就已经 finlock bundled interchangeable」一件事：

1. **看见 CometBFT locks the mempool / 看见引擎锁内存池 / 看见 When 第 7 步 locks mempool is not already 已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 629 notsettled interchangeable / 588 finlock interchangeable / 630 notoptional interchangeable / 631 notcommitlock interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 1 引擎才落盘这三份 interchangeable / 403 item 2 落完再锁内存池 interchangeable / 403 item 3 optional recheck interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量） interchangeable / 587 finreturn interchangeable / 616 notpersist interchangeable / 481 commitpersist interchangeable / 467 finpersist interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 601 notsettled interchangeable / 594 not settled interchangeable。**  
   官方 When 第 7 步写：_p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions。发生在 When 第 6 步 persist tx outputs / AppHash / ResultsHash 之后、第 8 步 `Commit` 之前。看见锁了，不是已经 Finalize + Commit 那种已经交差（33） interchangeable——588 bundled 第一件事常被写成「看见锁了内存池 就已经交差 interchangeable」，本页从 588 item 1 侧钉 not already settled 单句。看见 When 第 7 步，不是已经 CometBFT persists 这三份（587）那种已经 Commit 落盘应用状态 interchangeable——587 另钉 When 第 6 步，本页钉 locks mempool not settled 单句。看见锁内存池，不是已经 Finalize 之后 bundled（403）那种落完就锁 / 已经交差 interchangeable——403 另钉 Finalize 之后全流程，本页钉 not already settled 单句。
2. **看见 CometBFT locks the mempool / 看见引擎锁内存池 is not already 已经四门已经结算 interchangeable / 已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable / 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 478 finpersist interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 629 notsettled interchangeable / 588 finlock interchangeable / 630 notoptional interchangeable / 631 notcommitlock interchangeable，也不是已经 FinalizeBlock equiv ABCI 1.0 not four gates settled bundled（586 item 1 余量 / 602） interchangeable / 602 notgates interchangeable / 586 finequiv interchangeable / 601 notsettled interchangeable / 363 finresp interchangeable，也不是已经 Finalize 回包义务 not four gates settled bundled（600 / 363 item 1 余量） interchangeable / 600 notgates interchangeable / 363 finresp interchangeable / 465 equiv bundled interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 335 finpersist interchangeable。**  
   官方把 When 第 7 步锁内存池和四门已经结算分开——588 item 1 常与 33 / 602 混成「看见锁了 就已经四门已经结算 interchangeable」，本页钉 not four gates settled 单句。看见 locks the mempool，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了（33） interchangeable——33 钉四门已经结算，本页钉 588 item 1 第二件事。看见 When 第 7 步，不是已经 persist decision（478 第 1 步） interchangeable——478 钉 When 第 1 步，本页钉 locks mempool not four gates 单句。
3. **看见 CometBFT locks the mempool / 看见引擎锁内存池 is not already finlock bundled（588） interchangeable / 已经 no calls to CheckTx on new transactions interchangeable / 已经 CheckTx 技术上可选 interchangeable / 已经 Commit 锁 interchangeable / 588 finlock item 2 interchangeable / 588 finlock item 3 interchangeable / 630 notoptional interchangeable / 631 notcommitlock interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 629 notsettled interchangeable / 588 finlock interchangeable / 373 checktxopt interchangeable / 310 commitlock interchangeable / 312 checktxtype interchangeable，也不是已经 no calls to CheckTx on new transactions not CheckTx optional bundled（588 item 2 余量 / 630） interchangeable / 630 notoptional interchangeable / 373 checktxopt interchangeable / 312 checktxtype interchangeable / 403 finafter item 3 optional recheck interchangeable，也不是已经 locks mempool after persist not Commit lock bundled（588 item 3 余量 / 631） interchangeable / 631 notcommitlock interchangeable / 310 commitlock interchangeable / 403 finafter item 3 unlocks mempool interchangeable / 312 checktxtype RECHECK interchangeable。**  
   官方把 588 finlock bundled 三事里的 locks the mempool 和 no calls to CheckTx on new transactions / locks mempool after persist 分开——588 bundled 常与 item 2 / item 3 混成「看见锁了内存池 就已经 finlock bundled interchangeable」，本页钉 588 item 1 第三件事。看见 locks the mempool，不是已经 no calls to CheckTx on new transactions not CheckTx optional（588 item 2 余量 / 630） interchangeable——630 另钉 not CheckTx optional / not 进池，本页钉 item 1 单句。看见 When 第 7 步，不是已经 locks mempool after persist not Commit lock（588 item 3 余量 / 631） interchangeable——631 另钉 not Commit lock / not unlock / not Recheck，本页钉 not finlock bundled 单句。

怎样锁内存池、怎样再验池里剩下的、怎样解锁是规范里的做法，本页不抄。FinalizeBlock When locks mempool 正式三事 bundled（588）、no calls to CheckTx on new transactions not CheckTx optional（588 item 2 余量 / 630）、locks mempool after persist not Commit lock（588 item 3 余量 / 631）、Finalize 之后 bundled（403）、Commit 前上锁（310）、CheckTx Type（312）、CheckTx 技术上可选（373）、CometBFT persists 这三份（587）是另外那套，本页不抄。

## 官方为什么这样拆

- **locks mempool not already settled ≠ 403 finafter / 587 finreturn interchangeable：** 官方把 When 第 7 步锁内存池和 Finalize + Commit 交差 / persists 这三份 分开。
- **locks mempool not four gates settled ≠ 33 four gates / 602 notgates interchangeable：** 官方把 588 item 1 和四门已经结算 / finequiv not four gates 分开。
- **locks mempool not finlock bundled ≠ 630 notoptional / 631 notcommitlock interchangeable：** 官方把 588 item 1 和 item 2 / item 3 分开；588 finlock unbundling 启动（629 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| locks the mempool | 不是 already settled / 交差 | 不是 finafter bundled（403） |
| locks the mempool | 不是 already four gates settled | 不是 four gates（33） |
| locks the mempool | 不是 already finlock bundled | 不是 not CheckTx optional（588 item 2 / 630） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量），必须分开 CometBFT locks the mempool 是不是 already settled / 交差 interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable、locks the mempool 是不是 already four gates settled interchangeable / 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable、locks the mempool 是不是 already finlock bundled interchangeable / 630 notoptional interchangeable / 631 notcommitlock interchangeable / 373 checktxopt interchangeable。可以跳过「看见锁了内存池 就已经交差 interchangeable」。不要另写怎样锁内存池。588 finlock unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样锁内存池、怎样再验池里剩下的、怎样解锁。
- FinalizeBlock When locks mempool 正式三事 bundled。那是不变量 588。
- no calls to CheckTx on new transactions not CheckTx optional。那是不变量 588 item 2 余量 / 630。
- locks mempool after persist not Commit lock。那是不变量 588 item 3 余量 / 631。
- Finalize 之后 bundled。那是不变量 403。
- Commit 前上锁就已经解锁。那是不变量 310。
- RECHECK 就已经是新交易。那是不变量 312。
- CheckTx 技术上可选。那是不变量 373。
- CometBFT persists 这三份。那是不变量 587。
