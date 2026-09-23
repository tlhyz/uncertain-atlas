# 例：看见 ProcessProposal 也会在这一轮的提议者那边叫 / 看见自己刚 Prepare 过 / 看见是提议者 is not already already skip-process interchangeable / already settled interchangeable / already already-processed interchangeable

**层次**：实现 / Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量）/ not 806 process-notskip interchangeable / not 351 processalso bundled interchangeable」，不是 Process 也会在提议者那边叫 bundled（351），也不是通常紧跟 Prepare、列表对得上不是已经保证是这一次（807 item 2 余量）或失败时可能对上更早一次或根本不调不是已经每轮都会叫（808 item 3 余量）。不要另写怎样写 Process。

## 官方三件事

规范把 Methods 里 `ProcessProposal` 也会在这一轮的提议者那边叫、自己刚 Prepare 过 和「已经是刚 Prepare 过就已经不用再 Process interchangeable / 已经是提议者就已经交差 interchangeable / 已经是列表自己编的就已经过了 Process interchangeable / 已经是 processalso bundled interchangeable」分开写成三件独立的实现事，不是「看见自己刚 Prepare 过就已经不用再 Process interchangeable / 就已经交差 interchangeable / 就已经过了 Process interchangeable」一件事：

1. **看见 `ProcessProposal` 也会在这一轮的提议者那边叫 / 看见自己刚 Prepare 过 / 看见自己刚回了 Prepare is not already 已经不用再 Process interchangeable / 已经 skip-process interchangeable / 已经跳过 Process 交差 interchangeable / 351 processalso bundled interchangeable / 33 fourgates interchangeable / processalso-sold-as-matched interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 806 process-notskip interchangeable / 351 processalso item 1 interchangeable，也不是已经 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事 bundled（351 item 1 余量） interchangeable / 351 processalso item 1 interchangeable，也不是已经通常对得上（807） interchangeable / 808 process-notalways interchangeable / 347 req3coherence interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`ProcessProposal` 也会在这一轮的提议者那边叫。看见自己刚回了 Prepare，不是已经不用再叫 Process。看见自己刚 Prepare 过，不是已经 skip-process interchangeable——351 钉 bundled 三事，本页从 item 1 侧钉 not already skip-process 单句。看见 `ProcessProposal` 也会在这一轮的提议者那边叫，不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable——351 钉 bundled，本页钉 item 1 第一件事。看见自己刚回了 Prepare，不是已经四门已经结算（33） interchangeable——33 另钉。351 processalso vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见是提议者 / 看见这一轮是自己提议 / 看见提议者身份 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 351 processalso bundled interchangeable / 33 fourgates interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 806 process-notskip interchangeable / 351 processalso item 2 对得上 interchangeable / 351 processalso item 3 失败 interchangeable，也不是已经 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事 bundled（351 item 1 余量） interchangeable / 351 processalso item 1 interchangeable，也不是已经不用再 Process（本页第一件事） interchangeable。**  
   官方写：看见是提议者，不是已经交差。看见这一轮是自己提议，不是已经 settled interchangeable——本页钉 not already settled 单句。看见提议者身份，不是已经不用再 Process（本页第一件事） interchangeable——三件事分开钉。351 processalso vs prepare bundled unbundling 在本页 item 1 启动。

3. **看见列表自己编的 / 看见 txs 自己刚回 / 看见自己编的列表 is not already 已经过了 Process interchangeable / 已经 already-processed interchangeable / 已经过 Process 交差 interchangeable / 351 processalso bundled interchangeable / 311 candidate interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 806 process-notskip interchangeable / 351 processalso item 2 / 351 processalso item 3，也不是已经 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事 bundled（351 item 1 余量） interchangeable / 351 processalso item 1 interchangeable，也不是已经不用再 Process（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见列表自己编的，不是已经过了 Process。看见 txs 自己刚回，不是已经 already-processed interchangeable——本页钉 not already already-processed 单句。看见自己编的列表，不是已经交差（本页第二件事） interchangeable——三件事分开钉。351 processalso vs prepare bundled unbundling 在本页 item 1 启动。

怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。Process 也会在提议者那边叫 bundled（351）、通常紧跟 Prepare、列表对得上不是已经保证是这一次（351 item 2 余量 / 807）、失败时可能对上更早一次或根本不调不是已经每轮都会叫（351 item 3 余量 / 808）、四门已经结算（33）、正确提议者的准备提案必须被正确接收者 Accept（347）、候选已经是 ExecuteTxState（311）是另外那套，本页不抄。

## 官方为什么这样拆

- **Process 也会在提议者那边叫 not already skip-process ≠ 351 / 33 interchangeable：** 官方把刚 Prepare 过和已经不用再 Process 分开。
- **是提议者 not already settled ≠ 已经交差 interchangeable：** 官方把是提议者和已经交差分开。
- **列表自己编的 not already already-processed ≠ 已经过了 Process interchangeable：** 官方把列表自己编的和已经过了 Process 分开；351 processalso vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 也会在提议者那边叫 | 不是 already skip-process | 不是四门已经结算 alone（33） |
| 是提议者 | 不是 already settled | 不是通常对得上 already guaranteed alone（807） |
| 列表自己编的 | 不是 already already-processed | 不是失败路径 already every-round alone（808） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量），必须分开 Process 也会在提议者那边叫 是不是 already skip-process interchangeable / 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable、是提议者 是不是 already settled interchangeable、列表自己编的 是不是 already already-processed interchangeable。可以跳过「看见自己刚 Prepare 过就已经不用再 Process interchangeable / 就已经交差 interchangeable / 就已经过了 Process interchangeable」。不要另写怎样写 Process。351 processalso vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-process-notguaranteed-vs-bundled.md`](worked-example-process-notguaranteed-vs-bundled.md)（不变量 807 item 2）；完成见 808。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径。
- Process 也会在提议者那边叫 bundled。那是不变量 351。
- 通常紧跟 Prepare、列表对得上不是已经保证是这一次。那是不变量 351 item 2 余量 / 807。
- 失败时可能对上更早一次或根本不调不是已经每轮都会叫。那是不变量 351 item 3 余量 / 808。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 候选已经是 ExecuteTxState。那是不变量 311。
