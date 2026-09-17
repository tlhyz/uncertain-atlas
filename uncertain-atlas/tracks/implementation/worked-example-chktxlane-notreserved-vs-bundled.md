# 例：看见 empty lane_id is not already priority 0 reserved interchangeable / not already deleted from pool interchangeable / not already no-lane means rejected interchangeable

**层次**：实现 / CheckTx Usage empty lane_id not priority 0 reserved / not deleted from pool / not no-lane means rejected 正式三事（482 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage empty lane_id not priority 0 reserved / not deleted from pool / not no-lane means rejected 正式三事（482 余量）/ not 704 chktxlane-notreserved interchangeable / not 482 chktxlane-vs-default bundled interchangeable」，不是 CheckTx Usage lane_id 正式二事 bundled（482），也不是 Info 车道 priority 0（367）或 CheckTx 可选（373）。不要另写怎样填 lane_id。

## 官方三件事

1. **看见 If `lane_id` is an empty string, it means that the application did not set any lane in the response message / 看见空字符串表示应用没在 CheckTx 回包里设道 / empty is not already 已经 Info Usage 里 priority 0 留给不设道（367） interchangeable / 367 infolane interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 704 chktxlane-notreserved interchangeable / 705 chktxlane-notassigned interchangeable / 482 chktxlane item 2 assigned interchangeable，也不是已经 empty lane_id not priority 0 reserved / not deleted from pool / not no-lane means rejected 正式三事 bundled（482 item 1 余量） interchangeable / 482 chktxlane item 1 interchangeable。**  
   官方 Usage 写：If lane_id is an empty string, it means that the application did not set any lane in the response message。看见 empty string，不是已经 Info 侧 priority 0 留给不设道 interchangeable——367 钉 Info 预留，本页从 482 item 1 侧钉 not priority 0 reserved 单句。482 chktxlane vs default bundled unbundling 在本页 item 1 启动。

2. **看见应用没在回包里设道 / 看见 empty string / 看见 Usage 这句 is not already 已经从池里删掉 / 已经没进池 interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 704 chktxlane-notreserved interchangeable / 482 chktxlane item 3 range interchangeable / 706 chktxlane-notrange interchangeable。**  
   官方把 Usage empty lane_id 单句和从池里删掉路径分开——482 bundled 第一件事常与池门混成「看见没设道就已经从池里删掉 interchangeable」，本页钉 not deleted from pool 单句。

3. **看见 empty / 看见 Usage 这句 / 看见没设道 is not already 已经 CheckTx 技术上可选 / 已经可以不跑 CheckTx 就已经拒了（373） interchangeable / 373 checktxopt interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 704 chktxlane-notreserved interchangeable / 705 chktxlane-notassigned interchangeable。**  
   官方把 Usage empty lane_id 单句和 CheckTx 可选就已经拒了路径分开——482 bundled 第一件事常与 373 混成「看见空 lane_id 就已经可选拒 interchangeable」，本页钉 not no-lane means rejected 单句。482 chktxlane vs default bundled unbundling 在本页 item 1 启动。

怎样填 lane_id、怎样选 default_lane、怎样写 lane_priorities 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **empty lane_id not priority 0 reserved ≠ 367 interchangeable：** 官方把 CheckTx Usage 侧空 lane_id 和 Info 侧 priority 0 预留分开。
- **empty lane_id not deleted from pool ≠ 已经没进池 interchangeable：** 官方把没在回包里设道和从池里删掉分开。
- **empty lane_id not no-lane means rejected ≠ 373 interchangeable：** 官方把空 lane_id 和 CheckTx 可选就已经拒了分开；482 chktxlane vs default bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| empty lane_id | 不是 priority 0 留给不设道（367） | 不是 assigned to default lane（705/482 item 2） |
| 看见没在回包里设道 | 不是已经从池里删掉 | 不是 CheckTx Usage lane_id bundled（482） |
| 看见 Usage 这句 | 不是 CheckTx 可选就已经拒了（373） | 不是 lane_id in range（706/482 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage empty lane_id not priority 0 reserved / not deleted from pool / not no-lane means rejected 正式三事（482 余量），必须分开 empty 是不是 Info 侧 priority 0 不设道 interchangeable / 367、是不是已经从池里删掉、是不是 CheckTx 可选就已经拒了 interchangeable / 373。可以跳过「看见 CheckTx 回了空 lane_id 就已经不设道」。不要另写怎样填 lane_id。482 chktxlane vs default bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxlane-notassigned-vs-bundled.md`](worked-example-chktxlane-notassigned-vs-bundled.md)（不变量 705 item 2）。

## 本页不抄

- 怎样填 lane_id、怎样选 default_lane、怎样写 lane_priorities。
- CheckTx Usage lane_id 正式二事 bundled。那是不变量 482。
- assigned to the default lane。那是不变量 482 item 2 余量 / 705。
- lane_id in ResponseInfo range。那是不变量 482 item 3 余量 / 706。
- Info 车道 priority 0 留给不设道。那是不变量 367。
- CheckTx 技术上可选。那是不变量 373。
