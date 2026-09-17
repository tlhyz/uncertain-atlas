# 例：看见 CheckTx 回包 events 是给索引用的类型键值 is not already settled interchangeable / not already not-in-block interchangeable / not already consensus order interchangeable

**层次**：实现 / CheckTx 回包 events not already settled / not already not-in-block / not already consensus order 正式三事（381 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 回包 events not already settled / not already not-in-block / not already consensus order 正式三事（381 余量）/ not 786 checktxspace-notsettled interchangeable / not 381 checktxspace-vs-code bundled interchangeable」，不是 CheckTx 回包 bundled（381），也不是结果列表就已经同一顺序（316），也不是 Finalize 回包 events 就已经必须确定（382/784）。不要另写怎样写 CheckTx 回包。

## 官方三件事

1. **看见 CheckTx 回包 `events` 是给索引用的类型键值 / 看见回了事件 / CheckTx 这份索引事件 is not already 已经交差 interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 786 checktxspace-notsettled interchangeable / 785 checktxspace-notcode interchangeable / 381 checktxspace item 1 codespace interchangeable，也不是已经 events not already settled / not already not-in-block / not already consensus order 正式三事 bundled（381 item 2 余量） interchangeable / 381 checktxspace item 2 interchangeable。**  
   官方写：`events` 是给交易建索引的类型和键值，例如按账户。看见回了事件，不是已经交差 interchangeable——本页从 381 item 2 侧钉 not already settled 单句。381 checktxspace vs code bundled unbundling 在本页 item 2 续。

2. **看见回了事件 / 看见能按账户查 / CheckTx 这份索引事件 is not already 已经没进块 interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 786 checktxspace-notsettled interchangeable / 381 checktxspace item 3 lane_id interchangeable / 787 checktxspace-notlane interchangeable，也不是已经 Finalize 回包 events 就已经必须确定 interchangeable / 382 syncingheight / 784 syncingheight-notdet interchangeable。**  
   官方把能按账户查和已经没进块分开——381 bundled 第二件事常与 316 / 382 混成「看见回了事件就已经交差或已经没进块 interchangeable」，本页钉 not already not-in-block 单句。

3. **看见回了事件 / 看见有类型键值 / CheckTx 这份索引事件 is not already 已经是共识顺序 interchangeable / 316 txorder interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 786 checktxspace-notsettled interchangeable / 785 checktxspace-notcode interchangeable。**  
   官方把有类型键值和已经是共识顺序分开。看见有类型键值，不是已经是共识顺序 interchangeable。381 checktxspace vs code bundled unbundling 在本页 item 2 续。

怎样写 CheckTx 回包、怎样填码空间、怎样选道是规范里的做法，本页不抄。

## 官方为什么这样拆

- **events not already settled ≠ 已经交差 interchangeable：** 官方把索引事件和 Finalize 回执交差分开。
- **events not already not-in-block ≠ 已经没进块 interchangeable：** 官方把能按账户查和已经没进块分开。
- **events not already consensus order ≠ 316 interchangeable：** 官方把有类型键值和已经是共识顺序分开；381 checktxspace vs code bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 回包 events 是给索引用的类型键值 | 不是已经交差 | 不是 CheckTx 回包 codespace（785/381 item 1） |
| 看见回了事件 | 不是已经没进块 | 不是 Finalize 回包 events（382/784） |
| 看见有类型键值 | 不是已经是共识顺序（316） | 不是结果列表就已经同一顺序（316） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 events not already settled / not already not-in-block / not already consensus order 正式三事（381 余量），必须分开 events 是不是已经交差、是不是已经没进块、是不是已经是共识顺序 interchangeable / 316。可以跳过「看见回了事件就已经交差」。不要另写怎样写 CheckTx 回包。381 checktxspace vs code bundled unbundling 在本页 item 2 续；完成 [`worked-example-checktxspace-notlane-vs-bundled.md`](worked-example-checktxspace-notlane-vs-bundled.md)（不变量 787 item 3）。

## 本页不抄

- 怎样写 CheckTx 回包、怎样填码空间、怎样选道。
- CheckTx 回包 bundled。那是不变量 381。
- CheckTx 回包 codespace。那是不变量 381 item 1 余量 / 785。
- CheckTx 的 lane_id。那是不变量 381 item 3 余量 / 787。
- 结果列表就已经同一顺序。那是不变量 316。
- Finalize 回包 events 就已经必须确定。那是不变量 382 / 784。
