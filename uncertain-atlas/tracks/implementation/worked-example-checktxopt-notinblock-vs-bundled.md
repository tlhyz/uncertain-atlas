# 例：看见 Code ≠ 0 会被拒、不会广播也不会进提案 is not already not-in-block interchangeable / not already byzantine blocked interchangeable / not already settled interchangeable

**层次**：实现 / Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事（373 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事（373 余量）/ not 807 checktxopt-notinblock interchangeable / not 373 checktxopt-vs-block bundled interchangeable」，不是 CheckTx 可选 bundled（373），也不是 Finalize 的 Code 非零就已经没进块（316），也不是 Usage Code≠0 就已经拒广播（489/686），也不是 CheckTx codespace 就已经是回包码（381/785）。不要另写怎样写 CheckTx 可选。

## 官方三件事

1. **看见 `Code ≠ 0` 会被拒、不会广播也不会进提案 / 看见拒了 / 这份拒收 is not already 已经没进块 interchangeable / 316 txorder interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 807 checktxopt-notinblock interchangeable / 806 checktxopt-notsettled interchangeable / 373 checktxopt item 1 可选 interchangeable，也不是已经 Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事 bundled（373 item 2 余量） interchangeable / 373 checktxopt item 2 interchangeable。**  
   官方写：`CheckTxResponse.Code ≠ 0` 的交易会被拒，不会广播给别的节点，也不会装进提案。看见拒了，不是已经是 Finalize 那种 Code 非零仍在块里 interchangeable——本页从 373 item 2 侧钉 not already not-in-block 单句。373 checktxopt vs block bundled unbundling 在本页 item 2 续。

2. **看见拒了 / 看见没广播 / 这份拒收 is not already 已经被池子挡住拜占庭 interchangeable / 316 txorder interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 807 checktxopt-notinblock interchangeable / 373 checktxopt item 3 回包码 interchangeable / 808 checktxopt-notdata interchangeable，也不是已经 Usage Code≠0 就已经拒广播 interchangeable / 489 chktxcodereject / 686 chktxcodereject-notgossip interchangeable，也不是已经 CheckTx codespace 就已经是回包码 interchangeable / 381 checktxspace / 785 checktxspace-notcode interchangeable。**  
   官方把没广播和已经被池子挡住拜占庭分开——373 bundled 第二件事常与 316 / 489 / 381 混成「看见拒了就已经没进块或已经被挡住 interchangeable」，本页钉 not already byzantine blocked 单句。

3. **看见拒了 / 看见没进提案 / 这份拒收 is not already 已经交差 interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 807 checktxopt-notinblock interchangeable / 806 checktxopt-notsettled interchangeable。**  
   官方把没进提案和已经交差分开。看见没进提案，不是已经交差 interchangeable。373 checktxopt vs block bundled unbundling 在本页 item 2 续。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Code≠0 拒收 not already not-in-block ≠ 316 interchangeable：** 官方把内存池拒收和 Finalize 那种 Code 非零仍在块里分开。
- **看见没广播 not already byzantine blocked ≠ 已经被挡住 interchangeable：** 官方把没广播和已经被池子挡住拜占庭分开。
- **看见没进提案 not already settled ≠ 已经交差 interchangeable：** 官方把没进提案和已经交差分开；373 checktxopt vs block bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code ≠ 0 会被拒、不会广播也不会进提案 | 不是已经没进块（316） | 不是可选（806/373 item 1） |
| 看见拒了 | 不是已经被挡住拜占庭 | 不是 Usage Code≠0（489/686） |
| 看见没进提案 | 不是已经交差 | 不是 CheckTx codespace（381/785） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code≠0 拒收 not already not-in-block / not already byzantine blocked / not already settled 正式三事（373 余量），必须分开是不是已经没进块 interchangeable / 316、是不是已经被挡住拜占庭、是不是已经交差。可以跳过「看见拒了就已经没进块」。不要另写怎样写 CheckTx 可选。373 checktxopt vs block bundled unbundling 在本页 item 2 续；续 [`worked-example-checktxopt-notdata-vs-bundled.md`](worked-example-checktxopt-notdata-vs-bundled.md)（不变量 808 item 3）。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- CheckTx 可选 bundled。那是不变量 373。
- CheckTx 可选。那是不变量 373 item 1 余量 / 806。
- Finalize 的 Code 非零就已经没进块。那是不变量 316。
- Usage Code≠0 就已经拒广播。那是不变量 489 / 686。
