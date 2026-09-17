# 例：看见 unlocks the mempool / 看见 When 第 10 步解锁内存池 is not already 已经交差 interchangeable / 已经四门已经结算 interchangeable / 已经 finunlock bundled interchangeable

**层次**：实现 / FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 10。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量）/ not 638 finunlock-notsettled interchangeable / not 639 finunlock-notnewly interchangeable / not 640 finunlock-notcommitlock interchangeable / not 588 finlock interchangeable / not 403 finafter interchangeable」，不是 FinalizeBlock When unlocks mempool 正式三事 bundled（592），也不是 locks mempool（588），也不是 Finalize 之后 bundled（403）。不要另写怎样解锁、怎样再验、怎样开下一高。

## 官方三件事

规范把 When 第 10 步 _p_'s CometBFT unlocks the mempool — newly received transactions can now be checked 和「已经是已经交差 interchangeable / 已经是四门已经结算 interchangeable / 已经是 finunlock bundled interchangeable」分开写成三件独立的实现事，不是「看见 When 第 10 步解锁了 就已经交差、就已经四门已经结算、就已经 finunlock bundled interchangeable」一件事：

1. **看见 unlocks the mempool / 看见 When 第 10 步解锁内存池 / 看见 unlocks the mempool is not already 已经交差 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 601 notsettled interchangeable，也不是已经 FinalizeBlock When unlocks mempool 正式三事 bundled（592） interchangeable / 638 finunlock-notsettled interchangeable / 592 finunlock interchangeable / 639 finunlock-notnewly interchangeable / 640 finunlock-notcommitlock interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 3 optional recheck unlock h+1 interchangeable / 634 notrecheck interchangeable / 633 notlock interchangeable，也不是已经 CometBFT persists tx outputs / AppHash / ResultsHash bundled（587 余量） interchangeable / 587 finreturn interchangeable / 616 notpersist interchangeable / 632 notsettled interchangeable / 481 commitpersist interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 594 not settled interchangeable。**  
   官方 When 第 10 步写：_p_'s CometBFT unlocks the mempool。发生在 When 第 9 步 optional recheck 之后、第 11 步 starts consensus for height _h+1_, round 0 之前。看见 unlocks，不是已经 Finalize + Commit 那种已经交差（33） interchangeable——592 bundled 第一件事常被写成「看见 When 第 10 步解锁了 就已经交差 interchangeable」，本页从 592 item 1 侧钉 not already settled 单句。看见 When 第 10 步，不是已经 locks the mempool（588） interchangeable——588 钉 When 第 7 步锁，本页钉 When 第 10 步解锁 not settled 单句。看见 unlocks the mempool，不是已经 Finalize 之后 bundled（403）那种 recheck+unlock+h+1 整包 interchangeable——403 另钉 Finalize 之后全流程，本页钉 not already settled 单句。
2. **看见 unlocks the mempool / 看见 When 第 10 步解锁内存池 is not already 已经四门已经结算 interchangeable / 已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable / 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 478 finpersist interchangeable，也不是已经 FinalizeBlock When unlocks mempool 正式三事 bundled（592） interchangeable / 638 finunlock-notsettled interchangeable / 592 finunlock interchangeable / 639 finunlock-notnewly interchangeable / 640 finunlock-notcommitlock interchangeable，也不是已经 FinalizeBlock equiv ABCI 1.0 not four gates settled bundled（586 item 1 余量 / 602） interchangeable / 602 notgates interchangeable / 586 finequiv interchangeable / 601 notsettled interchangeable / 363 finresp interchangeable，也不是已经 Finalize 回包义务 not four gates settled bundled（600 / 363 item 1 余量） interchangeable / 600 notgates interchangeable / 363 finresp interchangeable / 465 equiv bundled interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 335 finpersist interchangeable。**  
   官方把 When 第 10 步解锁内存池和四门已经结算分开——592 item 1 常与 33 / 602 混成「看见 When 第 10 步解锁了 就已经四门已经结算 interchangeable」，本页钉 not four gates settled 单句。看见 unlocks the mempool，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了（33） interchangeable——33 钉四门已经结算，本页钉 592 item 1 第二件事。看见 When 第 10 步，不是已经 persist decision（478 第 1 步） interchangeable——478 钉 When 第 1 步，本页钉 unlocks not four gates 单句。
