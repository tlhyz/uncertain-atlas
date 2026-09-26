# 模式：把 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[填了两列 not already matched ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notmatched-vs-bundled.md)。

## 三个名字

1. **填了两列 不是 already matched：** 看见填了两列 / block_version / p2p_version 是引擎块版本和 P2P 版本 / 填了 block_version 与 p2p_version，不是已经版本也对上 interchangeable / 已经 matched interchangeable / 已经版本也对上交差 interchangeable，不是 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable。

2. **有块版本 不是 already history：** 看见有块版本 / 有 CometBFT 块版本 / 有 block_version，不是已经有完整历史 interchangeable / 已经 history interchangeable / 已经有从创世的完整历史交差 interchangeable，不是 323 transition interchangeable / 370 info-handshake interchangeable。

3. **有 P2P 版本 不是 already settled：** 看见有 P2P 版本 / 有 CometBFT P2P 版本 / 有 p2p_version，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 884 infover-notappversion interchangeable / 379 infover item 3 interchangeable。

官方把填了两列、不是已经有完整历史、不是已经交差写成三个名字。把它们叫成一个「看见填了两列就已经版本也对上 interchangeable / 就已经有完整历史 interchangeable / 就已经交差 interchangeable」，会把 not already matched、not already history、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量），先数清问的是填了两列 是不是 already matched / 379 / infover-sold-as-appversion，是不是有块版本 是不是 already history，还是有 P2P 版本 是不是 already settled，再决定要不要同一次发布。379 infover-vs-appversion bundled unbundling 在本页 item 2 续。
