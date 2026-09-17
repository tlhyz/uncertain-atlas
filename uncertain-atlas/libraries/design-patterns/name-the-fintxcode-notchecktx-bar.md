# 模式：把 FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed ≠ bundled（585）](../../tracks/implementation/worked-example-fintxcode-notchecktx-vs-bundled.md)。

## 三个名字

1. **only if fully valid 不是已经 CheckTx 过了：** 看见 only if fully valid，不是已经 CheckTx 弱过滤器 interchangeable，不是 339 checktxweak interchangeable / 313 checktxguard interchangeable / 312 checktxopt interchangeable。
2. **only if fully valid 不是已经 Process Accept：** 看见 only if fully valid，不是已经 Process 回了 Accept interchangeable，不是 347 req3coherence interchangeable / 530 procaccept interchangeable / 354 processwhen interchangeable。
3. **only if fully valid 不是 fintxcode bundled：** 看见 only if fully valid，不是已经 fintxcode bundled interchangeable，不是 627 notinvalid interchangeable / 628 notsettled interchangeable / 585 fintxcode item 2 Code 非零仍可能在块里 interchangeable / 585 fintxcode item 3 回了 tx_results interchangeable。

## 为什么要分开叫

官方把 `tx_results[i].Code == 0` only if fully valid、Code 非零仍可能在块里、Finalize 回包和交差 / 印进本头写成三个名字。把它们叫成一个「看见 only if fully valid 就已经 CheckTx 过了 interchangeable、就已经 Process Accept interchangeable、就已经 fintxcode bundled interchangeable」，会把 not CheckTx passed、not Process Accept、not fintxcode bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量），先数清问的是 only if fully valid 是不是 already CheckTx 过了 / 339 / 313，是不是 already Process Accept / 347 / 530，还是 only if fully valid 是不是 already fintxcode bundled / 627 / 628，再决定要不要同一次发布。
