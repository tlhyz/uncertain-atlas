# 例：看见崩溃了 / 看见回包坏了 / 看见引擎停了 is not already already process-reject interchangeable / already req3-accept interchangeable / already settled interchangeable

**层次**：实现 / Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量）/ not 825 prepvalid-notreject interchangeable / not 357 preparevalid bundled interchangeable」，不是 Prepare 回包校验 bundled（357），也不是引擎没有再验重复交易不是已经验过重复（824 item 1 余量）或 Prepare 里产出了事件不是已经交给引擎（826 item 3 余量）。不要另写怎样再验 Prepare 回包。

## 官方三件事

规范把 Methods 里若 CometBFT 验不过 `PrepareProposalResponse` 就把应用当成故障并崩溃 和「已经是崩溃了就已经是 Process REJECT interchangeable / 已经是回包坏了就已经是 Req 3 必须 Accept interchangeable / 已经是引擎停了就已经交差 interchangeable / 已经是 preparevalid bundled interchangeable」分开写成三件独立的实现事，不是「看见崩溃了就已经是 Process REJECT interchangeable / 就已经是 Req 3 必须 Accept interchangeable / 就已经交差 interchangeable」一件事：

1. **看见崩溃了 / 看见 Prepare 回包验不过 / 看见引擎当应用坏了并崩溃 is not already 已经是 Process REJECT interchangeable / 已经 process-reject interchangeable / 已经是 Process REJECT 交差 interchangeable / 357 preparevalid bundled interchangeable / 347 req3 interchangeable / preparevalid-sold-as-checked interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 825 prepvalid-notreject interchangeable / 357 preparevalid item 2 interchangeable，也不是已经 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事 bundled（357 item 2 余量） interchangeable / 357 preparevalid item 2 interchangeable，也不是已经验过重复（824） interchangeable / 826 prepvalid-notfinalize interchangeable / 347 req3-accept interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable。**  
   官方写：若 CometBFT 验不过 `PrepareProposalResponse`，就把应用当成故障并崩溃。看见崩溃了，不是已经是 Process REJECT。看见崩溃了，不是已经 process-reject interchangeable——357 钉 bundled 三事，本页从 item 2 侧钉 not already process-reject 单句。看见 Prepare 回包验不过，不是已经 Prepare 回包校验 bundled（357） interchangeable——357 钉 bundled，本页钉 item 2 第一件事。看见崩溃了，不是已经验过重复（824） interchangeable——824 另钉 item 1。看见崩溃了，不是已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable——347 另钉。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

2. **看见回包坏了 / 看见验不过 PrepareProposalResponse / 看见回包验不过 is not already 已经是 Req 3 必须 Accept interchangeable / 已经 req3-accept interchangeable / 已经是 Req 3 必须 Accept 交差 interchangeable / 357 preparevalid bundled interchangeable / 347 req3 interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 825 prepvalid-notreject interchangeable / 357 preparevalid item 1 去重 interchangeable / 357 preparevalid item 3 事件 interchangeable，也不是已经 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事 bundled（357 item 2 余量） interchangeable / 357 preparevalid item 2 interchangeable，也不是已经是 Process REJECT（本页第一件事） interchangeable。**  
   官方写：看见回包坏了，不是已经是 Req 3 必须 Accept。看见验不过 PrepareProposalResponse，不是已经 req3-accept interchangeable——本页钉 not already req3-accept 单句。看见回包验不过，不是已经是 Process REJECT（本页第一件事） interchangeable——三件事分开钉。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

3. **看见引擎停了 / 看见崩溃停机 / 看见应用被当成故障 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 357 preparevalid bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 825 prepvalid-notreject interchangeable / 357 preparevalid item 1 / 357 preparevalid item 3，也不是已经 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事 bundled（357 item 2 余量） interchangeable / 357 preparevalid item 2 interchangeable，也不是已经是 Process REJECT（本页第一件事） interchangeable / 已经是 Req 3 必须 Accept（本页第二件事） interchangeable。**  
   官方写：看见引擎停了，不是已经交差。看见崩溃停机，不是已经 settled interchangeable——本页钉 not already settled 单句。看见应用被当成故障，不是已经是 Req 3 必须 Accept（本页第二件事） interchangeable——三件事分开钉。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

怎样再验 Prepare 回包、怎样查重复、怎样攒事件是规范里的做法，本页不抄。Prepare 回包校验 bundled（357）、引擎没有再验重复交易不是已经验过重复（357 item 1 余量 / 824）、Prepare 里产出了事件不是已经交给引擎（357 item 3 余量 / 826）、内存池去重就已经保证不重放（313）、正确提议者的准备提案必须被正确接收者 Accept（347）、Code / Data 就已经印进本头（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **崩溃了 not already process-reject ≠ 357 / 347 interchangeable：** 官方把崩溃和 Process REJECT 分开。
- **回包坏了 not already req3-accept ≠ 已经是 Req 3 必须 Accept interchangeable：** 官方把回包坏了和已经是 Req 3 必须 Accept 分开。
- **引擎停了 not already settled ≠ 已经交差 interchangeable：** 官方把引擎停了和已经交差分开；357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 崩溃了 | 不是 already process-reject | 不是正确提议者的准备提案必须被正确接收者 Accept alone（347） |
| 回包坏了 | 不是 already req3-accept | 不是回了提案 already dedup-checked alone（824） |
| 引擎停了 | 不是 already settled | 不是产出事件 already finalize alone（826） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量），必须分开崩溃了 是不是 already process-reject interchangeable / 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable、回包坏了 是不是 already req3-accept interchangeable、引擎停了 是不是 already settled interchangeable。可以跳过「看见崩溃了就已经是 Process REJECT interchangeable / 就已经是 Req 3 必须 Accept interchangeable / 就已经交差 interchangeable」。不要另写怎样再验 Prepare 回包。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续（824 + 825）。

## 本页不抄

- 怎样再验 Prepare 回包、怎样查重复、怎样攒事件。
- Prepare 回包校验 bundled。那是不变量 357。
- 引擎没有再验重复交易不是已经验过重复。那是不变量 357 item 1 余量 / 824。
- Prepare 里产出了事件不是已经交给引擎。那是不变量 357 item 3 余量 / 826。
- 内存池去重就已经保证不重放。那是不变量 313。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Code / Data 就已经印进本头。那是不变量 316。
