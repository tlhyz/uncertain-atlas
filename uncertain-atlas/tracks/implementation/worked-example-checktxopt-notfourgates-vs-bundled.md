# 例：看见能回 / 看见可选 / 看见没参与处理块 is not already already fourgates interchangeable / already settled interchangeable / already removed interchangeable

**层次**：实现 / CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量）/ not 866 checktxopt-notfourgates interchangeable / not 373 checktxopt bundled interchangeable」，不是 checktxopt bundled（373），也不是 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块（373 item 2 余量）或引擎对回包码不再赋予别的含义不是已经被引擎用了 Data（373 item 3 余量）。不要另写怎样写 CheckTx 可选。

## 官方三件事

规范把 Methods 里 CheckTx 技术上可选、不参与处理块 和「已经是能回就已经是四门已经结算 interchangeable / 已经是可选就已经交差 interchangeable / 已经是没参与处理块就已经从池里删掉 interchangeable / 已经是 checktxopt bundled interchangeable」分开写成三件独立的实现事，不是「看见能回就已经是四门已经结算 interchangeable / 就已经交差 interchangeable / 就已经从池里删掉 interchangeable」一件事：

1. **看见能回 / 看见 CheckTx 技术上可选、不参与处理块 / 看见能回 CheckTx is not already 已经是四门已经结算 interchangeable / 已经 fourgates interchangeable / 已经是四门已经结算交差 interchangeable / 373 checktxopt bundled interchangeable / 33 four gates interchangeable / checktxopt-sold-as-block interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 866 checktxopt-notfourgates interchangeable / 373 checktxopt item 1 interchangeable，也不是已经 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事 bundled（373 item 1 余量） interchangeable / 373 checktxopt item 1 interchangeable，也不是已经 Code ≠ 0 就已经没进块（373 item 2） interchangeable / 316 Finalize Code interchangeable / 317 CheckTx Data interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CheckTx 技术上可选，不参与处理块。看见能回，不是已经是 CheckTx / Prepare / Process / Finalize 四门齐了。看见能回，不是已经 fourgates interchangeable——373 钉 bundled 三事，本页从 item 1 侧钉 not already fourgates 单句。看见 CheckTx 技术上可选、不参与处理块，不是已经 checktxopt bundled（373） interchangeable——373 钉 bundled，本页钉 item 1 第一件事。看见能回，不是已经四门已经结算（33） interchangeable——33 另钉。373 checktxopt-vs-block bundled unbundling 在本页 item 1 启动。

2. **看见可选 / 看见技术上可选 / 看见 CheckTx 可选 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 373 checktxopt bundled interchangeable / 33 four gates interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 866 checktxopt-notfourgates interchangeable / 373 checktxopt item 2 拒了 interchangeable / 373 checktxopt item 3 有码 interchangeable，也不是已经 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事 bundled（373 item 1 余量） interchangeable / 373 checktxopt item 1 interchangeable，也不是已经是四门已经结算（本页第一件事） interchangeable。**  
   官方写：看见可选，不是已经交差。看见技术上可选，不是已经 settled interchangeable——本页钉 not already settled 单句。看见 CheckTx 可选，不是已经是四门已经结算（本页第一件事） interchangeable——三件事分开钉。373 checktxopt-vs-block bundled unbundling 在本页 item 1 启动。

3. **看见没参与处理块 / 看见不参与处理块 / 看见没处理块 is not already 已经从池里删掉 interchangeable / 已经 removed interchangeable / 已经从池里删掉交差 interchangeable / 373 checktxopt bundled interchangeable / 301 proposed-removed interchangeable，也不是已经 checktxopt bundled（373） interchangeable / 866 checktxopt-notfourgates interchangeable / 373 checktxopt item 2 / 373 checktxopt item 3，也不是已经 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事 bundled（373 item 1 余量） interchangeable / 373 checktxopt item 1 interchangeable，也不是已经是四门已经结算（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见没参与处理块，不是已经从池里删掉。看见不参与处理块，不是已经 removed interchangeable——本页钉 not already removed 单句。看见没处理块，不是已经交差（本页第二件事） interchangeable——三件事分开钉。373 checktxopt-vs-block bundled unbundling 在本页 item 1 启动。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。checktxopt bundled（373）、Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块（373 item 2 余量）、引擎对回包码不再赋予别的含义不是已经被引擎用了 Data（373 item 3 余量）、四门已经结算（33）、Finalize 的 Code 非零就已经没进块（316）、CheckTx 的 Data 就已经被引擎用了（317）、提案收了就已经从池里删掉（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **能回 not already fourgates ≠ 373 / 33 interchangeable：** 官方把可选的 CheckTx 和四门结算分开。
- **可选 not already settled ≠ 已经交差 interchangeable：** 官方把可选和已经交差分开。
- **没参与处理块 not already removed ≠ 已经从池里删掉 interchangeable：** 官方把不参与处理块和已经从池里删掉分开；373 checktxopt-vs-block bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能回 | 不是 already fourgates | 不是四门已经结算 alone（33） |
| 可选 | 不是 already settled | 不是 Finalize Code 非零就已经没进块 alone（316） |
| 没参与处理块 | 不是 already removed | 不是提案收了就已经从池里删掉 alone（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量），必须分开能回 是不是 already fourgates interchangeable / 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable、可选 是不是 already settled interchangeable、没参与处理块 是不是 already removed interchangeable。可以跳过「看见能回就已经是四门已经结算 interchangeable / 就已经交差 interchangeable / 就已经从池里删掉 interchangeable」。不要另写怎样写 CheckTx 可选。373 checktxopt-vs-block bundled unbundling 在本页 item 1 启动（866）。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- checktxopt bundled。那是不变量 373。
- Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块。那是不变量 373 item 2 余量。
- 引擎对回包码不再赋予别的含义不是已经被引擎用了 Data。那是不变量 373 item 3 余量。
- 四门已经结算。那是不变量 33。
- Finalize 的 Code 非零就已经没进块。那是不变量 316。
- CheckTx 的 Data 就已经被引擎用了。那是不变量 317。
- 提案收了就已经从池里删掉。那是不变量 301。
