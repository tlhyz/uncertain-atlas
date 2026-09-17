# 例：看见 CheckTx 回包 info 是附加信息 is not already Query info interchangeable / not already CheckTx log interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx 回包 info not already Query info / not already CheckTx log / not already settled 正式三事（391 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 回包 info not already Query info / not already CheckTx log / not already settled 正式三事（391 余量）/ not 754 checktxtx-notqueryinfo interchangeable / not 391 checktxtx-vs-recheck bundled interchangeable」，不是 CheckTx 请求余栏 bundled（391），也不是 Query 回包 info 就已经是按键查（384），也不是 CheckTx 回包 log 就已经是 Query 日志（390/745）。不要另写怎样写 CheckTx 请求余栏。

## 官方三件事

1. **看见 CheckTx 回包 `info` 是附加信息 / 看见回了信息 / CheckTx 这份附加信息 is not already 已经是 Query 回包那份附加信息 interchangeable / 384 queryinfo interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 754 checktxtx-notqueryinfo interchangeable / 752 checktxtx-notrecheck interchangeable / 391 checktxtx item 1 tx interchangeable，也不是已经 info not already Query info / not already CheckTx log / not already settled 正式三事 bundled（391 item 3 余量） interchangeable / 391 checktxtx item 3 interchangeable。**  
   官方写：`info` 是附加信息。看见回了信息，不是已经是 Query 回包那份附加信息 interchangeable——本页从 391 item 3 侧钉 not already Query info 单句。391 checktxtx vs recheck bundled unbundling 在本页 item 3 完成。

2. **看见回了信息 / 看见有附加字段 / CheckTx 这份附加信息 is not already 已经是 CheckTx 回包那份日志 interchangeable / 390 proofop / 745 proofop-notquerylog interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 754 checktxtx-notqueryinfo interchangeable / 391 checktxtx item 2 validate interchangeable / 753 checktxtx-notexecstate interchangeable。**  
   官方把 CheckTx 这份附加信息和 CheckTx 回包日志分开——391 bundled 第三件事常与 384 / 390 混成「看见回了信息就已经是 Query 附加信息或 CheckTx 日志 interchangeable」，本页钉 not already CheckTx log 单句。

3. **看见回了信息 / 看见能回 / CheckTx 这份附加信息 is not already 已经交差 interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 754 checktxtx-notqueryinfo interchangeable / 752 checktxtx-notrecheck interchangeable。**  
   官方把能回 CheckTx 回包 info 和已经交差分开。看见能回，不是已经交差 interchangeable。391 checktxtx vs recheck bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **info not already Query info ≠ 384 interchangeable：** 官方把 CheckTx 这份附加信息和 Query 那份附加信息分开。
- **info not already CheckTx log ≠ 390/745 interchangeable：** 官方把有附加字段和 CheckTx 回包日志分开。
- **info not already settled ≠ 已经交差 interchangeable：** 官方把能回 info 和已经交差分开；391 checktxtx vs recheck bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 回包 info 是附加信息 | 不是已经是 Query 附加信息（384） | 不是 CheckTx 请求 tx（752/391 item 1） |
| 看见回了信息 | 不是已经是 CheckTx 日志（390/745） | 不是 CheckTx 请求余栏 bundled（391） |
| 看见能回 | 不是已经交差 | 不是 Query 回包 info 就已经是按键查（384） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 info not already Query info / not already CheckTx log / not already settled 正式三事（391 余量），必须分开 info 是不是已经是 Query 附加信息 interchangeable / 384、是不是已经是 CheckTx 日志 interchangeable / 390、是不是已经交差。可以跳过「看见回了信息就已经是 Query 附加信息」。不要另写怎样写 CheckTx 请求余栏。391 checktxtx vs recheck bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息。
- CheckTx 请求余栏 bundled。那是不变量 391。
- CheckTx 请求 tx。那是不变量 391 item 1 余量 / 752。
- CheckTx 对照当前状态验。那是不变量 391 item 2 余量 / 753。
- Query 回包 info 就已经是按键查。那是不变量 384。
- CheckTx 回包 log 就已经是 Query 日志。那是不变量 390 / 745。
