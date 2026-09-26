# 模式：把 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[写了 ABCI 版本 not already handshake ≠ bundled（379）](../../tracks/implementation/worked-example-infover-nothandshake-vs-bundled.md)。

## 三个名字

1. **写了 ABCI 版本 不是 already handshake：** 看见写了 ABCI 版本 / abci_version 是 ABCI 语义版本、按 X.X.x 显示 / 写了 abci_version，不是已经是握手对齐 interchangeable / 已经 handshake interchangeable / 已经是握手对齐交差 interchangeable，不是 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable。

2. **显示成 X.X.x 不是 already priority：** 看见显示成 X.X.x / 语义版本显示成 X.X.x / 有 X.X.x 显示，不是已经排了优先 interchangeable / 已经 priority interchangeable / 已经排了优先交差 interchangeable，不是 367 lane-priority interchangeable / 370 info-handshake interchangeable。

3. **有脚注 不是 already settled：** 看见有脚注 / 脚注写了 semver / 有语义版本脚注，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 885 infover-notmatched interchangeable / 379 infover item 2 interchangeable。

官方把写了 ABCI 版本、不是已经排了优先、不是已经交差写成三个名字。把它们叫成一个「看见写了 ABCI 版本就已经是握手对齐 interchangeable / 就已经排了优先 interchangeable / 就已经交差 interchangeable」，会把 not already handshake、not already priority、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量），先数清问的是写了 ABCI 版本 是不是 already handshake / 379 / infover-sold-as-appversion，是不是显示成 X.X.x 是不是 already priority，还是有脚注 是不是 already settled，再决定要不要同一次发布。379 infover-vs-appversion bundled unbundling 在本页 item 3 完成。
