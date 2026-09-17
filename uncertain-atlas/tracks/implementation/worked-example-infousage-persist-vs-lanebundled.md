# 例：看见 CometBFT expects last_block_app_hash and last_block_height updated and persisted during Commit 不是已经 Info 握手 bundled（370）第三件事 interchangeable；看见 application does not have to define lane_priorities 不是已经 Info 车道 bundled（367）第一件事 interchangeable；看见 lane_priorities is empty if and only if default_lane is empty 不是已经 Info 车道 bundled（367）第二件事 interchangeable

**层次**：实现 / Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「last_block persisted during Commit 不是 Info 握手 bundled interchangeable / does not have to define lane_priorities 不是 Info 车道 bundled interchangeable / lane_priorities empty iff default_lane empty 不是 Info 车道 bundled interchangeable」，不是 Info Usage 正式三事 part 1（494），也不是 Info 用来握手对齐 bundled（370）或 Info 车道 bundled（367）。不要另写怎样写 Info 回包、怎样填 lane_priorities、怎样落盘。

## 官方三件事

规范把 Info Usage 第 4–6 条核心英文句写成三件独立的实现事，不是「看见 Info 回了 last_block / 车道 就已经 Commit 交差、已经排了优先、已经选型」一件事：

1. **看见 CometBFT expects `last_block_app_hash` and `last_block_height` to be updated and persisted during `Commit` / 看见引擎指望 last_block 在 Commit 里更新并落盘 不是已经 Info 用来握手对齐 bundled（370）第三件事 interchangeable，也不是已经 Info Usage part 1（494）app_version included in Header interchangeable，也不是已经 Info 回包 last_block_height / last_block_app_hash 栏（389） bundled 就代表已经 persisted interchangeable，也不是已经 Commit Usage persist signal（481） bundled 就代表 Info 已经交差 interchangeable，也不是已经本头 AppHash 就已经是本高度交差（147） interchangeable，也不是已经崩溃三步就已经 Commit（320） interchangeable。**  
   官方 Usage 写：CometBFT expects `last_block_app_hash` and `last_block_height` to be updated and persisted during `Commit`。看见 updated and persisted during Commit，不是已经 Info 握手 bundled（370）第三件事 interchangeable——370 钉 bundled 三事，本页钉 Methods Info Usage last_block persist 单句。看见 expects during Commit，不是已经 Signal the Application to persist application state（481） bundled interchangeable——481 钉 Commit Usage persist signal，本页钉 Info Usage expects 语境。看见 last_block_app_hash / last_block_height，不是已经 Info Response 栏 Latest height / Latest AppHash（389） bundled 就代表已经落盘 interchangeable——389 钉 Response 栏语义，本页钉 Usage persist 义务。看见 persisted during Commit，不是已经本头 AppHash 就已经是本高度交差（147） interchangeable。看见要在 Commit 里落，不是已经崩溃三步就已经 Commit（320） interchangeable。
2. **看见 The application does not have to define `lane_priorities`. In that case, CometBFT will assign all transactions to one lane / 看见应用可以不定义 lane_priorities、这时引擎把交易都放进一条道 不是已经 Info 车道 bundled（367）第一件事 bundled 就代表已经排了优先 interchangeable，也不是已经 Info 回包 lane_priorities / default_lane 栏（389） bundled 就代表 Usage 已经验完 interchangeable，也不是已经 CheckTx Usage lane_id empty → default lane（482） interchangeable，也不是已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable。**  
   官方 Usage 写：The application does not have to define `lane_priorities`. In that case, CometBFT will assign all transactions to one lane。看见 does not have to define，不是已经 Info 车道 bundled（367）第一件事 interchangeable——367 钉 bundled 三事，本页钉 Methods Info Usage optional lane_priorities 单句。看见 assign all transactions to one lane，不是已经没填表就已经排了优先 interchangeable。看见并成一条道，不是已经 CheckTx lane_id empty → assigned to default lane（482） interchangeable——482 钉 CheckTx Usage lane_id，本页钉 Info Usage 不定义表时的引擎行为。看见 Usage 这句，不是已经 CheckTx 回包 lane_id 必须在 Info 定义范围内（381） bundled 就代表 Usage 已经验完 interchangeable。
