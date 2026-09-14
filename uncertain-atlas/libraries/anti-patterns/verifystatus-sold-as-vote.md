# 反模式：看见 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩就当成已经验过扩展 / 看见 VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票就当成已经当成块非法 / 看见 VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票就当成已经会发 Prevote nil

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**例**：[VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩 ≠ 已经验过扩展](../../tracks/implementation/worked-example-verifystatus-vs-vote.md)。

## 塌法

1. 看见 VerifyStatus 的 `UNKNOWN` 一律是错、引擎当应用坏了会崩 / 看见回了 `UNKNOWN`，就当成已经验过扩展，或当成已经扩展启用。
2. 看见 VerifyStatus 的 `ACCEPT` 表示应用认为扩展合法、共识会收下这张票 / 看见回了 `ACCEPT`，就当成已经当成块非法，或当成已经正确进程交出的扩展必须 Accept。
3. 看见 VerifyStatus 的 `REJECT` 表示应用认为扩展非法、共识会拒掉整张票 / 看见回了 `REJECT`，就当成已经会发 Prevote nil，或当成已经 ProcessProposalResponse.status 那种 REJECT。

## 为什么会出事

官方写：`VerifyStatus` 用在 `VerifyVoteExtension` 回包。`UNKNOWN` 表示应用出了问题，CometBFT 会当应用坏了并崩溃。`ACCEPT` 表示共识算法会收下这张票。`REJECT` 表示共识算法会拒掉整张票。看见回了 VerifyStatus，不是已经验过扩展，也不是已经当成块非法，也不是已经会发 Prevote nil。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus 那种 ACCEPT 会发 Prevote，不是本页这种 VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票不是已经当成块非法。
- [verifystatus-unknown-sold-as-bundled](verifystatus-unknown-sold-as-bundled.md) 是 UNKNOWN always wrong 单句专用；本页是 434 bundled 三事专用。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张 Precommit 就已经是块非法，不是本页这种 VerifyStatus 的 ACCEPT 不是已经当成块非法。
