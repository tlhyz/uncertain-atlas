# 模式：把 FinalizeBlock When calls Commit after lock mempool not Commit lock / not optional recheck / unlock / not fincommit bundled 正式三事（590 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 8。  
**例**：[FinalizeBlock When calls Commit after lock mempool not Commit lock ≠ bundled（590）](../../tracks/implementation/worked-example-fincommit-notcommitlock-vs-bundled.md)。

## 三个名字

1. **calls Commit after lock 不是已经 Commit 锁：** 看见 When 第 8 步 calls Commit after lock mempool / lock 之后才 Commit，不是已经 Commit 前上锁 interchangeable，不是 310 commitlock interchangeable / 307 commitlock interchangeable / 631 notcommitlock interchangeable / 588 finlock interchangeable。
2. **calls Commit after lock 不是 optional recheck / unlock：** 看见 calls Commit after lock，不是已经 optional recheck interchangeable，不是 591 finrecheck interchangeable / 592 finunlock interchangeable / 403 finafter item 3 interchangeable / 634 notrecheck interchangeable / 312 checktxtype RECHECK interchangeable。
3. **calls Commit after lock 不是 fincommit bundled：** 看见 When 第 8 步 lock 之后才 Commit，不是已经 fincommit bundled interchangeable，不是 644 fincommit-notsettled interchangeable / 645 fincommit-notpersist interchangeable / 590 fincommit item 1 calls Commit interchangeable / 590 fincommit item 2 instruct persist interchangeable。

## 为什么要分开叫

官方把 When 第 8 步 calls Commit after lock mempool、Commit 锁 / optional recheck / unlock、590 fincommit bundled 三事 写成三个名字。把它们叫成一个「看见 When 第 8 步 lock 之后才 Commit 就已经 Commit 锁 interchangeable、就已经 optional recheck / unlock interchangeable、就已经 fincommit bundled interchangeable」，会把 not Commit lock、not optional recheck / unlock、not fincommit bundled / not 590 item 1 / item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calls Commit after lock mempool not Commit lock / not optional recheck / unlock / not fincommit bundled 正式三事（590 余量），先数清问的是 calls Commit after lock 是不是 already Commit lock / 310 / 631 / 588，是不是 already optional recheck / unlock / 591 / 592 / 403 / 634，还是 calls Commit after lock 是不是 already fincommit bundled / 644 / 645 / 481，再决定要不要同一次发布。590 fincommit unbundling 在本页 item 3 完成。