3. **看见 `lane_priorities` is empty if and only if `default_lane` is empty / 看见 lane_priorities 空当且仅当 default_lane 空 不是已经 Info 车道 bundled（367）第二件事 bundled 就代表已经选型 interchangeable，也不是已经 default_lane has to be one of the identifiers defined in lane_priorities（Usage 下一条） interchangeable，也不是已经 priority 0 留给不设道（367 bundled 第三件事） interchangeable，也不是已经 CheckTx Usage lane_id in ResponseInfo range（482） bundled interchangeable。**  
   官方 Usage 写：`lane_priorities` is empty if and only if `default_lane` is empty。看见 empty if and only if，不是已经 Info 车道 bundled（367）第二件事 interchangeable——367 钉 bundled 三事，本页钉 Methods Info Usage empty iff 单句。看见空对空，不是已经选型 interchangeable。看见 lane_priorities 空当且仅当 default_lane 空，不是已经 default_lane must be in lane_priorities（Usage bullet 7） interchangeable——bullet 7 钉 default 必须在表里，本页钉 empty iff 规则。看见 Usage 这句，不是已经 priority 0 留给不设道 interchangeable——367 bundled 第三件事 bundled，本页钉 empty iff 单句。

怎样写 Info 回包、怎样填 lane_priorities、怎样在 Commit 落盘是规范里的做法，本页不抄。Info Usage 正式三事 part 1（494）、Info 用来握手对齐 bundled（370）、Info 回包 data / version / last_block 栏（389）、Commit Usage persist signal（481）、Info 车道 bundled（367）、CheckTx Usage lane_id（482）是另外那套，本页不抄。

## 官方为什么这样拆

- **last_block persisted during Commit ≠ Info 握手 bundled interchangeable：** 官方把 Usage expects during Commit 和 bundled 370 第三件事分开。
- **does not have to define lane_priorities ≠ Info 车道 bundled interchangeable：** 官方把 optional lane_priorities 单句和 bundled 367 第一件事分开。
- **lane_priorities empty iff default_lane empty ≠ Info 车道 bundled interchangeable：** 官方把 empty iff 规则和 bundled 367 第二件事分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| last_block persisted during Commit | 不是 Info 握手 bundled（370） | 不是 Commit persist signal（481） |
| does not have to define lane_priorities | 不是 Info 车道 bundled（367） | 不是 CheckTx lane_id default lane（482） |
| lane_priorities empty iff default_lane empty | 不是 Info 车道 bundled（367） | 不是 default_lane must be in lane_priorities（Usage bullet 7） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2，必须分开 last_block persisted during Commit 是不是 Info 握手 bundled interchangeable / 已经 Commit 交差 / Info 回包 last_block 栏 interchangeable、does not have to define lane_priorities 是不是 Info 车道 bundled interchangeable / 已经排了优先、lane_priorities empty iff default_lane empty 是不是 Info 车道 bundled interchangeable / 已经选型。可以跳过「看见 Info 回了 last_block / 车道 就已经 Commit 交差、已经排了优先」。不要另写怎样写 Info。

## 本页不抄

- 怎样写 Info 回包、怎样填 lane_priorities、怎样在 Commit 落盘。
- Info Usage 正式三事 part 1。那是不变量 494。
- Info 用来握手对齐 bundled。那是不变量 370。
- Info 回包 data / version / last_block 栏。那是不变量 389。
- Commit Usage persist signal。那是不变量 481。
- Info 车道 bundled。那是不变量 367。
- CheckTx Usage lane_id。那是不变量 482。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- 崩溃三步就已经 Commit。那是不变量 320。
