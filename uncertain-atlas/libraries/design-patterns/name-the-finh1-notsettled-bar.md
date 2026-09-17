# 模式：把 FinalizeBlock When starts consensus for height h+1 not already settled / not persist decision / not finh1 bundled 正式三事（593 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 11。  
**例**：[FinalizeBlock When starts consensus for height h+1 not already settled ≠ bundled（593）](../../tracks/implementation/worked-example-finh1-notsettled-vs-bundled.md)。

## 三个名字

1. **starts consensus for height h+1 不是已经交差：** 看见 starts consensus for height h+1 / When 第 11 步开下一高，不是已经 Finalize + Commit 交差 interchangeable，不是 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable / 33 four gates interchangeable / 632 notsettled interchangeable。
2. **starts consensus for height h+1 不是 persist decision：** 看见 starts consensus for height _h+1_，不是已经 _p_ persists _v_ as the decision for height _h_ interchangeable，不是 478 finpersist interchangeable / 605 notpersist interchangeable / 594 not settled interchangeable / 479 fintrigger interchangeable / 610 notdecides interchangeable。
3. **starts consensus for height h+1 不是 finh1 bundled：** 看见 When 第 11 步开下一高，不是已经 finh1 bundled interchangeable，不是 642 finh1-notround interchangeable / 643 finh1-notafterunlock interchangeable / 593 finh1 item 2 round 0 interchangeable / 593 finh1 item 3 after unlock interchangeable / 592 finunlock interchangeable / 640 finunlock-notcommitlock interchangeable。

## 为什么要分开叫

官方把 When 第 11 步 starts consensus for height h+1、交差 / persist decision、593 finh1 bundled 三事 写成三个名字。把它们叫成一个「看见 When 第 11 步开下一高了 就已经交差 interchangeable、就已经 persist decision interchangeable、就已经 finh1 bundled interchangeable」，会把 not already settled、not persist decision、not finh1 bundled / not 593 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When starts consensus for height h+1 not already settled / not persist decision / not finh1 bundled 正式三事（593 余量），先数清问的是 starts consensus for height h+1 是不是 already settled / 403 / 587 / 632，是不是 already persist decision / 478 / 605 / 479 / 610，还是 starts consensus for height h+1 是不是 already finh1 bundled / 642 / 643 / 592 / 640，再决定要不要同一次发布。593 finh1 unbundling 在本页 item 1 启动。
