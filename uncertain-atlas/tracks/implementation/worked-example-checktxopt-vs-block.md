# 例：看见 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算；看见 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块；看见引擎对回包码不再赋予别的含义不是已经被引擎用了 Data

**层次**：实现 / CheckTx 可选。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 / Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 / 引擎对回包码不再赋予别的含义不是已经被引擎用了 Data」，不是 CheckTx 的 Data 就已经被引擎用了，也不是 Finalize 的 Code 非零就已经没进块。不要另写怎样写 CheckTx 可选。

## 官方三件事

规范把 CheckTx 技术上可选、不参与处理块、`Code ≠ 0` 会被拒、不会广播也不会进提案、引擎对回包码不再赋予别的含义写成三件独立的实现事，不是「看见能回 CheckTx 就已经是四门已经结算、已经没进块、已经被引擎用了 Data」一件事：

1. **看见 CheckTx 技术上可选、不参与处理块 / 看见能回 不是已经是四门已经结算，也不是已经交差。**  
   官方写：CheckTx 技术上可选，不参与处理块。看见能回，不是已经是 CheckTx / Prepare / Process / Finalize 四门齐了。看见可选，不是已经交差。看见没参与处理块，不是已经从池里删掉。
2. **看见 `Code ≠ 0` 会被拒、不会广播也不会进提案 / 看见拒了 不是已经没进块，也不是已经被池子挡住拜占庭。**  
   官方写：`CheckTxResponse.Code ≠ 0` 的交易会被拒，不会广播给别的节点，也不会装进提案。看见拒了，不是已经是 Finalize 那种 Code 非零仍在块里。看见没广播，不是拜占庭已经被挡住。看见没进提案，不是已经交差。
3. **看见引擎对回包码不再赋予别的含义 / 看见有码 不是已经被引擎用了 Data，也不是已经是共识顺序。**  
   官方写：CometBFT 对这个回包码不再赋予别的含义。看见有码，不是已经被引擎用了 `CheckTxResponse.Data`。看见码在，不是已经是共识顺序。看见拒了，不是已经分叉。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **CheckTx 技术上可选、不参与处理块 ≠ 已经是四门已经结算：** 官方把可选的 CheckTx 和四门结算分开。
- **Code ≠ 0 会被拒、不会广播也不会进提案 ≠ 已经没进块：** 官方把内存池拒收和 Finalize 那种 Code 非零仍在块里分开。
- **引擎对回包码不再赋予别的含义 ≠ 已经被引擎用了 Data：** 官方把回包码不再另有含义和 Data / Priority 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 技术上可选、不参与处理块 | 不是已经是四门已经结算 | 不是 CheckTx 弱过滤器就已经验完（339） |
| Code ≠ 0 会被拒、不会广播也不会进提案 | 不是已经没进块 | 不是 Finalize 的 Code 非零就已经没进块（316） |
| 引擎对回包码不再赋予别的含义 | 不是已经被引擎用了 Data | 不是 CheckTx 的 Data 就已经被引擎用了（317） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能回 CheckTx 就已经是四门已经结算、已经没进块、已经被引擎用了 Data」，必须分开 CheckTx 技术上可选、不参与处理块是不是已经是四门已经结算、Code ≠ 0 会被拒、不会广播也不会进提案是不是已经没进块、引擎对回包码不再赋予别的含义是不是已经被引擎用了 Data。可以跳过「看见能回 CheckTx 就已经是四门已经结算」。不要另写怎样写 CheckTx 可选。373 checktxopt vs block bundled unbundling 完成（806 item 1 / 807 item 2 / 808 item 3）；精读 [`worked-example-checktxopt-notsettled-vs-bundled.md`](worked-example-checktxopt-notsettled-vs-bundled.md)（不变量 806 item 1）。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- 四门已经结算。那是不变量 33。
- Finalize 的 Code 非零就已经没进块。那是不变量 316。
- CheckTx 的 Data 就已经被引擎用了。那是不变量 317。
