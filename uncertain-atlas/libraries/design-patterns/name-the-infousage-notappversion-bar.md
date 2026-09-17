# 模式：把 Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage app_version included in Header not last_block persisted ≠ bundled（494）](../../tracks/implementation/worked-example-infousage-notappversion-vs-bundled.md)。

## 三个名字

1. **app_version in Header 不是 last_block persisted during Commit：** 看见 The returned `app_version` will be included in the Header of every block，不是已经 Info 握手 bundled（370）第三件事 last_block persisted interchangeable，不是 370 info-handshake bundled interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 interchangeable / 494 infousage-vs-handshakebundled interchangeable / 670 infousage-notappversion interchangeable。

2. **returned app_version 不是 Info response version 栏：** 看见 returned app_version / 会写进每一块 Header，不是已经 Info 回包 version 是应用软件语义版本 interchangeable，不是 389 info-lane-fields interchangeable / 379 info-req-version interchangeable / 669 infousage-nothandshake interchangeable / 668 infousage-notquerystate interchangeable。

3. **included in Header 不是印进本头 AppHash：** 看见 app_version will be included in the Header of every block，不是已经印进本头 AppHash interchangeable，不是 147 apphash-this-block interchangeable / 320 crash recovery interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable。

官方把 Info Usage app_version in Header 单句、Info 握手 bundled 第三件事（370）、Info Response version 栏（389）、本头 AppHash 交差（147）写成三个名字。把它们叫成一个「看见 app_version included in Header 就已经 last_block persisted interchangeable / 就已经 Info version 栏 interchangeable / 就已经印进 AppHash interchangeable」，会把 not last_block persisted during Commit、not Info response version、not AppHash in header 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量），先数清问的是 app_version in Header 是不是 last_block persisted / 370 / 665 / 497，是不是 returned app_version 是不是 Info response version / 389 / 379 / 669，还是 included in Header 是不是 AppHash in header / 147 / 320 / 587，再决定要不要同一次发布。494 infousage vs handshake bundled unbundling 在本页 item 3 完成。
