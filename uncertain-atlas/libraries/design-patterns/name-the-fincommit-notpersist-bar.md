# 模式：把 FinalizeBlock When instruct Application to persist its state not engine persist tx outputs / AppHash / ResultsHash / not Commit Usage signal bundled / not fincommit bundled 正式三事（590 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 8。  
**例**：[FinalizeBlock When instruct Application to persist its state not engine persist ≠ bundled（590）](../../tracks/implementation/worked-example-fincommit-notpersist-vs-bundled.md)。

## 三个名字

1. **instruct persist 不是已经引擎 persist 这三份：** 看见 to instruct the Application to persist its state / instruct Application to persist its state，不是已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable，不是 587 finreturn interchangeable / 616 notpersist interchangeable / 632 notsettled interchangeable / 403 finafter item 1 interchangeable。
2. **instruct persist 不是 Commit Usage signal bundled：** 看见 instruct Application to persist its state，不是已经 Signal the Application to persist application state interchangeable，不是 481 commitpersist interchangeable / 481 item 1 persist signal interchangeable / 335 finpersist interchangeable / 399 commitnoparam interchangeable。
3. **instruct persist 不是 fincommit bundled：** 看见 instruct Application to persist its state，不是已经 fincommit bundled interchangeable，不是 644 fincommit-notsettled interchangeable / 646 fincommit-notcommitlock interchangeable / 590 fincommit item 1 calls Commit interchangeable / 590 fincommit item 3 after lock mempool interchangeable。

## 为什么要分开叫

官方把 When 第 8 步 instruct Application to persist its state、引擎 persist 这三份 / Commit Usage signal、590 fincommit bundled 三事 写成三个名字。把它们叫成一个「看见 instruct Application to persist its state 就已经引擎 persist 这三份 interchangeable、就已经 Commit Usage signal bundled interchangeable、就已经 fincommit bundled interchangeable」，会把 not engine persist 这三份、not Commit Usage signal bundled、not fincommit bundled / not 590 item 1 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When instruct Application to persist its state not engine persist tx outputs / AppHash / ResultsHash / not Commit Usage signal bundled / not fincommit bundled 正式三事（590 余量），先数清问的是 instruct persist 是不是 already engine persist 这三份 / 587 / 616 / 632，是不是 already Commit Usage signal bundled / 481 / 335 / 399，还是 instruct persist 是不是 already fincommit bundled / 644 / 646 / 590 item 1 / item 3，再决定要不要同一次发布。590 fincommit unbundling 在本页 item 2 续。
