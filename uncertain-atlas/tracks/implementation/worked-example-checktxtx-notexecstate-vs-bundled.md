# 例：看见 CheckTx 对照当前状态验、不应用这笔描述的状态改动 is not already ExecuteTxState interchangeable / not already processing block interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx 对照当前状态验 not already ExecuteTxState / not already processing block / not already settled 正式三事（391 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 对照当前状态验 not already ExecuteTxState / not already processing block / not already settled 正式三事（391 余量）/ not 753 checktxtx-notexecstate interchangeable / not 391 checktxtx-vs-recheck bundled interchangeable」，不是 CheckTx 请求余栏 bundled（391），也不是 CheckTx Usage validate-no-apply（486/680–682），也不是 CheckTxState 就已经是 ExecuteTxState（312）。不要另写怎样写 CheckTx 请求余栏。

## 官方三件事

1. **看见 CheckTx 对照当前状态验、不应用这笔描述的状态改动 / 看见验了 / CheckTx 这份对照当前状态 is not already 已经按将要执行的那份状态验过 interchangeable / 312 execstate interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 753 checktxtx-notexecstate interchangeable / 752 checktxtx-notrecheck interchangeable / 391 checktxtx item 1 tx interchangeable，也不是已经 validate not already ExecuteTxState / not already processing block / not already settled 正式三事 bundled（391 item 2 余量） interchangeable / 391 checktxtx item 2 interchangeable。**  
   官方写：CheckTx 对照应用当前状态验这笔交易，例如验签和余额，但不应用这笔描述的任何状态改动。看见验了，不是已经按 ExecuteTxState 验过 interchangeable——本页从 391 item 2 侧钉 not already ExecuteTxState 单句。391 checktxtx vs recheck bundled unbundling 在本页 item 2 续。

2. **看见验了 / 看见没应用改动 / CheckTx 这份对照当前状态 is not already 已经参与处理块 interchangeable / 373 fourgates interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 753 checktxtx-notexecstate interchangeable / 391 checktxtx item 3 info interchangeable / 754 checktxtx-notqueryinfo interchangeable，也不是已经 CheckTx Usage validate-no-apply interchangeable / 486 chktxvalidate / 680–682 chktxvalidate-not* interchangeable。**  
   官方把对照当前状态验和不应用改动、已经参与处理块分开——391 bundled 第二件事常与 486 / 373 混成「看见验了就已经是 Usage validate-no-apply 或已经处理块 interchangeable」，本页钉 not already processing block 单句。

3. **看见验了 / 看见对照当前状态 / CheckTx 这份对照当前状态 is not already 已经交差 interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 753 checktxtx-notexecstate interchangeable / 752 checktxtx-notrecheck interchangeable。**  
   官方把对照当前状态验和已经交差分开。看见对照当前状态，不是已经交差 interchangeable。391 checktxtx vs recheck bundled unbundling 在本页 item 2 续。

怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **validate not already ExecuteTxState ≠ 312 interchangeable：** 官方把对照当前状态验和按工作状态验分开。
- **validate not already processing block ≠ 373/486 interchangeable：** 官方把不应用改动和已经参与处理块 / Usage validate-no-apply 分开。
- **validate not already settled ≠ 已经交差 interchangeable：** 官方把对照当前状态验和已经交差分开；391 checktxtx vs recheck bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 对照当前状态验、不应用这笔描述的状态改动 | 不是已经按 ExecuteTxState 验过（312） | 不是 CheckTx 请求 tx（752/391 item 1） |
| 看见验了 | 不是已经参与处理块（373） | 不是 CheckTx Usage validate-no-apply（486/680） |
| 看见对照当前状态 | 不是已经交差 | 不是 CheckTx 请求余栏 bundled（391） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 对照当前状态验 not already ExecuteTxState / not already processing block / not already settled 正式三事（391 余量），必须分开是不是已经按 ExecuteTxState 验过 interchangeable / 312、是不是已经参与处理块 interchangeable / 373、是不是已经交差。可以跳过「看见验了就已经按 ExecuteTxState 验过」。不要另写怎样写 CheckTx 请求余栏。391 checktxtx vs recheck bundled unbundling 在本页 item 2 续；完成 [`worked-example-checktxtx-notqueryinfo-vs-bundled.md`](worked-example-checktxtx-notqueryinfo-vs-bundled.md)（不变量 754 item 3）。

## 本页不抄

- 怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息。
- CheckTx 请求余栏 bundled。那是不变量 391。
- CheckTx 请求 tx。那是不变量 391 item 1 余量 / 752。
- CheckTx 回包 info。那是不变量 391 item 3 余量 / 754。
- CheckTx Usage validate-no-apply。那是不变量 486 / 680–682。
- CheckTxState 就已经是 ExecuteTxState。那是不变量 312。
