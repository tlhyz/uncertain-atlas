# 模式：把 FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 8。  
**例**：[FinalizeBlock When CometBFT calls Commit not already settled ≠ bundled（590）](../../tracks/implementation/worked-example-fincommit-notsettled-vs-bundled.md)。

## 三个名字

1. **calls Commit 不是已经交差：** 看见 CometBFT calls Commit / When 第 8 步叫 Commit，不是已经 Finalize + Commit 交差 interchangeable，不是 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable / 33 four gates interchangeable / 632 notsettled interchangeable。
2. **calls Commit 不是四门已经结算：** 看见 When 第 8 步 calls Commit，不是已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable，不是 33 four gates interchangeable / 602 notgates interchangeable / 600 notgates interchangeable / 478 finpersist interchangeable。
3. **calls Commit 不是 fincommit bundled：** 看见 When 第 8 步叫 Commit，不是已经 fincommit bundled interchangeable，不是 645 fincommit-notpersist interchangeable / 646 fincommit-notcommitlock interchangeable / 590 fincommit item 2 instruct persist interchangeable / 590 fincommit item 3 after lock mempool interchangeable / 481 commitpersist interchangeable。

## 为什么要分开叫

官方把 When 第 8 步 CometBFT calls Commit、交差 / 四门已经结算、590 fincommit bundled 三事 写成三个名字。把它们叫成一个「看见 When 第 8 步叫了 Commit 就已经交差 interchangeable、就已经四门已经结算 interchangeable、就已经 fincommit bundled interchangeable」，会把 not already settled、not four gates settled、not fincommit bundled / not 590 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT calls Commit not already settled / not four gates settled / not fincommit bundled 正式三事（590 余量），先数清问的是 calls Commit 是不是 already settled / 403 / 587 / 632，是不是 already four gates settled / 33 / 602 / 600，还是 calls Commit 是不是 already fincommit bundled / 645 / 646 / 481，再决定要不要同一次发布。590 fincommit unbundling 在本页 item 1 启动。
