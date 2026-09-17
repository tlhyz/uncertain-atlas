# 反模式：把 Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量）说成已经 QueryState / 已经 Info data 栏 / 已经 handshake sync 交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage Return information about application state not QueryState ≠ bundled（494）](../../tracks/implementation/worked-example-infousage-notquerystate-vs-bundled.md)。

## 卖法

把 Return information about the application state 写成已经 QueryState 就已经是 ExecuteTxState interchangeable / 314 querystate interchangeable / 已经 Query 可以对当前或过去高度查 interchangeable / 已经 ExecuteTxState interchangeable / 371 queryheight interchangeable；把 return information about application state / 回报应用状态 写成已经 Info 回包 data 是任意信息 interchangeable / 389 info-lane-fields interchangeable / 已经 Info Response data 栏 interchangeable / 已经 data 是任意信息 interchangeable / 379 info-req-version interchangeable；把能回 Info 写成已经 Used to sync during handshake on startup or on recovery 就等于已经 persisted interchangeable / 370 info-handshake bundled interchangeable / 320 crash recovery interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 interchangeable，或已经和 494 infousage-vs-handshakebundled bundled / infousage-sold-as-handshakebundled interchangeable / 668 infousage-notquerystate interchangeable。

## 为什么错

官方把 Info Usage Return state 单句、QueryState vs ExecuteTxState（314）、Info Response data 栏（389）、handshake sync = persisted 路径写成三件独立的实现事。把它们卖成 QueryState interchangeable / Info data 栏 interchangeable / handshake sync 交差 interchangeable，会把 not QueryState、not Info response data arbitrary info、not handshake sync already persisted 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量），必须分开 not QueryState、not Info response data arbitrary info、not handshake sync already persisted 三件事，不要和 494 / 314 / 389 / 379 / 370 / 320 / 665 / 497 / 669 / 670 糊成一句。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手 bundled 三事，不是本页 Methods Info Usage Return state 单句边界。
- [infousage-notcommitpersist-sold-as-bundled](infousage-notcommitpersist-sold-as-bundled.md) 是 497 item 1 last_block persist 单句边界，不是本页 Return state 单句边界。
