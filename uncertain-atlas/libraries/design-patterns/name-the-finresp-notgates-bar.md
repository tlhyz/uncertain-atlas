# 模式：把 Finalize 回包义务 not four gates settled 正式三事（363 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize equiv not four gates settled ≠ bundled（363）](../../tracks/implementation/worked-example-finresp-notgates-vs-bundled.md)。

## 三个名字

1. **equiv not four gates settled 不是 finresp bundled：** 看见收成一门不是已经四门已经结算 interchangeable，不是 363 finresp interchangeable / 33 four gates interchangeable / 478 finpersist interchangeable。
2. **equiv not finresp bundled 不是 463 / 594：** 看见等价不是已经 must provide 四列 interchangeable，不是 463 finreward interchangeable / 594 not settled interchangeable / 567 not slashed interchangeable。
3. **equiv not no Prepare/Process 不是 586 / 460：** 看见收成一门不是已经没有 Prepare/Process interchangeable，不是 586 finequiv interchangeable / 373 CheckTx optional interchangeable / 460 fincand interchangeable。

## 为什么要分开叫

官方把 equiv 收成一门、finresp bundled 三事 和 ABCI++ 仍保留 Prepare/Process 写成三个名字。把它们叫成一个「看见收成一门 就已经四门已经结算 / 已经 finresp bundled interchangeable」，会把 not four gates settled、not finresp bundled、not no Prepare/Process 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包义务 not four gates settled 正式三事（363 余量），先数清问的是 equiv 是不是 already four gates settled / 33 / 478、是不是 already finresp bundled / 463 / 594、还是 already no Prepare/Process / 586 / 460，再决定要不要同一次发布。
