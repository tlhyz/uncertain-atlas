# 例：看见 OfferSnapshot 回包 result 是这次 Offer 的结果 is not already restored interchangeable / not already accepted interchangeable / not already settled interchangeable

**层次**：实现 / OfferSnapshot 回包 result not already restored / not already accepted / not already settled 正式三事（396 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot 回包 result not already restored / not already accepted / not already settled 正式三事（396 余量）/ not 738 offersnapreq-notrestored interchangeable / not 396 offersnap-vs-listed bundled interchangeable」，不是 OfferSnapshot 请求 bundled（396），也不是 Offer 收下就已经装完（321）或 Offer ACCEPT 开始装块（402 / 726）或 Offer 收下之后才去拉装（401 / 728）。不要另写怎样写 OfferSnapshot 请求。

## 官方三件事

1. **看见 OfferSnapshot 回包 `result` 是这次 Offer 的结果 / 看见回了 result / 这次 Offer 的结果 is not already 已经 Offer 收下就已经装完 interchangeable / 321 offerrestored interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 738 offersnapreq-notrestored interchangeable / 737 offersnapreq-notlisted interchangeable / 396 offersnap item 1 snapshot interchangeable，也不是已经 result not already restored / not already accepted / not already settled 正式三事 bundled（396 item 2 余量） interchangeable / 396 offersnap item 2 interchangeable。**  
   官方写：`result` 是这次 Offer 的结果。看见回了 result，不是已经 Offer 收下就已经装完 interchangeable——本页从 396 item 2 侧钉 not already restored 单句。396 offersnap vs listed bundled unbundling 在本页 item 2 续。

2. **看见回了 result / 看见有结果 / 这次 Offer 的结果 is not already 已经收下 interchangeable / 402 / 726 offerunk-notrestored interchangeable / 401 / 728 offerafter-notrestored interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 738 offersnapreq-notrestored interchangeable / 396 offersnap item 3 引导时叫 interchangeable / 739 offersnapreq-notrequired interchangeable。**  
   官方把这次 Offer 的结果和已经收下分开——396 bundled 第二件事常与 402 / 401 混成「看见回了 result 就已经收下 interchangeable」，本页钉 not already accepted 单句。

3. **看见回了 result / 看见能回 / 这次 Offer 的结果 is not already 已经交差 interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 738 offersnapreq-notrestored interchangeable / 737 offersnapreq-notlisted interchangeable。**  
   官方把能回 result 和已经交差分开。看见能回，不是已经交差 interchangeable。396 offersnap vs listed bundled unbundling 在本页 item 2 续。

怎样写 OfferSnapshot 请求、怎样填 snapshot、怎样填 result 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **result not already restored ≠ 321 interchangeable：** 官方把这次 Offer 的结果和 Offer 收下就已经装完分开。
- **result not already accepted ≠ 402 / 726 / 401 / 728 interchangeable：** 官方把这次 Offer 的结果和已经收下分开。
- **result not already settled ≠ 已经交差 interchangeable：** 官方把能回 result 和已经交差分开；396 offersnap vs listed bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| OfferSnapshot 回包 result 是这次 Offer 的结果 | 不是已经装完（321） | 不是 snapshot 本地清单（737/396 item 1） |
| 看见回了 result | 不是已经收下（402 / 726 / 401 / 728） | 不是 OfferSnapshot 请求 bundled（396） |
| 看见能回 | 不是已经交差 | 不是引导时叫（739/396 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot 回包 result not already restored / not already accepted / not already settled 正式三事（396 余量），必须分开 result 是不是已经装完 interchangeable / 321、是不是已经收下 interchangeable / 402 / 401、是不是已经交差。可以跳过「看见回了 result 就已经装完」。不要另写怎样写 OfferSnapshot 请求。396 offersnap vs listed bundled unbundling 在本页 item 2 续；完成 [`worked-example-offersnapreq-notrequired-vs-bundled.md`](worked-example-offersnapreq-notrequired-vs-bundled.md)（不变量 739 item 3）。

## 本页不抄

- 怎样写 OfferSnapshot 请求、怎样填 snapshot、怎样填 result。
- OfferSnapshot 请求 bundled。那是不变量 396。
- OfferSnapshot 请求 snapshot。那是不变量 396 item 1 余量 / 737。
- OfferSnapshot 在引导时叫。那是不变量 396 item 3 余量 / 739。
- Offer 收下就已经装完。那是不变量 321。
- OfferSnapshot Result ACCEPT。那是不变量 402 / 726。
- Offer 收下之后才去拉装。那是不变量 401 / 728。
