# 模式：把 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[没回 not already clear ≠ bundled（319）](../../tracks/implementation/worked-example-consensusparams-notclear-vs-bundled.md)。

## 三个名字

1. **没回 不是 already clear：** 看见 Finalize 没回 ConsensusParams / FinalizeBlock 回了空，不是已经清成默认 interchangeable / 已经清掉 interchangeable，不是 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable。

2. **空着 不是 already changed：** 看见 Finalize 空着 / 回包空，不是已经改过 interchangeable / 已经改了参数 interchangeable，不是 319 consensusparams item 1 interchangeable / 716 consensusparams-notempty interchangeable。

3. **能更新 不是 already InitChain-empty-same：** 看见 Finalize 能更新参数 / 能回 ConsensusParams，不是已经和 InitChain 空回包同一句 interchangeable / 已经和 InitChain nil 同一路径 interchangeable，不是 319 consensusparams item 3 interchangeable / 718 consensusparams-notpartial interchangeable。

官方把没回单句、already clear、already changed、already InitChain-empty-same 写成三个名字。把它们叫成一个「看见没回就已经清成默认 interchangeable / 就已经改过 interchangeable / 就已经和 InitChain 空回包同一句 interchangeable」，会把 not already clear、not already changed、not already InitChain-empty-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量），先数清问的是没回 是不是 already clear / 319 / consensusparams-sold-as-updated，是不是空着 是不是 already changed，还是能更新 是不是 already InitChain-empty-same，再决定要不要同一次发布。319 consensusparams vs update bundled unbundling 在本页 item 2 完成。
