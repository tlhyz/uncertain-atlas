# 例：看见 ProcessProposalResponse.status exclusive dependence is not already prepare-nondet interchangeable / not already same-ruling interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事（430 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事（430 余量）/ not 1068 presp-notprep interchangeable / not 430 procresp-vs-status bundled interchangeable」，不是 Process 回包栏 bundled（430），也不是 Prepare 没有确定性要求就已经可以像 Prepare 那样（338），也不是 Process 必须只依赖请求和上一份状态那种对任意块同一裁决（340）。不要另写怎样写 Process 回包栏。

## 官方三件事

1. **看见 ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态 / 看见回了 status 这份栏 is not already 已经可以像 Prepare 那样依赖其它值 interchangeable，也不是已经 Process 回包栏 bundled（430） interchangeable / 1068 presp-notprep interchangeable / 1067 presp-notinvalid interchangeable / 430 procresp item 1 status interchangeable，也不是已经 ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事 bundled（430 item 2 余量） interchangeable / 430 procresp item 2 interchangeable。**  
   官方写：ProcessProposal 的实现 MUST 确定。ProcessProposalResponse.status MUST exclusively depend on ProcessProposalRequest 里的参数，以及上一份已提交的 Application state。看见回了 status，不是已经可以像 Prepare 那样依赖其它值 interchangeable——本页从 430 item 2 侧钉 not already prepare-nondet 单句。430 procresp vs status bundled unbundling 在本页 item 2 续。

2. **看见必须只依赖请求和上一份状态 / 看见回了 status / 这份栏 is not already 已经和对任意块同一裁决一回事 interchangeable，也不是已经 Process 回包栏 bundled（430） interchangeable / 1068 presp-notprep interchangeable / 430 procresp item 3 should-accept interchangeable / 1069 presp-nothonest interchangeable，也不是已经 Prepare 没有确定性要求就已经可以像 Prepare 那样 interchangeable / 338 prepare-nondet interchangeable。**  
   官方把必须只依赖请求和上一份状态和已经和对任意块同一裁决一回事分开。看见必须只依赖，不是已经和对任意块同一裁决一回事 interchangeable。本页钉 not already same-ruling 单句。

3. **看见有确定要求 / 看见回了 status / 这份栏 is not already 已经和对诚实提案同一裁决一回事 interchangeable，也不是已经 Process 回包栏 bundled（430） interchangeable / 1068 presp-notprep interchangeable / 1067 presp-notinvalid interchangeable，也不是已经 Process 必须只依赖请求和上一份状态那种对任意块同一裁决 interchangeable / 340 process-det interchangeable。**  
   官方把有确定要求和已经和对诚实提案同一裁决一回事分开。看见有确定要求，不是已经和对诚实提案同一裁决一回事 interchangeable。430 procresp vs status bundled unbundling 在本页 item 2 续。

怎样写 Process 回包栏、怎样挑 ACCEPT/REJECT、怎样整块执行候选是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalResponse.status exclusive dependence not already prepare-nondet ≠ 已经可以像 Prepare 那样依赖其它值 interchangeable：** 官方把 status 的 exclusive dependence 和 Prepare 没有确定性要求分开。
- **看见必须只依赖请求和上一份状态 not already same-ruling ≠ 已经和对任意块同一裁决一回事 interchangeable：** 官方把 exclusive dependence 和已经和对任意块同一裁决一回事分开。
- **看见有确定要求 not already settled ≠ 已经和对诚实提案同一裁决一回事 interchangeable：** 官方把有确定要求和已经和对诚实提案同一裁决一回事分开；430 procresp vs status bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态 | 不是已经可以像 Prepare 那样依赖其它值 | 不是 Prepare 没有确定性要求就已经可以像 Prepare 那样（338） |
| 看见必须只依赖请求和上一份状态 | 不是已经和对任意块同一裁决一回事 | 不是 Process 必须只依赖请求和上一份状态那种对任意块同一裁决（340） |
| 看见有确定要求 | 不是已经和对诚实提案同一裁决一回事 | 不是 SHOULD Accept 就已经 honest proposal 必须 Accept（1069） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事（430 余量），必须分开是不是已经可以像 Prepare 那样依赖其它值、是不是已经和对任意块同一裁决一回事、是不是已经和对诚实提案同一裁决一回事。可以跳过「看见回了 ProcessProposalResponse.status 就已经当成块非法」。不要另写怎样写 Process 回包栏。430 procresp vs status bundled unbundling 在本页 item 2 续；续 [`worked-example-presp-nothonest-vs-bundled.md`](worked-example-presp-nothonest-vs-bundled.md)（不变量 1069 item 3）。

## 本页不抄

- 怎样写 Process 回包栏、怎样挑 ACCEPT/REJECT、怎样整块执行候选。
- Process 回包栏 bundled。那是不变量 430。
- Prepare 没有确定性要求就已经可以像 Prepare 那样。那是不变量 338。
- Process 必须只依赖请求和上一份状态那种对任意块同一裁决。那是不变量 340。
