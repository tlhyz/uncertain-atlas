# 例：看见 Finalize app_hash empty-or-hardcoded-det is not already header-printed interchangeable / not already this-header interchangeable / not already settled interchangeable

**层次**：实现 / Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量）/ not 1100 fhash-notheader interchangeable / not 404 finapphash-vs-header bundled interchangeable」，不是 Finalize 回包余量 bundled（404），也不是本头 AppHash 就已经是本高度交差（147），也不是 app_hash 就已经写进下一块头（432）。不要另写怎样写 Finalize 回包余量。

## 官方三件事

1. **看见 Finalize 回包 app_hash 可以空或硬编码、但必须确定 / 看见回了 app_hash 这份栏 is not already 已经印进本头 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1100 fhash-notheader interchangeable / 1101 fhash-notalign interchangeable / 404 finapphash item 2 query-anchor interchangeable，也不是已经 Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事 bundled（404 item 1 余量） interchangeable / 404 finapphash item 1 interchangeable。**  
   官方写：FinalizeBlockResponse.app_hash 可以空，也可以硬编码，但必须确定——不得依赖这次请求和上一份已提交状态以外的东西。看见回了空根，不是已经印进本头 interchangeable——本页从 404 item 1 侧钉 not already header-printed 单句。404 finapphash vs header bundled unbundling 在本页 item 1 启动。

2. **看见硬编码 / 看见回了 app_hash / 这份栏 is not already 已经是本头 AppHash interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1100 fhash-notheader interchangeable / 404 finapphash item 3 code0 interchangeable / 1102 fhash-notout interchangeable，也不是已经本头 AppHash 就已经是本高度交差 interchangeable / 147 apphash interchangeable。**  
   官方把硬编码和已经是本头 AppHash 分开。看见硬编码，不是已经是本头 AppHash interchangeable。本页钉 not already this-header 单句。

3. **看见必须确定 / 看见回了 app_hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1100 fhash-notheader interchangeable / 1101 fhash-notalign interchangeable，也不是已经 app_hash 就已经写进下一块头 interchangeable / 432 finrespend interchangeable。**  
   官方把必须确定和已经交差分开。看见必须确定，不是已经交差 interchangeable。404 finapphash vs header bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 回包余量、怎样挑空根、怎样回证明是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize app_hash empty-or-hardcoded-det not already header-printed ≠ 已经印进本头 interchangeable：** 官方把可以空或硬编码和已经印进本头分开。
- **看见硬编码 not already this-header ≠ 已经是本头 AppHash interchangeable：** 官方把硬编码和已经是本头 AppHash 分开。
- **看见必须确定 not already settled ≠ 已经交差 interchangeable：** 官方把必须确定和已经交差分开；404 finapphash vs header bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 回包 app_hash 可以空或硬编码、但必须确定 | 不是已经印进本头 | 不是本头 AppHash 就已经是本高度交差（147） |
| 看见硬编码 | 不是已经是本头 AppHash | 不是 app_hash 就已经写进下一块头（432） |
| 看见必须确定 | 不是已经交差 | 不是 Query 锚就已经对上 AppHash（1101） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize app_hash empty-or-hardcoded-det not already header-printed / not already this-header / not already settled 正式三事（404 余量），必须分开是不是已经印进本头、是不是已经是本头 AppHash、是不是已经交差。可以跳过「看见回了 Finalize 回包余量就已经印进本头」。不要另写怎样写 Finalize 回包余量。404 finapphash vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-fhash-notalign-vs-bundled.md`](worked-example-fhash-notalign-vs-bundled.md)（不变量 1101 item 2）。

## 本页不抄

- 怎样写 Finalize 回包余量、怎样挑空根、怎样回证明。
- Finalize 回包余量 bundled。那是不变量 404。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- app_hash 就已经写进下一块头。那是不变量 432。
