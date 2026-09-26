# 反模式：把 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量）说成已经版本也对上 / 已经有完整历史 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了两列 not already matched ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notmatched-vs-bundled.md)。

## 卖法

把填了两列 / block_version / p2p_version 是引擎块版本和 P2P 版本 / 填了 block_version 与 p2p_version 写成已经版本也对上 interchangeable / 已经 matched interchangeable / 已经版本也对上交差 interchangeable / 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable；把有块版本 / 有 CometBFT 块版本 / 有 block_version 写成已经有完整历史 interchangeable / 已经 history interchangeable / 已经有从创世的完整历史交差 interchangeable；把有 P2P 版本 / 有 CometBFT P2P 版本 / 有 p2p_version 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 379 infover bundled / infover-sold-as-appversion interchangeable / 885 infover-notmatched interchangeable。

## 为什么错

官方把填了两列、不是已经有完整历史、不是已经交差写成三件独立的实现事。把它们卖成 already matched interchangeable / already history interchangeable / already settled interchangeable，会把 not already matched、not already history、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量），必须分开 not already matched、not already history、not already settled 三件事，不要和 379 / 323 / 884 / 370 糊成一句。

## 和相邻反模式

- [infover-sold-as-appversion](infover-sold-as-appversion.md) 是 infover bundled 全段，不是本页填了两列 item 2 单句边界。
- [infover-notappversion-sold-as-bundled](infover-notappversion-sold-as-bundled.md) 是填了 version not already appversion（379 item 1），不是本页 not already matched 边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Info 的 AppHash 对上就已经是版本也对上（323），不是本页 not already matched 单句。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 用来握手对齐就已经是快照重放（370），不是本页 not already history 边界。
