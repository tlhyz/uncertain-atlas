# 模式：把 FinalizeBlock When after unlock not unlock mempool / not finafter bundled / not When trigger 正式三事（593 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 11。  
**例**：[FinalizeBlock When after unlock not unlock mempool ≠ bundled（593）](../../tracks/implementation/worked-example-finh1-notafterunlock-vs-bundled.md)。

## 三个名字

1. **after unlock 不是 unlocks the mempool：** 看见 When 第 11 步 after unlock / unlock 之后才开下一高，不是已经 unlocks the mempool interchangeable，不是 592 finunlock interchangeable / 640 finunlock-notcommitlock interchangeable / 638 finunlock-notsettled interchangeable / 639 finunlock-notnewly interchangeable / 634 notrecheck interchangeable。
2. **after unlock 不是 Finalize 之后 bundled：** 看见 When 第 11 步 after unlock，不是已经 Finalize 之后 bundled interchangeable，不是 403 finafter interchangeable / 632 notsettled interchangeable / 633 notlock interchangeable / 634 notrecheck interchangeable / 588 finlock interchangeable / 631 notcommitlock interchangeable。
3. **after unlock 不是 When trigger / finh1 bundled：** 看见 When 第 11 步 after unlock，不是已经 When trigger 2f+1 precommit decides _v_ interchangeable，不是 479 fintrigger interchangeable / 610 notdecides interchangeable / 362 +2/3 precommit interchangeable / 641 finh1-notsettled interchangeable / 642 finh1-notround interchangeable。

## 为什么要分开叫

官方把 When 第 11 步 after unlock、When 第 10 步 unlocks the mempool、Finalize 之后 bundled、When 前导 trigger、593 finh1 bundled 三事 写成三个名字。把它们叫成一个「看见 unlock 之后才开下一高了 就已经 unlocks the mempool interchangeable、就已经 finafter bundled interchangeable、就已经 When trigger interchangeable」，会把 not unlock mempool、not finafter bundled、not When trigger / not 641 / not 642 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When after unlock not unlock mempool / not finafter bundled / not When trigger 正式三事（593 余量），先数清问的是 When 第 11 步 after unlock 是不是 already unlocks the mempool / 592 / 640 / 634，是不是 already finafter bundled / 403 / 632 / 633，还是 When 第 11 步 after unlock 是不是 already When trigger / 479 / 641 / 642，再决定要不要同一次发布。593 finh1 unbundling 在本页 item 3 完成。
