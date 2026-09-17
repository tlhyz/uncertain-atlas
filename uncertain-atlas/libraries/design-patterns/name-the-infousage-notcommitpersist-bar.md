# 模式：把 Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage last_block persisted during Commit not Info 握手 bundled ≠ bundled（497）](../../tracks/implementation/worked-example-infousage-notcommitpersist-vs-bundled.md)。

## 三个名字

1. **last_block persisted during Commit 不是 Info 握手 bundled：** 看见 CometBFT expects last_block_app_hash and last_block_height updated and persisted during Commit，不是已经 Info 用来握手对齐 bundled（370）第三件事 interchangeable，不是 370 info-handshake bundled interchangeable / 494 infousage item 1 app_version interchangeable / 497 infousage-persist interchangeable。

2. **updated and persisted during Commit 不是 Commit persist signal：** 看见 expects during Commit，不是已经 Commit Usage Signal the Application to persist application state interchangeable，不是 481 commitpersist interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable / 403 finafter interchangeable。

3. **last_block_app_hash / last_block_height 不是 Info response last_block fields：** 看见 last_block 在 Commit 里更新并落盘，不是已经 Info 回包 last_block_height / last_block_app_hash 栏 interchangeable，不是 389 info-lane-fields interchangeable / 147 apphash-this-block interchangeable / 320 crash recovery interchangeable。

官方把 Info Usage last_block persist 单句、Info 握手 bundled（370）、Commit persist signal（481）、Info Response last_block 栏（389）写成三个名字。把它们叫成一个「看见 last_block persisted during Commit 就已经 Info 握手 bundled interchangeable / 就已经 Commit persist signal interchangeable / 就已经 Info 回包 last_block 栏 interchangeable」，会把 not Info 握手 bundled、not Commit persist signal、not Info response last_block fields 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量），先数清问的是 last_block persisted during Commit 是不是 Info 握手 bundled / 370 / 494，是不是 updated and persisted during Commit 是不是 Commit persist signal / 481 / 335 / 587，还是 last_block_app_hash / last_block_height 是不是 Info response last_block fields / 389 / 147 / 320，再决定要不要同一次发布。497 infousage persist/lane unbundling 在本页 item 1 启动。
