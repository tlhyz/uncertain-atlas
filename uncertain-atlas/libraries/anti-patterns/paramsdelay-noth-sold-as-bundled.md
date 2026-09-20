# 反模式：把本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量）说成已经在本高生效 / 已经本高提议按新参数 / 已经和本高交差同一句

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[本高回了 not already in-effect-at-h ≠ bundled（333）](../../tracks/implementation/worked-example-paramsdelay-noth-vs-bundled.md)。

## 卖法

把本高 FinalizeBlock 回了 ConsensusParams / 本高回了参数 / 回了 ConsensusParams 写成已经在本高生效 interchangeable / 已经 in-effect-at-h interchangeable / 已经本高用上交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable；把本高 Finalize 绿了 / 本高已经交差 / 本高 Finalize 过了 写成已经本高提议按新参数 interchangeable / 已经 prepare-new-at-h interchangeable；把能更新 / 本高能回参数 / 参数更新口开了 写成已经和本高交差同一句 interchangeable / 已经 tied-to-finalize interchangeable，或已经和 333 paramsdelay bundled / paramsdelay-sold-as-validatordelay interchangeable / 755 paramsdelay-noth interchangeable。

## 为什么错

官方把本高回了参数单句、already in-effect-at-h、already prepare-new-at-h、already tied-to-finalize 写成三件独立的实现事。把它们卖成 already in-effect-at-h interchangeable / already prepare-new-at-h interchangeable / already tied-to-finalize interchangeable，会把 not already in-effect-at-h、not already prepare-new-at-h、not already tied-to-finalize 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量），必须分开 not already in-effect-at-h、not already prepare-new-at-h、not already tied-to-finalize 三件事，不要和 333 / 33 / 319 / 35 / 330 / 756 / 757 糊成一句。

## 和相邻反模式

- [paramsdelay-sold-as-validatordelay](paramsdelay-sold-as-validatordelay.md) 是 ConsensusParams 生效延迟 bundled 全段，不是本页本高回了 item 1 单句边界。
- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是 InitChain 空 / Finalize 没回 / 只填一项（319），不是本页本高生效边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 已经 Prepare 带了扩展（330），不是本页本高回了参数边界。
