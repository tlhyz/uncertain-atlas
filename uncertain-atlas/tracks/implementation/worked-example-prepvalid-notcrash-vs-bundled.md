# 例：看见 Prepare response fail crashes engine is not already Process REJECT interchangeable / not already must Accept interchangeable / not already ProposalStatus REJECT interchangeable

**层次**：实现 / Prepare 回包校验 crash not Process REJECT / not must Accept / not ProposalStatus REJECT 正式三事（357 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 回包校验 crash not Process REJECT / not must Accept / not ProposalStatus REJECT 正式三事（357 余量）/ not 717 prepvalid-notcrash interchangeable / not 357 prepare-valid-vs-checked bundled interchangeable」，不是 Prepare 回包校验 bundled（357），也不是正确提议者的准备提案必须被正确接收者 Accept（347）或 ProposalStatus REJECT（376）。不要另写怎样再验 Prepare 回包。

## 官方三件事

1. **看见 Prepare 回包验不过 / 看见引擎当应用坏了并崩溃 / If CometBFT fails to validate PrepareProposalResponse, assume Application is faulty and crash / crash is not already 已经是 Process REJECT interchangeable / 455 procreject interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 717 prepvalid-notcrash interchangeable / 716 prepvalid-notchecked interchangeable / 357 preparevalid item 1 no checks interchangeable，也不是已经 crash not Process REJECT / not must Accept / not ProposalStatus REJECT 正式三事 bundled（357 item 2 余量） interchangeable / 357 preparevalid item 2 interchangeable。**  
   官方 Usage 写：若 CometBFT 验不过 PrepareProposalResponse，就把应用当成故障并崩溃。看见崩溃了，不是已经是 Process REJECT interchangeable——本页从 357 item 2 侧钉 not Process REJECT 单句。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

2. **看见回包坏了 / 看见引擎停了 / crash is not already 已经是正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable / 347 mustaccept interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 717 prepvalid-notcrash interchangeable / 357 preparevalid item 3 events interchangeable / 718 prepvalid-notevents interchangeable。**  
   官方把 Prepare 回包坏了就停进程和 Req 3 必须 Accept 分开——357 bundled 第二件事常与 347 混成「看见崩了就已经是必须 Accept interchangeable」，本页钉 not must Accept 单句。

3. **看见崩溃了 / 看见 Usage 这句 / crash is not already 已经 ProposalStatus REJECT 会发 Prevote nil（376） interchangeable / 376 / 715 propstat-notreject interchangeable / 已经 Prepare Usage no checks / crash / nondet bundled（504） interchangeable / 504 nochecks interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 717 prepvalid-notcrash interchangeable / 716 prepvalid-notchecked interchangeable。**  
   官方把 357 回包校验侧 crash 和 376 REJECT 发 nil / 504 Usage 末尾 crash 单句分开。看见崩了，不是已经 376 / 504 交差 interchangeable。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

怎样再验 Prepare 回包、怎样查重复、怎样攒事件是规范里的做法，本页不抄。

## 官方为什么这样拆

- **crash not Process REJECT ≠ 455 interchangeable：** 官方把 Prepare crash 和 Process REJECT 分开。
- **crash not must Accept ≠ 347 interchangeable：** 官方把回包坏了就停和 Req 3 必须 Accept 分开。
- **crash not ProposalStatus REJECT ≠ 376 / 504 interchangeable：** 官方把 357 crash 和 REJECT 发 nil / Usage 末尾 crash 分开；357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 回包验不过引擎崩溃 | 不是已经是 Process REJECT（455） | 不是没有再验（716/357 item 1） |
| 看见回包坏了 | 不是 honest proposal 必须 Accept（347） | 不是 Prepare 回包校验 bundled（357） |
| 看见崩溃了 | 不是 ProposalStatus REJECT（376） / Usage 末尾 crash（504） | 不是 Prepare 事件已交（718/357 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 crash not Process REJECT / not must Accept / not ProposalStatus REJECT 正式三事（357 余量），必须分开崩溃是不是 Process REJECT interchangeable / 455、是不是 Req 3 必须 Accept interchangeable / 347、是不是 ProposalStatus REJECT / Usage 末尾 crash interchangeable / 376 / 504。可以跳过「看见崩了就已经是 Process REJECT」。不要另写怎样再验 Prepare 回包。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续；完成 [`worked-example-prepvalid-notevents-vs-bundled.md`](worked-example-prepvalid-notevents-vs-bundled.md)（不变量 718 item 3）。

## 本页不抄

- 怎样再验 Prepare 回包、怎样查重复、怎样攒事件。
- Prepare 回包校验 bundled。那是不变量 357。
- 引擎没有再验重复交易。那是不变量 357 item 1 余量 / 716。
- Prepare 里产出了事件。那是不变量 357 item 3 余量 / 718。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- ProposalStatus REJECT。那是不变量 376。
- Prepare Usage no checks / crash / nondet bundled。那是不变量 504。
