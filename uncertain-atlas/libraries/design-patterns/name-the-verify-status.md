# 模式：把 VerifyStatus 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**例**：[VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩 ≠ 已经验过扩展](../../tracks/implementation/worked-example-verifystatus-vs-vote.md)。

## 三个名字

1. **VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经验过扩展：** 看见回了 UNKNOWN 不是已经扩展启用。
2. **VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票不是已经当成块非法：** 看见回了 ACCEPT 不是已经正确进程交出的扩展必须 Accept。
3. **VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票不是已经会发 Prevote nil：** 看见回了 REJECT 不是已经 ProcessProposalResponse.status 那种 REJECT。

## 为什么要分开叫

官方把 VerifyStatus 的 UNKNOWN 一律是错、ACCEPT 会收下这张票、REJECT 会拒掉整张票写成三件事。把它们叫成一个「看见回了 VerifyStatus 就已经验过扩展」，会把已经验过扩展、已经当成块非法和已经会发 Prevote nil 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 VerifyStatus 就已经验过扩展」，先数清问的是 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经验过扩展、VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票不是已经当成块非法，还是 VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票不是已经会发 Prevote nil，再决定要不要同一次发布。
