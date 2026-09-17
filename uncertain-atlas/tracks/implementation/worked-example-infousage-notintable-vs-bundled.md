# 例：看见 default_lane has to be one of the identifiers defined in lane_priorities is not already Info 车道 bundled（367） interchangeable / empty iff（497） interchangeable / CheckTx lane_id in range（482） interchangeable

**层次**：实现 / Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量）/ not 663 infousage-notintable interchangeable / not 498 infousage-defaultlane bundled interchangeable」，不是 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498），也不是 Info 车道 bundled（367）。不要另写怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id。

## 官方三件事

规范把 Info Usage 里 `default_lane` has to be one of the identifiers defined in `lane_priorities` 和「已经是 Info 车道 bundled（367）第二件事 bundled 就代表已经选型 interchangeable / 已经是 Info Usage part 2（497）lane_priorities empty iff default_lane empty interchangeable / 已经是 CheckTx Usage lane_id in ResponseInfo range（482） bundled 就代表 Info 已经选型 interchangeable / 已经是 Info 回包 default_lane 栏（389） bundled 就代表 Usage 已经验完 interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 default_lane has to be one of identifiers defined in lane_priorities 就已经 Info 车道 bundled interchangeable / 就已经 empty iff interchangeable / 就已经 CheckTx lane_id in range interchangeable / 就已经选型 interchangeable」一件事：

1. **看见 `default_lane` has to be one of the identifiers defined in `lane_priorities` / 看见 default_lane 必须是 lane_priorities 里定义过的一个标识 is not already 已经 Info 车道 bundled（367）第二件事 bundled 就代表已经选型 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第二件事 interchangeable / 已经 lane_priorities empty iff default_lane empty interchangeable / 497 infousage-persist interchangeable / 650 offersnaptrust-notmetadata interchangeable，也不是已经 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498） interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable / 664 infousage-notpriorityzero interchangeable / 497 infousage-persist item 3 empty iff interchangeable，也不是已经 default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事 bundled（498 item 1 余量） interchangeable / 498 infousage-defaultlane item 1 interchangeable，也不是已经 priority 0 reserved for empty lane_id in ResponseCheckTx bundled（498 item 2 余量） interchangeable / 482 chktxlane interchangeable / 317 priority consensus interchangeable。**  
   官方 Usage 写：`default_lane` has to be one of the identifiers defined in `lane_priorities`。看见 has to be one of the identifiers defined in lane_priorities，不是已经 Info 车道 bundled（367）第二件事 interchangeable——367 钉 bundled 三事（含 empty iff + default in table），本页从 498 item 1 侧钉 not Info 车道 bundled 单句。看见 default_lane 必须在表里，不是已经 Info Usage default_lane in table / priority 0 reserved bundled（498） interchangeable——498 钉 bundled 二事，本页钉 Methods Info Usage default in table 单句。看见 default in table，不是已经 priority 0 reserved for empty lane_id（664/498 item 2） interchangeable——664 另钉 item 2，本页钉 item 1 第一件事。498 infousage default_lane/priority0 unbundling 在本页 item 1 启动。

2. **看见 default_lane has to be one of the identifiers defined in lane_priorities / has to be one of the identifiers is not already 已经 Info Usage part 2（497）lane_priorities empty iff default_lane empty interchangeable / 497 infousage-persist interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 已经 lane_priorities empty iff default_lane empty interchangeable / 367 infolane bundled interchangeable / 497 infousage-persist item 2 lane optional interchangeable，也不是已经 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498） interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane item 1 default in table interchangeable / 664 infousage-notpriorityzero interchangeable，也不是已经 default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事 bundled（498 item 1 余量） interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable，也不是已经 Info 车道 bundled（367）第一件事 lane optional / one lane interchangeable / 494 infousage item 1 app_version interchangeable。**  
   官方把 Usage default in table 单句和 Info Usage part 2 empty iff 规则分开——498 bundled 第一件事常与 497 混成「看见 default_lane in table 就已经 lane_priorities empty iff default_lane empty interchangeable / 就已经 empty iff interchangeable」，本页钉 not empty iff 单句。看见 has to be one of identifiers defined in lane_priorities，不是已经 lane_priorities empty iff default_lane empty interchangeable——497 钉 empty iff 规则，本页钉 Usage 侧 default 必须在表里的约束。看见 default_lane 必须在表里，不是已经 Info 车道 bundled（367）第一件事 lane optional interchangeable——367 钉 bundled 第一件事，本页钉 item 1 第二件事。

