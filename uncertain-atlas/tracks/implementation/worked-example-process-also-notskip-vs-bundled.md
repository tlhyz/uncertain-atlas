# 例：看见 Process 也会在提议者那边叫 is not already no need to Process again interchangeable / not already settled interchangeable / not already this call interchangeable

**层次**：实现 / Process 也会在提议者那边叫 not already no need to Process again / not already settled / not already this call 正式三事（351 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 也会在提议者那边叫 not already no need to Process again / not already settled / not already this call 正式三事（351 余量）/ not 860 process-also-notskip interchangeable / not 351 process-also-vs-prepare bundled interchangeable」，不是 Process 也会在提议者那边叫 bundled（351），也不是四门已经结算（33），也不是 Process 调用是同步的就已经能稍后改裁决（354/857）。不要另写怎样写 Process。

## 官方三件事

1. **看见 `ProcessProposal` 也会在这一轮的提议者那边叫 / 看见自己刚 Prepare 过 这份提议者 is not already 已经不用再 Process interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 860 process-also-notskip interchangeable / 861 process-also-notsame interchangeable / 351 process-also item 2 对得上 interchangeable，也不是已经 Process 也会在提议者那边叫 not already no need to Process again / not already settled / not already this call 正式三事 bundled（351 item 1 余量） interchangeable / 351 process-also item 1 interchangeable。**  
   官方写：`ProcessProposal` 也会在这一轮的提议者那边叫。看见自己刚回了 Prepare，不是已经不用再叫 Process interchangeable——本页从 351 item 1 侧钉 not already no need to Process again 单句。351 process-also vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见自己刚 Prepare 过 / 看见是提议者 / 这份提议者 is not already 已经交差 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 860 process-also-notskip interchangeable / 351 process-also item 3 失败 interchangeable / 862 process-also-notevery interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把是提议者和已经交差分开——351 bundled 第一件事常与 33 混成「看见自己刚 Prepare 过就已经不用再 Process 或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见自己刚 Prepare 过 / 看见列表自己编的 / 这份提议者 is not already 已经过了 Process interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 860 process-also-notskip interchangeable / 861 process-also-notsame interchangeable，也不是已经 Process 调用是同步的就已经能稍后改裁决 interchangeable / 354 process-when / 857 process-when-notlater interchangeable。**  
   官方把列表自己编的和已经过了 Process 分开。看见列表自己编的，不是已经过了 Process interchangeable。351 process-also vs prepare bundled unbundling 在本页 item 1 启动。

怎样写 Process、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process 也会在提议者那边叫 not already no need to Process again ≠ 已经不用再 Process interchangeable：** 官方把提议者也会叫 Process 和刚 Prepare 过分开。
- **看见是提议者 not already settled ≠ 已经交差 interchangeable：** 官方把是提议者和已经交差分开。
- **看见列表自己编的 not already this call ≠ 已经过了 Process interchangeable：** 官方把列表自己编的和已经过了 Process 分开；351 process-also vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 也会在提议者那边叫 | 不是已经不用再 Process | 不是四门已经结算（33） |
| 看见是提议者 | 不是已经交差 | 不是 Process 同步就已经能稍后改裁决（354/857） |
| 看见列表自己编的 | 不是已经过了 Process | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 也会在提议者那边叫 not already no need to Process again / not already settled / not already this call 正式三事（351 余量），必须分开是不是已经不用再 Process、是不是已经交差、是不是已经过了 Process。可以跳过「看见自己刚 Prepare 过就已经不用再 Process」。不要另写怎样写 Process。351 process-also vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-process-also-notsame-vs-bundled.md`](worked-example-process-also-notsame-vs-bundled.md)（不变量 861 item 2）。

## 本页不抄

- 怎样写 Process、怎样缓存候选、怎样测失败路径。
- Process 也会在提议者那边叫 bundled。那是不变量 351。
- 通常紧跟 Prepare、列表对得上。那是不变量 351 item 2 余量 / 861。
- 四门已经结算。那是不变量 33。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354 / 857。
