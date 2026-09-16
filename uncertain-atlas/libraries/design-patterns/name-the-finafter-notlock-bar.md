# 模式：把 FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**例**：[FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock ≠ bundled（403）](../../tracks/implementation/worked-example-finafter-notlock-vs-bundled.md)。

## 三个名字

1. **落完再锁内存池 不是 Commit 锁：** 看见落完再锁内存池、新交易不进 CheckTx / locks the mempool / no calls to CheckTx on new transactions，不是已经是 Commit 锁 interchangeable，不是 310 commitlock interchangeable / 307 commitlock interchangeable / 590 fincommit interchangeable / 631 notcommitlock interchangeable。
2. **落完再锁内存池 不是已经交差：** 看见锁了，不是已经交差 interchangeable，不是已经 Finalize + Commit 交差 interchangeable，不是 632 notsettled interchangeable / 335 finpersist interchangeable / 629 notsettled interchangeable / 33 four gates interchangeable。
3. **落完再锁内存池 不是 finafter bundled：** 看见 When 第 7 步 落完再锁，不是已经 finafter bundled interchangeable，不是 634 notrecheck interchangeable / 632 notsettled interchangeable / 403 finafter item 1 落盘 interchangeable / 403 finafter item 3 optional recheck interchangeable / 588 finlock interchangeable。

## 为什么要分开叫

官方把 When 第 7 步落完再锁内存池、Commit 锁 / 已经交差、403 finafter bundled 三事 写成三个名字。把它们叫成一个「看见锁了 就已经 Commit 锁 interchangeable、就已经交差 interchangeable、就已经 finafter bundled interchangeable」，会把 not Commit lock、not already settled、not finafter bundled / not 403 item 1 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 落完再锁内存池、新交易不进 CheckTx not Commit lock / not already settled / not finafter bundled 正式三事（403 余量），先数清问的是落完再锁内存池 是不是 already Commit lock / 310 / 631，是不是 already 已经交差 / 632 / 629 / 335，还是落完再锁内存池 是不是 already finafter bundled / 634 / 632 item 1，再决定要不要同一次发布。403 finafter unbundling 在本页 item 2 续。
