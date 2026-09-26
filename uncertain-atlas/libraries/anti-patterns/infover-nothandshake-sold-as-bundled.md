# 反模式：把 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量）说成已经是握手对齐 / 已经排了优先 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写了 ABCI 版本 not already handshake ≠ bundled（379）](../../tracks/implementation/worked-example-infover-nothandshake-vs-bundled.md)。

## 卖法

把写了 ABCI 版本 / abci_version 是 ABCI 语义版本、按 X.X.x 显示 / 写了 abci_version 写成已经是握手对齐 interchangeable / 已经 handshake interchangeable / 已经是握手对齐交差 interchangeable / 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable；把显示成 X.X.x / 语义版本显示成 X.X.x / 有 X.X.x 显示 写成已经排了优先 interchangeable / 已经 priority interchangeable / 已经排了优先交差 interchangeable；把有脚注 / 脚注写了 semver / 有语义版本脚注 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 379 infover bundled / infover-sold-as-appversion interchangeable / 886 infover-nothandshake interchangeable。

## 为什么错

官方把写了 ABCI 版本、不是已经排了优先、不是已经交差写成三件独立的实现事。把它们卖成 already handshake interchangeable / already priority interchangeable / already settled interchangeable，会把 not already handshake、not already priority、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量），必须分开 not already handshake、not already priority、not already settled 三件事，不要和 379 / 370 / 367 / 885 糊成一句。

## 和相邻反模式

- [infover-sold-as-appversion](infover-sold-as-appversion.md) 是 infover bundled 全段，不是本页写了 ABCI 版本 item 3 单句边界。
- [infover-notappversion-sold-as-bundled](infover-notappversion-sold-as-bundled.md) 是填了 version not already appversion（379 item 1），不是本页 not already handshake 边界。
- [infover-notmatched-sold-as-bundled](infover-notmatched-sold-as-bundled.md) 是填了两列 not already matched（379 item 2），不是本页 not already handshake 单句。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 用来握手对齐就已经是快照重放（370），不是本页 not already handshake 边界。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是没定义 lane_priorities 就已经排了优先（367），不是本页 not already priority 边界。
