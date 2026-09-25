# 反模式：把 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量）说成已经印进本头 AppHash / 已经是本高度交差 / 已经选型

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有版本 not already apphash ≠ bundled（370）](../../tracks/implementation/worked-example-info-notapphash-vs-bundled.md)。

## 卖法

把有版本 / 回的 `app_version` 会写进每一块的头 / 有 app_version 写成已经印进本头 AppHash interchangeable / 已经 apphash interchangeable / 已经印进本头 AppHash 交差 interchangeable / 370 info bundled interchangeable / info-sold-as-handshake interchangeable；把进了头 / 会写进每一块的 Header / 进头了 写成已经是本高度交差 interchangeable / 已经 settled interchangeable / 已经是本高度交差交差 interchangeable；把字段在 / app_version 字段在 / 版本字段在 写成已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，或已经和 370 info bundled / info-sold-as-handshake interchangeable / 858 info-notapphash interchangeable。

## 为什么错

官方把有版本、不是已经是本高度交差、不是已经选型写成三件独立的实现事。把它们卖成 already apphash interchangeable / already settled interchangeable / already algo interchangeable，会把 not already apphash、not already settled、not already algo 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量），必须分开 not already apphash、not already settled、not already algo 三件事，不要和 370 / 147 / 857 / 859 糊成一句。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 info bundled 全段，不是本页有版本 item 2 单句边界。
- [info-notstatesync-sold-as-bundled](info-notstatesync-sold-as-bundled.md) 是握手对齐 not already statesync（370 item 1），不是本页 not already apphash 边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差（147），不是本页 not already apphash 单句。
