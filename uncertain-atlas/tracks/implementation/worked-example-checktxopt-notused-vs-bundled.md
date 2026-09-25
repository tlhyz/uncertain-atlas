# 例：看见有码 / 看见码在 / 看见拒了 is not already already used interchangeable / already consensus interchangeable / already fork interchangeable

**层次**：实现 / 引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量）/ not 868 checktxopt-notused interchangeable / not 373 checktxopt bundled interchangeable」，不是 checktxopt bundled（373），也不是 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算（866 item 1 余量）或 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块（867 item 2 余量）。不要另写怎样写 CheckTx 可选。

## 官方三件事

规范把 Methods 里引擎对回包码不再赋予别的含义 和「已经是有码就已经被引擎用了 Data interchangeable / 已经是码在就已经是共识顺序 interchangeable / 已经是拒了就已经分叉 interchangeable / 已经是 checktxopt bundled interchangeable」分开写成三件独立的实现事，不是「看见有码就已经被引擎用了 Data interchangeable / 就已经是共识顺序 interchangeable / 就已经分叉 interchangeable」一件事：

1. **看见有码 / 看见引擎对回包码不再赋予别的含义 / 看见有回包码 is not already 已经被引擎用了 Data interchangeable / 已经 used interchangeable / 已经被引擎用了 Data 交差 interchangeable / 373 checktxopt bundled interchangeable / 317 CheckTx Data interchangeable / checktxopt-sold-as-block interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 868 checktxopt-notused interchangeable / 373 checktxopt item 3 interchangeable，也不是已经引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事 bundled（373 item 3 余量） interchangeable / 373 checktxopt item 3 interchangeable，也不是已经能回就已经是四门（866） interchangeable / 已经拒了就已经没进块（867） interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 的 Data 就已经被引擎用了（317） interchangeable。**  
   官方写：CometBFT 对这个回包码不再赋予别的含义。看见有码，不是已经被引擎用了 `CheckTxResponse.Data`。看见有码，不是已经 used interchangeable——373 钉 bundled 三事，本页从 item 3 侧钉 not already used 单句。看见引擎对回包码不再赋予别的含义，不是已经 checktxopt bundled（373） interchangeable——373 钉 bundled，本页钉 item 3 第一件事。看见有码，不是已经能回就已经是四门（866） interchangeable——866 另钉 item 1。看见有码，不是已经拒了就已经没进块（867） interchangeable——867 另钉 item 2。373 checktxopt-vs-block bundled unbundling 在本页 item 3 完成。

2. **看见码在 / 看见回包码在 / 看见码列在 is not already 已经是共识顺序 interchangeable / 已经 consensus interchangeable / 已经是共识顺序交差 interchangeable / 373 checktxopt bundled interchangeable / 317 Priority interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 868 checktxopt-notused interchangeable / 373 checktxopt item 1 能回 interchangeable / 373 checktxopt item 2 拒了 interchangeable，也不是已经引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事 bundled（373 item 3 余量） interchangeable / 373 checktxopt item 3 interchangeable，也不是已经被引擎用了 Data（本页第一件事） interchangeable。**  
   官方写：看见码在，不是已经是共识顺序。看见回包码在，不是已经 consensus interchangeable——本页钉 not already consensus 单句。看见码列在，不是已经被引擎用了 Data（本页第一件事） interchangeable——三件事分开钉。373 checktxopt-vs-block bundled unbundling 在本页 item 3 完成。

3. **看见拒了 / 看见回包码拒了 / 看见码拒了 is not already 已经分叉 interchangeable / 已经 fork interchangeable / 已经分叉交差 interchangeable / 373 checktxopt bundled interchangeable / 711 CheckTx notfork interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 868 checktxopt-notused interchangeable / 373 checktxopt item 1 / 373 checktxopt item 2，也不是已经引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事 bundled（373 item 3 余量） interchangeable / 373 checktxopt item 3 interchangeable，也不是已经被引擎用了 Data（本页第一件事） interchangeable / 已经是共识顺序（本页第二件事） interchangeable。**  
   官方写：看见拒了，不是已经分叉。看见回包码拒了，不是已经 fork interchangeable——本页钉 not already fork 单句。看见码拒了，不是已经是共识顺序（本页第二件事） interchangeable——三件事分开钉。373 checktxopt-vs-block bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。checktxopt bundled（373）、CheckTx 技术上可选、不参与处理块不是已经是四门已经结算（373 item 1 余量 / 866）、Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块（373 item 2 余量 / 867）、四门已经结算（33）、Finalize 的 Code 非零就已经没进块（316）、CheckTx 的 Data 就已经被引擎用了（317）是另外那套，本页不抄。

## 官方为什么这样拆

- **有码 not already used ≠ 373 / 317 interchangeable：** 官方把回包码不再另有含义和 Data / Priority 分开。
- **码在 not already consensus ≠ 已经是共识顺序 interchangeable：** 官方把码在和已经是共识顺序分开。
- **拒了 not already fork ≠ 已经分叉 interchangeable：** 官方把拒了和已经分叉分开；373 checktxopt-vs-block bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有码 | 不是 already used | 不是 CheckTx 的 Data 就已经被引擎用了 alone（317） |
| 码在 | 不是 already consensus | 不是能回 already fourgates alone（866） |
| 拒了 | 不是 already fork | 不是拒了 already excluded alone（867） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量），必须分开有码 是不是 already used interchangeable / 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable、码在 是不是 already consensus interchangeable、拒了 是不是 already fork interchangeable。可以跳过「看见有码就已经被引擎用了 Data interchangeable / 就已经是共识顺序 interchangeable / 就已经分叉 interchangeable」。不要另写怎样写 CheckTx 可选。373 checktxopt-vs-block bundled unbundling 在本页 item 3 完成（866 + 867 + 868）。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- checktxopt bundled。那是不变量 373。
- CheckTx 技术上可选、不参与处理块不是已经是四门已经结算。那是不变量 373 item 1 余量 / 866。
- Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块。那是不变量 373 item 2 余量 / 867。
- 四门已经结算。那是不变量 33。
- Finalize 的 Code 非零就已经没进块。那是不变量 316。
- CheckTx 的 Data 就已经被引擎用了。那是不变量 317。
