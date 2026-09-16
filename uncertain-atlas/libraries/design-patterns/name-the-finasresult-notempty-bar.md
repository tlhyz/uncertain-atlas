# 模式：把 FinalizeBlock must provide values provided values not empty keep current / not CheckTx 正式三事（477 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[provided values not empty keep current / not CheckTx ≠ bundled（477）](../../tracks/implementation/worked-example-finasresult-notempty-vs-bundled.md)。

## 三个名字

1. **provided values not empty keep current 不是 finasresult bundled：** 看见提供了值不是已经空着就没有 must provide 义务 interchangeable，不是 477 finasresult interchangeable / 458 finempty interchangeable / 471 fincparam interchangeable。
2. **provided values not CheckTx passed 不是 Code==0 fully valid：** 看见 must provide tx_results 不是已经 CheckTx 过了就不需要 Finalize 再回 tx_results interchangeable，不是 339 CheckTx 弱过滤器 interchangeable / 464 fintxcode interchangeable / 347 Process Accept interchangeable。
3. **provided values not finasresult bundled 不是 not settled / not candidate：** 看见提供了值不是已经 finasresult bundled interchangeable，不是 594 not settled interchangeable / 595 notcand interchangeable / 363 finresp interchangeable / 335 Finalize 落盘禁令 interchangeable。

## 为什么要分开叫

官方把 must provide values、provided values from execution、empty keep current 和 CheckTx passed 写成三个名字。把它们叫成一个「看见提供了值 就已经空着就没有义务 / 已经 CheckTx 过了就不用再回 tx_results / 已经 477 finasresult bundled interchangeable」，会把 not empty keep current、not CheckTx passed、not finasresult bundled / not settled / not candidate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values provided values not empty keep current / not CheckTx 正式三事（477 余量），先数清问的是 provided values 是不是 already empty means no must provide / 458 finempty、是不是 already CheckTx passed / 339 / 464、还是 provided values 是不是 already finasresult bundled / 594 / 595 / 363，再决定要不要同一次发布。
