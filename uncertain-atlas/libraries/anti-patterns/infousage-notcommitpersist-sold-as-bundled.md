# 反模式：把 Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量）说成已经 Info 握手 bundled / 已经 Commit persist signal / 已经 Info 回包 last_block 栏

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage last_block persisted during Commit not Info 握手 bundled ≠ bundled（497）](../../tracks/implementation/worked-example-infousage-notcommitpersist-vs-bundled.md)。

## 卖法

把 CometBFT expects `last_block_app_hash` and `last_block_height` to be updated and persisted during `Commit` 写成已经 Info 用来握手对齐 bundled（370）第三件事 interchangeable / 370 info-handshake bundled interchangeable / 已经 Info 握手 bundled 第三件事 interchangeable / 494 infousage item 1 app_version interchangeable / 497 infousage-persist interchangeable；把 updated and persisted during Commit 写成已经 Commit Usage Signal the Application to persist application state interchangeable / 481 commitpersist interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable / 已经 Signal persist interchangeable / 已经 expected persist at end interchangeable；把 last_block_app_hash / last_block_height 写成已经 Info 回包 last_block_height / last_block_app_hash 栏 interchangeable / 389 info-lane-fields interchangeable / 已经 Info Response Latest height / Latest AppHash interchangeable / 147 apphash-this-block interchangeable，或已经和 497 infousage-persist bundled / infousage-persist-sold-as-committed interchangeable / 665 infousage-notcommitpersist interchangeable。

## 为什么错

官方把 Info Usage expects during Commit 单句、Info 握手 bundled（370）、Commit Usage persist signal（481）、Info Response last_block 栏（389）写成三件独立的实现事。把它们卖成 Info 握手 bundled interchangeable / Commit persist signal interchangeable / Info 回包 last_block 栏 interchangeable，会把 not Info 握手 bundled、not Commit persist signal、not Info response last_block fields 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量），必须分开 not Info 握手 bundled、not Commit persist signal、not Info response last_block fields 三件事，不要和 497 / 370 / 481 / 389 / 494 / 147 / 320 / 666 / 667 糊成一句。

## 和相邻反模式

- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 497 bundled 专用 last_block/lane 三事，不是本页 497 item 1 last_block persist 单句边界。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手 bundled 三事，不是本页 Methods Info Usage last_block persist 单句边界。
