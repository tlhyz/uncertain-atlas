# 反模式：把 Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量）说成已经 last_block persisted / 已经 Info version 栏 / 已经印进 AppHash

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage app_version included in Header not last_block persisted ≠ bundled（494）](../../tracks/implementation/worked-example-infousage-notappversion-vs-bundled.md)。

## 卖法

把 The returned `app_version` will be included in the Header of every block 写成已经 Info 握手 bundled（370）第三件事 last_block persisted during Commit interchangeable / 370 info-handshake bundled interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 interchangeable / 481 commitpersist interchangeable / 已经 Info 握手 bundled 第三件事 interchangeable；把 returned app_version / 会写进每一块 Header 写成已经 Info 回包 version 是应用软件语义版本 interchangeable / 389 info-lane-fields interchangeable / 379 info-req-version interchangeable / 已经 Info Response version 栏 interchangeable / 已经 version 是应用软件语义版本 interchangeable；把 included in Header of every block 写成已经印进本头 AppHash interchangeable / 147 apphash-this-block interchangeable / 已经本头 AppHash 就已经是本高度交差 interchangeable / 320 crash recovery interchangeable / 587 finreturn interchangeable，或已经和 494 infousage-vs-handshakebundled bundled / info-sold-as-handshake interchangeable / 670 infousage-notappversion interchangeable。

## 为什么错

官方把 Info Usage app_version in Header 单句、Info 握手 bundled 第三件事（370）、Info Response version 栏（389）、本头 AppHash 交差（147）写成三件独立的实现事。把它们卖成 last_block persisted interchangeable / Info version 栏 interchangeable / 印进 AppHash interchangeable，会把 not last_block persisted during Commit、not Info response version、not AppHash in header 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量），必须分开 not last_block persisted during Commit、not Info response version、not AppHash in header 三件事，不要和 494 / 370 / 389 / 379 / 147 / 665 / 497 / 668 / 669 / 320 / 587 糊成一句。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手 bundled 三事，不是本页 Methods Info Usage app_version in Header 单句边界。
- [infousage-notcommitpersist-sold-as-bundled](infousage-notcommitpersist-sold-as-bundled.md) 是 497 item 1 last_block persist 单句边界，不是本页 app_version in Header 单句边界。
- [infousage-nothandshake-sold-as-bundled](infousage-nothandshake-sold-as-bundled.md) 是 494 item 2 handshake sync 单句边界，不是本页 item 3 app_version in Header 单句边界。
