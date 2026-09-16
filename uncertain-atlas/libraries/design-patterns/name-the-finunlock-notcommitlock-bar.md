# 模式：把 FinalizeBlock When unlock after optional recheck not Commit lock / not h+1 round 0 / not finunlock bundled 正式三事（592 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 10。  
**例**：[FinalizeBlock When unlock after optional recheck not Commit lock ≠ bundled（592）](../../tracks/implementation/worked-example-finunlock-notcommitlock-vs-bundled.md)。

## 三个名字

1. **unlock after optional recheck 不是 Commit 锁：** 看见 When 第 10 步 unlock after optional recheck / unlock 之后才开下一高，不是已经是 Commit 锁 interchangeable，不是 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable / 631 notcommitlock interchangeable。
2. **unlock after optional recheck 不是 h+1 round 0：** 看见 unlocks the mempool after optional recheck，不是已经 starts consensus for h+1 round 0 interchangeable，不是 593 finh1 interchangeable / 403 finafter item 3 optional recheck unlock h+1 interchangeable / 634 notrecheck interchangeable / 361 finalizewhen interchangeable。
3. **unlock after optional recheck 不是 finunlock bundled：** 看见 When 第 10 步 unlock，不是已经 finunlock bundled interchangeable，不是 638 finunlock-notsettled interchangeable / 639 finunlock-notnewly interchangeable / 592 finunlock item 1 unlocks the mempool interchangeable / 592 finunlock item 2 newly received can now be checked interchangeable。

## 为什么要分开叫

官方把 When 第 10 步 unlock after optional recheck、Commit 锁 / starts consensus h+1 round 0、592 finunlock bundled 三事 写成三个名字。把它们叫成一个「看见 When 第 10 步 unlock after optional recheck 就已经 Commit 锁 interchangeable、就已经开下一高 round 0 interchangeable、就已经 finunlock bundled interchangeable」，会把 not Commit lock、not h+1 round 0、not finunlock bundled / not 592 item 1 / item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When unlock after optional recheck not Commit lock / not h+1 round 0 / not finunlock bundled 正式三事（592 余量），先数清问的是 When 第 10 步 unlock 是不是 already Commit lock / 310 / 631 / 590，是不是 already h+1 round 0 / 593 / 403 / 634，还是 When 第 10 步 unlock 是不是 already finunlock bundled / 638 / 639，再决定要不要同一次发布。592 finunlock unbundling 在本页 item 3 完成。
