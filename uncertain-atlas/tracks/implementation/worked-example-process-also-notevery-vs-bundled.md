# 例：看见失败时可能对上更早一次或根本不调 is not already this Prepare interchangeable / not already every round calls interchangeable / not already settled interchangeable

**层次**：实现 / 失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事（351 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事（351 余量）/ not 862 process-also-notevery interchangeable / not 351 process-also-vs-prepare bundled interchangeable」，不是 Process 也会在提议者那边叫 bundled（351），也不是候选已经是 ExecuteTxState（311），也不是四门已经结算（33）。不要另写怎样写 Process。

## 官方三件事

1. **看见失败时可能对上更早一次 Prepare / 看见叫了 Process 这份失败 is not already 已经是这一次 Prepare interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 862 process-also-notevery interchangeable / 860 process-also-notskip interchangeable / 351 process-also item 1 提议者 interchangeable，也不是已经失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事 bundled（351 item 3 余量） interchangeable / 351 process-also item 3 interchangeable。**  
   官方写：失败时不保证。`ProcessProposalRequest` 可能对上更早一次 Prepare 的回包。看见叫了 Process，不是已经是这一次刚回的那份 interchangeable——本页从 351 item 3 侧钉 not already this Prepare 单句。351 process-also vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见根本不调 Process / 看见进了这一轮 / 这份失败 is not already 已经每轮都会叫 Process interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 862 process-also-notevery interchangeable / 351 process-also item 2 对得上 interchangeable / 861 process-also-notsame interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把进了这一轮和已经每轮都会叫分开——351 bundled 第三件事常与 311 混成「看见进了这一轮就已经是这一次或已经每轮都会叫 interchangeable」，本页钉 not already every round calls 单句。

3. **看见根本不调 Process / 看见失败了 / 这份失败 is not already 已经交差 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 862 process-also-notevery interchangeable / 860 process-also-notskip interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把失败了和已经交差分开。看见失败了，不是已经交差 interchangeable。351 process-also vs prepare bundled unbundling 在本页 item 3 完成。

怎样写 Process、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。

## 官方为什么这样拆

- **失败时可能对上更早一次 not already this Prepare ≠ 已经是这一次 Prepare interchangeable：** 官方把叫了 Process 和已经是这一次分开。
- **看见进了这一轮 not already every round calls ≠ 已经每轮都会叫 interchangeable：** 官方把进了这一轮和已经每轮都会叫分开。
- **看见失败了 not already settled ≠ 已经交差 interchangeable：** 官方把失败了和已经交差分开；351 process-also vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 失败时可能对上更早一次或根本不调 | 不是已经是这一次 Prepare | 不是候选已经是 ExecuteTxState（311） |
| 看见进了这一轮 | 不是已经每轮都会叫 | 不是四门已经结算（33） |
| 看见失败了 | 不是已经交差 | 不是提议者就已经不用再 Process（860） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事（351 余量），必须分开是不是已经是这一次 Prepare、是不是已经每轮都会叫、是不是已经交差。可以跳过「看见进了这一轮就已经每轮都会叫」。不要另写怎样写 Process。351 process-also vs prepare bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Process、怎样缓存候选、怎样测失败路径。
- Process 也会在提议者那边叫 bundled。那是不变量 351。
- Process 也会在提议者那边叫。那是不变量 351 item 1 余量 / 860。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 四门已经结算。那是不变量 33。
