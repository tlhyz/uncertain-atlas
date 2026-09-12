# 模式：把 Process 回包栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**例**：[ProcessProposalResponse.status 是应用认为这份提案合法还是非法 ≠ 已经当成块非法](../../tracks/implementation/worked-example-procresp-vs-status.md)。

## 三个名字

1. **ProcessProposalResponse.status 是应用认为这份提案合法还是非法不是已经当成块非法：** 看见回了 REJECT 不是已经不能整块执行候选。
2. **ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态不是已经可以像 Prepare 那样依赖其它值：** 看见回了 status 不是已经和对任意块同一裁决一回事。
3. **应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经 honest proposal 必须 Accept：** 看见写了默认 Accept 不是已经是 Req 3 已经测过。

## 为什么要分开叫

官方把 ProcessProposal Response 表上 `status` 是应用认为这份提案合法还是非法、必须只依赖请求和上一份已提交状态、SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价写成三件事。把它们叫成一个「看见回了 ProcessProposalResponse.status 就已经当成块非法」，会把已经当成块非法、已经可以像 Prepare 那样依赖其它值和已经 honest proposal 必须 Accept 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 ProcessProposalResponse.status 就已经当成块非法」，先数清问的是 ProcessProposalResponse.status 是应用认为这份提案合法还是非法不是已经当成块非法、ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态不是已经可以像 Prepare 那样依赖其它值，还是应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经 honest proposal 必须 Accept，再决定要不要同一次发布。
