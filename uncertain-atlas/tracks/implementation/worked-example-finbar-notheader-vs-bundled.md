# 例：看见 FinalizeBlockResponse.events is not already header-printed interchangeable / not already engine-handed interchangeable / not already must-det interchangeable

**层次**：实现 / FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量）/ not 1070 finbar-notheader interchangeable / not 431 finrespbar-vs-header bundled interchangeable」，不是 Finalize 回包栏 bundled（431），也不是 Prepare 里产出了事件就已经交给引擎（357），也不是 Code / Data 就已经印进本头（316）。不要另写怎样写 Finalize 回包栏。

## 官方三件事

1. **看见 FinalizeBlockResponse.events 是给索引用的类型键值事件 / 看见回了 events 这份栏 is not already 已经印进本头 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1070 finbar-notheader interchangeable / 1071 finbar-notchktx interchangeable / 431 finrespbar item 2 tx_results interchangeable，也不是已经 FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事 bundled（431 item 1 余量） interchangeable / 431 finrespbar item 1 interchangeable。**  
   官方写：events 是 Type & Key-Value events for indexing。Deterministic 列是 No。看见回了 events，不是已经印进本头 interchangeable——本页从 431 item 1 侧钉 not already header-printed 单句。431 finrespbar vs header bundled unbundling 在本页 item 1 启动。

2. **看见能指索引 / 看见回了 events / 这份栏 is not already 已经交给引擎 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1070 finbar-notheader interchangeable / 431 finrespbar item 3 validator_updates interchangeable / 1072 finbar-notrotate interchangeable，也不是已经 Prepare 里产出了事件就已经交给引擎 interchangeable / 357 prepvalid interchangeable。**  
   官方把能指索引和已经交给引擎分开。看见能指索引，不是已经交给引擎 interchangeable。本页钉 not already engine-handed 单句。

3. **看见标成非确定 / 看见回了 events / 这份栏 is not already 已经必须确定 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1070 finbar-notheader interchangeable / 1071 finbar-notchktx interchangeable，也不是已经 Code / Data 就已经印进本头 interchangeable / 316 exectx interchangeable。**  
   官方把标成非确定和已经必须确定分开。看见标成非确定，不是已经必须确定 interchangeable。431 finrespbar vs header bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.events not already header-printed ≠ 已经印进本头 interchangeable：** 官方把给索引用的事件和已经印进本头分开。
- **看见能指索引 not already engine-handed ≠ 已经交给引擎 interchangeable：** 官方把能指索引和已经交给引擎分开。
- **看见标成非确定 not already must-det ≠ 已经必须确定 interchangeable：** 官方把标成非确定和已经必须确定分开；431 finrespbar vs header bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.events 是给索引用的类型键值事件 | 不是已经印进本头 | 不是 Prepare 里产出了事件就已经交给引擎（357） |
| 看见能指索引 | 不是已经交给引擎 | 不是 Code / Data 就已经印进本头（316） |
| 看见标成非确定 | 不是已经必须确定 | 不是 tx_results 就已经是 CheckTx 回包（1071） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.events not already header-printed / not already engine-handed / not already must-det 正式三事（431 余量），必须分开是不是已经印进本头、是不是已经交给引擎、是不是已经必须确定。可以跳过「看见回了 Finalize 回包栏就已经印进本头」。不要另写怎样写 Finalize 回包栏。431 finrespbar vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-finbar-notchktx-vs-bundled.md`](worked-example-finbar-notchktx-vs-bundled.md)（不变量 1071 item 2）。

## 本页不抄

- 怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate。
- Finalize 回包栏 bundled。那是不变量 431。
- Prepare 里产出了事件就已经交给引擎。那是不变量 357。
- Code / Data 就已经印进本头。那是不变量 316。
