# 例：看见自己是提议者会先走完 Prepare 那五步不是已经不用再 Process；看见 Process 的 height / time 对上拟议块头不是已经验过块头；看见 Finalize 的 height / time 对上拟议块头不是已经是刚决定那块的字段

**层次**：实现 / 头字段对上余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「自己是提议者会先走完 Prepare 那五步不是已经不用再 Process / Process 的 height / time 对上拟议块头不是已经验过块头 / Finalize 的 height / time 对上拟议块头不是已经是刚决定那块的字段」，不是 Process 也会在提议者那边叫就已经不用再 Process，也不是收到带上头的提案会先验块头就已经跑过 Process。不要另写怎样写头字段对上余量。

## 官方三件事

规范把自己是提议者会先走完 Prepare 那五步、Process 的 `height` / `time` 对上拟议块头、Finalize 的 `height` / `time` 对上拟议块头写成三件独立的实现事，不是「看见填了头字段就已经不用再 Process、已经验过块头、已经是刚决定那块的字段」一件事：

1. **看见自己是提议者会先走完 Prepare 那五步 / 看见走完了 不是已经不用再 Process，也不是已经保证是这一次。**  
   官方写：若 *p* 是提议者，*p* 先执行 Prepare 那五步。看见走完了，不是已经 Process 也会在提议者那边叫那种已经不用再 Process。看见自己是提议者，不是已经通常紧跟 Prepare、列表对得上那种已经保证是这一次。看见先走 Prepare，不是已经交差。
2. **看见 Process 的 `height` / `time` 对上拟议块头 / 看见对上了 不是已经验过块头，也不是已经跑过 Process。**  
   官方写：Process 的 height 和 time 对上拟议块的头。看见对上了，不是已经收到带上头的提案会先验块头那种已经验过。看见字段对上，不是已经 Prepare 和 Process / Finalize 同一套字段那种已经跑过 Process。看见能对，不是已经交差。
3. **看见 Finalize 的 `height` / `time` 对上拟议块头 / 看见对上了 不是已经是刚决定那块的字段，也不是已经知道本头哈希。**  
   官方写：Finalize 的 height 和 time 对上拟议块的头。看见对上了，不是已经 Finalize 含刚决定那块的字段那种已经是四门已经结算。看见字段对上，不是已经 Finalize 请求 hash 那种已经知道本头哈希。看见能对，不是已经交差。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。Process 也会在提议者那边叫就已经不用再 Process 是不变量 351，本页不抄。

## 官方为什么这样拆

- **自己是提议者会先走完 Prepare 那五步 ≠ 已经不用再 Process：** 官方把先走 Prepare 那五步和已经调过 Process 分开。
- **Process 的 height / time 对上拟议块头 ≠ 已经验过块头：** 官方把 Usage 里这份对上和 When 里先验块头分开。
- **Finalize 的 height / time 对上拟议块头 ≠ 已经是刚决定那块的字段：** 官方把 Finalize 这份对上和已经含刚决定那块的字段分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 自己是提议者会先走完 Prepare 那五步 | 不是已经不用再 Process | 不是 Process 也会在提议者那边叫就已经不用再 Process（351） |
| Process 的 height / time 对上拟议块头 | 不是已经验过块头 | 不是收到带上头的提案会先验块头就已经跑过 Process（416） |
| Finalize 的 height / time 对上拟议块头 | 不是已经是刚决定那块的字段 | 不是 Finalize 含刚决定那块的字段就已经是四门已经结算（407） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了头字段就已经不用再 Process、已经验过块头、已经是刚决定那块的字段」，必须分开自己是提议者会先走完 Prepare 那五步是不是已经不用再 Process、Process 的 height / time 对上拟议块头是不是已经验过块头、Finalize 的 height / time 对上拟议块头是不是已经是刚决定那块的字段。可以跳过「看见填了头字段就已经不用再 Process」。不要另写怎样写头字段对上余量。417 htmatch vs header bundled unbundling 完成（1097 item 1 / 1098 item 2 / 1099 item 3）；精读 [`worked-example-htmt-notskip-vs-bundled.md`](worked-example-htmt-notskip-vs-bundled.md)（不变量 1097 item 1）。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
- 收到带上头的提案会先验块头就已经跑过 Process。那是不变量 416。
- Finalize 含刚决定那块的字段就已经是四门已经结算。那是不变量 407。
