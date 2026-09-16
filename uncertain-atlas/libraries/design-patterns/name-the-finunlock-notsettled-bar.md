# 模式：把 FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 10。  
**例**：[FinalizeBlock When unlocks the mempool not already settled ≠ bundled（592）](../../tracks/implementation/worked-example-finunlock-notsettled-vs-bundled.md)。

## 三个名字

1. **unlocks mempool 不是已经交差：** 看见 unlocks the mempool / When 第 10 步解锁内存池，不是已经 Finalize + Commit 交差 interchangeable，不是 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable / 33 four gates interchangeable。
2. **unlocks mempool 不是四门已经结算：** 看见 unlocks the mempool，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable，不是 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 478 finpersist interchangeable。
3. **unlocks mempool 不是 finunlock bundled：** 看见 unlocks the mempool，不是已经 finunlock bundled interchangeable，不是 639 finunlock-notnewly interchangeable / 640 finunlock-notcommitlock interchangeable / 592 finunlock item 2 newly received can now be checked interchangeable / 592 finunlock item 3 unlock after optional recheck interchangeable。

## 为什么要分开叫

官方把 When 第 10 步 unlocks the mempool、交差 / 四门已经结算、592 finunlock bundled 三事 写成三个名字。把它们叫成一个「看见 When 第 10 步解锁了 就已经交差 interchangeable、就已经四门已经结算 interchangeable、就已经 finunlock bundled interchangeable」，会把 not already settled、not four gates settled、not finunlock bundled / not 592 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When unlocks the mempool not already settled / not four gates settled / not finunlock bundled 正式三事（592 余量），先数清问的是 unlocks the mempool 是不是 already settled / 403 / 587，是不是 already four gates settled / 33 / 602 notgates，还是 unlocks the mempool 是不是 already finunlock bundled / 639 / 640，再决定要不要同一次发布。592 finunlock unbundling 在本页 item 1 启动。
