# 模式：把先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[落决定再同步调 not already settled ≠ bundled（362）](../../tracks/implementation/worked-example-finwhen-notpersist-vs-bundled.md)。

## 三个名字

1. **决定了 不是 already settled：** 看见决定了 / 先把 *v* 落成这一高的决定再同步调 Finalize / 决定了，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable。

2. **先落了决定 不是 already app-persist：** 看见先落了决定 / 先把 *v* 落成高度 *h* 的决定 / 决定落了，不是已经落盘应用状态 interchangeable / 已经 app-persist interchangeable / 已经落盘应用状态交差 interchangeable，不是 335 finpersist interchangeable / 836 finwhen-notwillcall interchangeable。

3. **是同步的 不是 already sync-settled：** 看见是同步的 / 再同步调 Finalize / CometBFT 同步调用，不是已经交差 interchangeable / 已经 sync-settled interchangeable / 已经同步交差交差 interchangeable，不是 838 finwhen-notprinted interchangeable / 33 fourgates interchangeable。

官方把决定了、不是已经落盘应用状态、不是已经交差写成三个名字。把它们叫成一个「看见决定了就已经交差 interchangeable / 就已经落盘应用状态 interchangeable / 就已经交差 interchangeable」，会把 not already settled、not already app-persist、not already sync-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量），先数清问的是决定了 是不是 already settled / 362 / finalizewhen-sold-as-decided，是不是先落了决定 是不是 already app-persist，还是是同步的 是不是 already sync-settled，再决定要不要同一次发布。362 finalize-when vs decided bundled unbundling 在本页 item 2 续。
