# 例：看见 CometBFT expects last_block_app_hash and last_block_height updated and persisted during Commit is not already Info 握手 bundled（370） interchangeable / Commit persist signal（481） interchangeable / Info response last_block fields（389） interchangeable

**层次**：实现 / Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量）/ not 665 infousage-notcommitpersist interchangeable / not 497 infousage-persist bundled interchangeable」，不是 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497），也不是 Info 用来握手对齐 bundled（370）。不要另写怎样写 Info 回包、怎样在 Commit 落盘。

## 官方三件事

规范把 Info Usage 里 CometBFT expects `last_block_app_hash` and `last_block_height` to be updated and persisted during `Commit` 和「已经是 Info 用来握手对齐 bundled（370）第三件事 interchangeable / 已经是 Info Usage part 1（494）app_version included in Header interchangeable / 已经是 Info 回包 last_block_height / last_block_app_hash 栏（389） bundled 就代表已经 persisted interchangeable / 已经是 Commit Usage persist signal（481） bundled 就代表 Info 已经交差 interchangeable / 已经是本头 AppHash 就已经是本高度交差（147） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 last_block persisted during Commit 就已经 Info 握手 bundled interchangeable / 就已经 Commit persist signal interchangeable / 就已经 Info 回包 last_block 栏 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 CometBFT expects `last_block_app_hash` and `last_block_height` to be updated and persisted during `Commit` / 看见引擎指望 last_block 在 Commit 里更新并落盘 is not already 已经 Info 用来握手对齐 bundled（370）第三件事 interchangeable / 370 info-handshake bundled interchangeable / 370 info-handshake item 3 last_block persisted interchangeable / 已经 Info 握手 bundled 第三件事 interchangeable / 494 infousage item 1 app_version interchangeable / 389 info-lane-fields interchangeable，也不是已经 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497） interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist interchangeable / 666 infousage-notlaneoptional interchangeable / 667 infousage-notemptyiff interchangeable / 497 infousage-persist item 2 lane optional interchangeable，也不是已经 last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事 bundled（497 item 1 余量） interchangeable / 497 infousage-persist item 1 interchangeable，也不是已经 does not have to define lane_priorities bundled（497 item 2 余量 / 666） interchangeable / 481 commitpersist interchangeable / 320 crash recovery interchangeable。**  
   官方 Usage 写：CometBFT expects `last_block_app_hash` and `last_block_height` to be updated and persisted during `Commit`。看见 updated and persisted during Commit，不是已经 Info 握手 bundled（370）第三件事 interchangeable——370 钉 bundled 三事，本页从 497 item 1 侧钉 not Info 握手 bundled 单句。看见 expects during Commit，不是已经 Info Usage last_block persisted / lane_priorities bundled（497） interchangeable——497 钉 bundled 三事，本页钉 Methods Info Usage last_block persist 单句。看见 last_block_app_hash / last_block_height，不是已经 does not have to define lane_priorities（666/497 item 2） interchangeable——666 另钉 item 2，本页钉 item 1 第一件事。497 infousage persist/lane unbundling 在本页 item 1 启动。

2. **看见 updated and persisted during Commit / expects during Commit / last_block 在 Commit 里更新并落盘 is not already 已经 Commit Usage Signal the Application to persist application state（481） bundled 就代表 Info 已经交差 interchangeable / 481 commitpersist interchangeable / 481 commitpersist item 1 persist signal interchangeable / 481 commitpersist item 2 expected persist at end interchangeable / 335 finpersist interchangeable / 478 finpersist interchangeable / 已经 Signal persist interchangeable / 已经 expected persist at end of this call interchangeable，也不是已经 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497） interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 last_block persisted interchangeable / 666 infousage-notlaneoptional interchangeable / 667 infousage-notemptyiff interchangeable，也不是已经 last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事 bundled（497 item 1 余量） interchangeable / 370 info-handshake interchangeable / 494 infousage item 1 app_version interchangeable / 389 info-lane-fields interchangeable，也不是已经 已经在 Finalize 改了就已经落盘 interchangeable / 587 finreturn interchangeable / 403 finafter interchangeable / 320 crash recovery interchangeable。**  
   官方把 Usage expects during Commit 单句和 Commit Usage persist signal 路径分开——497 bundled 第一件事常与 481 混成「看见 last_block persisted during Commit 就已经 Signal persist interchangeable / 就已经 expected persist at end interchangeable / 就已经 Info 已经交差 interchangeable」，本页钉 not Commit persist signal 单句。看见 updated and persisted during Commit，不是已经 Commit Usage persist signal interchangeable——481 钉 Commit Usage 侧 persist signal，本页钉 Info Usage expects 语境。看见 expects during Commit，不是已经 已经在 Finalize 改了就已经落盘 interchangeable——335/587 另钉 Finalize/Commit 路径，本页钉 item 1 第二件事。

