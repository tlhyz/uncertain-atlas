# 模式：把 FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**例**：[FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional ≠ bundled（588）](../../tracks/implementation/worked-example-finlock-notoptional-vs-bundled.md)。

## 三个名字

1. **no calls on new transactions 不是 CheckTx 可选：** 看见 no calls to `CheckTx` on new transactions / 新交易不再进 CheckTx，不是已经 CheckTx 技术上可选 interchangeable，不是 373 checktxopt interchangeable / 312 checktxopt interchangeable / 313 checktxguard interchangeable。
2. **no calls on new transactions 不是已经进池：** 看见 no calls on new transactions，不是已经进了池 interchangeable，不是已经开始了流言 interchangeable，不是 33 four gates interchangeable / 301 mempool interchangeable / 339 checktxweak interchangeable。
3. **no calls on new transactions 不是 finlock bundled：** 看见 no calls on new transactions，不是已经 finlock bundled interchangeable，不是 629 notsettled interchangeable / 631 notcommitlock interchangeable / 588 finlock item 1 locks the mempool interchangeable / 588 finlock item 3 Commit lock interchangeable。

## 为什么要分开叫

官方把 When 第 7 步 no calls to CheckTx on new transactions、CheckTx optional / 已经进池、588 finlock bundled 三事 写成三个名字。把它们叫成一个「看见新交易不再进 CheckTx 就已经 CheckTx 可选 interchangeable、就已经进池 interchangeable、就已经 finlock bundled interchangeable」，会把 not CheckTx optional、not already in pool、not finlock bundled / not 588 item 1 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量），先数清问的是 no calls on new transactions 是不是 already CheckTx optional / 373 / 313，是不是 already 进池 / 33 / 301，还是 no calls on new transactions 是不是 already finlock bundled / 629 / 631，再决定要不要同一次发布。
