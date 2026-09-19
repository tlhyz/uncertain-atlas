# 反模式：把 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量）说成已经清成默认 / 已经改过 / 已经和 InitChain 空回包同一句

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[没回 not already clear ≠ bundled（319）](../../tracks/implementation/worked-example-consensusparams-notclear-vs-bundled.md)。

## 卖法

把没回 / Finalize 没回 ConsensusParams / FinalizeBlock 回了空 写成已经清成默认 interchangeable / 已经 clear interchangeable / 已经清掉 interchangeable / 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable；把空着 / Finalize 空着 / 回包空 写成已经改过 interchangeable / 已经 changed interchangeable；把能更新 / Finalize 能更新参数 / 能回 ConsensusParams 写成已经和 InitChain 空回包同一句 interchangeable / 已经 InitChain-empty-same interchangeable，或已经和 319 consensusparams bundled / consensusparams-sold-as-updated interchangeable / 717 consensusparams-notclear interchangeable。

## 为什么错

官方把没回单句、already clear、already changed、already InitChain-empty-same 写成三件独立的实现事。把它们卖成 already clear interchangeable / already changed interchangeable / already InitChain-empty-same interchangeable，会把 not already clear、not already changed、not already InitChain-empty-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量），必须分开 not already clear、not already changed、not already InitChain-empty-same 三件事，不要和 319 / 33 / 716 / 718 / 35 糊成一句。

## 和相邻反模式

- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是 ConsensusParams vs update bundled 全段，不是本页 Finalize 没回 item 2 单句边界。
- [consensusparams-notempty-sold-as-bundled](consensusparams-notempty-sold-as-bundled.md) 是 InitChain 空参数 item 1，不是本页 Finalize nil 边界。
- [validatorupdate-notempty-sold-as-bundled](validatorupdate-notempty-sold-as-bundled.md) 是 InitChain 空验证者名单（318），不是本页 Finalize 参数边界。
