# 反模式：看见 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法就当成已经当成块非法 / 看见 VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态就当成已经可以像 ExtendVote 那样依赖其它值 / 看见应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价就当成已经正确进程交出的扩展必须 Accept

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**例**：[VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 ≠ 已经当成块非法](../../tracks/implementation/worked-example-verifyresp-vs-status.md)。

## 塌法

1. 看见 `VerifyVoteExtensionResponse.status` 是应用认为这份扩展合法还是非法 / 看见回了 `REJECT`，就当成已经当成块非法，或当成已经不能收这张 Precommit。
2. 看见 `VerifyVoteExtensionResponse.status` 必须只依赖 `VerifyVoteExtensionRequest` 和上一份已提交状态 / 看见回了 status，就当成已经可以像 ExtendVote 那样依赖其它值，或当成已经和对任意扩展同一裁决一回事。
3. 看见应用 SHOULD 总是设 `ACCEPT`，除非真的知道 REJECT 的活性代价 / 看见写了默认 Accept，就当成已经正确进程交出的扩展必须 Accept，或当成已经是 Req 6 已经测过。

## 为什么会出事

官方写：若 `VerifyVoteExtensionResponse.status` 是 `REJECT`，共识算法会拒掉整张收到的票。`VerifyVoteExtensionResponse.status` MUST exclusively depend on `VerifyVoteExtensionRequest` 和上一份已提交 Application state。应用实现者 SHOULD always set status to `ACCEPT`，除非真的知道 REJECT 的活性代价。看见回了 Verify 回包栏，不是已经当成块非法，也不是已经可以像 ExtendVote 那样依赖其它值，也不是已经正确进程交出的扩展必须 Accept。

## 和相邻反模式

- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张 Precommit 就已经是块非法，不是本页这种 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法不是已经当成块非法。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样，不是本页这种 VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态不是已经可以像 ExtendVote 那样依赖其它值。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept，不是本页这种应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经正确进程交出的扩展必须 Accept。
