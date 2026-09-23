# 模式：把通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[通常紧跟 Prepare、列表对得上 not already guaranteed-this ≠ bundled（351）](../../tracks/implementation/worked-example-process-notguaranteed-vs-bundled.md)。

## 三个名字

1. **通常紧跟 Prepare、列表对得上 不是 already guaranteed-this：** 看见通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` / 通常对得上 / 列表对得上，不是已经保证是这一次 Prepare 的回包 interchangeable / 已经 guaranteed-this interchangeable / 已经保证这一次交差 interchangeable，不是 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable。

2. **txs 一样 不是 already must-match：** 看见 txs 一样 / 请求 txs 等于回包 txs / 列表字节一样，不是已经必须一样 interchangeable / 已经 must-match interchangeable / 已经必须对上交差 interchangeable，不是 33 fourgates interchangeable / 347 req3coherence interchangeable。

3. **刚 Prepare 完 不是 already same-call：** 看见刚 Prepare 完 / 刚回了 Prepare / 紧跟 Prepare，不是已经是同一份调用 interchangeable / 已经 same-call interchangeable / 已经同一调用交差 interchangeable，不是 806 process-notskip interchangeable / 808 process-notalways interchangeable。

官方把通常紧跟 Prepare、列表对得上、不是已经必须一样、不是已经是同一份调用写成三个名字。把它们叫成一个「看见通常对得上就已经保证是这一次 interchangeable / 就已经必须一样 interchangeable / 就已经是同一份调用 interchangeable」，会把 not already guaranteed-this、not already must-match、not already same-call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量），先数清问的是通常紧跟 Prepare、列表对得上 是不是 already guaranteed-this / 351 / processalso-sold-as-matched，是不是 txs 一样 是不是 already must-match，还是刚 Prepare 完 是不是 already same-call，再决定要不要同一次发布。351 processalso vs prepare bundled unbundling 在本页 item 2 续。
