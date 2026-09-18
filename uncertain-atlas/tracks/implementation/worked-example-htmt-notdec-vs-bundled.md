# 例：看见 Finalize height/time match is not already decided-fields interchangeable / not already header-known interchangeable / not already settled interchangeable

**层次**：实现 / Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事（417 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事（417 余量）/ not 1099 htmt-notdec interchangeable / not 417 htmatch-vs-header bundled interchangeable」，不是头字段对上余量 bundled（417），也不是 Finalize 含刚决定那块的字段就已经是四门已经结算（407），也不是 Finalize 请求 hash 就已经知道本头哈希。不要另写怎样写头字段对上余量。

## 官方三件事

1. **看见 Finalize 的 height / time 对上拟议块头 / 看见对上了 这份栏 is not already 已经是刚决定那块的字段 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1099 htmt-notdec interchangeable / 1097 htmt-notskip interchangeable / 417 htmatch item 1 prepare-first interchangeable，也不是已经 Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事 bundled（417 item 3 余量） interchangeable / 417 htmatch item 3 interchangeable。**  
   官方写：Finalize 的 height 和 time 对上拟议块的头。看见对上了，不是已经是刚决定那块的字段 interchangeable——本页从 417 item 3 侧钉 not already decided-fields 单句。417 htmatch vs header bundled unbundling 在本页 item 3 完成。

2. **看见字段对上 / 看见对上了 / 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1099 htmt-notdec interchangeable / 417 htmatch item 2 process-ht interchangeable / 1098 htmt-notverif interchangeable，也不是已经 Finalize 含刚决定那块的字段就已经是四门已经结算 interchangeable / 407 finfields interchangeable。**  
   官方把字段对上和已经知道本头哈希分开。看见字段对上，不是已经知道本头哈希 interchangeable。本页钉 not already header-known 单句。

3. **看见能对 / 看见对上了 / 这份栏 is not already 已经交差 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1099 htmt-notdec interchangeable / 1097 htmt-notskip interchangeable，也不是已经先验块头就已经跑过 Process interchangeable / 416 proposetimeout interchangeable。**  
   官方把能对和已经交差分开。看见能对，不是已经交差 interchangeable。417 htmatch vs header bundled unbundling 在本页 item 3 完成。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize height/time match not already decided-fields ≠ 已经是刚决定那块的字段 interchangeable：** 官方把 Finalize 这份对上和已经含刚决定那块的字段分开。
- **看见字段对上 not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把字段对上和已经知道本头哈希分开。
- **看见能对 not already settled ≠ 已经交差 interchangeable：** 官方把能对和已经交差分开；417 htmatch vs header bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 的 height / time 对上拟议块头 | 不是已经是刚决定那块的字段 | 不是 Finalize 含刚决定那块的字段就已经是四门已经结算（407） |
| 看见字段对上 | 不是已经知道本头哈希 | 不是先验块头就已经跑过 Process（416） |
| 看见能对 | 不是已经交差 | 不是提议者先走 Prepare 就已经不用再 Process（1097） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事（417 余量），必须分开是不是已经是刚决定那块的字段、是不是已经知道本头哈希、是不是已经交差。可以跳过「看见填了头字段就已经不用再 Process」。不要另写怎样写头字段对上余量。417 htmatch vs header bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- 头字段对上余量 bundled。那是不变量 417。
- Finalize 含刚决定那块的字段就已经是四门已经结算。那是不变量 407。
- 先验块头就已经跑过 Process。那是不变量 416。
