# 例：看见 default_lane has to be one of the identifiers defined in lane_priorities 不是已经 Info 车道 bundled（367）第二件事 interchangeable；看见 lowest priority is 1 and 0 is reserved for empty lane_id in ResponseCheckTx 不是已经 Info 车道 bundled（367）第三件事 interchangeable

**层次**：实现 / Info Usage default_lane in table / priority 0 reserved 正式二事 part 3。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「default_lane must be in lane_priorities 不是 Info 车道 bundled interchangeable / priority 0 reserved for empty lane_id 不是 Info 车道 bundled interchangeable」，不是 Info Usage part 2（497），也不是 Info 车道 bundled（367）或 CheckTx Usage lane_id（482）。不要另写怎样填 lane_priorities、怎样选 default_lane、怎样写 lane_id。

## 官方两件事

规范把 Info Usage 第 7–8 条核心英文句写成两件独立的实现事，不是「看见 Info 回了 default_lane / 优先级 0 就已经选型、已经排了优先、已经进了块」一件事：

1. **看见 `default_lane` has to be one of the identifiers defined in `lane_priorities` / 看见 default_lane 必须是 lane_priorities 里定义过的一个标识 不是已经 Info 车道 bundled（367）第二件事 bundled 就代表已经选型 interchangeable，也不是已经 Info Usage part 2（497）lane_priorities empty iff default_lane empty interchangeable，也不是已经 CheckTx Usage lane_id in ResponseInfo range（482） bundled 就代表 Info 已经选型 interchangeable，也不是已经 Info 回包 default_lane 栏（389） bundled 就代表 Usage 已经验完 interchangeable。**  
   官方 Usage 写：`default_lane` has to be one of the identifiers defined in `lane_priorities`。看见 has to be one of the identifiers defined in lane_priorities，不是已经 Info 车道 bundled（367）第二件事 interchangeable——367 钉 bundled 三事（含 empty iff + default in table），本页钉 Methods Info Usage default in table 单句。看见 default_lane 必须在表里，不是已经 lane_priorities empty iff default_lane empty（497） interchangeable——497 钉 empty iff 规则，本页钉 default 必须在表里的约束。看见 default 在表里，不是已经 CheckTx lane_id 必须在 Info 定义范围内（482） interchangeable——482 钉 CheckTx Usage 侧范围，本页钉 Info Usage 侧 default_lane 配置。看见 Usage 这句，不是已经 Info 回包 lane_priorities / default_lane 栏（389） bundled 就代表已经选型 interchangeable。
2. **看见 The lowest priority a lane can have is `1`. The value `0` is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`) / 看见最低优先级是 1、0 留给应用不设道（ResponseCheckTx 里空 lane_id） 不是已经 Info 车道 bundled（367）第三件事 bundled 就代表已经进了块 interchangeable，也不是已经 CheckTx Usage lane_id empty → assigned to default lane（482） interchangeable，也不是已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable，也不是已经 CheckTx 回包 lane_id 必须在 Info 定义范围内（381） bundled interchangeable。**  
   官方 Usage 写：The lowest priority a lane can have is `1`. The value `0` is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`)。看见 lowest priority is 1，不是已经在 lane_priorities 里写了 0 就代表已经排了优先 interchangeable。看见 0 reserved for empty lane_id in ResponseCheckTx，不是已经 CheckTx Usage empty lane_id → default lane（482） interchangeable——482 钉 CheckTx Usage 引擎分配，本页钉 Info Usage priority 0 预留语义。看见 reserved for empty lane_id，不是已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable。看见 Usage 这句，不是已经 Info 车道 bundled（367）第三件事 bundled 就代表已经不从池里删掉 interchangeable——367 钉 bundled 池门语境，本页钉 Methods Info Usage priority 0 单句。

怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id` 是规范里的做法，本页不抄。Info Usage part 2（497）、Info 车道 bundled（367）、CheckTx Usage lane_id（482）、CheckTx 回包 lane_id 栏（381）、CheckTx 的 Priority 就已经是共识顺序（317）是另外那套，本页不抄。

## 官方为什么这样拆

- **default_lane must be in lane_priorities ≠ Info 车道 bundled interchangeable：** 官方把 Usage default in table 单句和 bundled 367 第二件事分开。
- **priority 0 reserved for empty lane_id ≠ Info 车道 bundled interchangeable：** 官方把 Usage priority 0 预留单句和 bundled 367 第三件事、CheckTx lane_id 分配分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| default_lane must be in lane_priorities | 不是 Info 车道 bundled（367） | 不是 empty iff（497） |
| priority 0 reserved for empty lane_id | 不是 Info 车道 bundled（367） | 不是 CheckTx lane_id default lane（482） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage default_lane in table / priority 0 reserved 正式二事 part 3，必须分开 default_lane must be in lane_priorities 是不是 Info 车道 bundled interchangeable / empty iff interchangeable / CheckTx lane_id in range interchangeable、priority 0 reserved for empty lane_id 是不是 Info 车道 bundled interchangeable / CheckTx lane_id default lane interchangeable / 已经排了优先。可以跳过「看见 Info 回了 default_lane / 优先级 0 就已经选型、已经进了块」。不要另写怎样写 Info 车道。 498 infousage default_lane/priority0 unbundling 在本页 item 1 启动；精读 [`worked-example-infousage-notintable-vs-bundled.md`](worked-example-infousage-notintable-vs-bundled.md)（不变量 663 item 1）；续 priority 0 reserved for empty lane_id（664 item 2 余量）。

## 本页不抄

- 怎样填 `lane_priorities`、怎样选 `default_lane`、怎样写 `lane_id`。
- Info Usage part 2。那是不变量 497。
- Info 车道 bundled。那是不变量 367。
- CheckTx Usage lane_id。那是不变量 482。
- CheckTx 回包 lane_id 栏。那是不变量 381。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
