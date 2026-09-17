# 例：看见 lane_priorities is empty if and only if default_lane is empty is not already Info 车道 bundled（367） interchangeable / default_lane in table（663/498） interchangeable / CheckTx lane_id in range（482） interchangeable

**层次**：实现 / Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量）/ not 667 infousage-notemptyiff interchangeable / not 666 infousage-notlaneoptional interchangeable / not 497 infousage-persist bundled interchangeable」，不是 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497），也不是 Info 车道 bundled（367）。不要另写怎样写 Info 回包、怎样填 lane_priorities。

## 官方三件事

规范把 Info Usage 里 `lane_priorities` is empty if and only if `default_lane` is empty 和「已经是 Info 车道 bundled（367）第二件事 bundled 就代表已经选型 interchangeable / 已经是 default_lane has to be one of the identifiers defined in lane_priorities（663/498 item 1） interchangeable / 已经是 priority 0 留给不设道（367/664/498 item 2） interchangeable / 已经是 CheckTx Usage lane_id in ResponseInfo range（482） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 lane_priorities empty iff default_lane empty 就已经 Info 车道 bundled interchangeable / 就已经 default in table interchangeable / 就已经 CheckTx lane_id in range interchangeable / 就已经选型 interchangeable」一件事：

1. **看见 `lane_priorities` is empty if and only if `default_lane` is empty / 看见 lane_priorities 空当且仅当 default_lane 空 is not already 已经 Info 车道 bundled（367）第二件事 bundled 就代表已经选型 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第二件事 interchangeable / 已经 lane optional / one lane interchangeable / 497 infousage-persist interchangeable / 666 infousage-notlaneoptional interchangeable / 665 infousage-notcommitpersist interchangeable，也不是已经 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497） interchangeable / 667 infousage-notemptyiff interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 663 infousage-notintable interchangeable / 664 infousage-notpriorityzero interchangeable / 498 infousage-defaultlane interchangeable，也不是已经 lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事 bundled（497 item 3 余量） interchangeable / 497 infousage-persist item 3 interchangeable，也不是已经 does not have to define lane_priorities bundled（497 item 2 余量 / 666） interchangeable / 482 chktxlane interchangeable。**  
   官方 Usage 写：`lane_priorities` is empty if and only if `default_lane` is empty。看见 empty if and only if，不是已经 Info 车道 bundled（367）第二件事 interchangeable——367 钉 bundled 三事，本页从 497 item 3 侧钉 not Info 车道 bundled 单句。看见 lane_priorities 空当且仅当 default_lane 空，不是已经 Info Usage last_block persisted / lane_priorities bundled（497） interchangeable——497 钉 bundled 三事，本页钉 Methods Info Usage empty iff 单句。看见空对空，不是已经 does not have to define lane_priorities（666/497 item 2） interchangeable——666 另钉 item 2，本页钉 item 3 第一件事。497 infousage persist/lane unbundling 在本页 item 3 完成。

2. **看见 empty if and only if / lane_priorities 空当且仅当 default_lane 空 is not already 已经 default_lane has to be one of the identifiers defined in lane_priorities（663/498 item 1） interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable / 498 infousage-defaultlane item 1 default in table interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 389 info-lane-fields interchangeable / 389 info-lane-fields item 2 default_lane interchangeable / 已经 default_lane must be in lane_priorities interchangeable / 已经 default in table interchangeable，也不是已经 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497） interchangeable / 667 infousage-notemptyiff interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 666 infousage-notlaneoptional interchangeable / 665 infousage-notcommitpersist interchangeable，也不是已经 lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事 bundled（497 item 3 余量） interchangeable / 367 infolane bundled interchangeable / 494 infousage item 1 app_version interchangeable，也不是已经 priority 0 reserved for empty lane_id bundled（664/498 item 2） interchangeable / 664 infousage-notpriorityzero interchangeable / 498 infousage-defaultlane item 2 priority 0 interchangeable。**  
   官方把 Usage empty iff 单句和 default_lane must be in lane_priorities 路径分开——497 bundled 第三件事常与 663/498 混成「看见 lane_priorities empty iff default_lane empty 就已经 default in table interchangeable / 就已经 default_lane must be in lane_priorities interchangeable / 就已经选型 interchangeable」，本页钉 not default_lane in table 单句。看见 empty if and only if，不是已经 default_lane has to be one of identifiers defined in lane_priorities interchangeable——663/498 另钉 default in table，本页钉 Info Usage empty iff 规则。看见 lane_priorities 空当且仅当 default_lane 空，不是已经 priority 0 reserved for empty lane_id interchangeable——664 另钉 priority 0，本页钉 item 3 第二件事。

