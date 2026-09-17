# 模式：把 FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 6–7。  
**例**：[FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled ≠ bundled（403）](../../tracks/implementation/worked-example-finafter-notsettled-vs-bundled.md)。

## 三个名字

1. **Finalize 之后引擎才落盘 不是已经交差：** 看见 Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash / CometBFT persists 这三份，不是已经 Finalize + Commit 交差 interchangeable，不是 33 four gates interchangeable / 335 finpersist interchangeable / 616 notpersist interchangeable。
2. **Finalize 之后引擎才落盘 不是 Commit 落盘应用状态：** 看见 persists 这三份，不是已经落盘应用状态 interchangeable，不是已经应用在 Commit 里落盘 interchangeable，不是 481 commitpersist interchangeable / 590 fincommit interchangeable / 335 item 2 interchangeable。
3. **Finalize 之后引擎才落盘 不是 finafter bundled：** 看见 persists 这三份，不是已经 finafter bundled interchangeable，不是 633 notlock interchangeable / 634 notrecheck interchangeable / 403 finafter item 2 落完再锁 interchangeable / 403 finafter item 3 optional recheck interchangeable。

## 为什么要分开叫

官方把 When 第 6 步 Finalize 之后引擎才落盘这三份、交差 / Commit 落盘应用状态、403 finafter bundled 三事 写成三个名字。把它们叫成一个「看见 Finalize 之后引擎才落盘 就已经交差 interchangeable、就已经 Commit 落盘 interchangeable、就已经 finafter bundled interchangeable」，会把 not already settled、not Commit persist application state、not finafter bundled / not 403 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Finalize 之后引擎才落盘 tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state / not finafter bundled 正式三事（403 余量），先数清问的是 Finalize 之后引擎才落盘 是不是 already 已经交差 / 335 / 616，是不是 already 落盘应用状态 / 481 / 590，还是 Finalize 之后引擎才落盘 是不是 already finafter bundled / 633 / 634，再决定要不要同一次发布。
