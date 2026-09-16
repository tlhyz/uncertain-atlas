# 模式：把 FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state 正式三事（587 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 6。  
**例**：[FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not Commit 落盘 ≠ bundled（587）](../../tracks/implementation/worked-example-finreturn-notpersist-vs-bundled.md)。

## 三个名字

1. **CometBFT persists tx outputs / AppHash / ResultsHash 不是已经交差：** 看见 persists 这三份 不是已经 Finalize + Commit 交差 interchangeable，不是 335 finpersist interchangeable / 403 finafter interchangeable / 33 four gates interchangeable / 601 notsettled interchangeable。
2. **CometBFT persists tx outputs / AppHash / ResultsHash 不是 Commit 落盘应用状态：** 看见 persists 这三份 不是已经 Commit 落盘应用状态 interchangeable，不是 481 commitpersist interchangeable / 481 persist signal interchangeable / 335 item 2 必须在 Commit 落盘 interchangeable / 467 finpersist interchangeable。
3. **CometBFT persists tx outputs / AppHash / ResultsHash 不是 finreturn bundled：** 看见 persists 这三份 不是已经 finreturn bundled interchangeable，不是 614 notheader interchangeable / 615 notresulthash interchangeable / 587 finreturn item 1 Application returns interchangeable / 587 finreturn item 2 hashes into ResultHash interchangeable。

## 为什么要分开叫

官方把 When 第 6 步 persists tx outputs / AppHash / ResultsHash、第 4 步 Application returns AppHash + tx outputs、第 5 步 hashes into ResultHash 这三份写成三个名字。把它们叫成一个「看见 persists 这三份 就已经交差 interchangeable、就已经 Commit 落盘 interchangeable、就已经 finreturn bundled interchangeable」，会把 not already settled、not Commit persist application state、not finreturn bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT persists tx outputs / AppHash / ResultsHash not already settled / not Commit persist application state 正式三事（587 余量），先数清问的是 persists 这三份 是不是 already 已经交差 / 335 / 403，是不是 already Commit 落盘应用状态 / 481 / 467，还是 persists 这三份 是不是 already finreturn bundled / 614 / 615，再决定要不要同一次发布。587 finreturn unbundling 在本页 item 3 完成。
