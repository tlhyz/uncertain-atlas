# 模式：把 FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**例**：[FinalizeBlock When locks mempool not already settled ≠ bundled（588）](../../tracks/implementation/worked-example-finlock-notsettled-vs-bundled.md)。

## 三个名字

1. **locks mempool 不是已经交差：** 看见 CometBFT locks the mempool / 引擎锁内存池，不是已经 Finalize + Commit 交差 interchangeable，不是 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable / 33 four gates interchangeable。
2. **locks mempool 不是四门已经结算：** 看见 locks the mempool，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable，不是 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 478 finpersist interchangeable。
3. **locks mempool 不是 finlock bundled：** 看见 locks the mempool，不是已经 finlock bundled interchangeable，不是 630 notoptional interchangeable / 631 notcommitlock interchangeable / 588 finlock item 2 no CheckTx optional interchangeable / 588 finlock item 3 Commit lock interchangeable。

## 为什么要分开叫

官方把 When 第 7 步 locks the mempool、交差 / 四门已经结算、588 finlock bundled 三事 写成三个名字。把它们叫成一个「看见锁了内存池 就已经交差 interchangeable、就已经四门已经结算 interchangeable、就已经 finlock bundled interchangeable」，会把 not already settled、not four gates settled、not finlock bundled / not 588 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool not already settled / not four gates settled / not finlock bundled 正式三事（588 余量），先数清问的是 locks the mempool 是不是 already settled / 403 / 587，是不是 already four gates settled / 33 / 602 notgates，还是 locks the mempool 是不是 already finlock bundled / 630 / 631，再决定要不要同一次发布。