3. **看见 lane_priorities is empty if and only if default_lane is empty / 空对空 is not already 已经 CheckTx Usage lane_id in ResponseInfo range（482） bundled interchangeable / 482 chktxlane interchangeable / 482 chktxlane item 2 lane_id in range interchangeable / 381 chktxlane-range interchangeable / 已经 CheckTx 回包 lane_id 必须在 Info 定义范围内 interchangeable / 317 priority consensus interchangeable / 664 infousage-notpriorityzero interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable，也不是已经 Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497） interchangeable / 667 infousage-notemptyiff interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 666 infousage-notlaneoptional interchangeable / 665 infousage-notcommitpersist interchangeable，也不是已经 lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事 bundled（497 item 3 余量） interchangeable / 367 infolane bundled interchangeable / 389 info-lane-fields interchangeable，也不是已经 priority 0 留给不设道 interchangeable / 367 infolane bundled item 3 interchangeable / 494 infousage item 1 app_version interchangeable / 370 info-handshake interchangeable。**  
   官方把 Usage empty iff 单句和 CheckTx Usage lane_id 范围路径分开——497 bundled 第三件事常与 482/381 混成「看见 lane_priorities empty iff default_lane empty 就已经 CheckTx lane_id in range interchangeable / 就已经 Info 已经选型 interchangeable / 就已经 priority 0 不设道 interchangeable」，本页钉 not CheckTx lane_id in range 单句。看见 empty if and only if，不是已经 CheckTx Usage lane_id in ResponseInfo range interchangeable——482 钉 CheckTx Usage 侧范围，本页钉 Info Usage empty iff 规则。看见 lane_priorities 空当且仅当 default_lane 空，不是已经 priority 0 留给不设道 interchangeable——367/664 另钉 priority 0 语境，本页钉 item 3 第三件事。497 infousage persist/lane unbundling 在本页 item 3 完成。

怎样写 Info 回包、怎样填 lane_priorities 是规范里的做法，本页不抄。Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled（497）、last_block persisted during Commit（497 item 1 余量 / 665）、does not have to define lane_priorities（497 item 2 余量 / 666）、default_lane has to be one of identifiers defined in lane_priorities（498 item 1 余量 / 663）、Info 车道 bundled（367）、CheckTx Usage lane_id（482）、CheckTx 回包 lane_id 栏（381）是另外那套，本页不抄。

## 官方为什么这样拆

- **lane_priorities empty iff default_lane empty not Info 车道 bundled ≠ 367 infolane bundled interchangeable：** 官方把 Methods Info Usage empty iff 单句和 bundled 367 第二件事分开。
- **empty iff not default_lane in table ≠ 663 infousage-notintable interchangeable：** 官方把 Usage empty iff 单句和 default_lane must be in lane_priorities 路径分开。
- **empty iff not CheckTx lane_id in range ≠ 482 chktxlane interchangeable：** 官方把 Usage empty iff 单句和 CheckTx Usage lane_id 范围路径分开；497 infousage persist/lane unbundling 完成（667 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| lane_priorities empty iff default_lane empty | 不是 Info 车道 bundled（367） | 不是 optional lane_priorities（666/497 item 2） |
| empty if and only if | 不是 default in table（663/498 item 1） | 不是 priority 0 reserved（664/498 item 2） |
| 空对空 | 不是 CheckTx lane_id in range（482） | 不是 Info response lane fields（389） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量），必须分开 lane_priorities empty iff default_lane empty 是不是 Info 车道 bundled interchangeable / 367 infolane bundled interchangeable / 666 infousage-notlaneoptional interchangeable / 665 infousage-notcommitpersist interchangeable、empty if and only if 是不是 default_lane in table interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable / 389 info-lane-fields interchangeable、空对空 是不是 CheckTx lane_id in range interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 664 infousage-notpriorityzero interchangeable。可以跳过「看见 lane_priorities empty iff default_lane empty 就已经 Info 车道 bundled interchangeable / 就已经 default in table interchangeable / 就已经 CheckTx lane_id in range interchangeable」。不要另写怎样写 Info 回包、怎样填 lane_priorities。497 infousage persist/lane unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Info 回包、怎样填 lane_priorities、怎样在 Commit 落盘。
- Info Usage last_block persisted during Commit / lane_priorities 正式三事 bundled。那是不变量 497。
- last_block persisted during Commit。那是不变量 497 item 1 余量 / 665。
- does not have to define lane_priorities。那是不变量 497 item 2 余量 / 666。
- default_lane has to be one of identifiers defined in lane_priorities。那是不变量 498 item 1 余量 / 663。
- Info 车道 bundled。那是不变量 367。
- CheckTx Usage lane_id。那是不变量 482。
- CheckTx 回包 lane_id 栏。那是不变量 381。
- priority 0 reserved for empty lane_id。那是不变量 498 item 2 余量 / 664。
