# 例：看见 ProcessProposalResponse.status 是应用认为这份提案合法还是非法不是已经当成块非法；看见 ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态不是已经可以像 Prepare 那样依赖其它值；看见应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经 honest proposal 必须 Accept

**层次**：实现 / Process 回包栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalResponse.status 是应用认为这份提案合法还是非法不是已经当成块非法 / ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态不是已经可以像 Prepare 那样依赖其它值 / 应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经 honest proposal 必须 Accept」，不是 ProposalStatus 那种 UNKNOWN/ACCEPT/REJECT 枚举语义，也不是 Process 必须只依赖请求和上一份状态那种对任意块同一裁决。不要另写怎样写 Process 回包栏。

## 官方三件事

规范把 ProcessProposal Response 表上 `status` 是应用认为这份提案合法还是非法、必须只依赖请求和上一份已提交状态、SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价写成三件独立的实现事，不是「看见回了 ProcessProposalResponse.status 就已经当成块非法、已经可以像 Prepare 那样依赖其它值、已经 honest proposal 必须 Accept」一件事：

1. **看见 `ProcessProposalResponse.status` 是应用认为这份提案合法还是非法 / 看见回了 `REJECT` 不是已经当成块非法，也不是已经不能整块执行候选。**  
   官方写：若 `ProcessProposalResponse.status` 是 `REJECT`，共识假设收到的提案不合法，验证者会 prevote nil。Usage 也写：应用 MAY 像处理 Finalize 那样整块执行，但任何状态改动必须留作候选，并准备另一块被决定时丢掉。看见回了 `REJECT`，不是已经 ProposalStatus 那种 `REJECT` 表示提案非法、共识会发 Prevote nil 就已经不能稍后改裁决。看见共识假设不合法，不是已经不能整块执行候选。看见会 prevote nil，不是已经当成块非法。
2. **看见 `ProcessProposalResponse.status` 必须只依赖 `ProcessProposalRequest` 和上一份已提交状态 / 看见回了 status 不是已经可以像 Prepare 那样依赖其它值，也不是已经和对任意块同一裁决一回事。**  
   官方写：`ProcessProposal` 的实现 MUST 确定。`ProcessProposalResponse.status` MUST **exclusively** depend on `ProcessProposalRequest` 里的参数，以及上一份已提交的 Application state。看见回了 status，不是已经 Prepare 没有确定性要求那种可以依赖其它值。看见必须只依赖请求和上一份状态，不是已经 Process 必须只依赖请求和上一份状态那种对任意块同一裁决就已经是 status 必须只依赖。看见有确定要求，不是已经和对诚实提案同一裁决一回事。
3. **看见应用 SHOULD 总是设 `ACCEPT`，除非真的知道 REJECT 的活性代价 / 看见写了默认 Accept 不是已经 honest proposal 必须 Accept，也不是已经是 Req 3 已经测过。**  
   官方写：应用实现者 SHOULD always set `ProcessProposalResponse.status` to `ACCEPT`，除非他们 _really_ know what the potential liveness implications of returning `REJECT` are。看见 SHOULD 总是 Accept，不是已经正确提议者的准备提案必须被正确接收者 Accept 那种 honest proposal 必须 Accept。看见除非真的知道活性代价，不是已经 Requirement 3 是大量测试和自动验证的目标那种已经测过。看见写了默认 Accept，不是已经四门默认 Accept 那种已经结算。

怎样写 Process 回包栏、怎样挑 ACCEPT/REJECT、怎样整块执行候选是规范里的做法，本页不抄。ProposalStatus 那种 UNKNOWN/ACCEPT/REJECT 枚举语义是不变量 376，本页不抄。

## 官方为什么这样拆

- **ProcessProposalResponse.status 是应用认为这份提案合法还是非法 ≠ 已经当成块非法：** 官方把 prevote nil 和整块执行候选、状态留作候选分开。
- **ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态 ≠ 已经可以像 Prepare 那样依赖其它值：** 官方把 status 的 exclusive dependence 和 Prepare 没有确定性要求分开。
- **应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价 ≠ 已经 honest proposal 必须 Accept：** 官方把 SHOULD Accept 和 Requirement 3 必须 Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalResponse.status 是应用认为这份提案合法还是非法 | 不是已经当成块非法 | 不是 REJECT 表示提案非法、共识会发 Prevote nil 就已经不能稍后改裁决（376） |
| ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态 | 不是已经可以像 Prepare 那样依赖其它值 | 不是 Prepare 没有确定性要求就已经可以像 Prepare 那样（338） |
| 应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价 | 不是已经 honest proposal 必须 Accept | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 ProcessProposalResponse.status 就已经当成块非法、已经可以像 Prepare 那样依赖其它值、已经 honest proposal 必须 Accept」，必须分开 ProcessProposalResponse.status 是应用认为这份提案合法还是非法是不是已经当成块非法、ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态是不是已经可以像 Prepare 那样依赖其它值、应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价是不是已经 honest proposal 必须 Accept。可以跳过「看见回了 ProcessProposalResponse.status 就已经当成块非法」。不要另写怎样写 Process 回包栏。430 procresp vs status bundled unbundling 完成（1067 item 1 / 1068 item 2 / 1069 item 3）；精读 [`worked-example-presp-notinvalid-vs-bundled.md`](worked-example-presp-notinvalid-vs-bundled.md)（不变量 1067 item 1）。

## 本页不抄

- 怎样写 Process 回包栏、怎样挑 ACCEPT/REJECT、怎样整块执行候选。
- ProposalStatus 那种 UNKNOWN/ACCEPT/REJECT 枚举语义。那是不变量 376。
- Prepare 没有确定性要求就已经可以像 Prepare 那样。那是不变量 338。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
