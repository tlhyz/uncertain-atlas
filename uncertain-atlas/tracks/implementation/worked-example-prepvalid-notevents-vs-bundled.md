# 例：看见 Prepare MAY produce events is not already handed to engine interchangeable / not already LastResultsHash interchangeable / not already Finalize events interchangeable

**层次**：实现 / Prepare 回包校验 events not handed / not LastResultsHash / not Finalize events 正式三事（357 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 回包校验 events not handed / not LastResultsHash / not Finalize events 正式三事（357 余量）/ not 718 prepvalid-notevents interchangeable / not 357 prepare-valid-vs-checked bundled interchangeable」，不是 Prepare 回包校验 bundled（357），也不是 Code / Data 就已经印进本头（316）或 Finalize 回包 events（431）。不要另写怎样攒事件。

## 官方三件事

1. **看见 Prepare 里产出了块事件或交易事件 / 看见先跑了 / 应用 MAY 产出块事件或交易事件，必须把这些事件留到块决定之后，再经 FinalizeBlockResponse 交给 CometBFT / events is not already 已经交给引擎 interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 718 prepvalid-notevents interchangeable / 716 prepvalid-notchecked interchangeable / 357 preparevalid item 1 no checks interchangeable，也不是已经 events not handed / not LastResultsHash / not Finalize events 正式三事 bundled（357 item 3 余量） interchangeable / 357 preparevalid item 3 interchangeable。**  
   官方 Usage 写：执行这份准备提案时，应用 MAY 产出块事件或交易事件。必须把这些事件留到块决定之后，再经 FinalizeBlockResponse 交给 CometBFT。看见先跑了，不是已经交出去 interchangeable——本页从 357 item 3 侧钉 not handed 单句。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

2. **看见有事件 / 看见留着 / events is not already 已经印进 LastResultsHash interchangeable / 316 results interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 718 prepvalid-notevents interchangeable / 357 preparevalid item 2 crash interchangeable / 717 prepvalid-notcrash interchangeable。**  
   官方把 Prepare 先产出事件和印进 LastResultsHash 分开——357 bundled 第三件事常与 316 混成「看见有事件就已经印进本头 interchangeable」，本页钉 not LastResultsHash 单句。

3. **看见先跑了 / 看见 Usage 这句 / events is not already 已经 FinalizeBlockResponse.events 给索引用（431） interchangeable / 431 finevents interchangeable / 已经 Prepare 事件保留路径 bundled（451） interchangeable / 451 prepareevents interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 718 prepvalid-notevents interchangeable / 716 prepvalid-notchecked interchangeable。**  
   官方把 357 回包校验侧先产出事件和 Finalize 回包 events / 451 事件保留路径分开。看见先跑了，不是已经 431 / 451 交差 interchangeable。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

怎样再验 Prepare 回包、怎样查重复、怎样攒事件是规范里的做法，本页不抄。

## 官方为什么这样拆

- **events not handed ≠ 已经交给引擎 interchangeable：** 官方把先产出和经 Finalize 交回分开。
- **events not LastResultsHash ≠ 316 interchangeable：** 官方把 Prepare 先产出和印进本头分开。
- **events not Finalize events ≠ 431 / 451 interchangeable：** 官方把 357 先产出和 Finalize events / 事件保留路径分开；357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 里产出了事件 | 不是已经交给引擎 | 不是没有再验（716/357 item 1） |
| 看见有事件 | 不是已经印进 LastResultsHash（316） | 不是 Prepare 回包校验 bundled（357） |
| 看见先跑了 | 不是 Finalize events（431） / 事件保留路径（451） | 不是回包验不过会崩（717/357 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 events not handed / not LastResultsHash / not Finalize events 正式三事（357 余量），必须分开先产出是不是已经交给引擎、是不是已经印进 LastResultsHash interchangeable / 316、是不是 Finalize events / 事件保留路径 interchangeable / 431 / 451。可以跳过「看见有事件就已经交给引擎」。不要另写怎样攒事件。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样再验 Prepare 回包、怎样查重复、怎样攒事件。
- Prepare 回包校验 bundled。那是不变量 357。
- 引擎没有再验重复交易。那是不变量 357 item 1 余量 / 716。
- Prepare 回包验不过引擎崩溃。那是不变量 357 item 2 余量 / 717。
- Code / Data 就已经印进本头。那是不变量 316。
- FinalizeBlockResponse.events。那是不变量 431。
- Prepare 事件保留路径。那是不变量 451。
