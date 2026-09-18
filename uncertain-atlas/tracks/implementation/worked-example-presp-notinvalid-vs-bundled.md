# 例：看见 ProcessProposalResponse.status is not already block-invalid interchangeable / not already no-exec interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量）/ not 1067 presp-notinvalid interchangeable / not 430 procresp-vs-status bundled interchangeable」，不是 Process 回包栏 bundled（430），也不是 ProposalStatus REJECT 就已经不能稍后改裁决（376），也不是 REJECT 就已经不能整块执行候选。不要另写怎样写 Process 回包栏。

## 官方三件事

1. **看见 ProcessProposalResponse.status 是应用认为这份提案合法还是非法 / 看见回了 REJECT 这份栏 is not already 已经当成块非法 interchangeable，也不是已经 Process 回包栏 bundled（430） interchangeable / 1067 presp-notinvalid interchangeable / 1068 presp-notprep interchangeable / 430 procresp item 2 exclusive interchangeable，也不是已经 ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事 bundled（430 item 1 余量） interchangeable / 430 procresp item 1 interchangeable。**  
   官方写：若 ProcessProposalResponse.status 是 REJECT，共识假设收到的提案不合法，验证者会 prevote nil。看见回了 REJECT，不是已经当成块非法 interchangeable——本页从 430 item 1 侧钉 not already block-invalid 单句。430 procresp vs status bundled unbundling 在本页 item 1 启动。

2. **看见共识假设不合法 / 看见回了 REJECT / 这份栏 is not already 已经不能整块执行候选 interchangeable，也不是已经 Process 回包栏 bundled（430） interchangeable / 1067 presp-notinvalid interchangeable / 430 procresp item 3 should-accept interchangeable / 1069 presp-nothonest interchangeable，也不是已经 ProposalStatus REJECT 就已经不能稍后改裁决 interchangeable / 376 proposalstatus interchangeable。**  
   官方把共识假设不合法和已经不能整块执行候选分开。看见共识假设不合法，不是已经不能整块执行候选 interchangeable。本页钉 not already no-exec 单句。

3. **看见会 prevote nil / 看见回了 REJECT / 这份栏 is not already 已经当成块非法 interchangeable，也不是已经 Process 回包栏 bundled（430） interchangeable / 1067 presp-notinvalid interchangeable / 1068 presp-notprep interchangeable，也不是已经 REJECT 就已经不能稍后改裁决 interchangeable / 376 proposalstatus interchangeable。**  
   官方把会 prevote nil 和已经当成块非法分开。看见会 prevote nil，不是已经当成块非法 interchangeable。430 procresp vs status bundled unbundling 在本页 item 1 启动。

怎样写 Process 回包栏、怎样挑 ACCEPT/REJECT、怎样整块执行候选是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalResponse.status not already block-invalid ≠ 已经当成块非法 interchangeable：** 官方把应用认为非法和已经当成块非法分开。
- **看见共识假设不合法 not already no-exec ≠ 已经不能整块执行候选 interchangeable：** 官方把共识假设不合法和已经不能整块执行候选分开。
- **看见会 prevote nil not already settled ≠ 已经当成块非法 interchangeable：** 官方把会 prevote nil 和已经当成块非法分开；430 procresp vs status bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalResponse.status 是应用认为这份提案合法还是非法 | 不是已经当成块非法 | 不是 REJECT 就已经不能稍后改裁决（376） |
| 看见共识假设不合法 | 不是已经不能整块执行候选 | 不是 Process 必须只依赖请求和上一份状态那种对任意块同一裁决（340） |
| 看见会 prevote nil | 不是已经当成块非法 | 不是 exclusive dependence 就已经可以像 Prepare 那样（1068） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量），必须分开是不是已经当成块非法、是不是已经不能整块执行候选、是不是已经当成块非法交差。可以跳过「看见回了 ProcessProposalResponse.status 就已经当成块非法」。不要另写怎样写 Process 回包栏。430 procresp vs status bundled unbundling 在本页 item 1 启动；续 [`worked-example-presp-notprep-vs-bundled.md`](worked-example-presp-notprep-vs-bundled.md)（不变量 1068 item 2）。

## 本页不抄

- 怎样写 Process 回包栏、怎样挑 ACCEPT/REJECT、怎样整块执行候选。
- Process 回包栏 bundled。那是不变量 430。
- ProposalStatus REJECT 就已经不能稍后改裁决。那是不变量 376。
- Process 必须只依赖请求和上一份状态那种对任意块同一裁决。那是不变量 340。
