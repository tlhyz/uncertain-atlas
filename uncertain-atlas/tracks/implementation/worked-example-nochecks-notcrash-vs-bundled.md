# 例：看见Prepare 回包验不过引擎崩溃不是已经是 Process REJECT；看见当应用坏了并崩溃不是已经是正确提议者必须被 Accept；看见Prepare 回包验不过引擎崩溃不是已经 ProposalStatus REJECT

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事（504 余量）/ not 1308 nochecks-notcrash interchangeable / not 504 prepareusage-nochecks-vs-bundled bundled interchangeable」，不是 prepareusage nochecks vs bundled bundled（504），也不是已经 Process REJECT（455），也不是已经 Req 3 Accept（347）。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。

## 官方三件事

1. **看见Prepare 回包验不过引擎崩溃 / 看见Prepare 回包验不过引擎崩溃 这份对象 is not already 已经是 Process REJECT interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1308 nochecks-notcrash interchangeable / 1307 nochecks-notdup interchangeable，也不是已经 PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事 bundled（504 item 2 余量） interchangeable / 504 nochecks item 2 interchangeable。**  
   官方把Prepare 回包验不过引擎崩溃和已经是 Process REJECT写成两件。看见Prepare 回包验不过引擎崩溃，不是已经是 Process REJECT。

2. **看见当应用坏了并崩溃 / 看见Prepare 回包验不过引擎崩溃 / 这份对象 is not already 已经是正确提议者必须被 Accept interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1308 nochecks-notcrash interchangeable / 1309 nochecks-notdet interchangeable，也不是已经 Process REJECT interchangeable / 455 Process REJECT interchangeable。**  
   官方把当应用坏了并崩溃和已经是正确提议者必须被 Accept写成两件。看见当应用坏了并崩溃，不是已经是正确提议者必须被 Accept。

3. **看见Prepare 回包验不过引擎崩溃 / 看见当应用坏了并崩溃 / 这份对象 is not already 已经 ProposalStatus REJECT interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1308 nochecks-notcrash interchangeable / 1307 nochecks-notdup interchangeable，也不是已经 Req 3 Accept interchangeable / 347 Req 3 Accept interchangeable。**  
   官方把Prepare 回包验不过引擎崩溃和已经 ProposalStatus REJECT写成两件。看见Prepare 回包验不过引擎崩溃，不是已经 ProposalStatus REJECT。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。

## 官方为什么这样拆

- **crash on invalid response 不是 Process REJECT interchangeable：官方把 Prepare crash 单句和 Process REJECT / Req 3 Accept 分开。**
- **看见当应用坏了并崩溃 不是已经是正确提议者必须被 Accept：347 钉 Req 3，本页钉 Prepare 回包坏了就停进程。**
- **看见崩溃 不是已经 ProposalStatus REJECT：376 钉 REJECT 会发 Prevote nil，本页钉 Usage crash 单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 Process REJECT | 不是已经是 Process REJECT | 不是已经Process REJECT（455） |
| 已经是正确提议者必须被 Accept | 不是已经是正确提议者必须被 Accept | 不是已经Req 3 Accept（347） |
| 已经 ProposalStatus REJECT | 不是已经 ProposalStatus REJECT | 不是已经1307 nochecks-notdup |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事（504 余量），必须分开是不是已经是 Process REJECT、是不是已经是正确提议者必须被 Accept、是不是已经 ProposalStatus REJECT。可以跳过「看见回了 Prepare 回包就已经验过重复、已经是 Process REJECT、已经必须确定 interchangeable」。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。504 PrepareProposal Usage nochecks bundled unbundling 在本页 item 2 续；续 [`worked-example-nochecks-notdet-vs-bundled.md`](worked-example-nochecks-notdet-vs-bundled.md)（不变量 1309 item 3）。

## 本页不抄

- 怎样做再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
- 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