3. **看见 last_block_app_hash and last_block_height / last_block 在 Commit 里更新并落盘 is not already 已经 Info 回包 last_block_height / last_block_app_hash 栏（389） bundled 就代表已经 persisted interchangeable / 389 info-lane-fields interchangeable / 389 info-lane-fields item 3 last_block fields interchangeable / 494 infousage item 1 app_version interchangeable / 370 info-handshake item 3 last_block persisted interchangeable / 已经 Info Response Latest height / Latest AppHash interchangeable / 已经 Info 回包 last_block 栏 interchangeable，也不是已经 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497） interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 last_block persisted interchangeable / 666 infousage-notlaneoptional interchangeable / 667 infousage-notemptyiff interchangeable / 498 infousage-defaultlane interchangeable，也不是已经 last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事 bundled（497 item 1 余量） interchangeable / 147 apphash-this-block interchangeable / 320 crash recovery interchangeable / 370 info-handshake interchangeable，也不是已经本头 AppHash 就已经是本高度交差 interchangeable / 481 commitpersist interchangeable / 663 infousage-notintable interchangeable。**  
   官方把 Usage expects during Commit 单句和 Info Response last_block 栏路径分开——497 bundled 第一件事常与 389/494 混成「看见 last_block persisted during Commit 就已经 Info 回包 last_block 栏 interchangeable / 就已经 app_version in Header interchangeable / 就已经 persisted interchangeable」，本页钉 not Info response last_block fields 单句。看见 last_block_app_hash / last_block_height，不是已经 Info Response 栏 Latest height / Latest AppHash interchangeable——389 钉 Response 栏语义，本页钉 Usage persist 义务。看见 persisted during Commit，不是已经本头 AppHash 就已经是本高度交差 interchangeable——147 另钉 AppHash 语境，本页钉 item 1 第三件事。497 infousage persist/lane unbundling 在本页 item 1 启动。

怎样写 Info 回包、怎样在 Commit 落盘是规范里的做法，本页不抄。Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497）、does not have to define lane_priorities（497 item 2 余量 / 666）、lane_priorities empty iff default_lane empty（497 item 3 余量 / 667）、Info Usage 正式三事 part 1（494）、Info 用来握手对齐 bundled（370）、Commit Usage persist signal（481）是另外那套，本页不抄。

## 官方为什么这样拆

- **last_block persisted during Commit not Info 握手 bundled ≠ 370 info-handshake bundled interchangeable：** 官方把 Methods Info Usage last_block persist 单句和 bundled 370 第三件事分开。
- **last_block persisted during Commit not Commit persist signal ≠ 481 commitpersist interchangeable：** 官方把 Usage expects during Commit 单句和 Commit Usage persist signal 路径分开。
- **last_block persisted during Commit not Info response last_block fields ≠ 389 info-lane-fields interchangeable：** 官方把 Usage expects during Commit 单句和 Info Response last_block 栏路径分开；497 infousage persist/lane unbundling 启动（665 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| last_block persisted during Commit | 不是 Info 握手 bundled（370） | 不是 does not have to define lane_priorities（666/497 item 2） |
| updated and persisted during Commit | 不是 Commit persist signal（481） | 不是 Finalize 改了就已经落盘（335/587） |
| last_block_app_hash / last_block_height | 不是 Info response last_block fields（389） | 不是 apphash this block（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage last_block persisted during Commit not Info 握手 bundled / not Commit persist signal / not Info response last_block fields 正式三事（497 余量），必须分开 last_block persisted during Commit 是不是 Info 握手 bundled interchangeable / 370 info-handshake bundled interchangeable / 494 infousage item 1 app_version interchangeable、updated and persisted during Commit 是不是 Commit persist signal interchangeable / 481 commitpersist interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable、last_block_app_hash / last_block_height 是不是 Info response last_block fields interchangeable / 389 info-lane-fields interchangeable / 147 apphash-this-block interchangeable / 320 crash recovery interchangeable。可以跳过「看见 last_block persisted during Commit 就已经 Info 握手 bundled interchangeable / 就已经 Commit persist signal interchangeable / 就已经 Info 回包 last_block 栏 interchangeable」。不要另写怎样写 Info 回包、怎样在 Commit 落盘。497 infousage persist/lane unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样写 Info 回包、怎样填 lane_priorities、怎样在 Commit 落盘。
- Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled。那是不变量 497。
- does not have to define lane_priorities。那是不变量 497 item 2 余量 / 666。
- lane_priorities empty iff default_lane empty。那是不变量 497 item 3 余量 / 667。
- Info Usage 正式三事 part 1。那是不变量 494。
- Info 用来握手对齐 bundled。那是不变量 370。
- Commit Usage persist signal。那是不变量 481。
- Info 回包 data / version / last_block 栏。那是不变量 389。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- 崩溃三步就已经 Commit。那是不变量 320。
