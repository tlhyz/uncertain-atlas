# 模式：把 PrepareProposal Usage no checks / crash / nondet 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[no checks / crash / nondet ≠ bundled](../../tracks/implementation/worked-example-prepareusage-nochecks-vs-bundled.md)。

## 三个名字

1. **no additional validity checks 不是已经验过重复：** 看见 Methods PrepareProposal Usage does NOT provide additional validity checks，不是 357 Prepare 回包校验 bundled interchangeable。
2. **crash on invalid response 不是 Process REJECT：** 看见 fails to validate PrepareProposalResponse → crash，不是 455 Process REJECT / 347 Req 3 Accept interchangeable。
3. **MAY be non-deterministic 不是必须确定：** 看见 PrepareProposal MAY be non-deterministic，不是 430 Process MUST deterministic interchangeable。

## 为什么要分开叫

官方把 no checks、crash on invalid response、MAY nondet、Prepare 回包校验 bundled（357）、Prepare 没有确定性要求 bundled（338）写成三个名字。把它们叫成一个「看见回了 Prepare 回包就已经验过重复、已经是 Process REJECT、已经必须确定 interchangeable」，会把 no checks、crash、MAY nondet 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事，先数清问的是 no additional validity checks 是不是已经验过重复 interchangeable、crash 是不是 Process REJECT interchangeable、MAY nondet 是不是必须确定 interchangeable，再决定要不要同一次发布。
