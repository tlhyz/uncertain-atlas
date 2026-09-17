# 例：看见 CheckTx 技术上可选、不参与处理块 is not already four gates settled interchangeable / not already settled interchangeable / not already deleted from pool interchangeable

**层次**：实现 / CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事（373 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事（373 余量）/ not 806 checktxopt-notsettled interchangeable / not 373 checktxopt-vs-block bundled interchangeable」，不是 CheckTx 可选 bundled（373），也不是四门已经结算（33），也不是 CheckTx 弱过滤器就已经验完（339），也不是 Usage validate-no-apply 就已经可选（486/682）。不要另写怎样写 CheckTx 可选。

## 官方三件事

1. **看见 CheckTx 技术上可选、不参与处理块 / 看见能回 / 这份可选 is not already 已经是四门已经结算 interchangeable / 33 fourgates interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 806 checktxopt-notsettled interchangeable / 807 checktxopt-notinblock interchangeable / 373 checktxopt item 2 Code≠0 interchangeable，也不是已经 CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事 bundled（373 item 1 余量） interchangeable / 373 checktxopt item 1 interchangeable。**  
   官方写：CheckTx 技术上可选，不参与处理块。看见能回，不是已经是 CheckTx / Prepare / Process / Finalize 四门齐了 interchangeable——本页从 373 item 1 侧钉 not already four gates settled 单句。373 checktxopt vs block bundled unbundling 在本页 item 1 启动。

2. **看见能回 / 看见可选 / 这份可选 is not already 已经交差 interchangeable / 33 fourgates interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 806 checktxopt-notsettled interchangeable / 373 checktxopt item 3 回包码 interchangeable / 808 checktxopt-notdata interchangeable，也不是已经 CheckTx 弱过滤器就已经验完 interchangeable / 339 checktxweak interchangeable，也不是已经 Usage validate-no-apply 就已经可选 interchangeable / 486 chktxvalidate / 682 chktxvalidate-notoptional interchangeable。**  
   官方把可选和已经交差分开——373 bundled 第一件事常与 33 / 339 / 486 混成「看见能回就已经是四门已经结算或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见能回 / 看见没参与处理块 / 这份可选 is not already 已经从池里删掉 interchangeable，也不是已经 CheckTx 可选 bundled（373） interchangeable / 806 checktxopt-notsettled interchangeable / 807 checktxopt-notinblock interchangeable。**  
   官方把没参与处理块和已经从池里删掉分开。看见没参与处理块，不是已经从池里删掉 interchangeable。373 checktxopt vs block bundled unbundling 在本页 item 1 启动。

怎样写 CheckTx、怎样挑回包码、怎样广播是规范里的做法，本页不抄。

## 官方为什么这样拆

- **CheckTx 可选 not already four gates settled ≠ 33 interchangeable：** 官方把可选的 CheckTx 和四门结算分开。
- **看见可选 not already settled ≠ 已经交差 interchangeable：** 官方把可选和已经交差分开。
- **看见没参与处理块 not already deleted from pool ≠ 已经从池里删掉 interchangeable：** 官方把没参与处理块和已经从池里删掉分开；373 checktxopt vs block bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 技术上可选、不参与处理块 | 不是已经是四门已经结算（33） | 不是 Code≠0 拒收（807/373 item 2） |
| 看见能回 | 不是已经交差 | 不是弱过滤器就已经验完（339） |
| 看见没参与处理块 | 不是已经从池里删掉 | 不是 Usage validate-no-apply（486/682） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事（373 余量），必须分开是不是已经是四门已经结算 interchangeable / 33、是不是已经交差、是不是已经从池里删掉。可以跳过「看见能回就已经是四门已经结算」。不要另写怎样写 CheckTx 可选。373 checktxopt vs block bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktxopt-notinblock-vs-bundled.md`](worked-example-checktxopt-notinblock-vs-bundled.md)（不变量 807 item 2）。

## 本页不抄

- 怎样写 CheckTx、怎样挑回包码、怎样广播。
- CheckTx 可选 bundled。那是不变量 373。
- Code ≠ 0 拒收。那是不变量 373 item 2 余量 / 807。
- 四门已经结算。那是不变量 33。
- Usage validate-no-apply 就已经可选。那是不变量 486 / 682。
