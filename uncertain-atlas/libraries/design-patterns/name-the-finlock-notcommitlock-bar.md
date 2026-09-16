# 模式：把 FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**例**：[FinalizeBlock When locks mempool after persist not Commit lock ≠ bundled（588）](../../tracks/implementation/worked-example-finlock-notcommitlock-vs-bundled.md)。

## 三个名字

1. **locks mempool after persist 不是 Commit 锁：** 看见 locks mempool after persist / persist 之后才锁，不是已经是 Commit 锁 interchangeable，不是 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable。
2. **locks mempool after persist 不是 unlock / Recheck：** 看见 locks mempool after persist，不是已经解锁 interchangeable，不是已经是 Recheck interchangeable，不是 592 finunlock interchangeable / 591 finrecheck interchangeable / 312 checktxtype RECHECK interchangeable / 403 finafter item 3 optional recheck interchangeable。
3. **locks mempool after persist 不是 finlock bundled：** 看见 locks mempool after persist，不是已经 finlock bundled interchangeable，不是 629 notsettled interchangeable / 630 notoptional interchangeable / 588 finlock item 1 locks the mempool interchangeable / 588 finlock item 2 no CheckTx optional interchangeable。

## 为什么要分开叫

官方把 When 第 7 步 persist 之后才锁、Commit 锁 / unlock / Recheck、588 finlock bundled 三事 写成三个名字。把它们叫成一个「看见 persist 之后才锁 就已经 Commit 锁 interchangeable、就已经解锁 interchangeable、就已经 Recheck interchangeable、就已经 finlock bundled interchangeable」，会把 not Commit lock、not unlock / not Recheck、not finlock bundled / not 588 item 1 / item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool after persist not Commit lock / not unlock / not Recheck / not finlock bundled 正式三事（588 余量），先数清问的是 locks mempool after persist 是不是 already Commit lock / 310 / 590，是不是 already unlock / Recheck / 592 / 591 / 312，还是 locks mempool after persist 是不是 already finlock bundled / 629 / 630，再决定要不要同一次发布。588 finlock unbundling 在本页 item 3 完成。
