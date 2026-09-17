# 例：看见 The lowest priority a lane can have is 1 / 0 is reserved for empty lane_id in ResponseCheckTx is not already Info 车道 bundled（367） interchangeable / CheckTx empty lane_id default lane（482） interchangeable / CheckTx Priority consensus order（317） interchangeable

**层次**：实现 / Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量）/ not 664 infousage-notpriorityzero interchangeable / not 663 infousage-notintable interchangeable / not 498 infousage-defaultlane bundled interchangeable」，不是 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498），也不是 Info 车道 bundled（367）。不要另写怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id。

## 官方三件事

规范把 Info Usage 里 The lowest priority a lane can have is `1`. The value `0` is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`) 和「已经是 Info 车道 bundled（367）第三件事 bundled 就代表已经进了块 interchangeable / 已经是 CheckTx Usage lane_id empty → assigned to default lane（482） interchangeable / 已经是 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable / 已经是 CheckTx 回包 lane_id 必须在 Info 定义范围内（381） bundled interchangeable / 已经排了优先 interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 priority 0 reserved for empty lane_id 就已经 Info 车道 bundled interchangeable / 就已经 CheckTx empty lane_id default lane interchangeable / 就已经 Priority 共识顺序 interchangeable / 就已经排了优先 interchangeable」一件事：

1. **看见 The lowest priority a lane can have is `1`. The value `0` is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`) / 看见最低优先级是 1、0 留给应用不设道（ResponseCheckTx 里空 lane_id） is not already 已经 Info 车道 bundled（367）第三件事 bundled 就代表已经进了块 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第三件事 interchangeable / 已经 lane_priorities empty iff default_lane empty interchangeable / 497 infousage-persist interchangeable / 663 infousage-notintable interchangeable，也不是已经 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498） interchangeable / 664 infousage-notpriorityzero interchangeable / 498 infousage-defaultlane interchangeable / 663 infousage-notintable interchangeable / 497 infousage-persist item 3 empty iff interchangeable，也不是已经 priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事 bundled（498 item 2 余量） interchangeable / 498 infousage-defaultlane item 2 interchangeable，也不是已经 default_lane has to be one of identifiers defined in lane_priorities bundled（498 item 1 余量 / 663） interchangeable / 663 infousage-notintable interchangeable / 482 chktxlane interchangeable。**  
   官方 Usage 写：The lowest priority a lane can have is `1`. The value `0` is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`)。看见 lowest priority is 1，不是已经在 lane_priorities 里写了 0 就代表已经排了优先 interchangeable——367 钉 bundled 池门语境，本页从 498 item 2 侧钉 not Info 车道 bundled 单句。看见 0 reserved for empty lane_id in ResponseCheckTx，不是已经 Info 车道 bundled（367）第三件事 interchangeable——367 钉 bundled 三事，本页钉 Methods Info Usage priority 0 单句。看见 priority 0 reserved，不是已经 default_lane in table（663/498 item 1） interchangeable——663 另钉 item 1，本页钉 item 2 第一件事。498 infousage default_lane/priority0 unbundling 在本页 item 2 续。

2. **看见 0 is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`) / 0 留给 ResponseCheckTx 里空 lane_id is not already 已经 CheckTx Usage lane_id empty → assigned to default lane（482） interchangeable / 482 chktxlane interchangeable / 482 chktxlane item 1 empty lane_id default lane interchangeable / 381 chktxlane-range interchangeable / 已经 empty lane_id → default lane interchangeable / 已经 assigned to the default lane interchangeable / 317 priority consensus interchangeable，也不是已经 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498） interchangeable / 664 infousage-notpriorityzero interchangeable / 498 infousage-defaultlane item 2 priority 0 interchangeable / 663 infousage-notintable interchangeable，也不是已经 priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事 bundled（498 item 2 余量） interchangeable / 367 infolane bundled interchangeable / 497 infousage-persist item 2 lane optional interchangeable，也不是已经 Info 回包 lane_id 必须在 Info 定义范围内（381） bundled interchangeable / 389 info-lane-fields interchangeable / 494 infousage item 1 app_version interchangeable。**  
   官方把 Usage priority 0 预留单句和 CheckTx Usage empty lane_id → default lane 路径分开——498 bundled 第二件事常与 482 混成「看见 priority 0 reserved 就已经 CheckTx empty lane_id default lane interchangeable / 就已经 assigned to default lane interchangeable」，本页钉 not CheckTx empty lane_id default lane 单句。看见 0 reserved for empty lane_id in ResponseCheckTx，不是已经 CheckTx Usage empty lane_id → default lane interchangeable——482 钉 CheckTx Usage 引擎分配，本页钉 Info Usage priority 0 预留语义。看见 reserved for empty lane_id，不是已经 empty lane_id 就代表已经从池里删掉 interchangeable——482 另钉池门语境，本页钉 item 2 第二件事。

