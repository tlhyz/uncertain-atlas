# 例：看见 proposer Prepare-first is not already skip-process interchangeable / not already same-round interchangeable / not already settled interchangeable

**层次**：实现 / proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量）/ not 1097 htmt-notskip interchangeable / not 417 htmatch-vs-header bundled interchangeable」，不是头字段对上余量 bundled（417），也不是 Process 也会在提议者那边叫就已经不用再 Process（351），也不是先验块头就已经跑过 Process（416）。不要另写怎样写头字段对上余量。

## 官方三件事

1. **看见自己是提议者会先走完 Prepare 那五步 / 看见走完了 这份栏 is not already 已经不用再 Process interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1097 htmt-notskip interchangeable / 1098 htmt-notverif interchangeable / 417 htmatch item 2 process-ht interchangeable，也不是已经 proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事 bundled（417 item 1 余量） interchangeable / 417 htmatch item 1 interchangeable。**  
   官方写：若 p 是提议者，p 先执行 Prepare 那五步。看见走完了，不是已经不用再 Process interchangeable——本页从 417 item 1 侧钉 not already skip-process 单句。417 htmatch vs header bundled unbundling 在本页 item 1 启动。

2. **看见自己是提议者 / 看见走完了 / 这份栏 is not already 已经保证是这一次 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1097 htmt-notskip interchangeable / 417 htmatch item 3 finalize-ht interchangeable / 1099 htmt-notdec interchangeable，也不是已经 Process 也会在提议者那边叫就已经不用再 Process interchangeable / 351 process-proposer interchangeable。**  
   官方把自己是提议者和已经保证是这一次分开。看见自己是提议者，不是已经保证是这一次 interchangeable。本页钉 not already same-round 单句。

3. **看见先走 Prepare / 看见走完了 / 这份栏 is not already 已经交差 interchangeable，也不是已经头字段对上余量 bundled（417） interchangeable / 1097 htmt-notskip interchangeable / 1098 htmt-notverif interchangeable，也不是已经先验块头就已经跑过 Process interchangeable / 416 proposetimeout interchangeable。**  
   官方把先走 Prepare 和已经交差分开。看见先走 Prepare，不是已经交差 interchangeable。417 htmatch vs header bundled unbundling 在本页 item 1 启动。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **proposer Prepare-first not already skip-process ≠ 已经不用再 Process interchangeable：** 官方把先走 Prepare 那五步和已经调过 Process 分开。
- **看见自己是提议者 not already same-round ≠ 已经保证是这一次 interchangeable：** 官方把自己是提议者和已经保证是这一次分开。
- **看见先走 Prepare not already settled ≠ 已经交差 interchangeable：** 官方把先走 Prepare 和已经交差分开；417 htmatch vs header bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 自己是提议者会先走完 Prepare 那五步 | 不是已经不用再 Process | 不是 Process 也会在提议者那边叫就已经不用再 Process（351） |
| 看见自己是提议者 | 不是已经保证是这一次 | 不是先验块头就已经跑过 Process（416） |
| 看见先走 Prepare | 不是已经交差 | 不是 Process height/time 对上就已经验过块头（1098） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量），必须分开是不是已经不用再 Process、是不是已经保证是这一次、是不是已经交差。可以跳过「看见填了头字段就已经不用再 Process」。不要另写怎样写头字段对上余量。417 htmatch vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-htmt-notverif-vs-bundled.md`](worked-example-htmt-notverif-vs-bundled.md)（不变量 1098 item 2）。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- 头字段对上余量 bundled。那是不变量 417。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
- 先验块头就已经跑过 Process。那是不变量 416。
