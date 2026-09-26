# 反模式：把 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量）说成已经是 app_version / 已经印进本头 AppHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了 version not already appversion ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notappversion-vs-bundled.md)。

## 卖法

把填了 version / Info 请求 version 是 CometBFT 软件语义版本 / 填了 version 字段 写成已经是 app_version interchangeable / 已经 appversion interchangeable / 已经是 app_version 交差 interchangeable / 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable；把有软件版本 / 有 CometBFT 软件语义版本 / 有版本字符串 写成已经印进本头 AppHash interchangeable / 已经 matched interchangeable / 已经印进每块头交差 interchangeable；把能回 / 能回 Info / 有回包 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 379 infover bundled / infover-sold-as-appversion interchangeable / 884 infover-notappversion interchangeable。

## 为什么错

官方把填了 version、不是已经印进本头 AppHash、不是已经交差写成三件独立的实现事。把它们卖成 already appversion interchangeable / already matched interchangeable / already settled interchangeable，会把 not already appversion、not already matched、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量），必须分开 not already appversion、not already matched、not already settled 三件事，不要和 379 / 370 / 147 / 323 糊成一句。

## 和相邻反模式

- [infover-sold-as-appversion](infover-sold-as-appversion.md) 是 infover bundled 全段，不是本页填了 version item 1 单句边界。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 用来握手对齐就已经是快照重放（370），不是本页 not already appversion 边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Info 的 AppHash 对上就已经是版本也对上（323），不是本页 not already matched 单句。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是没定义 lane_priorities 就已经排了优先（367），不是本页 not already settled 边界。