3. **看见 default_lane has to be one of the identifiers defined in lane_priorities / default_lane 必须是 lane_priorities 里定义过的一个标识 is not already 已经 CheckTx Usage lane_id in ResponseInfo range（482） bundled 就代表 Info 已经选型 interchangeable / 482 chktxlane interchangeable / 482 chktxlane item 2 lane_id in range interchangeable / 381 chktxlane-range interchangeable / 已经 CheckTx 回包 lane_id 必须在 Info 定义范围内 interchangeable / 317 priority consensus interchangeable / 已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable，也不是已经 Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498） interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane item 1 default in table interchangeable / 664 infousage-notpriorityzero interchangeable / 498 infousage-defaultlane item 2 priority 0 interchangeable，也不是已经 default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事 bundled（498 item 1 余量） interchangeable / 367 infolane bundled interchangeable / 497 infousage-persist interchangeable，也不是已经 Info 回包 default_lane 栏（389） bundled 就代表 Usage 已经验完 interchangeable / 389 info-lane-fields interchangeable / 494 infousage item 1 app_version interchangeable / 370 info-handshake interchangeable。**  
   官方把 Usage default in table 单句和 CheckTx Usage lane_id 范围路径分开——498 bundled 第一件事常与 482/381 混成「看见 default_lane in table 就已经 CheckTx lane_id in range interchangeable / 就已经 Info 已经选型 interchangeable」，本页钉 not CheckTx lane_id in range 单句。看见 default_lane 必须在表里，不是已经 CheckTx Usage lane_id in ResponseInfo range interchangeable——482 钉 CheckTx Usage 侧范围，本页钉 Info Usage 侧 default_lane 配置。看见 has to be one of identifiers defined in lane_priorities，不是已经 Info 回包 default_lane 栏（389） bundled interchangeable——389 钉 Response 栏，本页钉 item 1 第三件事。498 infousage default_lane/priority0 unbundling 在本页 item 1 启动。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。Info Usage default_lane in table / priority 0 reserved 正式二事 bundled（498）、priority 0 reserved for empty lane_id（498 item 2 余量）、Info Usage part 2（497）、Info 车道 bundled（367）、CheckTx Usage lane_id（482）、CheckTx 回包 lane_id 栏（381）、CheckTx 的 Priority 就已经是共识顺序（317）是另外那套，本页不抄。

## 官方为什么这样拆

- **default_lane in table not Info 车道 bundled ≠ 367 infolane bundled interchangeable：** 官方把 Methods Info Usage default in table 单句和 bundled 367 第二件事分开。
- **default_lane in table not empty iff ≠ 497 infousage-persist interchangeable：** 官方把 Usage default in table 单句和 Info Usage part 2 empty iff 规则分开。
- **default_lane in table not CheckTx lane_id in range ≠ 482 chktxlane interchangeable：** 官方把 Usage default in table 单句和 CheckTx Usage lane_id 范围路径分开；498 infousage default_lane/priority0 unbundling 启动（663 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| default_lane has to be one of identifiers defined in lane_priorities | 不是 Info 车道 bundled（367） | 不是 empty iff（497） |
| has to be one of the identifiers defined in lane_priorities | 不是 empty iff（497） | 不是 lane optional / one lane（367 item 1） |
| default_lane 必须是 lane_priorities 里定义过的一个标识 | 不是 CheckTx lane_id in range（482） | 不是 priority 0 reserved（664/498 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量），必须分开 default_lane has to be one of identifiers defined in lane_priorities 是不是 Info 车道 bundled interchangeable / 367 infolane bundled interchangeable / 497 infousage-persist interchangeable、has to be one of the identifiers defined in lane_priorities 是不是 empty iff interchangeable / 497 infousage-persist item 3 interchangeable / 367 infolane bundled interchangeable、default_lane 必须是 lane_priorities 里定义过的一个标识 是不是 CheckTx lane_id in range interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable。可以跳过「看见 default_lane in table 就已经 Info 车道 bundled interchangeable / 就已经 empty iff interchangeable / 就已经 CheckTx lane_id in range interchangeable」。不要另写怎样填 lane_priorities、怎样选 default_lane。498 infousage default_lane/priority0 unbundling 在本页 item 1 启动；续 [`worked-example-infousage-notpriorityzero-vs-bundled.md`](worked-example-infousage-notpriorityzero-vs-bundled.md)（不变量 664 item 2）。498 infousage default_lane/priority0 unbundling 完成（663→664）。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- Info Usage default_lane in table / priority 0 reserved 正式二事 bundled。那是不变量 498。
- priority 0 reserved for empty lane_id。那是不变量 498 item 2 余量 / 664。
- Info Usage part 2。那是不变量 497。
- Info 车道 bundled。那是不变量 367。
- CheckTx Usage lane_id。那是不变量 482。
- CheckTx 回包 lane_id 栏。那是不变量 381。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
