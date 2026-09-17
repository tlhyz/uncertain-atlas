# 例：看见 lane_id in ResponseInfo range is not already Info table selection interchangeable / not already in-table means prioritized interchangeable / not already CheckTx response field bundled interchangeable

**层次**：实现 / CheckTx Usage lane_id in ResponseInfo range not Info table selection / not in-table means prioritized / not CheckTx response field bundled 正式三事（482 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage lane_id in ResponseInfo range not Info table selection / not in-table means prioritized / not CheckTx response field bundled 正式三事（482 余量）/ not 706 chktxlane-notrange interchangeable / not 482 chktxlane-vs-default bundled interchangeable」，不是 CheckTx Usage lane_id 正式二事 bundled（482），也不是 Info 车道（367）或 CheckTx 回包栏（381）。不要另写怎样写 lane_priorities。

## 官方三件事

1. **看见 The value of `lane_id` has to be in the range of lanes defined by the application in `ResponseInfo` / 看见填了道必须在 Info 定义过的车道范围内 / in range is not already 已经 Info 回了 `lane_priorities` / `default_lane` 就算选型交差（367） interchangeable / 367 infolane interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 706 chktxlane-notrange interchangeable / 704 chktxlane-notreserved interchangeable / 482 chktxlane item 1 empty interchangeable，也不是已经 lane_id in ResponseInfo range not Info table selection / not in-table means prioritized / not CheckTx response field bundled 正式三事 bundled（482 item 3 余量） interchangeable / 482 chktxlane item 3 interchangeable。**  
   官方 Usage 写：The value of lane_id has to be in the range of lanes defined by the application in ResponseInfo。看见 in the range of lanes defined in ResponseInfo，不是已经 Info 车道表对上了 interchangeable——367 钉 Info 配置，本页从 482 item 3 侧钉 not Info table selection 单句。482 chktxlane vs default bundled unbundling 在本页 item 3 完成。

2. **看见必须在范围内 / 看见 Usage 这句 / in range is not already 已经填了 lane_id 在表里就代表已经排了优先 interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 706 chktxlane-notrange interchangeable / 482 chktxlane item 2 assigned interchangeable / 705 chktxlane-notassigned interchangeable。**  
   官方把 Usage in range 单句和填了就排了优先路径分开——482 bundled 第三件事常与 317/367 混成「看见必须在范围内就已经排了优先 interchangeable」，本页钉 not in-table means prioritized 单句。

3. **看见 Usage 这句 / 看见必须在 ResponseInfo 范围内 / in range is not already 已经 CheckTx Response 表 `lane_id` 栏（381） bundled 第三件事 interchangeable / 381 chktxlane-range interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 706 chktxlane-notrange interchangeable / 704 chktxlane-notreserved interchangeable。**  
   官方把 Usage 范围约束和 CheckTx Response 字段 bundled 分开——381 钉 Response 字段描述，本页钉 CheckTx Usage 侧约束。482 chktxlane vs default bundled unbundling 在本页 item 3 完成。

怎样填 lane_id、怎样选 default_lane、怎样写 lane_priorities 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **lane_id in range not Info table selection ≠ 367 interchangeable：** 官方把 Usage 侧范围约束和 Info 车道表选型分开。
- **lane_id in range not in-table means prioritized ≠ 填了就排了优先 interchangeable：** 官方把必须在范围内和填了就排了优先分开。
- **lane_id in range not CheckTx response field bundled ≠ 381 interchangeable：** 官方把 Usage 范围约束和 Response 字段 bundled 分开；482 chktxlane vs default bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| lane_id in ResponseInfo range | 不是 Info 表选型交差（367） | 不是 empty lane_id（704/482 item 1） |
| 看见必须在范围内 | 不是填了就排了优先 | 不是 assigned to default lane（705/482 item 2） |
| 看见 Usage 这句 | 不是 CheckTx 回包栏 bundled（381） | 不是 CheckTx Usage lane_id bundled（482） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage lane_id in ResponseInfo range not Info table selection / not in-table means prioritized / not CheckTx response field bundled 正式三事（482 余量），必须分开 in range 是不是 Info 表选型 interchangeable / 367、是不是填了就排了优先、是不是 CheckTx 回包栏 bundled interchangeable / 381。可以跳过「看见必须在范围内就已经选型交差」。不要另写怎样写 lane_priorities。482 chktxlane vs default bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样填 lane_id、怎样选 default_lane、怎样写 lane_priorities。
- CheckTx Usage lane_id 正式二事 bundled。那是不变量 482。
- empty lane_id。那是不变量 482 item 1 余量 / 704。
- assigned to the default lane。那是不变量 482 item 2 余量 / 705。
- Info 车道。那是不变量 367。
- CheckTx 回包栏。那是不变量 381。
