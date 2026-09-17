# 模式：把 FinalizeBlock equiv ABCI 1.0 not four gates settled 正式三事（586 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock equiv not four gates settled ≠ bundled（586）](../../tracks/implementation/worked-example-finequiv-notgates-vs-bundled.md)。

## 三个名字

1. **equiv not four gates settled 不是 finequiv bundled：** 看见收成一门不是已经四门已经结算 interchangeable，不是 586 finequiv interchangeable / 600 notgates interchangeable / 33 four gates interchangeable / 478 finpersist interchangeable。
2. **equiv not settled 不是 finresp notsettled：** 看见收成一门不是已经 Finalize + Commit 交差 interchangeable，不是 601 notsettled interchangeable / 594 not settled interchangeable / 478 finpersist interchangeable / 363 finresp interchangeable。
3. **equiv not finequiv bundled 不是 586 item 2 / item 3：** 看见等价不是已经 finequiv bundled interchangeable，不是 586 item 2 no Prepare/Process interchangeable / 586 item 3 Contains newly decided interchangeable / 460 fincand interchangeable / 461 finnewfields interchangeable。

## 为什么要分开叫

官方把 equiv 收成一门、four gates settled / 交差、586 finequiv bundled 三事 写成三个名字。把它们叫成一个「看见收成一门 就已经四门已经结算 / 已经交差 / 已经 finequiv bundled interchangeable」，会把 not four gates settled、not settled、not finequiv bundled / not 586 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not four gates settled 正式三事（586 余量），先数清问的是 equiv 是不是 already four gates settled / 33 / 600 notgates、是不是 already settled / 601 notsettled / 478 finpersist，还是 equiv 是不是 already finequiv bundled / 586 item 2 / 586 item 3，再决定要不要同一次发布。
