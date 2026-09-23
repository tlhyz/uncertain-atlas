# 例：看见引擎没有再验重复交易 / 看见回了提案 / 看见能提 / 看见没有再验 is not already already dedup-checked interchangeable / already app-replay interchangeable / already settled interchangeable

**层次**：实现 / 引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量）/ not 824 prepvalid-notdedup interchangeable / not 357 preparevalid bundled interchangeable」，不是 Prepare 回包校验 bundled（357），也不是 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT（825 item 2 余量）或 Prepare 里产出了事件不是已经交给引擎（826 item 3 余量）。不要另写怎样再验 Prepare 回包。

## 官方三件事

规范把 Methods 里 CometBFT **不**再做额外有效性检查（例如查有没有重复交易）和「已经是回了提案就已经验过重复 interchangeable / 已经是能提就已经有应用级重放保护 interchangeable / 已经是没有再验就已经交差 interchangeable / 已经是 preparevalid bundled interchangeable」分开写成三件独立的实现事，不是「看见回了提案就已经验过重复 interchangeable / 就已经有应用级重放保护 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见引擎没有再验重复交易 / 看见回了提案 / 看见没有再做额外有效性检查 is not already 已经验过重复 interchangeable / 已经 dedup-checked interchangeable / 已经验过重复交差 interchangeable / 357 preparevalid bundled interchangeable / 313 indexer interchangeable / preparevalid-sold-as-checked interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 824 prepvalid-notdedup interchangeable / 357 preparevalid item 1 interchangeable，也不是已经引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事 bundled（357 item 1 余量） interchangeable / 357 preparevalid item 1 interchangeable，也不是已经是 Process REJECT（825） interchangeable / 826 prepvalid-notfinalize interchangeable / 313 mempool-dedup interchangeable，也不是已经内存池去重就已经保证不重放（313） interchangeable。**  
   官方写：CometBFT **不**再做额外有效性检查，例如查有没有重复交易。看见回了提案，不是引擎已经验过重复。看见回了提案，不是已经 dedup-checked interchangeable——357 钉 bundled 三事，本页从 item 1 侧钉 not already dedup-checked 单句。看见引擎没有再验重复交易，不是已经 Prepare 回包校验 bundled（357） interchangeable——357 钉 bundled，本页钉 item 1 第一件事。看见回了提案，不是已经是 Process REJECT（825） interchangeable——825 另钉 item 2。看见回了提案，不是已经内存池去重就已经保证不重放（313） interchangeable——313 另钉。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

2. **看见能提 / 看见回了提案 / 看见没有再验 is not already 已经有应用级重放保护 interchangeable / 已经 app-replay interchangeable / 已经有应用级重放保护交差 interchangeable / 357 preparevalid bundled interchangeable / 313 indexer interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 824 prepvalid-notdedup interchangeable / 357 preparevalid item 2 崩溃 interchangeable / 357 preparevalid item 3 事件 interchangeable，也不是已经引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事 bundled（357 item 1 余量） interchangeable / 357 preparevalid item 1 interchangeable，也不是已经验过重复（本页第一件事） interchangeable。**  
   官方写：看见能提，不是已经有应用级重放保护。看见回了提案，不是已经 app-replay interchangeable——本页钉 not already app-replay 单句。看见没有再验，不是已经验过重复（本页第一件事） interchangeable——三件事分开钉。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

3. **看见没有再验 / 看见引擎没有再验 / 看见没有再做额外检查 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 357 preparevalid bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 824 prepvalid-notdedup interchangeable / 357 preparevalid item 2 / 357 preparevalid item 3，也不是已经引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事 bundled（357 item 1 余量） interchangeable / 357 preparevalid item 1 interchangeable，也不是已经验过重复（本页第一件事） interchangeable / 已经有应用级重放保护（本页第二件事） interchangeable。**  
   官方写：看见没有再验，不是已经交差。看见引擎没有再验，不是已经 settled interchangeable——本页钉 not already settled 单句。看见没有再做额外检查，不是已经有应用级重放保护（本页第二件事） interchangeable——三件事分开钉。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

怎样再验 Prepare 回包、怎样查重复、怎样攒事件是规范里的做法，本页不抄。Prepare 回包校验 bundled（357）、Prepare 回包验不过引擎崩溃不是已经是 Process REJECT（357 item 2 余量 / 825）、Prepare 里产出了事件不是已经交给引擎（357 item 3 余量 / 826）、内存池去重就已经保证不重放（313）、正确提议者的准备提案必须被正确接收者 Accept（347）、Code / Data 就已经印进本头（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了提案 not already dedup-checked ≠ 357 / 313 interchangeable：** 官方把不再检查和已经验过重复分开。
- **能提 not already app-replay ≠ 已经有应用级重放保护 interchangeable：** 官方把能提和已经有应用级重放保护分开。
- **没有再验 not already settled ≠ 已经交差 interchangeable：** 官方把没有再验和已经交差分开；357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了提案 | 不是 already dedup-checked | 不是内存池去重就已经保证不重放 alone（313） |
| 能提 | 不是 already app-replay | 不是回包崩溃 already process-reject alone（825） |
| 没有再验 | 不是 already settled | 不是产出事件 already finalize alone（826） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量），必须分开回了提案 是不是 already dedup-checked interchangeable / 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable、能提 是不是 already app-replay interchangeable、没有再验 是不是 already settled interchangeable。可以跳过「看见回了提案就已经验过重复 interchangeable / 就已经有应用级重放保护 interchangeable / 就已经交差 interchangeable」。不要另写怎样再验 Prepare 回包。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动；完成 [`worked-example-prepvalid-notreject-vs-bundled.md`](worked-example-prepvalid-notreject-vs-bundled.md)（不变量 825 item 2）；完成 [`worked-example-prepvalid-notfinalize-vs-bundled.md`](worked-example-prepvalid-notfinalize-vs-bundled.md)（不变量 826 item 3）。

## 本页不抄

- 怎样再验 Prepare 回包、怎样查重复、怎样攒事件。
- Prepare 回包校验 bundled。那是不变量 357。
- Prepare 回包验不过引擎崩溃不是已经是 Process REJECT。那是不变量 357 item 2 余量 / 825。
- Prepare 里产出了事件不是已经交给引擎。那是不变量 357 item 3 余量 / 826。
- 内存池去重就已经保证不重放。那是不变量 313。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Code / Data 就已经印进本头。那是不变量 316。
