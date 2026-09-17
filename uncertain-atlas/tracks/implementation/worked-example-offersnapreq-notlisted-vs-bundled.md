# 例：看见 OfferSnapshot 请求 snapshot 是拿来装回的那份快照 is not already local list interchangeable / not already identical interchangeable / not already settled interchangeable

**层次**：实现 / OfferSnapshot 请求 snapshot not local list / not already identical / not already settled 正式三事（396 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot 请求 snapshot not local list / not already identical / not already settled 正式三事（396 余量）/ not 737 offersnapreq-notlisted interchangeable / not 396 offersnap-vs-listed bundled interchangeable」，不是 OfferSnapshot 请求 bundled（396），也不是 ListSnapshots 本地清单就已经是同一份（395 / 735）或全字段对上就已经是同一份（368）。不要另写怎样写 OfferSnapshot 请求。

## 官方三件事

1. **看见 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照 / 看见填了 snapshot / 拿来装回的那份 is not already 已经是 ListSnapshots 回的那份本地清单 interchangeable / 395 / 735 listsnapempty-notidentical interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 737 offersnapreq-notlisted interchangeable / 738 offersnapreq-notrestored interchangeable / 396 offersnap item 2 result interchangeable，也不是已经 snapshot not local list / not already identical / not already settled 正式三事 bundled（396 item 1 余量） interchangeable / 396 offersnap item 1 interchangeable。**  
   官方写：`snapshot` 是拿来装回的那份快照。看见填了 snapshot，不是已经是 ListSnapshots 回的那份本地清单 interchangeable——本页从 396 item 1 侧钉 not local list 单句。396 offersnap vs listed bundled unbundling 在本页 item 1 启动。

2. **看见填了 snapshot / 看见有这份 / 拿来装回的那份 is not already 已经五个字段都对上、已经是同一份 interchangeable / 368 snapidentical interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 737 offersnapreq-notlisted interchangeable / 396 offersnap item 3 引导时叫 interchangeable / 739 offersnapreq-notrequired interchangeable。**  
   官方把拿来装回的那份和已经是同一份分开——396 bundled 第一件事常与 368 混成「看见填了 snapshot 就已经是同一份 interchangeable」，本页钉 not already identical 单句。

3. **看见填了 snapshot / 看见能填 / 拿来装回的那份 is not already 已经交差 interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 737 offersnapreq-notlisted interchangeable / 738 offersnapreq-notrestored interchangeable。**  
   官方把能填 snapshot 和已经交差分开。看见能填，不是已经交差 interchangeable。396 offersnap vs listed bundled unbundling 在本页 item 1 启动。

怎样写 OfferSnapshot 请求、怎样填 snapshot、怎样填 result 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **snapshot not local list ≠ 395 / 735 interchangeable：** 官方把拿来装回的那份和本地清单分开。
- **snapshot not already identical ≠ 368 interchangeable：** 官方把拿来装回的那份和全字段对上就已经是同一份分开。
- **snapshot not already settled ≠ 已经交差 interchangeable：** 官方把能填 snapshot 和已经交差分开；396 offersnap vs listed bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| OfferSnapshot 请求 snapshot 是拿来装回的那份快照 | 不是已经是本地清单（395 / 735） | 不是回包 result（738/396 item 2） |
| 看见填了 snapshot | 不是已经是同一份（368） | 不是 OfferSnapshot 请求 bundled（396） |
| 看见能填 | 不是已经交差 | 不是引导时叫（739/396 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot 请求 snapshot not local list / not already identical / not already settled 正式三事（396 余量），必须分开 snapshot 是不是已经是本地清单 interchangeable / 395 / 735、是不是已经是同一份 interchangeable / 368、是不是已经交差。可以跳过「看见填了 snapshot 就已经是本地清单」。不要另写怎样写 OfferSnapshot 请求。396 offersnap vs listed bundled unbundling 在本页 item 1 启动；续 [`worked-example-offersnapreq-notrestored-vs-bundled.md`](worked-example-offersnapreq-notrestored-vs-bundled.md)（不变量 738 item 2）。

## 本页不抄

- 怎样写 OfferSnapshot 请求、怎样填 snapshot、怎样填 result。
- OfferSnapshot 请求 bundled。那是不变量 396。
- OfferSnapshot 回包 result 是这次 Offer 的结果。那是不变量 396 item 2 余量 / 738。
- OfferSnapshot 在引导时叫。那是不变量 396 item 3 余量 / 739。
- ListSnapshots 本地清单就已经是同一份。那是不变量 395 / 735。
- 全字段对上就已经是同一份。那是不变量 368。
