# 模式：把本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[本高回了 not already in-effect-at-h ≠ bundled（333）](../../tracks/implementation/worked-example-paramsdelay-noth-vs-bundled.md)。

## 三个名字

1. **本高回了参数 不是 already in-effect-at-h：** 看见本高 FinalizeBlock 回了 ConsensusParams / 本高回了参数 / 回了 ConsensusParams，不是已经在本高生效 interchangeable / 已经本高用上交差 interchangeable，不是 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable。

2. **本高 Finalize 绿了 不是 already prepare-new-at-h：** 看见本高 Finalize 绿了 / 本高已经交差 / 本高 Finalize 过了，不是已经本高提议按新参数 interchangeable / 已经本高 Prepare 按新上限交差 interchangeable，不是 319 consensusparams interchangeable / 333 paramsdelay item 2 interchangeable。

3. **能更新 不是 already tied-to-finalize：** 看见能更新 / 本高能回参数 / 参数更新口开了，不是已经和本高交差同一句 interchangeable / 已经本高交差同一句交差 interchangeable，不是 33 four gates interchangeable / 333 paramsdelay item 3 interchangeable。

官方把本高回了参数单句、already in-effect-at-h、already prepare-new-at-h、already tied-to-finalize 写成三个名字。把它们叫成一个「看见本高回了就已经在本高生效 interchangeable / 就已经本高提议按新参数 interchangeable / 就已经和本高交差同一句 interchangeable」，会把 not already in-effect-at-h、not already prepare-new-at-h、not already tied-to-finalize 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量），先数清问的是本高回了参数 是不是 already in-effect-at-h / 333 / paramsdelay-sold-as-validatordelay，是不是本高 Finalize 绿了 是不是 already prepare-new-at-h，还是能更新 是不是 already tied-to-finalize，再决定要不要同一次发布。333 paramsdelay vs set bundled unbundling 在本页 item 1 启动。
