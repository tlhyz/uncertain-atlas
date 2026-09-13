# 例：看见 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法不是已经当成块非法；看见 VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态不是已经可以像 ExtendVote 那样依赖其它值；看见应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经正确进程交出的扩展必须 Accept

**层次**：实现 / Verify 回包栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法不是已经当成块非法 / VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态不是已经可以像 ExtendVote 那样依赖其它值 / 应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价不是已经正确进程交出的扩展必须 Accept」，不是验签拒收整张 Precommit 就已经是块非法，也不是 Verify 必须只依赖扩展、这块和上一份状态那种对任意扩展同一裁决。不要另写怎样写 Verify 回包栏。

## 官方三件事

规范把 VerifyVoteExtension Response 表上 `status` 是应用认为这份扩展合法还是非法、必须只依赖请求和上一份已提交状态、SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价写成三件独立的实现事，不是「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法、已经可以像 ExtendVote 那样依赖其它值、已经正确进程交出的扩展必须 Accept」一件事：

1. **看见 `VerifyVoteExtensionResponse.status` 是应用认为这份扩展合法还是非法 / 看见回了 `REJECT` 不是已经当成块非法，也不是已经不能收这张 Precommit。**  
   官方写：若 `VerifyVoteExtensionResponse.status` 是 `REJECT`，共识算法会拒掉整张收到的票。Usage 也写：*p* 会把这张 Precommit 当非法丢掉。看见回了 `REJECT`，不是已经验签拒收整张 Precommit 就已经是块非法那种已经当成块非法。看见拒掉整张票，不是已经 ProcessProposalResponse.status 那种 REJECT 会让验证者 prevote nil。看见 Precommit 被丢掉，不是已经不能收这张 Precommit。
2. **看见 `VerifyVoteExtensionResponse.status` 必须只依赖 `VerifyVoteExtensionRequest` 和上一份已提交状态 / 看见回了 status 不是已经可以像 ExtendVote 那样依赖其它值，也不是已经和对任意扩展同一裁决一回事。**  
   官方写：`VerifyVoteExtension` 的实现 MUST 确定。`VerifyVoteExtensionResponse.status` MUST **exclusively** depend on `VerifyVoteExtensionRequest` 里的参数，以及上一份已提交的 Application state。看见回了 status，不是已经 ExtendVote 没有确定性要求那种可以依赖其它值。看见必须只依赖请求和上一份状态，不是已经 Verify 必须只依赖扩展、这块和上一份状态那种对任意扩展同一裁决就已经是 status 必须只依赖。看见有确定要求，不是已经和 ExtendVote 同一把尺。
3. **看见应用 SHOULD 总是设 `ACCEPT`，除非真的知道 REJECT 的活性代价 / 看见写了默认 Accept 不是已经正确进程交出的扩展必须 Accept，也不是已经是 Req 6 已经测过。**  
   官方写：应用实现者 SHOULD always set `VerifyVoteExtensionResponse.status` to `ACCEPT`，除非他们 _really_ know what the potential liveness implications of returning `REJECT` are。看见 SHOULD 总是 Accept，不是已经正确进程交出的扩展、正确接收者 Verify 必须 Accept 那种必须 Accept。看见除非真的知道活性代价，不是已经 Requirement 6 是大量测试和自动验证的目标那种已经测过。看见写了默认 Accept，不是已经 Verify 默认 Accept 那种已经验过扩展。

怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit 是规范里的做法，本页不抄。验签拒收整张 Precommit 就已经是块非法是不变量 34，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 ≠ 已经当成块非法：** 官方把拒整张 Precommit 和 Process 的 prevote nil、块非法分开。
- **VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态 ≠ 已经可以像 ExtendVote 那样依赖其它值：** 官方把 status 的 exclusive dependence 和 ExtendVote 没有确定性要求分开。
- **应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价 ≠ 已经正确进程交出的扩展必须 Accept：** 官方把 SHOULD Accept 和 Requirement 6 必须 Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 | 不是已经当成块非法 | 不是验签拒收整张 Precommit 就已经是块非法（34） |
| VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态 | 不是已经可以像 ExtendVote 那样依赖其它值 | 不是 ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样（338） |
| 应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价 | 不是已经正确进程交出的扩展必须 Accept | 不是正确进程交出的扩展必须被正确接收者 Verify Accept（348） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法、已经可以像 ExtendVote 那样依赖其它值、已经正确进程交出的扩展必须 Accept」，必须分开 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法是不是已经当成块非法、VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态是不是已经可以像 ExtendVote 那样依赖其它值、应用 SHOULD 总是设 ACCEPT 除非真的知道 REJECT 的活性代价是不是已经正确进程交出的扩展必须 Accept。可以跳过「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法」。不要另写怎样写 Verify 回包栏。

## 本页不抄

- 怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit。
- 验签拒收整张 Precommit 就已经是块非法。那是不变量 34。
- ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样。那是不变量 338。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
