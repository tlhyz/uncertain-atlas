# 例：看见 CheckTx 请求 tx 是请求交易字节 is not already Recheck interchangeable / not already four gates interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx 请求 tx not already Recheck / not already four gates / not already settled 正式三事（391 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 请求 tx not already Recheck / not already four gates / not already settled 正式三事（391 余量）/ not 752 checktxtx-notrecheck interchangeable / not 391 checktxtx-vs-recheck bundled interchangeable」，不是 CheckTx 请求余栏 bundled（391），也不是 CheckTx Request type New vs Recheck（484/707），也不是 RECHECK 就已经是一笔新交易（312）。不要另写怎样写 CheckTx 请求余栏。

## 官方三件事

1. **看见 CheckTx 请求 `tx` 是请求交易字节 / 看见填了 tx / CheckTx 这份请求字节 is not already 已经是 `CheckTx_Recheck` 那种再验 interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 752 checktxtx-notrecheck interchangeable / 753 checktxtx-notexecstate interchangeable / 391 checktxtx item 2 validate interchangeable，也不是已经 tx not already Recheck / not already four gates / not already settled 正式三事 bundled（391 item 1 余量） interchangeable / 391 checktxtx item 1 interchangeable。**  
   官方写：`tx` 是请求交易字节。看见填了 tx，不是已经是 Recheck 那种再验 interchangeable——本页从 391 item 1 侧钉 not already Recheck 单句。391 checktxtx vs recheck bundled unbundling 在本页 item 1 启动。

2. **看见填了 tx / 看见有字节 / CheckTx 这份请求字节 is not already 已经是 CheckTx 技术上可选那种四门齐了 interchangeable / 373 fourgates interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 752 checktxtx-notrecheck interchangeable / 391 checktxtx item 3 info interchangeable / 754 checktxtx-notqueryinfo interchangeable，也不是已经 CheckTx Request type New vs Recheck interchangeable / 484 chktxtype / 707 chktxtype-notrecheck interchangeable。**  
   官方把请求交易字节和四门已经结算分开——391 bundled 第一件事常与 373 / 484 混成「看见填了 tx 就已经是 Recheck type 或四门齐了 interchangeable」，本页钉 not already four gates 单句。

3. **看见填了 tx / 看见能填 / CheckTx 这份请求字节 is not already 已经交差 interchangeable，也不是已经 CheckTx 请求余栏 bundled（391） interchangeable / 752 checktxtx-notrecheck interchangeable / 753 checktxtx-notexecstate interchangeable。**  
   官方把能填 CheckTx 请求 tx 和已经交差分开。看见能填，不是已经交差 interchangeable。391 checktxtx vs recheck bundled unbundling 在本页 item 1 启动。

怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **tx not already Recheck ≠ Recheck interchangeable：** 官方把请求交易字节和再验类型分开。
- **tx not already four gates ≠ 373 interchangeable：** 官方把有字节和 CheckTx 技术上可选就已经四门齐了分开。
- **tx not already settled ≠ 已经交差 interchangeable：** 官方把能填 tx 和已经交差分开；391 checktxtx vs recheck bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 请求 tx 是请求交易字节 | 不是已经是 Recheck | 不是 validate-no-apply（753/391 item 2） |
| 看见填了 tx | 不是已经四门齐了（373） | 不是 CheckTx 请求余栏 bundled（391） |
| 看见能填 | 不是已经交差 | 不是 CheckTx Request type（484/707） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 请求 tx not already Recheck / not already four gates / not already settled 正式三事（391 余量），必须分开 tx 是不是已经是 Recheck、是不是已经四门齐了 interchangeable / 373、是不是已经交差。可以跳过「看见填了 tx 就已经是 Recheck」。不要另写怎样写 CheckTx 请求余栏。391 checktxtx vs recheck bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktxtx-notexecstate-vs-bundled.md`](worked-example-checktxtx-notexecstate-vs-bundled.md)（不变量 753 item 2）。

## 本页不抄

- 怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息。
- CheckTx 请求余栏 bundled。那是不变量 391。
- CheckTx 对照当前状态验、不应用改动。那是不变量 391 item 2 余量 / 753。
- CheckTx 回包 info。那是不变量 391 item 3 余量 / 754。
- CheckTx Request type New vs Recheck。那是不变量 484 / 707。
- CheckTx 技术上可选、不参与处理块就已经是四门已经结算。那是不变量 373。
