# 反模式：看见 ProcessProposalResponse.status 是应用认为这份提案合法还是非法就当成已经当成块非法 / 看见 ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态就当成已经可以像 Prepare 那样依赖其它值 / 看见应用 SHOULD 总是设 ACCEPT 就当成已经 honest proposal 必须 Accept

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**例**：[ProcessProposalResponse.status 是应用认为这份提案合法还是非法 ≠ 已经当成块非法](../../tracks/implementation/worked-example-procresp-vs-status.md)。

## 塌法

1. 看见 `ProcessProposalResponse.status` 是应用认为这份提案合法还是非法 / 看见回了 `REJECT`，就当成已经当成块非法，或当成已经不能整块执行候选。
2. 看见 `ProcessProposalResponse.status` 必须只依赖 `ProcessProposalRequest` 和上一份已提交状态 / 看见回了 status，就当成已经可以像 Prepare 那样依赖其它值，或当成已经和对任意块同一裁决一回事。
3. 看见应用 SHOULD 总是设 `ACCEPT` 除非真的知道 REJECT 的活性代价 / 看见写了默认 Accept，就当成已经 honest proposal 必须 Accept，或当成已经是 Req 3 已经测过。

## 为什么会出事

官方写：若 `ProcessProposalResponse.status` 是 `REJECT`，共识假设收到的提案不合法。`ProcessProposalResponse.status` MUST exclusively depend on `ProcessProposalRequest` 和上一份已提交 Application state。应用实现者 SHOULD always set `ProcessProposalResponse.status` to `ACCEPT`，除非他们 really know what the potential liveness implications of returning `REJECT` are。看见回了 status，不是已经当成块非法，也不是已经可以像 Prepare 那样依赖其它值，也不是已经 honest proposal 必须 Accept。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus 那种 UNKNOWN/ACCEPT/REJECT 就已经是四门已经结算，不是本页这种 ProcessProposalResponse.status 是应用认为这份提案合法还是非法不是已经当成块非法。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求就已经可以像 Prepare 那样，不是本页这种 ProcessProposalResponse.status 必须只依赖 ProcessProposalRequest 和上一份已提交状态不是已经可以像 Prepare 那样依赖其它值。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept 就已经 honest proposal 必须 Accept，不是本页这种应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经 honest proposal 必须 Accept。
