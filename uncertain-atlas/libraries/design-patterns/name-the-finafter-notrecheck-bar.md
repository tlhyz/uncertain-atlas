# 模式：把 FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 9–11。  
**例**：[FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck ≠ bundled（403）](../../tracks/implementation/worked-example-finafter-notrecheck-vs-bundled.md)。

## 三个名字

1. **optional recheck unlock h+1 不是 Recheck：** 看见可选再验池里剩下的 / optionally re-checks outstanding transactions / against newly persisted Application state，不是已经是 Recheck interchangeable，不是 591 finrecheck interchangeable / 312 checktxtype RECHECK interchangeable / 484 chktxtype interchangeable。
2. **optional recheck unlock h+1 不是 unlock：** 看见 unlocks the mempool / newly received transactions can now be checked，不是已经解锁 interchangeable，不是 592 finunlock interchangeable / 631 notcommitlock item 2 not unlock interchangeable / 310 commitlock interchangeable。
3. **optional recheck unlock h+1 不是 finafter bundled：** 看见 starts consensus for height h+1 round 0 / When 第 9–11 步 recheck+unlock+h+1，不是已经 finafter bundled interchangeable，不是 632 notsettled interchangeable / 633 notlock interchangeable / 403 finafter item 1 落盘 interchangeable / 403 finafter item 2 落完再锁 interchangeable / 593 finh1 interchangeable。

## 为什么要分开叫

官方把 When 第 9–11 步 optional recheck、unlock、h+1 round 0、Recheck type / unlock mempool、403 finafter bundled 三事 写成三个名字。把它们叫成一个「看见再验了 就已经 Recheck interchangeable、就已经解锁 interchangeable、就已经 finafter bundled interchangeable」，会把 not Recheck、not unlock、not finafter bundled / not 403 item 1 / item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 可选再验池里剩下的、再解锁、再开下一高 round 0 not Recheck / not unlock / not finafter bundled 正式三事（403 余量），先数清问的是 optional recheck unlock h+1 是不是 already Recheck / 591 / 312 / 484，是不是 already unlock / 592 / 631，还是 optional recheck unlock h+1 是不是 already finafter bundled / 632 / 633 / 593，再决定要不要同一次发布。403 finafter unbundling 在本页 item 3 完成。
