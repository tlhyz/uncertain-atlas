# 例：看见 Process height/time match is not already header-verified interchangeable / not already processed interchangeable / not already settled interchangeable

**层次**：实现 / Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量）/ not 1098 htmt-notverif interchangeable / not 417 htmatch-vs-header bundled interchangeable」，不是头字段对上余量 bundled（417），也不是收到带上头的提案会先验块头就已经跑过 Process（416），也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359）。不要另写怎样写头字段对上余量。

## 官方三件事

1. **看见 Process 的 height / time 对上拟议块头 / 看见对上了 这份栏 is not already 已经验过块头 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1098 htmt-notverif interchangeable / 1097 htmt-notskip interchangeable / 417 htmatch item 1 prepare-first interchangeable，也不是已经 Process height/time match not already header-verified / not already processed / not already settled 正式三事 bundled（417 item 2 余量） interchangeable / 417 htmatch item 2 interchangeable。**  
   官方写：Process 的 height 和 time 对上拟议块的头。看见对上了，不是已经验过块头 interchangeable——本页从 417 item 2 侧钉 not already header-verified 单句。417 htmatch vs header bundled unbundling 在本页 item 2 续。

2. **看见字段对上 / 看见对上了 / 这份栏 is not already 已经跑过 Process interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1098 htmt-notverif interchangeable / 417 htmatch item 3 finalize-ht interchangeable / 1099 htmt-notdec interchangeable，也不是已经收到带上头的提案会先验块头就已经跑过 Process interchangeable / 416 proposetimeout interchangeable。**  
   官方把字段对上和已经跑过 Process 分开。看见字段对上，不是已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见能对 / 看见对上了 / 这份栏 is not already 已经交差 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1098 htmt-notverif interchangeable / 1097 htmt-notskip interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process interchangeable / 359 prepare-fields interchangeable。**  
   官方把能对和已经交差分开。看见能对，不是已经交差 interchangeable。417 htmatch vs header bundled unbundling 在本页 item 2 续。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process height/time match not already header-verified ≠ 已经验过块头 interchangeable：** 官方把 Usage 里这份对上和 When 里先验块头分开。
- **看见字段对上 not already processed ≠ 已经跑过 Process interchangeable：** 官方把字段对上和已经跑过 Process 分开。
- **看见能对 not already settled ≠ 已经交差 interchangeable：** 官方把能对和已经交差分开；417 htmatch vs header bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 的 height / time 对上拟议块头 | 不是已经验过块头 | 不是收到带上头的提案会先验块头就已经跑过 Process（416） |
| 看见字段对上 | 不是已经跑过 Process | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 看见能对 | 不是已经交差 | 不是 Finalize height/time 对上就已经是刚决定那块的字段（1099） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量），必须分开是不是已经验过块头、是不是已经跑过 Process、是不是已经交差。可以跳过「看见填了头字段就已经不用再 Process」。不要另写怎样写头字段对上余量。417 htmatch vs header bundled unbundling 在本页 item 2 续；续 [`worked-example-htmt-notdec-vs-bundled.md`](worked-example-htmt-notdec-vs-bundled.md)（不变量 1099 item 3）。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- 头字段对上余量 bundled。那是不变量 417。
- 收到带上头的提案会先验块头就已经跑过 Process。那是不变量 416。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
