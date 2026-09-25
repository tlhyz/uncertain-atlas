# 例：看见拒了 / 看见没广播 / 看见没进提案 is not already already excluded interchangeable / already blocked interchangeable / already settled interchangeable

**层次**：实现 / Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量）/ not 867 checktxopt-notexcluded interchangeable / not 373 checktxopt bundled interchangeable」，不是 checktxopt bundled（373），也不是 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算（866 item 1 余量）或引擎对回包码不再赋予别的含义不是已经被引擎用了 Data（373 item 3 余量）。不要另写怎样写 CheckTx 可选。

## 官方三件事

规范把 Methods 里 `Code ≠ 0` 会被拒、不会广播也不会进提案 和「已经是拒了就已经没进块 interchangeable / 已经是没广播就已经挡住拜占庭 interchangeable / 已经是没进提案就已经交差 interchangeable / 已经是 checktxopt bundled interchangeable」分开写成三件独立的实现事，不是「看见拒了就已经没进块 interchangeable / 就已经挡住拜占庭 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见拒了 / 看见 `Code ≠ 0` 会被拒、不会广播也不会进提案 / 看见拒了交易 is not already 已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable / 373 checktxopt bundled interchangeable / 316 Finalize Code interchangeable / checktxopt-sold-as-block interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 867 checktxopt-notexcluded interchangeable / 373 checktxopt item 2 interchangeable，也不是已经 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事 bundled（373 item 2 余量） interchangeable / 373 checktxopt item 2 interchangeable，也不是已经能回就已经是四门（866） interchangeable / 33 four gates interchangeable / 339 CheckTx weak interchangeable，也不是已经 Finalize 的 Code 非零就已经没进块（316） interchangeable。**  
   官方写：`CheckTxResponse.Code ≠ 0` 的交易会被拒，不会广播给别的节点，也不会装进提案。看见拒了，不是已经是 Finalize 那种 Code 非零仍在块里。看见拒了，不是已经 excluded interchangeable——373 钉 bundled 三事，本页从 item 2 侧钉 not already excluded 单句。看见 `Code ≠ 0` 会被拒、不会广播也不会进提案，不是已经 checktxopt bundled（373） interchangeable——373 钉 bundled，本页钉 item 2 第一件事。看见拒了，不是已经能回就已经是四门（866） interchangeable——866 另钉 item 1。373 checktxopt-vs-block bundled unbundling 在本页 item 2 续。

2. **看见没广播 / 看见不会广播 / 看见没广播给别的节点 is not already 已经被池子挡住拜占庭 interchangeable / 已经 blocked interchangeable / 已经挡住拜占庭交差 interchangeable / 373 checktxopt bundled interchangeable / 339 CheckTx weak interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 867 checktxopt-notexcluded interchangeable / 373 checktxopt item 1 能回 interchangeable / 373 checktxopt item 3 有码 interchangeable，也不是已经 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事 bundled（373 item 2 余量） interchangeable / 373 checktxopt item 2 interchangeable，也不是已经没进块（本页第一件事） interchangeable。**  
   官方写：看见没广播，不是拜占庭已经被挡住。看见不会广播，不是已经 blocked interchangeable——本页钉 not already blocked 单句。看见没广播给别的节点，不是已经没进块（本页第一件事） interchangeable——三件事分开钉。373 checktxopt-vs-block bundled unbundling 在本页 item 2 续。

3. **看见没进提案 / 看见不会装进提案 / 看见没进提案 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 373 checktxopt bundled interchangeable / 33 four gates interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 867 checktxopt-notexcluded interchangeable / 373 checktxopt item 1 / 373 checktxopt item 3，也不是已经 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事 bundled（373 item 2 余量） interchangeable / 373 checktxopt item 2 interchangeable，也不是已经没进块（本页第一件事） interchangeable / 已经挡住拜占庭（本页第二件事） interchangeable。**  
   官方写：看见没进提案，不是已经交差。看见不会装进提案，不是已经 settled interchangeable——本页钉 not already settled 单句。看见没进提案，不是已经挡住拜占庭（本页第二件事） interchangeable——三件事分开钉。373 checktxopt-vs-block bundled unbundling 在本页 item 2 续。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。checktxopt bundled（373）、CheckTx 技术上可选、不参与处理块不是已经是四门已经结算（373 item 1 余量 / 866）、引擎对回包码不再赋予别的含义不是已经被引擎用了 Data（373 item 3 余量）、四门已经结算（33）、Finalize 的 Code 非零就已经没进块（316）、CheckTx 的 Data 就已经被引擎用了（317）、CheckTx 弱过滤器就已经验完（339）是另外那套，本页不抄。

## 官方为什么这样拆

- **拒了 not already excluded ≠ 373 / 316 interchangeable：** 官方把内存池拒收和 Finalize 那种 Code 非零仍在块里分开。
- **没广播 not already blocked ≠ 已经挡住拜占庭 interchangeable：** 官方把没广播和拜占庭已经被挡住分开。
- **没进提案 not already settled ≠ 已经交差 interchangeable：** 官方把没进提案和已经交差分开；373 checktxopt-vs-block bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拒了 | 不是 already excluded | 不是 Finalize 的 Code 非零就已经没进块 alone（316） |
| 没广播 | 不是 already blocked | 不是能回 already fourgates alone（866） |
| 没进提案 | 不是 already settled | 不是四门已经结算 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量），必须分开拒了 是不是 already excluded interchangeable / 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable、没广播 是不是 already blocked interchangeable、没进提案 是不是 already settled interchangeable。可以跳过「看见拒了就已经没进块 interchangeable / 就已经挡住拜占庭 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 CheckTx 可选。373 checktxopt-vs-block bundled unbundling 在本页 item 2 续（866 + 867）。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- checktxopt bundled。那是不变量 373。
- CheckTx 技术上可选、不参与处理块不是已经是四门已经结算。那是不变量 373 item 1 余量 / 866。
- 引擎对回包码不再赋予别的含义不是已经被引擎用了 Data。那是不变量 373 item 3 余量。
- 四门已经结算。那是不变量 33。
- Finalize 的 Code 非零就已经没进块。那是不变量 316。
- CheckTx 的 Data 就已经被引擎用了。那是不变量 317。
- CheckTx 弱过滤器就已经验完。那是不变量 339。
