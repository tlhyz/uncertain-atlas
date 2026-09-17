# 例：看见引擎对回包码不再赋予别的含义 is not already Data used interchangeable / not already consensus order interchangeable / not already forked interchangeable

**层次**：实现 / 回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事（373 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事（373 余量）/ not 808 checktxopt-notdata interchangeable / not 373 checktxopt-vs-block bundled interchangeable」，不是 CheckTx 可选 bundled（373），也不是 CheckTx 的 Data 就已经被引擎用了（317），也不是 Usage no other value 就已经用了 Data（489/688），也不是 CheckTx events 就已经是共识顺序（381/786）。不要另写怎样写 CheckTx 可选。

## 官方三件事

1. **看见引擎对回包码不再赋予别的含义 / 看见有码 / 这份回包码 is not already 已经被引擎用了 Data interchangeable / 317 chktxdata interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 808 checktxopt-notdata interchangeable / 806 checktxopt-notsettled interchangeable / 373 checktxopt item 1 可选 interchangeable，也不是已经回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事 bundled（373 item 3 余量） interchangeable / 373 checktxopt item 3 interchangeable。**  
   官方写：CometBFT 对这个回包码不再赋予别的含义。看见有码，不是已经被引擎用了 `CheckTxResponse.Data` interchangeable——本页从 373 item 3 侧钉 not already Data used 单句。373 checktxopt vs block bundled unbundling 在本页 item 3 完成。

2. **看见有码 / 看见码在 / 这份回包码 is not already 已经是共识顺序 interchangeable / 317 chktxdata interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 808 checktxopt-notdata interchangeable / 373 checktxopt item 2 Code≠0 interchangeable / 807 checktxopt-notinblock interchangeable，也不是已经 Usage no other value 就已经用了 Data interchangeable / 489 chktxcodereject / 688 chktxcodereject-notothervalue interchangeable，也不是已经 CheckTx events 就已经是共识顺序 interchangeable / 381 checktxspace / 786 checktxspace-notsettled interchangeable。**  
   官方把码在和已经是共识顺序分开——373 bundled 第三件事常与 317 / 489 / 381 混成「看见有码就已经被引擎用了 Data 或已经是共识顺序 interchangeable」，本页钉 not already consensus order 单句。

3. **看见有码 / 看见拒了 / 这份回包码 is not already 已经分叉 interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 808 checktxopt-notdata interchangeable / 806 checktxopt-notsettled interchangeable。**  
   官方把拒了和已经分叉分开。看见拒了，不是已经分叉 interchangeable。373 checktxopt vs block bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。

## 官方为什么这样拆

- **回包码不再另有含义 not already Data used ≠ 317 interchangeable：** 官方把回包码不再另有含义和 Data / Priority 分开。
- **看见码在 not already consensus order ≠ 已经是共识顺序 interchangeable：** 官方把码在和已经是共识顺序分开。
- **看见拒了 not already forked ≠ 已经分叉 interchangeable：** 官方把拒了和已经分叉分开；373 checktxopt vs block bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 引擎对回包码不再赋予别的含义 | 不是已经被引擎用了 Data（317） | 不是可选（806/373 item 1） |
| 看见有码 | 不是已经是共识顺序 | 不是 Usage no other value（489/688） |
| 看见拒了 | 不是已经分叉 | 不是 CheckTx events（381/786） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事（373 余量），必须分开是不是已经被引擎用了 Data interchangeable / 317、是不是已经是共识顺序、是不是已经分叉。可以跳过「看见有码就已经被引擎用了 Data」。不要另写怎样写 CheckTx 可选。373 checktxopt vs block bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- CheckTx 可选 bundled。那是不变量 373。
- CheckTx 可选。那是不变量 373 item 1 余量 / 806。
- CheckTx 的 Data 就已经被引擎用了。那是不变量 317。
- Usage no other value 就已经用了 Data。那是不变量 489 / 688。
