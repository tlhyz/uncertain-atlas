# 模式：把 PrepareProposal When suggested validate like Verify 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**例**：[suggested validate like Verify ≠ bundled](../../tracks/implementation/worked-example-preparewhen-suggestvalidate-vs-bundled.md)。

## 三个名字

1. **it is suggested 不是 MUST / 不是 Req 6 Accept：** 看见 suggested，不是 348 Req 6 must Accept interchangeable / 516 Application returns ACCEPT interchangeable / 352 第二件事 bundled interchangeable。
2. **same manner as VerifyVoteExtension 不是 step 2 call：** 看见 same manner as Verify，不是 515 step 2 call interchangeable / 435 Verify When bundled interchangeable / 433 MUST deterministic interchangeable。
3. **not engine re-Verify 不是已经 Verify 过：** 看见 suggested validate is not CometBFT calling VerifyVoteExtension again，不是 352 第二件事 bundled interchangeable / 519 +2/3 not verified interchangeable / 518 MAY add without Verify interchangeable。

## 为什么要分开叫

官方把 suggested、same manner as Verify、not engine re-Verify、迟到扩展 bundled（352 第二件事）、Verify When step 2 call（515）、+2/3 not verified（519）写成三个名字。把它们叫成一个「看见建议按 Verify 同款逻辑再看一遍就已经是引擎会再 Verify interchangeable、已经 Accept interchangeable」，会把 suggested、应用自验、引擎再 call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When suggested validate like Verify 正式三事，先数清问的是 it is suggested 是不是 MUST / Accept、suggested validate 是不是 step 2 call、not engine re-Verify 是不是已经 Verify 过，再决定要不要同一次发布。
