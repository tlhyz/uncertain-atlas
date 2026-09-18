# 例：看见 proposal header-first is not already processed interchangeable / not already header-known interchangeable / not already settled interchangeable

**层次**：实现 / proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量）/ not 1095 ptime-notproc interchangeable / not 416 proposetimeout-vs-process bundled interchangeable」，不是 Process 何时调用余量 bundled（416），也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359），也不是 Finalize 请求 hash 就已经知道本头哈希。不要另写怎样写 Process 何时调用余量。

## 官方三件事

1. **看见收到带上头的提案会先验块头 / 看见验了头 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1095 ptime-notproc interchangeable / 1094 ptime-notcfg interchangeable / 416 proposetimeout item 1 timeout interchangeable，也不是已经 proposal header-first not already processed / not already header-known / not already settled 正式三事 bundled（416 item 2 余量） interchangeable / 416 proposetimeout item 2 interchangeable。**  
   官方写：收到提议者 q 这一轮这一高的 Proposal（里头带上头），p 先验块头。看见验了头，不是已经跑过 Process interchangeable——本页从 416 item 2 侧钉 not already processed 单句。416 proposetimeout vs process bundled unbundling 在本页 item 2 续。

2. **看见提案带上头 / 看见验了头 / 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1095 ptime-notproc interchangeable / 416 proposetimeout item 3 prevote interchangeable / 1096 ptime-notcall interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process interchangeable / 359 prepare-fields interchangeable。**  
   官方把提案带上头和已经知道本头哈希分开。看见提案带上头，不是已经知道本头哈希 interchangeable。本页钉 not already header-known 单句。

3. **看见先验 / 看见验了头 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 何时调用余量 bundled（416） interchangeable / 1095 ptime-notproc interchangeable / 1094 ptime-notcfg interchangeable，也不是已经 Process height/time 对上就已经验过块头 interchangeable / 417 htmatch interchangeable。**  
   官方把先验和已经交差分开。看见先验，不是已经交差 interchangeable。416 proposetimeout vs process bundled unbundling 在本页 item 2 续。

怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **proposal header-first not already processed ≠ 已经跑过 Process interchangeable：** 官方把先验块头和已经调过 Process 分开。
- **看见提案带上头 not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把提案带上头和已经知道本头哈希分开。
- **看见先验 not already settled ≠ 已经交差 interchangeable：** 官方把先验和已经交差分开；416 proposetimeout vs process bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收到带上头的提案会先验块头 | 不是已经跑过 Process | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 看见提案带上头 | 不是已经知道本头哈希 | 不是 Process height/time 对上就已经验过块头（417） |
| 看见先验 | 不是已经交差 | 不是还在看 prevote 就已经会调 Process（1096） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量），必须分开是不是已经跑过 Process、是不是已经知道本头哈希、是不是已经交差。可以跳过「看见到了 Process 何时调用就已经填了 TimeoutPropose」。不要另写怎样写 Process 何时调用余量。416 proposetimeout vs process bundled unbundling 在本页 item 2 续；续 [`worked-example-ptime-notcall-vs-bundled.md`](worked-example-ptime-notcall-vs-bundled.md)（不变量 1096 item 3）。

## 本页不抄

- 怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头。
- Process 何时调用余量 bundled。那是不变量 416。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- Process height/time 对上就已经验过块头。那是不变量 417。
