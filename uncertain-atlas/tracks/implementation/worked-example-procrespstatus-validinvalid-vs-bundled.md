# 例：看见 ProcessProposalResponse.status is application considers proposal valid or invalid / REJECT assumes not valid is not block invalid / REJECT not can't execute candidate 不是已经 Process 回包栏 bundled interchangeable / 已经当成块非法 interchangeable / 已经不能整块执行候选 interchangeable

**层次**：实现 / ProcessProposal Response status valid/invalid 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response status 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「status is application considers valid/invalid / REJECT assumes not valid not block invalid / REJECT not can't execute candidate 不是 Process 回包栏 bundled interchangeable / 不是已经当成块非法 interchangeable / 不是已经不能整块执行候选 interchangeable」，不是 ProcessProposal Response bundled（430），也不是 Process REJECT consensus assume bundled（455），也不是 ProposalStatus 枚举语义（376）。不要另写怎样写 Process 回包栏。

## 官方三件事

规范把 ProcessProposal Response 表上 status 是应用认为这份提案合法还是非法写成三件独立的实现事，不是「看见回了 ProcessProposalResponse.status 就已经当成块非法 interchangeable、已经不能整块执行候选 interchangeable、已经 prevote nil interchangeable」一件事：

1. **看见 `ProcessProposalResponse.status` is application considers proposal valid or invalid / 看见 status 是应用认为这份提案合法还是非法 不是已经 Process 回包栏 bundled（430） interchangeable / 已经当成块非法 interchangeable / 已经 MUST Accept interchangeable，也不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 prevote nil interchangeable，也不是已经 ProposalStatus REJECT bundled（376） interchangeable / 已经不能稍后改裁决 interchangeable，也不是已经 status must exclusively depend bundled（430 第二件事 / 534 余量） interchangeable / 已经可以像 Prepare 那样依赖其它值 interchangeable。**  
   官方 ProcessProposal Response 写：`status` indicates whether the Application considers the proposal valid or invalid。看见 status 是合法/非法判断，不是已经 Process 回包栏 bundled（430） interchangeable——430 钉 bundled 三事，本页钉 status valid/invalid 单句。看见 application considers valid or invalid，不是已经 Process REJECT consensus assume（455） interchangeable——455 钉 Usage/When assumes not valid bundled，本页钉 Response 表 status 语义单句。看见回了 status，不是已经 ProposalStatus（376） interchangeable——376 钉 UNKNOWN/ACCEPT/REJECT 枚举，本页钉 Response 表 status 单句。
2. **看见 REJECT assumes not valid prevote nil is not block invalid / 看见 REJECT 时共识 assumes not valid、会 prevote nil 不是已经当成块非法 不是已经 Process 回包栏 bundled（430） interchangeable / 已经当成块非法 interchangeable，也不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经永久标成非法块 interchangeable，也不是已经 VerifyVoteExtensionResponse.status is REJECT bundled（433） interchangeable / 已经 consensus rejects whole vote interchangeable / 已经验签拒收整张 Precommit interchangeable，也不是已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable / 已经 REJECT 是免费过滤 interchangeable。**  
   官方 ProcessProposal Response/Usage 写：若 `ProcessProposalResponse.status` 是 `REJECT`，共识假设收到的提案不合法，验证者会 prevote nil。看见 assumes not valid，不是已经当成块非法 interchangeable——430 bundled 常被写成「回了 REJECT 就已经块非法」，本页钉 assumes not valid not block invalid 单句。看见 prevote nil，不是已经 Verify 433 REJECT whole vote interchangeable——433 钉拒整张 Precommit，本页钉 Process prevote nil 单句。看见 not block invalid，不是已经 Process REJECT = prevote nil 不是免费过滤（33） interchangeable——33 钉四门 REJECT 不是免费过滤，本页钉 Response status REJECT 语义边界。
3. **看见 REJECT not can't execute candidate / MAY fully execute candidate state is not block invalid / 看见 REJECT 不是已经不能整块执行候选 不是已经 Process 回包栏 bundled（430） interchangeable / 已经不能整块执行候选 interchangeable / 已经当成块非法 interchangeable，也不是已经 ProcessProposal MAY fully execute bundled（452） interchangeable / 已经交差 interchangeable / 已经改了已提交状态 interchangeable，也不是已经 Process REJECT consensus assume bundled（455 第三件事） interchangeable / 已经不能 MAY 整块执行 interchangeable，也不是已经 status must exclusively depend bundled（534 余量） interchangeable / 已经和对任意块同一裁决 interchangeable。**  
   官方 ProcessProposal Usage 写：应用 MAY 像处理 Finalize 那样整块执行，但任何状态改动必须留作 candidate state。看见 MAY fully execute，不是已经 REJECT 就不能执行 interchangeable——430 bundled 常与 452 bundled 混成「回了 REJECT 就已经不能整块执行」，本页钉 REJECT not can't execute candidate 单句。看见 candidate state，不是已经 Process MAY fully execute（452） interchangeable——452 钉 MAY execute not committed，本页钉 Response REJECT 与 candidate 可并存单句。看见 not can't execute，不是已经 Process REJECT consensus assume（455） interchangeable——455 钉 REJECT 与 candidate 分开，本页钉 Response status REJECT 单句。

怎样做写 Process 回包栏、怎样整块执行候选 是规范里的做法，本页不抄。Process 回包栏 bundled（430）、Process REJECT consensus assume（455）、status must exclusively depend（534 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **status is valid/invalid judgment ≠ 已经当成块非法 interchangeable：** 官方把 Response status 语义和块非法分开。
- **REJECT assumes not valid not block invalid ≠ Verify REJECT whole vote interchangeable：** 官方把 Process prevote nil 和 Verify 拒整张票分开。
- **REJECT not can't execute candidate ≠ Process MAY execute already committed interchangeable：** 官方把 REJECT 与 MAY fully execute / candidate state 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| status valid/invalid | 不是 block invalid | 不是 Process REJECT consensus assume bundled（455） |
| REJECT assumes not valid | 不是 block invalid | 不是 Verify REJECT whole vote（433） |
| REJECT not can't execute candidate | 不是 can't execute | 不是 Process MAY execute committed（452） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Response status valid/invalid 正式三事，必须分开 status is valid/invalid 是不是已经 block invalid interchangeable / 已经 MUST Accept interchangeable、REJECT assumes not valid 是不是 block invalid interchangeable / 433 whole vote interchangeable、REJECT not can't execute candidate 是不是已经 can't execute interchangeable / 452 already committed interchangeable。可以跳过「看见回了 ProcessProposalResponse.status 就已经当成块非法 interchangeable」。不要另写怎样写 Process 回包栏。

## 本页不抄

- 怎样做写 Process 回包栏、怎样整块执行候选。
- ProcessProposalResponse.status must exclusively depend。那是不变量 534（430 item 2 余量）。
- 应用 SHOULD always set ACCEPT。那是不变量 530（456 item 1 / 430 Usage 余量）。
- Process REJECT consensus assume 正式三事 bundled。那是不变量 455。