3. **看见 The lowest priority a lane can have is `1` / lowest priority is 1 / 0 is reserved for empty lane_id is not already 已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable / 317 priority consensus interchangeable / 已经 Priority 字段 interchangeable / 已经排了优先 interchangeable / 已经进了块 interchangeable / 482 chktxlane item 1 empty lane_id default lane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable，也不是已经 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498） interchangeable / 664 infousage-notpriorityzero interchangeable / 498 infousage-defaultlane item 2 priority 0 interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane item 1 default in table interchangeable，也不是已经 priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事 bundled（498 item 2 余量） interchangeable / 367 infolane bundled interchangeable / 497 infousage-persist interchangeable，也不是已经 lane_priorities 里写了 0 就代表已经排了优先 interchangeable / 494 infousage item 1 app_version interchangeable / 370 info-handshake interchangeable。**  
   官方把 Usage priority 0 预留单句和 CheckTx Priority 共识顺序路径分开——498 bundled 第二件事常与 317/381 混成「看见 priority 0 reserved 就已经 Priority 共识顺序 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」，本页钉 not CheckTx Priority consensus order 单句。看见 lowest priority is 1，不是已经在 lane_priorities 里写了 0 就代表已经排了优先 interchangeable——367 钉 bundled 排优先语境，本页钉 Usage 侧最低优先级是 1 单句。看见 0 reserved for empty lane_id，不是已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable——317 钉 Priority 字段，本页钉 item 2 第三件事。498 infousage default_lane/priority0 unbundling 在本页 item 2 完成。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498）、default_lane has to be one of identifiers defined in lane_priorities（498 item 1 余量 / 663）、Info Usage part 2（497）、Info 车道 bundled（367）、CheckTx Usage lane_id（482）、CheckTx 回包 lane_id 栏（381）、CheckTx 的 Priority 就已经是共识顺序（317）是另外那套，本页不抄。

## 官方为什么这样拆

- **priority 0 reserved not Info 车道 bundled ≠ 367 infolane bundled interchangeable：** 官方把 Methods Info Usage priority 0 单句和 bundled 367 第三件事分开。
- **priority 0 reserved not CheckTx empty lane_id default lane ≠ 482 chktxlane interchangeable：** 官方把 Usage priority 0 预留单句和 CheckTx Usage empty lane_id → default lane 路径分开。
- **priority 0 reserved not CheckTx Priority consensus order ≠ 317 priority consensus interchangeable：** 官方把 Usage priority 0 单句和 CheckTx Priority 共识顺序路径分开；498 infousage default_lane/priority0 unbundling 完成（664 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| lowest priority is 1 / 0 reserved for empty lane_id | 不是 Info 车道 bundled（367） | 不是 default in table（663/498 item 1） |
| 0 reserved for empty lane_id in ResponseCheckTx | 不是 CheckTx empty lane_id default lane（482） | 不是 CheckTx lane_id range（381） |
| priority 0 reserved | 不是 CheckTx Priority consensus order（317） | 不是 lane_priorities 写了 0 就排了优先 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量），必须分开 lowest priority is 1 / 0 reserved for empty lane_id 是不是 Info 车道 bundled interchangeable / 367 infolane bundled interchangeable / 497 infousage-persist interchangeable / 663 infousage-notintable interchangeable、0 reserved for empty lane_id in ResponseCheckTx 是不是 CheckTx empty lane_id default lane interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable、priority 0 reserved 是不是 CheckTx Priority consensus order interchangeable / 317 priority consensus interchangeable / 494 infousage item 1 app_version interchangeable。可以跳过「看见 priority 0 reserved 就已经 Info 车道 bundled interchangeable / 就已经 CheckTx empty lane_id default lane interchangeable / 就已经 Priority 共识顺序 interchangeable」。不要另写怎样填 lane_priorities、怎样选 default_lane。498 infousage default_lane/priority0 unbundling 在本页 item 2 完成。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- Info Usage default_lane in table / priority 0 reserved 正式二事 bundled。那是不变量 498。
- default_lane has to be one of identifiers defined in lane_priorities。那是不变量 498 item 1 余量 / 663。
- Info Usage part 2。那是不变量 497。
- Info 车道 bundled。那是不变量 367。
- CheckTx Usage lane_id。那是不变量 482。
- CheckTx 回包 lane_id 栏。那是不变量 381。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
