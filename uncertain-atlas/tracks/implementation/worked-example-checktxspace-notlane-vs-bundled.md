# 例：看见 CheckTx 的 lane_id 必须在 Info 回包车道范围内 is not already no-lane interchangeable / not already prioritized interchangeable / not already in-block interchangeable

**层次**：实现 / CheckTx lane_id not already no-lane / not already prioritized / not already in-block 正式三事（381 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx lane_id not already no-lane / not already prioritized / not already in-block 正式三事（381 余量）/ not 787 checktxspace-notlane interchangeable / not 381 checktxspace-vs-code bundled interchangeable」，不是 CheckTx 回包 bundled（381），也不是没定义 lane_priorities 就已经排了优先（367），也不是空 lane_id 就已经放进默认道（482）。不要另写怎样写 CheckTx 回包。

## 官方三件事

1. **看见 CheckTx 的 `lane_id` 必须在 Info 回包车道范围内 / 看见填了道 / CheckTx 这份车道 is not already 已经空 `lane_id` 那种不设道 interchangeable / 367 laneprio interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 787 checktxspace-notlane interchangeable / 785 checktxspace-notcode interchangeable / 381 checktxspace item 1 codespace interchangeable，也不是已经 lane_id not already no-lane / not already prioritized / not already in-block 正式三事 bundled（381 item 3 余量） interchangeable / 381 checktxspace item 3 interchangeable。**  
   官方写：`lane_id` 的值必须落在应用在 `ResponseInfo` 里定义过的那些道。看见填了道，不是已经空 `lane_id` 那种不设道 interchangeable——本页从 381 item 3 侧钉 not already no-lane 单句。381 checktxspace vs code bundled unbundling 在本页 item 3 完成。

2. **看见填了道 / 看见在范围内 / CheckTx 这份车道 is not already 已经排了优先 interchangeable / 367 laneprio interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 787 checktxspace-notlane interchangeable / 381 checktxspace item 2 events interchangeable / 786 checktxspace-notsettled interchangeable，也不是已经空 lane_id 就已经放进默认道 interchangeable / 482 chktxlane interchangeable。**  
   官方把在范围内和已经排了优先分开——381 bundled 第三件事常与 367 / 482 混成「看见填了道就已经不设道或已经排了优先 interchangeable」，本页钉 not already prioritized 单句。

3. **看见填了道 / 看见能指道 / CheckTx 这份车道 is not already 已经进了块 interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 787 checktxspace-notlane interchangeable / 785 checktxspace-notcode interchangeable。**  
   官方把能指道和已经进了块分开。看见能指道，不是已经进了块 interchangeable。381 checktxspace vs code bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx 回包、怎样填码空间、怎样选道是规范里的做法，本页不抄。

## 官方为什么这样拆

- **lane_id not already no-lane ≠ 367 interchangeable：** 官方把必须落在 Info 车道里和空 lane_id 留给不设道分开。
- **lane_id not already prioritized ≠ 367 interchangeable：** 官方把在范围内和已经排了优先分开。
- **lane_id not already in-block ≠ 已经进了块 interchangeable：** 官方把能指道和已经进了块分开；381 checktxspace vs code bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 的 lane_id 必须在 Info 回包车道范围内 | 不是已经不设道（367） | 不是 CheckTx 回包 codespace（785/381 item 1） |
| 看见填了道 | 不是已经排了优先（367） | 不是空 lane_id 就已经放进默认道（482） |
| 看见能指道 | 不是已经进了块 | 不是 CheckTx 回包 bundled（381） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx lane_id not already no-lane / not already prioritized / not already in-block 正式三事（381 余量），必须分开 lane_id 是不是已经不设道 interchangeable / 367、是不是已经排了优先、是不是已经进了块。可以跳过「看见填了道就已经不设道」。不要另写怎样写 CheckTx 回包。381 checktxspace vs code bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 CheckTx 回包、怎样填码空间、怎样选道。
- CheckTx 回包 bundled。那是不变量 381。
- CheckTx 回包 codespace。那是不变量 381 item 1 余量 / 785。
- CheckTx 回包 events。那是不变量 381 item 2 余量 / 786。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
- 空 lane_id 就已经放进默认道。那是不变量 482。
