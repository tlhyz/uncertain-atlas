# 例：看见先跑了 / 看见有事件 / 看见留着 is not already already handed-over interchangeable / already results-hash interchangeable / already settled interchangeable

**层次**：实现 / Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量）/ not 826 prepvalid-notfinalize interchangeable / not 357 preparevalid bundled interchangeable」，不是 Prepare 回包校验 bundled（357），也不是引擎没有再验重复交易不是已经验过重复（824 item 1 余量）或 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT（825 item 2 余量）。不要另写怎样再验 Prepare 回包。

## 官方三件事

规范把 Methods 里执行这份准备提案时应用 MAY 产出块事件或交易事件、必须把这些事件留到块决定之后再经 `FinalizeBlockResponse` 交给 CometBFT 和「已经是先跑了就已经交出去 interchangeable / 已经是有事件就已经印进 LastResultsHash interchangeable / 已经是留着就已经交差 interchangeable / 已经是 preparevalid bundled interchangeable」分开写成三件独立的实现事，不是「看见先跑了就已经交出去 interchangeable / 就已经印进 LastResultsHash interchangeable / 就已经交差 interchangeable」一件事：

1. **看见先跑了 / 看见 Prepare 里产出了块事件或交易事件 / 看见应用 MAY 产出事件 is not already 已经交出去 interchangeable / 已经 handed-over interchangeable / 已经交给引擎交差 interchangeable / 357 preparevalid bundled interchangeable / 316 exectxresult interchangeable / preparevalid-sold-as-checked interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 826 prepvalid-notfinalize interchangeable / 357 preparevalid item 3 interchangeable，也不是已经 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事 bundled（357 item 3 余量） interchangeable / 357 preparevalid item 3 interchangeable，也不是已经验过重复（824） interchangeable / 825 prepvalid-notreject interchangeable / 316 LastResultsHash interchangeable，也不是已经 Code / Data 就已经印进本头（316） interchangeable。**  
   官方写：执行这份准备提案时，应用 MAY 产出块事件或交易事件。必须把这些事件留到块决定之后，再经 `FinalizeBlockResponse` 交给 CometBFT。看见先跑了，不是已经交出去。看见先跑了，不是已经 handed-over interchangeable——357 钉 bundled 三事，本页从 item 3 侧钉 not already handed-over 单句。看见 Prepare 里产出了事件，不是已经 Prepare 回包校验 bundled（357） interchangeable——357 钉 bundled，本页钉 item 3 第一件事。看见先跑了，不是已经验过重复（824） interchangeable——824 另钉 item 1。看见先跑了，不是已经是 Process REJECT（825） interchangeable——825 另钉 item 2。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

2. **看见有事件 / 看见产出了块事件或交易事件 / 看见先产出了 is not already 已经印进 LastResultsHash interchangeable / 已经 results-hash interchangeable / 已经印进 LastResultsHash 交差 interchangeable / 357 preparevalid bundled interchangeable / 316 exectxresult interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 826 prepvalid-notfinalize interchangeable / 357 preparevalid item 1 去重 interchangeable / 357 preparevalid item 2 崩溃 interchangeable，也不是已经 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事 bundled（357 item 3 余量） interchangeable / 357 preparevalid item 3 interchangeable，也不是已经交出去（本页第一件事） interchangeable。**  
   官方写：看见有事件，不是已经印进 LastResultsHash。看见产出了块事件或交易事件，不是已经 results-hash interchangeable——本页钉 not already results-hash 单句。看见先产出了，不是已经交出去（本页第一件事） interchangeable——三件事分开钉。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

3. **看见留着 / 看见必须留到块决定之后 / 看见还没经 Finalize 交回 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 357 preparevalid bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 826 prepvalid-notfinalize interchangeable / 357 preparevalid item 1 / 357 preparevalid item 2，也不是已经 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事 bundled（357 item 3 余量） interchangeable / 357 preparevalid item 3 interchangeable，也不是已经交出去（本页第一件事） interchangeable / 已经印进 LastResultsHash（本页第二件事） interchangeable。**  
   官方写：看见留着，不是已经交差。看见必须留到块决定之后，不是已经 settled interchangeable——本页钉 not already settled 单句。看见还没经 Finalize 交回，不是已经印进 LastResultsHash（本页第二件事） interchangeable——三件事分开钉。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

怎样再验 Prepare 回包、怎样查重复、怎样攒事件是规范里的做法，本页不抄。Prepare 回包校验 bundled（357）、引擎没有再验重复交易不是已经验过重复（357 item 1 余量 / 824）、Prepare 回包验不过引擎崩溃不是已经是 Process REJECT（357 item 2 余量 / 825）、内存池去重就已经保证不重放（313）、正确提议者的准备提案必须被正确接收者 Accept（347）、Code / Data 就已经印进本头（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **先跑了 not already handed-over ≠ 357 / 316 interchangeable：** 官方把先产出和经 Finalize 交回分开。
- **有事件 not already results-hash ≠ 已经印进 LastResultsHash interchangeable：** 官方把有事件和已经印进 LastResultsHash 分开。
- **留着 not already settled ≠ 已经交差 interchangeable：** 官方把留着和已经交差分开；357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 先跑了 | 不是 already handed-over | 不是 Code / Data 就已经印进本头 alone（316） |
| 有事件 | 不是 already results-hash | 不是回了提案 already dedup-checked alone（824） |
| 留着 | 不是 already settled | 不是回包崩溃 already process-reject alone（825） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量），必须分开先跑了 是不是 already handed-over interchangeable / 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable、有事件 是不是 already results-hash interchangeable、留着 是不是 already settled interchangeable。可以跳过「看见先跑了就已经交出去 interchangeable / 就已经印进 LastResultsHash interchangeable / 就已经交差 interchangeable」。不要另写怎样再验 Prepare 回包。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成（824 + 825 + 826）。

## 本页不抄

- 怎样再验 Prepare 回包、怎样查重复、怎样攒事件。
- Prepare 回包校验 bundled。那是不变量 357。
- 引擎没有再验重复交易不是已经验过重复。那是不变量 357 item 1 余量 / 824。
- Prepare 回包验不过引擎崩溃不是已经是 Process REJECT。那是不变量 357 item 2 余量 / 825。
- 内存池去重就已经保证不重放。那是不变量 313。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Code / Data 就已经印进本头。那是不变量 316。