3. **看见 unlocks the mempool / 看见 When 第 10 步解锁内存池 is not already finunlock bundled（592） interchangeable / 已经 newly received transactions can now be checked interchangeable / 已经 When 第 10 步 unlock after optional recheck interchangeable / 592 finunlock item 2 interchangeable / 592 finunlock item 3 interchangeable / 639 finunlock-notnewly interchangeable / 640 finunlock-notcommitlock interchangeable / 634 notrecheck interchangeable，也不是已经 FinalizeBlock When unlocks mempool 正式三事 bundled（592） interchangeable / 638 finunlock-notsettled interchangeable / 592 finunlock interchangeable / 373 checktxopt interchangeable / 591 finrecheck interchangeable / 310 commitlock interchangeable，也不是已经 newly received transactions can now be checked not optional recheck bundled（592 item 2 余量 / 639） interchangeable / 639 finunlock-notnewly interchangeable / 591 finrecheck interchangeable / 636 finrecheck-notoutstanding interchangeable / 373 checktxopt interchangeable，也不是已经 When 第 10 步 unlock after optional recheck not Commit lock bundled（592 item 3 余量 / 640） interchangeable / 640 finunlock-notcommitlock interchangeable / 310 commitlock interchangeable / 593 finh1 interchangeable / 403 finafter item 3 optional recheck interchangeable / 631 notcommitlock interchangeable，也不是已经 Finalize 之后 optional recheck unlock h+1 not unlock bundled（403 item 3 余量 / 634） interchangeable / 634 notrecheck interchangeable / 633 notlock interchangeable / 592 finunlock interchangeable。**  
   官方把 592 finunlock bundled 三事里的 unlocks the mempool 和 newly received can now be checked / unlock after optional recheck 分开——592 bundled 常与 item 2 / item 3 混成「看见 When 第 10 步解锁了 就已经 finunlock bundled interchangeable」，本页钉 592 item 1 第三件事。看见 unlocks the mempool，不是已经 newly received transactions can now be checked not optional recheck（592 item 2 余量 / 639） interchangeable——639 另钉 not optional recheck / not CheckTx optional，本页钉 item 1 单句。看见 When 第 10 步，不是已经 unlock after optional recheck not Commit lock（592 item 3 余量 / 640） interchangeable——640 另钉 not Commit lock / not h+1 round 0，本页钉 not finunlock bundled 单句。592 finunlock unbundling 在本页 item 1 启动。

怎样解锁、怎样再验、怎样开下一高是规范里的做法，本页不抄。FinalizeBlock When unlocks mempool 正式三事 bundled（592）、newly received transactions can now be checked not optional recheck（592 item 2 余量 / 639）、When 第 10 步 unlock after optional recheck not Commit lock（592 item 3 余量 / 640）、locks mempool（588）、optional recheck（591）、Finalize 之后 bundled（403）、Commit 前上锁（310）、CheckTx 技术上可选（373）、starts consensus h+1 round 0（593）是另外那套，本页不抄。

## 官方为什么这样拆

- **unlocks mempool not already settled ≠ 403 finafter / 587 finreturn interchangeable：** 官方把 When 第 10 步解锁和 Finalize + Commit 交差 / persists 这三份 分开。
- **unlocks mempool not four gates settled ≠ 33 four gates / 602 notgates interchangeable：** 官方把 592 item 1 和四门已经结算 / finequiv not four gates 分开。
- **unlocks mempool not finunlock bundled ≠ 639 finunlock-notnewly / 640 finunlock-notcommitlock interchangeable：** 官方把 592 item 1 和 item 2 / item 3 分开；592 finunlock unbundling 启动（638 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| unlocks the mempool | 不是 already settled / 交差 | 不是 finafter bundled（403） |
| unlocks the mempool | 不是 already four gates settled | 不是 four gates（33） |
| unlocks the mempool | 不是 already finunlock bundled | 不是 newly received not optional recheck（592 item 2 / 639） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量），必须分开 unlocks the mempool 是不是 already settled / 交差 interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable、unlocks the mempool 是不是 already four gates settled interchangeable / 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable、unlocks the mempool 是不是 already finunlock bundled interchangeable / 639 finunlock-notnewly interchangeable / 640 finunlock-notcommitlock interchangeable / 591 finrecheck interchangeable。可以跳过「看见 When 第 10 步解锁了 就已经交差 interchangeable」。不要另写怎样解锁。592 finunlock unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样解锁、怎样再验、怎样开下一高。
- FinalizeBlock When unlocks mempool 正式三事 bundled。那是不变量 592。
- newly received transactions can now be checked not optional recheck。那是不变量 592 item 2 余量 / 639。
- When 第 10 步 unlock after optional recheck not Commit lock。那是不变量 592 item 3 余量 / 640。
- locks mempool。那是不变量 588。
- optional recheck。那是不变量 591。
- Finalize 之后 bundled。那是不变量 403。
- Commit 前上锁。那是不变量 310。
- CheckTx 技术上可选。那是不变量 373。
- starts consensus h+1 round 0。那是不变量 593。
