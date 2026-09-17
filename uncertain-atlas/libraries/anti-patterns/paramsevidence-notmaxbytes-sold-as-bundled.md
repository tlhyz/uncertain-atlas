# 反模式：把 ConsensusParams.evidence not already evidence MaxBytes / not already unbonding / not already settled 正式三事（386 余量） 说成已经是证据 MaxBytes / 已经盖住解绑 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ConsensusParams.evidence ≠ bundled（386）](../../tracks/implementation/worked-example-paramsevidence-notmaxbytes-vs-bundled.md)。

## 卖法

把 ConsensusParams 余栏这句写成已经已经是证据 MaxBytes / 已经盖住解绑 / 已经交差 interchangeable，或已经和 386 paramsevidence-vs-maxbytes bundled / paramsevidence-notmaxbytes-sold-as-bundled interchangeable。

## 为什么错

官方把 ConsensusParams.evidence / abci / synchrony 三条核心句写成三件独立的实现事。把它们卖成已经是证据 MaxBytes / 已经盖住解绑 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.evidence 正式三事（386 余量），必须分开 not already evidence MaxBytes、not already unbonding、not already settled 三件事，不要和 386 / 331 / 385 / 771 / 772 糊成一句。

## 和相邻反模式

- [paramsevidence-sold-as-maxbytes](paramsevidence-sold-as-maxbytes.md) 是 ConsensusParams 余栏 bundled（386），不是本页 item 1 单句边界。
- [paramsblock-sold-as-maxbytes](paramsblock-sold-as-maxbytes.md) 是 ConsensusParams.block 就已经是 MaxBytes 上限（385），不是本页 evidence 边界。
